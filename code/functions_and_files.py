import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # janky, but I don't have venv yet so PYTHONPATH isn't an option

from intropy import functions_and_files as func_files

script, input_file = sys.argv

current_file = open(input_file)

print("Let's print the whole file:")

func_files.print_all(current_file)

print("Rewind!")

func_files.rewind(current_file)

print("Printing 3 lines...")

for i in range(0, 3):
    func_files.print_a_line(i, current_file)