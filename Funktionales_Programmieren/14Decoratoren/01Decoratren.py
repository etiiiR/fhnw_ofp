def myfunction():
    print("Hello World")

var_func = myfunction
var_func()


dict_of_functions = {
    "func1": myfunction,
    "func2": open,
    "func3": print
}

dict_of_functions["func3"]("Hey Wolfgang")