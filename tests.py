# tests.py

import os
from main import main



## TEST TO CHECK IF MAIN SCRIPT RUNS CORRECTLY USING MAIN_URL
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# api_key = os.getenv("OPENAI_API_KEY") ## ADD YOUR OPENAI_API_KEY HERE
# output_path = r"C:\Users\ANIL\Documents\Data Engineering\Python\Python fundamentals\InoviaBio_code_test\output_csv_files" ## ADD YOUR OUTPUT PATH
# main_url = "https://pubmed.ncbi.nlm.nih.gov/?term=carbapenem+resistance&filter=dates.2022%2F1%2F1-2022%2F1%2F30&filter=simsearch1.fha&filter=simsearch2.ffrft&filter=hum_ani.humans"
# # Run main function 
# main(api_key=api_key, 
#      output_path=output_path, 
#      main_url=main_url)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





## TEST CASE 1 RUN using incorrect url
# USE INCORRECT_URL
# Expect error message:
        # Error message: 
        #         Error validating url in is_valid_url function:
        #         pubmed url not provided url should start with 'https://pubmed.ncbi.nlm.nih.gov/'
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# incorrect_url = "https://www.google.com/"
# api_key = os.getenv("OPENAI_API_KEY") ## ADD YOUR OPENAI_API_KEY HERE
# output_path = r"C:\Users\ANIL\Documents\Data Engineering\Python\Python fundamentals\InoviaBio_code_test\output_csv_files"
# main_url = incorrect_url
# # Run main function 
# main(api_key=api_key, 
#      output_path=output_path, 
#      main_url=main_url)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





## TEST TO CHECK IF SCRIPT RUNS CORRECTLY BY BUILDING CUSTOM URL USING FILTERS DICT
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

api_key = os.getenv("OPENAI_API_KEY") ## ADD YOUR OPENAI_API_KEY HERE
output_path = r"E:\Users\ANIL\Documents\Data Engineering\Python\Python fundamentals\InoviaBio_code_test\output_csv_files"

# Build new main_url by populating below fields for searching PubMed
base_url = "https://pubmed.ncbi.nlm.nih.gov/" # NEEDED Add base url (ONLY works for the provided base url)
search_term = "gout" # NEEDED input term to be searched 
date_from = "2024/1/1" # OPTIONAL input date from in format: yyyy/mm/dd or yyyy/m//d or yyyy/mm/d or yyyy/m/d
date_to = "2025/1/1" # OPTIONAL input to date to in format: yyyy/mm/dd or yyyy/m//d or yyyy/mm/d or yyyy/m/d
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





## TEST CASE 2.1 BUILD URL INCORRECTLY and RUN USING api_key, output_path, filters
# DONT USE URL
# Expected error message:
        # Error message:
        #         Error building url in build_main_url function:
        #         Base URL is NOT provided! Please use 'https://pubmed.ncbi.nlm.nih.gov/'
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# no_url = ""
# api_key = os.getenv("OPENAI_API_KEY") ## ADD YOUR OPENAI_API_KEY HERE
# output_path = r"C:\Users\ANIL\Documents\Data Engineering\Python\Python fundamentals\InoviaBio_code_test\output_csv_files"

# # Build new main_url by populating below fields for searching PubMed
# base_url = no_url # NEEDED Add base url (ONLY works for the provided base url)
# search_term = "folliculitis" # NEEDED input term to be searched 
# date_from = "2022/1/1" # OPTIONAL input date from in format: yyyy/mm/dd or yyyy/m//d or yyyy/mm/d or yyyy/m/d
# date_to = "2022/1/1" # OPTIONAL input to date to in format: yyyy/mm/dd or yyyy/m//d or yyyy/mm/d or yyyy/m/d
# species = "humans" # OPTIONAL input humans or animal or leave blank to select both
# abstract_text_availability  = "yes" # NEEDED input yes or no
# free_full_text_availability  = "yes" # NEEDED input yes or no
# full_text_availability = "no" # NEEDED input yes or no

# filters = {
#     "base_url": base_url,
#     "search_term": search_term,
#     "date_from": date_from,
#     "date_to": date_to,
#     "species": species,
#     "abstract_text_availability": abstract_text_availability,
#     "free_full_text_availability": free_full_text_availability,
#     "full_text_availability": full_text_availability
# }

# # Run main function 
# main(api_key=api_key, output_path=output_path, filters=filters)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





## TEST CASE 2.2 BUILD url INCORRECTLY and RUN USING api_key, output_path, filters
# NO SEARCH TERM USED 
# expected error message:
        # Error message:
        #         Error building url in build_main_url function:
        #         search_term is required and cannot be blank! Please input search_term.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# no_search_term = ""
# api_key = os.getenv("OPENAI_API_KEY") ## ADD YOUR OPENAI_API_KEY HERE
# output_path = r"C:\Users\ANIL\Documents\Data Engineering\Python\Python fundamentals\InoviaBio_code_test\output_csv_files"

# # Build new main_url by populating below fields for searching PubMed
# base_url = "https://pubmed.ncbi.nlm.nih.gov/" # NEEDED Add base url (ONLY works for the provided base url)
# search_term = no_search_term # NEEDED input term to be searched 
# date_from = "2022/1/1" # OPTIONAL input date from in format: yyyy/mm/dd or yyyy/m//d or yyyy/mm/d or yyyy/m/d
# date_to = "2022/1/1" # OPTIONAL input to date to in format: yyyy/mm/dd or yyyy/m//d or yyyy/mm/d or yyyy/m/d
# species = "humans" # OPTIONAL input humans or animal or leave blank to select both
# abstract_text_availability  = "yes" # NEEDED input yes or no
# free_full_text_availability  = "yes" # NEEDED input yes or no
# full_text_availability = "no" # NEEDED input yes or no

# filters = {
#     "base_url": base_url,
#     "search_term": search_term,
#     "date_from": date_from,
#     "date_to": date_to,
#     "species": species,
#     "abstract_text_availability": abstract_text_availability,
#     "free_full_text_availability": free_full_text_availability,
#     "full_text_availability": full_text_availability
# }

# # Run main function 
# main(api_key=api_key, 
#      output_path=output_path, 
#      filters=filters)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





## TEST CASE 2.3 BUILD url INCORRECTLY and RUN USING api_key, output_path, filters
# USE INCORRECT DATE_FROM/DATE_TO
# expected error message:
        # Error message:
        #         Error parsing date in parse_date function:
        #         Invalid date format or non-existent date: {date_str}.
        #         Expected format: YYYY/MM/DD, YYYY/M/D, YYYY/MM/D, YYYY/M/DD.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# incorrect_date_from = "2022/01/100"
# api_key = os.getenv("OPENAI_API_KEY") ## ADD YOUR OPENAI_API_KEY HERE
# output_path = r"C:\Users\ANIL\Documents\Data Engineering\Python\Python fundamentals\InoviaBio_code_test\output_csv_files"

# # Build new main_url by populating below fields for searching PubMed
# base_url = "https://pubmed.ncbi.nlm.nih.gov/" # NEEDED Add base url (ONLY works for the provided base url)
# search_term = "folliculitis" # NEEDED input term to be searched 
# date_from = incorrect_date_from # OPTIONAL input date from in format: yyyy/mm/dd or yyyy/m//d or yyyy/mm/d or yyyy/m/d
# date_to = "2022/1/1" # OPTIONAL input to date to in format: yyyy/mm/dd or yyyy/m//d or yyyy/mm/d or yyyy/m/d
# species = "humans" # OPTIONAL input humans or animal or leave blank to select both
# abstract_text_availability  = "yes" # NEEDED input yes or no
# free_full_text_availability  = "yes" # NEEDED input yes or no
# full_text_availability = "no" # NEEDED input yes or no

# filters = {
#     "base_url": base_url,
#     "search_term": search_term,
#     "date_from": date_from,
#     "date_to": date_to,
#     "species": species,
#     "abstract_text_availability": abstract_text_availability,
#     "free_full_text_availability": free_full_text_availability,
#     "full_text_availability": full_text_availability
# }

# # Run main function 
# main(api_key=api_key, 
#      output_path=output_path, 
#      filters=filters)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





## TEST CASE 2.4 BUILD url INCORRECTLY and RUN USING api_key, output_path, filters
# USE INCORRECT SPECIES
# expected error message:
        # Error message:
        #         Error building url in build_main_url function:
        #         Provide species as ('humans', 'animal') or leave blank if not needed.
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# incorrect_species = "aliens"
# api_key = os.getenv("OPENAI_API_KEY") ## ADD YOUR OPENAI_API_KEY HERE
# output_path = r"C:\Users\ANIL\Documents\Data Engineering\Python\Python fundamentals\InoviaBio_code_test\output_csv_files"

# # Build new main_url by populating below fields for searching PubMed
# base_url = "https://pubmed.ncbi.nlm.nih.gov/" # NEEDED Add base url (ONLY works for the provided base url)
# search_term = "folliculitis" # NEEDED input term to be searched 
# date_from = "2022/1/1" # OPTIONAL input date from in format: yyyy/mm/dd or yyyy/m//d or yyyy/mm/d or yyyy/m/d
# date_to = "2022/1/1" # OPTIONAL input to date to in format: yyyy/mm/dd or yyyy/m//d or yyyy/mm/d or yyyy/m/d
# species = incorrect_species # OPTIONAL input humans or animal or leave blank to select both
# abstract_text_availability  = "yes" # NEEDED input yes or no
# free_full_text_availability  = "yes" # NEEDED input yes or no
# full_text_availability = "no" # NEEDED input yes or no

# filters = {
#     "base_url": base_url,
#     "search_term": search_term,
#     "date_from": date_from,
#     "date_to": date_to,
#     "species": species,
#     "abstract_text_availability": abstract_text_availability,
#     "free_full_text_availability": free_full_text_availability,
#     "full_text_availability": full_text_availability
# }

# # Run main function 
# main(api_key=api_key, 
#      output_path=output_path, 
#      filters=filters)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

