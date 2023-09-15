#create function named get_options_ratio that accepts two parameters with names option, total and returns the ratio.
#The function get_options_ratio will return the ratio of options divided by total.

def get_options_ratio(option, total):

    ratio = option / total
    return ratio

def get_faculty_rating(ratio):
    result = ""

    if (ratio >= .9 and ratio <= 1): 
        result = "Excellent"
        
    elif(ratio >= 0.8 and ratio < .9):
        result = "Very Good"
        
    elif(ratio >= 0.7 and ratio < 0.8):
        result = "Good"
    
    elif(ratio >= 0.6 and ratio < 0.7):
        result = "Needs Improvement"

    elif(ratio >= 0.0 and ratio  < 0.6):
        result = "Unacceptable"

    else:
        result = "Invalid"
        
    return result
    
    