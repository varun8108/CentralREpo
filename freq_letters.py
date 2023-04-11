string = "google.com"

#To find the frequency of all letters in string

emp = {}
for i in string:
    if i in emp.keys():
        emp[i] = emp[i]+1
    else:
        emp[i] = 1