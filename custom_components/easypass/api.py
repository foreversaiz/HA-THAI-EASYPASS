import re
import time
import requests
from bs4 import BeautifulSoup

import logging

EASYPASS_LOGIN_URL = 'https://www.thaieasypass.com/th/member/login'
EASYPASS_SIGNIN_URL = 'https://www.thaieasypass.com/th/member/signin'
EASYPASS_URL = 'https://www.thaieasypass.com/th/easypass/smartcard'

REFRESH_SEC = 120  # will be over writen if refresh in meta content is higher
MAX_CONNECTION = 50
MIN_CONTENT_SIZE = 2000  # for check if no data return even 50with status_code 200
MAX_CONNECTION_USED = MAX_CONNECTION - 1

_LOGGER = logging.getLogger("easypass_api")


TIMEZONE = 'Asia/Bangkok'
DATETIME_FORMAT = '%Y/%m/%dT%H:%M:%S%z'  # ISO 8601
EASYPASS_RETRY_WAIT_SEC = 300

class LoginEasyPass:

    def login_easypass(session,login):
        #_LOGGER.info(login)
        session.get(EASYPASS_LOGIN_URL)
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = f"email={login["username"]}&password={login["password"]}"
        session.post(EASYPASS_SIGNIN_URL, data=payload, headers=headers)

    
    def get_response(session, url, min_cont_size=MIN_CONTENT_SIZE):
        global REFRESH_SEC
        result = None
        try:
            response = session.get(url)
            if response.status_code != 200 or int(response.headers['Content-Length']) < min_cont_size:
                if response != 200:
                    print(f'Response status is {response.status_code}')
                LoginEasyPass.login_easypass(session)
            else:
                match = re.search(r'timeout=(\d+)', response.headers["Keep-Alive"])
                if match:
                    timeout = int(match[1])
                    match = re.search(r'max=(\d+)', response.headers["Keep-Alive"])
                    if match:
                        connection_left = int(match[1])
                        if connection_left < MAX_CONNECTION_USED:
                            time.sleep(timeout * 2)
                match = re.search(r'refresh.*\b(\d+)\b', response.content.decode('UTF-8'))
                if match:
                    refresh = int(match[1])
                    if refresh > REFRESH_SEC:
                        REFRESH_SEC = refresh
                result = response
        except Exception as err:
            time.sleep(EASYPASS_RETRY_WAIT_SEC)
        return result

    def get_easypass(session):
        results = []
        response = LoginEasyPass.get_response(session, EASYPASS_URL)
        #print(response)
        try:
            if response:
                soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
                table = soup.find("table")
                #print(table)
                headers = [header.text.strip() for header in
                        table.find('tr', class_='head-table').find_all('td')]
                for row in table.find_all('tr'):
                    if 'head-table' in row.get('class', []):
                        continue
                    row_dict = {headers[i]: cell.text.strip() for i, cell in enumerate(row.find_all('td'))}
                    results.append(row_dict)
                #logger.info("%s", results)
                _LOGGER.info(results)
            return results
        except:
            return "Login Failed"        




