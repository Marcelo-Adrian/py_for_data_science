#1. Create a variable called "values" and store inside it the number from 1 to 10. Print the seventh element, and in the next line, the complete list.
def exp_01():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'Seventh element = {values[6]}')
    print(f'all values = {values}')

#2. Modify the last exp adding a variable called "numbers_in_full" that hold all the number of the last exp writting in full and a composite list. Print the numereic value and in full of the corresponding number and then the first and last in the list.
def exp_02():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_in_full = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    number_list = [values, numbers_in_full]
    print(f'Full list = {number_list}')
    print(f'First number = {number_list[0][0],number_list[1][0]}')
    print(f'Last number = {number_list[0][9],number_list[1][9]}')

#3. Create an empty list and name it "items" and add 3 strings to it: "book", "notebook" and "eraser". Change index item 1 to "ruler". Verify if the item "notebook" still is in the list. Print the lenght of the list, remove the last element and print it and then print the lenght of the list again. Create a variable called "slice" that hold the last two elements and print it.
def exp_03():
    items = []
    elements = "book", "notebook", "eraser"
    items += elements
    items[1] = "ruler"
    if "notebook" not in items:
        print("Nop")
    print(f'List lenght is = {len(items)}')
    print(f'Last element = {items.pop()}')
    print(f'New Lenght = {len(items)}')
    slice = items[-2:]
    print(f'Slice = {slice}')

#Copy the last exp and add the string "book" to the index 0 and print the list
def exp_04():
    items = []
    elements = "book", "notebook", "eraser"
    items += elements
    items[1] = "ruler"
    if "notebook" not in items:
        print("Nop")
    print(f'List lenght is = {len(items)}')
    print(f'Last element = {items.pop()}')
    print(f'New Lenght = {len(items)}')
    slice = items[-2:]
    print(f'Slice = {slice}')
    items.insert(0,"book")
    print(f'Items = {items}')

#Create a set 'A' with number from 1 to 5 and a set 'B' with all integer and even numbers from 0 to 10. Print A union B and A intersection B.
def exp_05():
    A = {1, 2, 3, 4, 5}
    B = {0, 2, 4, 8, 10}
    print(f'A union B = {A.union(B)}')
    print(f'A interserction B = {A.intersection(B)}')

def main():
    exp_01()
    exp_02()
    exp_03()
    exp_04()
    exp_05()

if __name__ == "__main__":
    main()