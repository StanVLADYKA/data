# Создать и прочитать CSV файл с помощью Pandas.

import pandas as pd

read_f = pd.read_csv("inv.csv",sep=";")
print(read_f)