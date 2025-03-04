#  from sqlalchemy import create_engine
#  from sqlalchemy.orm import sessionmaker, DeclarativeBase
#  from sqlalchemy import Column
#  from sqlalchemy import Integer, String
#
#  engine = create_engine('sqlite:///ecommerce.db', echo=True)
#  SessionLocal = sessionmaker(bind=engine)
#
#
#  class Base(DeclarativeBase):
#      pass
#
#
#  class User(Base):
#      __tablename__ = "user"
#
#      id = Column(Integer, primary_key=True)
#      name = Column(String(50), nullable=False)
#      fullname = Column(String)
#      nickname = Column(String(30))

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase


engine = create_async_engine('postgresql+asyncpg://ecommerce:postgres@localhost:5432/ecommerce', echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase):
    pass
