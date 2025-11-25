x = "Samia"
y = 'Samia'
print(x)
print(y)
# Single line string
x = "Samia"
# Multilines string
z = '''my name is Samia 
and whats your name brother where 
are you from '''
print(z)

# Strings are Arrays(indexing like arrays)
a = "Samia Sajid"
print(a[1])

# Looping through the string

for x in "Orange":
  print(x)
# String length
a = "Samia Sajid"
print(len(a))

# Check string 

txt = "Great course by sharad khare and i like this course very much"
print("much" in txt)

txt = "Great course by sharad khare and i like this course very much"
print("mucher" in txt)

# Check string with If for user friendly 
txt = "Great course by sharad khare and i like this course very much"
if "much" in txt:
  print("Yes , 'much' is present in string")

# Check  If "much" is not present
txt = "Great course by sharad khare and i like this course very much"
print("mucher" not in txt)

# print only if "mucher" is not present
txt = "Great course by sharad khare and i like this course very much"
if "mucher" not in txt:
  print("No , 'mucher' is not present in string")