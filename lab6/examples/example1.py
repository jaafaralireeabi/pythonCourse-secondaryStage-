LOOK_UP  =  1
ADD  =  2
QUIT  =  5

def main():
    birthdays = {}
    choice = 0
    while choice !=QUIT :
          choice  =  get_menu_choice()
          if choice==LOOK_UP:
             look_up(birthdays)
          elif choice==ADD:
             add(birthdays)

def get_menu_choice():
    print('1.  Look  up  a  birthday') 
    print('2.  Add  a  new  birthday') 
    choice  =  int(input('Enter  your  choice:  '))
    while  choice  <  LOOK_UP  or  choice  >  QUIT: 
        choice  =  int(input('Enter  a  valid  choice:  '))
    return  choice

def  look_up(birthdays):
     name  =  input('Enter  a  name:  ') 
     print(birthdays.get(name,  'Not  found.'))
def add(birthdays):
    name = input('enter a name: ')
    bday = input('enter a birth day: ')
    if name not in birthdays:
        birthdays[name]  =  bday 
    else:
         print('That  entry  already  exists.')

main()

