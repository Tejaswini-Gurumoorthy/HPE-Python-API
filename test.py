import requests

BASE= "http://127.0.0.1:5000"
COUNTSETS= "/countsets"
COUNTPANDAS= "/countpandas"

# Edit this to test the API with a timestamp of your choice.
TIMESTAMP= "/2015-08-04 00:02:05"

# Edit this to test the API with an optional end timestamp of your choice.
OPTIONAL_TIMESTAMP= "/"

## Uncomment the below code to test the API that uses dataframes from the Pandas Library. 
## Make sure to check if the program "main_pandas.py" is already up and running.
## Comment the below code if the url with COUNTSETS is being used currently.

response= requests.get(BASE + COUNTPANDAS +TIMESTAMP+ OPTIONAL_TIMESTAMP)

## Uncomment the below code to test the API that uses the sets data structure in Python. 
## Make sure to check if the program "main_sets.py" is already up and running.
## Comment the below code if the url with COUNTPANDAS is being used currently.

#response= requests.get(BASE + COUNTSETS +TIMESTAMP + OPTIONAL_TIMESTAMP)

print(response.json()) 