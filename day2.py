import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('panda_chart/marks.csv')
plt.scatter(data['Subject'], data['Marks'])
plt.show()
