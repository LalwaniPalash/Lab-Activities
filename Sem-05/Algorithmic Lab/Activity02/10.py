def combination_sum(candidates, target):
    def backtrack(start, target, current_combination):
        if target == 0:
            result.append(list(current_combination))
            return
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])
            backtrack(i, target - candidates[i], current_combination)
            current_combination.pop()

    result = []
    backtrack(0, target, [])
    return result

if __name__ == "__main__":
    candidates = [2, 3, 6]
    target = 7
    result = combination_sum(candidates, target)
    print(f"Combinations that sum to {target}: {result}")
