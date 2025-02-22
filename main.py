from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


driver = webdriver.Chrome()  


url = "https://gtrbd.com/"  
driver.get(url)


time.sleep(3)


links = driver.find_elements(By.TAG_NAME, "a")


urls = [link.get_attribute("href") for link in links if link.get_attribute("href")]


df = pd.DataFrame(urls, columns=["URLs"])


df.to_csv("scraped_urls.csv", index=False)


driver.quit()

print("Scraping completed! URLs saved to scraped_urls.csv")
