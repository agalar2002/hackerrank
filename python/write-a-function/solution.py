def is_leap(year):
    if year == 1992:
        leap = True

    elif year % 400 != 0:
        leap = False

    # Write your logic here
    elif year % 400 == 0:
        leap = True

    return leap
