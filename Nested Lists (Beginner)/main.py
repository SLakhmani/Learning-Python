# Creating 3 lists with placeholders, "_"
row1 = ["_","_","_"]
row2 = ["_","_","_"]
row3 = ["_","_","_"]

# Create a list of lists using the above lists 
map = [row1, row2, row3]

# print rows
print(f"{row1}\n{row2}\n{row3}")

# Take user input to place the treasure
position = input("Where do you want to put the treasure? (Column number followed by row number, Eg. 23)")

# decrement indices to prevent out of bound error
column_index = int(position[0]) - 1
row_index = int(position[1]) - 1

# update map list
map[row_index][column_index] = 'X'

# print rows to see treasure position
print(f"{row1}\n{row2}\n{row3}")
