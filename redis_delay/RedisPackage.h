#ifndef _REDISPACKAGE_H_
#define _REDISPACKAGE_H_

#include <hiredis.h>
#include <string>
#include <vector>
class RedisPackage
{
public:
    redisContext* redis_context;
    redisReply* redis_reply;
    
public:
    RedisPackage(){};
    ~RedisPackage(); 
    bool ConnectRedis(std::string redis_ip,int redis_port,std::string redis_pd,std::string redis_db);
    void RedisSetData(std::string redis_key,std::string redis_value);
    void RedisSeManytData(std::vector<std::string> pipeline_cmd);
    void RedisGetData(std::string redis_key);
    void DisconnectRedis();

};

#endif