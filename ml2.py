import pandas as pd
import quandl


mydata = quandl.get("EIA/PET_RWTC_D")
quandl.ApiConfig.api_key = "yd1zD_AwBNs-4mgpjXgf"

print(mydata.head())
