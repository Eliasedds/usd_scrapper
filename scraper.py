import requests
import lxml.html as html

URL_HOME_BANCO_NACION = 'https://www.bna.com.ar/Personas'
XPATH_NACION = '//table[@class="table cotizacion"]/tbody/tr[1]/td[not(@class)]/text()'

def usd_scraper_banco_nacion(url:int, xpath:int):    
    """ Scrap on the banco nacion website
    on the indicated node

    param str url banco nacion url
    param str xpath node to scrap
    
    returns dict with usd values
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            currency = response.content.decode('utf-8')
            parsed = html.fromstring(currency)

            usd_price = parsed.xpath(xpath)
            dict_usd = {
                'usd_billete_compra':usd_price[0],'usd_billete_venta':usd_price[1],
            'usd_divisa_compra':usd_price[2],'usd_divisa_venta':usd_price[3]  
            }
            return dict_usd

    except ValueError as ve:
        print(ve)

def run():
    dict_usd = usd_scraper_banco_nacion(URL_HOME_BANCO_NACION, XPATH_NACION)
    print(dict_usd)

if __name__=='__main__':
    run()
