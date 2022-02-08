import sys
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import read_excel

df = pd.read_excel("National_Stock_Exchange_of_India_Ltd.xlsx", sheet_name="National_Stock_Exchange_of_Indi")
print(df.to_string())
df.plot()
plt.show()
plt.savefig("result.png")
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
