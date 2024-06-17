import json
import requests


def main():
    API_URL = "https://newsapi.org/v2/top-headlines"
    response = requests.get(API_URL)

    if response.status_code == 200:
        articles = response.json().get('articles', [])

        #for index, article in enumerate(articles[:3], start=1):
        #    print(f"Article {index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n")
        return articles
    else:
        print(f"Error: {response.status_code}")

def jprint(obj):
    print(json.dumps(obj, sort_keys=True, indent=4))

if __name__ == "__main__":
    print('in "if __'
          'name__ == __main__()')
    #args = sys.argv[1:]
    #fetch_and_print_articles("https://newsapi.org/v2/top-headlines")
    main()
