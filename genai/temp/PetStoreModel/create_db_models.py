# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Pet(Base):
    """
    description: Stores pets available in the store
    """
    __tablename__ = 'pet'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    photo_urls = Column(String)  # Designed to store a string representation of URLs
    status = Column(Enum('available', 'pending', 'sold'))


class Category(Base):
    """
    description: Categories to which pets belong
    """
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class Tag(Base):
    """
    description: Tags associated with pets
    """
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class PetTag(Base):
    """
    description: Association table for pets and tags
    """
    __tablename__ = 'pet_tag'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pet_id = Column(Integer, ForeignKey('pet.id'))
    tag_id = Column(Integer, ForeignKey('tag.id'))


class Order(Base):
    """
    description: Orders placed in the store
    """
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pet_id = Column(Integer, ForeignKey('pet.id'))
    quantity = Column(Integer)
    ship_date = Column(DateTime)
    status = Column(Enum('placed', 'approved', 'delivered'))
    complete = Column(Boolean)


class Customer(Base):
    """
    description: Customers who purchase pets
    """
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    address_id = Column(Integer, ForeignKey('address.id'))


class Address(Base):
    """
    description: Customer addresses
    """
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)


class User(Base):
    """
    description: Users who can perform operations
    """
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(String)
    user_status = Column(Integer)


class Inventory(Base):
    """
    description: Inventory with quantities by status
    """
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String)
    quantity = Column(Integer)


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    pet1 = Pet(id=1, name="Buddy", category_id=1, photo_urls="url1", status="available")
    pet2 = Pet(id=2, name="Kitty", category_id=2, photo_urls="url2", status="pending")
    pet3 = Pet(id=3, name="Bruno", category_id=1, photo_urls="url3", status="sold")
    pet4 = Pet(id=4, name="Max", category_id=3, photo_urls="url4", status="available")
    category1 = Category(id=1, name="Dogs")
    category2 = Category(id=2, name="Cats")
    category3 = Category(id=3, name="Birds")
    category4 = Category(id=4, name="Fish")
    tag1 = Tag(id=1, name="Cute")
    tag2 = Tag(id=2, name="Small")
    tag3 = Tag(id=3, name="Furry")
    tag4 = Tag(id=4, name="Friendly")
    pet_tag1 = PetTag(id=1, pet_id=1, tag_id=1)
    pet_tag2 = PetTag(id=2, pet_id=2, tag_id=2)
    pet_tag3 = PetTag(id=3, pet_id=3, tag_id=3)
    pet_tag4 = PetTag(id=4, pet_id=4, tag_id=4)
    order1 = Order(id=1, pet_id=1, quantity=2, ship_date=date(2023, 10, 10), status="placed", complete=True)
    order2 = Order(id=2, pet_id=3, quantity=1, ship_date=date(2023, 10, 12), status="approved", complete=False)
    order3 = Order(id=3, pet_id=2, quantity=4, ship_date=date(2023, 11, 5), status="delivered", complete=True)
    order4 = Order(id=4, pet_id=4, quantity=3, ship_date=date(2023, 11, 1), status="approved", complete=False)
    customer1 = Customer(id=1, username="john_doe", address_id=1)
    customer2 = Customer(id=2, username="jane_smith", address_id=2)
    customer3 = Customer(id=3, username="jim_brown", address_id=3)
    customer4 = Customer(id=4, username="lisa_white", address_id=4)
    address1 = Address(id=1, street="437 Lytton", city="Palo Alto", state="CA", zip="94301")
    address2 = Address(id=2, street="123 Main St", city="San Francisco", state="CA", zip="94105")
    address3 = Address(id=3, street="789 Elm St", city="Los Angeles", state="CA", zip="90001")
    address4 = Address(id=4, street="456 Oak St", city="San Jose", state="CA", zip="95112")
    user1 = User(id=1, username="theUser", first_name="John", last_name="James", email="john@email.com", password="12345", phone="1234567890", user_status=1)
    user2 = User(id=2, username="admin", first_name="Admin", last_name="User", email="admin@email.com", password="admin", phone="0987654321", user_status=2)
    user3 = User(id=3, username="guest", first_name="Guest", last_name="User", email="guest@email.com", password="guest", phone="1122334455", user_status=0)
    user4 = User(id=4, username="superuser", first_name="Super", last_name="User", email="superuser@email.com", password="super", phone="1231231234", user_status=3)
    inventory1 = Inventory(id=1, status="available", quantity=50)
    inventory2 = Inventory(id=2, status="pending", quantity=20)
    inventory3 = Inventory(id=3, status="sold", quantity=30)
    inventory4 = Inventory(id=4, status="available", quantity=15)
    
    
    
    session.add_all([pet1, pet2, pet3, pet4, category1, category2, category3, category4, tag1, tag2, tag3, tag4, pet_tag1, pet_tag2, pet_tag3, pet_tag4, order1, order2, order3, order4, customer1, customer2, customer3, customer4, address1, address2, address3, address4, user1, user2, user3, user4, inventory1, inventory2, inventory3, inventory4])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
