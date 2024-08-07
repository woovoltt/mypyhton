# % 포맷 코드 : %d(decimal), %s(string), %c(character)
# %f(float)의 기본 값은 소수점 6자리까지 표시됩니다.
# %m.nf(float) : m과 n은 정수이고, m은 전체 자리수, n은 소수점 자리수입니다.

name = "김철수"
age = 30
height = 175.3456789
address = '마포'

print('이름 : %s' % (name))
print('나이 : %d' % (age))
print('키01 : %.3f' % (height))
print('키02 : [%10.4f]' % (height))
print('주소 : %s' % (address))

message = '이름은 %s이고, 나이는 %d살입니다.'
print(message % (name, age))

su = 2
bread = '단팥빵'
message = '나는 배고파서 %s %d개를 먹었습니다.'
print(message % (bread, su))

su01 = 3
su02 = 5
message = '%d 더하기 %d는 %d입니다.'
print(message % (su01, su02, (su01+su02)))

hello = '안녕' # 기호 [와 ]는 편의상 테두리 임을 알려 주는 역할
message = '[%10s]' % hello # 숫자가 양수이면, 오른쪽 정렬
print(message)

message = '[%-10s]' % hello # 숫자가 음수이면, 왼쪽 정렬
print(message)