import requests
import bs4
url="http://quotes.toscrape.com/"
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text,"lxml")

author_class = soup.select('.author')

for item in author_class:
    # print(item.text)
    pass
    
quotes_list = [quote.text for quote in soup.select(".text")]
for item in quotes_list:
    # print(item)
    pass

for item in soup.select(".tag-item"):
    # print(item.text)
    pass

'''
TASK: Notice how there is more than one page,
and subsequent pages look like this http://quotes.toscrape.com/page/2/.
Use what you know about for loops and string concatenation to loop through all the pages 
and get all the unique authors on the website. Keep in mind there are 
many ways to achieve this, also note that you will need to somehow 
figure out how to check that your loop is on the last page with quotes. 
For debugging purposes, I will let you know that there are only 10 pages, so the last page 
is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust enough that
it wouldn't matter to know the amount of
pages beforehand, perhaps use try/except for this, its up to you!
'''
page_url = 'http://quotes.toscrape.com/page/{}/'
test_text="No quotes found!"
authors = set()
page_number = 1
# Obtain Request
while True:
    response = requests.get(page_url.format(page_number))
    if response.status_code != 200:
        break

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    
    # Знайдемо усіх авторів на поточній сторінці та додамо їх до множини
    current_page_authors = soup.find_all('small', class_='author')
    for author in current_page_authors:
        authors.add(author.get_text())

    # Перевіримо наявність кнопки "Next"
    next_button = soup.find('li', class_='next')
    if not next_button:
        break
    
    # Якщо кнопка "Next" є, перехід на наступну сторінку
    page_number += 1

# Виведемо усіх унікальних авторів
for author in authors:
    print(author)