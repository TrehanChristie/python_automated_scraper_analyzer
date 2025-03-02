# llm_text_extractor.py

import openai
import re
import json
import inspect
from openai import OpenAI

# Function to run LLM model
def llm_text_extractor(articles: list, api_key: str) -> list:
    """Iterates through the abstract from each article, submits the abstract to openai gpt-3.5-turbo llm model 
    and extracts identified diseases and treatments from the abstract text and adds them into the articles"""

    # Print current function name
    print("--------------------------------------------------------------------")
    print(f"Executing function: {inspect.currentframe().f_code.co_name}")  
    
    client = OpenAI(api_key=api_key)

    for article in articles:
        if article["abstract"]:
            abstract = article["abstract"]

            identified_diseases = []
            identified_treatments = []

            try:
                # Call OpenAI API to extract diseases and treatments and return in JSON format
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "Extract diseases and treatments from the given text and return them in JSON format."},
                        {"role": "user", "content": abstract}
                    ]
                )
                
                # Retrieve model response and parse using JSON
                output_text = response.choices[0].message.content
                output_data = json.loads(output_text)
                
                # Extract diseases and treatments from response
                identified_diseases = output_data.get("diseases", [])
                identified_treatments = output_data.get("treatments", [])

            except Exception as e:
                print(f"An error whilst running the llm model for pubmed_paper_id: {article['pubmed_paper_id']} with url {article['url']}"
                      f"\n\t {e}")

            # Add identified_diseases and identified_treatments to respective article
            article["identified_diseases"] = identified_diseases
            article["identified_treatments"] = identified_treatments

            # Print results      
            print(f"LLM model extracted below data for PubMed ID: {article['pubmed_paper_id']}, URL: {article['url']}")                             
            print(f"Identified Diseases: {identified_diseases}")
            print(f"Identified Treatments: {identified_treatments}")
            print("-----------------")             
            
        else:
            # For acrticles without any abstract text
            print(f"Cannot run llm text extractor on {article['pubmed_paper_id']} with url {article['url']} as there is no abstract provided.")

    return articles