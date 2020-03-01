#!/bin/python3

from bs4 import BeautifulSoup
import re
# this is just substitution(will explain later)
r_filename = "topics.html"
f = open(r_filename,'r')

# this is the file where content would be written
w_filename = "content.txt"
p = open(w_filename,'w')

soup = BeautifulSoup(f,'html.parser')
list(soup.children)

test = []
test = list(soup.find_all('a',href = re.compile(r'[/]([a-z]|[A-Z])\w+')))

for i in test:
    p.write(str(i))
    p.write('\n')

f.close
p.close
