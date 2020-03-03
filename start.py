from media import *
from research import *
import os

print("\t\tWelcome to new feeds!!")
print('=============================================================================================')
print("So today which section do you want to explore")
print("1. Want some your favorite vedios")
print('2. Want to know what is happenning around the globe')
print('3. Have some research to do')
print('=============================================================================================')
choice = int(input("So,  what do you want to do??\n"))

if choice==1:
    print('=============================================================================================')
    opeartion()
elif choice==2:
    print('=============================================================================================')
    print('Get ready for news')

elif choice==3:
    print('=============================================================================================')
    do_research()
else:
    print('Your Bad!! You entered something wrong!!')
