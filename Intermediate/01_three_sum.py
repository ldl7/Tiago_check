"""
🟡 INTERMEDIATE LEVEL - Three Sum

PROBLEM: Three Sum
Given an array of integers, find all unique triplets that sum to zero.

Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

🎯 Pattern: Two Pointer + Sorting
Hint: This builds on the two-sum problem. Sort first, then for each element,
use two pointers to find pairs that complete the triplet.

⏰ Time: O(n²)  💾 Space: O(1) excluding output
"""

def three_sum(nums):
    """
    Find all unique triplets that sum to zero.
    
    Args:
        nums: List[int] - array of integers
    
    Returns:
        List[List[int]] - list of unique triplets
    """
    # Your implementation here
    # Hints:
    # 1. Sort the array first
    # 2. For each element nums[i], find two elements that sum to -nums[i]
    # 3. Use two pointers for the inner search
    # 4. Skip duplicates to avoid duplicate triplets
    
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [0, 0, 0],
        []
    ]
    
    for nums in test_cases:
        result = three_sum(nums)
        print(f"Input: {nums}")
        print(f"Output: {result}")
        print()

"""
💡 Key Insights:
- Sorting enables two-pointer technique
- Skip duplicates at all three positions
- Fix one element, find two-sum for the rest

🔄 Follow-up: Can you solve Three Sum Closest?
"""
