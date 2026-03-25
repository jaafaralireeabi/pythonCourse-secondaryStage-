def  main():
    cars =  ['BMW',  'Toyota',  'Kia',  'Hyundai'] 
    search  =  input('Enter  a  product  number:  ')
    if  search  in  cars:
        print(search,  'was  found  in  the  list.') 
    else:
        print(search,  'was  not  found  in  the  list.')

main()
