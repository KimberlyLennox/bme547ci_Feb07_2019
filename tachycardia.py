def is_tachycardic(s):
    s=s.lower() #Convert string to completely lowercase
    s=s.lstrip() #Remove all leading spaces
    s=s.rstrip() #Remove all trailing spaces
    if s == "tachycardic":
        R = True
    else:
        R = False
    return(R)
