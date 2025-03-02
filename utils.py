# utils.py

# Import required libraries
import inspect
import validators
import requests
import re
from datetime import datetime
from typing import Optional

# Function to validate url
def is_valid_url(url: str) -> bool:
    """Checks if the URL is valid and accessible."""

    # Print current function name
    print("--------------------------------------------------------------------")
    print(f"Executing function: {inspect.currentframe().f_code.co_name}")  

    # Check if url is valid
    if validators.url(url):
        try:
            # Check if url is Pubmed url 
            if not url.startswith("https://pubmed.ncbi.nlm.nih.gov/"):
                raise ValueError(f"\n\t Error validating url in {inspect.currentframe().f_code.co_name} function: "
                                 "\n\t pubmed url not provided url should start with 'https://pubmed.ncbi.nlm.nih.gov/'")
            
            # Check if url is accessible
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return True
            else:
                raise ValueError(f"\n\t Error validating url in {inspect.currentframe().f_code.co_name} function: "
                                "\n\t url provided received status code {response.status_code}")
        except requests.RequestException as e:
            raise ValueError(f"\n\t Error validating url in {inspect.currentframe().f_code.co_name} function: "
                            f"\n\t Error message for url provided:" 
                            f"\n\t {e}")
    else: 
        raise ValueError(f"\n\t Error validating url in {inspect.currentframe().f_code.co_name} function: "
                        "\n\t Invalid URL format")
    

# Date parser function to be used by validate_date() function
def parse_date(date_str: str) -> Optional[datetime]:
    """Tries different accepted date formats and converts to a valid datetime object."""

    # Print current function name
    print("--------------------------------------------------------------------")
    print(f"Executing function: {inspect.currentframe().f_code.co_name}")  

    # Return None if date is empty
    if not date_str:
        return None  

    ## Corrected valid formats list (Now contains all variations)
    valid_formats = ["%Y/%m/%d", "%Y/%-m/%-d", "%Y/%m/%-d", "%Y/%-m/%d"]
    
    for date_format in valid_formats:
        try:
            parsed_date = datetime.strptime(date_str, date_format)  # Convert to datetime object
            return parsed_date  # Return the valid datetime object
        except ValueError:
            continue  # Try next format

    raise ValueError(f"\n\t Error parsing date in {inspect.currentframe().f_code.co_name} function: "
                    "\n\t Invalid date format or non-existent date: {date_str}."
                    "\n\t Expected format: YYYY/MM/DD, YYYY/M/D, YYYY/MM/D, YYYY/M/DD.")


# Function to Validate Date Format USED BY validate_date() function
def validate_date(date_from: str, date_to: str) -> None:
    """Validate if dates are in expected formats and ensures date_from is <= date_to."""

    # Print current function name
    print("--------------------------------------------------------------------")
    print(f"Executing function: {inspect.currentframe().f_code.co_name}")  

    # Ensure both date_from and date_to are present
    if not date_from or not date_to:
        raise ValueError(f"\n\t Error validating date in {inspect.currentframe().f_code.co_name} function: "
                        "\n\t Provide both `date_from` and `date_to`, or leave both blank.\n"
                        "\t If using a date filter, ensure both dates are entered in one of the following formats:\n"
                        "\t Expected format: YYYY/MM/DD, YYYY/M/D, YYYY/MM/D, YYYY/M/DD.")

    # Convert to datetime objects and check if date is valid
    from_date = parse_date(date_from)
    to_date = parse_date(date_to)

    # Ensure date_from is not after date_to
    if from_date and to_date and from_date > to_date:
        raise ValueError(f"\n\t Error validating date in {inspect.currentframe().f_code.co_name} function: "
                        f"\n\t Invalid date range: date_from({date_from}) cannot be later than date_to({date_to}).")

    print(f"Valid date range: {date_from} to {date_to}")


# Function to Build Main URL
def build_main_url(filters: dict[str, str]) -> str:
    """Builds a PubMed search URL using the filters provided in the dictionary."""

    # Print current function name
    print("--------------------------------------------------------------------")
    print(f"Executing function: {inspect.currentframe().f_code.co_name}")  

    # Check if base url is provided and matches required url
    base_url = filters.get("base_url", "")
    print(f"Using base_url: {base_url} to build main_url")
    if not base_url: 
        raise ValueError(f"\n\t Error building url in {inspect.currentframe().f_code.co_name} function: "
                        f"\n\t Base URL is NOT provided! Please use 'https://pubmed.ncbi.nlm.nih.gov/'")
    elif base_url != "https://pubmed.ncbi.nlm.nih.gov/":
        raise ValueError(f"\n\t Error building url in {inspect.currentframe().f_code.co_name} function: "
                        f"\n\t Base URL is INCORRECT! Please use 'https://pubmed.ncbi.nlm.nih.gov/'")

    # Pick up search_term and format string as per url requirements
    search_term = filters.get("search_term").replace(" ", "+")
    if not search_term: 
        raise ValueError(f"\n\t Error building url in {inspect.currentframe().f_code.co_name} function: "
                        f"\n\t search_term is required and cannot be blank! Please input search_term.")
    if not re.search(r"[a-zA-Z]", search_term):
        raise ValueError(f"\n\t Error building url in {inspect.currentframe().f_code.co_name} function: "
                        f"\n\t search_term must contain at least one letter (A-Z or a-z). Please provide a valid serach_term.")

    # Date filters (validate before adding) and format string as per url requirements
    date_from = filters.get("date_from", "")
    date_to = filters.get("date_to", "")
    if date_from or date_to:
        validate_date(date_from, date_to)
    date_filter = f"dates.{date_from}-{date_to}" if date_from and date_to else "" 
    
    # check if Species is in humans/animal/"" and format string as per url requirements
    species_text = filters.get("species", "").lower()
    if species_text not in ("humans", "animal", ""):
        raise ValueError(f"\n\t Error building url in {inspect.currentframe().f_code.co_name} function: "
                        f"\n\t Provide species as ('humans', 'animal') or leave blank if not needed.")
    species_filter = f"hum_ani.{species_text}" if species_text in ("humans", "animal") else ""
    
    # check if abstract_text_availability filter in yes/no and format string as per url requirements
    abstract_text = filters.get("abstract_text_availability", "").lower()
    if abstract_text not in ("yes", "no"):
        raise ValueError(f"\n\t Error building url in {inspect.currentframe().f_code.co_name} function: "
                        f"\n\t Provide abstract_text_availability as ('yes', 'no').")
    abstract_filter = "simsearch1.fha" if abstract_text == "yes" else ""

    # check if free_full_text_availability filter in yes/no and format string as per url requirements
    free_text = filters.get("free_full_text_availability", "").lower()
    if free_text not in ("yes", "no"):
        raise ValueError(f"\n\t Error building url in {inspect.currentframe().f_code.co_name} function: "
                        f"\n\t Provide free_full_text_availability as ('yes', 'no').")
    free_text_filter = "simsearch2.ffrft" if free_text == "yes" else ""

    # check if full_text_availability filter in yes/no and format string as per url requirements
    full_text = filters.get("full_text_availability", "").lower()
    if full_text not in ("yes", "no"):
        raise ValueError(f"\n\t Error building url in {inspect.currentframe().f_code.co_name} function: "
                        f"\n\t Provide full_text_availability as ('yes', 'no').")
    full_text_filter = "simsearch1.fha" if full_text == "yes" else ""

    # Construct filters list (remove empty strings)
    filters_list = [date_filter, abstract_filter, free_text_filter, full_text_filter, species_filter]
    filters_list = [f for f in filters_list if f]  # Remove empty entries

    # Construct full URL
    main_url = f"{base_url}?term={search_term}" + "".join([f"&filter={f}" for f in filters_list])
    print(f"Successfully completed building main_url: {main_url}")

    # Validate constructed url
    result = is_valid_url(main_url)
    if result is not True:
        raise ValueError(f"Error validating built main_url: {result}") 
    print(f"built main_url is validated ({main_url})")
    
    return main_url