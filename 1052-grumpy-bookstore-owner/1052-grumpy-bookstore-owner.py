class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        # Calculate the number of satisfied customers without using the special power
        satisfied = sum(customers[:minutes])
        satisfied += sum((1 - grumpy[i]) * customers[i] for i in range(minutes, n))
        
        # Initialize the maximum satisfied customers
        max_satisfied = satisfied

        # Iterate through the remaining customers
        for i in range(minutes, n):
            # Subtract the satisfaction of the customer 'minutes' ago
            satisfied -= grumpy[i - minutes] * customers[i - minutes]
            # Add the satisfaction of the current customer
            satisfied += grumpy[i] * customers[i]
            # Update the maximum satisfied customers
            max_satisfied = max(max_satisfied, satisfied)

        return max_satisfied
        
        
        
        """n = len(customers)
        ans = 0
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]
        
        unsatis = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                unsatis += customers[i]
        
        max_ = unsatis
        for i in range(minutes, n):
            if grumpy[i - minutes] == 1:
                unsatis -= customers[i - minutes]
            if grumpy[i] == 1:
                unsatis += customers[i]
            max_ = max(max_, unsatis)
        
        return ans + max_
        """
        
        
        """initial_satisfaction = 0
        max_extra_satisfaction = 0
        current_window_satisfaction = 0
        
        for i in range(len(customers)):
            if grumpy[i] == 0:
                initial_satisfaction += customers[i]
            elif i < minutes:
                current_window_satisfaction += customers[i]
        
        max_extra_satisfaction = current_window_satisfaction
        
        for i in range(minutes, len(customers)):
            current_window_satisfaction += customers[i] * grumpy[i]
            current_window_satisfaction -= customers[i - minutes] * grumpy[i - minutes]
            max_extra_satisfaction = max(max_extra_satisfaction, current_window_satisfaction)
        
        return initial_satisfaction + max_extra_satisfaction
        """