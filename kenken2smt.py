#!/usr/bin/env python

import fileinput
import textwrap
import sys
import csv

def get_region_data(): 

    regions = {}
    entries = []
    variables = ["V" + str(i) for i in range(49)]

    with open(sys.argv[2], 'r') as file:
        puzzle = file.read()

    lines = puzzle.split('\n')

    while lines and lines[-1].strip() == "":
        lines.pop()
    
    for line in lines[1:]:
        entries.extend(line.split(','))

    #isolate region operation and target and add to dictionary with relevent variables (cells)
    for i, entry in enumerate(entries):
        region_number = int(entry.split('.')[0][1:])
        parts = entry.split('.')

        if len(parts) > 1:
            target_operation = parts[1]
            target = target_operation[:-1]
            operation = target_operation[-1]     
        else:
            target_operation = None
        
        if region_number not in regions:
            regions[region_number] = []
        
        if target_operation is not None:
            regions[region_number].append(operation)
            regions[region_number].append(target)

        regions[region_number].append(variables[i])

    return regions

#Generate list of constraints
def generate_constraint_list(regions):
    
    #Setup, declare variables
    cnf_content= "(set-logic UFNIA)\n(set-option :produce-models true)\n(set-option :produce-assignments true)"
    variables = ["V" + str(i) for i in range(49)]
    for i in range(49):
        cnf_content += "\n(declare-const {} Int)".format(variables[i])
    
    #value constraints
    for i in range(49):
        cnf_content += "\n(assert (and (> {} 0) (< {} 8)))".format(variables[i], variables[i])

    #row uniqueness constraints
    for i in range(0, 49, 7):
        cnf_content += ("\n(assert (distinct {} ))".format(" ".join(variables[i:i+7])))
    
    #column uniqueness constraints
    for i in range(7):
        cnf_content += ("\n(assert (distinct {} ))".format(" ".join(variables[i:i+43:7])))

    #region constraints
    for region, info in regions.items():
        operation, target, *variables = info
        variables_str = ' '.join(variables)
        if operation == '*':
            cnf_content += (f"\n(assert (= {target} (* {variables_str}))) ; Region {region}")
        elif operation == '-':
            cnf_content += (f"\n(assert (or (= {target} (- {variables[0]} {variables[1]})) (= {target} (- {variables[1]} {variables[0]})))) ; Region {region}")
        elif operation == '+':
            cnf_content += (f"\n(assert (= {target} (+ {variables_str}))) ; Region {region}")
        elif operation == '/':
            cnf_content += (f"\n(assert (or (= {target} (/ {variables[0]} {variables[1]})) (= {target} (/ {variables[1]} {variables[0]})))) ; Region {region}")
    
    #wrap up
    cnf_content += "\n(check-sat)\n(get-value ({}))\n(exit)".format(" ".join("V" + str(i) for i in range(49)))

    return cnf_content

def write_to_output(cnf_content):
    w = open(sys.argv[1],"w")
    w.write(cnf_content)

regions = get_region_data()
cnf_content = generate_constraint_list(regions)
write_to_output(cnf_content)
