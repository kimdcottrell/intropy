import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # janky, but I don't have venv yet so PYTHONPATH isn't an option

from intropy import intro_to_functions as intro_func

intro_func.print_args('something', 'evil', 'this', 'way', 'comes!')

print('')

intro_func.print_kwargs(animal='dog', says='woof')

print('')

intro_func.public_func()

print('')

sum_of_nums = intro_func.add(2, 4)
print(f"sum: {sum_of_nums}")
