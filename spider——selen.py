from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def ChromeDriverNOBrowser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driverChrome = webdriver.Chrome(chrome_options=chrome_options)
    return driverChrome


url = 'https://hotels.ctrip.com/international/mombasa818'


def get_trip_info(url):

    wb = ChromeDriverNOBrowser()
    wb.get(url)
    while not wb.find_elements_by_css_selector(".J_hlist_item.hlist_item"):
        pass
    divs = wb.find_elements_by_css_selector(".J_hlist_item.hlist_item")

    for div in divs:

        id = div.get_attribute('id')
        name = wb.find_element_by_xpath(f'//*[@id={id}]/div/div[3]/div[1]/a').text
        try:
            price = wb.find_element_by_xpath(f'//*[@id="{id}"]/div/div[5]/a/div[1]/div/span').text
        except:

            price = wb.find_element_by_xpath(f'//*[@id="{id}"]/div/div[6]/a/div[1]/div/span').text

        print(name, price)


if __name__ == '__main__':
    get_trip_info(url)
