import requests
from bs4 import BeautifulSoup


RUS_LETTERS = [
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
    'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь',
    'Э', 'Ю', 'Я',
]
ANIMALS_IN_ONE_PAGE = 200
last_animal = 'Аардоникс'
hash_table = {}


while last_animal[:1] in RUS_LETTERS:
    page = f'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom={last_animal}#mw-pages'
    html = BeautifulSoup(requests.get(page).content, 'html.parser')
    for step, element in enumerate(html.select('li')[2:]):
        if step == ANIMALS_IN_ONE_PAGE:
            break
        s = element.select('a')
        last_animal = s[0].text.replace(' ', '+')
        if s[0].text[:1] not in hash_table.keys():
            hash_table[s[0].text[:1]] = 1
        else:
            hash_table[s[0].text[:1]] += 1
    hash_table[last_animal[:1]] -= 1

for letter in RUS_LETTERS:
    if letter in hash_table.keys():
        print(f'{letter}: {hash_table[letter]}')
