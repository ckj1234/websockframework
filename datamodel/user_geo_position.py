__author__ = 'amen'
from sqlalchemy import *
import dbconfig
import time
class UserGeoPosition(dbconfig.DBBase):
    __tablename__ = 'user_geo_pos'
    uid=Column(BigInteger,autoincrement=True,primary_key=True,nullable=False)
    geokey=Column(BigInteger,index=True,nullable=False)
    lat=Column(Float,nullable=False)
    long=Column(Float,nullable=Float)
    time=Column(TIMESTAMP,server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))