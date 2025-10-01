
"""
🟢 BEGINNER LEVEL - Sliding Window (Fixed Size)

PROBLEM: Maximum Sum of Subarray of Size K
Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.

Example:
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9 (subarray [5, 1, 3] has sum 9)

🎯 ALGORITHMIC PATTERN: Fixed-Size Sliding Window
This is a sliding window problem because:
1. We need to examine ALL subarrays of a FIXED size k
2. Adjacent subarrays overlap significantly (only 1 element difference)
3. We can "slide" the window to avoid recalculating the entire sum

💡 APPROACH HINTS:
1. Calculate sum of first k elements (initial window)
2. Slide the window: remove leftmost element, add new rightmost element
3. Keep track of maximum sum seen so far
4. Continue until we've examined all possible windows

⏰ TIME COMPLEXITY: O(n) - we visit each element exactly once
💾 SPACE COMPLEXITY: O(1) - only storing a few variables

🔍 WHY SLIDING WINDOW WORKS HERE:
- Naive approach: Calculate sum of every k-sized subarray = O(n*k)
- Sliding window: Reuse previous calculation, just add/subtract = O(n)
- Key insight: sum[i+1...i+k] = sum[i...i+k-1] - nums[i] + nums[i+k]
"""

def max_sum_subarray_k(nums, k):
    """
    Find maximum sum of any contiguous subarray of size k.
    
    Args:
        nums: List[int] - array of integers
        k: int - size of subarray
    
    Returns:
        int - maximum sum of k-sized subarray
    """
    # EDGE CASE: Check if array is large enough
    if len(nums) < k:
        return 0  # or raise an exception
    
    # STEP 1: Calculate sum of first window (first k elements)
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
    
    # STEP 2: Initialize max_sum with first window
    max_sum = window_sum
    
    # TODO: STEP 3 - YOUR TASK: Slide the window through rest of array
    # Start from index k (the element after first window)
    for i in range(k, len(nums)):
        # TODO: SLIDING WINDOW TECHNIQUE - YOUR CORE TASK:
        # You need to update window_sum by:
        # 1. REMOVE the leftmost element of previous window: nums[i-k]
        # 2. ADD the new rightmost element of current window: nums[i]
        #window_sum -= nums[i-k]
        # HINT: Think about the relationship between windows:
        # Previous window: [nums[i-k], nums[i-k+1], ..., nums[i-1]]
        # Current window:  [nums[i-k+1], nums[i-k+2], ..., nums[i]]
        # What element is removed? What element is added?
        #
        # YOUR CODE HERE:
        # window_sum = window_sum - ??? + ???
        window_sum = window_sum + nums[i] - nums[i-k] #window_sum -nums[i-k] + nums[i]
          # Remove this line when you implement the sliding logic above
        
        # TODO: STEP 4 - YOUR TASK: Update maximum if current window sum is larger
        # HINT: Compare current window_sum with max_sum
        # YOUR CODE HERE:
        if window_sum > max_sum:
            print(f"New maximum: {max_sum} ⭐")
            max_sum  = window_sum
    
    return max_sum

def max_sum_subarray_k_verbose(nums, k):
    """
    Same algorithm but with detailed step-by-step output for learning.
    """
    if len(nums) < k:
        return 0
    
    print(f"Array: {nums}, k = {k}")
    print("=" * 50)
    
    # Calculate first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    print(f"Initial window: {nums[:k]} = {window_sum}")
    print(f"Max so far: {max_sum}")
    print()
    
    # Slide the window
    for i in range(k, len(nums)):
        old_element = nums[i - k]  # Element leaving the window
        new_element = nums[i]      # Element entering the window
        
        # Update window sum
        window_sum = window_sum - old_element + new_element
        
        # Show current window
        current_window = nums[i - k + 1:i + 1]
        print(f"Window: {current_window}")
        print(f"  Removed: {old_element}, Added: {new_element}")
        print(f"  Sum: {window_sum}")
        
        # Update maximum
        if window_sum > max_sum:
            max_sum = window_sum
            print(f"  New maximum: {max_sum} ⭐")
        else:
            print(f"  Max still: {max_sum}")
        print()
    
    return max_sum

# 🧪 TEST CASES
if __name__ == "__main__":
    # Test Case 1: Basic example
    nums1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    result1 = max_sum_subarray_k(nums1, k1)
    print(f"Test 1: {nums1}, k={k1}")
    print(f"Result: {result1}")  # Expected: 9
    print()
    
    # Detailed walkthrough of Test 1
    print("DETAILED WALKTHROUGH:")
    max_sum_subarray_k_verbose(nums1, k1)
    print("=" * 50)
    
    # Test Case 2: All negative numbers
    nums2 = [-1, -2, -3, -4, -5]
    k2 = 2
    result2 = max_sum_subarray_k(nums2, k2)
    print(f"Test 2: {nums2}, k={k2}")
    print(f"Result: {result2}")  # Expected: -3 (subarray [-1, -2])
    print()
    
    # Test Case 3: Single element window
    nums3 = [5, 2, 8, 1, 9]
    k3 = 1
    result3 = max_sum_subarray_k(nums3, k3)
    print(f"Test 3: {nums3}, k={k3}")
    print(f"Result: {result3}")  # Expected: 9

"""
🎓 LEARNING OBJECTIVES:
After solving this problem, you should understand:
1. How sliding window avoids redundant calculations
2. The add-one-remove-one pattern of fixed-size windows
3. How to maintain running sums efficiently
4. When to use sliding window vs. brute force

🔄 VARIATIONS TO TRY:
1. Minimum sum subarray of size k
2. Average of all subarrays of size k
3. First subarray with sum >= target
4. Longest subarray with sum <= target (variable window)

📝 PRACTICE TIPS:
1. Always handle edge cases (k > array length)
2. Trace through the sliding process step by step
3. Verify your window boundaries are correct
4. Think about what happens at the start and end of the array

🧠 MENTAL MODEL:
Imagine a physical window sliding across the array:
[2, 1, 5, 1, 3, 2]
[===]           <- Window at position 0: sum = 2+1+5 = 8
   [===]        <- Window at position 1: sum = 1+5+1 = 7  
      [===]     <- Window at position 2: sum = 5+1+3 = 9
         [===]  <- Window at position 3: sum = 1+3+2 = 6
"""
