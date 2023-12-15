def over_write(List, Dictionary):   # an overwrite function
    L = List    # assign list with variable name 'L'
    d = Dictionary    # assign Dictionary with variable name 'd'
    """
    Update quantity of product after customer purchased some quantity of any product.
    And print remaining stock products.
    """
    for keys in d.keys():
        if keys == "METAL PASTE":
            L[0][2] = str(int(L[0][2])-d['METAL PASTE'])
        elif keys == "WOODEN FLOOR":
            L[1][2] = str(int(L[1][2])-d['WOODEN FLOOR'])
        else:
            L[2][2] = str(int(L[2][2])-d['WOODEN PUTT'])
    print("\nRemaining Products:\n",L)
        
    files = open("products.txt", "w")  # opens stock file (products.txt) file in write mode.
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return
