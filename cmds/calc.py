import sys
sys.path.append("/")
def calc(arg):
    if arg == "-h":
        print("calculates an expression\ncalc [expression]")
    else:
        try:
            result = eval(arg)
            print("Result:", result)
        except:
            print("Error: Invalid expression")
