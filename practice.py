



def readHeader(file):
    header = file.readline()
    header_components = header.split()
    return int(header_components[0]), int(header_components[1]), int(header_components[2]), int(header_components[3])

def read(file):
    line = file.readline()
    components = line.split()
    return components[1:]


f = open("a_example", "r")
no_of_pizzas, teams_of_2, teams_of_3, teams_of_4 = readHeader(f) 
print(no_of_pizzas)
print(teams_of_2)
print(teams_of_3)
print(teams_of_4)

for i in range(no_of_pizzas):
    print(read(f))