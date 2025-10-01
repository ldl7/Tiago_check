"""
🟡 INTERMEDIATE LEVEL - Search in Rotated Sorted Array

PROBLEM: Search in Rotated Sorted Array
A sorted array has been rotated at some pivot. Find the target value's index.

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

🎯 Pattern: Modified Binary Search
Hint: At least one half of the array is always sorted. Determine which half
is sorted, then decide which half to search.

⏰ Time: O(log n)  💾 Space: O(1)
"""

def search_rotated(nums, target):
    """
    Search for target in rotated sorted array.
    
    Args:
        nums: List[int] - rotated sorted array
        target: int - target value
    
    Returns:
        int - index of target, or -1 if not found
    """
    # Your implementation here
    # Hints:
    # 1. Use binary search framework (left, right, mid)
    # 2. Check if left half is sorted: nums[left] <= nums[mid]
    # 3. If left half sorted and target in range, search left
    # 4. Otherwise search right half
    # 5. Handle the case when right half is sorted similarly
    
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([4,5,6,7,0,1,2], 0),
        ([4,5,6,7,0,1,2], 3),
        ([1], 0),
        ([1], 1),
        ([1,3], 3)
    ]
    
    for nums, target in test_cases:
        result = search_rotated(nums, target)
        print(f"Input: nums={nums}, target={target}")
        print(f"Output: {result}")
        print()

"""
💡 Key Insights:
- One half is always properly sorted in rotated array
- Use sorted half to determine search direction
- Handle edge cases: single element, target at rotation point

🔄 Follow-up: What if the array contains duplicates?
"""
