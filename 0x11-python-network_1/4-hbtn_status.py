#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == "__main__":
    import requests

    r = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print(f'\t- type: {type(response.text)}')
    print(f'\t- content: {response.text}')
