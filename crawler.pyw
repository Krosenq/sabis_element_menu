from datetime import datetime
from bs4 import BeautifulSoup as bs
import requests


url = "https://www.sabis.se/element/dagens-lunch/"
selector = "#post-1368 > div > div > div.entry-body > div.lunch-data .lunch-day-container"

def today_string():
    return datetime.today().weekday()

def request_data(url, selector):

    req = requests.get(url)
    soup = bs(req.text, "html.parser")

    daily_menus = soup.select(selector)

    return daily_menus

def day_menu(daily_menus):
    weekday = today_string()

    dishes = [dish.text.strip() for dish in daily_menus[weekday].select(".lunch-dish-description")]
    
    for i, dish in enumerate(dishes):
        dishes[i] = dish.replace('\n', ' ')
        
    return dishes

def render_string(dishes_list):
    output_string = "".join([" "*2 + dish + " "*2  + "\n\n" for dish in dishes_list])
    return output_string
