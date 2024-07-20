from googleapiclient.discovery import build
import re

API_KEY = 'AIzaSyDFmO8x9OjLpp_ud3SM211XwAEzdjGhPU4'
CX = '64cc21fe5067f47d2'
sites_dict = {
    'telegra.ph': True,
    'teletype.in': True,
    'habr.com': False,
    'notion.site': False,
    'medium.com': False,
}


class DorksSearch:
    def __init__(self):
        self._date = None

    @staticmethod
    def search_links(api_key, query, num_results=10):
        service = build('customsearch', 'v1', developerKey=api_key)
        res = service.cse().list(
            q=query,
            cx=CX,
            num=num_results
        ).execute()

        return res.get('items', [])

    def search(self, query, *, num_res=10, s=1):
        results = self.search_links(API_KEY, query, num_res)

        links = []
        for i, result in enumerate(results, start=s):
            title = result.get('title', 'Нет заголовка').replace('– Telegraph', '').replace('— Teletype', '')
            link = result.get('link', 'Нет ссылки')

            total_title = f"{title}\n{i}. {link}"
            links.append({
                'number': i,
                'title': title,
                'link': link})
            # print(total_title)
            # print()
        return links

    def search_api(self, io):
        sites_dorks = ' | '.join([f'site:{site}' for site, value in sites_dict.items() if value])
        after = f"after:{self._date} " if self._date else ''
        dorks_payload = f'after:{after} {io} {sites_dorks}'
        # dorks_payload = f'{after} ({io} | intext:({io})) {sites_dorks}'

        # СТАРЫЙ ЗАПРОС
        # dorks_payload = f"{io} | intext:({io}) {' | '.join([f'site:{site}' for site, value in sites_dict.items() if value])} {f"AFTER:{self._date}" if self._date else None}"
        return self.search(dorks_payload)

    def set_data_api(self):
        while True:
            print()
            io = input(
                '0. Назад\nНажмите Enter чтобы поставить 2023-01-01\nИли введите свою дату в формате ГГГГ-ММ-ДД, вместе с тире: ')
            if io == '0':
                break

            if io == '':
                self._date = '2023-01-01'
                print('Дата задана, можно искать информацию!')
                break
            pattern = r'\d{4}-\d{2}-\d{2}'
            match = re.findall(pattern, io)
            if match:
                self._date = match[0]
                print('Дата задана, можно искать информацию!')
                break
            else:
                print("\nВы ввели неправильный формат даты,"
                      "\nФормат: ГГГГ-ММ-ДД"
                      "\nПример: 2023-01-01\n")

ds = DorksSearch()
ds.search_api('popa')
