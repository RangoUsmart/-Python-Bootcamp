import requests
import bs4

res = requests.get("http://www.example.com")
soup = bs4.BeautifulSoup(res.text,"lxml")

title_tag=soup.select('title')
res=title_tag[0].getText()
print(res)