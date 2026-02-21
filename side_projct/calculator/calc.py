# calculator آلة  حاسبة

"""
1-  تعريف متغيرين بأسم a,b على سبيل المثال لا الحصر
2- واخذ قيمتهما من المستخدم input from user
3- تعريف متغير يقرأ من المستخدم، لتحديد العملية الحسابية المطلوبة
4- اذا كان المدخل opr == "+" -> res= a+b ....
4- عرض نتيجة

"""

a = float(input("enter the first number: "))
opr = input("enter the opertion (+,-,*,/,%,^): ")
b = float(input("enter the second number: "))
res = 0

if opr == "+":
    res = a + b
elif opr == "-":
    res = a - b
elif opr == "*":
    res = a * b
elif opr == "/":
    res = a / b
elif opr == "%":
    res = a % b
elif opr == "^":
    res = a ** b
else:
    print("please enter (+,-,*,/,%,^)")


print(f"{a} {opr} {b} = {res}")