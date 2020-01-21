import requests
import pprint
import re

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


class CtripHotel(object):

    @staticmethod
    def city_code()->dict:
        data = {}
        city_code_source = 'https://hotels.ctrip.com/international/Tool/citySource_J.aspx?charset=utf-8'
        city_codes = requests.get(url=city_code_source, headers=header).text

        for info in re.findall('\|.{0,10}\|city\|[0-9]+\|.+?\|', city_codes):
            data[info.split('|')[1]] = info.split('|')[4] + info.split('|')[3]
        return data


class Action(object):
    """
    我就是命名空间
    """

    @staticmethod
    def check_city_code():
        pprint.pprint(CtripHotel.city_code())


def run():
    Action.check_city_code()


if __name__ == '__main__':
    run()
