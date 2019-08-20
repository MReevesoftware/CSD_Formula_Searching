from ccdc.io import EntryReader
from itertools import groupby
import re

def split_text(s):
    for k, g in groupby(s, str.isalpha):
        yield ''.join(g)


formulas = open("formulas.txt",'rb')
formulas_list = formulas.readlines()
new_formula_list = []

for formula_string in formulas_list:
    formula_string = formula_string.rstrip('\n')
    output_formula_list_item = []
    fully_split_up = (list(split_text(formula_string)))
    for index, index_item in enumerate(fully_split_up):
        if  index %2 == 0:
            output_formula_list_item.append(index_item + fully_split_up[(index+1)])
    output_formula_list_item.sort()
    new_formula_list.append(output_formula_list_item)

print new_formula_list

csd_entry_reader = EntryReader('CSD')
output = open("Results.txt",'w')

for entry in csd_entry_reader:
    for component in entry.molecule.components:
        entry_formula = (component.formula).strip("(")
        entry_formula = entry_formula.strip(")n")
        entry_formula = (entry_formula).split(" ")
        entry_formula.sort()
        entry_formula = [i for i in entry_formula if re.search('[a-zA-Z]', i)]
        print entry.identifier
        if entry_formula in new_formula_list:
            output.write(component.formula+"," +entry.identifier+"\n")

