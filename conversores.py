from scraper import usd_scraper_banco_nacion, dai_prices_buenbit, dai_prices_tienda_dolar, usd_mep_prices_iol

def nacion_converter_str_to_float(diccionario):
    lista = []
    coma = ','
    punto = '.'
    for x in diccionario.values():
       y = x.replace(',','.')
       y = float(y)
       lista.append(y)
    return lista 


def buenbit_converter_str_to_float(diccionario):
    y = diccionario['purchase_price']
    y_1 = diccionario['selling_price']
    y, y_1 = float(y), float(y_1)

    return y, y_1


def dolartienda_datos(diccionario):
    ask = diccionario['sell']
    bid = diccionario['buy']

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