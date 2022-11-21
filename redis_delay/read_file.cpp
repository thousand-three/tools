#include <fstream>
#include <sstream>
#include <iostream>
#include <time.h>
#include "RedisPackage.h"
#include "common.h"

void TestSingleData();
void TestManyData();
int main()
{
    TestSingleData();
    //TestManyData();
    return 0;
}

void TestSingleData()
{
    std::fstream file("/home/risk/redis_delay/OnRtnRiskSyncAccount_20221118.txt",std::ios::in);
    RedisPackage* redis = new RedisPackage();
    std::string data_str,mid_temp,redis_key;
    int cnt = 0;
    double start_time,end_time;
    if(file.is_open())
    {
        redis->ConnectRedis(redis_ip,redis_port,redis_pd,redis_db);
        start_time = clock();
        while(getline(file,data_str))
        {
            std::istringstream ss(data_str);
            int split_cnt = 0;
            while(getline(ss,mid_temp,'\t'))
            {
                split_cnt++;
                if(split_cnt == 4)
                {
                    redis_key = mid_temp;
                    break;
                }
            }
            cnt++;
            redis->RedisSetData(redis_key,data_str);
            if(cnt%10000==0)
            {
                std::cout << "push over data: "<<cnt/10000<<"万条"<<std::endl;
            }
        }
        end_time = clock();
        std::cout<<cnt<<std::endl;
        std::cout<<(end_time-start_time)/CLOCKS_PER_SEC<<std::endl;
    }
    else
    {
        std::cout<<"file open fail"<<std::endl;
    }
}

void TestManyData()
{
    std::fstream file("/home/risk/redis_delay/OnRtnRiskSyncAccount_20221118.txt",std::ios::in);
    RedisPackage* redis = new RedisPackage();
    std::string data_str,mid_temp,redis_key;
    std::vector<std::string> pipeline_cmd;
    int cnt = 0;
    double start_time,end_time;
    if(file.is_open())
    {
        redis->ConnectRedis(redis_ip,redis_port,redis_pd,redis_db);
        start_time = clock();
        while(getline(file,data_str))
        {
            std::istringstream ss(data_str);
            int split_cnt = 0;
            while(getline(ss,mid_temp,'\t'))
            {
                split_cnt++;
                if(split_cnt == 4)
                {
                    redis_key = mid_temp;
                    pipeline_cmd.push_back("set " + redis_key + " " + data_str);
                    break;
                }
            }
            cnt++;
            if(cnt%10000==0)
            {
                redis->RedisSeManytData(pipeline_cmd);
                std::cout << "push over data: "<<cnt/10000<<"万条"<<std::endl;
                pipeline_cmd.clear();
            }
        }
        redis->RedisSeManytData(pipeline_cmd);
        end_time = clock();
        std::cout<<cnt<<std::endl;
        std::cout<<(end_time-start_time)/CLOCKS_PER_SEC<<std::endl;
    }
    else
    {
        std::cout<<"file open fail"<<std::endl;
    }    

}