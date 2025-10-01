"""
🟢 BEGINNER LEVEL - Sliding Window (Variable Size)

PROBLEM: Longest Subarray with Sum <= K
Given an array of positive integers and a target sum k, find the length of the longest 
contiguous subarray whose sum is less than or equal to k.

Example:
Input: nums = [1, 2, 3, 4, 5], k = 8
Output: 3 (subarray [1, 2, 3] or [3, 4] both have length 3 and sum <= 8)

🎯 ALGORITHMIC PATTERN: Variable-Size Sliding Window
This is a variable sliding window problem because:
1. We don't know the size of the optimal subarray in advance
2. We need to expand/contract the window based on a condition (sum <= k)
3. We're looking for the LONGEST valid window

💡 APPROACH HINTS:
1. Use two pointers: left and right (window boundaries)
2. Expand window by moving right pointer and adding elements
3. If sum exceeds k, contract window by moving left pointer
4. Track the maximum window size seen so far
5. Continue until right pointer reaches the end

⏰ TIME COMPLEXITY: O(n) - each element is visited at most twice (once by left, once by right)
💾 SPACE COMPLEXITY: O(1) - only using pointer variables and sum

🔍 WHY VARIABLE SLIDING WINDOW WORKS HERE:
- We expand when we can (sum + next_element <= k)
- We contract when we must (sum > k)
- The window size changes dynamically based on the constraint
- Two pointers ensure we don't miss any valid subarrays
"""

def longest_subarray_sum_k(nums, k):
    """
    Find length of longest contiguous subarray with sum <= k.
    
    Args:
        nums: List[int] - array of positive integers
        k: int - maximum allowed sum
    
    Returns:
        int - length of longest valid subarray
    """
    # STEP 1: Initialize variables
    left = 0           # Left boundary of window
    window_sum = 0     # Current sum of elements in window
    max_length = 0     # Maximum length found so far
    
    # STEP 2: Expand window with right pointer
    for right in range(len(nums)):
        # EXPAND: Add current element to window
        window_sum += nums[right]
        
        # TODO: STEP 3 - YOUR TASK: Contract window if sum exceeds k
        # HINT: You need a while loop because you might need to contract multiple times
        # When should you contract? When window_sum > k
        # How do you contract? Remove nums[left] and move left pointer right
        #
        # YOUR CODE HERE:
        # while ???:
        #     # CONTRACT: Remove leftmost element from window
        #     window_sum -= ???
        #     left += ???
        
        pass  # Remove this line when you implement the contraction logic above
        
        # TODO: STEP 4 - YOUR TASK: Update maximum length
        # HINT: Current window size = right - left + 1
        # Compare with max_length and update if current window is larger
        #
        # YOUR CODE HERE:
        # current_length = ???
        # max_length = ???
    
    return max_length

def longest_subarray_sum_k_verbose(nums, k):
    """
    Same algorithm with detailed step-by-step output for learning.
    """
    print(f"Array: {nums}, k = {k}")
    print("=" * 60)
    
    left = 0
    window_sum = 0
    max_length = 0
    
    for right in range(len(nums)):
        # Expand window
        window_sum += nums[right]
        print(f"Step {right + 1}: Add nums[{right}] = {nums[right]}")
        print(f"  Window: [{left}, {right}] = {nums[left:right+1]}")
        print(f"  Sum: {window_sum}")
        
        # Contract if necessary
        while window_sum > k:
            print(f"  Sum {window_sum} > {k}, need to contract!")
            print(f"  Remove nums[{left}] = {nums[left]}")
            window_sum -= nums[left]
            left += 1
            print(f"  New window: [{left}, {right}] = {nums[left:right+1]}")
            print(f"  New sum: {window_sum}")
        
        # Update maximum
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            print(f"  New max length: {max_length} ⭐")
        else:
            print(f"  Max length still: {max_length}")
        print()
    
    return max_length

# 🧪 TEST CASES
if __name__ == "__main__":
    # Test Case 1: Basic example
    nums1 = [1, 2, 3, 4, 5]
    k1 = 8
    result1 = longest_subarray_sum_k(nums1, k1)
    print(f"Test 1: {nums1}, k={k1}")
    print(f"Result: {result1}")  # Expected: 3
    print()
    
    # Detailed walkthrough
    print("DETAILED WALKTHROUGH:")
    longest_subarray_sum_k_verbose(nums1, k1)
    print("=" * 60)
    
    # Test Case 2: All elements fit
    nums2 = [1, 1, 1, 1]
    k2 = 10
    result2 = longest_subarray_sum_k(nums2, k2)
    print(f"Test 2: {nums2}, k={k2}")
    print(f"Result: {result2}")  # Expected: 4 (entire array)
    print()
    
    # Test Case 3: Single element windows only
    nums3 = [5, 5, 5, 5]
    k3 = 4
    result3 = longest_subarray_sum_k(nums3, k3)
    print(f"Test 3: {nums3}, k={k3}")
    print(f"Result: {result3}")  # Expected: 0 (no valid subarray)
    print()
    
    # Test Case 4: Mixed sizes
    nums4 = [2, 1, 4, 1, 1, 2]
    k4 = 6
    result4 = longest_subarray_sum_k(nums4, k4)
    print(f"Test 4: {nums4}, k={k4}")
    print(f"Result: {result4}")  # Expected: 4 (subarray [1, 1, 2, 1] or similar)

"""
🎓 LEARNING OBJECTIVES:
After solving this problem, you should understand:
1. How variable sliding window adapts to constraints
2. The expand-contract pattern with two pointers
3. When to expand vs. when to contract the window
4. How to track optimal solutions during the process

🔄 VARIATIONS TO TRY:
1. Shortest subarray with sum >= k
2. Longest subarray with at most k distinct characters
3. Longest subarray with sum exactly equal to k
4. Maximum number of 1s after flipping at most k 0s

📝 PRACTICE TIPS:
1. Always think "expand when possible, contract when necessary"
2. Make sure your window boundaries are correct
3. Handle edge cases: empty array, k=0, all elements > k
4. Trace through examples to understand pointer movements

🧠 MENTAL MODEL - Window Expansion/Contraction:
nums = [1, 2, 3, 4, 5], k = 8

Step 1: [1] sum=1 ≤ 8 ✓ (expand)
Step 2: [1,2] sum=3 ≤ 8 ✓ (expand)  
Step 3: [1,2,3] sum=6 ≤ 8 ✓ (expand)
Step 4: [1,2,3,4] sum=10 > 8 ✗ (contract!)
        [2,3,4] sum=9 > 8 ✗ (contract!)
        [3,4] sum=7 ≤ 8 ✓
Step 5: [3,4,5] sum=12 > 8 ✗ (contract!)
        [4,5] sum=9 > 8 ✗ (contract!)
        [5] sum=5 ≤ 8 ✓

Maximum window size seen: 3

🔑 KEY INSIGHT:
The beauty of variable sliding window is that it automatically finds the optimal 
balance between including more elements (longer subarray) and staying within 
constraints (sum ≤ k).
"""
