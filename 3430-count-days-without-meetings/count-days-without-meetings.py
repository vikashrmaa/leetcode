class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days
        
        # Sort the meetings by their start day
        meetings.sort()
        merged = []
        
        for meeting in meetings:
            if not merged:
                merged.append(meeting)
            else:
                last_start, last_end = merged[-1]
                current_start, current_end = meeting
                if current_start <= last_end:
                    # Merge the intervals
                    new_start = last_start
                    new_end = max(last_end, current_end)
                    merged[-1] = [new_start, new_end]
                else:
                    merged.append(meeting)
        
        total_busy = 0
        for start, end in merged:
            adj_start = max(start, 1)
            adj_end = min(end, days)
            if adj_start > adj_end:
                continue
            total_busy += adj_end - adj_start + 1
        
        return days - total_busy