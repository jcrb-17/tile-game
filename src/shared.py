#!/usr/bin/env python
# -*- coding: utf-8 -*-

def findInBoard(board,id1):
    """
    board = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    """

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == id1:
                return True,i,j
    return False,-1,-1


