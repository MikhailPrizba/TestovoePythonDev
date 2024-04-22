import requests
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from bs4 import BeautifulSoup

def get_link_data_from_url(url):
    try:
        URLValidator()(url)
    except ValidationError:
        return None

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0"
}

    try:
        response = requests.get(url, headers= headers)
        response.raise_for_status()  # Проверяем успешность запроса
        html_content = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    if html_content is None:
        return None

    soup = BeautifulSoup(html_content, 'lxml')

    # Проверяем наличие Open Graph разметки
    title_tag = soup.find('meta', property='og:title')
    description_tag = soup.find('meta', property='og:description')
    image_tag = soup.find('meta', property='og:image')
    type_tag = soup.find('meta', property='og:type')

    link_data = {
        'url': url,
        'title': title_tag['content'] if title_tag else '',
        'description': description_tag['content'] if description_tag else '',
        'image_url': image_tag['content'] if image_tag else '',
        'type': type_tag['content'] if type_tag else '',
    }
    if not link_data['title']:
        link_data['title'] = soup.find('title').text
    if not link_data['description']:
        description_tag = soup.find('meta', {'name': 'description'})
        link_data['description'] = description_tag['content'] if description_tag else ''
    return link_data


