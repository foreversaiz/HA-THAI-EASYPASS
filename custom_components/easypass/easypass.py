import logging
import random
from .api import LoginEasyPass
import requests



class EasyPassInstance:


    def __init__(self, value: str) -> None:
        self._sensor = value
        self._attr_native_value = None

    @property
    def value(self):
        self._offset = self._sensor["offset"] 
        self._offset = int(self._offset) - 1
        with requests.session() as session:
            LoginEasyPass.login_easypass(session,self._sensor)
            cards = LoginEasyPass.get_easypass(session)
            if cards == "Login Failed" :
                return cards , ""
            else :
                try:
                    attr = []
                    attr = { "ทะเบียนรถ": cards[self._offset]['ทะเบียนรถ'], "เลขสมาร์ทการ์ด": cards[self._offset]['เลขสมาร์ทการ์ด (S/N)']}
                    return cards[self._offset]['จำนวนเงิน'] , attr
                except:
                    length = len(cards)
                    attr = []
                    attr = { "offset": self._sensor["offset"], "ควรตั้งoffsetเป็น": length}
                    return cards , attr
        







