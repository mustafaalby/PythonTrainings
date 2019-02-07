#%%
def deneme(a,b):
    if(a<b):
        print(a,' ',b,'den küçüktür')
    elif(b<a):
        print(b ,' ', a, 'den küçüktür')
    else:
       print ("eşitler")
#%%
liste=[1,2,3,4,5,6]
value=3
if value in liste:
    print("evet", value," değeri liste içerisinde")
else:
    print(value," değeri liste içerisinde yok")

#%%
for each in range(1,6):
    print(each)
for each in "ankara","istanbul":
    print(each)
#%%
i=0
while(i<5):
    print(i)
    i=i+1