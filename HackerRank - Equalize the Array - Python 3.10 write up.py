##    https://www.hackerrank.com/challenges/equality-in-a-array/problem
##
##    Given an array of integers, determine the minimum number of elements to
##    delete to leave only elements of equal value.

##### ##### ##### #####

#   O(n)
#   n is the number of elements in arr

#   Idea:
#       If we know which element in arr occurs the most and we know
#       how many times it occurs, then we can simply subtract that number
#       from the total number of elements in arr to find the value we are
#       looking for.

#   Algo:
#       1. initalize an empty dictionary to use as an occurrence table => O(1)
#       2. loop through arr, storing elements of arr as keys in the dictionary,
#           and the number of occurrences as the associated value => O(|arr|)
#       3. initalize variable to keep track of the current max occurrence count => O(1)
#       4. loop through the occurrence table and keep track of the largest
#           value found => O(|occurrence table|)
#       5. return |arr| - max occurrence count => O(1)

def equalizeArray(arr):
    
    #####
    
    occurrence_table = dict()
    
    for integer in arr:
        
        try:
            occurrence_table[integer] += 1
            
        except:
            occurrence_table[integer] = 1
            
    #####
    
    max_occurring_count = 0
    
    for integer_key in occurrence_table:
        
        if occurrence_table[integer_key] > max_occurring_count:
            
            max_occurring_count = occurrence_table[integer_key]
            
    return len(arr) - max_occurring_count
