# -*- coding: utf-8 -*-
"""
@author: guqiuyang
@description: 封装用户类
@create time: 2018/12/18
"""

import json
import usertable


class User(object):
    
    def __init__(self, user_json=None, sql_json=None):
        self.user_json = user_json
        self.sql_json = sql_json
        usertable.CreateTable(self.sql_json).create_table()
    """
    def engine(self):
        '''连接数据库'''
        f = open(self.sql_json)
        sql_dict = json.load(f)
        engine = create_engine(
            'mysql+pymysql://' +
            sql_dict['user'] +
            ':' +
            sql_dict['password'] +
            '@' +
            sql_dict['host'] +
            ':3306/' +
            sql_dict['database'] +
            '?charset=utf8')
        return engine

    def init_sql_table(self):
        '''初始化用户表，如果没存在则新建'''
        usertable.Base.metadata.create_all(self.engine())
    """            

    def LoadInfo(self): #辅助函数
        print('get user info from mysql')

    def register(self):
        info_dict = json.loads(self.user_json)
        pass

        
    def SignOut(self, name, passwd):
        print('add a record to mysql')
    
    def Login(self, name, passwd):
        print('%s has login, passwd = %s' % (name, passwd))

    def DeleteUser(self, name, passwd):
        print('delete a user')

def user_test():
    print('just a test')

if __name__ == '__main__':
    user = User(sql_json="E:\\Project\\easydo\\scripts\\sqlinfo.json")
    