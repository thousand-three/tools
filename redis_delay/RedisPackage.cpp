#include "RedisPackage.h"
#include "common.h"
#include <iostream>


bool RedisPackage::ConnectRedis(std::string redis_ip,int redis_port,std::string redis_pd,std::string redis_db)
{
    this->redis_context = redisConnect(redis_ip.c_str(),redis_port);
    if(this->redis_context != NULL && this->redis_context->err != 0)
    {
        std::cout<<"redis连接失败："<<this->redis_context->errstr<<std::endl;
        return false;
    }
    std::cout<<"redis连接成功"<<this->redis_context->errstr<<std::endl;

    this->redis_reply = (redisReply*)redisCommand(this->redis_context,"auth %s",redis_pd.c_str());
    if(this->redis_reply->type == REDIS_REPLY_ERROR)
    {
        std::cout<<"redis认证失败"<<std::endl;
        return false;
    }
    std::cout<<"redis认证成功"<<std::endl;

    this->redis_reply = (redisReply*)redisCommand(this->redis_context,"select %s",redis_db.c_str());
    if(this->redis_reply->type == REDIS_REPLY_ERROR)
    {
        std::cout<<"redis进入数据库"<<redis_db<<"失败"<<std::endl;
        return false;
    }
    std::cout<<"redis进入数据库"<<redis_db<<"成功"<<std::endl;

    return true;
}


void RedisPackage::RedisSetData(std::string redis_key,std::string redis_value)
{
    this->redis_reply = (redisReply*)redisCommand(this->redis_context,"set %s %s",redis_key.c_str(),redis_value.c_str());
    if(this->redis_reply == NULL && this->redis_context->err != 0)
    {
        std::cout<<"数据"<<redis_key<<":"<<redis_value<<"插入失败："<<this->redis_context->errstr<<std::endl;
        //this->ConnectRedis();
    }
    //std::cout<<"数据"<<redis_key<<"插入成功"<<this->redis_context->errstr<<std::endl;
    //freeReplyObject(this->redis_reply);
}

void RedisPackage::RedisSeManytData(std::vector<std::string> pipeline_cmd)
{
    for(int i=0;i<pipeline_cmd.size();i++)
    {
        redisAppendCommand(this->redis_context,pipeline_cmd[i].c_str());
    }
    redisReply *reply = 0;
    for (int i = 0; i < pipeline_cmd.size(); i++) 
    {
            int type = -1;
            std::string resp_str = "";
            
            int reply_status = redisGetReply(this->redis_context, (void **) &reply);
            if (reply_status == REDIS_OK && reply != NULL) 
            {
                type = reply->type;
                if (reply->str != NULL) 
                {
                    resp_str = reply->str;
                }
            } 
            else
            {
                std::cout<<"error: "<<pipeline_cmd[i]<<std::endl;
            }
    }
    freeReplyObject(reply);
    
    // if(this->redis_reply == NULL && this->redis_context->err != 0)
    // {
    //     std::cout<<"数据"<<redis_key<<":"<<redis_value<<"插入失败："<<this->redis_context->errstr<<std::endl;
    //     //this->ConnectRedis();
    // }
    //std::cout<<"数据"<<redis_key<<"插入成功"<<this->redis_context->errstr<<std::endl;
    //freeReplyObject(this->redis_reply);
}

void RedisPackage::RedisGetData(std::string redis_key)
{
    this->redis_reply = (redisReply*)redisCommand(this->redis_context,"get %s",redis_key.c_str());
    if(this->redis_reply == NULL && this->redis_context->err != 0)
    {
        std::cout<<"数据"<<redis_key<<"获取失败："<<this->redis_context->errstr<<std::endl;
        //this->ConnectRedis();
    }
    std::cout<<redis_key<<":"<<this->redis_reply->str<<std::endl;
    freeReplyObject(this->redis_reply);
}


void RedisPackage::DisconnectRedis()
{
    redisFree(this->redis_context);
    std::cout<<"redis断开连接"<<std::endl;
}


RedisPackage::~RedisPackage()
{
    redisFree(this->redis_context);
    this->redis_reply = NULL;
}