def  main():
      numbers  =  get_values()
      print(numbers)
def  get_values():
      values  =  []
      again  =  'y'
      while  again  ==  'y':
            num = int(input('Enter  a  number:  ')) 
            values.append(num)
            again = input('y = yes, anything else = no: ')
      return values

main()