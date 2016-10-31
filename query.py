"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like ('%Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

Brand.query.filter(db.or_(Brand.founded < 1950 , Brand.discontinued != None)).all()

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):

    car_info = db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand, Brand.name == Model.brand_name).all()

    for name, brand_name, headquarters in car_info:      
        print "Name: " + name, "   " + "Brand: " + brand_name,"   " + "Headquarters: " +headquarters

get_model_info(1958)

    

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''
    brand_info = db.session.query(Model.name, Model.brand_name).join(Brand, Brand.name == Model.brand_name).all()

    for brand_name, name in brand_info:      
        print "Name: " + name, "        " + "Brand: " + brand_name

get_brands_summary()

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# ANSWER 1. An object is returned because we didnt fetch a record by using .all(), etc.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# ANSWER 2. An association table is a table that on it own has no particular fields that are needed,
# but is required to connect two "many to many" tables.  
# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):

    brand_name_list = []

    name_info = db.session.query(Model.brand_name).filter(Model.name.like ('%(mystr)%')).all() 
    for name in name_info:
        brand_name_list.append(name)

        print brand_name_list

search_brands_by_name('Cor')

def get_models_between(start_year, end_year):

    model_list = []

    model_info = db.session.query(Model.brand_name).filter(Model.year >= 'start_year', Model.yeat < 'end_year')
    for info in model_info:
        model_list.append(info)

        print model_list

    get_models_between(1904, 1955)
