from pandas.tseries.offsets import Minute, Second


def normalizer():
    from scraper import usd_scraper_banco_nacion, dai_prices_buenbit, dai_prices_tienda_dolar, usd_mep_prices_iol
    from conversores import nacion_converter_str_to_float, buenbit_converter_str_to_float, dolartienda_datos
    from datetime import datetime as dt_dt
    from datetime import date as dt_date
    from datetime import time as dt_t
    
    
    dolares_nacion = usd_scraper_banco_nacion()
    nacion_billete_bid, nacion_billete_ask,nacion_divisa_bid, nacion_divisa_ask = nacion_converter_str_to_float(dolares_nacion)

    tiendadolar = dai_prices_tienda_dolar()
    tiendadolar_dai_ask, tiendadolar_dai_bid = dolartienda_datos(tiendadolar)

    dai_buenbit = dai_prices_buenbit()
    buenbit_dai_bid, buenbit_dai_ask = buenbit_converter_str_to_float(dai_buenbit)

    usd_dollars = usd_mep_prices_iol()
    bid_mep, ask_mep, bid_ccl, ask_ccl = usd_dollars

    now = dt_dt.now()
    hour, minute, second = now.hour, now.minute, now.second
    time = dt_t(hour=hour, minute=minute, second=second)
    today = dt_date.today()

    dict_data = {
        'dolar':['nacion_billete','nacion_divisa','tiendadolar_dai','buenbit_dai','mep_48','ccl_48'],
        'bid':[nacion_billete_bid, nacion_billete_ask, tiendadolar_dai_bid, buenbit_dai_bid, bid_mep, bid_ccl],
        'ask':[nacion_divisa_bid, nacion_divisa_ask, tiendadolar_dai_ask, buenbit_dai_ask, ask_mep, ask_ccl],
        'last':[nacion_billete_bid, nacion_billete_ask, tiendadolar_dai_ask, buenbit_dai_ask, ask_mep, ask_ccl],
        'time':[time, time, time, time, time, time],
        'date':[today, today, today, today, today, today]
    }

    return dict_data


def df_creator(dict_data:dict):
    import pandas as pd
    df = pd.DataFrame(dict_data)
    return df


def csv_creator(df_to_save):
    import pandas as pd
    df_to_save.to_csv('db.csv')


def x(df_agg):
    import pandas as pd
    df = pd.read_csv('db.csv')
    df = df.append(df_agg)
    df = df.drop(['Unnamed: 0'], axis=1)
    df = df.reset_index(drop=True)
    df.to_csv('db.csv')
    return df

def run():
    dict_data = normalizer()
    df = df_creator(dict_data)
    print(df.columns)
    # csv_creator(df)
    df_n = x(df)
    print(df_n)


if __name__=='__main__':
    run()