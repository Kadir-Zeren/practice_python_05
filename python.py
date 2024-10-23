text = 'Clarusway'
text[0]

yeni_string = text[:5] + 'k' +text[-3:]
print(yeni_string)

text = 'AaBbCc'
print(text.lower())
text = text.lower() 


print('t' in text)
print('r' not in text)

text = 'www.clarusway.com'
print(text.endswith('.com'))
print(text.startswith('http'))

print(text.startswith('a'))
print(text.startswith('aa'))
print(text.startswith('b',2))

print('abcdeabcde'.startswith('c',2,8))

text = 'a b c d'
print(len(text))

text = 'www.clarusway.com'
print(text.endswith('.co'))

text = 'abcdef'
print(text.startswith('b',-5))

text = 'abcabcabc'
print(text.find('ca'))
print(text.find('klm'))
print(text.rfind('a'))
print(text.index('ca'))

text ='ClaRusWay'
print(text.upper())
print(text.lower())
print(text.swapcase())
print(text.replace('W','***'))
print(text.replace('W','***').lower())
print(text.replace('W','***').lower().upper())

text = text.title()
print(text)

text = 'S0d0me and G0m0re'
print(text.replace('0','o'))

isim = ' Ali '
print(isim.strip())

meslek = ' \n codder \t'
print(meslek.strip())

text = 'abcdabcd'
print(text.strip('a'))
print(text.strip('ab'))
print(text.strip('ba'))
print(text.strip('bad'))
print(text.strip('badc'))
print(text.strip('c'))

print(None or 1)

a =" "
b ="false"
c = True
d = ""
print(a or b or c or not d)

print('None or True and 1')

A = True
B = False
logic = (A or B) and (not A)
print(logic)
 
text = 'tyou can learn almost everythin in pre-classz'
print(text.strip('tz'))
print(text.strip('tz').upper())
print(text.rstrip('z'))
print(text.rstrip('z').lstrip('t'))
print(text.rstrip('z').lstrip('t').upper())

text = 'In God wee Trust'
print(text.replace('wee','we'))