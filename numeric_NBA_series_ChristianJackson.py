'''
Purpose: Create a class that inherits everything from NumericSeries and adds
attributes and/or behavior specific to Weather. 

If you don't need to add specialized attributes or behavior, 
you can just use the original NumericSeries class directly. 
No subclassing required.

We get all of our parent's attributes and methods for free (no coding required).

Name: Christian Jackson
Date: 5/18/23
Domain: NBA Players
Project: 2 task 5

Goal: Your goal is to create another derived class associated with your chosen subject area domain

NBA Players adds: a Team attribute

'''

# From the name of the module (the file name without .py), import the class we want to inherit from
from numeric_series import NumericSeries

# From the util_datafun_logger module, import the setup_logger function
from util_datafun_logger import setup_logger


class NumericNBASeries(NumericSeries):
    """
    A class representing a numeric series customized for weather data.

    (Additional) Attributes:
       location (string): the location where the data was collected
    """

    def __init__(self, name, units, data, team):
        """
        Initialize the object when first created using the arguments passed in.
        Every class needs an __init__ method to construct a new object.

        @args:
            self (object): the object being created that will hold the real data
            name (str): a short name for this list of numeric data
            units (str): the units in which the data is measured
            data (list): the list of numeric data to be held by the object
            location (str): the location where the data was collected

        """

        # First, initialize the parent (super) class with parent's attributes
        # By calling the super constructor method
        super().__init__(name, units, data)

        # Then, initialize our additional specialized attributes
        self.team = team

    def __str__(self):
        """
        Return a string representation of the instantiated object.
        The two underscores before and after indicate this is a special method.
        Every class needs a __str__ method that returns a string representation of the object.
        Be sure to use self.attribute_name so you use the object's attribute, not a local variable! 

        Returns:
            str: a string representation of the instantiated object
        """
        str = f"NumericNBASeries with name={self.name}, units={self.units}, team={self.team}, and {len(self.data)} data points: {self.data}"
        return str



if __name__ == "__main__":
    # If we're running this script (instead of using it in another class or script), 
    # Run some code to try our class

    # First, setup logging
    logger, logname = setup_logger(__file__)

    # Create an object by calling the constructor 
    # The constructor method is always the name of the class
    # pass in the information required by the __init__ method defined in the class

    name1 = "Lebron James"
    units1 = "Pts"
    data1 = [23, 44, 31, 37, 34, 45]
    team1 = "Lakers"

    object1 = NumericNBASeries(name1, units1, data1, team1)

  
    name2 = "Zion Williamson"
    units2 = "Pts"
    data2 = [17, 32, 40, 21, 26, 28]
    team2 = "Pelicans"

    object2 = NumericNBASeries(name2, units2, data2, team2)

    
    # Create another object 

    # use range() to create a list of values from 65 to 78
    # list() converts the range object to a list
    # range() is a generator - it creates a sequence of numbers without storing them in memory
    # The arguments in range are from (inclusive) and to (exclusive)

    data3 = list(range(26, 34))
    name3 = "Donovan Mitchell"
    units3 = "Pts"
    team3 = "Cavaliers"

    object3 = NumericNBASeries(name3, units3, data3, team3)

    # log the objects created
    logger.info(f"Created: {object1}")
    logger.info(f"Created: {object2}")
    logger.info(f"Created: {object3}")

    object_list = [object1, object2, object3]

    # Loop through our objects and get some statistics
    # Rather than using a built-in function and passing in our data
    # we call methods directly on our objects
    # Why? It's just another way to organize and reuse code. 
    # We encapusulate (wrap up) the attributes and associated methods into a resuable class. 
    # Write the class once, and use it many times. 
    # We'll see this a lot when we use dataframes to hold tables of data. 
    # Many popular libraries provide reusuable classes. 
    # It's a powerful way to organize code when dealing with many objects of the same type.

    for object in object_list:
        logger.info(object)
        logger.info(f"Count: {object.count()}")
        logger.info(f"Sum: {object.sum()}")
        logger.info(f"Mean: {object.mean()}")
        logger.info(f"Median: {object.median()}")
        logger.info("------------------")

    # Read log file and print it to the terminal
    with open(logname, 'r') as file_wrapper:
      print(file_wrapper.read())