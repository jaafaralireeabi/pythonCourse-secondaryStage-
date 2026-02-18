# calculator آلة  حاسبة

"""
1-  تعريف متغيرين بأسم a,b على سبيل المثال لا الحصر
2- واخذ قيمتهما من المستخدم input from user
3- تعريف متغير لكل عملية حسابية )...,sum,sub,mul,div)
4- عرض نتائج كل عملية

"""

a = float(input("enter the first number: "))
b = float(input("enter the second number: "))

sum = a + b
sub = a - b
mul = a * b
div = a % b

"""
يمكنك اضافة عمليات حسابية اخرى
مختلفة حاول ان تجرب ذلك )مثل باقي القسمة او الاس او غير ذلك(
"""

print("a + b = ", sum)
print("a - b = ", sub)
print("a * b = ", mul)
print("a / b = ", div)
