def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    
    table = [[0] * (n + 1) for _ in range(m + 1)]
    
    max_length = 0
    
    end_index = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_index = i
            else:
                table[i][j] = 0
    
    longest_common_substring = str1[end_index - max_length: end_index]
    return longest_common_substring

str1 = "abcdxyz"
str2 = "xyzabcd"
print("Longest common substring:", longest_common_substring(str1, str2))
