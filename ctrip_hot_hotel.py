import requests
import pprint
import re

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}


class CtripHotel(object):

    @staticmethod
    def city_code():
        data = {}
        city_code_source = 'https://hotels.ctrip.com/international/Tool/citySource_J.aspx?charset=utf-8'
        city_codes = requests.get(url=city_code_source,headers=header).text
        print(city_codes)
        for info in re.findall('\|.{0,10}\|city\|[0-9]+\|.+?\|', city_codes):
            data[info.split('|')[1]] = info.split('|')[4] + info.split('|')[3]
        return data

    @staticmethod
    def get_hotel_city_index_ajax():
        data={
            'checkIn': '2020 - 02 - 03',
            'checkOut': '2020 - 02 - 04',
            'destinationType': '1',
            'IsSuperiorCity': '1',
            'cityId': '338',
            'cityPY': 'london',
            'rooms': '2',
            'childNum': '2',
            'roomQuantity': '1',
            'pageIndex': '1'
        }
        res = requests.put(url='https://hotels.ctrip.com/international/tool/AjaxHotelList.aspx',data=data,headers=header)
        print(res.text)
class Action(object):
    """
    我就是命名空间
    """

    @staticmethod
    def check_city_code():
        pprint.pprint(CtripHotel.city_code())


def run():
    Action.check_city_code()
    # CtripHotel.get_hotel_city_index_ajax()

if __name__ == '__main__':
    run()
