from bs4 import BeautifulSoup
import requests



response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()

data = response.text
soup = BeautifulSoup(data,'html.parser')
aritcles = soup.find_all(name='span',class_="titleline")
article_texts = []
article_links = []
article_votes = []
for topic in aritcles:
    article_texts.append(topic.getText())
    article_links.append(topic.find('a').get('href'))

article_vote = soup.find_all(name='span',class_='score')

for vote in article_vote:
    article_votes.append(vote.text.split(" ")[0])

# print(article_texts)
# print(article_links)
# print(article_votes)
each_article = []
for val in range(0,len(article_votes)):
    text = article_texts[val]
    link = article_links[val]
    vote = article_votes[val]
    tup = (text,link,vote)
    each_article.append(tup)
sort_artic = sorted(each_article,key= lambda x:x[2],reverse=True)
for x in range(3):
    print(f"Aricle heading: {sort_artic[x][0]}")
    print(f"Aricle Link: {sort_artic[x][1]}")
    print(f"Aricle votes: {sort_artic[x][2]}")









# with open("website.html",encoding="utf-8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents,'html.parser')
# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)
# for link in all_anchor_tags:
#     print(link.getText())
#     print(link.get('href'))
#     print(link.get('href'))
#
# # this selector use css selector method
# company_url = soup.select_one(selector="p a")
# print(company_url)