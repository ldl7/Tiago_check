# 🟡 Intermediate Level Problems

Welcome to the intermediate level! These problems provide **reduced guidance** and expect you to apply the patterns you learned in the beginner section more independently.

## 📚 Problem List

### 1. Three Sum
**File:** `01_three_sum.py`  
**Pattern:** Two Pointer + Sorting  
**Challenge:** Extend two-sum to three elements, handle duplicates

### 2. Longest Substring Without Repeating Characters
**File:** `02_longest_substring_no_repeat.py`  
**Pattern:** Variable Sliding Window + Hash Set  
**Challenge:** Dynamic window size based on character uniqueness

### 3. Subarray Sum Equals K
**File:** `03_subarray_sum_equals_k.py`  
**Pattern:** Prefix Sum + Hash Map  
**Challenge:** Count subarrays instead of just finding them

### 4. Search in Rotated Sorted Array
**File:** `04_search_rotated_array.py`  
**Pattern:** Modified Binary Search  
**Challenge:** Adapt binary search for rotated arrays

### 5. Next Greater Element
**File:** `05_next_greater_element.py`  
**Pattern:** Monotonic Stack + Hash Map  
**Challenge:** Process one array to answer queries about another

## 🎯 What's Different at Intermediate Level

### **Less Hand-Holding**
- Fewer step-by-step explanations
- You need to figure out the implementation details
- Hints point you in the right direction but don't give away the solution

### **Pattern Combination**
- Problems often combine multiple patterns
- You need to recognize which patterns to use
- Integration of data structures becomes important

### **Edge Case Handling**
- You're expected to think about edge cases yourself
- Test cases include tricky scenarios
- Error handling becomes your responsibility

### **Optimization Focus**
- Solutions should be efficient from the start
- You need to analyze time/space complexity independently
- Consider multiple approaches and choose the best one

## 💡 Approach Strategy

### **1. Pattern Recognition**
- Read the problem and identify familiar patterns
- Look for keywords: "subarray", "next greater", "sorted", etc.
- Think about what data structures might be helpful

### **2. Plan Before Coding**
- Sketch out your approach on paper
- Consider edge cases and how to handle them
- Think about the time/space complexity

### **3. Implement Incrementally**
- Start with a basic solution
- Add optimizations and edge case handling
- Test frequently with the provided test cases

### **4. Debug and Refine**
- If your solution doesn't work, trace through examples
- Check boundary conditions and off-by-one errors
- Consider alternative approaches if stuck

## 🔄 Problem-Solving Tips

### **For Two Pointer Problems**
- Always consider if sorting helps
- Think about what each pointer represents
- Handle duplicates carefully

### **For Sliding Window Problems**
- Clearly define your window invariant
- Know when to expand vs. contract
- Use appropriate data structures to track window state

### **For Binary Search Problems**
- Identify what you're searching for (value vs. condition)
- Be careful with boundary updates
- Test with edge cases (empty array, single element)

### **For Hash Map Problems**
- Think about what you need to "remember"
- Consider frequency counting vs. existence checking
- Handle the case where you need to avoid using the same element twice

### **For Stack Problems**
- Determine if you need monotonic increasing or decreasing
- Think about what each stack element represents
- Consider what triggers a pop operation

## 🚀 Success Metrics

You're ready for advanced level when you can:

- [ ] Recognize patterns quickly (within 1-2 minutes)
- [ ] Implement solutions with minimal hints
- [ ] Handle edge cases without explicit guidance
- [ ] Analyze time/space complexity correctly
- [ ] Debug your own solutions effectively
- [ ] Consider multiple approaches and choose the optimal one

## 📝 Common Pitfalls to Avoid

### **Rushing to Code**
- Take time to understand the problem fully
- Plan your approach before implementing
- Consider edge cases upfront

### **Ignoring Complexity**
- Always analyze your solution's efficiency
- Look for opportunities to optimize
- Don't settle for brute force if better solutions exist

### **Not Testing Thoroughly**
- Run all provided test cases
- Create your own edge case tests
- Trace through your algorithm with examples

### **Pattern Tunnel Vision**
- Don't force a pattern if it doesn't fit
- Some problems may require novel approaches
- Be flexible in your thinking

## 🔄 Next Steps

- **Complete all intermediate problems**
- **Time yourself** - aim for 15-20 minutes per problem
- **Review beginner patterns** if you get stuck
- **Move to advanced level** when consistently successful
- **Practice on external platforms** (LeetCode, HackerRank)

Remember: The goal is to develop independent problem-solving skills! 💪
