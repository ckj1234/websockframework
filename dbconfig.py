from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis
import memcache
import tools.dbAutoSwitchSlave
import qiniu.conf

db=create_engine("mysql://root:@localhost/site?charset=utf8",pool_recycle=10)
DBBase=declarative_base(name="DBBase")
#Session = sessionmaker(bind=db)
Session = sessionmaker(bind=db,class_=tools.dbAutoSwitchSlave.RoutingSession,slave_bind=[])

redisdb=redis.StrictRedis()
memclient=memcache.Client(['127.0.0.1:11211'])

qiniu.conf.ACCESS_KEY = "x5yGWWp6fBGMwlJyEU0GVzilkNIa7Mc87ibrKpdU"
qiniu.conf.SECRET_KEY = "r_8i1p4LCaiI0isFxuF2paAKhoQotGeqngCD4B1O"
qiniuSpace="kidswant"