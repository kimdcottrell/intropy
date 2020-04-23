from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

# we could do these two on one line
in_data = open(from_file).read()

print(f"""
The Input file is {len(in_data)} bytes long.
Does the output file exist? {exists(to_file)}
Ready, hit RETURN to continue. CTRL-C to abort.
""")
input()

open(to_file, 'w').write(in_data)

print("We're done!")
