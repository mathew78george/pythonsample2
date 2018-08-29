import pandas as pd
import matplotlib.pyplot as plt;

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

content = pd.read_excel('Presidents.xls',sheet_name='Elected presidents')
content['Political Party'].value_counts().plot(kind='pie')
plt.legend('Political Party')
plt.plot()
plt.show()
