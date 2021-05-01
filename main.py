#Oscar Barbosa Aquino
#23/08/2019

import random
import sys

class Node:
    def __init__(self,data,level):
        self.data = data
        self.level = level

    def generate_children(self):
        if self.level == 1:
            return []
        if self.level == 2:
            return [ Node(1,self.level-1) ]
        if self.level == 3:
            return [ Node(0,self.level-1), Node(1,self.level-2) ]
        else:
            return [ Node(0,self.level-1), Node(0,self.level-2) ]
                
    def __str__(self):
        return f'Node(level={self.level})'

class Puzzle:
        
    def __init__(self,size, turn, debug):
        self.size = size
        self.turn = turn%2 # 0 for player, 1 for pc
        self.debug = debug
        self.children_ignored = 0
        self.puzzle = self.create_puzzle(size)

    def h(self,node):
        return node.level

    def create_puzzle(self,size):
        puzzle = []
        for i in range(size):
            puzzle.append(0)
        puzzle[-1] = 1
        return puzzle

    def pop(self,n):
        for i in range(n):
            if self.puzzle != []:
                self.puzzle.pop(0)
                self.size -= 1
    
    def minimax(self, node, depth, alpha, beta, maximizing):
        if depth == 0 or node.level == 1 or node.level == 2 or node.level == 3:
            return [self.h(node),node]
        i=0
        children = node.generate_children()
        if maximizing:
            max_eval = [-sys.maxsize-1,node]
            for child in children:
                i+=1
                evaluation = self.minimax(child, depth-1, alpha, beta, False)
                max_eval = max(evaluation, max_eval, key=lambda e: e[0])
                alpha = max(alpha, evaluation[0])
                if beta <= alpha:
                    self.children_ignored+=len(children)-i
                    break
            return max_eval
        else:
            min_eval = [sys.maxsize,node]
            for child in children:
                i+=1
                evaluation = self.minimax(child, depth-1, alpha, beta, True)
                min_eval = min(evaluation, min_eval, key=lambda e: e[0])
                beta = min(beta, evaluation[0])
                if beta <= alpha:
                    self.children_ignored+=len(children)-i
                    break
            return min_eval

    def calculate_move(self, depth):
        node = Node(self.puzzle[0], self.size)
        
        alpha = -sys.maxsize-1
        beta = sys.maxsize

        min_eval = [beta, None]
        good_kid = None

        for child in node.generate_children():
            evaluation = self.minimax(child,depth,alpha,beta,False)
            if evaluation[0] < min_eval[0]: good_kid = child
            min_eval = min(evaluation,min_eval,key=lambda e: e[0])

        if good_kid:
            return node.level - good_kid.level
        else:
            return 1

    def player_move(self):
        n = int(input())
        while n<1 or n>2:
            self.print_invalid()
            n = int(input())
        return n

    def process(self, players, depth):
        n = 0
        while self.puzzle != []:
            self.print_player()
            self.print_puzzle()
            if self.turn == 1:
                self.turn = 0
                if players == 1 or players == 2:
                    n = self.player_move()
                if players == 0:
                    n = self.calculate_move(depth)
            else:
                self.turn = 1
                if players == 2:
                    n = self.player_move()
                if players == 1 or players == 0:
                    n = self.calculate_move(depth)
            self.pop(n)
        
        if self.debug==True:
            print(f"root children ignored = {self.children_ignored}")
        
        if self.turn == 1:
            if self.puzzle == []:
                return "Player 1 wins!"
            else:
                return "Player 2 wins!"
        else:
            if self.puzzle == []:
                return "Player 2 wins!"
            else:
                return "Player 1 wins!"

    def print_puzzle(self):
        if self.debug==True:
            print("|", end="")
            for e in self.puzzle:
                if e == 0:
                    print("O|",end="")
                else:
                    print("X|",end="")
            print()
    
    def print_player(self):
        if self.debug==True:
            if self.turn == 1:
                print("Player 1, pick 1 or 2")
            else:
                print("Player 2, pick 1 or 2")

    def print_invalid(self):
        if self.debug==True:
            print("Invalid, please select 1 or 2")

def main():
    size = int(input())
    turn = int(input())
    puz = Puzzle(size,turn,debug=False)
    print(puz.process(0,10))

def main2(size, turn, depth, players, debug):
    if debug == "True":
        puz = Puzzle(size,turn,True)
    else:
        puz = Puzzle(size,turn,False)
    print(puz.process(players,depth))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else: 
        if len(sys.argv) == 6:
            main2(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),sys.argv[5])
        else:
            print("Not enough arguments --size --turn --depth --players --debug")