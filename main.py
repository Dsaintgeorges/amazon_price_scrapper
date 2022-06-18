from bs4 import BeautifulSoup
import requests
import pandas as pd

from Mail_sender import Mail_sender

excel_file = pd.read_excel('data.xlsx')

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 '
                'Safari/537.36',
            'Accept-Language': 'fr-FR, en;q=0.5'})
url_list = excel_file.values.tolist()

for index,url in enumerate(url_list):
    product_url = url[0]
    product_price = url[1]
    mailing = Mail_sender()
    response = requests.get(str(url[0]), headers=HEADERS)
    soup = BeautifulSoup(response.content, features="lxml")
    template = f'<htmL><a>{product_url}</a></html>'
    try:
        up_to_day_price = float(
            soup.find('input', type="hidden", attrs={'id': 'attach-base-product-price'}).get('value'))
        name = soup.find(id="productTitle").get_text().strip()
    except Exception as e:
        price = ''
    if up_to_day_price < product_price:
        mailing.send_email('', f'{name} is cheaper than {product_price}',template)
        excel_file.at[index,'current_price'] = up_to_day_price
        excel_file.to_excel('data.xlsx', index=False)
    else:
        excel_file.at[index,'current_price'] = up_to_day_price
        excel_file.to_excel('data.xlsx', index=False)
