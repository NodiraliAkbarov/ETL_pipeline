import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract_data(url:str)->dict:
    
    #Extracting from API source 

    try: 
        data = requests.get(url=url).json()
        if data != []:
            logging.info("Extracted from API source")
        else:
            logging.info("No data")
    
    except Exception as e:
            logging.error(f"{e}")

    return data