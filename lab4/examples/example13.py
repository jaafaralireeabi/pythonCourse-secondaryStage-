def  main():
    #  Get  the  user's  age.
    first_age  =  int(input('Enter  your  age:  '))
    #  Get  the  user's  best  friend's  age.
    second_age  =  int(input("Enter  your  best  friend's  age:  ")) 
    total  =  sum(first_age,  second_age)
    print(total)

def  sum(num1,  num2):
    result  =  num1  +  num2 
    return  result

main()
