from bs4 import BeautifulSoup
import requests
import csv

'''
The task for my english class was to choose 20 confusables and find a sentence for each and every one of them. THat is 40 sentences. 
So i wrote script to scrape a news site for me. I used vox.com because it doesn't require subscription. 

The keywords in match_keywords method are the ones I was looking for. 

There are definitely limitations. I coded this within 30 minutes to quickly finish my work. 

TL.DR -->  Not all words were found, some words were found within wrong words; however, it scraped and did almost half of my work. I consider it worth the practice. Especially if the homework is not 
graded. 

Maybe some of this stuff can help you in your web scraping journey. 

Scrape from vox.com
'''

def collect_post_urls():
    urls = ["https://www.vox.com/the-highlight", "https://www.vox.com/", "https://www.vox.com/business-and-finance", "https://www.vox.com/world", "https://www.vox.com/the-goods","https://www.vox.com/policy-and-politics","https://www.vox.com/technology", "https://www.vox.com/future-perfect", "https://www.vox.com/recode","https://www.vox.com/even-better"]
    urls_to_send = []
    for url in urls:
        print(f"url to analyse {url}")
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        articles = soup.find_all("div", class_="l-segment")
        
        links = []
        for article in articles:
            list_elements = article.find_all('div', class_="c-compact-river__entry")
            for el in list_elements:
                links.append(el.find("a"))

        # print(links[0]['href'])

        # URLS to scrape separately. All are separate articles
        
        for link in links:
            urls_to_send.append(link['href'])
    print(len(urls_to_send))
    return urls_to_send



def match_keywords(urls):
    

    keywords = ["who", "whom", "wait for", "wait on", "ingenious", "ingenuous", "fewer", "less", "elicit", "illicit", "eminent", "imminent", "evnetually", "ultimately", "disinterested", "uninterested", "conscience", "conscious", "bad", "badly", "militate", "mitigate",
    "farther", "further", "epigram","epigraph", "disassociate", "dissociate","baklava", "balaclava", "blond", "blonde", "amok", "amuck", "anymore", "any more", "adverse", "averse", "aid", "aide" ]
    matched = 0
    rows = []
    for url in urls:
        content_page = requests.get(url)
        soup = BeautifulSoup(content_page.content, "html.parser")
        try:
            text = soup.find("main")
            paragraphs_section = text.find('div', class_="c-entry-content")

            # now find all the paragraphs

            paragraphs = paragraphs_section.find_all('p')

            for el in paragraphs:
                cont = el.text
                cont = cont.lower()
                # print(cont.lower())
                for keyword in keywords:
                    if keyword in cont:
                        # print(f"found a match keyword = {keyword} with index of {keywords.index(keyword)}")
                        matched += 1
                        # keywords.pop(keywords[keyword].index())
                        # print(f"keyword I matched {keywords.index(keyword)}")
                        index = keywords.index(keyword)
                        print(f"popping from the index {index} the keyword {keyword}")
                        keywords.pop(index)
                        row = (keyword, url)
                        rows.append(row)
                       

                       

        except:
            continue
    print(f"In total I matched: {matched} keywords")

        # writing to file

    # open the file in the write mode
    with open('web_scraping.csv', 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        
        for row in rows:
            # write a row to the csv file
            writer.writerow(row)
        row = keywords

        writer.writerow("Left:")
        writer.writerow(row)
        
    






if __name__ == "__main__":
    urls = collect_post_urls()
    match_keywords(urls)

