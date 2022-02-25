def dictTotext(toConvert):
    converted = ""
    for key in toConvert:
        converted = converted + (str(key) + ": " + str(toConvert[key]) + "\n")
    return converted
