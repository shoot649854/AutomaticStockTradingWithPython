# encoding: utf-8

# This code is free, THANK YOU!
# It is explained at the guide you can find at www.theincompleteguide.com

from pathlib import Path
from datetime import datetime

MAX_WORKERS = 1 # max threads at a time

gainRatio = 1.5 # takeProfit = -stopLoss*gainRatio
stopLossMargin = 0.05 # extra margin for the stop loss

operEquity = 10000 # defines the target amount per execution
limitOrderMargin = 0.1# defines the offset for the limit orders

#### FILL THESE VALUES ###########################
API_KEY = "PKBZKMBSP448LVHFMOR7"
API_SECRET_KEY = "trhPOZxV8KeP3eiNRisqgdLSk3rR6hEv3JyvRu64"
ALPACA_API_URL = "https://paper-api.alpaca.markets"
#### FILL THESE VALUES ###########################

if API_KEY == "" or API_SECRET_KEY == "":
    print('\n\n #### Please get an API key at the Alpaca website! #### \n\n')
    raise ValueError

################################################################ ATTEMPTS ->
# max iteration attempts
maxAttempts = {
            'SO':5, # SUBMIT ORDER
            'CP':5, # CHECK POSITION
            'CO':5, # CANCEL ORDER
            'GP':5, # GET POSITION
            'FA':3, # FETCH ASSETS
            'LHD1':10, # LOAD HISTORICAL DATA 1
            'LHD2':20 # LOAD HISTORICAL DATA 2
            }

# limit for the indicators
limStoch = {
            'maxBuy':75, # max allowed value to buy
            'minSell':25  # min allowed value to sell
            }

################################################################ TIMEFRAMES ->
# fetch historical data intervals
fetchItval = {
            'little':'5Min',
            'big':'30Min'
            }

timeouts = {
        'operation':40*60*60, # main operation
        'posEntered':8*60*60, # position entered
        'GT':0 # if 0, it discards a bad general trend instantly
        }

# temps d'espera per a cada iteració
sleepTimes = {
                'operation':60,
                'GT': 10*60, # general trend
                'IT': 2*60, # instant trend
                'RS': 60, # RSI
                'FA': 3, # fetch assets
                'ST': 60, # stochastic cada minut
                'CO': 10, # check order cada 10 segons
                'SO': 5, # submit order cada 5 segons
                'LH': 5, # load_historical_data
                'PF': 10, # price fetch (current price)
                'CP': 10, # check position, a veure si ha entrat
                'GS': 60, # get slope dins d'enter position
                'UA': 10*60, # unlock assets
                'CL': 2
                }

################################################################ PATHS ->
home = str(Path.home())

FILES_FOLDER = home + '/tbot_files/'
RAW_ASSETS = './_raw_assets.csv'
LOGS_PATH = FILES_FOLDER + 'logs/'

################################################################ ASSET PARAMS ->
# filtering parameters at the asset handler
filterParams = {
    'MIN_SHARE_PRICE':30, #dòlars
    'MIN_AVG_VOL':0.5, #milions de dòlars
    }
