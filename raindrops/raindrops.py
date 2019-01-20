# append two lists, so [1, 2] + [3, 4] yields [1, 2, 3, 4]
def raindrops(number):
    list_of_factors = []
    factor3 = "Pling"
    factor5 = "Plang"
    factor7 = "Plong"
    factor35 = "PlingPlang"
    factor37 = "PlingPlong"
    factor735 = "PlingPlangPlong"
    factor75 = "PlangPlong"
    nofactor = str(number)

    for i in range(1, number):
        if number % i == 0:
            list_of_factors.append(i)
    if 3 in list_of_factors and 7 not in list_of_factors and 5 not in list_of_factors:
        return factor3
    if 5 in list_of_factors and 3 not in list_of_factors and 7 not in list_of_factors:
        return factor5
    if 7 in list_of_factors and 3 not in list_of_factors and 5 not in list_of_factors:
        return factor7
    if 3 in list_of_factors and 5 in list_of_factors and 7 not in list_of_factors:
        return factor35
    if 7 in list_of_factors and 3 in list_of_factors and 5 not in list_of_factors:
        return factor37
    if 7 in list_of_factors and 5 in list_of_factors and 3 not in list_of_factors:
        return factor75
    if 7 in list_of_factors and 3 in list_of_factors and 5 in list_of_factors:
        return factor735
    elif 3 not in list_of_factors and 5 not in list_of_factors and 7 not in list_of_factors:
        return nofactor



# short
drops = ((3,'Pling'), (5,'Plang'), (7,'Plong'))

def raindrops(n):
	"""Converts a number to a string according to the raindrop sounds."""

	speak = [s for f, s in drops if n % f == 0]
	return "".join(speak) if speak else str(n)
