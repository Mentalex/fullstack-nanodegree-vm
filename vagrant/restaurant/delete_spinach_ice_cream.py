# Code to practice Database DELETE #
# This code is to DELETE Spinach Ice Cream of MenuItems.

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

# THREE-STEP PROCESS #

# 1. Find Entry.
# Execute a Query to Find the Spinach Ice Cream, and store in a variable.
# spinachIceCreams = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream')
# for spinachIceCream in spinachIceCreams:
#     print spinachIceCream.id
#     print spinachIceCream.restaurant.name
#     print "\n"

# Only Auntie Ann's Dinner was the only restaurant with Spinach Ice Cream.
spinachIceCream = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
print spinachIceCream.restaurant.name

# 2. Delete item with delete Session method.
session.delete(spinachIceCream)

# 3. Commit the Session.
session.commit()
