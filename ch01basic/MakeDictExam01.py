coffees = dict() # empty dict

coffees['에스프레소'] = 1000
coffees['에스프레소'] = 1500

coffees['카페라떼'] = 2000
coffees['카푸치노'] = 3000
coffees['마끼야또'] = 4000
print(coffees)

targetItem = '카페라떼'
bool = targetItem in coffees
print(bool)

if bool:
    print('%s키가 있습니다.' % targetItem)
else:
    print('%s키가 없습니다.' % targetItem)

# '핫초코'가 있는지 확인하고 없으면 5000원으로 추가해 보세요.
targetItem = '핫초코'
bool = targetItem in coffees

if not bool:
    coffees[targetItem] = 5000

print(coffees.keys())

print(coffees.values())

price = 6000
bool = price in coffees.values()

if bool:
    print('%d짜리 품목이 존재합니다.' % price)
else:
    print('품목이 존재 하지 않아서 추가합니다.')
    coffees['아이스커피'] = price

listCoffee = ['바닐라라떼', '라벤더', '딸기라떼', '콜드브루']

for idx in range(len(listCoffee)):
    coffees[listCoffee[idx]] = (idx + 7) * 1000

targetList = ['라벤더', '우유커피']

for key in targetList:
    try:
        price = coffees[key]
        message = '품명 : %s, 가격 : %d' % (key, price)
        print(message)
    except KeyError:
        print('%s가 존재 하지 않아서 신규 추가 합니다.' % key)
        coffees[key] = 5000
    # end try
# end for

targetItem = '둥글레차'
price = coffees.get(targetItem, 3000)
print('품명 : %s, 가격 %d' % (targetItem, price))

del coffees['에스프레소']

for (key, value) in coffees.items():
    message = '항목 %s의 단가는 %d원 입니다.' % (key, value)
    print(message)
# end for

# 500원 인상 : '카페라떼', '카푸치노'
# 500원 인하 : '핫초코'
for key in coffees.keys():
    if key == '카페라떼' or key == '카푸치노':
        coffees[key] += 500
    elif key == '핫초코':
        coffees[key] -= 500
    else:
        pass

    message = '항목 %s의 단가는 %d원 입니다.' % (key, coffees[key])
    print(message)
    # end if
# end for

coffees.clear()

if len(coffees) == 0:
    print('mydict is empty')
else:
    print('mydict is not empty')

# print(coffees)

