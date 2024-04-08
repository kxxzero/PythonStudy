from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import mysql.connector
import random

def getConnection():
    try:
        conn = mysql.connector.connect(
            host="211.238.142.113",
            user="root",
            password="root",
            database="mydb"
        )
        return conn
    except Exception as e:
        print(e)
        return None

def board_insert(insert_value):
    conn = getConnection()
    cursor = conn.cursor()
    sql = """
           INSERT INTO recruit(NO,cno,title,stack_txt,stack_img,career,education,content_j,content_q,content_p,content_b,end_date) 
           VALUES((SELECT IFNULL(MAX(no)+1,1) FROM recruit), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
         """
    cursor.execute(sql, insert_value)
    print("게시물 등록 완료")
    conn.commit()
    cursor.close()
    conn.close()


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

current_page = 1
max_pages = 14

while current_page <= max_pages:
    driver.get(f'https://join-watch.com/product/list.html?cate_no=529&page={current_page}')

    post_links = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@id, 'anchorBoxId_')]/div/div/div/a"))
    )

    for link in post_links:
        link_url = link.get_attribute('href')
        print(link_url)

        driver.execute_script(f"window.open('{link_url}', '_blank');")

        # 새로운 창 핸들러 가져오기
        driver.switch_to.window(driver.window_handles[1])

        try:
            # 상세 페이지가 로드될 때까지 대기
            wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#df-product-detail > div > div.infoArea-wrap > div > div > div.scroll-wrapper.df-detail-fixed-scroll.scrollbar-macosx > div.df-detail-fixed-scroll.scrollbar-macosx.scroll-content > div.headingArea > h2'))
            )
            # 상세 페이지의 제목 가져오기
            title_element = driver.find_element(By.CSS_SELECTOR,
                                                '#df-product-detail > div > div.infoArea-wrap > div > div > div.scroll-wrapper.df-detail-fixed-scroll.scrollbar-macosx > div.df-detail-fixed-scroll.scrollbar-macosx.scroll-content > div.headingArea > h2')
            title = title_element.text
            print(f"게시물 제목: {title}")

            # 상세 페이지에서 이미지 가져오기
            image_element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#df-product-detail > div > div.imgArea-wrap > div > div > div.thumbnail > span > img'))
            )
            image_url = image_element.get_attribute("src")
            print(f"이미지: {image_url}")

            # 가격 가져오기
            price_selector = "#span_product_price_text"
            price_element = driver.find_element(By.CSS_SELECTOR, price_selector)
            price = price_element.text.strip()
            print(f"가격: {price}")

            try:
                image_element2 = driver.find_element(By.CSS_SELECTOR, '#prdDetail > div.cont > div:nth-child(4) > p:nth-child(1) > img:nth-child(1)')
                image_url2 = image_element2.get_attribute("src")
            except:
                image_element2 = driver.find_element(By.CSS_SELECTOR, '#prdDetail > div.cont > div:nth-child(4) > img')
                image_url2 = image_element2.get_attribute("src")
            print(f"상세이미지: {image_url2}")

        except Exception as e:
            print("제목 또는 이미지를 찾을 수 없음")
            print(e)

        finally:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    current_page += 1

driver.quit()