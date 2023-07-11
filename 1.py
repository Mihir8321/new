text=input("enter a text")
import re
x=re.findall(r'[a-zA-Z0-9._+%]+@[a-zA-Z0-9._+%]+[.][a-zA-Z0-9]+',text)
print(x)