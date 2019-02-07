#%%
#LIST
list1=[1,2,3,4,5,6]
list2=["lul","lul1","lul2","lel"]
#%%
list1[-1]
list1[0:3]
##
dir(list1)
##list1 ile kullanılabilecek fonksiyonları gösterir
#%%
list1.append(7)
list1.remove(7)
list1.reverse()
print(list1)
list1.sort()
print(list1)
#%%
#TUPLE
t=(1,2,3,4,5,5,6,7)
dir(t)
print(t.count(5))#5 adetini yazdırır
print(t.index(4))#indexteki değeri yazdırır
#%%

dictionary={"keys":"values","eda":21,"göz":23}
print(dictionary)
dictionary["eda"]   