#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，
# 奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高
# 于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%
# ；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万
# 元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输
# 入当月利润I，求应发放奖金总数？

#方法一
# reword = 0.00
# benfit = int(input('请输入利润金额'))
# if benfit <= 100000:
#     reword = benfit*0.1
# elif benfit > 100000 and benfit <= 200000:
#     reword = (benfit-100000)*0.075+10000
# elif benfit > 200000 and benfit <= 400000:
#     reword = (benfit-200000)*0.05+17500
# elif benfit > 400000 and benfit <=600000:
#     reword = (benfit-400000)*0.03+27500
# elif benfit > 600000 and benfit <=1000000:
#     reword = (benfit-400000)*0.015+33500
# else :
#     reword = (benfit-1000000)*0.01+37500
# print('奖金='+str(reword)+'元')

#方法二：
i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0.00
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print((i-arr[idx])*rat[idx]) 
        i=arr[idx]
print(r)
print(r）