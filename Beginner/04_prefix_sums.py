"""
🟢 BEGINNER LEVEL - Prefix Sums

PROBLEM: Range Sum Query
Given an array of integers, answer multiple queries asking for the sum of elements 
between indices i and j (inclusive).

Example:
Input: nums = [1, 3, 5, 7, 9, 11]
Query: sum from index 1 to 4 → sum of [3, 5, 7, 9] = 24
Query: sum from index 2 to 5 → sum of [5, 7, 9, 11] = 32

🎯 ALGORITHMIC PATTERN: Prefix Sums
This is a prefix sum problem because:
1. We need to calculate sums of SUBARRAYS multiple times
2. Naive approach would recalculate the same sums repeatedly
3. We can precompute cumulative sums to answer queries in O(1) time

💡 APPROACH HINTS:
1. Build a prefix sum array where prefix[i] = sum of nums[0] to nums[i-1]
2. To get sum from index i to j: prefix[j+1] - prefix[i]
3. Handle edge cases carefully (0-indexed vs 1-indexed)

⏰ TIME COMPLEXITY: 
   - Preprocessing: O(n) to build prefix array
   - Each query: O(1)
   - Total for q queries: O(n + q)
💾 SPACE COMPLEXITY: O(n) for prefix sum array

🔍 WHY PREFIX SUMS WORK:
- prefix[i] = nums[0] + nums[1] + ... + nums[i-1]
- sum(i, j) = nums[i] + nums[i+1] + ... + nums[j]
- sum(i, j) = prefix[j+1] - prefix[i]
- This eliminates the need to sum elements repeatedly
"""

class RangeSumQuery:
    """
    Class to handle range sum queries efficiently using prefix sums.
    """
    
    def __init__(self, nums):
        """
        Initialize with the array and build prefix sum array.
        
            nums: List[int] - input array
        """
        self.nums = nums
        self.n = len(nums)
        
        # TODO: STEP 2 - YOUR TASK: Build prefix sum array
        # prefix[i] represents sum of nums[0] to nums[i-1]
        self.prefix = [0]  # prefix[0] = 0 (sum of empty subarray)
        
        # TODO: Build the prefix array
        # HINT: Each prefix[i+1] should equal prefix[i] + nums[i]
        # This creates a cumulative sum array
        #
        # YOUR CODE HERE:
        # for i in range(len(nums)):
        #     # Each prefix[i+1] = prefix[i] + nums[i]
        #     self.prefix.append(???)
        
        pass  # Remove this line when you implement the prefix sum building above
        
        print(f"Original array: {nums}")
        print(f"Prefix sum array: {self.prefix}")
        print("Prefix[i] represents sum of nums[0] to nums[i-1]")
        print()
    
    def range_sum(self, i, j):
        """
        Calculate sum of elements from index i to j (inclusive).
        
        Args:
            i: int - start index (inclusive)
            j: int - end index (inclusive)
        
        Returns:
            int - sum of elements from index i to j
        
        Time Complexity: O(1) - constant time lookup!
        """
        # TODO: YOUR TASK - Calculate range sum using prefix sums
        # CORE INSIGHT: sum[i:j+1] = prefix[j+1] - prefix[i]
        # This works because:
        # prefix[j+1] = sum of nums[0] to nums[j]
        # prefix[i] = sum of nums[0] to nums[i-1]
        # Difference = sum of nums[i] to nums[j]
        #
        # YOUR CODE HERE:
        # result = self.prefix[???] - self.prefix[???]
        
        pass  # Remove this line when you implement the prefix sum formula above
        
        print(f"Query: sum from index {i} to {j}")
        print(f"  Elements: {self.nums[i:j+1]}")
        print(f"  Prefix formula: prefix[{j+1}] - prefix[{i}] = {self.prefix[j+1]} - {self.prefix[i]} = {result}")
        
        return result

def demonstrate_prefix_sum_concept():
    """
    Demonstrate how prefix sums work step by step.
    """
    nums = [1, 3, 5, 7, 9, 11]
    print("🔍 UNDERSTANDING PREFIX SUMS")
    print("=" * 50)
    print(f"Array: {nums}")
    print()
    
    # Build prefix sum manually to show the process
    print("Building prefix sum array:")
    prefix = [0]  # Start with 0
    
    for i, num in enumerate(nums):
        new_prefix = prefix[-1] + num
        prefix.append(new_prefix)
        print(f"  prefix[{i+1}] = prefix[{i}] + nums[{i}] = {prefix[i]} + {num} = {new_prefix}")
    
    print(f"\nFinal prefix array: {prefix}")
    print()
    
    # Show how to use prefix sums for range queries
    print("Using prefix sums for range queries:")
    print()
    
    # Query 1: sum from index 1 to 4
    i, j = 1, 4
    result = prefix[j + 1] - prefix[i]
    print(f"Query: sum from index {i} to {j}")
    print(f"  Elements: {nums[i:j+1]}")
    print(f"  Manual sum: {' + '.join(map(str, nums[i:j+1]))} = {sum(nums[i:j+1])}")
    print(f"  Prefix formula: prefix[{j+1}] - prefix[{i}] = {prefix[j+1]} - {prefix[i]} = {result}")
    print(f"  ✓ Both methods give same result: {result}")
    print()
    
    # Query 2: sum from index 2 to 5
    i, j = 2, 5
    result = prefix[j + 1] - prefix[i]
    print(f"Query: sum from index {i} to {j}")
    print(f"  Elements: {nums[i:j+1]}")
    print(f"  Manual sum: {' + '.join(map(str, nums[i:j+1]))} = {sum(nums[i:j+1])}")
    print(f"  Prefix formula: prefix[{j+1}] - prefix[{i}] = {prefix[j+1]} - {prefix[i]} = {result}")
    print(f"  ✓ Both methods give same result: {result}")

# 🧪 TEST CASES
if __name__ == "__main__":
    # First, demonstrate the concept
    demonstrate_prefix_sum_concept()
    print("\n" + "=" * 60 + "\n")
    
    # Test the class implementation
    print("🧪 TESTING RANGE SUM QUERY CLASS")
    print("=" * 50)
    
    # Test Case 1: Basic example
    nums1 = [1, 3, 5, 7, 9, 11]
    rsq = RangeSumQuery(nums1)
    
    # Multiple queries
    queries = [(1, 4), (2, 5), (0, 2), (3, 5), (0, 5)]
    
    for i, j in queries:
        result = rsq.range_sum(i, j)
        print()
    
    print("=" * 50)
    
    # Test Case 2: Array with negative numbers
    print("Test with negative numbers:")
    nums2 = [-2, 1, -3, 4, -1, 2]
    rsq2 = RangeSumQuery(nums2)
    
    result = rsq2.range_sum(1, 4)  # sum of [1, -3, 4, -1] = 1
    print()

"""
🎓 LEARNING OBJECTIVES:
After solving this problem, you should understand:
1. How prefix sums eliminate redundant calculations
2. The relationship between prefix sums and range queries
3. Why we use prefix[j+1] - prefix[i] for range [i, j]
4. How to handle 0-indexed arrays with prefix sums

🔄 VARIATIONS TO TRY:
1. 2D Range Sum Query (2D prefix sums)
2. Subarray Sum Equals K (prefix sums + hash map)
3. Maximum Subarray Sum (Kadane's algorithm)
4. Range Update Queries (difference arrays)

📝 PRACTICE TIPS:
1. Always include prefix[0] = 0 for easier calculations
2. Be careful with index boundaries (off-by-one errors)
3. Draw diagrams to visualize the prefix sum concept
4. Test with negative numbers and edge cases

🧠 MENTAL MODEL - Visual Representation:
Array:  [1,  3,  5,  7,  9, 11]
Index:   0   1   2   3   4   5

Prefix: [0,  1,  4,  9, 16, 25, 36]
Index:   0   1   2   3   4   5   6

To get sum from index 2 to 4 (elements 5, 7, 9):
sum(2,4) = prefix[5] - prefix[2] = 25 - 4 = 21
         = 5 + 7 + 9 = 21 ✓

🔑 KEY INSIGHT:
Prefix sums transform the problem from "calculate sum of range" to 
"subtract two precomputed values". This is especially powerful when 
you have many queries on the same array.

💡 WHEN TO USE PREFIX SUMS:
- Multiple range sum queries on the same array
- Subarray problems involving sums
- When you need O(1) query time after O(n) preprocessing
- Problems asking about cumulative values
"""
