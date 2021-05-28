import hashlib
import json


with open('countries.json', encoding='utf-8') as f:
    countries = json.load(f)


class WikiIterate:

    def __iter__(self):
        self.countries_iterator = iter(countries)
        return self

    def __next__(self):
        item = next(self.countries_iterator)
        country = item['name']['common']
        country_for_href = country.replace(' ', '_')
        href = f'https://en.wikipedia.org/wiki/{country_for_href}'
        with open('result.txt', 'a', encoding='utf-8') as f:
            f.write(f'{country}, {href}\n')
        return


for result in WikiIterate():
    print(result)


def wiki_gen():
    with open('result.txt', encoding='utf-8') as f:
        for line in f:
            result_hash = hashlib.md5(line.encode()).hexdigest()
            yield result_hash


for i in wiki_gen():
    print(i)
