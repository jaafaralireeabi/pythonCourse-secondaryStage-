def  main():
    food  =  ['Pizza',  'Burgers',  'Chips']
    print(food)
    item  =  input('Which  item  should  I  change?  ') 
    try:
        item_index  =  food.index(item)
        new_item  =  input('Enter  the  new  value:  ') 
        food[item_index]  =  new_item
        print(food)
    except  ValueError:
             print('That  item  was  not  found  in  the  list.')

main()
