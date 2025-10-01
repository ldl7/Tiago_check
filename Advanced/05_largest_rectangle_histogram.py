"""
🔴 ADVANCED LEVEL - Largest Rectangle in Histogram

PROBLEM: Largest Rectangle in Histogram
Given an array of integers representing histogram bar heights, find the area of 
the largest rectangle that can be formed.

Example:
Input: heights = [2,1,5,6,2,3]
Output: 10

Visual representation:
    █
    █ █
█   █ █   █
█ █ █ █ █ █
2 1 5 6 2 3

Largest rectangle has area 10 (height=5, width=2, covering indices 2-3)

⏰ Time: O(n)  💾 Space: O(n)
"""

def largest_rectangle_area(heights):
    """
    Find area of largest rectangle in histogram.
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [2,1,5,6,2,3],
        [2,4],
        [1,1,1,1],
        [5,4,3,2,1],
        [1,2,3,4,5],
        []
    ]
    
    for heights in test_cases:
        result = largest_rectangle_area(heights)
        print(f"heights={heights} → {result}")
