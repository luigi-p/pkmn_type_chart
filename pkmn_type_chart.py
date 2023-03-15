# importing pandas, numpy
import pandas as pd
import numpy as np

def pkmn_mono_type_chart(): # asks for a pkmn type and prints its super effective moves and weaknesses 
    # read excel file into pandas DataFrame
    df = pd.read_excel('pkmn_types_chart.xlsx')

    # initialaze all the nedded lists
    not_very_effective = []
    no_effect = []
    super_effective = []
    weak = []

    # take the type in input
    type = input("Which pkmn tipologie you want to check?\n").upper()

    # if the type is not in the colum names, keep asking a new input
    while type not in df.columns:
        type = input("Invalid input, retry: ").upper()

    # using .get_loc() to retrieve the index number of the given type
    # since rows and columns are the same here, we can use it for both
    index_n = df.columns.get_loc(type)

    # Super effective
    for i in range(len(df.index)):
        if np.array(df)[index_n-1][i] == "2x":
            super_effective.append(df.columns[i])

    # Weak
    for i in range(len(df.index)):
        if np.array(df)[i][index_n] == "2x":
            # if the value is 2x, add it to the list
            weak.append(df.axes[1][i+1])

    # Not very effective
    for i in range(len(df.index)):
        if np.array(df)[i][index_n] == "½×":
            # if the value is ½×, add it to the list
            not_very_effective.append(df.axes[1][i+1])

    # No effect
    for i in range(len(df.index)):
        if np.array(df)[i][index_n] == "0x":
            # if the value is 0x, add it to the list
            no_effect.append(df.axes[1][i+1])

    # print super effective
    print("\nAttack section")

    # Condition to spot the normal type, with no super effective moves
    if len(super_effective) > 0:
        print(type, "moves are super effective against:", ', '.join(super_effective))
    else:
        print(type, "type got no super effective moves, sadly.")

    print("\nDefense section")
    print("A", type, "type PKMN:")
    print("- is weak against:", ', '.join(weak))
    print("- resists against:", ', '.join(not_very_effective))

    # Condition because not all the types got a 0x
    if len(no_effect) > 0:
        print(type, "type can't be damaged by:", ', '.join(no_effect))

    print("\n")

def pkmn_double_types_chart(): # asks for a double type pkmn combination and prints its super effective moves and weaknesses
    # read excel file into pandas DataFrame
    df = pd.read_excel('pkmn_types_chart.xlsx')

    # take the type in input
    type_1 = input("Which is the first type?\n").upper()

    # if the type is not in the colum names, keep asking a new input
    while type_1 not in df.columns:
        type_1 = input("Invalid input, retry: ").upper()

    type_2 = input("Which is the second type?\n").upper()

    # if the type is not in the colum names or it's equal to the first input, keep asking a new input
    while type_2 not in df.columns or type_2 == type_1:
        type_2 = input("Invalid input, retry: ").upper()
    
    # using .get_loc() to retrieve the index number of the given type
    # since rows and columns are the same here, we can use it for both
    index_n_1 = df.columns.get_loc(type_1)
    index_n_2 = df.columns.get_loc(type_2)

    # initialaze all the needed lists
    not_very_effective_2x = []
    not_very_effective_4x = []
    no_effect = []
    super_effective_1 = []
    super_effective_2 = []
    weak_2x = []
    weak_4x = []

    """
    Legend
    weak 4x -> if both type_1 and type_2 got "2x" in the same cell
    weak 2x -> if only one between type_1 and type_2 got a "2x"
    standard dmg 1x -> if both type_1 and type got a "1x" OR if one of them got a "2x" and the second got a "½×"
    resists 2x -> if at lest one type got a "½×" and the second got NOT a "2x"
    resists 4x -> if both types got "½×"
    no effect 0x -> if at least one of them got a "0x"

    """

    # Weak 4x / weak 2x / not very effective 2x and 4x
    for i in range(len(df.index)):
        if np.array(df)[i][index_n_1] == "2x" and np.array(df)[i][index_n_2]== "2x":
            weak_4x.append(df.axes[1][i + 1])
        elif (np.array(df)[i][index_n_1] == "2x" or np.array(df)[i][index_n_2]== "2x") and (np.array(df)[i][index_n_1] == "1x" or np.array(df)[i][index_n_2] == "1x"):
            weak_2x.append(df.axes[1][i + 1])
        elif np.array(df)[i][index_n_1] == "½×" and np.array(df)[i][index_n_2]== "½×":
            not_very_effective_4x.append(df.axes[1][i + 1])
        elif (np.array(df)[i][index_n_1] == "½×" or np.array(df)[i][index_n_2]== "½×") and (np.array(df)[i][index_n_1] != "2x" or np.array(df)[i][index_n_2] != "2x"):
            not_very_effective_2x.append(df.axes[1][i + 1])
            
    # No effect 0x
    for i in range(len(df.index)):
        if np.array(df)[i][index_n_1] == "0x" or np.array(df)[i][index_n_2]== "0x":
            no_effect.append(df.axes[1][i+1])

    # Super effective moves type 1
    for i in range(len(df.index)):
        if np.array(df)[index_n_1 - 1][i] == "2x":
            super_effective_1.append(df.columns[i])

    # Super effective moves type 2
    for i in range(len(df.index)):
        if np.array(df)[index_n_2 - 1][i] == "2x":
            super_effective_2.append(df.columns[i])

    # starting of the print section
    print("\nAttack section")

     # Following conditions to verify if there is at least 1 match for every check
    if len(super_effective_1) > 0:
        print(type_1, "moves are super effective against:", ', '.join(super_effective_1))
    else:
        print(type_1, "type got no super effective moves, sadly.")

    if len(super_effective_2) > 0:
        print(type_2, "moves are super effective against:", ', '.join(super_effective_2))
    else:
        print(type_2, "type got no super effective moves, sadly.")

    print("\nDefense section")
    print("A", type_1 + "/" + type_2, "double type PKMN:")

    if len(weak_4x) > 0:
        print("- is 4 times weak against:", ', '.join(weak_4x))
    else:
        print("- got NO 4 times weaknesses, lucky you!")
    
    if len(weak_2x) > 0:
        print("- is 2 times weak against:", ', '.join(weak_2x))

    if len(not_very_effective_2x) > 0:
        print("- resists 2 times against:", ', '.join(not_very_effective_2x))
    
    if len(not_very_effective_4x) > 0:
        print("- resists 4 times against:", ', '.join(not_very_effective_4x))
    
    if len(no_effect) > 0:
        print("- can't be damaged by:", ', '.join(no_effect))
        
    print("\n")

def types_list():
    # read excel file into pandas DataFrame
    df = pd.read_excel('pkmn_types_chart.xlsx', index_col=0)

    print("\n")
    print(" \n".join(df.columns))
    print("\n")

while True:
  try:
    n_type = int(input("Does your PKMN have 1 or 2 types?\nIf you want to display the types list, type 3.\nIf you want to quit type 0.\n"))
    if n_type == 3:
        types_list()
        continue

    elif n_type == 1:
        pkmn_mono_type_chart()
        continue

    elif n_type == 2:
        pkmn_double_types_chart()
        continue

    elif n_type < 0 or n_type > 3:
        print("Integer must be 1, 2, 3 or 0, please retry.")
        continue
    elif n_type == 0:
        break
  
  except ValueError:
      print("Input must be an integer (1, 2, 3 or 0), please retry.")  
      continue
