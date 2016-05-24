# Author : Arjo Ghosh আর্য্য ঘোষ

import requests
x=input("Enter username : ")
x=x.strip()
y=input("Enter password : ")
params = {'user': x, 'pass': y, 'login':'Login'}
r = requests.post("http://10.254.254.24/0/up/", data=params)
if r.status_code==200:
    print('Your Internet connection is configured properly.')
else:
   print('Something went wrong. Please try again later.')
