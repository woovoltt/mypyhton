def girlFriendCheck(findName):
    girlFriend = ['은하', '소원', '유주', '예린', '신비', '엄지']
    isMember = findName in girlFriend

    if isMember:
        message = '\'%s\'님은 여자친구 멤버 입니다.' % findName
        print(message)
    else:
        message = '\'%s\'님은 여자친구 멤버가 아닙니다.' % findName
        raise Exception(message)
# end def

name = '소원'

try:
    girlFriendCheck(name)
except Exception as err:
    print('예외 발생 : {}'.format(err))