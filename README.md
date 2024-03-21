# smt-kenken-solver

kenken2smt:

kenken2smt takes a kenken puzzle input in the format seen in 22395-puzzle.txt and generates the clause list seen in puzzle.cnf. Values pertaining to each region, as well as the target value and operation required for that region are stored in a dictionary whose key is the region number. Then, we simply use for loops to generate the list of necessary constraints: no repeats in any column or row, values must be between 1 and 7 inclusive, and the values for each region must be able to combine with the given operation in a way that produces the target value. To generate a solved puzzle model.smt, we run:

1. $ kenken2smt.py puzzle.txt puzzle.smt
2. $ mathsat puzzle.smt > model.smt

