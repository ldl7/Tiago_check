"""
🟢 BEGINNER LEVEL - Heap Basics (Priority Queue)

PROBLEM: Kth Largest Element in Array
Find the kth largest element in an unsorted array. Note that it is the kth largest 
element in sorted order, not the kth distinct element.

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5 (the 2nd largest element)

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4  
Output: 4 (sorted: [6,5,5,4,3,3,2,2,1], 4th largest is 4)

🎯 ALGORITHMIC PATTERN: Min Heap (Priority Queue)
This is a heap problem because:
1. We need to efficiently find the Kth largest element
2. We can maintain a min heap of size k
3. The root of the min heap will be the kth largest element
4. Heaps provide O(log k) insertion and O(1) access to min/max

💡 APPROACH HINTS:
1. Use a min heap to keep track of the k largest elements seen so far
2. If heap size < k, add element to heap
3. If heap size = k and current element > heap root, replace root
4. The root of the min heap is the kth largest element

⏰ TIME COMPLEXITY: O(n log k) - n elements, each operation takes O(log k)
💾 SPACE COMPLEXITY: O(k) - heap stores at most k elements

🔍 WHY MIN HEAP WORKS:
- Min heap of size k stores the k largest elements
- The smallest of these k elements (heap root) is the kth largest overall
- When we see a larger element, we remove the smallest and add the new one
- This maintains the "k largest" property efficiently
"""

import heapq

def find_kth_largest(nums, k):
    """
    Find the kth largest element using a min heap.
    
    Args:
        nums: List[int] - array of integers
        k: int - find kth largest (1-indexed)
    
    Returns:
        int - kth largest element
    """
    # STEP 1: Create min heap to store k largest elements
    min_heap = []
    
    # STEP 2: Process each element
    for num in nums:
        # TODO: STEP 3 - YOUR TASK: Add element to heap
        # HINT: Use heapq.heappush(heap, element) to add element to min heap
        # YOUR CODE HERE:
        # heapq.heappush(???, ???)
        
        # TODO: STEP 4 - YOUR TASK: Maintain heap size of k
        # HINT: If heap size > k, remove the smallest element using heapq.heappop()
        # This keeps only the k largest elements seen so far
        # YOUR CODE HERE:
        # if len(min_heap) > ???:
        #     heapq.???(???)
        
        pass  # Remove this line when you implement the heap operations above
    
    # TODO: STEP 5 - YOUR TASK: Return kth largest element
    # HINT: The root of the min heap (index 0) is the kth largest element
    # YOUR CODE HERE:
    # return min_heap[???]
    
    pass  # Remove this line when you implement the return statement above

def find_kth_largest_verbose(nums, k):
    """
    Same algorithm with detailed step-by-step output for learning.
    """
    print(f"Finding {k}th largest in: {nums}")
    print("=" * 50)
    
    min_heap = []
    
    for i, num in enumerate(nums):
        print(f"Step {i + 1}: Processing {num}")
        print(f"  Heap before: {min_heap}")
        
        # Add element to heap
        heapq.heappush(min_heap, num)
        print(f"  After adding {num}: {min_heap}")
        
        # Remove excess elements
        if len(min_heap) > k:
            removed = heapq.heappop(min_heap)
            print(f"  Heap size > {k}, removed {removed}: {min_heap}")
        
        print(f"  Current {k} largest elements: {sorted(min_heap, reverse=True)}")
        if len(min_heap) == k:
            print(f"  Current {k}th largest: {min_heap[0]}")
        print()
    
    result = min_heap[0]
    print(f"Final answer: {k}th largest = {result}")
    return result

def demonstrate_heap_operations():
    """
    Demonstrate basic heap operations in Python.
    """
    print("🔍 UNDERSTANDING PYTHON HEAPS (heapq)")
    print("=" * 50)
    print("Python's heapq implements a MIN HEAP")
    print()
    
    # Basic heap operations
    heap = []
    elements = [3, 1, 4, 1, 5, 9, 2, 6]
    
    print("Building heap by adding elements:")
    for elem in elements:
        heapq.heappush(heap, elem)
        print(f"  Added {elem}: {heap} (min = {heap[0]})")
    
    print(f"\nFinal heap: {heap}")
    print("Note: heap[0] is always the minimum element")
    print()
    
    print("Removing elements (always gets minimum):")
    while heap:
        min_elem = heapq.heappop(heap)
        print(f"  Removed {min_elem}: {heap}")
    
    print()
    print("🔄 FOR MAX HEAP: Negate values or use custom comparison")
    
    # Max heap simulation
    max_heap = []
    for elem in [3, 1, 4, 1, 5]:
        heapq.heappush(max_heap, -elem)  # Negate for max heap
    
    print(f"Max heap (negated): {max_heap}")
    print(f"Actual max element: {-max_heap[0]}")

def find_k_smallest(nums, k):
    """
    Alternative: Find kth smallest using max heap.
    This demonstrates the opposite approach.
    """
    # Use max heap (negate values) to keep k smallest elements
    max_heap = []
    
    for num in nums:
        heapq.heappush(max_heap, -num)  # Negate for max heap behavior
        
        if len(max_heap) > k:
            heapq.heappop(max_heap)  # Remove largest (most negative when negated)
    
    return -max_heap[0]  # Return actual value (negate back)

# 🧪 TEST CASES
if __name__ == "__main__":
    # First demonstrate heap operations
    demonstrate_heap_operations()
    print("\n" + "=" * 60 + "\n")
    
    # Test Case 1: Basic example
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    result1 = find_kth_largest(nums1, k1)
    print(f"Test 1: nums={nums1}, k={k1}")
    print(f"Result: {result1}")  # Expected: 5
    print()
    
    # Detailed walkthrough
    print("DETAILED WALKTHROUGH:")
    find_kth_largest_verbose(nums1, k1)
    print("=" * 60)
    
    # Test Case 2: With duplicates
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    result2 = find_kth_largest(nums2, k2)
    print(f"Test 2: nums={nums2}, k={k2}")
    print(f"Sorted: {sorted(nums2, reverse=True)}")
    print(f"Result: {result2}")  # Expected: 4
    print()
    
    # Test Case 3: k = 1 (largest element)
    nums3 = [1, 2, 3, 4, 5]
    k3 = 1
    result3 = find_kth_largest(nums3, k3)
    print(f"Test 3: nums={nums3}, k={k3}")
    print(f"Result: {result3}")  # Expected: 5
    print()
    
    # Test Case 4: k = n (smallest element)
    nums4 = [7, 10, 4, 3, 20, 15]
    k4 = len(nums4)
    result4 = find_kth_largest(nums4, k4)
    print(f"Test 4: nums={nums4}, k={k4}")
    print(f"Result: {result4}")  # Expected: 3
    print()
    
    # Bonus: Compare with kth smallest
    k_smallest = find_k_smallest(nums4, k4)
    print(f"Bonus - {k4}th smallest: {k_smallest}")  # Should be same as kth largest when k=n

"""
🎓 LEARNING OBJECTIVES:
After solving this problem, you should understand:
1. How heaps provide efficient access to min/max elements
2. The difference between min heap and max heap
3. How to maintain "top k" elements efficiently
4. When to use heaps vs. sorting for finding kth elements

🔄 VARIATIONS TO TRY:
1. Top K Frequent Elements
2. Merge k Sorted Lists  
3. Find Median from Data Stream
4. Sliding Window Median

📝 PRACTICE TIPS:
1. Remember: Python's heapq is a MIN heap by default
2. For max heap behavior, negate values or use custom comparison
3. Heap operations: heappush(), heappop(), heapify()
4. heap[0] always gives you the min element (don't pop to just peek!)

🧠 MENTAL MODEL - Heap as "Top K Tracker":
Think of the min heap as keeping track of the "VIP list" of k largest elements:

Processing [3,2,1,5,6,4] for k=2:

Add 3: [3] (VIP list: [3])
Add 2: [2,3] (VIP list: [3,2])  
Add 1: [2,3] → remove 1 (VIP list: [3,2])
Add 5: [2,3] → remove 2, add 5: [3,5] (VIP list: [5,3])
Add 6: [3,5] → remove 3, add 6: [5,6] (VIP list: [6,5])
Add 4: [5,6] → 4 < 5, no change (VIP list: [6,5])

The 2nd largest (min of VIP list) = 5

🔑 KEY INSIGHTS:
1. Min heap of size k maintains the k largest elements efficiently
2. The root (minimum) of this heap is exactly the kth largest overall
3. This avoids sorting the entire array O(n log n)
4. Especially efficient when k << n (k much smaller than n)

💡 WHEN TO USE HEAPS:
- Finding kth largest/smallest elements
- Maintaining top k elements in a stream
- Merging sorted sequences
- Priority-based processing
- When you need efficient min/max access

🚨 HEAP GOTCHAS:
1. Python heapq is min heap only (use negation for max heap)
2. heappop() removes and returns, heap[0] just peeks
3. Heap doesn't maintain sorted order (only heap property)
4. Building heap from list: use heapq.heapify() for O(n) construction
"""
