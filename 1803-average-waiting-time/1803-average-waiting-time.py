class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = 0
        total_time = 0
        for arrival, order in customers:
            if time > arrival:
                total_time += time - arrival
            else:
                time = arrival 
            total_time += order
            time += order
        return total_time / len(customers)
        
        
        
        
        
        
        
        
        
        
        
        
        """available_at = 0
        total_wait = 0
        for arrival, t in customers:
            available_at = max(available_at, arrival) + t
            total_wait += available_at - arrival
        
        return total_wait / len(customers)"""