import requests
import bs4

url = "https://www.jdsports.ie/men/mens-clothing/track-pants/"
# agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
response = requests.get(url)
page = bs4.BeautifulSoup(response.content, "html5lib")

print(page.title)
