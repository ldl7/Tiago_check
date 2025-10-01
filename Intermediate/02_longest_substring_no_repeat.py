"""
🟡 INTERMEDIATE LEVEL - Longest Substring Without Repeating Characters

PROBLEM: Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3 (substring "abc")

Input: s = "bbbbb"
Output: 1 (substring "b")

🎯 Pattern: Sliding Window + Hash Set
Hint: Use a variable-size sliding window. Expand when no duplicates,
contract when duplicates are found.

⏰ Time: O(n)  💾 Space: O(min(m,n)) where m is charset size
"""

def length_of_longest_substring(s):
    """
    Find length of longest substring without repeating characters.
    
    Args:
        s: str - input string
    
    Returns:
        int - length of longest substring
    """
    # Your implementation here
    # Hints:
    # 1. Use two pointers (left, right) for the sliding window
    # 2. Use a set to track characters in current window
    # 3. Expand window by moving right pointer
    # 4. Contract window by moving left pointer when duplicate found
    # 5. Track maximum window size seen
    
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        "abcabcbb",
        "bbbbb", 
        "pwwkew",
        "",
        "dvdf"
    ]
    
    for s in test_cases:
        result = length_of_longest_substring(s)
        print(f"Input: '{s}'")
        print(f"Output: {result}")
        print()

"""
💡 Key Insights:
- Sliding window adapts to constraint (no repeating chars)
- Hash set provides O(1) duplicate detection
- Window contracts only when necessary

🔄 Follow-up: What if you need to return the actual substring?
"""
