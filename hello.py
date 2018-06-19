"""
print('Hello world')

a = 1
b = 'this is a string'
c = [1, 2, 3, 4]
d = (5, 6, 7, 8)
e = {'name': 'Perry', 'number': 1}

print(a)
print(b)
print(c)
print(d)

print(len(c))
c.append(42)
print(c)
c.append('will this work?')
print(c)
print(e)

print(e['name'])
e['number'] += 9000
print(e['number'])

for n in c:
  for m in d:
    print(n * m)
"""

def count_to_one_hundred():
  for x in range(1, 101):
    print(x)


def stub_function():
  pass

def multiply_two_numbers(x, y):
  return x * y

def main():
  print ('Hello world!')

  # count_to_one_hundred()

  print(multiply_two_numbers(6, 8))
  
if __name__ == "__main__":
  main()