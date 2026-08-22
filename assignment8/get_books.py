from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

results = []

# get the list or the searched book results
searched_book_li = driver.find_elements(By.CSS_SELECTOR, '.cp-search-result-item')
if len(searched_book_li) > 0:
    for book in searched_book_li:
        book_info ={}
        #book title
        title = book.find_element(By.CSS_SELECTOR,'.title-content')
        if title:
            book_info['Title'] = title.text
        #book Author
        author = book.find_elements(By.CSS_SELECTOR,'.author-link')
        if author:
            # one author vs multi author
            if len(author)> 1:
                author_list = [auth.text for auth in author ]
                book_info['Author'] = ";".join(author_list)
            else:
                book_info['Author'] = author[0].text
        # book media
        media = book.find_element(By.CSS_SELECTOR,'.display-info')
        if media:
            book_info['Format-Year'] = media.text
        #append the book info to results
        results.append(book_info)

df = pd.DataFrame(results)
print(df)
    
driver.quit() # close the browser window and end the session.  This is important to avoid leaving a bunch of browser windows open in the background.

# Task 3 completed

#Task 4

#write to CSV
import csv
# Save extracted data to a CSV file
with open('get_books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Author", 'Format-Year'])
    for result in results:
        writer.writerow([result["Title"], result["Author"], result['Format-Year']])

#write to JSON
import json 
data = {"results": results}
with open('get_books.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

# Task 4 Completed