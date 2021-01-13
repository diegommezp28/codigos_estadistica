from google.cloud import bigquery
from google.oauth2 import service_account

client = bigquery.Client()

QUERY = (
    'SELECT * FROM `bi202020.prueba2.Peaje` '
    'LIMIT 100')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row)