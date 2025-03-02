# export_df_as_csv.py

# Import required libraries
import pandas as pd
import inspect
import os

# Exports dataframes as csvs to output path
def export_df_as_csv(output_path: str, 
                     main_url: str, 
                     df_combined: pd.DataFrame, 
                     df_identified_diseases: pd.DataFrame, 
                     df_identified_treatments: pd.DataFrame) -> None:
    """Exports dataframes as csvs to output path"""
    
    # Print current function name
    print("--------------------------------------------------------------------")
    print(f"Executing function: {inspect.currentframe().f_code.co_name}")  

    # Create CSV names
    try:
        csv_prefix = main_url.split("&")[0].replace("https://pubmed.ncbi.nlm.nih.gov/?term=", "").replace("+", "_")

        csv_combined = csv_prefix + "_combined.csv"
        csv_identified_diseases = csv_prefix + "_identified_diseases.csv"
        csv_identified_treatments = csv_prefix + "_identified_treatments.csv"

        print(f"Exporting the following csvs to {output_path}:"
              f"\n\t {csv_combined},"
              f"\n\t {csv_identified_diseases}," 
              f"\n\t {csv_identified_treatments}")

    except ValueError as e:
        raise ValueError(f"\n\t Error in {inspect.currentframe().f_code.co_name} function:"
                         f"\n\t Error creating csv names:" 
                         f"\n\t {e}") 
           

    # Output dataframes as CSVs to output path
    try:
        if not os.path.exists(output_path): 
        # if the demo_folder directory is not present  
            os.makedirs(output_path) 

        # Create output path variables
        csv_combined_output_path = os.path.join(output_path, csv_combined)
        csv_identified_diseases_output_path = os.path.join(output_path, csv_identified_diseases)
        csv_identified_treatments_output_path = os.path.join(output_path, csv_identified_treatments)
        
        # Export dfs to csv file path
        df_combined.to_csv(csv_combined_output_path, index=False)
        df_identified_diseases.to_csv(csv_identified_diseases_output_path, index=False)
        df_identified_treatments.to_csv(csv_identified_treatments_output_path, index=False)
        print(f"Data extraction completed and saved to CSVs! Exported to {output_path}")

    except ValueError as e:
        raise ValueError(f"\n\t Error in {inspect.currentframe().f_code.co_name} function:"
                         f"\n\t Error exporting csvs to {output_path}:"
                         f"\n\t {e}")