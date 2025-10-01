"""
🔴 ADVANCED LEVEL - Minimum Window Substring

PROBLEM: Minimum Window Substring
Given strings s and t, find the minimum window substring of s that contains all 
characters of t (including duplicates).

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Input: s = "a", t = "a"
Output: "a"

Input: s = "a", t = "aa"
Output: ""

⏰ Time: O(|s| + |t|)  💾 Space: O(|s| + |t|)
"""

def min_window(s, t):
    """
    Find minimum window substring containing all characters of t.
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa"),
        ("ab", "b"),
        ("abc", "cba")
    ]
    
    for s, t in test_cases:
        result = min_window(s, t)
        print(f's="{s}", t="{t}" → "{result}"')
