import logging
import random

import requests

from .api import LoginEasyPass


class EasyPassInstance:
    def __init__(self, value: str) -> None:
        self._sensor = value
        self._attr_native_value = None

    @property
    def value(self):
        self._offset = self._sensor["offset"]
        self._offset = int(self._offset) - 1
        with requests.session() as session:
            LoginEasyPass.login_easypass(session, self._sensor)
            cards = LoginEasyPass.get_easypass(session)
            if cards == "Login Failed":
                return cards, ""
            else:
                try:
                    attr = []
                    attr = {
                        "ทะเบียนรถ": cards[self._offset]["ทะเบียนรถ"],
                        "เลขสมาร์ทการ์ด": cards[self._offset]["เลขสมาร์ทการ์ด (S/N)"],
                    }
                    balance_value = cards[self._offset]["จำนวนเงิน"]
                    balance_value = balance_value.replace(",", "")
                    return balance_value, attr
                except:
                    length = len(cards)
                    attr = []
                    # attr = { "offset": self._sensor["offset"], "ควรตั้งoffsetเป็น": length}
                    balance_value = cards[0]["จำนวนเงิน"]
                    balance_value = balance_value.replace(",", "")
                    attr = {
                        "license_plate": cards[0]["ทะเบียนรถ"],
                        "balance": balance_value,
                        "smartcard": cards[0]["เลขสมาร์ทการ์ด (S/N)"],
                    }
                    return cards, attr
