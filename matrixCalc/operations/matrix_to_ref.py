from elementary_operations import ElementaryOperations
from matrix import Matrix
from matrix_console_printer import MatrixConsolePrinter as matrix_printer

class MatrixREF:

    def __init__(self, matrix):
        self.mx = matrix
        self.mx_ref = Matrix(matrix.m, matrix.n)
        self.mx_ref.Data = matrix.Data
        self.rank = 0

    def convert_matrix_to_ref(self):

        pivot_i_pos = 0
        j = 0
        while (j < self.mx_ref.n and pivot_i_pos < self.mx_ref.m):
            
            # Pokud je pivot 0, tak je nutné prohodit řádky
            if(self.mx_ref.Data[pivot_i_pos][j] == 0):

                new_pivot_pos = ElementaryOperations.find_first_most_left_value(self.mx_ref, pivot_i_pos, j)

                # Už nejsou další pivoty, matice je odstupňovaná
                if(new_pivot_pos[0] == 0 and new_pivot_pos[1] == 0):
                    return self.mx_ref

                ElementaryOperations.exchange_rows(self.mx_ref, pivot_i_pos, int(new_pivot_pos[0]))
                j = int(new_pivot_pos[1])

            for i in range(pivot_i_pos+1, self.mx_ref.m):
                multiply_const = (-1)*self.mx_ref.Data[i][j] / self.mx_ref.Data[pivot_i_pos][j]

                # Přičtení násobku řádku
                for s in range(j, self.mx_ref.n):
                    self.mx_ref.Data[i][s] = self.mx_ref.Data[i][s] + self.mx_ref.Data[pivot_i_pos][s] * multiply_const
            
            matrix_printer.print_default(self.mx_ref)

            j += 1
            pivot_i_pos += 1

        return self.mx_ref
                    

                

                
