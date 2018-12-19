# -*- coding: utf-8 -*-
"""
@author: guqiuyang
@description: 定义用户类相关的表
@create time: 2018/12/02
"""


import json
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base


# 创建对象的基类:
Base = declarative_base()

# 定义UserInfo对象:
class UserInfo(Base):
    # 表的名字:
    __tablename__ = 'userInfo'

    # 表的结构:
    u_userid = Column(Integer, primary_key=True, autoincrement=True)
    u_userpassword = Column(String(20))
    u_sex = Column(String(2))
    u_birthday = Column(String(10))
    u_mail = Column(String(20))
    u_phonenumber = Column(String(12))


# 定义UserAccount对象:
class UserAccount(Base):
    # 表的名字:
    __tablename__ = 'userAccount'

    # 表的结构:
    u_account_no = Column(Integer, primary_key=True, autoincrement=True)
    u_userid = Column(None, ForeignKey('userInfo.u_userid'))
    u_account_balance = Column(String(20))
    u_near_modif_time = Column(String(20))



# 定义UserStock对象:
class UserStock(Base):
    # 表的名字:
    __tablename__ = 'userStock'

    # 表的结构:
    u_stock_no = Column(Integer, primary_key=True, autoincrement=True)
    stock_number = Column(String(10))
    u_account_no = Column(None, ForeignKey('userAccount.u_account_no'))
    

# 定义StockInformation对象:
class StockInformation(Base):
    # 表的名字:
    __tablename__ = 'stockInformation'

    # 表的结构:
    u_stock_no = Column(Integer, primary_key=True, autoincrement=True)
    stock_number = Column(String(10))
    u_account_no = Column(None, ForeignKey('userAccount.u_account_no'))
  
# 定义StockDealRecord对象:
class StockDealRecord(Base):
    # 表的名字:
    __tablename__ = 'stockDealRecord'

    # 表的结构:
    u_deal_no = Column(Integer, primary_key=True, autoincrement=True)
    s_stock_no = Column(None, ForeignKey('userStock.u_stock_no'))
    u_account_no = Column(None, ForeignKey('userAccount.u_account_no'))
    s_stock_price = Column(String(15))
    s_deal_number = Column(String(15))
    s_not_deal_number = Column(String(15))
    s_deal_type = Column(String(8))
    s_deal_state = Column(String(8))
    s_document_create_time = Column(String(20))
    s_deal_finish_time = Column(String(20))
  

class CreateTable(object):
    """
    建立User相关的表
    """

    def __init__(self, sql_json):
        self.sql_json = sql_json

    def create_table(self):
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
            sql_dict['database'],
            encoding='utf-8',
            echo=True)
        Base.metadata.create_all(engine)
        