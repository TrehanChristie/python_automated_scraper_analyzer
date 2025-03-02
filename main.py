# main.py

# Import required libraries and modules
import pandas as pd
import inspect
import os
import sys
from datetime import datetime
from utils import is_valid_url, build_main_url
from article_scraper import article_scraper
from llm_text_extractor import llm_text_extractor
from articles_to_dataframe import articles_to_dataframe
from export_df_as_csv import export_df_as_csv

# Main Function
def main(api_key: str, output_path: str, main_url: str = None, filters: dict = None):  

    # Use timer to calculate run time
    start_time = datetime.now()
    print(f"Start Time: {start_time.strftime('%H:%M:%S')}")

    # Print current function name
    print("--------------------------------------------------------------------")
    print(f"Executing function: {inspect.currentframe().f_code.co_name}") 
    
    try:
        # STEP 1: Validate main_url or build URL using filters dict
        if main_url:
            print(f"Using main_url: {main_url}")
            is_valid_url(main_url)
            print("main_url provided is validated")
        else:           
            if not filters:
                raise ValueError(f"\n\t Error: main_url not provided, provide filters by populating respective variables")
            main_url = build_main_url(filters)
        
        # STEP 2: Run the Scraper
        articles = article_scraper(main_url)

        # STEP 3: Run the LLM text extractor
        articles = llm_text_extractor(articles, api_key)  

        # STEP 4: Add articles to a dataframe
        df_combined, df_identified_diseases, df_identified_treatments = articles_to_dataframe(articles)    

        # STEP 5: Add articles to a dataframe
        export_df_as_csv(output_path, main_url, df_combined, df_identified_diseases, df_identified_treatments)       
        
    except ValueError as e:
        print(f"Error message: {e}")
        return

    except Exception as e:
        print(f"Exception message: {e}")

    finally:
        end_time = datetime.now()
        print(f"End Time: {end_time.strftime('%H:%M:%S')}")
        print(f"Time taken to run: {end_time - start_time}")

    
# Run Script
if __name__ == "__main__":

    # UPDATE OPENAI api key accordingly for using gpt-3.5-turbo
    api_key = os.getenv("OPENAI_API_KEY") ## ADD YOUR OPENAI_API_KEY HERE

    # UPDATE Output path for CSVs
    output_path = r"C:\Users\ANIL\Documents\Data Engineering\Python\Python fundamentals\InoviaBio_code_test\output_csv_files"

    # RUN USING api_key, output_path, main_url
    # Main url (populate here if you have the main url link)
    main_url = "https://pubmed.ncbi.nlm.nih.gov/?term=carbapenem+resistance&filter=dates.2022%2F1%2F1-2022%2F1%2F30&filter=simsearch1.fha&filter=simsearch2.ffrft&filter=hum_ani.humans"

    # Run main function 
    main(api_key = api_key, 
         output_path = output_path, 
         main_url = main_url)