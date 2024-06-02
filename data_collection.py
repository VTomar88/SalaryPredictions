import glassdoor_scraper as gs 
import pandas as pd 

# path = add your path to chromedriver
path = ""

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)