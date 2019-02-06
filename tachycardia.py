def is_tachycardic(s):

    """This function takes a test input string and determines if
    the string is the word tachycardic"""

    s = s.lower()  # Convert string to completely lowercase
    s = s.lstrip()  # Remove all leading spaces
    s = s.rstrip()  # Remove all trailing spaces
    if s == "tachycardic":  # Returns tachycardic per specs of assignment
        R = True
    else:  # Extra credit: Check for a close string match
        # Used fuzzywuzzy package to calculate Levenshtein distance
        from fuzzywuzzy import fuzz
        from fuzzywuzzy import process
        n = fuzz.ratio(s, "tachycardic")
        if n >= 82:  # Ratio determined by trial and error
            R = True
        else:
            R = False
    return(R)
