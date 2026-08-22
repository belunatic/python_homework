from selenium import webdriver #imports Selenium’s main browser automation interface.
from selenium.webdriver.chrome.service import Service as ChromeService #imports Chrome-specific driver “service” configuration.
from webdriver_manager.chrome import ChromeDriverManager #imports the helper that downloads/manages the right ChromeDriver automatically.
from selenium.webdriver.common.by import By # imports the element-locator helpers (e.g., By.ID, By.CSS_SELECTOR, By.XPATH).

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

driver.get("https://owasp.org/Top10/2025/") #fetcht he web page.  This is a blocking call, so the next line will not execute until the page is fully loaded.

results = []

top_10_list = driver.find_elements(By.CSS_SELECTOR, 'ol li')
print(len(top_10_list))
if len(top_10_list) > 0:
    for vul in top_10_list:
        vul_list={}
        a_tag=vul.find_element(By.CSS_SELECTOR, 'a')
        vul_list['Title']= a_tag.text
        vul_list['Link'] = a_tag.get_attribute('href')
        results.append(vul_list)

print(results)
    
driver.quit()

#write to CSV
import csv
# Save extracted data to a CSV file
with open('owasp_top_10.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])
    for result in results:
        writer.writerow([result["Title"], result["Link"]])