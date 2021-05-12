def usd_scraper_banco_nacion():    
    """ Scrap on the 'banco nacion' website
    on the indicated node

    returns dict with usd values
    """
    import requests
    import lxml.html as html
    
    try:
        response = requests.get('https://www.bna.com.ar/Personas')
        if response.status_code == 200:
            currency = response.content.decode('utf-8')
            parsed = html.fromstring(currency)

            usd_price = parsed.xpath('//table[@class="table cotizacion"]/tbody/tr[1]/td[not(@class)]/text()')
            dict_usd = {
                'usd_billete_compra':usd_price[0],'usd_billete_venta':usd_price[1],
            'usd_divisa_compra':usd_price[2],'usd_divisa_venta':usd_price[3]  
            }
            return dict_usd

    except ValueError as ve:
        print(ve)


def dai_prices_tienda_dolar():
    """get .json from url
   
    returns a dict
    """
    import requests

    try:
        response = requests.get('https://api.tiendadolar.com.ar/api/v2/price/coins')
        if response.status_code == 200:
            currency = response.json()
            currency = currency[0]

            return currency
    except ValueError as ve:
        print(ve)


def dai_prices_buenbit():
    """get .json from url

    returns a dict
    """
    import requests

    try:
        response = requests.get('https://be.buenbit.com/api/market/tickers/')
        if response.status_code == 200:
            currency = response.json()
            currency = currency['object']['daiars']
            
            return currency
    except ValueError as ve:
        print(ve)


def usd_mep_prices_iol():
    import pandas as pd

    bid_mep, ask_mep = pd.read_html("https://www.invertironline.com/mercado/cotizaciones/argentina/monedas",thousands=".", decimal=',')[0].iloc[2][1:3]
    bid_ccl, ask_ccl = pd.read_html("https://www.invertironline.com/mercado/cotizaciones/argentina/monedas",thousands=".", decimal=',')[0].iloc[3][1:3]
    
    return bid_mep, ask_mep, bid_ccl, ask_ccl


def run():
    dict_usd = usd_scraper_banco_nacion()
    print(dict_usd)
    dict_usd = dai_prices_tienda_dolar()
    print(dict_usd)
    usd_tuple = dai_prices_buenbit()
    print(usd_tuple)
    usd_iol = usd_mep_prices_iol()
    print(usd_iol)

if __name__=='__main__':
    run()
