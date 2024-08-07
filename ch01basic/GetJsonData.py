filename = 'jumsu.json'

# 'rt'는 텍스트 모드로 읽어 들이겠습니다.
myfile = open(filename, mode='rt', encoding='UTF-8')
mystring = myfile.read()
print(type(mystring))
myfile.close()

import json
jsonData = json.loads(mystring)
print(type(jsonData))

humanList = list()

for human in jsonData:
    name = human['name']
    print('이름 : %s' % name)

    kor = float(human['kor'])
    eng = float(human['eng'])
    math = float(human['math'])

    total = kor + eng + math

    _gender = human['gender'].upper() # 반대는 lower()
    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'

    print(type(human))
    if 'hello' in human.keys():
        message = human['hello']
        print('메세지 : ', message)
    # end if

    mytuple = (name, kor, eng, math, total)
    humanList.append(mytuple)
# end for

print(humanList)