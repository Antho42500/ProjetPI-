# -*- coding: utf-8 -*-
import sqlite3 as sq
import pandas as pd
import numpy as np
import matplotlib as plt

def import_data():
    connection=sq.connect("C:/Users/user/Downloads/trade_db.db")
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSBTC_12h ORDER BY Id DESC')
    rows1 = cursor.fetchall()
    EOSBTC12H=pd.DataFrame(rows1,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSBTC_14D ORDER BY Id DESC')
    rows2 = cursor.fetchall()
    EOSBTC14D=pd.DataFrame(rows2,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSBTC_15m ORDER BY Id DESC')
    rows3 = cursor.fetchall()
    EOSBTC15M=pd.DataFrame(rows3,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSBTC_1D ORDER BY Id DESC')
    rows4 = cursor.fetchall()
    EOSBTC1D=pd.DataFrame(rows4,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSBTC_1H ORDER BY Id DESC')
    rows5 = cursor.fetchall()
    EOSBTC1H=pd.DataFrame(rows5,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSBTC_1m ORDER BY Id DESC')
    rows6 = cursor.fetchall()
    EOSBTC1M=pd.DataFrame(rows6,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSBTC_30m ORDER BY Id DESC')
    rows7 = cursor.fetchall()
    EOSBTC30M=pd.DataFrame(rows7,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSBTC_3h ORDER BY Id DESC')
    rows8 = cursor.fetchall()
    EOSBTC13H=pd.DataFrame(rows8,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSBTC_5m ORDER BY Id DESC')
    rows9 = cursor.fetchall()
    EOSBTC5M=pd.DataFrame(rows9,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSBTC_6h ORDER BY Id DESC')
    rows10 = cursor.fetchall()
    EOSBTC6H=pd.DataFrame(rows10,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSBTC_7D ORDER BY Id DESC')
    rows11 = cursor.fetchall()
    EOSBTC7D=pd.DataFrame(rows11,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSETH_12h ORDER BY Id DESC')
    rows12 = cursor.fetchall()
    EOSETH12H=pd.DataFrame(rows12,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSETH_14D ORDER BY Id DESC')
    rows13 = cursor.fetchall()
    EOSETH14D=pd.DataFrame(rows13,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSETH_15m ORDER BY Id DESC')
    rows14 = cursor.fetchall()
    EOSETH15M=pd.DataFrame(rows14,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSETH_1D ORDER BY Id DESC')
    rows15 = cursor.fetchall()
    EOSETH1D=pd.DataFrame(rows15,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSETH_1h ORDER BY Id DESC')
    rows16 = cursor.fetchall()
    EOSETH1H=pd.DataFrame(rows16,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSETH_1m ORDER BY Id DESC')
    rows17 = cursor.fetchall()
    EOSETH1M=pd.DataFrame(rows17,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSETH_30m ORDER BY Id DESC')
    rows18 = cursor.fetchall()
    EOSETH30M=pd.DataFrame(rows18,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSETH_3h ORDER BY Id DESC')
    rows19 = cursor.fetchall()
    EOSETH3H=pd.DataFrame(rows19,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSETH_5m ORDER BY Id DESC')
    rows20 = cursor.fetchall()
    EOSETH5M=pd.DataFrame(rows20,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSETH_6h ORDER BY Id DESC')
    rows21 = cursor.fetchall()
    EOSETH6H=pd.DataFrame(rows21,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_EOSETH_7D ORDER BY Id DESC')
    rows22 = cursor.fetchall()
    EOSETH7D=pd.DataFrame(rows22,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_ETHBTC_12h ORDER BY Id DESC')
    rows23 = cursor.fetchall()
    ETHBTC12H=pd.DataFrame(rows23,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_ETHBTC_14D ORDER BY Id DESC')
    rows24 = cursor.fetchall()
    ETHBTC14D=pd.DataFrame(rows24,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_ETHBTC_15m ORDER BY Id DESC')
    rows25 = cursor.fetchall()
    ETHBTC15M=pd.DataFrame(rows25,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_ETHBTC_1D ORDER BY Id DESC')
    rows26 = cursor.fetchall()
    ETHBTC1D=pd.DataFrame(rows26,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_ETHBTC_1h ORDER BY Id DESC')
    rows27 = cursor.fetchall()
    ETHBTC1H=pd.DataFrame(rows27,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_ETHBTC_1m ORDER BY Id DESC')
    rows28 = cursor.fetchall()
    ETHBTC1M=pd.DataFrame(rows28,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_ETHBTC_30m ORDER BY Id DESC')
    rows29 = cursor.fetchall()
    ETHBTC30M=pd.DataFrame(rows29,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_ETHBTC_3h ORDER BY Id DESC')
    rows30 = cursor.fetchall()
    ETHBTC3H=pd.DataFrame(rows30,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_ETHBTC_5m ORDER BY Id DESC')
    rows31 = cursor.fetchall()
    ETHBTC5M=pd.DataFrame(rows31,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_ETHBTC_6h ORDER BY Id DESC')
    rows32 = cursor.fetchall()
    ETHBTC6H=pd.DataFrame(rows32,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_ETHBTC_7D ORDER BY Id DESC')
    rows33 = cursor.fetchall()
    ETHBTC7D=pd.DataFrame(rows33,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_LTCBTC_12h ORDER BY Id DESC')
    rows34 = cursor.fetchall()
    LTCBTC12H=pd.DataFrame(rows34,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_LTCBTC_14D ORDER BY Id DESC')
    rows35 = cursor.fetchall()
    LTCBTC14D=pd.DataFrame(rows35,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_LTCBTC_15m ORDER BY Id DESC')
    rows36 = cursor.fetchall()
    LTCBTC15M=pd.DataFrame(rows36,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_LTCBTC_1D ORDER BY Id DESC')
    rows37 = cursor.fetchall()
    LTCBTC1D=pd.DataFrame(rows37,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_LTCBTC_1h ORDER BY Id DESC')
    rows38 = cursor.fetchall()
    LTCBTC1H=pd.DataFrame(rows38,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_LTCBTC_1m ORDER BY Id DESC')
    rows39 = cursor.fetchall()
    LTCBTC1M=pd.DataFrame(rows39,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_LTCBTC_30m ORDER BY Id DESC')
    rows40 = cursor.fetchall()
    LTCBTC30M=pd.DataFrame(rows40,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_LTCBTC_3h ORDER BY Id DESC')
    rows41 = cursor.fetchall()
    LTCBTC3H=pd.DataFrame(rows41,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_LTCBTC_5m ORDER BY Id DESC')
    rows42 = cursor.fetchall()
    LTCBTC5M=pd.DataFrame(rows42,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_LTCBTC_6h ORDER BY Id DESC')
    rows43 = cursor.fetchall()
    LTCBTC6H=pd.DataFrame(rows43,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_LTCBTC_7D ORDER BY Id DESC')
    rows44 = cursor.fetchall()
    LTCBTC7D=pd.DataFrame(rows44,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_XRPBTC_12h ORDER BY Id DESC')
    rows45 = cursor.fetchall()
    XRPBTC12H=pd.DataFrame(rows45,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_XRPBTC_14D ORDER BY Id DESC')
    rows46 = cursor.fetchall()
    XRPBTC14D=pd.DataFrame(rows46,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_XRPBTC_15m ORDER BY Id DESC')
    rows47 = cursor.fetchall()
    XRPBTC15M=pd.DataFrame(rows47,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_XRPBTC_1D ORDER BY Id DESC')
    rows48 = cursor.fetchall()
    XRPBTC1D=pd.DataFrame(rows48,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_XRPBTC_1h ORDER BY Id DESC')
    rows49 = cursor.fetchall()
    XRPBTC1H=pd.DataFrame(rows49,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_XRPBTC_1m ORDER BY Id DESC')
    rows50 = cursor.fetchall()
    XRPBTC1M=pd.DataFrame(rows50,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_XRPBTC_30m ORDER BY Id DESC')
    rows51 = cursor.fetchall()
    XRPBTC30M=pd.DataFrame(rows51,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_XRPBTC_3h ORDER BY Id DESC')
    rows52 = cursor.fetchall()
    XRPBTC3H=pd.DataFrame(rows52,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_XRPBTC_5m ORDER BY Id DESC')
    rows53 = cursor.fetchall()
    XRPBTC5M=pd.DataFrame(rows53,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_XRPBTC_6h ORDER BY Id DESC')
    rows54 = cursor.fetchall()
    XRPBTC6H=pd.DataFrame(rows54,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    cursor.execute('SELECT * FROM Bitfinex_candle_XRPBTC_7D ORDER BY Id DESC')
    rows55 = cursor.fetchall()
    XRPBTC7D=pd.DataFrame(rows55,columns=['Id','date','high','low','open','close','volume','quotevolume','weightedaverage','sma_7','ema_7','sma_30','ema_30','sma_200','ema_20'] )
    print(EOSBTC12H.head())
    connection.close()
  
import_data()
EOSBTC12H['close'].plot(figsize=(11,7))
LTCBTC12H['close'].plot(figsize=(11,7))
LTCBTC1H['close'].plot(figsize=(11,7))

