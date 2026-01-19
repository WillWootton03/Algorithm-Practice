numbers = input('Enter numbers seperated by a comma: ')
# Gets a list of nums 
numbers = [int(num.strip()) for num in numbers.split(',')] 

def insertionSort(numbers):
    for i in range(len(numbers)):
        j = i   # sets j = to current location in list

# j must be at least 1, and if so checks if current j is greater than prev j
        while j > 0 and numbers[j] < numbers[j-1]: 
            # swaps curr j with the smaller element and swap j-1 with j which was set as temp
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            # move j back to represent the smaller element and loop in while again
            j -= 1
    return numbers                      

print(insertionSort(numbers))