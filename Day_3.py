import numpy as np
import pandas as pd 

number = np.arange(0,100)

dist = np.linspace(0,1,5)

rand = np.random.rand(100) #uniform
randn = np.random.randn(100) #normal distribution

data = np.random.randint(1,100, size=(100,5))

print(np.sum(data))
print(np.mean(data))
print(np.std(data))

print(np.sum(data, axis = 0))

new = data >50
new_data = data[new]

A = np.array([[1,2],[4,5]])
B = np.array([[4,7],[9,7]])

C = np.dot(A,B)

inverse_A = np.linalg.inv(A)

print(C)
print(inverse_A)

df = pd.read_csv(r"C:\Users\milan\OneDrive\Desktop\train.csv")
print(df.head())

df.tail(3)     
df.info()       
df.describe()   
df.shape        
df.columns

df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B'],
    'Value': [10, 15, 10, 20]
})


grouped = df.groupby('Category').sum()

df.isnull().sum()         
df.fillna(0)               

print(df[['Category', 'Value']])
print(df.iloc[0])  


print(df.loc[0, 'Value'])