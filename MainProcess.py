from ctrip_hot_hotel import CtripHotel
from spider_selen import get_trip_info
from spider_selen import ChromeDriverNOBrowser
import pandas as pd
import datetime

doc = pd.DataFrame(columns=['city','hotel','shown_price'])
wb  = ChromeDriverNOBrowser()
for x,y in CtripHotel.city_code().items():
    city = [x]
    for info in get_trip_info(wb,y):
        line = city + info
        print(line)
        doc.loc[len(doc)]=line
today = (datetime.datetime.today()).strftime('%Y-%m-%d')
doc.to_excel(f'CtripHotelPrice{today}.xlsx')