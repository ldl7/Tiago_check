"""
🟡 INTERMEDIATE LEVEL - Subarray Sum Equals K

PROBLEM: Subarray Sum Equals K
Given an array of integers and an integer k, find the total number of continuous 
subarrays whose sum equals k.

Example:
Input: nums = [1, 1, 1], k = 2
Output: 2 (subarrays [1,1] appear twice)

Input: nums = [1, 2, 3], k = 3
Output: 2 (subarrays [1,2] and [3])

🎯 Pattern: Prefix Sum + Hash Map
Hint: If prefix_sum[j] - prefix_sum[i] = k, then subarray from i+1 to j has sum k.
Rearranging: prefix_sum[i] = prefix_sum[j] - k

⏰ Time: O(n)  💾 Space: O(n)
"""

def subarray_sum(nums, k):
    """
    Count number of continuous subarrays with sum equal to k.
    
    Args:
        nums: List[int] - array of integers
        k: int - target sum
    
    Returns:
        int - number of subarrays with sum k
    """
    # Your implementation here
    # Hints:
    # 1. Use running prefix sum as you iterate
    # 2. For each position, check if (prefix_sum - k) exists in hash map
    # 3. Hash map stores {prefix_sum: count_of_occurrences}
    # 4. Don't forget to handle prefix_sum = k case (subarray from start)
    
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1], 2),
        ([1, 2, 3], 3),
        ([1, -1, 0], 0),
        ([1, 2, 1, 2, 1], 3)
    ]
    
    for nums, k in test_cases:
        result = subarray_sum(nums, k)
        print(f"Input: nums={nums}, k={k}")
        print(f"Output: {result}")
        print()

"""
💡 Key Insights:
- Prefix sums transform subarray sum to difference of prefix sums
- Hash map counts occurrences of each prefix sum
- Handle the case where subarray starts from index 0

🔄 Follow-up: Can you solve this with O(1) space? (Hint: Only for positive numbers)
"""
