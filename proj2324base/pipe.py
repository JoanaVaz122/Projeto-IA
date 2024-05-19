# pipe.py: Template para implementação do projeto de Inteligência Artificial 2023/2024.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes sugeridas, podem acrescentar outras que considerem pertinentes.

# Grupo 17:
# 107161 Irell Zane
# 106078 Joana Vaz

import sys
from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)


class PipeManiaState:

    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = PipeManiaState.state_id
        PipeManiaState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    def rotate(self, row, col, clockwise):
        headings_list = {
            "F": ["FD", "FC", "FE", "FB"],
            "B": ["BD", "BC", "BE", "BB"],
            "V": ["VD", "VC", "VE", "VB"],
            "L": ["LH","LV"]
        }
        #print(row, col, clockwise)

        new_board = self.board.copy_board()
        value = self.board.get_value(row, col)
        headings = headings_list[value[0]]
        inc = -1 if clockwise else 1
        new_board.pipes[row][col] = headings[(headings.index(value) + inc) % len(headings)]
        return PipeManiaState(Board(new_board.pipes))


class Board:
    """Representação interna de um tabuleiro de PipeMania."""
    def __init__(self, pipes) -> None:
        self.pipes = pipes
        self.nrows = len(self.pipes)
        self.ncols = len(self.pipes)

    def is_valid_indices(self, row: int, col: int) -> bool:
        """Devolve True se os indices existem no Board e
        False caso contrário"""

        return 0 <= row < self.nrows and 0 <= col < self.ncols

    def get_value(self, row: int, col: int) -> str:
        if not self.is_valid_indices(row, col):
            raise IndexError("Board row or column out of bounds")
        return self.pipes[row][col]

    def copy_board(self):
        """Copia da Representação interna de um tabuleiro de PipeMania."""

        new_board = Board([[get_value(row, col) for col in range(self.ncols)] for row in range(self.nrows)], self.nrows, self.ncols)
        return new_board

    def adjacent_vertical_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""
        if not self.is_valid_indices(row, col):
            raise IndexError("Board row or column out of bounds")

        if self.is_valid_indices(row - 1, col):
            pipe_above = self.get_value(row - 1, col)
        else:
            pipe_above = None

        if self.is_valid_indices(row + 1, col):
            pipe_below = self.get_value(row + 1, col)
        else:
            pipe_below = None

        return (pipe_above, pipe_below)

    def adjacent_horizontal_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        if not self.is_valid_indices(row, col):
            raise IndexError("Board row or column out of bounds")

        if self.is_valid_indices(row, col - 1):
            pipe_left = self.get_value(row, col - 1)
        else:
            pipe_left = None

        if self.is_valid_indices(row, col + 1):
            pipe_right = self.get_value(row, col + 1)
        else:
            pipe_right = None

        return (pipe_left, pipe_right)

    @staticmethod 
    def read_pipes():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma matriz dos pipes."""
        pipes = list()
        while True:
            pipe_row = sys.stdin.readline().split()
            if not pipe_row:
                break
            pipes.append(pipe_row)
        return pipes

    @staticmethod
    def parse_instance():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 pipe.py < test-01.txt


        """
        pipes = Board.read_pipes()
        return Board(pipes)

    def print(self):
        """Imprime o tabuleiro de PipeMania."""
        board_output = []
        for row in range(self.nrows):
            board_output.append("\t".join([self.get_value(row, col) for col in range(self.ncols)]))
        return "\n".join(board_output)



    # TODO: outros metodos da classe


class PipeMania(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        super().__init__(PipeManiaState(board))

    def actions(self, state: PipeManiaState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        action_list = list()
        nrows = self.initial.board.nrows
        ncols = self.initial.board.ncols
        for i in range(nrows):
            for j in range(ncols):
                # Verificar se a peça já está na orientação correta
                pipe = state.board.get_value(i, j)
                if pipe not in ['FD', 'FC', 'FE', 'FB', 'BD', 'BC', 'BE', 'BB', 'VD', 'VC', 'VE', 'VB', 'LH', 'LV']:
                    # Adicionar a ação de rotação para a direita
                    action_list.append((i, j, True))
                    # Adicionar a ação de rotação para a esquerda
                    action_list.append((i, j, False))
        return action_list


    def result(self, state: PipeManiaState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""

        return state.rotate(*action)

        
# pipe.py: Template para implementação do projeto de Inteligência Artificial 2023/2024.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes sugeridas, podem acrescentar outras que considerem pertinentes.

# Grupo 17:
# 107161 Irell Zane
# 106078 Joana Vaz

import sys
from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)


class PipeManiaState:

    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = PipeManiaState.state_id
        PipeManiaState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    def rotate(self, row, col, clockwise):
        headings_list = {
            "F": ["FD", "FC", "FE", "FB"],
            "B": ["BD", "BC", "BE", "BB"],
            "V": ["VD", "VC", "VE", "VB"],
            "L": ["LH","LV"]
        }
        #print(row, col, clockwise)

        new_board = self.board.copy_board()
        value = self.board.get_value(row, col)
        headings = headings_list[value[0]]
        inc = -1 if clockwise else 1
        new_board.pipes[row][col] = headings[(headings.index(value) + inc) % len(headings)]
        return PipeManiaState(new_board)


class Board:
    """Representação interna de um tabuleiro de PipeMania."""
    def __init__(self, pipes) -> None:
        self.pipes = pipes
        self.nrows = len(self.pipes)
        self.ncols = len(self.pipes)


    def is_valid_indices(self, row: int, col: int) -> bool:
        """Devolve True se os indices existem no Board e
        False caso contrário"""

        return 0 <= row < self.nrows and 0 <= col < self.ncols

    def get_value(self, row: int, col: int) -> str:
        if not self.is_valid_indices(row, col):
            raise IndexError("Board row or column out of bounds")
        return self.pipes[row][col]


    def adjacent_vertical_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente acima e abaixo,
        respectivamente."""
        if not self.is_valid_indices(row, col):
            raise IndexError("Board row or column out of bounds")

        if self.is_valid_indices(row - 1, col):
            pipe_above = self.get_value(row - 1, col)
        else:
            pipe_above = None

        if self.is_valid_indices(row + 1, col):
            pipe_below = self.get_value(row + 1, col)
        else:
            pipe_below = None

        return (pipe_above, pipe_below)

    def copy_board(self):
        """Copia da Representação interna de um tabuleiro de PipeMania."""
        return Board([[self.get_value(row, col) for col in range(self.ncols)] for row in range(self.nrows)])

    def adjacent_horizontal_values(self, row: int, col: int) -> (str, str):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        if not self.is_valid_indices(row, col):
            raise IndexError("Board row or column out of bounds")

        if self.is_valid_indices(row, col - 1):
            pipe_left = self.get_value(row, col - 1)
        else:
            pipe_left = None

        if self.is_valid_indices(row, col + 1):
            pipe_right = self.get_value(row, col + 1)
        else:
            pipe_right = None

        return (pipe_left, pipe_right)

    @staticmethod 
    def read_pipes():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma matriz dos pipes."""
        pipes = list()
        while True:
            pipe_row = sys.stdin.readline().split()
            if not pipe_row:
                break
            pipes.append(pipe_row)
        return pipes

    @staticmethod
    def parse_instance():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 pipe.py < test-01.txt


        """
        pipes = Board.read_pipes()
        return Board(pipes)

    def print(self):
        """Imprime o tabuleiro de PipeMania."""
        board_output = []
        for row in range(self.nrows):
            board_output.append("\t".join([self.get_value(row, col) for col in range(self.ncols)]))
        return "\n".join(board_output)



    # TODO: outros metodos da classe


class PipeMania(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        super().__init__(PipeManiaState(board))

    
    def adiciona_lista_pecas_F(i, j, pipe, action_list):
        if pipe[0] == 'F':
            if pipe[1]== 'C':
                action_list.append((i, j, 'FB'))
                action_list.append((i, j, 'FE'))
                action_list.append((i, j, 'FD'))
            elif pipe[1]== 'B':
                action_list.append((i, j, 'FC'))
                action_list.append((i, j, 'FE'))
                action_list.append((i, j, 'FD'))
            elif pipe[1]== 'E':
                action_list.append((i, j, 'FC'))
                action_list.append((i, j, 'FB'))
                action_list.append((i, j, 'FD'))  
            elif pipe[1]== 'D':
                action_list.append((i, j, 'FC'))
                action_list.append((i, j, 'FB'))
                action_list.append((i, j, 'FE'))  
    
    def adiciona_lista_pecas_B(i, j,pipe, action_list):
        if pipe[0] == 'B':
            if pipe[1]== 'C':
                action_list.append((i, j, 'BB'))
                action_list.append((i, j, 'BE'))
                action_list.append((i, j, 'BD'))
            elif pipe[1]== 'B':
                action_list.append((i, j, 'BC'))
                action_list.append((i, j, 'BE'))
                action_list.append((i, j, 'BD'))
            elif pipe[1]== 'E':
                action_list.append((i, j, 'BC'))
                action_list.append((i, j, 'BB'))
                action_list.append((i, j, 'BD'))  
            elif pipe[1]== 'D':
                action_list.append((i, j, 'BC'))
                action_list.append((i, j, 'BB'))
                action_list.append((i, j, 'BE'))

    def adiciona_lista_pecas_V(i, j,pipe, action_list):
        if pipe[0] == 'V':
            if pipe[1]== 'C':
                action_list.append((i, j, 'VB'))
                action_list.append((i, j, 'VE'))
                action_list.append((i, j, 'VD'))
            elif pipe[1]== 'B':
                action_list.append((i, j, 'VC'))
                action_list.append((i, j, 'VE'))
                action_list.append((i, j, 'VD'))
            elif pipe[1]== 'E':
                action_list.append((i, j, 'VC'))
                action_list.append((i, j, 'VB'))
                action_list.append((i, j, 'VD'))  
            elif pipe[1]== 'D':
                action_list.append((i, j, 'VC'))
                action_list.append((i, j, 'VB'))
                action_list.append((i, j, 'VE'))

    def adiciona_lista_pecas_V(i,j,pipe, action_list):
        if pipe[0] == 'L':
            if pipe[1]== 'H':
                action_list.append((i, j, 'LV'))

            elif pipe[1]== 'V':
                action_list.append((i, j, 'LH'))
 


        



    def actions(self, state: PipeManiaState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""

        action_list = list()

        nrows = self.initial.board.nrows
        ncols = self.initial.board.ncols
        #print(ncols, nrows)

        for i in range(nrows):
            for j in range(ncols):

                pipe = state.board.get_value(i, j)
                rotated = False

                #casoso cantos
                if(i,j) == (0,0):
                    if pipe == 'VB':
                        continue
                    elif pipe == 'VC' or pipe == 'VE' or pipe == 'VD':
                        pipe = 'VB'
                elif (i, j) == (0, ncols - 1):
                    if pipe == 'VE':
                        continue
                    elif pipe == 'VB' or pipe == 'VC' or pipe == 'VD':
                        pipe = 'VE'
                elif (i, j) == (nrows - 1, 0):
                    if pipe == 'VD':
                        continue
                    elif pipe == 'VB' or pipe == 'VC' or pipe == 'VE':
                        pipe = 'VD'
                elif (i, j) == (nrows - 1, ncols - 1):
                    if pipe == 'VC':
                        continue
                    elif pipe == 'VB' or pipe == 'VD' or pipe == 'VE':
                        pipe = 'VC'
                adiciona_lista_pecas_F(i, j, pipe, action_list)
                adiciona_lista_pecas_B(i, j, pipe, action_list)
                adiciona_lista_pecas_L(i, j, pipe, action_list)



                # Casos para a linha de cima
                elif i == 0:
                    if pipe == "BB" or pipe == "LH":
                        continue
                    elif pipe == "BC":
                        action_list.append((i, j, 'BC')) 

                    elif pipe == "BE":
                        action_list.append((i, j, 'BC'))
  
                    else:
                        adiciona_lista_pecas_F(i, j, pipe, action_list)
                        adiciona_lista_pecas_B(i, j, pipe, action_list)
                        adiciona_lista_pecas_L(i, j, pipe, action_list)
                        adiciona_lista_pecas_V(i, j, pipe, action_list)



                # Casos para linha de baixo
                elif i == nrows - 1:
                    if pipe == "BC" or pipe == "LH":
                        continue
                    elif pipe == "BB":
                        action_list.append((i, j, 'BC')) 
                        
                    elif pipe == "BD":
                        action_list.append((i, j, 'BC'))  
                        
                    else:
                        adiciona_lista_pecas_F(i, j, pipe, action_list)
                        adiciona_lista_pecas_B(i, j, pipe, action_list)
                        adiciona_lista_pecas_L(i, j, pipe, action_list)
                        adiciona_lista_pecas_V(i, j, pipe, action_list)
                        
                # Casos para a linha da direita
                elif j == ncols - 1:
                    if pipe == "BE" or pipe == "LV":
                        continue
                    elif pipe == "BD":
                        action_list.append((i, j, 'BE')) 
                         
                    elif pipe == "BC":
                        action_list.append((i, j, 'BE'))
                           
                    else:
                        adiciona_lista_pecas_F(i, j, pipe, action_list)
                        adiciona_lista_pecas_B(i, j, pipe, action_list)
                        adiciona_lista_pecas_L(i, j, pipe, action_list)
                        adiciona_lista_pecas_V(i, j, pipe, action_list)
                         
                # Casos para a linha da esquerda
                elif j == 0:
                    if pipe == "BD" or pipe == "LV":
                        continue
                    elif pipe == "BE":
                        action_list.append((i, j, 'BD')) 
                         
                    elif pipe == "BB":
                        action_list.append((i, j, 'BD'))  
                         
                    else:
                        adiciona_lista_pecas_F(i, j, pipe, action_list)
                        adiciona_lista_pecas_B(i, j, pipe, action_list)
                        adiciona_lista_pecas_L(i, j, pipe, action_list)
                        adiciona_lista_pecas_V(i, j, pipe, action_list)
                         
                # restantes casos que faltam (dentro do board)
                else:
                    adiciona_lista_pecas_F(i, j, pipe, action_list)
                    adiciona_lista_pecas_B(i, j, pipe, action_list)
                    adiciona_lista_pecas_L(i, j, pipe, action_list)
                    adiciona_lista_pecas_V(i, j, pipe, action_list)
                     
        return action_list


    def result(self, state: PipeManiaState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""

        return state.rotate(*action)

        
    def goal_test(self, state: PipeManiaState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas corretamente e formam um caminho contínuo."""

        # Verificar se todas as posicoes do board estao corretamente preenchidas
        pipe_list = ["FD", "FC", "FE", "FB", "BD", "BC", "BE", "BB", "VD", "VC", "VE", "VB", "LH", "LV"]
        
        for row in range(state.board.nrows):
            for col in range(state.board.ncols):
                pipe = state.board.get_value(row, col)
                if pipe not in pipe_list:
                    return False  # Encontrou uma posicao vazia ou com input errado, nao e um estado objetivo

        # Verificar se todas as peças estao conectadas formando um caminho contínuo
        visited = [[False] * state.board.ncols for _ in range(state.board.nrows)]
        #num_connected_components = 0

        def dfs(row, col, source=None):
            if not state.board.is_valid_indices(row, col):
                return False 
            if visited[row][col]:
                return True

            visited[row][col] = True
            pipe = state.board.get_value(row, col)

            lig_esq = ["FE", "BC", "BB", "BE", "VC", "VE", "LH"]
            lig_dir = ["FD", "BC", "BB", "BD", "VB", "VD", "LH"]
            lig_cima = ["FC", "BC", "BE", "BD", "VC", "VD", "LV"]
            lig_baixo = ["FB", "BB", "BE","BD", "VB", "VE", "LV"]

            if pipe not in lig_dir:
                if source=="D":
                    return False
            else:
                next_row, next_col = row, col + 1
                if dfs(next_row, next_col, source="E") == False:
                    return False

            if pipe not in lig_baixo:
                if source=="B":
                    return False
            else:
                next_row, next_col = row + 1, col
                if dfs(next_row, next_col, source="C") == False:
                    return False

            if pipe not in lig_esq:
                if source=="E":
                    return False
            else:
                next_row, next_col = row, col - 1
                if dfs(next_row, next_col, source="D") == False:
                    return False

            if pipe not in lig_cima:
                if source=="C":
                    return False
            else:
                next_row, next_col = row - 1, col
                if dfs(next_row, next_col, source="B") == False:
                    return False
            return True

        for row in range(state.board.nrows):
            for col in range(state.board.ncols):
                if (dfs(row, col) == False):
                    return False
        return True


    def h(self, node: Node):
            """Função heurística utilizada para a procura A*."""
            state = node.state
            # Pecas que faltam ir ao lugar
            misplaced_pieces = 0
            nrows = state.board.nrows
            ncols = state.board.ncols
            for row in range(nrows):
                for col in range(ncols):
                    current_pipe = state.board.get_value(row, col)
                    goal_pipe = self.goal.get_value(row, col)  # Corrigir esta linha
                    if current_pipe != goal_pipe:
                        misplaced_pieces += 1

            # mete um peso maior para os tubos bem conectados
            connected_pieces = 0
            for row in range(nrows):
                for col in range(ncols):
                    pipe = state.board.get_value(row, col)
                    above, below = state.board.adjacent_vertical_values(row, col)
                    left, right = state.board.adjacent_horizontal_values(row, col)
                    #ve se os tubos adjacentes estão conectadas corretamente
                    if above and above[1] in ['B', 'C'] and pipe[1] in ['F', 'H']:
                        connected_pieces += 1
                    if below and below[1] in ['F', 'H'] and pipe[1] in ['B', 'C']:
                        connected_pieces += 1
                    if left and left[1] in ['D', 'E'] and pipe[1] in ['C', 'H']:
                        connected_pieces += 1
                    if right and right[1] in ['C', 'H'] and pipe[1] in ['D', 'E']:
                        connected_pieces += 1

            #soma dos tubos fora do lugar e dos tubos bem conectados
            return misplaced_pieces + connected_pieces * 2


if __name__ == "__main__":

    board = Board.parse_instance()
    problem = PipeMania(board)
    initial_state = PipeManiaState(board)
    print("Is goal?", problem.goal_test(initial_state))
   
    '''
     # Ler grelha do figura 1a:
    board = Board.parse_instance()
    print(board.adjacent_vertical_values(0, 0))
    print(board.adjacent_horizontal_values(0, 0))
    print(board.adjacent_vertical_values(1, 1))
    print(board.adjacent_horizontal_values(1, 1))'''






    '''
     # Ler grelha do figura 1a:
    board = Board.parse_instance()
    # Criar uma instância de PipeMania:
    problem = PipeMania(board)
    # Criar um estado com a configuração inicial:
    initial_state = PipeManiaState(board)
    # Mostrar valor na posição (2, 2):
    print(initial_state.board.get_value(2, 2))
    # Realizar ação de rodar 90° clockwise a peça (2, 2)
    result_state = problem.result(initial_state, (2, 2, True))
    # Mostrar valor na posição (2, 2):
    print(result_state.board.get_value(2, 2))
'''




    '''# Ler grelha do figura 1a:
    board = Board.parse_instance()
    # Criar uma instância de PipeMania:
    problem = PipeMania(board)
    # Criar um estado com a configuração inicial:
    s0 = PipeManiaState(board)
    # Aplicar as ações que resolvem a instância
    s1 = problem.result(s0, (0, 1, True))
    s2 = problem.result(s1, (0, 1, True))
    s3 = problem.result(s2, (0, 2, True))
    s4 = problem.result(s3, (0, 2, True))
    s5 = problem.result(s4, (1, 0, True))
    s6 = problem.result(s5, (1, 1, True))
    s7 = problem.result(s6, (2, 0, False)) # anti-clockwise (exemplo de uso)
    s8 = problem.result(s7, (2, 0, False)) # anti-clockwise (exemplo de uso)
    s9 = problem.result(s8, (2, 1, True))
    s10 = problem.result(s9, (2, 1, True))
    s11 = problem.result(s10, (2, 2, True))
    # Verificar se foi atingida a solução
    print("Is goal?", problem.goal_test(s5))
    print("Is goal?", problem.goal_test(s11))
    print("Solution:\n", s11.board.print(), sep="")'''



    
    '''# Ler grelha do figura 1a:
    board = Board.parse_instance()
    # Criar uma instância de PipeMania:
    problem = PipeMania(board)
    # Obter o nó solução usando a procura em profundidade:
    goal_node = depth_first_tree_search(problem)
    # Verificar se foi atingida a solução
    print("Is goal?", problem.goal_test(goal_node.state))
    print("Solution:\n", goal_node.state.board.print(), sep="")'''


    '''board = Board.parse_instance()
    board.print()
    problem = PipeMania(board)
    initial_state = PipeManiaState(board)
    print(problem.actions(initial_state))'''




