from scraper import usd_scraper_banco_nacion, dai_prices_buenbit, dai_prices_tienda_dolar, usd_mep_prices_iol

def nacion_converter_str_to_float(dictionary:dict):
    """convert str to float

    param dictionary dict from func:usd_scraper_banco_nacion

    returns a list with floats
    """
    usd_list = []
    for x in dictionary.values():
       y = x.replace(',','.')
       y = float(y)
       usd_list.append(y)
    return usd_list 


def buenbit_converter_str_to_float(dictionary:dict):
    """convert str to float

    param dictionary dict from func: buenbit_converter_str_to_float

    returns a tuple with floats
    """
    bid = dictionary['purchase_price']
    ask = dictionary['selling_price']
    bid, ask = float(bid), float(ask)

    return bid, ask


def dolartienda_datos(dictionary:dict):
    """take a dict to returns a pair of keys as tuple

    param dictionary dict from func:dolartienda_datos

    returns a tuple with floats
    """
    bid = dictionary['sell']
    ask = dictionary['buy']

    return bid, ask


def run():
    #banco nacion
    lista = usd_scraper_banco_nacion()
    x = nacion_converter_str_to_float(lista)
    print(type(x))

    #tienda dolar
    usd_tuple = dai_prices_tienda_dolar()
    y_1, y_2 = dolartienda_datos(usd_tuple)
    print(y_1, y_2)

    #buenbit
    x = dai_prices_buenbit()
    x_1, x_2 = buenbit_converter_str_to_float(x)
    print(x_1, x_2)


if __name__=='__main__':
    run()