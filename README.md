# Automated Article Scraper and Analyzer


## Overview

This project automates the process of scraping articles from PubMed, extracting relevant medical information using an LLM model, and exporting the data into structured CSV files for further analysis. It integrates web scraping, NLP-based text extraction, and data processing into a single workflow.

### Features

✔ **Article Scraping:** Uses Selenium to extract article metadata from PubMed.<br>
✔ **LLM Text Extraction:** Utilizes OpenAI's GPT-3.5-turbo to identify diseases and treatments from article abstracts.<br>
✔ **Data Structuring:** Converts extracted information into structured Pandas DataFrames.<br>
✔ **CSV Exporting:** Saves the processed data into CSV files for further use.<br>
✔ **URL Validation & Filtering:** Ensures only valid PubMed URLs are processed and supports custom filters.<br>


## 1. Project Structure

```bash
.
├── __init__.py                # Initializes the package
├── article_scraper.py         # Scrapes articles from PubMed
├── llm_text_extractor.py      # Extracts disease and treatment info using OpenAI's GPT model
├── articles_to_dataframe.py   # Converts scraped data into Pandas DataFrames
├── export_df_as_csv.py        # Exports DataFrames as CSV files
├── main.py                    # Main script orchestrating the entire workflow
├── tests.py                   # Test cases for validation and debugging
├── utils.py                   # Utility functions for validation and URL construction
└── README.md
```


## 2. Script Descriptions
### 2.1 main.py

```main(api_key: str, output_path: str, main_url: str = None, filters: dict = None):```<br>

**Purpose:**<br>
•	Acts as the entry point for the pipeline.<br>
•	Handles overall execution, calling functions from other scripts.<br>
•	Validates input parameters and executes necessary workflows.<br>

**Key Functions:**<br>
•	Validates `main_url` or builds a URL using `filters` dict.<br>
•	Calls the article scraper, LLM text extractor, DataFrame creator, and CSV exporter.<br>

### 2.2 utils.py

**Purpose:**<br>
•	Contains helper functions for URL validation, date formatting, and URL construction.<br>

**Key Functions:**<br>

```is_valid_url(url: str) -> bool:```<br>
•	Checks if a URL is a valid and accessible PubMed link.<br>

```parse_date(date_str: str) -> Optional[datetime]:```<br>
•	Parses different date formats and returns a valid datetime object.<br>

```validate_date(date_from: str, date_to: str) -> None:```<br>
•	Ensures `date_from` is not later than `date_to`.<br>

```build_main_url(filters: dict[str, str]) -> str:```<br>
o	Constructs a PubMed query URL based on given search `filters`.<br>

### 2.3 article_scraper.py

```article_scraper(main_url: str) -> list[dict]:```<br>

**Purpose:**<br>
•	Scrapes articles from PubMed based on the constructed `main_url`.<br>

**Key Functions:**<br>
•	Uses Selenium to navigate and scrape PubMed articles.<br>
•	Extracts details such as title, abstract, and PubMed ID.<br>
•	Returns a list of article dictionaries.<br>

### 2.4 llm_text_extractor.py

```llm_text_extractor(articles: list[dict], api_key: str) -> list[dict]:```<br>

**Purpose:**<br>
•	Uses OpenAI’s LLM to extract disease and treatment-related information from article abstracts.<br>

**Key Functions:**<br>
•	Calls OpenAI’s API for entity extraction.<br>
•	Parses the API response and adds extracted information to the article dictionary.<br>

### 2.5 articles_to_dataframe.py

```articles_to_dataframe(articles: list[dict]) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:```<br>

**Purpose:**<br>
•	Converts processed articles into Pandas DataFrames for structured analysis.<br>

**Key Functions:**<br>
•	Creates three DataFrames:<br>
  1.	df_combined: Includes article metadata and extracted entities.<br>
  2.	df_identified_diseases: Lists identified diseases per article.<br>
  3.	df_identified_treatments: Lists identified treatments per article.<br>

### 2.6 export_df_as_csv.py

```export_df_as_csv(output_path: str, main_url: str, df_combined: pd.DataFrame, df_identified_diseases: pd.DataFrame, df_identified_treatments: pd.DataFrame) -> None:```<br>

**Purpose:**<br>
•	Exports generated DataFrames into structured CSV files.<br>

**Key Functions:**<br>
•	Creates csv file names based on the search_term in `main_url`<br>
•	Saves the DataFrames as CSV files in the specified output directory.<br>

### 2.7 tests.py

Purpose:<br>
•	Contains test cases to validate the functionality of different modules.<br>

Key Features:<br>
•	Runs main() with predefined inputs.<br>
•	Tests error handling for incorrect URLs, missing filters.<br>

## 3. Dependencies
### Ensure you have the following installed:<br>
•	_Python 3.x_<br>
•	_Selenium_<br>
•	_Pandas_<br>
•	_requests_<br>
•	_validators_<br>
•	_inspect_<br>
•	_OpenAI API key_ (for text extraction)<br>
•	_Chrome WebDriver_ (managed using webdriver-manager)<br>

## 4. How to run the script
### 4.1. Running the Script
**Method 1-**<br> 
**Running with the provided PubMed URL:**
- Ensure all dependencies are installed.
-	Open the `tests.py` script which imports the main function
-	use the first block of code 
-	ensure you provide your _OPENAI_API_KEY_ in `api_key` and your desired path in `output_path`
```
## TEST TO CHECK IF MAIN SCRIPT RUNS CORRECTLY USING MAIN_URL
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

api_key = os.getenv("OPENAI_API_KEY") ## ADD YOUR OPENAI_API_KEY HERE
output_path = r"" ## ADD YOUR OUTPUT PATH
main_url = "https://pubmed.ncbi.nlm.nih.gov/?term=carbapenem+resistance&filter=dates.2022%2F1%2F1-2022%2F1%2F30&filter=simsearch1.fha&filter=simsearch2.ffrft&filter=hum_ani.humans"
# Run main function 
main(api_key=api_key, 
     output_path=output_path, 
     main_url=main_url)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

**Method 2. Running by building custom URL using filters dict (replicating an advanced search function):**
-	Open the tests.py script which imports the main function
-	use the third block of code 
-	ensure you provide your OPENAI_API_KEY in api_key and your desired path in output_path
-	The rest of the variables need to set according to their respective comments 
```
## TEST TO CHECK IF SCRIPT RUNS CORRECTLY BY BUILDING CUSTOM URL USING FILTERS DICT
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

api_key = os.getenv("OPENAI_API_KEY") ## ADD YOUR OPENAI_API_KEY HERE
output_path = r"C:\Users\ANIL\Documents\Data Engineering\Python\Python fundamentals\InoviaBio_code_test\output_csv_files"

# Build new main_url by populating below fields for searching PubMed
base_url = "https://pubmed.ncbi.nlm.nih.gov/" # NEEDED Add base url (ONLY works for the provided base url)
search_term = "folliculitis" # NEEDED input term to be searched 
date_from = "2022/1/1" # OPTIONAL input date from in format: yyyy/mm/dd or yyyy/m//d or yyyy/mm/d or yyyy/m/d
date_to = "2022/1/1" # OPTIONAL input to date to in format: yyyy/mm/dd or yyyy/m//d or yyyy/mm/d or yyyy/m/d
species = "humans" # OPTIONAL input humans or animal or leave blank to select both
abstract_text_availability  = "yes" # NEEDED input yes or no
free_full_text_availability  = "no" # NEEDED input yes or no
full_text_availability = "no" # NEEDED input yes or no

# Create filters dict used to build main_url
filters = {
    "base_url": base_url,
    "search_term": search_term,
    "date_from": date_from,
    "date_to": date_to,
    "species": species,
    "abstract_text_availability": abstract_text_availability,
    "free_full_text_availability": free_full_text_availability,
    "full_text_availability": full_text_availability
}

# Run main function 
main(api_key=api_key, 
     output_path=output_path, 
     filters=filters)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

### 4.2. Running Tests
Open `tests.py` and read through the instructions provided running each test individually. Run each test section individually. It provides the test case, expected message and the block of code to run.

**Eg- TEST CASE 1 RUN using incorrect url**
```
# USE INCORRECT_URL
# Expect error message:
        # Error message: 
        #         Error validating url in is_valid_url function:
        #         pubmed url not provided url should start with 'https://pubmed.ncbi.nlm.nih.gov/'
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

incorrect_url = "https://www.google.com/"
api_key = os.getenv("OPENAI_API_KEY") ## ADD YOUR OPENAI_API_KEY HERE
output_path = r"C:\Users\ANIL\Documents\Data Engineering\Python\Python fundamentals\InoviaBio_code_test\output_csv_files"
main_url = incorrect_url

# Run main function 
main(api_key=api_key, 
     output_path=output_path, 
     main_url=main_url)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

## 5. Output Files
The project generates three CSV files, each containing structured article data.

### 5.1 Combined Output File
Filename Example:<br>
_carbapenem_resistance_combined.csv_<br>

**Purpose:**<br>
•	This file contains a unique entry for each PubMed paper (pubmed_paper_id).<br>
•	The identified diseases and identified treatments are flattened (stored as comma-separated lists).<br>
•	The dataset is unique at the PubMed paper ID level.<br>

**Columns:**<br>
**_pubmed_paper_id_**:	Unique identifier for the PubMed article<br>
**_paper_title_**:	Title of the research paper<br>
**_url_**:	Direct link to the PubMed article<br>
**_abstract_**:	Extracted abstract of the article<br>
**_identified_diseases_combined_**:	Comma-separated list of extracted diseases<br>
**_identified_treatments_combined_**:	Comma-separated list of extracted treatments<br>

### 5.2 Identified Diseases File
Filename Example:<br>
carbapenem_resistance_identified_diseases.csv<br>

Purpose:<br>
•	This file contains one row per identified disease for each PubMed paper.<br>
•	Unlike the combined file, diseases are not flattened, meaning if an article mentions multiple diseases, each is listed in a separate row.<br>

Columns:<br>
**_pubmed_paper_id_**:	Unique identifier for the PubMed article<br>
**_Title_**:	Title of the research paper<br>
**_URL_**:	Direct link to the PubMed article<br>
**_Abstract_**:	Extracted abstract of the article<br>
**_identified_diseases_**:	A single disease identified from the abstract<br>

### 5.3 Identified Treatments File
Filename Example:<br>
carbapenem_resistance_identified_treatments.csv<br>

Purpose:<br>
•	This file contains one row per identified treatment for each PubMed paper.<br>
•	Unlike the combined file, treatments are not flattened, meaning if an article mentions multiple treatments, each is listed in a separate row.<br>

**Columns:**<br>
**_pubmed_paper_id_**:	Unique identifier for the PubMed article<br>
**_Title_**:	Title of the research paper<br>
**_URL_**:	Direct link to the PubMed article<br>
**_Abstract_**:	Extracted abstract of the article<br>
**_identified_treatments_**:	A single treatment identified from the abstract<br>



