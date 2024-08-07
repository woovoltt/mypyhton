print('파일에 기록합니다.')
myfile01 = open('mem.txt', mode='w', encoding='UTF-8')
print(type(myfile01))

members = ['홍영식', '김민수', '박진철', '강호숙']

for mem in members:
    message = '\'%s\'님 안녕하세요.\n' % mem
    myfile01.write(message)
# end for

myfile01.close()

print('기존 파일에 추가합니다.')
myfile02 = open('mem.txt', mode='a', encoding='UTF-8')

members = ['신유빈', '김진호', '하형주']

for idx in range(len(members)):
    message = '%d번째 고객님 : %s님\n' % (idx+1, members[idx])
    myfile02.write(message)
# end for

myfile02.close()

print('with 구문을 사용하면 close() 함수를 사용하지 않아도 됩니다.')
with open('mem.txt', mode='w', encoding='UTF-8') as testfile:
    testfile.write('가나다\n')
    testfile.write('abc\n')
    testfile.write('123\n')

    print('hello~~world', file=testfile)
# end with