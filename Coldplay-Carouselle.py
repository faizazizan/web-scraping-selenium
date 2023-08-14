#!/usr/bin/env python
# coding: utf-8

# In[7]:


from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Selenium web driver
driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
driver.get("https://www.carousell.com.my/search/coldplay%20ticket%20?addRecent=true&canChangeKeyword=true&includeSuggestions=true&searchId=tJS5_q&t-search_query_source=direct_search")

# Wait for the page to load (adjust the time as needed)
driver.implicitly_wait(10)

# Scrape the price
price_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/section[3]/div[1]/div/div/div[1]/div[1]/div/div[1]/a[2]/div[2]/p')
price = price_element.text

# Scrape the title
title_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/section[3]/div[1]/div/div/div[1]/div[1]/div/div[1]/a[2]/p[1]')
title = title_element.text

# Print the scraped data
print("Title:", title)
print("Price:", price)

# Close the browser
driver.quit()


# In[12]:


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium web driver
driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
driver.get("https://www.carousell.com.my/search/coldplay%20ticket%20?addRecent=true&canChangeKeyword=true&includeSuggestions=true&searchId=tJS5_q&t-search_query_source=direct_search")

# Wait for the page to load (adjust the time as needed)
driver.implicitly_wait(10)

# Find all ticket elements
ticket_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="main"]/div[2]/div/section[3]/div[1]/div/div/div'))
)

# Scrape the title and price for each ticket
for ticket_element in ticket_elements:
    try:
        title_element = ticket_element.find_element(By.XPATH, './/a[@class="D_qm D_pX D_qn D_qr D_qu D_qx D_qz D_qv D_qC"]/p[1]')
        price_element = ticket_element.find_element(By.XPATH, './/a[@class="D_qm D_pX D_qn D_qr D_qu D_qx D_qz D_qv D_qC"]/div[@class="D__E"]/p')
        title = title_element.text
        price = price_element.text

        # Print the scraped data for each ticket
        print("Title:", title)
        print("Price:", price)
        print()
    except NoSuchElementException:
        # Handle case when title or price element is not found for a ticket
        print("Error: Title or price element not found for a ticket")
        continue

# Close the browser
driver.quit()


# In[18]:


from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Selenium web driver
driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
driver.get("https://www.carousell.com.my/search/coldplay%20ticket%20?addRecent=true&canChangeKeyword=true&includeSuggestions=true&searchId=tJS5_q&t-search_query_source=direct_search")

# Find all elements with the specified XPath
elements = driver.find_elements(By.XPATH, '//*[@id="main"]/div[2]/div/section[3]/div[1]/div/div/div[1]/div[9]/div/div[1]/a[2]')

# Iterate through the found elements
for element in elements:
    # Extract the title and price elements from each element
    title_element = element.find_element(By.XPATH, './/p[1]')
    price_element = element.find_element(By.XPATH, './/div[2]/p')
    
    # Get the text values of title and price
    title = title_element.text
    price = price_element.text
    
    # Print the title and price
    print("Title:", title)
    print("Price:", price)
    print()
    
# Close the browser
driver.quit()


# In[16]:


from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Selenium web driver
driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
driver.get("https://www.carousell.com.my/search/coldplay%20ticket%20?addRecent=true&canChangeKeyword=true&includeSuggestions=true&searchId=tJS5_q&t-search_query_source=direct_search")

# Find the title element
title_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/section[3]/div[1]/div/div/div[1]/div[7]/div/div[1]/a[2]/p[1]')
title = title_element.text

# Find the price element
price_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/section[3]/div[1]/div/div/div[1]/div[7]/div/div[1]/a[2]/div[2]/p')
price = price_element.text

# Print the title and price
print("Title:", title)
print("Price:", price)

# Close the browser
driver.quit()


# In[24]:


from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Selenium web driver
driver = webdriver.Chrome()  # Assuming you have Chrome WebDriver installed
driver.get("https://www.carousell.com.my/search/coldplay%20ticket%20?addRecent=true&canChangeKeyword=true&includeSuggestions=true&searchId=tJS5_q&t-search_query_source=direct_search")

# Find all elements with the specified XPath
elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/main/div[2]/div/section[3]')

# Iterate through the found elements
for element in elements:
    # Extract the title and price elements from each element
    title_element = element.find_element(By.XPATH, './/div/div[1]/a[2]/p[1]')
    price_element = element.find_element(By.XPATH, './/div/div[1]/a[2]/div[2]/p')
    
    # Get the text values of title and price
    title = title_element.text
    price = price_element.text
    
    # Print the title and price
    print("Title:", title)
    print("Price:", price)
    print()
    
# Close the browser
driver.quit()


# In[7]:


from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Selenium web driver using Chrome
driver = webdriver.Chrome()

# Navigate to the Carousell URL
url = "https://www.carousell.com.my/search/coldplay?addRecent=true&canChangeKeyword=true&includeSuggestions=true&searchId=zz2o3O&t-search_query_source=direct_search"
driver.get(url)

# Get all the elements available with tag name 'p'
elements = driver.find_elements(By.TAG_NAME, 'p')

# Print the text content of each <p> element
for element in elements:
    print(element.text)

# Close the web driver
driver.quit()


# In[8]:


import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Selenium web driver using Chrome
driver = webdriver.Chrome()

# Navigate to the Carousell URL
url = "https://www.carousell.com.my/search/coldplay?addRecent=true&canChangeKeyword=true&includeSuggestions=true&searchId=zz2o3O&t-search_query_source=direct_search"
driver.get(url)

# Get all the elements available with tag name 'p'
elements = driver.find_elements(By.TAG_NAME, 'p')

# Extract the text content of each <p> element
text_content = [element.text for element in elements]

# Close the web driver
driver.quit()

# Save the data to a CSV file
filename = "p_elements.csv"
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Text Content"])  # Write header row
    writer.writerows([[text] for text in text_content])  # Write each text content as a separate row

print(f"Data saved to {filename}")


# In[12]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Set up the Selenium web driver using Chrome
driver = webdriver.Chrome()

# Navigate to the Carousell URL
url = "https://www.carousell.com.my/search/coldplay?addRecent=true&canChangeKeyword=true&includeSuggestions=true&searchId=zz2o3O&t-search_query_source=direct_search"
driver.get(url)

while True:
    try:
        # Find and click the "Show More" button
        show_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show more results')]")
        show_more_button.click()
        time.sleep(2)  # Wait for the page to load new products

    except NoSuchElementException:
        break  # Break the loop if the element is no longer found

# Get all the elements available with tag name 'p'
elements = driver.find_elements(By.TAG_NAME, 'p')

# Extract the text content of each <p> element
text_content = [element.text for element in elements]

# Close the web driver
driver.quit()

# Print the extracted text content
for text in text_content:
    print(text)


# In[15]:


import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Set up the Selenium web driver using Chrome
driver = webdriver.Chrome()

# Navigate to the Carousell URL
url = "https://www.carousell.com.my/search/coldplay?addRecent=true&canChangeKeyword=true&includeSuggestions=true&searchId=zz2o3O&t-search_query_source=direct_search"
driver.get(url)

while True:
    try:
        # Find and click the "Show More" button
        show_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Show more results')]")
        show_more_button.click()
        time.sleep(2)  # Wait for the page to load new products

    except NoSuchElementException:
        break  # Break the loop if the element is no longer found

# Get all the elements available with tag name 'p'
elements = driver.find_elements(By.TAG_NAME, 'p')

# Extract the text content of each <p> element
text_content = [element.text for element in elements]

# Close the web driver
driver.quit()

# Save the data to a CSV file
filename = "product_data.csv"
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Text Content"])
    writer.writerows([[text] for text in text_content])

print(f"Data saved to {filename}")


# In[ ]:




