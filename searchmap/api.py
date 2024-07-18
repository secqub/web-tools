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
        dorks_payload = f'{after} ({io} | intext:({io})) {sites_dorks}'
        # СТАРЫЙ ЗАПРОС
        # dorks_payload = f"{io} | intext:({io}) {' | '.join([f'site:{site}' for site, value in sites_dict.items() if value])} {f"AFTER:{self._date}" if self._date else None}"
        return self.search(dorks_payload)

    def settings_api(self):
        while True:
            print()
            print('` ~ ~ - - - Настройки - - - ~ ~ `\n'
                  f'Использовать такие сайты как: ')
            for i, (site, value) in enumerate(sites_dict.items(), start=1):
                print(f'{i}. {site} | {value}')
            print('0. Назад')
            choice = input('Выберите действие: ')
            if choice == '0':
                print()
                break
            if choice.isdecimal() and int(choice) > 0:
                sites = list(sites_dict)
                site = sites[int(choice) - 1]
                sites_dict[site] = not sites_dict[site]

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

    def get_dorks_api(self):
        print()
        io = input('Введите запрос: ')

        sites_dorks = ' | '.join([f'site:{site}' for site, value in sites_dict.items() if value])
        after = f"after:{self._date} " if self._date else ''
        dorks_payload = f'{after} ({io} | intext:({io})) {sites_dorks}'
        print(dorks_payload)

    def interface(self):
        while True:
            print()
            print('~ * - * - Меню - * - * ~')
            print('1. Поиск')
            print('2. Настройки')
            print(f'3. Сортировать по дате')
            print(f'4. Дорк пэйлоад')
            if self._date:
                print('5. Очистить дату')

            choice = input('Выберите действие: ')
            match choice:
                case '1':
                    self.search_api()
                case '2':
                    self.settings_api()
                case '3':
                    self.set_data_api()
                case '4':
                    self.get_dorks_api()
                case '5':
                    self._date = None


ds = DorksSearch()
ds.search_api('popa')
