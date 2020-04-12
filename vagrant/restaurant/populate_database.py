
# SCRIPT TO POPULATE OUR RESTAURANTMENU DATABASE #

import sys

# Import the SQLAlchemy dependencies from SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import our empty database into our environment.
# From our database_setup.py file import Base, Restaurant and MenuItem classes.
from database_setup import Base, Restaurant, MenuItem

# This is to communicate with our database.
engine = create_engine('sqlite:///restaurantmenu.db')

# Bind the engine to the base class.
# This makes the connections between our Class definitions and
# the corresponding Tables within our Database.
Base.metadata.bind = engine

# Create a SessionMaker Object, to establish a link of communication
# between our Code Executions and the Engine.
DBSession = sessionmaker(bind = engine)

# Create a session instance with the DBSession object.
session = DBSession()


# INSERT RESTAURANT #
# Insert my first Restaurant
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()

# READ RESTAURANTS #
# Read all Restaurants
restaurants = session.query(Restaurant).all()
print restaurants

# Read the first resturant.
# firstResult = session.query(Restaurant).first()
# print firstResult.name


# INSERT MENUITEM #
# Insert my first MenuItem
cheesepizza = MenuItem(
    name = "Cheese Pizza",
    description = "Made with all natural ingredients and fresh mozzarella",
    course = "Entree",
    price = "$8.99",
    restaurant = restaurants[0]
    )
session.add(cheesepizza)
session.commit()

# READ MENUITEMS #
# Read all MenuItems and show its name.
items = session.query(MenuItem).all()
for item in items:
    print item.name
