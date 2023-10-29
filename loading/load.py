import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

#Loading environmental variables
load_dotenv()

def connecting():

    try: 
        connect = psycopg2.connect(
            host = os.environ.get('host'),
            database=os.environ.get('db'),
            port=os.environ.get('port'),
            user=os.environ.get('user'),
            password=os.environ.get('password'))
        

        #Checking connection by checking postgres version
        cur = connect.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()

        if version is not None:
            logging.info("Connected to database")
    
    except Exception as e:
        logging.error(f"{e}")

    return connect

def load(data:pd.DataFrame):

    
    create_table = "CREATE TABLE IF NOT EXISTS universities \
            (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, domains VARCHAR(30) NOT NULL, \
             country VARCHAR(50) NOT NULL)"
    
    insert_data = "INSERT INTO universities(name, domains, country) values(%s, %s, %s)"
    
    conn = connecting()

    cursor = conn.cursor()
    

    #Creating table
    try: 
        cursor.execute(create_table)
        logging.info("Created table")
    except Exception as e:
        logging.error(f"{e}")
    

    #Inserting data by converting dataframe into list of tuples
    try:
       cursor.executemany(insert_data, data.to_records(index=False)) 
       logging.info("Inserted rows")
    except Exception as e:
        logging.error(f"{e}")

    conn.commit()
    cursor.close()
    conn.close()

    
        
    


    