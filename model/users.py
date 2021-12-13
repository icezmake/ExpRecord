from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, comment='自增id主键')
    name = Column(String(7), unique=True, comment='用户名')
    gender = Column(String(7), comment='用户性别')


if __name__ == "__main__":
    # 初始化数据库连接:
    engine = create_engine('mysql+pymysql://root:a19961217xian@localhost:3306/ExpRecord')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    res = session.query(Users).filter(Users.id == '1').first()
    print(res.name)
    session.close()