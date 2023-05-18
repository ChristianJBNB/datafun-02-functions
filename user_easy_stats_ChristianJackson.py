"""
Name: Christian Jackson
Date: 5/18/23
Domain: NBA Players

Project: 2 task 4

Purpose: Illustrate the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules.

@ uses statistics module for descriptive stats
@ uses turtle module for drawing a chart
@ uses sys module for checking Python version

"""
import statistics 
import sys  

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

#Project 2 Task 4
#numofgames = xtimes
#pts_scored = yvalues

numofgames = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
pts_scored = [120, 135, 142, 89, 161, 119, 92, 145, 105, 107, 121, 132, 151]

logger.info(f"Number of points scored on different days by a NBA team =  {pts_scored}")

#Calculate mean, median, mode, variance, standard deviation, smallest, largest, and range

mean = statistics.mean(pts_scored)
logger.info(f"The mean of points scored is {mean:.2f}")

median = statistics.median(pts_scored)
logger.info(f"The median of points scored is {median:.2f}")

mode = statistics.mode(pts_scored)
logger.info(f"The mode of points scored is {mode:.2f}")

var = statistics.variance(pts_scored)
logger.info(f"The variance of points scored is {var:.2f}")

stdev = statistics.stdev(pts_scored)
logger.info(f"The standard deviation of points scored is {stdev:.2f}")

smallest = min(pts_scored)
logger.info(f"The smallest number of points scored is {smallest:.2f}")

largest = max(pts_scored)
logger.info(f"The largest number of points scored is {largest:.2f}")

logger.info(f"The range in the number of points scored is {smallest:.2f} - {largest:.2f}")


# if the lists are not the same size,
# log an error and quit the program
if len(numofgames) != len(pts_scored):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(numofgames)}!={len(pts_scored)}")
    quit()

# check the Python version before using the correlation function
logger.warn("Correlation requires Python version 3.10 or greater.")
logger.warn(f"Your version is {sys.version_info.major}.{sys.version_info.minor}")

# if the Python version is too old, we can quit now
if sys.version_info.minor < 10:
    logger.error("Please update Python to 3.10 or greater")
    logger.error("or use View / Command Palette / Python: Select Interpreter")
    logger.error("to get a newer one.")
    quit()

# If we're still here, use the correlation function from the statistics module
xx_corr = statistics.correlation(numofgames, numofgames)
xy_corr = statistics.correlation(numofgames, pts_scored)

# log the information 
logger.info("Here's some time series data about how many points an NBA team could score on a given day:")
logger.info(f"numofgames:{numofgames}")
logger.info(f"pts_scored:{pts_scored}")
logger.info(f"correlation between numofgames and numofgames = {xx_corr:.2f}")
logger.info(f"correlation between numofgames and pts_scored = {xy_corr:.2f}")

# Calculate slope and intercept of a line

# Here's some bivariant data (two series of data)

# Call linear_regression() function -
# and get back 2 values: slope and intercept
# describing the 'best fit' line through the data
slope, intercept = statistics.linear_regression(numofgames, pts_scored)

# Choose an x value off in the future (future x)
future_x = 300

# Extend the line out into the unknown future
# and read the value (of future y)
future_y = round(slope * future_x + intercept)

logger.info("Here's some bivariant data (2 variables, together):")
logger.info(f"x:{numofgames}")
logger.info(f"y:{pts_scored}")
logger.info("Calculate the slope and intercept of a best fit straight line:")
logger.info(f"   slope = {slope:.2f}")
logger.info(f"   intercept = { intercept:.2f}")
logger.info("Let's use our best fit line to PREDICT a future value.")
logger.info(f"   At future x = {future_x:d},")
logger.info(f"   we predict the value of y will be { future_y:d}.")
logger.info("How'd we do? Does this make sense given the data?")
logger.info("Remember to close the app. Control c (or d or z maybe) to close it.")


# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())