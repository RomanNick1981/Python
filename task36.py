# Просто
def print_operation_table(x,y):
    for i in range(1, x+1):
        for j in range(1, y+1):
            print(i*j, end=' ')
        print()
    return x*y
print_operation_table(6,6)

# Лямбда: 

def print_operation_table(x=6,y=6):
    for i in range(1, x+1):
        for j in range(1, y+1):
            print_operation_table(lambda x, y: x * y)
