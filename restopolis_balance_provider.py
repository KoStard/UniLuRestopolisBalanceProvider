# A small script to get the balance of your Restopolis card
# To use it, you need to set the environment variables RESTOPOLIS_USERNAME and RESTOPOLIS_PASSWORD
# with your Uni.lu username and password
# You can then run the script with `python script.py`

import requests
import requests_ntlm
import os
from bs4 import BeautifulSoup


def get_restopolis_balance(username, password):
    # Set the URL of the API endpoint
    url = 'https://inscription.uni.lu/Inscriptions/Student/GuichetEtudiant/CarteRestopolis'

    # Create a requests session and set the auth parameter to NTLM with your credentials
    with requests.Session() as session:
        session.auth = requests_ntlm.HttpNtlmAuth(username, password)
        response = session.get(url)

    if response.status_code != 200:
        print('Error: ' + str(response.status_code) + ' ' + response.reason)
        return

    # Print the response
    response_body = response.text
    soup = BeautifulSoup(response_body, 'html.parser')
    my_span = soup.find('div', {'id': 'myCard'}) \
        .find('div') \
        .find('div') \
        .find('div') \
        .find('div', {'class': 'col'}) \
        .find('span')
    balance = my_span.get_text()
    return balance


if __name__ == '__main__':
    print(
        get_restopolis_balance(os.environ['RESTOPOLIS_USERNAME'],
                               os.environ['RESTOPOLIS_PASSWORD']))
