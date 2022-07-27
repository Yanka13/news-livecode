# main.py
from client import News

def main():
    choice = input("Country headlines [default] or Search [hit s]?\n> ")
    print(choice)
    news = News()
    if choice == "s":
        keyword = input("What are you looking for?\n> ")
        articles = news.search_keyword(keyword)
        for article in articles:
            print(f"- {article['title']}. url: {article['url']}" )
    else:
        articles_france = news.top_headlines("fr")
        for article in articles_france:
            print(f"- {article['title']}. url: {article['url']}" )



if __name__ == '__main__':
    main()
