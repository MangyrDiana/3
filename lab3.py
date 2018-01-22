from bs4 import BeautifulSoup
import requests

def news():
    soup = BeautifulSoup(requests.get("https://www.anews.com/").text, "html.parser") 

    for i in soup.find_all("div", ["news-item news-item_top-news","post-list","news-item news-item_default","widget-top__item"]):
        
        print("\n   \n") 

        annot = []

        for titles in i.find_all("a", ["news-item__link", "news-item__link news-item_top-news","widget-top__item-link"]):
            title = titles.get_text()
            print("Заголовок: ", title)

        for contents in i.find_all("div", "news-item__summary"):    
            content = contents.get_text()
            annot.append(content)  
        print('Аннотация:', annot)

news()