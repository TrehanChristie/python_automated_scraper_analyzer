# article_scraper.py

# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import inspect
import time

# Main Scraper Function
def article_scraper(main_url: str) -> list: 
    """Scrapes articles from main_url and adds scrapped info to articles"""

    # Print current function name
    print("--------------------------------------------------------------------")
    print(f"Executing function: {inspect.currentframe().f_code.co_name}")  

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    print("WebDriver started successfully!")

    # Open main_url
    try:
        driver.get(main_url)
        # time.sleep(2)  # Allow page to load   
    except ValueError as e:
        raise ValueError(f"\n\t Error in {inspect.currentframe().f_code.co_name} function: "
                        f"\n\t Error loading url ({main_url}) Check below error and check the input variables provided: {e}")     

    # Check if any articles are found
    number_of_articles_element = driver.find_element(By.CLASS_NAME, "results-amount").find_element(By.TAG_NAME, "h3")
    number_of_articles = number_of_articles_element.text.strip()

    print("Total number articles to scrape:", number_of_articles)

    if number_of_articles == "No results were found.":
        raise ValueError(f"\n\t Error in {inspect.currentframe().f_code.co_name} function: "
                         f"\n\t No articles found for the given main_url: {main_url}")

    # Find all elements for articles from initial page
    article_elements = driver.find_elements(By.CLASS_NAME, "docsum-content")
    
    # Extract the max page number from the "max" attribute value
    page_number__wrapper_element = driver.find_element(By.CLASS_NAME, "page-number-wrapper").find_element(By.CLASS_NAME, "page-number-form")
    max_page_number_element = page_number__wrapper_element.find_element(By.CLASS_NAME, "page-number")
    max_page_number = max_page_number_element.get_attribute("max")
    
    print("Pages to scrape:", max_page_number)

    # Create an articles list to append pubmed_paper_id, paper_title, url, abstract 
    articles = []

    # Iterate through all the pages
    for page_number in range(1, int(max_page_number)+1):
        
        page_url = main_url + "&page=" + str(page_number)

        # Open page url
        try:
            driver.get(page_url)
            # time.sleep(2)  # Allow page to load   
        except Exception as e:
            print(f"\n\t Exception in {inspect.currentframe().f_code.co_name} function:"
                  f"\n\t Error loading subsequent url ({page_url}):"
                  f"\n\t {e}")           
            continue 
        
        # Find all article elements from current page
        article_elements.clear()
        article_elements = driver.find_elements(By.CLASS_NAME, "docsum-content")     

        # Iterate through each article from the current page
        for index in range(len(article_elements)):
            try:
                # Go to current page
                driver.get(page_url)
                # time.sleep(2)  # Allow page to load  
                print(f"Scraping page number: {page_number} using {page_url}")

                # Re-fetch article elements to prevent staleness
                article_elements.clear()
                article_elements = driver.find_elements(By.CLASS_NAME, "docsum-content") 

                # set article to current article of iteration
                article = article_elements[index]

                # Extract article link
                article_link_element = article.find_element(By.CLASS_NAME, "docsum-title")
                article_link = article_link_element.get_attribute("href")
            
                # Go to article page using article link
                driver.get(article_link)
                # time.sleep(2)  # Allow page to load   
                print(f"Scraping article: {article_link}")
            
                # Extract PubMed Paper ID
                pubmed_paper_id_element = driver.find_element(By.CLASS_NAME, "current-id")
                pubmed_paper_id = pubmed_paper_id_element.text
            
                # Extract PubMed Paper title
                paper_title_element = driver.find_element(By.CLASS_NAME,"heading-title")
                paper_title = paper_title_element.text    
            
                # Extract abstract text
                abstract_element =  driver.find_element(By.ID, "eng-abstract") 
                abstract_texts = abstract_element.find_elements(By.TAG_NAME, "p")
                abstract_text = ""
                for a_text in abstract_texts:
                    abstract_text += a_text.text + " "

                # Append articles list with current article's pubmed_paper_id, paper_title, url, abstract 
                articles.append({
                    "pubmed_paper_id": pubmed_paper_id,
                    "paper_title": paper_title,
                    "url": article_link,
                    "abstract": abstract_text,
                    "identified_diseases": "",
                    "identified_treatments": ""
                    })

                print("-----------------")
                print(f"Article added- PubMed ID: {pubmed_paper_id}, URL: {article_link}")
                
            except StaleElementReferenceException:
                print(f"\n\t StaleElementReferenceException occurred. Retrying job {index}")
                driver.refresh()
                WebDriverWait(driver, 5).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "docsum-content"))
                )
                continue  # Retry the iteration
                
            except Exception as e:
                print(f"\n\t Exception in {inspect.currentframe().f_code.co_name} function:"
                      f"\n\t Exception extracting data for an article ({article_link}) on page ({page_url}):"
                      f"\n\t {e}")
        
    # Close the browser
    driver.quit()
    
    return articles