import os
from urllib import parse
for i in range(len(image_urls)):
    image_url = image_urls[i]
    url = parse.urlparse(image_url)
    name, ext = os.path.splitext(url.path)
    image_byte = Request(image_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})
    f = open(f'cat{i}.{ext}', 'wb')
    f.write(urlopen(image_byte).read())
    f.close()

def crawl_and_save_image(keyword, pages):
    image_urls = []
    for i in range(1, pages+1):
        url = f'https://pixabay.com/ko/images/search/{keyword}/?pagi={i}'
        driver.get(url)
        time.sleep(2)

        for _ in range(20):
            driver.execute_async_script('window.scrollTo(0, document.body.scrollHeight / 20)')
            time.sleep(0.3)

        image_area_xpath = '/html/body/div[1]/div[1]/div/div[2]/div[3]'
        image_area = driver.find_element(By.XPATH, image_area_xpath)
        image_elements = image_area.find_elements(By.TAG_NAME, 'img')

        image_urls = []

        for image_element in image_elements:
            image_url = image_element.get_attribute('src')
            print(image_url)
            image_urls.append(image_url)
    if not os.path.exists(keyword):
        os.mkdir(keyword)

    for i in range(len(image_urls)):
        image_url = image_urls[i]
        url = parse.urlparse(image_url)
        filename = image_url.split('/')[-1]
        image_byte = Request(image_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})
        f = open(f'{keyword}/{filename}', 'wb')
        f.write(urlopen(image_byte).read())
        f.close()
driver = webdriver.Chrome()
crawl_and_save_image('호랑이', 2)