import math

N=52
n=11
P=0

while 1 :

    result = math.factorial(N)/(math.factorial(n)*math.factorial(N-n)) # NCn 값
    one = result * (0.1**n) * (0.9**(N-n)) # 한번 계산한 값

    P = P + one
    print('n이 %d일 때, one은 %0.10e, P는 %0.10e입니다.' % (n, one, P))
    n = n + 1

    if(n>N):
        print("연산을 종료합니다.")
        break

    if(P >= 0.01):
        print("P=%0.10lf Happy Happy" % P)
        break