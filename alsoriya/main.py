from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time
import pandas as pd

driver = webdriver.Chrome()

print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] Opening the browser...')

driver.get("https://alsourayia.com/ar/%D9%85%D9%88%D9%83%D9%8A%D8%AA-%D8%A7%D9%84%D9%85%D9%83%D8%A7%D8%AA%D8%A8#/pageSize=12&viewMode=grid&orderBy=0")

print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] Scrolling the page...')

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

time.sleep(4)
print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] Finding all products links...')

linksElements = driver.find_elements(By.CSS_SELECTOR, '.product-title a')

links = []

for link_element in linksElements :
    link = link_element.get_attribute('href')
    links.append(link)

print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] number of products: {len(links)}...')

products = [['رابط المنتج', "اسم المنتج", "السعر", "الوصف", "روابط الصور", 'المقاس', 'نوع الخيط	', 'بناء المنتج	', 'وزن الخيط', 'عدد الغرز', 'Backing', 'الطبقة الأساسية السفلية', 'الطبقة الثانية السفلية', 'ارتفاع الخيط', 'الإرتفاع الكلي - السماكة']]
flag =1

for link in links:
    print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] opening product {flag} page...')
    driver.get(link)
    time.sleep(3)
    title = driver.find_element(By.CSS_SELECTOR, '.product-name h1').text
    
    try:
        price = driver.find_element(By.CSS_SELECTOR, '.product-price span').text
    except Exception:
        price = 0
        print('no price for this product')
    desc = driver.find_element(By.CSS_SELECTOR, '.short-description').text
    images = []
    images_elements = driver.find_elements(By.CSS_SELECTOR, '.slick-track img')

    for image_element in images_elements:
        image = image_element.get_attribute('src')
        images.append(image)
    
    image = ''
    if len(images) > 0:
        for i in images:
            image += i + ', '
    else:
        image = driver.find_element(By.CSS_SELECTOR, '.picture-link img').get_attribute('src')
    
    size : str
    role_type : str
    product_body : str
    role_weight : str
    number_of_roles : str
    backing : str
    main_lower : str
    second_lower : str
    role_height : str
    total_height : str

    specifications = driver.find_elements(By.CSS_SELECTOR, '.odd')
    if len(specifications) == 8:
        main_lower = ''
        second_lower = ''
        size = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('innerHTML')
        role_type = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('innerHTML')
        product_body = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('innerHTML')
        role_weight = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('innerHTML')
        number_of_roles = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('innerHTML')
        backing = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[7]/td[2]').get_attribute('innerHTML')
        role_height = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[8]/td[2]').get_attribute('innerHTML')
        try:

            total_height = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[9]/td[2]').get_attribute('innerHTML')
        except Exception:
            total_height = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[8]/td[2]').get_attribute('innerHTML')


    elif len(specifications) == 10:
        size = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('innerHTML')
        role_type = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('innerHTML')
        product_body = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('innerHTML')
        role_weight = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('innerHTML')
        number_of_roles = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('innerHTML')
        # backing = driver.find_element(By.XPATH, '')
        main_lower = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[7]/td[2]').get_attribute('innerHTML')
        second_lower = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[8]/td[2]').get_attribute('innerHTML')
        role_height = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[9]/td[2]').get_attribute('innerHTML')
        total_height = driver.find_element(By.XPATH, '//*[@id="quickTab-specifications"]/div/div[2]/table/tbody/tr[10]/td[2]').get_attribute('innerHTML')
    
    
    
    product = [link, title, price, desc, image, size, role_type, product_body, role_weight, number_of_roles, backing, main_lower, second_lower, role_height, total_height]
    products.append(product)
    print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] product {flag} added to the list...')
    flag += 1


# print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] saving data to json...')
# outputfilename = 'out.json'
# with open(outputfilename, 'wb') as outfile:
#     json.dump(products, outfile)

print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] saving data to excel...')
df = pd.DataFrame(products[1:], columns=products[0])
df.to_excel("items4.xlsx", index=False)


print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}] done...')
driver.quit()