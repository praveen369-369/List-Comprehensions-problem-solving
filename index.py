#Generate a list of squares for even numbers and cubes for odd numbers from 1–10 using list comprehension.
for i in range(1,11):
    if i%2==0:
        print(i**2)
    else:
        print(i**3)


print([ i**2 if i%2==0 else i**3 for i in range(1,11)])


#Create a multiplication table (1–3 × 1–3) using nested list comprehension.
for i in (1,4):
    for j in range(1,4):
        print(f'{i} x {j}={i*j}')

table = [[f'{i} x {j} = {i*j}' for j in range(1, 4)] for i in range(1, 4)]

print(table)

# Extract vowels from the string "Python" and store them in a list.

n='python'
for i in n:
    if i in 'aeiouAEIOU':
        print(i)
print([i for i in n if i in 'aeiouAEIOU'])
#Generate a list of ASCII values for the characters in the string "ABC" using list comprehension.
n='ABC'
for i in n:
    print(i,ord(i))
print([(i,ord(i)) for i in n])
#Generate uppercase alphabets A–Z using list comprehension.
for i in range(65,91):
    print(chr(i))
print([chr(i) for i in range(65,91)])
# Capitalize every word in the string "hello world python" and store the result in a list.
n="hello world python"
l=[]
for i in n.split():
    l.append(i.capitalize())
m=" ".join(l)
print(m)
j=([i.capitalize() for i in n.split()  ])
print(" ".join(j))
#Print "Even" or "Odd" for numbers 1–10 using list comprehension.
print(['even' if i%2==0 else 'odd' for i in range(1,10)])

