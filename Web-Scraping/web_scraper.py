from bs4 import BeautifulSoup
from utilities import config
import requests
from csv import writer


def glassdoor():
    with open('Web-Scraping/GlassDoor-DataAnalyst-JobData.csv', mode='w', newline='', encoding='utf8') as file:
        csv_writer = writer(file)

        header = ['Company', 'Job title', 'Location',
                  'No of days posted ago', 'Pay range']
        csv_writer.writerow(header)
        for i, url in enumerate(config.glassdoor_urls):
            try:
                print(
                    f"Scraping page {i+1} of glassdoor for Data analyst roles")
                response = requests.get(url, headers=config.url_header)
                response.raise_for_status()

                output = BeautifulSoup(response.text, 'html.parser')
                jobs = output.find(
                    'ul', class_="hover p-0 my-0 css-7ry9k1 exy0tjh5").find_all('li')  # type: ignore

                for job in jobs:
                    info = []
                    temp_job = job.find(
                        'div', class_="d-flex flex-column pl-sm css-3g3psg css-1of6cnp e1rrn5ka4")

                    try:
                        company = temp_job.find(
                            'div', class_='d-flex justify-content-between align-items-start').a.span.text
                        info.append(company)
                        title = temp_job.find(
                            'a', class_='jobLink css-1rd3saf eigr9kq2').span.text
                        info.append(title)
                        location = temp_job.find(
                            'div', class_='d-flex flex-wrap css-11d3uq0 e1rrn5ka2').span.text
                        info.append(location)
                    except:
                        pass

                    try:
                        posted_ago = temp_job.find('div', class_='css-pxdlb2').find(
                            'div', class_='d-flex align-items-end pl-std css-1vfumx3').text
                        info.append(posted_ago)
                        pay_range = temp_job.find(
                            'div', class_='css-3g3psg pr-xxsm').span.text
                        info.append(pay_range)
                    except:
                        pass

                    csv_writer.writerow(info)
            except Exception as err:
                print(err)


def amazon():
    with open('Web-Scraping/amazon-book-list.csv', mode='w', newline='', encoding='utf8') as file:
        csv_writer = writer(file)
        header = ['Name', 'Author', 'Rating', 'Format', 'Price']

        csv_writer.writerow(header)
        base_url = "https://www.amazon.com/s?k=nonfiction+books+best+sellers&page=[NUM]&ref=sr_pg_[NUM]"
        for i in range(1, 8):
            url = base_url.replace('[NUM]', str(i))
            print(f"Scraping page {i} of amazon for Non fictional books")
            try:
                response = requests.get(url, headers=config.url_header)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, 'html.parser')
                books = soup.find_all(
                    'div', class_="a-section a-spacing-small puis-padding-left-small puis-padding-right-small")
                for book in books:
                    info = []
                    try:
                        name = book.find(
                            'a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal").span.text
                        info.append(name)
                        author = book.find(
                            'div', class_="a-row a-size-base a-color-secondary").a.text
                        info.append(author)
                        rating = book.find(
                            'div', class_="a-row a-size-small").find('span', class_="a-size-base").text
                        info.append(rating)
                    except:
                        pass
                    try:
                        format = book.find(
                            'div', class_="a-row a-size-base a-color-base").a.text
                        info.append(format)
                        price = book.find(
                            'a', class_="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal").find('span', class_="a-price").span.text
                        info.append(price)
                    except:
                        pass
                    csv_writer.writerow(info)
            except Exception as err:
                print(err)


def allrecipes():
    response = requests.get(
        "https://www.allrecipes.com/recipes/1290/everyday-cooking/more-meal-ideas/30-minute-meals/vegetarian/", headers=config.url_header)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    recipes = soup.find_all('div', class_="card__content")
    with open('Web-Scraping/recipes.csv', mode='w', newline='', encoding='utf8') as file:
        header = ['Type', 'Name', 'Rating']
        csv_writer = writer(file)
        csv_writer.writerow(header)
        for recipe in recipes:
            info = []
            Type = recipe['data-tag']
            info.append(Type)
            Name = recipe.find('span', class_="card__title-text").text
            info.append(Name)
            Rating = 4.5
            info.append(Rating)
            csv_writer.writerow(info)


glassdoor()
