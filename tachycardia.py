def is_tachycardic(s):

    """This function takes a test input string and determines if
    the string is the word tachycardic"""

    s = s.lower()  # Convert string to completely lowercase
    s = s.lstrip()  # Remove all leading spaces
    s = s.rstrip()  # Remove all trailing spaces
    if s == "tachycardic":
        R = True
    else:
        R = False
    return(R)
