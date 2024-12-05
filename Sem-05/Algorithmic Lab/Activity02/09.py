def permute(s):
    def backtrack(start, end):
        if start == end:
            permutations.append(''.join(s))
        else:
            for i in range(start, end):
                s[start], s[i] = s[i], s[start]
                
                backtrack(start + 1, end)
                
                s[start], s[i] = s[i], s[start]

    permutations = []
    s = list(s) 
    backtrack(0, len(s))
    return permutations

if __name__ == "__main__":
    input_string = "abc"
    result = permute(input_string)
    print(f"All permutations of '{input_string}': {result}")
