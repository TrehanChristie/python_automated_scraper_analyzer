# articles_to_dataframe.py

# Import required libraries
import pandas as pd
import inspect
from typing import Tuple

# Function to add articles to dataframe
def articles_to_dataframe(articles: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Converts articles into a pandas DataFrames for structured analysis."""
    
    # Print current function name
    print("--------------------------------------------------------------------")
    print(f"Executing function: {inspect.currentframe().f_code.co_name}")  

    # Create the combined dataset with the list of diseases and treatments flattened
    try:
        combined_data = []
        for article in articles:
            combined_data.append({
                "pubmed_paper_id": article.get("pubmed_paper_id", ""),
                "paper_title": article.get("paper_title", ""),
                "url": article.get("url", ""),
                "abstract": article.get("abstract", ""),
                "identified_diseases_combined": ", ".join(article.get("identified_diseases", [])),
                "identified_treatments_combined": ", ".join(article.get("identified_treatments", []))
            })
        
        # Create DataFrame
        df_combined = pd.DataFrame(combined_data)
        print(f"Dataframe df_combined created")

    except ValueError as e:
        raise ValueError(f"\n\t Error in {inspect.currentframe().f_code.co_name} function: "
                         f"\n\t Error creating combined dataset: {e}") 

    # Create dataset for identified_diseases
    try:
        identified_diseases_data = []
        for article in articles:
            for identified_disease in article["identified_diseases"]:
                if identified_disease:
                    identified_diseases_data.append({
                        "pubmed_paper_id": article.get("pubmed_paper_id", ""),            
                        "identified_diseases": identified_disease
                    })
        
        # Create DataFrame
        df_identified_diseases = pd.DataFrame(identified_diseases_data) 
        print("Dataframe df_identified_diseases created")

    except ValueError as e:
        raise ValueError(f"\n\t Error in {inspect.currentframe().f_code.co_name} function:"
                         f"\n\t Error creating dataset for identified_diseases:"
                         f"\n\t {e}")     

    # Create dataset for identified_treatments
    try:
        identified_treatments_data = []
        for article in articles:
            for identified_treatment in article["identified_treatments"]:
                if identified_treatment:
                    identified_treatments_data.append({
                        "pubmed_paper_id": article.get("pubmed_paper_id", ""),           
                        "identified_treatments": identified_treatment
                    })

        # Create DataFrame
        df_identified_treatments = pd.DataFrame(identified_treatments_data)  
        print("Dataframe df_identified_treatments created")

    except ValueError as e:
        raise ValueError(f"\n\t Error in {inspect.currentframe().f_code.co_name} function: "
                         f"\n\t Error creating dataset for identified_treatments: {e}")      
    
    return df_combined, df_identified_diseases, df_identified_treatments