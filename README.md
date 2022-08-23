# Simple-Arbitrage-Betting-Calculator-Interface
A simple python code to gather betting data and interacting with the 'Arbitrage Betting Calculator'.]
Note: This code is not designed or tested to any standard, it only exists to give a quick starting point to other developers.


# Setup
 - Create an account at https://rapidapi.com (both the API's used in this project are currently free, you can check this at https://rapidapi.com/api-sports/api/api-football/pricing & https://rapidapi.com/dannyray44/api/arbitrage-betting-calculator/pricing)
 - Copy your 'X-RapidAPI-Key' into the config.json file
 - run the main.py file of this project using python

# description
This code takes all the odds data about future games from https://rapidapi.com/api-sports/api/api-football and passes one event at a time to https://rapidapi.com/dannyray44/api/arbitrage-betting-calculator, after the optimal betting strategy is returned if there is a profit it will then fetch extra information about the game (location, teams, etc..) and print both pieces of data to the console.
