from bs4 import BeautifulSoup

with open('index.html') as file:
    soup = BeautifulSoup(file, "html.parser")

ids = range(180, 12654)

for i in ids:
    myClass = "ft{}".format(i)
    data = soup.find('p', class_ = myClass )
    if data is not None:
        print(data.get_text())    

