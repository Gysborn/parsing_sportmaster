import json
import requests


# Proxy modification

def get_json():
    code = 0
    page = 1
    global_page = 1
    collect_data = []

    cookies = {
        'qrator_jsid': '1688929465.264.HPg2acVBk1Vj9TkT-dm4848vj0rpdumelgeam771n9l9isou6',
        'SMID': 'eyJhbGciOiJSUzI1NiJ9.eyJqdGkiOiJiN2RjNzY4Ni1lODVkLTRiYzQtYjY3Yy0yYmUxNDg4ZGE0YzEiLCJpc3MiOiJTTTMwIiwiaWF0IjoxNjg4OTI5NDcwLCJhdWQiOiJzcG9ydG1hc3RlciIsImFuVCI6IjMwZmM3NjhjLTdiZTEtNGE5Yi1iYjJlLTkzMjQ1MGIzZGFmMiIsImFuUCI6Ijc5NGMxY2MyLTBhOTgtNGYzMi05MjNmLTkyYmI5MDdlOTc4ZSIsImFuVSI6IjEwMDAwMDAwNjcxNTE2MDA1MCIsImNhblAiOiJBSUExcXhXY3h2QjlZZzVkbG9TcGczRXo5L0Q4QkMyc2hhVWg4bWlDTzRnWE5nRTRpaW0zMkM3OU9jTHhwbE9qUjk5ODdlUGU2bzB3V0tCUm5uMjZDa3o0VTlKVGQ5VGtxdVVudmlhQW0wN3FjckNWQjdQcVZlR3E3WFRaZk5IZDI2ZVZsWXVCVXBrUUtEOFdJeTlWcTMwdTdSbjlGM2Q5Ymk2QnE0OWJXQld3N0Z0MmpBMDVWdDRhY0dWYW1DSmhaT0dVUlFlaHdLS240MlpFS1BGeC91cjM4anJGUyswZ2VKZTlkZlVSTEs2bjQ3Z21nYXNQR2ZWa1pHRC9ScGNZOGlVPSIsImNhblQiOiJBSUFQOWdBRDNEOHlkYllScmRCTTA3dnlHVmFsdnZxUnB1QzdaR1FWZ01FK1VMNlhpUnY3S211V3BQQk9OLzVQUDRvZ0I4dGlzSTNRUHRHczNsaXAxTkRrQVZoR1NuM29GcUJFZnZmRGZFUnYvc25LcDI4Q284QWJMQkZ5cCtMY2p5VGtIMWlUQk12K3VuUUI3SThiV1BpZjlvNmpLWmlDSVgvZmlpRG9aRm4yK0RHMEdIY2ptY1Zwcm9OQlJuYkplY3pPZTBIMk82OEVaVU1iQUZ3WVg2UGNJdDB5M1hwcDVHcXFkbXN3T215VkNFd1pQYWZJckxQbXUzdGZKQkI0YUYwPSIsInYiOiJWMiJ9.lULGFE7lCYG1g-uVGFOsQ4JVaK5F1Sjpz5Jn-lQRnJwCvsfMNYcFZoseCl4HltetR6TuKs2kzC8cFj1zcnej7TaWdWAgex_oRg1epeTtqgPNvm84dVbDMBHQqS_omxxahUy72sCqwDZJwT5y1L-eP2mlc-FbzW4w-Zc0o4Xf79oAN_-rz8dND_uSoGQHN808pYUyflFaSHxVNdHmm3uyh5IFCWQWr7wpvR30pcN_GtBMl9Y8cg84E1-a4lbSK4n7AZ0h71qK6kUA-cJV8MlJ07xc7p4dr6bFlmSUzTGUXY2TRhzLX5fE5oC1slnLZhs2bZvO-W3fT4LT8ZZpyxnxmA',
    }

    headers = {
        'authority': 'www.sportmaster.ru',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.sportmaster.ru',
        'referer': 'https://www.sportmaster.ru/catalog/muzhskaya_obuv/krossovki/?f-kind_of_product=kind_of_product_krossovki&f-brand=4526360002,4930770002,4931390002&f-ra=size_41&page=1',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }

    proxies = {
        'https': '38.154.88.110:8000',
    }

    json_data = {
        'url': '/catalog/muzhskaya_obuv/krossovki?f-kind_of_product=kind_of_product_krossovki&f-brand=4526360002,4930770002,4931390002&f-ra=size_41&sortType=BY_POPULARITY&watched=0&utm_referrer=https://www.sportmaster.ru/catalog/muzhskaya_obuv/krossovki/?f-kind_of_product',
        'page': page,
    }

    url = 'https://www.sportmaster.ru/web-api/v1/catalog/'
    while global_page:  # Запускаем цикл по страницам с товарами
        response = requests.post(url=url, cookies=cookies, headers=headers,
                                 json=json_data, proxies=proxies)
        code = response.status_code
        if code == 200:
            data = response.json()  # Достаем json
            global_page = int(data['pagination']['pagesCount']) - page
            # Устанавливаем корректно, общее кол. страниц
            page += 1  # Инкрименируем номер страницы
            print(f"parsing {page - 1}...")
            for i in range(int(data['pagination']['pageSize'])):
                if data['products'][i]['price']['discountRate'] > 30:  # Собираем данные если скидка выше 30%
                    data_dict = {
                        "name": data["products"][i]["name"],
                        "link": "https://www.sportmaster.ru" + data["products"][i]["variants"][0]["url"],
                        "price": data["products"][i]["price"]["catalog"],
                        "price_retail": data["products"][i]["price"]["retail"],
                        "discount_rate": data["products"][i]["price"]["discountRate"],
                        "discount": data["products"][i]["price"]["discountAmount"],
                        "color": data["products"][i]["color"],
                    }
                    collect_data.append(data_dict)
        else:
            break
    if collect_data:
        with open('collect_data.json', 'w', encoding='utf-8') as f:
            json.dump(collect_data, f, indent=4, ensure_ascii=False)
        return code
    else:
        return code

