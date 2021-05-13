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
    api = api_conection()
    dict_data = normalizer()
    list_dolar, list_last = dict_data['dolar'], dict_data['last']
    dolar_type = generator(list_dolar)
    last_price = generator_float(list_last)
    api.update_status(f"""{next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}
    {next(dolar_type).capitalize()} $ {next(last_price)}""")



if __name__=='__main__':
    schedule.every(3).minutes().do(run)
    while True:
        schedule.run_pending()
        time.sleep(1)