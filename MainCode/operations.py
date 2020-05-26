'''
Operation Functions
'''

# Imports


# Main Functions
def ExecuteOperation(opname, op1, op2):
    if opname in ['Add', 'Addi']:
        return op1 + op2
    elif opname in ['Sub']:
        return op1 - op2
    elif opname in ['Mult']:
        return op1 * op2