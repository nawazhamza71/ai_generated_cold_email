from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def scrape_job_description(url, driver_path):
    service = Service(driver_path)
    options = Options()
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(url)
        time.sleep(5)
        for _ in range(5):
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight / 5);")
            time.sleep(2)
        try:
            job_description_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.jobs-box__html-content"))
            )
            job_description = job_description_element.text
        except:
            soup = BeautifulSoup(driver.page_source, "html.parser")
            job_description_element = soup.select_one("div.jobs-box__html-content")
            job_description = job_description_element.get_text(strip=True) if job_description_element else None
        try:
            job_title_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "t-24.job-details-jobs-unified-top-card__job-title"))
            )
            job_title = job_title_element.text.strip()
        except:
            job_title = "Job Title"
        return job_description, job_title
    except Exception as e:
        print(f"Error: {e}")
        return None, "Job Title"
    finally:
        driver.quit()