
# CONFIGURATION #

##### beginning of file #####
import sys
# Provides a number of functions and variables that can be used
# to manipulate different parts of the Python run-time environment.

from sqlalchemy import Column, ForeignKey, Integer, String
# These will come in handy when we are writing our mapper code.

from sqlalchemy.ext.declarative import declarative_base
# We will use in the configuration and class code.

from sqlalchemy.orm import relationship
# To create our foreign key relationship,
# and will be used when we write up our mapper.

from sqlalchemy import create_engine

# This instance will help us get set up when we begin to write our class code.
# The declarative_base will let SQLAlchemy know that our classes are special
# SQLAlchemy classes that correspond to tables in our database.
Base = declarative_base()


# CLASS #
class Restaurant(Base):
    # TABLE #
    __tablename__ = 'restaurant'

    # MAPPER #
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

# CLASS #
class MenuItem(Base):
    # TABLE #
    __tablename__ = 'menu_item'

    # MAPPER #
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


##### end of file #####
engine = create_engine('sqlite:///restaurantmenu.db')
# Will create a new file .db
# That we can use similarly to a more robust database like MySQL or PostgreSQL.

Base.metadata.create_all(engine)
# Will goes into the database
