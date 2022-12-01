# have user input a path to a file
try:
    path = input("enter a .ipynb file path (may vary based on your OS, typically defaults to root directory) >> ")
except:
    print("\nAn error occurred.")
    exit(0)

f = open(path, "r")

# read file as a dictionary
str_dict = f.read()
code = eval(str_dict)

# get the name of the ipynb file
ipynb_name = []
for i in range(1, len(path) + 1):
    if path[len(path) - i] != "/":
        ipynb_name.append(path[len(path) - i])
    else:
        break
file_name = ""
for i in range(1, len(ipynb_name) + 1):
    file_name += ipynb_name[len(ipynb_name) - i]

# get the path to the file location
path_to_file = path[0:path.index(file_name)]
file_name = file_name[0:file_name.index(".ipynb")] + ".R"

# create an R file in the same location with the same name
f_R = open(path_to_file + file_name, "w")

#write R code to the R file
for i in range(len(code["cells"])):
    for j in range(len(code["cells"][i]["source"])):
        to_print = code["cells"][i]["source"][j]
        if j == (len(code["cells"][i]["source"]) - 1):
            to_print += "\n"
        if code["cells"][i]["cell_type"] == "code":
            f_R.write(to_print)

# success message
print(file_name + " successfully created. Cheers.")