#소수를 판단할 방법부터

# def is_prime(number):
#     for n in range(2, number//2 +1):  #2부터, 어떤수의 절반까지 중에 약수가 없으면 소수임
#         if number%n == 0:  #약수를 찾았다. 소수가 아니다
#             return False
#     return True

# def solution(answers):  >>> 부분집합생성함수,숫자 순서가 포함안됨
#     n = len(answers)
#     for i in range(1<<n):
#         for j in range(n):
#             if i & (i<<j):
#                 print(answers[j], end=", ")
#         print()
#     print()

a = list('123')
a2 = ['']*(len(a)-1) + a

tmp_number_list = []
# for i in range(len(a2)^len(a)):  # 5^3
#     tmp_number = []
#     for j in range(len(a2)):
#         tmp_number += a2[j] #
#         a2.pop(j) ###
#         for k in range(len(a2)):
#             tmp_number += a2[k]  #
#             a2.pop(k)  ###
#             for m in range(len(a2)):
#                 tmp_number += a2[m]  #
#                 a2.pop(m)  ###
#     tmp_number_list.append(tmp_number)
cnt = 0
tmp_number_list = []
k=0
for i in range(len(a2)^len(a)): 숫자 125개 만들거
    tmp_number = []
    for j in range(len(a2)):
        tmp_number += a2[j+k]  #
        # a2.pop(j)

    k += 1


    tmp_number_list.append(tmp_number)

print(tmp_number_list)
# print(tmp_number_list)
# print(a)
# print(a2)
# print([]+['1'])


