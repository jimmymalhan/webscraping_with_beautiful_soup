from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
# print(soup.body)
# print(soup.head)
# print(soup.head.title)

# el = soup.find('div')
# el = soup.find_all('div')[1]

# el = soup.find(id='section-1')
# el = soup.find(class_='items')
# el = soup.find(attrs={"data-hello":"hi"})

# el = soup.select('#section-1')
# el = soup.select('#section-1')[0]
# el = soup.select('.item')[0]


# get_text()
# el = soup.find(class_='item').get_text()
# for item in soup.select('.item'):
#     print(item.get_text())


# Navigation
# el = soup.body.contents[1].contents[0].find_next_sibling()
# el = soup.find(id='section-2').find_previous_sibling()
# el = soup.find(class_='item').find_parent()
# el = soup.find('h3').find_next_sibling('p')


# print(el)