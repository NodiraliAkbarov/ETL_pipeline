from extraction.extract import extract_data
from transformation.transform import transform_data
from loading.load import load



if __name__== "__main__" :

    data = extract_data("http://universities.hipolabs.com/search?country=Uzbekistan")
    cleaned_data = transform_data(data)
    load(cleaned_data)