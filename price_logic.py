import requests
from bs4 import BeautifulSoup

import db_connection
from Mail_sender import Mail_sender

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 '
                'Safari/537.36',
            'Accept-Language': 'fr-FR, en;q=0.5'})
url_list = db_connection.select_data()


def update_price():
    print("update_price")
    for index, url in enumerate(url_list):
        product_url = url[1]
        product_price = url[2]
        lowest_price = url[3]
        highest_price = url[4]
        mailing = Mail_sender()
        response = requests.get(product_url, headers=HEADERS)
        soup = BeautifulSoup(response.content, features="lxml")
        template = f'<htmL><a>{product_url}</a></html>'
        up_to_day_price = 0
        try:
            up_to_day_price = soup.find('span', class_='a-price-whole').text + soup.find('span',
                                                                                         class_='a-price-fraction').text
            up_to_day_price = float(up_to_day_price.replace(',', '.'))
            name = soup.find(id="productTitle").get_text().strip()
        except Exception as e:
            price = 0
            name = 'No name'
        print(up_to_day_price)
        if up_to_day_price < product_price & up_to_day_price > 0:
            mailing.send_email('', f'{name} is cheaper than {product_price}', template)
        if up_to_day_price > 0:
            db_connection.update_data(url[0], product_price, up_to_day_price, highest_price)
