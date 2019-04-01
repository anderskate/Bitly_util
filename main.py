import requests
from dotenv import load_dotenv
import os
import sys
import argparse
    
def shorten_link(url):
    params = {"long_url": url}
    response_from_site = get_response('https://api-ssl.bitly.com/v4/shorten', params, post=True)

    return response_from_site.json()

def get_transitions_amount(url):
    params = {"units": -1}
    response_from_site = get_response('https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(url), params)

    return response_from_site.text

def get_response(url, params, post=False):
    payload = {"Authorization": "Bearer " + os.getenv("TOKEN")}

    if post:
        response = requests.post(url, headers=payload, json=params)
    else:
        response = requests.get(url, headers=payload, params=params)

    return response

def check_for_a_short_link(url):
    params = {"q":""}
    url_without_http = url.split("//")[1]
    response_from_site = get_response('https://api-ssl.bitly.com/v4/bitlinks/{}'.format(url_without_http), params)

    return response_from_site.ok

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='Данная программа сокращает ссылки.')
    parser.add_argument('link', help='Ссылка для сокращения')
    args = parser.parse_args()
    user_url = args.link

    response = requests.get(user_url)

    if not response.ok:
        sys.exit('Вы ввели некорректную ссылку!')

    if check_for_a_short_link(user_url):
        url_without_http = user_url.split("//")[1]
        transitions_amount = get_transitions_amount(url_without_http)
        print(transitions_amount)
    else:
        short_link = shorten_link(user_url)
        print(short_link)

if __name__ == '__main__':
    main()
