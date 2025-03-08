class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Create a HashSet to track seen elements
        Set<Integer> seen = new HashSet<>();
        // Iterate through the array
        for (int num : nums) {
            // If the element is already in the set, a duplicate exists
            if (seen.contains(num))
                return true;
            // Otherwise, add the element to the set
            else
                seen.add(num);
        }
        // No duplicates found
        return false;
    }
}   
    