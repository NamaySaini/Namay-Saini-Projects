from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import json
from os.path import join
import pandas as pd
data1 = pd.read_csv(r"/Users/namaysaini/Library/CloudStorage/OneDrive-Personal/Desktop/Teliatry/data_trial01_finapresPPG.csv")
data2 = pd.read_csv(r"/Users/namaysaini/Library/CloudStorage/OneDrive-Personal/Desktop/Teliatry/data_trial01_finapresBP.csv")
data1.tail()
data2.tail()
data2.drop([6346,16919])
features = extract_features(ppgdata)
x = data1["FinapresPPG"]
y = data2["FinapresBP"]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
lr = LinearRegression()
lr.fit(x_train, y_train)
predict = lr.predict(x_test)
score = lr.score(x_test, y_test)
print(score)
