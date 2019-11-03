
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import requests

#Pass the name of the player we want to search as a parameter
def scrape_data(name):
    #URL of the page we want to scrape (2019-2020 per game player stats)
    url = "https://www.basketball-reference.com/leagues/NBA_2020_per_game.html"

    #HTML from our URL
    html = urlopen(url)
    #Convert that HTML into an object
    soup = bs(html, 'html.parser')

    #Use findall() to get our headers
    soup.findAll('tr', limit = 2)

    #Extract the text so we can make a list
    headers = [th.getText() for th in soup.findAll('tr', limit = 2)[0].findAll('th')]
    #Exclude the first column, as we don't care about the ranking order from Basketball Reference
    headers = headers[1:]

    #Ignore the first header row
    rows = soup.findAll('tr')[1:]
    #Get the player's stats
    player_stats = [[td.getText() for td in rows[i].findAll('td')]for i in range(len(rows))]

    #Make our data frame
    stats = pd.DataFrame(player_stats, columns = headers)
    stats.head(10)

    #Convert it to a list so it is easier to use with HTML/Ajax/JS/etc
    doubleList = (stats[stats['Player'] == name]).values.tolist()

    #Our method above returns a list, within a list. This next method converts
    # it to a 'flat list'
    dataList = []
    for sublist in doubleList:
        for item in sublist:    
            dataList.append(item)
    return dataList

def data_headers():
    #URL of the page we want to scrape (2019-2020 per game player stats)
    url = "https://www.basketball-reference.com/leagues/NBA_2020_per_game.html"

    #HTML from our URL
    html = urlopen(url)

    #Convert that HTML into an object
    soup = bs(html, 'html.parser')

    #Use findall() to get our headers
    soup.findAll('tr', limit = 2)

    #Extract the text so we can make a list
    headers = [th.getText() for th in soup.findAll('tr', limit = 2)[0].findAll('th')]
    #Exclude the first column, as we don't care about the ranking order from Basketball Reference
    headers = headers[1:]
    return headers
