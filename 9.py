#using match method

import re

text='this is python language .python  is high-level language'

result=re.match("python",text)

if result :
    print(result.group())

else:
    print('not matched')

#using search method
text='this is python language it is high-level language'

result=re.search("python",text)

if result :
    print(result.group())

else:
    print('not matched')


#using search method
text='this is python language python is high-level language'

result=re.findall("python",text)

print(result)



 
