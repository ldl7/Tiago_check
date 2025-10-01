"""
🟢 BEGINNER LEVEL - Hash Maps/Sets Basics

PROBLEM: Two Sum (Unsorted Array)
Given an array of integers and a target sum, find two numbers that add up to the target.
Return their indices.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)

🎯 ALGORITHMIC PATTERN: Hash Map for Quick Lookups
This is a hash map problem because:
1. We need to find a PAIR that satisfies a condition
2. For each element, we need to check if its "complement" exists
3. Hash maps provide O(1) lookup time for existence checks
4. We can store elements we've seen along with their indices

💡 APPROACH HINTS:
1. For each element nums[i], calculate complement = target - nums[i]
2. Check if complement exists in our hash map
3. If yes: we found our pair! Return indices
4. If no: add current element and its index to hash map
5. Continue until pair is found

⏰ TIME COMPLEXITY: O(n) - single pass through array
💾 SPACE COMPLEXITY: O(n) - hash map can store up to n elements

🔍 WHY HASH MAPS WORK HERE:
- Brute force: Check every pair O(n²)
- Hash map: For each element, check if complement exists O(1)
- Trade space for time: use extra memory to achieve faster lookup
"""

def two_sum_hash_map(nums, target):
    """
    Find two numbers that add up to target using hash map.
    
    Args:
        nums: List[int] - array of integers
        target: int - target sum
    
    Returns:
        List[int] - indices of the two numbers
    """
    # STEP 1: Create hash map to store {value: index}
    seen = {}  # Dictionary to store numbers we've seen and their indices
    
    # STEP 2: Iterate through array
    for i, num in enumerate(nums):
        # STEP 3: Calculate what number we need to reach target
        complement = target - num
        
        # TODO: STEP 4 - YOUR TASK: Check if complement exists in hash map
        # HINT: Use the 'in' operator to check if complement is a key in seen dictionary
        # If found, return the indices: [seen[complement], i]
        #
        # YOUR CODE HERE:
        # if ??? in seen:
        #     # Found the pair! Return indices
        #     return [seen[???], i]
        
        # TODO: STEP 5 - YOUR TASK: Add current number and its index to hash map
        # HINT: Store the mapping num -> i in the seen dictionary
        # YOUR CODE HERE:
        # seen[???] = ???
        
        pass  # Remove this line when you implement the hash map logic above
    
    # No solution found (shouldn't happen with valid input)
    return []

def two_sum_hash_map_verbose(nums, target):
    """
    Same algorithm with detailed step-by-step output for learning.
    """
    print(f"Array: {nums}, Target: {target}")
    print("=" * 50)
    
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        print(f"Step {i + 1}: nums[{i}] = {num}")
        print(f"  Need complement: {target} - {num} = {complement}")
        print(f"  Hash map so far: {seen}")
        
        if complement in seen:
            print(f"  ✅ Found complement {complement} at index {seen[complement]}!")
            print(f"  Solution: [{seen[complement]}, {i}]")
            return [seen[complement], i]
        
        seen[num] = i
        print(f"  Added {num} -> {i} to hash map")
        print()
    
    print("❌ No solution found")
    return []

def frequency_counter(nums):
    """
    Count frequency of each element using hash map.
    This is another common hash map pattern.
    """
    print(f"Counting frequencies in: {nums}")
    
    # Method 1: Manual counting
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    print(f"Frequencies (manual): {freq}")
    
    # Method 2: Using get() method
    freq2 = {}
    for num in nums:
        freq2[num] = freq2.get(num, 0) + 1
    
    print(f"Frequencies (using get): {freq2}")
    
    # Method 3: Using defaultdict
    from collections import defaultdict
    freq3 = defaultdict(int)
    for num in nums:
        freq3[num] += 1
    
    print(f"Frequencies (defaultdict): {dict(freq3)}")
    
    return freq

def find_duplicates(nums):
    """
    Find all duplicate elements using hash set.
    """
    seen = set()
    duplicates = set()
    
    print(f"Finding duplicates in: {nums}")
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
            print(f"  Found duplicate: {num}")
        else:
            seen.add(num)
            print(f"  First time seeing: {num}")
    
    print(f"All duplicates: {list(duplicates)}")
    return list(duplicates)

# 🧪 TEST CASES
if __name__ == "__main__":
    # Test Case 1: Basic two sum
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum_hash_map(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Result: {result1}")  # Expected: [0, 1]
    print()
    
    # Detailed walkthrough
    print("DETAILED WALKTHROUGH:")
    two_sum_hash_map_verbose(nums1, target1)
    print("=" * 50)
    
    # Test Case 2: Different positions
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test 2: nums={nums2}, target={target2}")
    result2 = two_sum_hash_map_verbose(nums2, target2)
    print(f"Result: {result2}")  # Expected: [1, 2]
    print("=" * 50)
    
    # Test Case 3: Same number twice
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum_hash_map(nums3, target3)
    print(f"Test 3: nums={nums3}, target={target3}")
    print(f"Result: {result3}")  # Expected: [0, 1]
    print()
    
    # Test Case 4: Frequency counting
    print("FREQUENCY COUNTING EXAMPLE:")
    nums4 = [1, 2, 2, 3, 3, 3, 4]
    frequency_counter(nums4)
    print()
    
    # Test Case 5: Finding duplicates
    print("FINDING DUPLICATES EXAMPLE:")
    nums5 = [1, 2, 3, 2, 4, 3, 5]
    find_duplicates(nums5)

"""
🎓 LEARNING OBJECTIVES:
After solving this problem, you should understand:
1. How hash maps provide O(1) average lookup time
2. The trade-off between time and space complexity
3. Common hash map patterns: lookup, frequency counting, duplicate detection
4. When to use hash maps vs. other data structures

🔄 VARIATIONS TO TRY:
1. Three Sum: Find three numbers that add to target
2. Group Anagrams: Group strings that are anagrams of each other
3. Longest Substring Without Repeating Characters
4. Valid Anagram: Check if two strings are anagrams

📝 PRACTICE TIPS:
1. Think about what you need to "remember" as you iterate
2. Consider using hash maps when you need fast lookups
3. Be careful with hash map keys (immutable types only)
4. Handle edge cases: empty arrays, no solution, duplicate values

🧠 MENTAL MODEL - Hash Map as Memory:
As we iterate through [2, 7, 11, 15] looking for target 9:

Step 1: num=2, need 7, seen={} → not found, add 2->0
Step 2: num=7, need 2, seen={2:0} → found! return [0,1]

The hash map "remembers" what we've seen and where we saw it.

🔑 KEY INSIGHTS:
1. Hash maps excel at "have I seen this before?" questions
2. They're perfect for complement/pair-finding problems
3. The key insight: instead of checking all previous elements (O(n)), 
   check hash map (O(1))
4. Common pattern: check first, then add to avoid using same element twice

💡 WHEN TO USE HASH MAPS:
- Need fast lookups (O(1) average case)
- Counting frequencies of elements
- Checking for existence/duplicates
- Storing key-value relationships
- Complement/pair finding problems

🚨 HASH MAP GOTCHAS:
1. Keys must be immutable (strings, numbers, tuples - not lists)
2. Hash collisions can degrade performance to O(n) in worst case
3. No guaranteed order (use OrderedDict if order matters)
4. Memory overhead compared to arrays
"""
