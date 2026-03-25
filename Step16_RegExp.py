data:str = 'Hello, World!'

import re

data:str = 'apple, banana, cherry'

result = re.findall(r'a', data)

print(result)

text:str = 'Contact: 010-1111-2222.'

m_obj = re.search(r'010-[0-9]{4}-[0-9]{4}', text)

print(m_obj)

print(m_obj.group())