import json

d={}
e={}
p=[]
with open('dictionary.json') as json_file:
    data = json.load(json_file)
dictionary_items = data.items()
k=data["cars"]
my_dict={}
for index,value in enumerate(k):
  my_dict[index] = value


u=my_dict.keys()

y=my_dict[1].keys()


for i in range(len(y)):
               p1=list(my_dict[1].keys())[i]
               p.append(p1)
max1=my_dict[0]['hp']
mod1max=my_dict[0]['model']
min1=my_dict[0]['hp']
mod1min=my_dict[0]['model']
mod2max=my_dict[0]['model']
mod2min=my_dict[0]['model']
max2=my_dict[0]['year']
min2=my_dict[0]['year']
onomax=my_dict[0]['model']
onomin=my_dict[0]['model']

for i in range (len(u)):
    q=my_dict[i]['hp']
    a=my_dict[i]['year']
    w=my_dict[i]['model']
    if q>max1:
        max1=my_dict[i]['hp']
        mod1max=my_dict[1]['model']
    if q<min1:
        min1=my_dict[i]['hp']
        mod1min=my_dict[i]['model']
    if a>max2:
        mod2max=my_dict[i]['model']
        max2=my_dict[i]['year']
    if a<min2:
        mod2min=my_dict[i]['model']
        min2=my_dict[i]['year']
    if w>onomax:
        onomax=w 
    if w<onomin:
        onomin=w
for i in range(len(p)):
    print(p[i])
va = input("dwse model(modelo) h year(etos kataskevis) h hp(aloga).Se periptosi poy dwseis model ta apotelesmata emfanizontai alfavitika: : ")


search_key = va
if search_key in p:
  for i in range (len(p)):
        if search_key==p[i]:
            pos=i
            print (pos)
  if pos==1:
            print("to palaiotero amaksi einai to", mod2min,"me xronologia",min2)
            print("to neotero amaksi einai to", mod2max,"me xronologia",max2)
  if pos==2:
            print("to pio argo amaksi einai to ",mod1min,"me ",min1," aloga ")
            print("to pio grigoro amaksi einai to ",mod1max,"me ",max1," aloga ")
  if pos==0:
            print("me alfavitiki seira prwto einai to ",onomax," kai teleutaio einai to ",onomin)
else:
    print("den edwses sosto kleidi")
