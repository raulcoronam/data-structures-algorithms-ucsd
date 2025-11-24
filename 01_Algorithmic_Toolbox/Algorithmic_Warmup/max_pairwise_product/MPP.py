def max_pairwise_product(numbers):
    n = len(numbers)
    index1 = 0
    for i in range(1, n): 
        if numbers[i] > numbers[index1]: 
            index1 = i
    if index1 == 0:
        index2 = 1
    else:
        index2 = 0
    for i in range(n):
        if (numbers[i] > numbers[index2]) and (i != index1) :
            index2 = i 
    return numbers[index2] * numbers[index1]

if __name__ == '__main__':
    _ = int(input())
    input_numbers  = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
