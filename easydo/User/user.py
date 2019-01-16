# -*- coding: utf-8 -*-
"""
@author: guqiuyang
@description: 封装用户类
@create time: 2018/12/18
"""

import json
import logging
import usertable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from hashlib import sha1


class User(object):
    
    def __init__(self, sql_json=None):
        self.sql_json = sql_json

    def LoadInfo(self): #辅助函数
        print('get user info from mysql')

    def logger(self):
        """日志函数"""
        logging.basicConfig(level = logging.INFO,format = 
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log = logging.getLogger(__name__)
        return log

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

    def register(self, user_json):
        """用户注册"""
        f = open(user_json)
        user_dict = json.load(f)
        session = self.session()

        try:
            self.session().query(usertable.UserInfo).filter(usertable.UserInfo.u_phonenumber
                       == user_dict['phone']).one()
            self.logger().info("该手机号码已注册")
        except:
            user_pwd = sha1(user_dict['pwd'].encode('utf-8')).hexdigest()
            print(user_pwd, len(user_pwd))
            user = usertable.UserInfo(u_userpassword=user_pwd, u_sex=user_dict['sex'],
                                u_birthday=user_dict['birthday'], u_mail=user_dict['mail'],
                                u_phonenumber=user_dict['phone'])
            session.add(user)
            session.commit()
            session.close()
            self.logger().info("用户注册成功")

        
    def SignOut(self):
        """用户退出"""
        pass
    
    def Login(self, user_json):
        """用户登录"""
        f = open(user_json)
        user_dict = json.load(f)
        user_input_pwd = sha1(user_dict['pwd'].encode('utf-8')).hexdigest()
        # print(user_input_pwd)

        try:
            userinfo = self.session().query(usertable.UserInfo.u_userpassword).filter(
                usertable.UserInfo.u_phonenumber == user_dict['phone'])
            print(userinfo)
            if userinfo.u_userpassword == user_input_pwd:
                self.logger().info("登录成功")
                return True
            else:
                self.logger().info("登录失败")
        except:
            self.logger().info("请检查账号密码是否出错")

    def DeleteUser(self, name, passwd):
        print('delete a user')

    def test(self):
        self.session().query(usertable.UserInfo)
        self.session().close()

if __name__ == '__main__':
    user_json="E:\\Project\\easydo\\scripts\\userinfo.json"
    user = User(sql_json="E:\\Project\\easydo\\scripts\\sqlinfo.json")
    #user.register(user_json)
    #user.Login(user_json)
    print(user.test())
    
    