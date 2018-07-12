# Assignment 3

'''

Loops in a program go over a particular set of actions repeatedly until a condition is met/not met.
Below is a list with a set of numbers as given below. Print out all the even numbers in the sequence.
Write the solution (in Python 3) into a function and have it called in your main block for the requested
answer.

numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615,
83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907,
344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248,
866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742,
717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]

eg:
find_even()
output : The even numbers are : 2,4,6,8

'''

# Solution to Assignment 3

numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]
# print('Type: ', type(numbers), '\n\nContent of numbers: -> numbers\n', numbers)
# print("\nThe actual number sequence string: -> numbers[0]['sequence']\n", numbers[0]['sequence'])
# print("\nConverted to list: -> numbers[0]['sequence'].split(', ')\n",numbers[0]['sequence'].split(', '),'\n')
      
def find_even(n):
    even_numbers = ''
    for i in numbers[0]['sequence'].split(', '):
        # print(type(i))
        # print(i)
        if ((int(i) % 2) == 0):
            if even_numbers == '':
                even_numbers += i
                # print(even_numbers )
            else:
                even_numbers = even_numbers + ',' + i
                # print(even_numbers)
    return even_numbers

print('The even numbers are :', find_even(numbers))