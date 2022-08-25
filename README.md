# Simple Arbitrage Betting Calculator Interface
A simple python code for gathering betting data and interacting with the 'Arbitrage Betting Calculator'.
Note: This code is not tested, it only exists to give a quick starting point.

## API's used in this project
 - https://rapidapi.com/api-sports/api/api-football
 - https://rapidapi.com/dannyray44/api/arbitrage-betting-calculator

# Setup
 - Create an account at https://rapidapi.com (both the API's used in this project are currently free, you can check this at the urls detailed above + '/pricing')
 - Sign up to use the two APIs above
 - Copy your 'X-RapidAPI-Key' into the config.json file
 - run the main.py file of this project using python

# Description
This code is built to use two API's, both are hosted at https://rapidapi.com. The first API is api-football, this api provides information about upcoming football games. The second API is my arbitrage-betting-calculator, this is sent the football data gathered from api-football, it will return the optimal betting strategy to guarantee profit.

```
        (/odds)                    (football data)          (formatted football data)                       (betting strategy)
user -------------> API-Football -------------------> user ---------------------------> betting-calculator --------------------> User
```

# Information for developers
RapidAPI.com has excellent examples of how to call the API's hosted on through their website in many languages. Simply follow the link at the top of this page for an example.

## API-Football usage
This project gathers data from '/odds'. The response is a json string formatted as so. Note: Information relevant to this project is excluded.
```yaml
{
    ...
    "fixture": {...},
    "response": [
        {
            ...
            "bookmakers": [
                {
                    "id": Bookmaker ID (e.g. 12),
                    "name": Bookmaker Name (e.g. "Betfair"),
                    "bets": [
                        {
                            "id": Bet Type ID (e.g. 1),
                            "name": Bet Type Name (e.g "Match Winner"),
                            "values": [
                                {
                                    "value": What the bet is being placed on (e.g "Home"),
                                    "odd": The odds for this bet (e.g "2.35")
                                },
                                {},{},{},,,{}
                            ]
                        },
                        {},{},{},,,{}
                    ]
                },
                {},{},{},,,{}
            ]
        },
        {},{},{},,,{}
    ]
}
```

## Arbitrage Betting Calculator
### Accepted input format
The arbitrage betting calculator will accept data in a similar format as laid out above. However it will only accept one element from "response" at a time and only the "bookmaker" data. Also additional perimeters can be added (see below).
```yaml
{
    "bookmakers": [
        {
            "id": Bookmaker ID (e.g. 12),
            "name": Bookmaker Name (e.g. "Betfair"),
            "bets": [
                {
                    "id": Bet Type ID (e.g. 1),
                    "name": Bet Type Name (e.g "Match Winner"),
                    "max_bet": "235.12"                 // How much money is available in this website, or how much you are willing to bet (default=1000)
                    "values": [
                        {
                            "value": What the bet is being placed on (e.g "Home"),
                            "odd": The odds for this bet (e.g "2.35"),
                            "lay": true,                // if this is a lay bet (default: false)
                            "volume": "52.12",          // the maximum amount that can be placed on this bet (default: infinite, will be limited by the sites "max_bet")
                            "already placed": "15",     // acts as a minimum amount that can be placed on this bet (default: 0)
                        },
                        {},{},{},,,{}
                    ]
                },
                {},{},{},,,{}
            ]
        },
        {},{},{},,,{}
    ]
}
```
### Response format
The calculator will return the information in the same format that it received it with some additional parameters added. Note: only the data for the bets which money should be placed on will be returned
```yaml
{
    "total bet size": 3250,       // the total amount of money to be placed on bets
    "profit": 1565,               // the expected profit from these bets
    "slack": 0.05,                // the variation in potential profit dependant on the outcome
    "no. bets": 8,                // How many bets are needed to be placed
    "bookmakers": [
        {
            "id": Bookmaker ID (e.g. 12),
            "name": Bookmaker Name (e.g. "Betfair"),
            "bets": [
                {
                    "id": Bet Type ID (e.g. 1),
                    "name": Bet Type Name (e.g "Match Winner"),
                    "values": [
                        {
                            "value": What the bet is being placed on (e.g "Home"),
                            "odd": The odds for this bet (e.g "2.35"),
                            "wager": "325.15"   		// How much money to place on this bet (e.g. Place £325.15 on the home team to win @ betfair)
                        },
                        {},{},{},,,{}
                    ]
                },
                {},{},{},,,{}
            ]
        },
        {},{},{},,,{}
    ]
}
```




