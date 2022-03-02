# Molar Mass Calculator by Alex Tomsovic
# linktr.ee/alextomsovic

# List of all elemental symbols
element_symbols_list= ['H', 'HE', 'LI', 'BE', 'B', 'C', 'N', 'O', 'F', 'NE', 'NA', 'MG', 'AL', 'SI', 'P', 'S', 'CL', 'AR', 'K', 'CA', 'SC', 'TI', 'V', 'CR', 'MN', 'FE', 'CO', 'NI', 'CU', 'ZN', 'GA', 'GE', 'AS', 'SE', 'BR', 'KR', 'RB', 'SR', 'Y', 'ZR', 'NB', 'MO', 'TC', 'RU', 'RH', 'PD', 'AG', 'CD', 'IN', 'SN', 'SB', 'TE', 'I', 'XE', 'CS', 'BA', 'LA', 'CE', 'PR', 'ND', 'PM', 'SM', 'EU', 'GD', 'TB', 'DY', 'HO', 'ER', 'TM', 'YB', 'LU', 'HF', 'TA', 'W', 'RE', 'OS', 'IR', 'PT', 'AU', 'HG', 'TL', 'PB', 'BI', 'PO', 'AT', 'RN', 'FR', 'RA', 'AC', 'TH', 'PA', 'U', 'NP', 'PU', 'AM', 'CM', 'BK', 'CT', 'ES', 'FM', 'MD', 'NO', 'LR', 'RF', 'DB', 'SG', 'BH', 'HS', 'MT', 'DS', 'RG', 'CN', 'NH', 'FL', 'MC', 'LV', 'TS', 'OG']

# Symbol / MM dictionary
molar_mass_dictionary = {'H' : 1.007,'HE' : 4.003, 'LI' : 6.941, 'BE' : 9.012, 'B' : 10.811, 'C' : 12.011, 'N' : 14.007, 'O' : 15.999, 'F' : 18.998, 'NE' : 20.180, 'NA' : 22.990, 'MG' : 24.305, 'AL' : 26.982, 'SI' : 28.086, 'P' : 30.974, 'S' : 32.066, 'CL' : 35.453, 'AR' : 39.948, 'K' : 39.098, 'CA' : 40.078, 'SC' : 44.956, 'TI' : 47.867, 'V' : 50.942, 'CR' : 51.996, 'MN' : 54.938, 'FE' : 55.845, 'CO' : 58.933, 'NI' : 58.693, 'CU' : 63.546, 'ZN' : 65.38, 'GA' : 69.723, 'GE' : 72.631, 'AS' : 74.922, 'SE' : 78.971, 'BR' : 79.904, 'KR' : 84.798, 'RB' : 84.468, 'SR' : 87.62, 'Y' : 88.906, 'ZR' : 91.224, 'NB' : 92.906, 'MO' : 95.95, 'TC' : 98.907, 'RU' : 101.07, 'RH' : 102.906, 'PD' : 106.42, 'AG' : 107.868, 'CD' : 112.414, 'IN' : 114.818, 'SN' : 118.711, 'SB' : 121.760, 'TE' : 126.7, 'I' : 126.904, 'XE' : 131.294, 'CS' : 132.905, 'BA' : 137.328, 'LA' : 138.905, 'CE' : 140.116, 'PR' : 140.908, 'ND' : 144.243, 'PM' : 144.913, 'SM' : 150.36, 'EU' : 151.964, 'GD' : 157.25, 'TB' : 158.925, 'DY': 162.500, 'HO' : 164.930, 'ER' : 167.259, 'TM' : 168.934, 'YB' : 173.055, 'LU' : 174.967, 'HF' : 178.49, 'TA' : 180.948, 'W' : 183.84, 'RE' : 186.207, 'OS' : 190.23, 'IR' : 192.217, 'PT' : 195.085, 'AU' : 196.967, 'HG' : 200.592, 'TL' : 204.383, 'PB' : 207.2, 'BI' : 208.980, 'PO' : 208.982, 'AT' : 209.987, 'RN' : 222.081, 'FR' : 223.020, 'RA' : 226.025, 'AC' : 227.028, 'TH' : 232.038, 'PA' : 231.036, 'U' : 238.029, 'NP' : 237, 'PU' : 244, 'AM' : 243, 'CM' : 247, 'BK' : 247, 'CT' : 251, 'ES' : 252, 'FM' : 257, 'MD' : 258, 'NO' : 259, 'LR' : 262, 'RF' : 261, 'DB' : 262, 'SG' : 266, 'BH' : 264, 'HS' : 269, 'MT' : 268, 'DS' : 271, 'RG' : 272, 'CN' : 285, 'NH' : 284, 'FL' : 289, 'MC' : 288, 'LV' : 292, 'TS' : 294, 'OG' : 294}

# Title and instructions
print('Molar Mass Calculator ')

print("")

print("To use the molar mass calculator, enter your element or compound with spaces between each compound and subscript. To calculate C4H8O2, input 'C 4 H 8 O 2'. ")

print("")

# retrieve users elemental formula
formula = input("Enter your element / compound or type 'exit' to exit: ").upper().split()
print("")

# Loops the retrieval request for data until EXIT is given.
while formula != ["EXIT"]:
    
    # Set the conditons for a new loop.
    molar_mass_float = 0.0
    invalid_input = False
    equation_coeff = 1
    
    # Loops through each formula index.__file__
    for i, ch in enumerate(formula):
        # If the given character is an  element in the list, check if the following character is an int.
        if ch in element_symbols_list:
            element_mass = molar_mass_dictionary.get(ch)
            # If the following character is an integer, multiply the mass of the given element by that integer and add that float to the sum.
            if formula[i + 1].isdigit() == True:
                molar_mass_float += element_mass * int(formula[i + 1])
            #If it's not an integer, just add to the sum.
            else:
                molar_mass_float += element_mass
        # If the charcter is an integer
        elif ch.isdigit() == True:
            # If the first index is an integer it is assumed as a coeff and the formula is multiplied by said coeff.
            if i == 0:
                equation_coeff = int(ch)
            # Makes sure previous index wasn't an integer since it needs an element to multiply with if it was. Else produce an error message. 
            elif formula[i - 1].isalpha() == False:
                invalid_input = True
            else:
                pass
        # Produce an error if the only character is an integer.
        elif ch.isdigit() == True and len(formula) == 1:
            invalid_input = True
        # Produce an error if the character returned isn't an integer or element. 
        else:
            invalid_input = True
    
    # Muliply the coeff by the whole molar mass. 
    molar_mass_float *= equation_coeff
    
    if invalid_input == True:
        # Prodice an error for only a subscript.__package__
        if ch.isdigit() == True and len(formula) == 1:
            print("Subscript not assigned to element.")
            print()
        # Produce an error for a float or non element. 
        else:
            print("Enter only elements and whole number subscripts.")
            print()
    
    # Print molar mass assuming no errors.
    else:
        print("The molar mass is: " , round(molar_mass_float, 3))
        print("")
    
    # Requests another formula. 
    formula = input("Enter your element / compound or type 'exit' to exit: ").upper().split()
    print("")      
