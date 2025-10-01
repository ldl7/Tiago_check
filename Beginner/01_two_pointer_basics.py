"""
🟢 BEGINNER LEVEL - Two Pointer Technique

PROBLEM: Two Sum - Sorted Array
Given a sorted array of integers and a target sum, find two numbers that add up to the target.
Return their indices (1-indexed).

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [1, 2] (because nums[0] + nums[1] = 2 + 7 = 9)

🎯 ALGORITHMIC PATTERN: Two Pointer Technique
This is a classic two-pointer problem because:
1. The array is SORTED (key requirement for two pointers)
2. We're looking for a PAIR that satisfies a condition
3. We can eliminate possibilities by moving pointers intelligently

💡 APPROACH HINTS:
1. Use two pointers: left (start) and right (end)
2. Calculate sum = nums[left] + nums[right]
3. If sum == target: Found the answer!
4. If sum < target: We need a larger sum, so move left pointer right
5. If sum > target: We need a smaller sum, so move right pointer left
6. Continue until pointers meet

⏰ TIME COMPLEXITY: O(n) - we visit each element at most once
💾 SPACE COMPLEXITY: O(1) - only using two pointer variables

🔍 WHY TWO POINTERS WORK HERE:
- Sorted array allows us to make decisions about which pointer to move
- Moving left pointer increases the sum (larger number)
- Moving right pointer decreases the sum (smaller number)
- This eliminates the need for nested loops O(n²)
"""

def two_sum_sorted(nums, target):
    """
    Find two numbers in sorted array that add up to target.
    
    Args:
        nums: List[int] - sorted array of integers
        target: int - target sum
    
    Returns:
        List[int] - indices of the two numbers (1-indexed)
    """
    # STEP 1: Initialize two pointers
    left = 0              # Start pointer at beginning
    right = len(nums) - 1 # End pointer at end
    
    # STEP 2: Continue until pointers meet
    while left < right:
        # STEP 3: Calculate current sum
        current_sum = nums[left] + nums[right]
        
        # STEP 4: Check if we found the target
        if current_sum == target:
            return [left + 1, right + 1]  # Return 1-indexed positions
        
        # TODO: STEP 5 - YOUR TASK: Decide which pointer to move
        # HINT: Think about what happens when:
        # - current_sum < target (sum is too small)
        # - current_sum > target (sum is too large)
        # 
        # Remember: The array is SORTED!
        # - Moving left pointer RIGHT gets you a LARGER number
        # - Moving right pointer LEFT gets you a SMALLER number
        #
        # YOUR CODE HERE:
        elif current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1

        
        pass  # Remove this line when you implement the logic above
    
    # If no solution found (shouldn't happen with valid input)
    return []

# 🧪 TEST CASES - Try running these to verify your understanding
if __name__ == "__main__":
    # Test Case 1: Basic example
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum_sorted(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Result: {result1}")  # Expected: [1, 2]
    print(f"Verification: nums[{result1[0]-1}] + nums[{result1[1]-1}] = {nums1[result1[0]-1]} + {nums1[result1[1]-1]} = {nums1[result1[0]-1] + nums1[result1[1]-1]}")
    print()
    
    # Test Case 2: Numbers at the ends
    nums2 = [1, 2, 3, 4, 5]
    target2 = 6
    result2 = two_sum_sorted(nums2, target2)
    print(f"Test 2: nums={nums2}, target={target2}")
    print(f"Result: {result2}")  # Expected: [1, 5] (1+5=6)
    print()
    
    # Test Case 3: Adjacent numbers
    nums3 = [1, 3, 4, 6, 8]
    target3 = 7
    result3 = two_sum_sorted(nums3, target3)
    print(f"Test 3: nums={nums3}, target={target3}")
    print(f"Result: {result3}")  # Expected: [2, 3] (3+4=7)

"""
🎓 LEARNING OBJECTIVES:
After solving this problem, you should understand:
1. How two pointers eliminate the need for nested loops
2. Why sorting is crucial for two-pointer technique
3. How to make decisions about pointer movement
4. The time/space complexity benefits

🔄 VARIATIONS TO TRY:
1. Three Sum: Find three numbers that add to target
2. Two Sum - Closest: Find pair with sum closest to target
3. Container With Most Water: Two pointers for area maximization

📝 PRACTICE TIPS:
1. Draw the array and trace through pointer movements
2. Think about WHY each pointer movement makes sense
3. Consider edge cases: empty array, no solution, duplicate numbers
"""
