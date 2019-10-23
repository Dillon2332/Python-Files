array_of_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 100, 1233, 133]

def chop(num, array):
        index_val = len(array)




        first_half = array[:int(len(array)/2)]
        second_half = array[int(len(array)/2):]
        print(f"First half: {first_half}")
        print(f"Second half: {second_half}")
        if num not in first_half and num not in second_half:
                print("-1")
        elif first_half == [] or second_half == []:
                print("Done")
                print(index_val-1)
        elif num in first_half:
                index_val = [range(0, int(len(array/2)))]
                print(index_val)
                chop(num, first_half)
        elif num in second_half:
                index_val = [range((int(len(array)/2)), len(array))]
                print(index_val)
                chop(num, second_half)
chop(100, array_of_int)
