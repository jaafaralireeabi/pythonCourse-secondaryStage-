def  main():
    name_list  =  []
    again  =  'y'
    while  again  ==  'y':
        name  =  input('Enter  a  name:  ')
        name_list.append(name)
        print('Do  you  want  to  add  another  name?') 
        again  =  input('y  =  yes,  anything  else  =  no:  ')
    for  name  in  name_list:
        print(name) 
main()
