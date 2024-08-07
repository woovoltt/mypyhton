coffee01 = ('아메리카노', '카페라떼')
coffee02 = ('콜드브루', '아이스커피')

# 요소들을 콤마로 연결하면 tuple로 인식합니다.
coffee03 = '카푸치노', '마끼야또'

mytuple = coffee01 * 3
print(mytuple)

mylist = ['바닐라라떼', '플랫화이트']
coffee04 = tuple(mylist) # 리스트를 tuple로 변환

coffees = coffee01 + coffee02 + coffee03 + coffee04 + ('에스프레소',)
length = len(coffees)
print('요소 개수 : %d' % length , '개')
print(type(coffees))
print(coffees)

# 불변성을 가지는 tuple은 값을 할당할 수 없습니다.
# coffees[1] = '우유'

# 인덱싱과 슬라이싱
print('앞에서 3번째 요소 : %s' % coffees[3])
print('뒤에서 2번째 요소 : %s' % coffees[-2])

print('1번째 부터 3번째 까지의 요소들', end='')
print(coffees[1:4])

print('4번째 이후의 모든 요소들', end='')
print(coffees[4:])

print('3번째 요소까지 출력', end='')
print(coffees[:4])

mycount = coffees.count('아메리카노')
print(mycount)

myindex = coffees.index('콜드브루')
print(myindex)

x, y = 3, 4
print('before x : %d, y : %d' % (x, y))

x, y = y, x
print('after x : %d, y : %d' % (x, y))