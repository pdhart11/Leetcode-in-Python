class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = 0
        k = 0 
        index = 0
        my_array = []
        final_list = []
        s.split()
        if numRows == 1:
            return s
        for element in range(len(s)):
            if i == numRows - 1:
                my_array.append(i)
                i = i - 1
            elif i == 0:
                my_array.append(i)
                i = i + 1
            elif i < my_array[element-1]:
                my_array.append(i)
                i = i - 1
            else:
                my_array.append(i)
                i = i + 1
        while index <= len(my_array):
            if index == len(s):
                index = 0
                k = k + 1
            elif my_array[index] == k:
                final_list.append(s[index])
                index = index + 1
            elif len(s) == len(final_list):
                break
            else:
                index = index + 1
        final_string = ''.join(final_list)
        return final_string
