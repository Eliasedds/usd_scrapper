from funciones import *
import schedule
import tweepy
import time

def api_conection():
    CONSUMER_KEY = '5thI7IxIbU5bcW8o2TWlAYu3l'
    CONSUMER_SECRET = 'XBCPZqUeWfbI44O4YA9Q79rZpjN9rAAQmUikBJE4q9I667esL7'
    BEARER_TOKE = 'AAAAAAAAAAAAAAAAAAAAAEpuPgEAAAAA2ZnXdbapJI28AOVob%2B85h1GACQI%3DVqqk8AlIqJujx7OsuImPezegVPglIPJAlMU5dnpV3IW03zMfwo'
    ACCESS_TOKEN = '1136265079089971201-nTAsxcwpuB7IU0EPlLDyEyUqYvezKH'
    ACCESS_TOKEN_SECRET = 'RFWdNAzrfxQarPMgFpXLQB5pzwiE1yo4FiRzcRvyghUtJ'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    return api


def run():
    #Connecting to Twitter API
    api = api_conection()
    
    # Create a dict with data from the current requests
    dict_data = normalizer()
    df = df_creator(dict_data)
    new_df = append_df(df)
    print(new_df)

    #Take created dict to get values of the keys 'dolar' and 'last'
    brecha_list = list(df['brecha'])
    list_dolar, list_last = dict_data['dolar'], dict_data['last']
    dolar_type = generator(list_dolar)
    last_price = generator_float(list_last)
    brecha = generator_float(brecha_list)

    #Creating tweet
    api.update_status(f"""{next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}""")

    api.update_status(f"""{next(dolar_type).capitalize()} % {next(brecha)}
    {next(dolar_type).capitalize()} % {next(brecha)}
    {next(dolar_type).capitalize()} % {next(brecha)}
    {next(dolar_type).capitalize()} % {next(brecha)}
    {next(dolar_type).capitalize()} % {next(brecha)}
    {next(dolar_type).capitalize()} % {next(brecha)}
    {next(dolar_type).capitalize()} % {next(brecha)}
    {next(dolar_type).capitalize()} % {next(brecha)}""")
    


if __name__=='__main__':   
    schedule.every().hours.at(':21').until('17:23').do(run)
    while True:
        schedule.run_pending()
        time.sleep(1) 