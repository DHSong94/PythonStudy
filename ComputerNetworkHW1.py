# MaxMember - n값 변경하면서

import math

def sigma(N) :
    n=11 # n은 11부터
    P=0
    while 1 :
        result = math.factorial(N)/(math.factorial(n)*math.factorial(N-n)) # NCn 값
        one = result * (0.1**n) * (0.9**(N-n)) # 한번 계산한 값

        P+=one # 계산한 값들의 합 (시그마)
        n+=1 # n값 증가

        if(n>N):
            print("N이 %d일 때 P값은 %0.12lf입니다. %d번째 연산을 종료합니다." % (N, P, N-10))
            return P

def MaxMember():  # 최대 가입자 수(M) 구하기
    M=0
    N=11 # N은 11부터 시작

    while M < 0.01 :
        M=sigma(N)

        if(M < 0.01): # M값이 0.01보다 작으면 N값 증가시켜서 MaxMember(N) 다시 실행
            N+=1
        else:
            break

MaxMember()
#print("N이 %d일 때 M값이 %0.10lf이므로 최대 가입자수는 %d명입니다." %(N, M, N-1))