#%%
#Pandas Practices
import pandas as pd
dictionary= {"Name":["Mustafa","Eda","Berkay","Gözde"],
            "Age":[24,17,11,22],
            "Salary":[5000,2000,1000,5000]}
dataFrame1=pd.DataFrame(dictionary)

#%%
dataFrame1.head(5)#dataframe içerisindeki ilk 5 değeri döndürür
dataFrame1.tail(5)#dataframe içerisindeki son 5 değeri döndürür
#%%
print(dataFrame1.columns)#sütun isimlerini verir
print("------")
print(dataFrame1.info())#dataframe hakkında bilgiler verir
print("------")
print(dataFrame1.dtypes)#dataframe sütunlarının data typelarını verir
print("------")
print(dataFrame1.describe())#dataframe e ait istatistiksel bilgiler verir
#%%
###Indexing and Slicing
print((dataFrame1["Name"]))#sadece isim sütununu almak istiyoruz
print(dataFrame1.Name)#bu şekilde de çağırılabilir

dataFrame1["YeniSutun"]=[1,2,3,4]
print(dataFrame1.head())
#%%
print(dataFrame1.loc[:2,"Age"])
print("------")
print(dataFrame1.loc[:,"Name":"Salary"])
print("------")
print(dataFrame1.loc[:2,["Age","Salary"]])
print("------")
print(dataFrame1.loc[::-1,:])
print("------")
print(dataFrame1.iloc[:,2])#integer index ile sütun ismi yerine index ile çağırma
#%%
#Filtre
filtre1=dataFrame1.Salary>3000
print(filtre1)
print("------")
filteredData=dataFrame1[filtre1]
print(filteredData)
print("------")
filtre2=dataFrame1.Age>23
print(filtre2)
dataFrame1[filtre1 & filtre2]
print(dataFrame1)
print("------")
print(dataFrame1.Age>15)
#%%
#list comprehension
ortalamaMaas=dataFrame1.Salary.mean()
dataFrame1["MaasSeviyesi"]=["yuksek" if ortalamaMaas> each else "dusuk" for each in dataFrame1.Salary]
print(dataFrame1)

dataFrame1.columns=[each.lower() for each in dataFrame1.columns]#dataframe sütun isimlerini küçük harflerle yaz
dataFrame1
#%%
#Data Concatenating Data
dataFrame1.drop(["yenisutun"],axis=1,inplace=True)

data1=dataFrame1.head
data2=dataFrame1.tail
dataConcat= pd.concat([data1,data2],axis=0)
dataConcat



#%%
