from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_text = response.text


soup = BeautifulSoup(yc_web_text, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.find(name="a").get("href")
    article_links.append(link)
article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_scores)


highest_scoring_article = article_scores.index(max(article_scores))
#print(highest_scoring_article)
print(f"Highest scoring article: {article_texts[highest_scoring_article]}.\n"
      f"Link of said article: {article_links[highest_scoring_article]}.\n"
      f"Score of said article: {article_scores[highest_scoring_article]}")
