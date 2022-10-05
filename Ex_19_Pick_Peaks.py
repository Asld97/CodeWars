def pick_peaks(arr):
    testing_dict = {"pos": [], "peaks": []}
    item_index = []
    for item in range(1, len(arr) - 1):
        if arr[item] > arr[item - 1] and arr[item] > arr[item + 1]:
            testing_dict["peaks"].append(arr[item])
            testing_dict["pos"].append(item)
            item_index = []
        elif item_index and arr[item] > arr[item + 1]:
            testing_dict["peaks"].append(arr[item])
            testing_dict["pos"].append(item_index[0])
            item_index = []
        if arr[item] == arr[item + 1] and arr[item - 1] < arr[item]:
            item_index.append(item)

    return testing_dict


testing_arr_v1 = [1, 2, 3, 6, 4, 1, 2, 3, 2, 1]
testing_arr_v2 = [1, 1, 1, 1]
testing_arr_v3 = [3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]
testing_arr_v4 = [1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]
testing_arr_v5 = [2, 1, 3, 2, 2, 2, 2, 1]
print(pick_peaks(testing_arr_v1))
print(pick_peaks(testing_arr_v2))
print(pick_peaks(testing_arr_v3))
print(pick_peaks(testing_arr_v4))
print(pick_peaks(testing_arr_v5))

