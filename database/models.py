# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  December 06, 2024 19:31:55
# Database: sqlite:////tmp/tmp.euqO5H1gPc-01JEEQ7QVCPM14D2W4EF4PYMYW/PetStoreModel/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Address(SAFRSBaseX, Base):
    """
    description: Customer addresses
    """
    __tablename__ = 'address'
    _s_collection_name = 'Address'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    CustomerList : Mapped[List["Customer"]] = relationship(back_populates="address")



class Category(SAFRSBaseX, Base):
    """
    description: Categories to which pets belong
    """
    __tablename__ = 'category'
    _s_collection_name = 'Category'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    PetList : Mapped[List["Pet"]] = relationship(back_populates="category")



class Inventory(SAFRSBaseX, Base):
    """
    description: Inventory with quantities by status
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    status = Column(String)
    quantity = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)



class Tag(SAFRSBaseX, Base):
    """
    description: Tags associated with pets
    """
    __tablename__ = 'tag'
    _s_collection_name = 'Tag'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    PetTagList : Mapped[List["PetTag"]] = relationship(back_populates="tag")



class User(SAFRSBaseX, Base):
    """
    description: Users who can perform operations
    """
    __tablename__ = 'user'
    _s_collection_name = 'User'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(String)
    user_status = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)



class Customer(SAFRSBaseX, Base):
    """
    description: Customers who purchase pets
    """
    __tablename__ = 'customer'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    address_id = Column(ForeignKey('address.id'))

    # parent relationships (access parent)
    address : Mapped["Address"] = relationship(back_populates=("CustomerList"))

    # child relationships (access children)



class Pet(SAFRSBaseX, Base):
    """
    description: Stores pets available in the store
    """
    __tablename__ = 'pet'
    _s_collection_name = 'Pet'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(ForeignKey('category.id'))
    photo_urls = Column(String)
    status = Column(String(9))

    # parent relationships (access parent)
    category : Mapped["Category"] = relationship(back_populates=("PetList"))

    # child relationships (access children)
    OrderList : Mapped[List["Order"]] = relationship(back_populates="pet")
    PetTagList : Mapped[List["PetTag"]] = relationship(back_populates="pet")



class Order(SAFRSBaseX, Base):
    """
    description: Orders placed in the store
    """
    __tablename__ = 'order'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    pet_id = Column(ForeignKey('pet.id'))
    quantity = Column(Integer)
    ship_date = Column(DateTime)
    status = Column(String(9))
    complete = Column(Boolean)

    # parent relationships (access parent)
    pet : Mapped["Pet"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)



class PetTag(SAFRSBaseX, Base):
    """
    description: Association table for pets and tags
    """
    __tablename__ = 'pet_tag'
    _s_collection_name = 'PetTag'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    pet_id = Column(ForeignKey('pet.id'))
    tag_id = Column(ForeignKey('tag.id'))

    # parent relationships (access parent)
    pet : Mapped["Pet"] = relationship(back_populates=("PetTagList"))
    tag : Mapped["Tag"] = relationship(back_populates=("PetTagList"))

    # child relationships (access children)
