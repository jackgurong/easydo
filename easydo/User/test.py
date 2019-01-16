import json
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import usertable

# 创建对象的基类:
Base = declarative_base()

# 定义UserInfo对象:
class UserInfo(Base):
    # 表的名字:
    __tablename__ = 'userInfo'

    # 表的结构:
    u_userid = Column(Integer, primary_key=True, autoincrement=True)
    u_userpassword = Column(String(20))
    u_sex = Column(String(10))
    u_birthday = Column(String(20))
    u_mail = Column(String(20))
    u_phonenumber = Column(String(20))

if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:890919@localhost:3306/easydo', encoding='utf-8', echo=True)
    Base.metadata.create_all(engine)
    user = UserInfo(u_userpassword='pwd', u_sex='s',
                                u_birthday='birthday', u_mail='mail',
                                u_phonenumber='phone')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    session.add(user)
    session.commit()
    session.close()