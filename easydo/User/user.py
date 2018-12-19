# -*- coding: utf-8 -*-
"""
@author: guqiuyang
@description: 封装用户类
@create time: 2018/12/18
"""

import json
import logging
from usertable import UserInfo, UserAccount, UserStock
from usertable import StockInformation, StockDealRecord, CreateTable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class User(object):
    
    def __init__(self, user_json=None, sql_json=None):
        self.user_json = user_json
        self.sql_json = sql_json
        CreateTable(self.sql_json).create_table()

    def LoadInfo(self): #辅助函数
        print('get user info from mysql')

    def session(self):
        """创建数据库连接的session"""
        f = open(self.sql_json)
        sql_dict = json.load(f)

        engine = create_engine('mysql+pymysql://' + sql_dict['user'] +
            ':' + sql_dict['password'] + '@' + sql_dict['host'] +
            ':3306/' + sql_dict['database'], encoding='utf-8', echo=True)

        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        sion = DBSession()
        return sion

    def register(self):
        """用户注册模块"""
        f = open(self.user_json)
        user_dict = json.load(f)
        qu = self.session().query(UserInfo).filter(UserInfo.u_phonenumber
                       == user_dict['phone'])

        print("-"*20)
        print(qu)
        if qu is None:
            ed_user = UserInfo(u_userpassword=user_dict['pwd'], u_sex=user_dict['sex'],
                                u_birthday=user_dict['birthday'], u_mail=user_dict['mail'],
                                u_phonenumber=user_dict['phone'])
            self.session().add(ed_user)
            self.session().close()
        else:
            pass
        
    def SignOut(self, name, passwd):
        print('add a record to mysql')
    
    def Login(self, name, passwd):
        print('%s has login, passwd = %s' % (name, passwd))

    def DeleteUser(self, name, passwd):
        print('delete a user')


if __name__ == '__main__':
    user = User(user_json="E:\\Project\\easydo\\scripts\\userinfo.json", 
                sql_json="E:\\Project\\easydo\\scripts\\sqlinfo.json")
    user.register()
    
    