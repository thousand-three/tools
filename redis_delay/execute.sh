#!/bin/bash
g++ -std=c++11 /home/risk/redis_delay/common.cpp /home/risk/redis_delay/RedisPackage.cpp /home/risk/redis_delay/read_file.cpp -o /home/risk/redis_delay/redis_delay -I /home/risk/risk_system_future_redis/api/hiredis/ -L /home/risk/risk_system_future_redis/api/hiredis/ -lhiredis
