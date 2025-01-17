# List = a data type for collecting and storing
# other data types into one variable.
# - we can store any data type inside of a list, including
# other lists.
# - we can store duplicate data inside of lists.
# - we can locate and access data in a list.
# by its index position.
# - listis are changable. we can add and remove things from
# them.

skii_trip_items= ['snow boots','heavy coat']

# append() method - allows us to add items to a list.
# the new added item will be added to the back of the
# list.
skii_trip_items.append('gloves')
skii_trip_items.append('thick socks')
print(skii_trip_items)


#insert() method - allows us to add an item to a list,
# and also dictate what position that item will be at.
# insert takes two arguments, the index where you want to 
# place the data, and the acutal data.

skii_trip_items.insert(2,'goggles')
print(skii_trip_items)

# pop() method - allows us to remove the last item in a list.

skii_trip_items.pop()
print(skii_trip_items)

# remove ()  method- allos us to remove an item from the list.
# based specificallly on the data's value

skii_trip_items.remove('snow boots')
print(skii_trip_items)

# clear() method - allows us to delete the entire list.
skii_trip_items.clear()
print(skii_trip_items)

# del function
# del skii_trip_items

# def clothingBySeason():
   # summerClothes= []
   # winterClothes= []
    
   # clothingSelection= input('what are you wearing?')
   # if clothingSelection == 'tee-shirt':
    # summerClothes.append('tee-shirt')
   # print('here is your summer collection')
    # print(summerClothes)

# clothingBySeason()

# def favoriteRestarunt():
    # restaunts = ['wendys' ,'chick-fillet','kfc']
    # response = input('what is your favorite restarunt?')
    # print(' your faviorite restarunt is' + response)