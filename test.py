import pickle
from sklearn.preprocessing import StandardScaler
model=pickle.load(open('/Users/prajwalsaggurthi/Desktop/Project/model3.pkl','rb'))
r = model.predict([[20221221]])

print(r)