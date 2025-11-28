def print_congratulations_banner(name):
    banner = """

"""
    print(banner)
    print(f"       Well done, {name}!")
    print("       You've achieved something great!")

name = input("Enter the name of the person to congratulate: ")
print_congratulations_banner(name)