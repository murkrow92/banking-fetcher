from typing import List, Any
from string import Template
import requests
from bs4 import BeautifulSoup
import json

URL = 'https://sandbox.vnpayment.vn/apis/danh-sach-ngan-hang/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

tr_tags = soup.find_all('tr')

rows: List[Any] = []
for tr_tag in tr_tags:
    td_tags = tr_tag.find_all('td')
    row: List[Any] = []
    for td_tag in td_tags:
        text = td_tag.get_text()
        if len(text) > 0:
            row.append(text)
        else:
            image = td_tag.find('img')
            src = 'https://sandbox.vnpayment.vn' + image.get('src')
            row.append(src)

    if len(row) > 0:
        bank_dictionary = {
            "bank_id": row[0],
            "bank_code": row[1],
            "bank_name": row[2],
            "bank_logo": "require('../Images/Logos/" + row[0] + ".png')"
        }
        # remote_icon = requests.get(row[3], allow_redirects=True)
        # open(row[0] + '.png', 'wb').write(remote_icon.content)
        rows.append(bank_dictionary)

# print(json.dumps(rows))

print(rows)