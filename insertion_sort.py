numbers = input('Enter numbers seperated by a comma: ')
# Gets a list of nums 
numbers = [int(num.strip()) for num in numbers.split(',')] 

def insertionSort(numbers):
    for i, val in enumerate(numbers):
        j = i   # sets j = to current location in list
        
# j must be at least 1, and if so checks if current j is greater than prev j
        while j > 0 and numbers[j] < numbers[j-1]:  
            temp = numbers[j]           # sets temp to curr j
            numbers[j] = numbers[j-1]   # swaps curr j with the smaller element
            numbers[j-1] = temp         # swap j-1 with j which was set as temp
            j -= 1                      # move j back to represent the smaller ..
    return numbers                      # ..element and loop in while again

print(insertionSort(numbers))