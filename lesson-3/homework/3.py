#Create a list containing five different fruits and print the third fruit.
fruits = ["avocado", "watermelon", "kiwi", "papaya", "grape"]
print(fruits[2])
#Create two lists of numbers and concatenate them into a single list.
numbers = list(range(0, 100, 2))
numbers2 = list(range(1, 101, 2))
merged = []
for a, b in zip(numbers, numbers2):
    merged.append(a)
    merged.append(b)
print(merged) #this merges 2 lists but stops at the minimum length of the two lists
#Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = list(range(1, 11))
extracted = [numbers[0], numbers[len(numbers) // 2], numbers[-1]]
print(extracted)
#Create a list of your five favorite movies and convert it into a tuple.
movies = ["Inception", "Interstellar", "Shutter Island", "Tenet", "The Pursuit of Happyness"]
movies_tuple = tuple(movies)
print(movies_tuple)
#Given a list of cities, check if "Paris" is in the list and print the result.
cities = ["New York", "London", "Tokyo", "Sydney", "Berlin"]
if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")
#Create a list of numbers and duplicate it without using loops.
numbers = list(range(1, 11))
duplicated = numbers * 2
print(duplicated)
#Given a list of numbers, swap the first and last elements.
numbers = list(range(1, 11))
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)
#Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers_tuple = tuple(range(1, 11))
print(numbers_tuple[3:8])
#Create a list of colors and count how many times "blue" appears in the list.
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
blue_count = colors.count("blue")
print(f"'blue' appears {blue_count} times in the list.")
#Given a tuple of animals, find the index of "lion".
animals = ("cat", "dog", "lion", "tiger", "elephant")
lion_index = animals.index("lion")
print(f"The index of 'lion' is {lion_index}.")
#Create two tuples of numbers and merge them into a single tuple.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)
#Given a list and a tuple, find and print their lengths.
my_list = [1, 2, 3, 4, 5]
my_tuple = (6, 7, 8, 9, 10)
print(f"Length of list: {len(my_list)} and Length of tuple: {len(my_tuple)}")
#Create a tuple of five numbers and convert it into a list.
numbers_tuple = (1, 2, 3, 4, 5)
numbers_list = list(numbers_tuple)
print(numbers_list)
#Given a tuple of numbers, find and print the maximum and minimum values.
numbers_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5)
print(f"Maximum: {max(numbers_tuple)}, Minimum: {min(numbers_tuple)}")
#Create a tuple of words and print it in reverse order.
words_tuple = ("apple", "banana", "cherry", "date", "elderberry")
reversed_tuple = words_tuple[::-1]
print(reversed_tuple)