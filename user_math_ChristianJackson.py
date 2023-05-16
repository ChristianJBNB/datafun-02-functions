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


#Second Function, Finding the total points of scored by the starters for a game

def get_total_points_of_starters(pg, sg, sf, pf, c):

     logger.info(f"get_total_points_of_starters({pg},{sg},{sf},{pf},{c})")

     starters_points = [pg,sg,sf,pf,c]

     try:
          starters_total_points = math.fsum(starters_points)
          logger.info(f"The total points for the starters of an NBA team are {starters_total_points}")
          return starters_total_points
     except Exception as ex:
          logger.info(f"Error: {ex}")


#Third Function, Finding the average ppgs over the span of 5 games for a player

def get_average_over_five_games(g1,g2,g3,g4,g5):

     logger.info(f"get_average_over_five_games({g1},{g2},{g3},{g4},{g5})")
     sum_of_games = [g1,g2,g3,g4,g5]

     try:
          avg_of_games = math.fsum(sum_of_games)/len(sum_of_games)
          logger.info(f"The average points per game for the span of five games is {avg_of_games}")
          return avg_of_games
     except Exception as ex:
          logger.info(f"Error: {ex}")
          
          
#Fourth Function, Finding the height of an NBA player in inches, while getting it in feet and inches

def get_height_of_player(feet, inches):

     logger.info(f"get_height_of_player({feet}, {inches})")
     feet_to_inches = feet * 12

     try:
          total_height_inches = feet_to_inches + inches
          logger.info(f"The height of the given player in inches is {total_height_inches}")
          return total_height_inches
     except Exception as ex:
          logger.info(f"Error: {ex}")


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
    
    #Code to test First Function

    logger.info("TRY: Call get_area_of_NBA_court() function with a different values.")
    get_area_of_NBA_court(100, 50)
    get_area_of_NBA_court(75, 60)
    get_area_of_NBA_court(55, 30) 
    logger.info("")

    #Code to test Second Function

    logger.info("TRY: Call get_total_points_of_starters() function with a different values.")
    get_total_points_of_starters(20, 5, 11, 17, 28)
    get_total_points_of_starters(5, 18, 33, 12, 5)
    get_total_points_of_starters(11, 22, 14, 9, 35)
    logger.info("")

    #Code to test Thrid Function

    logger.info("TRY: Call get_average_over_five_games() function with a different values.")
    get_average_over_five_games(35, 16, 29, 14, 7)
    get_average_over_five_games(55, 50, 43, 37, 44)
    get_average_over_five_games(11, 12, 13, 14, 15)
    logger.info("")

    #Code to test Fourth Function
    logger.info("TRY: Call get_height_of_player() function with a different values.")
    get_height_of_player(6, 5)
    get_height_of_player(7, 2)
    get_height_of_player(5, 10)
    logger.info("")

