import requests
import tkinter as tk


global textctrl
API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = '3805f6bbabcb42b3a0c08a489baf603d'
api_endpoint = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"

def GetArticle(txtctl):
    textctrl = txtctl
    params = {
        "country": "us",
        "apiKey": API_KEY
    }
    # call Fetch_and_print_Article.py to get data
        # call Fn below to get data
    data = fetch_and_print_articles(API_URL, API_KEY,textctrl)
    #for sel in selarts:
    #    textctrl.insert(tk.END, f'Columns: {sel}\n')
    startpos = 0
    fullbuff = str(data)
    while True:
        # parse the entries and extract just the 'description' entries
        tmpstart = fullbuff.find("'description': \"", startpos, len(fullbuff)-startpos)
        para = fullbuff[tmpstart+16: len(fullbuff) - (tmpstart + 1) ]
        ends = para.find('\"')
        if ends == -1:
            fullbuff = para
        else:
            fullbuff = para[ends:]
        para = para[0:ends - 1]
        textctrl.insert(tk.END, para+ '\n')
        if len(fullbuff) <= 0:
            break
    #except Exception as e:
    #    print(f"An error occurred: {e}")

################################################################
## Call API to get a sleectigon of news articles from NEWSAPI ##
################################################################
def fetch_and_print_articles(api_url,API_KEY, textctrl):
    # Parameters for the API request
    params = {
        "country": "us",
        "apiKey": API_KEY
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        selarts = []
        articles = response.json().get('articles', [])
        textctrl.insert(tk.END, f'\nBBC News Headslines API feed:\nThere are {len(articles)} articles as shown below...\n\n')

        #for index, article in enumerate(articles[:1], start=1):
        #    entry = article

        # print 5 from the list of articles received
        notavailable=0
        print(f"BBC NEWS FEED: Fetching current articles...\n")

        for index, article in enumerate(articles[0:len(articles)], start=0):
            str = article['content']
            if str == '[Removed]':
                textctrl.insert(tk.END, f'\n[{index+1}] Removed from feed\n')
                notavailable += 1
                continue
            if str == None:
                textctrl.insert(tk.END, f'\n[{index + 1}] No longer available in feed\n')
                notavailable += 1
                continue
            if len(str) == 0:
                textctrl.insert(tk.END, f'\n[{index + 1}] No longer available in feed\n')
                notavailable += 1
                continue
            if str[len(str):] != '\n':
                textctrl.insert(tk.END, f'\n[{index + 1}] {str}\n\n')
            else:
                textctrl.insert(tk.END, f'\n[{index+1}] {str}\n')
        print(f"BBC NEWS FEED OUTPUT COMPLETED SUCCESSFULLY...\n")
        textctrl.insert(tk.END, f"\nBBC [{len(articles) - notavailable}/{len(articles)}] available NEWS FEED OUTPUT COMPLETED SUCCESSFULLY...\n")



def fetch_and_print_localbusiness(api_url,API_KEY, textctrl):
    # Parameters for the API request
    params = {
        "country": "us",
        "apiKey": "x-rapidapi-key:acbd8df680msh98e357e9edc3004p165757jsnb18cf7474e7e"
    }
    api_url = "http GET 'https://local-business-data.p.rapidapi.com/search-nearby?query=plumbers&lat=37.359428&lng=-121.925337&limit=20&language=en&region=us' "
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        selarts = []
        articles = response.json().get('articles', [])
        textctrl.insert(tk.END, f'\n-----------------------------\n')
        textctrl.insert(tk.END, f'\nBBC News Headslines API feed:\nThere are {len(articles)} articles as shown below...\n\n')
        textctrl.insert(tk.END, f'\n-----------------------------\n')

        #for index, article in enumerate(articles[:1], start=1):
        #    entry = article

        # print 5 from the list of articles received
        notavailable=0
        for index, article in enumerate(articles[0:len(articles)], start=0):
           #try:
            str = article['content']
            print(str)
            if str == '[Removed]':
                textctrl.insert(tk.END, f'\n[{index+1}] Removed from feed\n')
                notavailable += 1
                continue
            if str == None:
                textctrl.insert(tk.END, f'\n[{index + 1}] No longer available in feed\n')
                notavailable += 1
                continue
            if len(str) == 0:
                textctrl.insert(tk.END, f'\n[{index + 1}] No longer available in feed\n')
                notavailable += 1
                continue
            if str[len(str):] != '\n':
                print(str[len(str):])
                textctrl.insert(tk.END, f'\n[{index + 1}] {str}\n\n')
            else:
                textctrl.insert(tk.END, f'\n[{index+1}] {str}\n')
        print(f"BBC NEWS FEED OUTPUT COMPLETED SUCCESSFULLY...\n")
        textctrl.insert(tk.END, f"\nBBC [{len(articles) - notavailable}/{len(articles)}] available NEWS FEED OUTPUT COMPLETED SUCCESSFULLY...\n")
