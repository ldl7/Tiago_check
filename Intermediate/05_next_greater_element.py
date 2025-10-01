"""
🟡 INTERMEDIATE LEVEL - Next Greater Element

PROBLEM: Next Greater Element I
Given two arrays nums1 and nums2 where nums1 is a subset of nums2, find the next 
greater element for each element in nums1 in nums2.

Example:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: 
- 4: no greater element → -1
- 1: next greater is 3
- 2: no greater element → -1

🎯 Pattern: Monotonic Stack + Hash Map
Hint: Use a stack to find next greater elements in nums2, then use hash map
to look up results for nums1.

⏰ Time: O(n + m)  💾 Space: O(n)
"""

def next_greater_element(nums1, nums2):
    """
    Find next greater element for each element in nums1.
    
    Args:
        nums1: List[int] - query array (subset of nums2)
        nums2: List[int] - reference array
    
    Returns:
        List[int] - next greater elements for nums1
    """
    # Your implementation here
    # Hints:
    # 1. Use monotonic decreasing stack to process nums2
    # 2. When current element > stack top, stack top's next greater is current
    # 3. Store results in hash map {element: next_greater}
    # 4. Look up each element in nums1 from the hash map
    
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([4,1,2], [1,3,4,2]),
        ([2,4], [1,2,3,4]),
        ([1,3,5,2,4], [6,5,4,3,2,1,7])
    ]
    
    for nums1, nums2 in test_cases:
        result = next_greater_element(nums1, nums2)
        print(f"Input: nums1={nums1}, nums2={nums2}")
        print(f"Output: {result}")
        print()

"""
💡 Key Insights:
- Monotonic stack maintains decreasing order
- When we find a greater element, it resolves multiple stack elements
- Hash map provides O(1) lookup for final results

🔄 Follow-up: What about Next Greater Element II (circular array)?
"""
