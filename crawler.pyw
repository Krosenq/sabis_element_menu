from datetime import datetime
from bs4 import BeautifulSoup as bs
import requests
import re


url = "https://www.sabis.se/element/dagens-lunch/"
selector = "#post-1368 > div > div > div.entry-body > div.lunch-data .lunch-day-container"

DAY_MAP = {
    0: "Måndag", 
    1: "Tisdag", 
    2: "Onsdag", 
    3: "Torsdag", 
    4: "Fredag", 
}

def weekday_string():
    return DAY_MAP[datetime.today().weekday()]

def today_string():
    return datetime.today().weekday()

def request_data(url, selector):

    req = requests.get(url)
    soup = bs(req.text, "html.parser")

    daily_menus = soup.select(selector)

    return daily_menus

def day_menu(daily_menus):
    # weekday = today_string()
    weekday = 3
    dishes = [dish.text.strip() for dish in daily_menus[weekday].select(".lunch-dish-description")]
    
    for i, dish in enumerate(dishes):
        dishes[i] = dish.replace('\n', ' ')
        
    return dishes

def bila_menu(daily_menus):
    weekday = today_string()

    if weekday != 4:
        reg_string = re.escape(DAY_MAP[weekday]) + r"</strong><br/>(.+)<br/><br/><strong>" + re.escape(DAY_MAP[weekday+1]) + r""
    else:
        reg_string = r"<strong>Fredag</strong><br/>(.+)</div>"

    dishes = re.findall(reg_string, str(daily_menus[0]))[0].replace(" <br/>", "<br/>").split("<br/>") 
    return dishes

def render_string(dishes_list):
    output_string = "".join([" "*2 + dish + " "*2  + "\n\n" for dish in dishes_list])
    return output_string
