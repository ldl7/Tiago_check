# 📊 Big-O Complexity Analysis Guide

Understanding time and space complexity is crucial for algorithmic problem solving. This guide covers everything you need to know about Big-O notation and complexity analysis.

## 🎯 What is Big-O Notation?

Big-O notation describes the **worst-case** performance of an algorithm as the input size grows. It helps us:
- Compare different algorithms
- Predict how algorithms scale
- Make informed decisions about which approach to use

## 📈 Common Time Complexities (Best to Worst)

### O(1) - Constant Time
**Examples:** Array access, hash map lookup, stack push/pop
```python
def get_first_element(arr):
    return arr[0]  # Always takes same time regardless of array size
```

### O(log n) - Logarithmic Time  
**Examples:** Binary search, heap operations, balanced tree operations
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### O(n) - Linear Time
**Examples:** Single loop through array, linear search
```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:  # Visit each element once
        max_val = max(max_val, num)
    return max_val
```

### O(n log n) - Linearithmic Time
**Examples:** Efficient sorting (merge sort, heap sort), divide and conquer
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # log n levels
    right = merge_sort(arr[mid:])   # log n levels
    
    return merge(left, right)       # O(n) merge at each level
```

### O(n²) - Quadratic Time
**Examples:** Nested loops, bubble sort, selection sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):          # Outer loop: n times
        for j in range(n-1):    # Inner loop: n times
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

### O(2ⁿ) - Exponential Time
**Examples:** Recursive Fibonacci, subset generation, brute force solutions
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Each call makes 2 more calls
```

## 💾 Common Space Complexities

### O(1) - Constant Space
Using a fixed amount of extra space regardless of input size
```python
def reverse_array_inplace(arr):
    left, right = 0, len(arr) - 1  # Only using 2 variables
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

### O(n) - Linear Space
Space grows proportionally with input size
```python
def create_frequency_map(arr):
    freq = {}  # Could store up to n unique elements
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq
```

### O(log n) - Logarithmic Space
Typically from recursive call stack
```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
    # Call stack depth is log n
```

## 🔍 Complexity Analysis by Pattern

### Two Pointer Technique
- **Time:** O(n) - each element visited at most once
- **Space:** O(1) - only using pointer variables
```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:  # O(n) iterations max
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
```

### Sliding Window
- **Time:** O(n) - each element added and removed at most once
- **Space:** O(1) or O(k) depending on what we track
```python
def max_sum_subarray_k(nums, k):
    window_sum = sum(nums[:k])  # O(k)
    max_sum = window_sum
    
    for i in range(k, len(nums)):  # O(n-k) = O(n)
        window_sum = window_sum - nums[i-k] + nums[i]  # O(1)
        max_sum = max(max_sum, window_sum)
    
    return max_sum
# Total: O(n) time, O(1) space
```

### Binary Search
- **Time:** O(log n) - search space halved each iteration
- **Space:** O(1) iterative, O(log n) recursive
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:  # O(log n) iterations
        mid = (left + right) // 2  # O(1)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
# Time: O(log n), Space: O(1)
```

### Hash Map Operations
- **Time:** O(1) average for insert/lookup/delete, O(n) worst case
- **Space:** O(n) for storing n elements
```python
def two_sum(nums, target):
    seen = {}  # O(n) space in worst case
    
    for i, num in enumerate(nums):  # O(n) iterations
        complement = target - num
        if complement in seen:  # O(1) average lookup
            return [seen[complement], i]
        seen[num] = i  # O(1) average insertion
    
    return []
# Time: O(n), Space: O(n)
```

### Prefix Sums
- **Time:** O(n) preprocessing, O(1) per query
- **Space:** O(n) for prefix array
```python
class PrefixSum:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:  # O(n) preprocessing
            self.prefix.append(self.prefix[-1] + num)
    
    def range_sum(self, i, j):
        return self.prefix[j+1] - self.prefix[i]  # O(1) query

# Space: O(n), Time: O(n) + O(1) per query
```

### Monotonic Stack
- **Time:** O(n) - each element pushed and popped at most once
- **Space:** O(n) - stack can hold up to n elements
```python
def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # O(n) space worst case
    
    for i, temp in enumerate(temperatures):  # O(n) iterations
        while stack and temperatures[stack[-1]] < temp:  # Amortized O(1)
            prev_day = stack.pop()
            result[prev_day] = i - prev_day
        stack.append(i)
    
    return result
# Time: O(n), Space: O(n)
```

## 🧮 How to Analyze Complexity

### Step 1: Identify the Basic Operations
- What operations are performed most frequently?
- Are there nested loops?
- Are there recursive calls?

### Step 2: Count the Operations
- How many times is each operation performed?
- How does this relate to the input size n?

### Step 3: Find the Dominant Term
- Focus on the term that grows fastest
- Ignore constants and lower-order terms
- Express in Big-O notation

### Example Analysis:
```python
def example_function(arr):
    # Step 1: O(n) - single loop
    for i in range(len(arr)):
        print(arr[i])
    
    # Step 2: O(n²) - nested loops  
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                print(f"{arr[i]} > {arr[j]}")
    
    # Step 3: O(log n) - binary search
    target = arr[0]
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

# Total complexity: O(n) + O(n²) + O(log n) = O(n²)
# The quadratic term dominates
```

## ⚡ Optimization Strategies

### Time Optimization
1. **Eliminate nested loops** with hash maps or two pointers
2. **Use binary search** instead of linear search on sorted data
3. **Precompute results** (prefix sums, memoization)
4. **Choose better algorithms** (merge sort vs bubble sort)

### Space Optimization
1. **Reuse input space** when possible
2. **Use iterative instead of recursive** solutions
3. **Process data in chunks** for large datasets
4. **Use bit manipulation** for boolean arrays

## 🎯 Complexity Cheat Sheet

| Algorithm/Pattern | Time | Space | When to Use |
|------------------|------|-------|-------------|
| Two Pointers | O(n) | O(1) | Sorted arrays, pairs |
| Sliding Window | O(n) | O(1) | Subarrays, substrings |
| Binary Search | O(log n) | O(1) | Sorted data, optimization |
| Hash Map | O(n) | O(n) | Fast lookups, counting |
| Prefix Sums | O(n) + O(1) | O(n) | Range queries |
| Monotonic Stack | O(n) | O(n) | Next greater/smaller |
| Heap Operations | O(log n) | O(n) | Priority queues, top K |
| DFS/BFS | O(V+E) | O(V) | Graph traversal |
| Dynamic Programming | O(n²) typical | O(n) | Optimization problems |

## 🚨 Common Mistakes

### Mistake 1: Ignoring Hidden Complexity
```python
# This looks like O(n) but string concatenation is O(n)
def join_strings(strings):
    result = ""
    for s in strings:  # O(n) iterations
        result += s    # O(n) string concatenation each time!
    return result      # Total: O(n²)

# Better: O(n)
def join_strings_better(strings):
    return "".join(strings)  # O(n) total
```

### Mistake 2: Not Considering Average vs Worst Case
```python
# Hash map operations are O(1) average, O(n) worst case
# In practice, usually O(1), but be aware of worst case
```

### Mistake 3: Forgetting Space Complexity
```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Time: O(n) - much better than O(2^n)
# Space: O(n) - for memoization table + O(n) call stack
```

## 🎓 Practice Tips

1. **Always analyze complexity** for every solution you write
2. **Compare different approaches** and understand trade-offs
3. **Consider both time and space** complexity
4. **Think about best, average, and worst cases**
5. **Practice estimating** before calculating exactly
6. **Understand amortized analysis** for advanced problems

Remember: **Correctness first, then optimize!** A working O(n²) solution is better than a broken O(n) attempt. 🚀
