import decisions

options = int(input (" Input your option: "))

total = int(input ("Input the total: "))

return_ratio = decisions.get_options_ratio(options, total)

Score = decisions.get_faculty_rating(return_ratio)

print ("Your Rating Is: " + Score)

