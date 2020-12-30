from urllib.request import urlopen
from bs4 import BeautifulSoup

nameBook = input("Nome do livro que você procura: ")
languages = int(input("\nIdiomas Disponiveis:\n1 - Portugues      2 - English\nEscolha:"))
langPort = '/?e=1&language=portuguese'
langEng = '?e=1&language=english'
urlBase = 'https://pt.b-ok.lat'
nameDivided = nameBook.split(" ")
sizeName = len(nameDivided)
nameHTML = ''
if sizeName > 1 :
    for i in range(0, sizeName):
        nameHTML += nameDivided[i] + '%20'
else:
    nameHTML = nameDivided[0]

if languages == 1:
    urlComplete = urlBase + '/s/' + nameHTML + langPort
elif languages == 2:
    urlComplete = urlBase + '/s/' + nameHTML + langEng

htmlOpen = urlopen(urlComplete)
bs = BeautifulSoup(htmlOpen, 'lxml')
findResults = bs.find_all('h3')
print('Link:', urlComplete)
print("\nExistem {} resultados para a sua pesquisa:".format(len(findResults)))
for i in findResults:
    print(i)
