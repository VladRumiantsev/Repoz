mixed_list = [33,"mouse", 6, False, "keyboard", "monitor", 2, { 'gpu': 'headset' }, [1, 2, 3]]
string_count = 0
for element in mixed_list:
    if type(element) == str:  
        string_count += 1  
print("string elements in the list:", string_count)