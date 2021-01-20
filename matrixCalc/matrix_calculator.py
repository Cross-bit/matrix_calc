import sys
from matrix import *
from matrix_console_printer import MatrixConsolePrinter as matrix_printer
from elementary_operations import *
from input_reader import *
from operations.matrix_multiplication import *
from operations.matrix_transposition import *
from operations.matrix_to_ref import *
from operations.matrix_sum import *
from matrix_generator import *
from operation_handler import OperationExecutionHandler as OEH
from helpers import *
from operations.matrix_scalar_multiplication import MatrixScalarMultiplication
##Testovací matice
#matrix_generator = MatrixGenerator(5,2)
mx1 = MatrixGenerator.generate_random_matrix(5, 2)
matrix_printer.print_simple(mx1)
scal_multi = MatrixScalarMultiplication(mx1, 5)
matrix_printer.print_default(scal_multi.multiply()) 


# Hlavní blok programu
def main_loop():
    # 1)
    operation = operation_selection()
    # 2)
    data_load = data_load_selection()

    operations_handler = OEH(operation, data_load)
    operations_handler.execute()

    print("")
    return main_loop()


# Uživatelské rozhraní výběru operace uživatelem
def operation_selection():
    # Základní výpis dat
    # Separace UI od logiky
    print("Zvol operaci:\n")
    print("""1) Sečti matice \n2) Odečti matice \n3) Vynásob skalárem \n4) Vynásob mnatice \n5) Transponuj matici \n6) Převeď na REF \n7) Převeď to RREF \n8) Urči inverzní matici \n9) Urči hodnost \n10) Urči determinant 
        """)

    operation_input = input()

    operations = {
        1: OEH.mx_add,
        2: OEH.mx_sub,
        2: OEH.mx_sub,
        3: OEH.mx_scal,
        4: OEH.mx_multi,
        5: OEH.mx_trans,
        6: OEH.mx_ref,
        7: OEH.mx_rref,
        8: OEH.mx_inverse,
        9: OEH.mx_rank,
       10: OEH.mx_det,
       }
    

    if(operation_input.isnumeric()):
        operation_input = int(operation_input)
        if(operation_input < len(operations) and operation_input > 0):
            return operations.get(int(operation_input))

    print("Hodnota není povolena! Enter – opakujte akci")
    input()
    return operation_selection() # TODO: až bude v classe uklidit komentáře

# Uživatelské rozhraní výběru typu načtení dat
def data_load_selection():
    print("""Vyber způsob zadání hodnot:\n1) Zadání v konzoli \n2) Načtení ze souboru""")
    try:
        user_selection = int(input())
        if (user_selection == 1): #1 z konzole
            return OEH.load_data_from_console
        elif (user_selection == 2):
            return OEH.load_data_from_file

        print("Hodnota není povolena! Enter – opakujte akci")
        input()
        return data_load_selection()
    except:
        print("Hodnota není povolena! Enter – opakujte akci")
        input()
        return data_load_selection()

main_loop()


input()
sys.exit
matrix_printer.print_default(mx)

mx.generate_random_values()










