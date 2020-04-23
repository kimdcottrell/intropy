def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_line(line_number, f):
    print(line_number, f.readline())



