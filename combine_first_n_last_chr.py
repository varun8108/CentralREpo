string = "w3resource"
string1 = "w4resource edge"


#Now combine the first and the last characters of given string.
ch_frnt = ""
ch_lst = ""

for i in range(2):
    if i==0:
        ch_frnt = string[:2]
    if i==1:
        ch_lst = string[-2::]
for i in range(2):
    if i==0:
        ch_frnt = string1[:2]
    if i==1:
        ch_lst = string1[-2::]
print(ch_frnt+ch_lst)
