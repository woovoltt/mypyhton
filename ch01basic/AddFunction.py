def add(first, second):
    return first + second
# end def

su01 = 14
su02 = 5

result = add(su01, su02) # positional argument
print('%d + %d = %d' % (su01, su02, result))

result = add(first=10, second=20) # keyword argument
print('%d + %d = %d' % (10, 20, result))

result = add(100, 200) # positional argument
print('%d + %d = %d' % (su01, su02, result))