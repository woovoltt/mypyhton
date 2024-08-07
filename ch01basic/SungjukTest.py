# SungjukTest.py
def sungjukInfo(name, kor, eng = 50, math = 60):
    total = kor + eng + math
    average = total / 3.0

    if average >= 70.0:
        passOrFail = '합격'
    else:
        passOrFail = '불합격'

    print('%s 학생의 정보' % name)
    print('국어 : %d, 영어 : %d, 수학 : %d' % (kor, eng, math))
    print('총점 : %d, 평균 : %.2f, 합격 여부 : %s' % (total, average, passOrFail))
# end def

name, kor, eng, math = '김철수', 50, 60, 70
sungjukInfo(name, kor, eng, math) # positional argument
sungjukInfo('박영희', 80) # positional argument

sungjukInfo(math=30, eng=90, name='심현철', kor=100) # keyword argument

sungjukInfo('권유정', 50, math=70) # 혼합 형태