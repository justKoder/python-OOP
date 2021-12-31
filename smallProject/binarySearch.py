item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def binary_search(item, target_element, low, high):
    if low > high:
        return False
    else:
        i = (low + high)//2
    if target_element == item[i]:
        print("Got it at ", i)
        return True
    elif target_element < item[i]:
        return binary_search(item, target_element, low, (i - 1))
    elif target_element > item[i]:
        return binary_search(item, target_element, (i + 1), high)
    else:
        print("Not Found")
        return False

binary_search(item, 11, 0, 14)
    
