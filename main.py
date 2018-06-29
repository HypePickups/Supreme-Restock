import requests
from bs4 import BeautifulSoup
import playsound
import os 
from os.path import expanduser


Item_name = input('item name: ') #make sure to spell exacly simular to text (mona lisa tee = No) (Mona Lisa Tee = Yes) etc..
Category = input('category: ') #could add in code to find catagory automatically but dont have the time (you do it if you want lol)

User = expanduser("~")

r = requests.get('http://www.supremenewyork.com/shop/all/'+ (Category))
soup = BeautifulSoup(r.text, 'lxml')

thetable = soup.find('div', class_='turbolink_scroller')
items = thetable.find_all('div', class_='inner-article')

def availability():
    for item in items:
        #alt = item.find('img', alt=(Item_code)) ---- IF YOU ONLY WANT ONE COLOUR USE THIS CODE INSTEAD OF item.name and replace all the item.names below with alt
        name = item.h1.a
        item.name = item.find('a', text=(Item_name))
        color = item.p.a.text
        sold = item.div
        if Item_name == (None):
            pass

        #If Item restocks
        if sold == (None) and item.name != (None):
            print(name, '-', color, '-', 'is in stock')
            #plays sound when item restocks so you can focus on other things with this in the backround
            playsound.playsound((User)+'/Desktop/Lebron_James_Vine.mp3', True) #choose whatever audio file you wish and change name and location

        #If still sold out
        if sold and item.name != (None):
            print(Item_name, '-', color, '-', 'is not in stock')

#Infinite loop will play audio repeatedly (can add in once in stock stop)
while 5>4:
    availability()

