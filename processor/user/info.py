#coding:utf-8
from datamodel.user import User
from tools.helper import Res
from tools.session import CheckSession
import dbconfig


@CheckSession()
def run(uid):
    if isinstance(uid,list)==False:
        uid=[uid]
    with dbconfig.Session() as session:
        users=session.query(User).filter(User.uid.in_(uid)).all()
        ulist=[]
        for user in users:
            ulist.append(user.toJson())
    return Res({"users":ulist})