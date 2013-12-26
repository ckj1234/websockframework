from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import redis
import memcache
import tools.dbAutoSwitchSlave

db=create_engine("mysql://root:@localhost/site?charset=utf8")
DBBase=declarative_base(name="DBBase")
#Session = sessionmaker(bind=db)
Session = sessionmaker(bind=db,class_=tools.dbAutoSwitchSlave.RoutingSession,slave_bind=[])

redisdb=redis.StrictRedis()
memclient=memcache.Client(['127.0.0.1:11211'])