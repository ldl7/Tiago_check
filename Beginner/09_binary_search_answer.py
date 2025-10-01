"""
🟢 BEGINNER LEVEL - Binary Search on Answer Space

PROBLEM: Find Minimum in Rotated Sorted Array
A sorted array has been rotated at some unknown pivot. Find the minimum element.
All elements are unique.

Example:
Input: nums = [3,4,5,1,2]
Output: 1

Input: nums = [4,5,6,7,0,1,2]  
Output: 0

Input: nums = [11,13,15,17]
Output: 11

🎯 ALGORITHMIC PATTERN: Binary Search on Answer Space
This is binary search on answer space because:
1. We're not searching for a specific value in the array
2. We're searching for a PROPERTY (the minimum element)
3. We can eliminate half the search space by checking which half is sorted
4. The answer space is the range of possible minimum positions

💡 APPROACH HINTS:
1. Use binary search with left and right pointers
2. Compare nums[mid] with nums[right] to determine which half is sorted
3. If nums[mid] > nums[right]: minimum is in right half
4. If nums[mid] < nums[right]: minimum is in left half (including mid)
5. Continue until left == right

⏰ TIME COMPLEXITY: O(log n) - binary search
💾 SPACE COMPLEXITY: O(1) - only using pointers

🔍 WHY THIS WORKS:
- In a rotated sorted array, one half is always properly sorted
- The minimum element is always in the unsorted half
- We can identify the unsorted half by comparing mid with boundaries
- This eliminates the need to check every element
"""

def find_min_rotated(nums):
    """
    Find minimum element in rotated sorted array.
    
    Args:
        nums: List[int] - rotated sorted array with unique elements
    
    Returns:
        int - minimum element
    """
    # STEP 1: Initialize search boundaries
    left = 0
    right = len(nums) - 1
    
    # STEP 2: Binary search for minimum
    while left < right:
        # STEP 3: Calculate middle point
        mid = (left + right) // 2
        
        # TODO: STEP 4 - YOUR TASK: Compare mid with right to determine which half to search
        # HINT: This is the key insight for rotated arrays!
        # - If nums[mid] > nums[right]: minimum is in RIGHT half (move left boundary)
        # - If nums[mid] <= nums[right]: minimum is in LEFT half (move right boundary)
        #
        # YOUR CODE HERE:
        # if nums[mid] > nums[???]:
        #     # Mid is greater than right, so minimum is in right half
        #     left = ???
        # else:
        #     # Mid is less than or equal to right, so minimum is in left half
        #     right = ???
        
        pass  # Remove this line when you implement the comparison logic above
    
    # STEP 5: When left == right, we found the minimum
    return nums[left]

def find_min_rotated_verbose(nums):
    """
    Same algorithm with detailed step-by-step output for learning.
    """
    print(f"Finding minimum in rotated array: {nums}")
    print("=" * 60)
    
    left = 0
    right = len(nums) - 1
    step = 1
    
    while left < right:
        mid = (left + right) // 2
        
        print(f"Step {step}:")
        print(f"  Search range: [{left}, {right}]")
        print(f"  Elements: {nums[left:right+1]}")
        print(f"  Mid index: {mid}, Mid value: {nums[mid]}")
        print(f"  Right value: {nums[right]}")
        
        if nums[mid] > nums[right]:
            print(f"  {nums[mid]} > {nums[right]}, minimum is in right half")
            left = mid + 1
            print(f"  New search range: [{left}, {right}]")
        else:
            print(f"  {nums[mid]} <= {nums[right]}, minimum is in left half (including mid)")
            right = mid
            print(f"  New search range: [{left}, {right}]")
        
        print()
        step += 1
    
    print(f"🎯 Found minimum: {nums[left]} at index {left}")
    return nums[left]

def demonstrate_rotation_concept():
    """
    Demonstrate how rotation affects sorted arrays.
    """
    print("🔍 UNDERSTANDING ROTATED SORTED ARRAYS")
    print("=" * 50)
    
    original = [1, 2, 3, 4, 5, 6, 7]
    print(f"Original sorted array: {original}")
    print()
    
    # Show different rotations
    rotations = [
        ([1, 2, 3, 4, 5, 6, 7], "No rotation"),
        ([4, 5, 6, 7, 1, 2, 3], "Rotated at index 3"),
        ([6, 7, 1, 2, 3, 4, 5], "Rotated at index 5"),
        ([7, 1, 2, 3, 4, 5, 6], "Rotated at index 6")
    ]
    
    for arr, description in rotations:
        print(f"{description}: {arr}")
        print(f"  Minimum: {min(arr)} at index {arr.index(min(arr))}")
        
        # Show which parts are sorted
        min_idx = arr.index(min(arr))
        if min_idx == 0:
            print(f"  Entire array is sorted")
        else:
            left_part = arr[:min_idx]
            right_part = arr[min_idx:]
            print(f"  Left part {left_part}: sorted = {left_part == sorted(left_part)}")
            print(f"  Right part {right_part}: sorted = {right_part == sorted(right_part)}")
        print()

def binary_search_answer_space_example():
    """
    Demonstrate the concept of binary search on answer space.
    """
    print("🎯 BINARY SEARCH ON ANSWER SPACE CONCEPT")
    print("=" * 50)
    print("Instead of searching for a VALUE, we search for a CONDITION")
    print("Question: 'Where is the minimum element?'")
    print("Answer space: All possible positions in the array")
    print()
    
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(f"Array: {nums}")
    print("Positions: 0  1  2  3  4  5  6")
    print()
    
    print("Binary search process:")
    print("1. Check middle position")
    print("2. Determine which half contains the answer")
    print("3. Eliminate the other half")
    print("4. Repeat until answer found")
    print()
    
    find_min_rotated_verbose(nums)

# 🧪 TEST CASES
if __name__ == "__main__":
    # First demonstrate concepts
    demonstrate_rotation_concept()
    print("=" * 60)
    binary_search_answer_space_example()
    print("=" * 60)
    
    # Test Case 1: Basic rotation
    nums1 = [3, 4, 5, 1, 2]
    result1 = find_min_rotated(nums1)
    print(f"Test 1: {nums1}")
    print(f"Result: {result1}")  # Expected: 1
    print()
    
    # Test Case 2: Different rotation
    nums2 = [4, 5, 6, 7, 0, 1, 2]
    result2 = find_min_rotated(nums2)
    print(f"Test 2: {nums2}")
    print(f"Result: {result2}")  # Expected: 0
    print()
    
    # Test Case 3: No rotation (already sorted)
    nums3 = [11, 13, 15, 17]
    result3 = find_min_rotated(nums3)
    print(f"Test 3: {nums3}")
    print(f"Result: {result3}")  # Expected: 11
    print()
    
    # Test Case 4: Single element
    nums4 = [1]
    result4 = find_min_rotated(nums4)
    print(f"Test 4: {nums4}")
    print(f"Result: {result4}")  # Expected: 1
    print()
    
    # Test Case 5: Two elements
    nums5 = [2, 1]
    result5 = find_min_rotated(nums5)
    print(f"Test 5: {nums5}")
    print(f"Result: {result5}")  # Expected: 1

"""
🎓 LEARNING OBJECTIVES:
After solving this problem, you should understand:
1. How binary search can be applied to answer spaces, not just sorted arrays
2. The concept of eliminating half the possibilities based on conditions
3. How to identify which half of a rotated array contains the answer
4. The difference between searching for values vs. searching for properties

🔄 VARIATIONS TO TRY:
1. Find Minimum in Rotated Sorted Array II (with duplicates)
2. Search in Rotated Sorted Array
3. Find Peak Element
4. Sqrt(x) using binary search

📝 PRACTICE TIPS:
1. Think about what condition helps eliminate half the search space
2. Be careful with boundary conditions (left vs. right comparisons)
3. Consider edge cases: no rotation, single element, two elements
4. Draw diagrams to visualize the rotation and search process

🧠 MENTAL MODEL - Answer Space Search:
Traditional binary search: "Is the target at this position?"
Answer space search: "Does this position satisfy our condition?"

For rotated array minimum:
- Condition: "Is the minimum in the left half or right half?"
- Decision rule: Compare nums[mid] with nums[right]
- If nums[mid] > nums[right]: minimum is in right half
- If nums[mid] <= nums[right]: minimum is in left half

🔑 KEY INSIGHTS:
1. Binary search works on any space where you can eliminate half the possibilities
2. The key is finding a condition that reliably points to the correct half
3. Rotated arrays have the property that one half is always sorted
4. We use the sorted half to determine where the "break point" (minimum) is

💡 WHEN TO USE BINARY SEARCH ON ANSWER SPACE:
- Finding minimum/maximum values that satisfy conditions
- Optimization problems with monotonic properties
- "Find the first/last position where condition X is true"
- Problems where you can check a condition in O(log n) or better

🚨 COMMON PITFALLS:
1. Comparing with wrong boundary (left vs. right)
2. Off-by-one errors in boundary updates
3. Not handling edge cases (no rotation, single element)
4. Confusing the search condition logic
"""
