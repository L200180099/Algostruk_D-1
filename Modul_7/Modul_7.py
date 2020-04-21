import re

##########    1  ###############
a = open('Indonesia.txt','r')
baca = a.read()
a.close
cocok= re.findall(r"\sme\w+",baca)
print(cocok)
print("###############################################")

##########    2  ###############
a = open('Indonesia.txt','r')
baca = a.read()
a.close
cocok= re.findall(r"di\w+",baca)
print(cocok)
print("###############################################")

##########    3  ###############
a = open('Indonesia.txt','r')
baca = a.read()
a.close
cocok= re.findall(r"di\s\w+",baca)
print(cocok)
##print("###############################################")

##########    4  ###############
f = open('KEI.html','r',encoding='latin1')
teks = f.read()
f.close()

####step 1
pola4 = r'(\w+)</a></td>'
num4= re.findall(pola4,teks)
print(num4)
print("#################")

##step 2
pola5 = r'(\w+)</a></td>\n<td>(\d.\d+)'
tuples = re.findall(pola5,teks)
print(tuples)

##step 3
print("#################")
tupp = [(t[0], float(t[1]))for t in tuples]
print (tupp)



