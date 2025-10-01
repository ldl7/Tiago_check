"""
🟢 BEGINNER LEVEL - Binary Search (Basic)

PROBLEM: Search in Sorted Array
Given a sorted array of integers and a target value, return the index of the target 
if it exists, otherwise return -1.

Example:
Input: nums = [1, 3, 5, 7, 9, 11, 13], target = 7
Output: 3 (because nums[3] = 7)

🎯 ALGORITHMIC PATTERN: Binary Search
This is a binary search problem because:
1. The array is SORTED (key requirement)
2. We're looking for a specific TARGET value
3. We can eliminate half the search space in each step

💡 APPROACH HINTS:
1. Use two pointers: left and right (search boundaries)
2. Calculate middle index: mid = (left + right) // 2
3. Compare nums[mid] with target:
   - If equal: found the target!
   - If nums[mid] < target: search right half (left = mid + 1)
   - If nums[mid] > target: search left half (right = mid - 1)
4. Continue until left > right (target not found)

⏰ TIME COMPLEXITY: O(log n) - we halve the search space each time
💾 SPACE COMPLEXITY: O(1) - only using a few variables

🔍 WHY BINARY SEARCH WORKS:
- Sorted array allows us to make decisions about which half to search
- Each comparison eliminates half of the remaining possibilities
- This is much faster than linear search O(n) for large arrays
"""

def binary_search(nums, target):
    """
    Search for target in sorted array using binary search.
    
    Args:
        nums: List[int] - sorted array of integers
        target: int - value to search for
    
    Returns:
        int - index of target if found, -1 otherwise
    """
    # STEP 1: Initialize search boundaries
    left = 0                # Start of search range
    right = len(nums) - 1   # End of search range
    
    # STEP 2: Continue searching while range is valid
    while left <= right:
        # STEP 3: Calculate middle index
        # Use (left + right) // 2, but be careful of overflow in other languages
        mid = (left + right) // 2
        
        # TODO: STEP 4 - YOUR TASK: Compare middle element with target and decide which half to search
        # HINT: You need to handle three cases:
        # 1. nums[mid] == target: Found it! Return the index
        # 2. nums[mid] < target: Target is in RIGHT half, move left boundary
        # 3. nums[mid] > target: Target is in LEFT half, move right boundary
        #
        # YOUR CODE HERE:
        # if nums[mid] == target:
        #     return ???
        # elif nums[mid] < target:
        #     # Target is in the right half
        #     left = ???
        # else:  # nums[mid] > target
        #     # Target is in the left half  
        #     right = ???
        
        pass  # Remove this line when you implement the comparison logic above
    
    # STEP 5: Target not found
    return -1

def binary_search_verbose(nums, target):
    """
    Same algorithm with detailed step-by-step output for learning.
    """
    print(f"Searching for {target} in {nums}")
    print("=" * 60)
    
    left = 0
    right = len(nums) - 1
    step = 1
    
    while left <= right:
        mid = (left + right) // 2
        
        print(f"Step {step}:")
        print(f"  Search range: [{left}, {right}]")
        print(f"  Elements in range: {nums[left:right+1]}")
        print(f"  Middle index: {mid}, Middle value: {nums[mid]}")
        
        if nums[mid] == target:
            print(f"  🎯 Found target {target} at index {mid}!")
            return mid
        
        elif nums[mid] < target:
            print(f"  {nums[mid]} < {target}, search right half")
            left = mid + 1
        
        else:
            print(f"  {nums[mid]} > {target}, search left half")
            right = mid - 1
        
        print(f"  New search range: [{left}, {right}]")
        print()
        step += 1
    
    print(f"❌ Target {target} not found in array")
    return -1

def binary_search_first_occurrence(nums, target):
    """
    Find the FIRST occurrence of target in a sorted array with duplicates.
    This is a common variation of binary search.
    """
    left = 0
    right = len(nums) - 1
    result = -1  # Store the first occurrence index
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            result = mid  # Found target, but keep searching left for first occurrence
            right = mid - 1  # Continue searching in left half
        
        elif nums[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return result

# 🧪 TEST CASES
if __name__ == "__main__":
    # Test Case 1: Basic example
    nums1 = [1, 3, 5, 7, 9, 11, 13]
    target1 = 7
    result1 = binary_search(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Result: {result1}")  # Expected: 3
    print()
    
    # Detailed walkthrough
    print("DETAILED WALKTHROUGH:")
    binary_search_verbose(nums1, target1)
    print("=" * 60)
    
    # Test Case 2: Target not found
    nums2 = [1, 3, 5, 7, 9, 11, 13]
    target2 = 6
    print(f"Test 2: nums={nums2}, target={target2}")
    result2 = binary_search_verbose(nums2, target2)
    print(f"Result: {result2}")  # Expected: -1
    print("=" * 60)
    
    # Test Case 3: Target at boundaries
    nums3 = [2, 4, 6, 8, 10]
    
    # First element
    target3a = 2
    result3a = binary_search(nums3, target3a)
    print(f"Test 3a: nums={nums3}, target={target3a}")
    print(f"Result: {result3a}")  # Expected: 0
    
    # Last element
    target3b = 10
    result3b = binary_search(nums3, target3b)
    print(f"Test 3b: nums={nums3}, target={target3b}")
    print(f"Result: {result3b}")  # Expected: 4
    print()
    
    # Test Case 4: Array with duplicates
    nums4 = [1, 2, 2, 2, 3, 4, 5]
    target4 = 2
    result4_any = binary_search(nums4, target4)
    result4_first = binary_search_first_occurrence(nums4, target4)
    print(f"Test 4: nums={nums4}, target={target4}")
    print(f"Any occurrence: {result4_any}")    # Could be 1, 2, or 3
    print(f"First occurrence: {result4_first}") # Expected: 1
    print()
    
    # Test Case 5: Single element
    nums5 = [42]
    target5 = 42
    result5 = binary_search(nums5, target5)
    print(f"Test 5: nums={nums5}, target={target5}")
    print(f"Result: {result5}")  # Expected: 0

"""
🎓 LEARNING OBJECTIVES:
After solving this problem, you should understand:
1. How binary search eliminates half the search space each time
2. The importance of maintaining correct loop invariants
3. How to handle boundary conditions (left, right, mid calculations)
4. Why binary search only works on sorted data

🔄 VARIATIONS TO TRY:
1. Find first/last occurrence of target in array with duplicates
2. Search in rotated sorted array
3. Find peak element in array
4. Search for insertion position (lower_bound/upper_bound)

📝 PRACTICE TIPS:
1. Always verify the array is sorted before applying binary search
2. Be careful with integer overflow: use left + (right - left) // 2 in some languages
3. Pay attention to loop termination conditions (left <= right vs left < right)
4. Test edge cases: empty array, single element, target at boundaries

🧠 MENTAL MODEL - Search Space Elimination:
Array: [1, 3, 5, 7, 9, 11, 13], Target: 7

Step 1: [1, 3, 5, 7, 9, 11, 13]  mid=9 > 7, search left
Step 2: [1, 3, 5, 7]              mid=3 < 7, search right  
Step 3: [5, 7]                    mid=5 < 7, search right
Step 4: [7]                       mid=7 = 7, found!

Each step eliminates ~half of remaining elements!

🔑 KEY INSIGHTS:
1. Binary search is a "divide and conquer" algorithm
2. The key insight is that sorted data allows us to make elimination decisions
3. Always maintain the invariant: "if target exists, it's in [left, right]"
4. The algorithm naturally handles the case when target doesn't exist

💡 WHEN TO USE BINARY SEARCH:
- Searching in sorted arrays
- Finding insertion points
- Optimization problems (binary search on answer)
- Any problem where you can eliminate half the possibilities each step
"""
