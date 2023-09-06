#create function named get_options_ratio that accepts two parameters with names option, total and returns the ratio.
#The function get_options_ratio will return the ratio of options divided by total.

def get_options_ratio(option, total):
    result = option / total
    return result

def get_faculty_rating(ratio):
    if ratio >= 0.9:
        result = "Excellent"
        return result
    elif ratio > 0.8:
        result = "Very Good"
        return result
    elif ratio > 0.7:
        result = "Good"
        return result
    elif ratio > 0.6:
        result = "Needs improvement"
        return result
    else:
        result = "Unacceptable"
        return result