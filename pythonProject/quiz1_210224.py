# function quiz1
# 섭씨온도 -> 화씨온도
'''
def change_temparature(c):
    f = 9/5 * c + 32
    return f

print(change_temparature(10))
'''

# list and tuple 
# 다음 list의 element를 오름차순으로 정렬. 또한 내림차순으로 정렬. sort(), sort(reverse=True) 사용
# xlist = [2,1,3,5,4]
'''
xlist = [2,1,3,5,4]
xlist.sort()
print(type(xlist))

print("---오름차순---")
print(xlist)

print("---내림차순---")
xlist.sort(reverse=True)
print(xlist)

xlist.reverse()
print(xlist)
'''
# 반복자(iterator) 프로토콜을 가지고 있다면 반복시킬수 있다(__iter__) - zip, reversed, iter 등등

# sigma 만들기
import sys
'''
def sigma(n):
    sig = 0
    for k in range(1, n+1):
        sig = sig + k
    return sig
'''
'''
def sigma(n):
    return sum(list(range(1, n+1)))

if __name__ == '__main__':
    print(sys.argv)

n = int(sys.argv[1])

if type(n) == int or type(n) == float:
    print(True)
else:
    print(False)

print(sigma(n))
'''
''' =========================================================
5) 두개의 주사위를 던져서 두 주사위의 합이 같은 것끼리 출력하라.

pseudo-code
    d = {}

    Loop with 주사위1 from 1 to 6
        Loop with 주사위2 from 1 to 6
            newTuple = (주사위1, 주사위2)
            added = 주사위1 + 주사위2
            if added 가 d 에 없으면 empty list 를 d 에 추가
            d 의 기존 list 에 append
'''
'''
d={}
def main():
    for dice1 in range(1,7):
        for dice2 in range(1,7):
            dices = (dice1, dice2)
            added = dice1 + dice2
            if added not in d:
                d[added] = []
            d[added].append(dices)

    print(d)

if __name__ == '__main__':
    main()

'''



