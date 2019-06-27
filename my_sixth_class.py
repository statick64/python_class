x = {'foo', 'bar', 'baz', 'foo', 'qux'}
print(x)
x = {'q', 'u', 'u', 'x'}
print(x) 
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1|x2)
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
e = a.union(b,c,d)
print(e)
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1 & x2)
print(a&b&c&d)
print(a-b-c-d)
s = set('a', 'b', 'c')
print(s)