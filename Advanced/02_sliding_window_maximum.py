"""
🔴 ADVANCED LEVEL - Sliding Window Maximum

PROBLEM: Sliding Window Maximum
Given an array and a sliding window of size k, find the maximum element in each window.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Window positions:
[1  3  -1] -3  5  3  6  7  → max = 3
 1 [3  -1  -3] 5  3  6  7  → max = 3  
 1  3 [-1  -3  5] 3  6  7  → max = 5
 1  3  -1 [-3  5  3] 6  7  → max = 5
 1  3  -1  -3 [5  3  6] 7  → max = 6
 1  3  -1  -3  5 [3  6  7] → max = 7

⏰ Time: O(n)  💾 Space: O(k)
"""

def max_sliding_window(nums, k):
    """
    Find maximum in each sliding window of size k.
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1,3,-1,-3,5,3,6,7], 3),
        ([1], 1),
        ([1,-1], 1),
        ([9,11], 2),
        ([4,-2], 2)
    ]
    
    for nums, k in test_cases:
        result = max_sliding_window(nums, k)
        print(f"nums={nums}, k={k} → {result}")
