from django.db import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# from sqlalchemy_test.settings import db_session, DATABASES
from sqlalchemy_test.settings import SA_DB_SESSION
from django.conf import settings
from sqlalchemy import inspect

# Create your models here.
Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'my_users_table'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    description = Column(String(200))
    
    def __str__(self):
        return f"{self.email}"
    
    @classmethod
    def get_all(cls):
        all_data = None
        with SA_DB_SESSION() as db_session: 
            all_data = db_session.query(cls).all()
        return all_data


#creating the given table if it dosent exists
def create_users_table(engine):
    inspector = inspect(engine)
    if not inspector.has_table(UserModel.__tablename__):
        Base.metadata.create_all(engine)
        
create_users_table(settings.DATABASES['default']['SA_ENGINE'])


# In Django's class-based views, the model attribute expects a Django Model class, 
# which has an _meta attribute and more. Therefore, you cannot use SQLAlchemy models directly with Django's class-based views.
# One way to work around this is to create a simple Django model that mirrors the columns 
# of your SQLAlchemy model, and then use that model in your class-based views. 
# Alternatively, you can write your own custom view that do not rely on Django's class-based views,
class DjangoUserModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)