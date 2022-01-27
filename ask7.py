from collections import Counter
d={}
y={}
with open("dictionary.txt", "r") as f:
    for line in f:
        (key,val,val2,val3,val4,val5,val6,val7)=line.split(",")
        d[key]=val,val2,val3,val4,val5,val6,val7

keys = d.keys()
print(keys)

dictionary_items = d.items()

va = input("Enter one of the names: ")

 
search_key = va
 
if search_key in d: 
    print(d.get(va))
    y=d.get(va)
    print("to megalutero stoixeio einai",max(y, key=int))
    print("to mikrotero stoixeio einai",min(y, key=int))
    counts = Counter(y)
    top = counts.most_common(1)
    print("to stoixeio poy emfanistike tis perisoteres fores eina to",top,"fores emfanistike")
    


          
else: 
     print("The key does not exist in the dictionary.") 