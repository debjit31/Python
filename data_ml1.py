import pandas as pd
import Quandl 

mydata = quandl.get("EIA/PET_RWTC_D")

print(mydata.head())
