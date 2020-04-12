# Code to practice Database UPDATE #
# This code is to READ and UPDATE the price of some MenuItems,
# especialy the price of Veggie Burgers.

# Imports
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# Communicate with our database
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# FOUR-STEP PROCESS #

# 1. Find Entry.
# Execute a Query to Find the Veggie Burger we want, and store in a variable.
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"

# Get just one of the Veggie Burgers of Urban Burger
# For my database is id equal to 2 or 10
urbanVeggieBurger = session.query(MenuItem).filter_by(id = 2).one()
print urbanVeggieBurger.price # $7.50, before to be updated.

# 2. Reset Values.
# Set the new price of the variable.
# Update price to $2.99
urbanVeggieBurger.price = '$2.99'

# 3. Add to Session.
# Add the variable to our session.
session.add(urbanVeggieBurger)

# 4. Commit Session.
# Commit the session to the database.
session.commit()


# UPDATE PRICE OF ALL VEGGIE BURGES IN OUR DATABASE #
for veggieBurger in veggieBurgers:
    if veggieBurger.price != '$2.99':
        veggieBurger.price = '$2.99'
        session.add(veggieBurger)
        session.commit()
