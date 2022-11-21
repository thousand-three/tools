#!/bin/bash
end_date=$1
trading_day=$(date -d "1 days ago" +"%Y%m%d")
[ "x$2" != "x" ] && trading_day=$2
end_date_stamp=$(date -d "${end_date} 00:00:00" +%s)
trading_day_stamp=$(date -d "${trading_day} 00:00:00" +%s)
while [ ${end_date_stamp} -le ${trading_day_stamp} ]
do
        echo ${trading_day} >> a.txt
        trading_last_day=`date -d "${trading_day} 1 days ago" +"%Y%m%d"`
        trading_day=${trading_last_day}
        end_date_stamp=$(date -d "${end_date} 00:00:00" +%s)
        trading_day_stamp=$(date -d "${trading_day} 00:00:00" +%s)

done