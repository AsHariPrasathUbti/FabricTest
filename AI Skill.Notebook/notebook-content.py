# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "bb100b1a-643c-4d47-91df-bc2349177637",
# META       "default_lakehouse_name": "AI_Skill",
# META       "default_lakehouse_workspace_id": "ab07ef75-6eb1-4835-b9c5-d7087b9e7c4c"
# META     }
# META   }
# META }

# CELL ********************

import pandas as pd
from tqdm.auto import tqdm
base = "https://synapseaisolutionsa.blob.core.windows.net/public/AdventureWorks"

# load list of tables
df_tables = pd.read_csv(f"{base}/adventureworks.csv", names=["table"])

df_tables = df_tables.head(2)

for table in (pbar := tqdm(df_tables['table'].values)):
    pbar.set_description(f"Uploading {table} to lakehouse")
    # download
    df = pd.read_parquet(f"{base}/{table}.parquet")
    # save as lakehouse table
    spark.createDataFrame(df).write.mode('overwrite').saveAsTable(table)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_tables = df_tables.head(2)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_tables.count()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import requests
import json
import pprint
from synapse.ml.mlflow import get_mlflow_env_config


# the URL could change if the workspace is assigned to a different capacity
url = "https://<generic published URL value>"

configs = get_mlflow_env_config()

headers = {
    "Authorization": f"Bearer {configs.driver_aad_token}",
    "Content-Type": "application/json; charset=utf-8"
}

question = "{userQuestion: \"what is an example product?\"}"
response = requests.post(url, headers=headers, data = question)
print("RESPONSE: ", response)
print("")
response = json.loads(response.content)
print(response["result"])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
