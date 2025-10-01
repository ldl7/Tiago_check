"""
🔴 ADVANCED LEVEL - Median of Two Sorted Arrays

PROBLEM: Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2, find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0

Input: nums1 = [1,2], nums2 = [3,4]  
Output: 2.5

⏰ Time: O(log(min(m,n)))  💾 Space: O(1)
"""

def find_median_sorted_arrays(nums1, nums2):
    """
    Find median of two sorted arrays in O(log(min(m,n))) time.
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1,3], [2]),
        ([1,2], [3,4]),
        ([0,0], [0,0]),
        ([], [1]),
        ([2], [])
    ]
    
    for nums1, nums2 in test_cases:
        result = find_median_sorted_arrays(nums1, nums2)
        print(f"nums1={nums1}, nums2={nums2} → {result}")
