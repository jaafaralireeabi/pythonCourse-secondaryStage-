"""
write python code to check the number is eve or odd?  

1- عرف متغير لعدد واقرأ قيمته من المستخدم

2- افحص هل العدد زوجي او فردي )العدد الزوجي يقبل القسمة على 2 
والعدد الفردي لا يقبل القسمة عليه فيبقى باقي(

"""

number = int(input("enter the number: "))

if number % 2 == 0:
    print(f"({number}) is even")
else:
    print(f"({number}) is odd")
