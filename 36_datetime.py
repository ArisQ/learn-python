#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timedelta, timezone

print(datetime.now())
dt = datetime(2012, 12, 21, 0, 0, 0)
print(dt)
print(dt.timestamp())
print(datetime.fromtimestamp(1356019200.0))
print(datetime.utcfromtimestamp(1356019200.0))
print(datetime.strptime('2012-12-21 00:00:00', '%Y-%m-%d %H:%M:%S'))
print(dt.strftime('%a, %b %d %H:%M'))
print(datetime.now() + timedelta(days=1, hours=10))

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('utc_dt:', utc_dt)
print('bj_dt:', bj_dt)
print('tokyo_dt:', tokyo_dt)
print('tokyo_dt2:', tokyo_dt2)


def to_timestamp(dt_str, tz_str):
    time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    grp = re.match(r'UTC([+\-])?([0-9]+):([0-9]+)', tz_str).groups()  # TODO: 替换为精确表示时区的正则表达式
    tz_hours = int(grp[1])
    tz_minutes = int(grp[2])
    if grp[0] == '-':
        tz_hours = -tz_hours
        tz_minutes = -tz_minutes
    return time.replace(tzinfo=timezone(timedelta(hours=tz_hours, minutes=tz_minutes))).timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('ok')
