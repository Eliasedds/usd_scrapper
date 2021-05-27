from pandas.tseries.offsets import Minute, Second


def normalizer():
    """get different funcs to create a dict with normalized data

    returns a dict 
    """
    from .scraper import usd_scraper_banco_nacion, dai_prices_buenbit, dai_prices_tienda_dolar, usd_mep_prices_iol, usd_blue_scraper, last_price_iol
    from .conversores import nacion_converter_str_to_float, buenbit_converter_str_to_float, dolartienda_datos, dolarhoy_converter_str_to_float
    from datetime import datetime as dt_dt
    from datetime import date as dt_date
    from datetime import time as dt_t
    import numpy as np
    
    #getting data from "Banco Nación"
    dolares_nacion = usd_scraper_banco_nacion()
    nacion_billete_bid, nacion_billete_ask,nacion_divisa_bid, nacion_divisa_ask = nacion_converter_str_to_float(dolares_nacion)

    #getting "dolar solidario"
    dolar_solidario = round(nacion_billete_ask * 1.65, 2)

    #getting data from iol
    usd_dollars = usd_mep_prices_iol()
    bid_mep, ask_mep, bid_ccl, ask_ccl = usd_dollars
    last_ccl, last_mep = last_price_iol()

    #getting data from "Dolar Hoy"
    usd_blue = usd_blue_scraper()
    bid_blue, ask_blue = dolarhoy_converter_str_to_float(usd_blue)
    
    #getting data from "Tienda Dolar"
    tiendadolar = dai_prices_tienda_dolar()
    tiendadolar_dai_bid, tiendadolar_dai_ask = dolartienda_datos(tiendadolar)

    #getting data from "Buenbit"
    dai_buenbit = dai_prices_buenbit()
    buenbit_dai_bid, buenbit_dai_ask = buenbit_converter_str_to_float(dai_buenbit)

    # creating time and today to show when it was gotten the data
    now = dt_dt.now()
    hour, minute, second = now.hour, now.minute, now.second
    time = dt_t(hour=hour, minute=minute, second=second)
    today = dt_date.today()

    #a dict with the normalized data
    dict_data = {
        'dolar':['nacion_billete','nacion_divisa','solidario','dolar_blue','mep_48','ccl_48','tiendadolar_dai','buenbit_dai'],
        'bid':[nacion_billete_bid, nacion_divisa_bid, np.nan, bid_blue, bid_mep, bid_ccl, tiendadolar_dai_bid, buenbit_dai_bid],
        'ask':[nacion_billete_ask, nacion_divisa_ask, np.nan, ask_blue, ask_mep, ask_ccl, tiendadolar_dai_ask, buenbit_dai_ask],
        'last':[nacion_billete_ask, nacion_divisa_ask, dolar_solidario, ask_blue, last_mep, last_ccl, tiendadolar_dai_ask, buenbit_dai_ask],
        'time':[time, time, time, time, time, time, time, time],
        'date':[today, today, today, today, today, today, today, today]
    }

    return dict_data


def df_creator(dict_data:dict):
    """get a dict and creates Dataframe
    
    param dict_data dict from func:normalizer

    return <class 'pandas.core.frame.DataFrame'>
    """

    import pandas as pd
    df = pd.DataFrame(dict_data)
    df['brecha_%'] = round((df['last']/df['last'][0] - 1) * 100, 2)
    return df


def csv_creator(df_to_save):
    """Creates a DataFrame
    
    returns -
    """
    import pandas as pd
    df_to_save.to_csv('db.csv')


def append_df(df_to_append):
    """Take two df and returns a concatenated df

    param df_to_append DataFrame from func:df_creator

    returns a DataFrame
    """
    import pandas as pd
    df = pd.read_csv('db.csv')
    df = df.append(df_to_append)
    df = df.drop(['Unnamed: 0'], axis=1)
    df = df.reset_index(drop=True)
    df.to_csv('db.csv')
    return df

def run():
    dict_data = normalizer()
    df = df_creator(dict_data)
    print(df)
    # csv_creator(df)
    # df_n = append_df(df)
    # print(df_n)


if __name__=='__main__':
    run()