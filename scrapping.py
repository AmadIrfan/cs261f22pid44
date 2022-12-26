from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import sys
import pandas as pd

id = []
brandName = []
price = []
Discription = []
returnPolicy = []
instalment = []
Discount = []
seller_Name = []







def scraping(self):
        completed = 0
        pages = [
            'https://www.daraz.pk/catalog/?_keyori=ss&from=input&page=1&q=telivision&spm=a2a0e.searchlist.search.go.746e4cb1og0pJF',
        ]
        driver = webdriver.Chrome(
            executable_path='C:\Program Files (x86)\chromedriver.exe')
        for links in pages:
            lik = self.getlink(links, 'page=1')
            for u in range(1, 50):
                urls = lik.format(u)
                driver.get(urls)
                context = driver.page_source
                soup = BeautifulSoup(context, 'html.parser')
                data = soup.findAll('div', class_="gridItem--Yd0sa")
                for i in data:
                    link = i.find('a', class_='').attrs['href']
                    driver.get('https:{}'.format(link),)
                    context = driver.page_source
                    soup = BeautifulSoup(context, 'html.parser')
                    new = soup.findAll(
                        'div', class_='pdp-block pdp-block__main-information-detail')
                    for n in new:
                        try:
                            datas = str(datetime.now().strftime("%H:%M:%S.%f"))
                            newData = datas.replace(':', '')
                            final = newData.replace('-', '')
                            id.append(final.split('.')[0])
                        except:
                            datas = str(datetime.now().strftime("%H:%M:%S.%f"))
                            newData = datas.replace(':', '')
                            final = newData.replace('-', '')
                            id.append(final.split('.')[0])
                        try:
                            na = n.find(
                                'a', class_='pdp-link pdp-link_size_s pdp-link_theme_blue pdp-product-brand__brand-link').text
                            if na == 'No Brand':
                                fName = 'Local Brand '
                                brandName.append(fName)
                            else:
                                brandName.append(n.find(
                                    'a', class_='pdp-link pdp-link_size_s pdp-link_theme_blue pdp-product-brand__brand-link').text)
                        except:
                            brandName.append('not available name ')
                        try:
                            Discription.append(
                                n.find('span', attrs={'pdp-mod-product-badge-title'}).text)
                        except:
                            Discription.append('no description founded')
                        try:
                            price.append(n.find('span', attrs={
                                         'pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl'}).text)
                        except:
                            price.append('0')
                        try:
                            try:
                                a3 = ''
                                aa = n.findAll(
                                    'div', class_={'delivery-option-item delivery-option-item_type_returnPolicy7'})
                                if (len(aa) != 0):
                                    for az in aa:
                                        a1 = az.find(
                                            'div', attrs={'delivery-option-item__title'}).text
                                        a2 = az.find(
                                            'div', attrs={'delivery-option-item__subtitle'}).text
                                        a3 = a1+a2
                                    returnPolicy.append(a3)
                                else:
                                    returnPolicy.append(' not available ')
                            except:
                                returnPolicy.append('warranty not available ')
                        except:
                            print(5, 'warranty not available', 3)
                        try:
                            instalment.append(
                                n.find('p', attrs={'item-content'}).text)
                        except:
                            instalment.append('not available ')
                        try:
                            Discount.append(
                                n.find('span', attrs={'pdp-product-price__discount'}).text)
                        except:
                            Discount.append('0')
                        try:
                            sall = n.findAll(
                                'div', class_={'pdp-block pdp-block__delivery-seller'})
                            for s in sall:
                                sellerName = s.find(
                                    'a', class_="pdp-link pdp-link_size_l pdp-link_theme_black seller-name__detail-name").text
                                seller_Name.append(sellerName)
                        except:
                            seller_Name.append('Not available')
                            completed = +1
                    pf = pd.DataFrame({'id': id, 'Brand Name': seller_Name, 'price': price, 'Discription': Discription,
                                      'seller Name': seller_Name, 'instalment': instalment, 'Discount': Discount, 'return Policy': returnPolicy, })
                    pf.to_csv('scrapers.csv', index=False, mode='w',)
                    
                    
                    
                    