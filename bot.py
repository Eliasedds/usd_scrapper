from funciones import *
import schedule
import tweepy
import time

def api_conection():
    #Create CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
    CONSUMER_KEY = '----------------------------'
    CONSUMER_SECRET = '--------------------------'
    ACCESS_TOKEN = '--------------------------------------------------------------'
    ACCESS_TOKEN_SECRET = '---------------------------------------------------------'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
        print("Authentication OK")
        return api
    except:
        print("Error during authentication")


def run():
    #Connecting to Twitter API
    api = api_conection()
    
    # Create a dict with data from the current requests
    dict_data = normalizer()
    df = df_creator(dict_data)
    new_df = append_df(df)
    print(new_df)

    #Take created dict to get values of the keys 'dolar' and 'last'
    brecha_list = list(df['brecha_%'])
    list_dolar, list_last = dict_data['dolar'], dict_data['last']
    dolar_type = generator(list_dolar)
    dolar_type_1 = generator(list_dolar) #create a new generator
    last_price = generator_float(list_last)
    brecha = generator_float(brecha_list)

    #Creating tweet
    api.update_status(f"""Último precio
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    (1/2)""")

    api.update_status(f"""Brecha
    {next(dolar_type_1).capitalize()} % {next(brecha)}
    {next(dolar_type_1).capitalize()} % {next(brecha)}
    {next(dolar_type_1).capitalize()} % {next(brecha)}
    {next(dolar_type_1).capitalize()} % {next(brecha)}
    {next(dolar_type_1).capitalize()} % {next(brecha)}
    {next(dolar_type_1).capitalize()} % {next(brecha)}
    {next(dolar_type_1).capitalize()} % {next(brecha)}
    {next(dolar_type_1).capitalize()} % {next(brecha)}
    (2/2)""")
    


if __name__=='__main__':   
    schedule.every().hours.at(':21').until('17:23').do(run)
    while True:
        schedule.run_pending()
        time.sleep(1) 