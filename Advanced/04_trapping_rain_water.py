"""
🔴 ADVANCED LEVEL - Trapping Rain Water

PROBLEM: Trapping Rain Water
Given an elevation map represented by an array of heights, compute how much water 
can be trapped after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Visual representation:
   █
   █ █ █
 █ █ █ █ █ █
█ █ █ █ █ █ █ █
0 1 0 2 1 0 1 3 2 1 2 1

Water trapped (marked with ~):
   █
   █~█~█
 █~█~█~█~█~█
█~█~█~█~█~█~█~█

⏰ Time: O(n)  💾 Space: O(1)
"""

def trap(height):
    """
    Calculate amount of rainwater that can be trapped.
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [4,2,0,3,2,5],
        [3,0,2,0,4],
        [],
        [1],
        [1,2,3,4,5]
    ]
    
    for height in test_cases:
        result = trap(height)
        print(f"height={height} → {result}")
