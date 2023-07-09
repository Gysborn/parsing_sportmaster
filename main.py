import json
import requests


def get_json():
    page = 1
    global_page = 1
    collect_data = []

    cookies = {
        'UDID': '0c583f8a-fdd3-470f-aff6-3f6654fe0f71',
        'SMID': 'eyJhbGciOiJSUzI1NiJ9.eyJqdGkiOiIwMzUzNDQ3MS1jNTA1LTRlYmQtOGJhMS03OTU5ZDEwOGIwYjQiLCJpc3MiOiJTTTMwIiwiaWF0IjoxNjg4NzQwOTE3LCJhdWQiOiJzcG9ydG1hc3RlciIsImFuVCI6IjA5NDExZTBjLTlkYWItNGRlYy04Zjc1LTRlODZhN2NlMjM1NSIsImFuUCI6IjhkZTI2NzYyLTg2ODktNDMxZC1hNmNmLTEwZTJiZWE1OTczZSIsImFuVSI6IjEwMDAwMDAwNjY4NTIyNTYzNSIsImNhblAiOiJBSUJDcU1rbEFRTVhUZW8zZHJXbFdQNC9HSmYweDRsUklZYkFyTWg2SGN4VStuSHh0V0E5THk5czNnUmU5WERUUjRZTDlvSjVGWURDbWM5Y3VZaU1XclgvM25hNGlyOGVWVjRKYXJWazR4TUx2blZMY1JjeTZiaHZEbmUwdm9hbmJ0WTJHZy9LV1F1UmJVQkdNUHoxVUVmc1JET1diOHd1eDBzbURITjBYNk1sMUlHM3B6a1M0T1hlM0ZSMmptdmFlZm8xTGdWb0ZYZ0REWFR0eUJJUXl2b0VtSlVxNloyNzRleVB5NlY2SjgyNnN5WTBGTGd2b2lORDdiVU9wOVBHL0xnPSIsImNhblQiOiJBSUFqRHEycGxGOEZIT0RrWFRPV0hMVVYzV2N3cXdXekxSQXVVL2l2VEdDUTFqTjNFTUx1bGlGYngzUmlEdks3VktGbktJcjFMQXRsazdnU1lRaTAxeUtFS29nV1RhYVBiejAxbnByOVZQTHZnZE9mcmZPLzQvOXVDcHdqUmxpS2oxcTh6UFQ3MEg1eGdnY3lESFM5UytvK3FzV3FTS2MrUDJuTHhGOGsvZDFONkM1L1pERWlTRCt1Y0U4OG81NTAyWXFDZG5PbTVIMDAxUGRSL1N5ZFhDVlIvNFp3ZU5xVXVESm9pOEkyRHFwZGduS0tSY0dKMEUvV2dnVlIzc2dRT0NzPSIsInYiOiJWMiJ9.OPVPEnAZiht1x-XOnfiSbRvcaxl7hEqdI1vxs8bk_Hpl0Kb6vIq3LgCGbYB7t7A6UrPO8qaGuCR0bHhWO1KKBzz-LirUzkEfyCV21ehKrUBNKfINoRd_SXCywuRku9tkq5Tf-K_0SPnGfcXkKZKZT-Rrb8eH2_FNBJcq-jSJLsFcIae59HKAav7NbERzPt5wiT24_I9K07SWBw2-KQrkwxVwzZhzPYWaJ6bN7g-Me4EPLZRXEwF5xgPiupK1_3eAvuJrFyAMDlgoderGl-Vid2zHisVAzlrifvvMlHSYDJetTiUwALQweVZeoxGzFWLqP0ks4BeXn4IJtCvBQAT6RQ',
        'srv_id': '9c935903a1a5983603abc5cf9e24b037',
        'userAuth': '0',
        'ab_frisbuy': '3',
        '_gid': 'GA1.2.1686897493.1688740931',
        'tmr_lvid': '0f2c4fcf452f63f7a8843add2a73e9d4',
        'tmr_lvidTS': '1688740931125',
        'st_uid': '49465f2318f257b2041444e68de00b2f',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '5fc9d699-28be-46a9-92ac-aa6c4e067687',
        '_ym_uid': '1688740931270423675',
        '_ym_d': '1688740931',
        'uxs_uid': '74f4aa60-1cd4-11ee-a3b5-b539817fe835',
        '_ym_isad': '2',
        'adrcid': 'Au5InmQxR3u555_xAySH8Ww',
        'tt_deduplication_cookie': 'yandex',
        'tt_deduplication_cookie': 'yandex',
        'tt_deduplication_cookie': 'yandex',
        'SMAUTH': 'eyJpZCI6IjhkZTI2NzYyLTg2ODktNDMxZC1hNmNmLTEwZTJiZWE1OTczZSIsInN0IjoiUkVUVVJORUQiLCJ0bSI6MTY4ODc1NTA0N30=',
        '_ga_R1JBBZ02M3': 'GS1.2.1688755063.2.0.1688755063.0.0.0',
        'qrator_jsr': '1688911022.893.58U0D0sTKxUPPnDg-3j5qgjb8pkntfsphk7hjro8a5sq8c158-00',
        'qrator_jsid': '1688911022.893.58U0D0sTKxUPPnDg-t9old979cup9acaf1jgng6orosqgobb5',
        'utm_paidsource': 'google',
        'campaign': 'undefined',
        '_ym_visorc': 'w',
        'spcount': '7',
        '_ga': 'GA1.2.792482228.1688740931',
        'tmr_detect': '0%7C1688797537432',
        '_ga_Z7E27793QJ': 'GS1.1.1688795660.3.1.1688797635.60.0.0',
    }

    headers = {
        'authority': 'www.sportmaster.ru',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru,en;q=0.9,mt;q=0.8',
        'content-type': 'application/json',
        'origin': 'https://www.sportmaster.ru',
        'referer': 'https://www.sportmaster.ru/catalog/muzhskaya_obuv/krossovki?f-kind_of_product=kind_of_product_krossovki&f-brand=4526360002,4930770002,4931390002&f-ra=size_41&sortType=BY_POPULARITY&watched=0&utm_referrer=https://www.sportmaster.ru/catalog/muzhskaya_obuv/krossovki/?f-kind_of_product',
        'sec-ch-ua': '"Chromium";v="112", "YaBrowser";v="23", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.4.674 Yowser/2.5 Safari/537.36',
        'x-sm-accept-language': 'ru-RU',
        'x-sm-request-id': 'bdcee1b4-e09e',
        'x-sm-tracing-id': 'd670c99a-18576655',
    }

    json_data = {
        'url': '/catalog/muzhskaya_obuv/krossovki?f-kind_of_product=kind_of_product_krossovki&f-brand=4526360002,4930770002,4931390002&f-ra=size_41&sortType=BY_POPULARITY&watched=0&utm_referrer=https://www.sportmaster.ru/catalog/muzhskaya_obuv/krossovki/?f-kind_of_product',
        'page': page,
    }

    url = 'https://www.sportmaster.ru/web-api/v1/catalog/'
    while global_page:  # Запускаем цикл по страницам с товарами
        response = requests.post(url=url, cookies=cookies, headers=headers,
                                 json=json_data)
        if response.status_code == 200:
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
            print(response.status_code)
            break
    if collect_data:
        with open('collect_data.json', 'w', encoding='utf-8') as f:
            json.dump(collect_data, f, indent=4, ensure_ascii=False)
        return True
    else:
        return False


if __name__ == '__main__':
    get_json()
