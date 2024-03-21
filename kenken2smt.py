#!/usr/bin/env python

import fileinput
import textwrap
import sys
import csv

#WORK IN PROGRESS
#Generate constraint for a region
def generate_constraint(region, value):
    variables = [f"V{i}" for i in region]
    clauses = []
    for i in range(len(variables)):
        for j in range(i+1, len(variables)):
            clauses.append(f"(or (= {value} (- {variables[i]} {variables[j]})) (= {value} (- {variables[j]} {variables[i]})))")
    return clauses

#Generate list of constraints
def generate_constraint_list():
    
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

    #WORK IN PROGRESS
    #generate regional constraints from puzzle
    with open(sys.argv[2], 'r') as file:
        reader = csv.reader(file)
        next(reader) #skip puzzle description
        for row in reader:
            for entry in row:
                if '.' in entry:
                    region, value = entry.split('.')
                    value = int(value[:-1])
                    region = [int(x[1:]) for x in region.split(',')]
                    clauses = generate_constraint(region, value)
                    for clause in clauses:
                        cnf_content += ("\n(assert " + clause + ")")
    return cnf_content

def write_to_output(cnf_content):
    w = open(sys.argv[1],"w")
    w.write(cnf_content)

cnf_content = generate_constraint_list()
write_to_output(cnf_content)
