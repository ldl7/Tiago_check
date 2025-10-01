"""
🟢 BEGINNER LEVEL - Monotonic Stack

PROBLEM: Daily Temperatures
Given an array of daily temperatures, return an array where each element represents 
how many days you have to wait until a warmer temperature. If there's no future day 
with a warmer temperature, put 0.

Example:
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]

Explanation:
- Day 0 (73°): Next warmer day is day 1 (74°) → wait 1 day
- Day 1 (74°): Next warmer day is day 2 (75°) → wait 1 day  
- Day 2 (75°): Next warmer day is day 6 (76°) → wait 4 days
- Day 3 (71°): Next warmer day is day 5 (72°) → wait 2 days
- Day 4 (69°): Next warmer day is day 5 (72°) → wait 1 day
- Day 5 (72°): Next warmer day is day 6 (76°) → wait 1 day
- Day 6 (76°): No warmer day → 0
- Day 7 (73°): No warmer day → 0

🎯 ALGORITHMIC PATTERN: Monotonic Stack
This is a monotonic stack problem because:
1. We need to find the NEXT GREATER element for each position
2. We can use a stack to keep track of elements waiting for their "next greater"
3. The stack maintains a DECREASING order (monotonic decreasing)
4. When we find a greater element, it resolves multiple waiting elements

💡 APPROACH HINTS:
1. Use a stack to store indices of temperatures waiting for warmer days
2. For each day, while current temp > temp at stack top, pop and calculate days
3. Push current day's index onto stack
4. Stack maintains decreasing temperature order

⏰ TIME COMPLEXITY: O(n) - each element pushed and popped at most once
💾 SPACE COMPLEXITY: O(n) - stack can hold up to n elements

🔍 WHY MONOTONIC STACK WORKS:
- We process elements left to right
- Stack stores indices of elements that haven't found their "next greater" yet
- When we find a greater element, it can resolve multiple stack elements
- The stack naturally maintains the property we need (decreasing order)
"""

def daily_temperatures(temperatures):
    """
    Find how many days until next warmer temperature for each day.
    
    Args:
        temperatures: List[int] - daily temperatures
    
    Returns:
        List[int] - days to wait for warmer temperature
    """
    n = len(temperatures)
    result = [0] * n  # Initialize result array with zeros
    stack = []        # Stack to store indices of days waiting for warmer weather
    
    # STEP 1: Process each day
    for i in range(n):
        current_temp = temperatures[i]
        
        # TODO: STEP 2 - YOUR TASK: Process stack while conditions are met
        # HINT: While stack is not empty AND current temp > temp at stack top
        # This means current day is warmer than previous days waiting in stack
        #
        # YOUR CODE HERE:
        # while stack and temperatures[stack[-1]] < ???:
        #     # TODO: STEP 3 - Pop the day that found its warmer day
        #     prev_day = stack.???
        #     
        #     # TODO: STEP 4 - Calculate days waited
        #     days_waited = i - ???
        #     result[prev_day] = ???
        
        # TODO: STEP 5 - YOUR TASK: Push current day onto stack
        # HINT: Add current day index to stack (it's waiting for its warmer day)
        # YOUR CODE HERE:
        # stack.???(???)
        
        pass  # Remove this line when you implement the monotonic stack logic above
    
    # STEP 6: Remaining elements in stack have no warmer day (already 0 in result)
    return result

def daily_temperatures_verbose(temperatures):
    """
    Same algorithm with detailed step-by-step output for learning.
    """
    print(f"Temperatures: {temperatures}")
    print("=" * 60)
    
    n = len(temperatures)
    result = [0] * n
    stack = []
    
    for i in range(n):
        current_temp = temperatures[i]
        print(f"Day {i}: Temperature = {current_temp}°")
        print(f"  Stack before: {stack} (indices)")
        
        # Process stack while current temp is warmer
        resolved_days = []
        while stack and temperatures[stack[-1]] < current_temp:
            prev_day = stack.pop()
            days_waited = i - prev_day
            result[prev_day] = days_waited
            resolved_days.append((prev_day, days_waited))
            print(f"    Resolved day {prev_day}: waited {days_waited} days")
        
        if not resolved_days:
            print(f"    No days resolved (current temp not warmer than stack top)")
        
        # Add current day to stack
        stack.append(i)
        print(f"  Stack after: {stack} (indices)")
        print(f"  Result so far: {result}")
        print()
    
    print(f"Final result: {result}")
    return result

def demonstrate_monotonic_stack_concept():
    """
    Demonstrate the monotonic stack concept step by step.
    """
    print("🔍 UNDERSTANDING MONOTONIC STACK")
    print("=" * 50)
    print("Key insight: Stack maintains DECREASING order of temperatures")
    print("When we find a warmer day, it can resolve multiple previous days!")
    print()
    
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print("Let's trace through the algorithm:")
    print()
    
    daily_temperatures_verbose(temperatures)

# 🧪 TEST CASES
if __name__ == "__main__":
    # First demonstrate the concept
    demonstrate_monotonic_stack_concept()
    print("\n" + "=" * 60 + "\n")
    
    # Test Case 1: Basic example
    temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
    result1 = daily_temperatures(temps1)
    print(f"Test 1: {temps1}")
    print(f"Result: {result1}")  # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
    print()
    
    # Test Case 2: Increasing temperatures
    temps2 = [30, 40, 50, 60]
    result2 = daily_temperatures(temps2)
    print(f"Test 2: {temps2}")
    print(f"Result: {result2}")  # Expected: [1, 1, 1, 0]
    print()
    
    # Test Case 3: Decreasing temperatures
    temps3 = [60, 50, 40, 30]
    result3 = daily_temperatures(temps3)
    print(f"Test 3: {temps3}")
    print(f"Result: {result3}")  # Expected: [0, 0, 0, 0]
    print()
    
    # Test Case 4: Single temperature
    temps4 = [89]
    result4 = daily_temperatures(temps4)
    print(f"Test 4: {temps4}")
    print(f"Result: {result4}")  # Expected: [0]

"""
🎓 LEARNING OBJECTIVES:
After solving this problem, you should understand:
1. How monotonic stacks maintain order while processing elements
2. The "next greater element" pattern and its applications
3. How one element can resolve multiple waiting elements
4. Why this approach is more efficient than nested loops

🔄 VARIATIONS TO TRY:
1. Next Greater Element I & II
2. Largest Rectangle in Histogram
3. Remove K Digits
4. Online Stock Span

📝 PRACTICE TIPS:
1. Draw the stack state at each step to visualize the process
2. Remember: monotonic stack processes elements in order
3. Think about what each stack element is "waiting for"
4. Consider what happens when the stack is empty vs. non-empty

🧠 MENTAL MODEL - Stack as "Waiting Room":
Think of the stack as a waiting room where days are waiting for warmer weather:

Day 0 (73°) enters waiting room: [0]
Day 1 (74°) arrives - warmer than day 0! Day 0 leaves, waited 1 day: []
Day 1 (74°) enters waiting room: [1]
Day 2 (75°) arrives - warmer than day 1! Day 1 leaves, waited 1 day: []
Day 2 (75°) enters waiting room: [2]
Day 3 (71°) arrives - cooler than day 2, joins waiting room: [2, 3]
Day 4 (69°) arrives - cooler than day 3, joins waiting room: [2, 3, 4]
Day 5 (72°) arrives - warmer than days 4 and 3! Both leave: [2]
Day 6 (76°) arrives - warmer than day 2! Day 2 leaves, waited 4 days: []

🔑 KEY INSIGHT:
Monotonic stacks are perfect for "next greater/smaller element" problems because:
1. They maintain the order we need automatically
2. One element can resolve multiple waiting elements efficiently
3. Each element is processed exactly once (pushed once, popped at most once)

💡 WHEN TO USE MONOTONIC STACKS:
- Finding next/previous greater or smaller elements
- Problems involving "waiting" for a condition to be met
- Histogram-related problems (largest rectangle, etc.)
- When you need to maintain order while processing sequentially
"""
