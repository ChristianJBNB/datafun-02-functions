"""
Name: Christian Jackson
Date: 5/16/23
Domain: NBA Players
Project: 2 task 3

This file will use the math module to manipulate data.
"""

#Import math module

import math

#Steal logger setup code

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

#Define one function 

def get_area_of_NBA_court(height,length):

     logger.info(f"get_area_of_NBA_court({height},{length})")

     try:
          court_area = height * length
          logger.info(f"The area of an NBA sized court is {court_area} units")
          return court_area
     except Exception as ex:
          logger.error(f"Error: {ex}")

#Add some code from defenseive_math.py and Implement the method I made.

if __name__ == "__main__":
    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info(f"math.pi = {math.pi}")
    logger.info(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    logger.info(f"math.radians(180)         = {math.radians(180)}")
    logger.info("")
    
    logger.info("TRY: Call get_area_of_NBA_court() function with a different values.")
    get_area_of_NBA_court(100,50)
    get_area_of_NBA_court(75,60)
    get_area_of_NBA_court(55,30) 
    logger.info("")

