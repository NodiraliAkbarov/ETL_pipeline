import pandas as pd
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def transform_data(data:dict)->pd.DataFrame:

    try : 

        df = pd.DataFrame(data=data)

        #Filtering only State universities
        df = df[df['name'].str.contains("State")]

        #Removing square brackets
        df['domains'] = df['domains'].str.get(0)

        #Resetting index
        df=df.reset_index(drop=True)

        logging.info("Succesfully transformed data")
   
    except Exception as e:
        
        logging.error(f"{e} error occured")

    #Returning neccesary columns

    return df[['name','domains','country']]
