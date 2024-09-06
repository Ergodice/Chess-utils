import chess
import chess.svg
import chess.pgn
import sys
import os

# https://python-chess.readthedocs.io/en/latest/svg.html#chess.svg.Arrow





"""
maybe
4rrk1/1bpR1p2/1pq1pQp1/p3P2p/P1PR3P/5N2/2P2PP1/6K1 w - - 0 1 https://lichess.org/@/jk_182/blog/identifying-brilliant-moves-with-leela-chess-zero/5px1F9wA


"""
boards = [


    {"name": "board0", "fen": "8/3qk3/1p6/1p2p1p1/pPp1PpPp/P1P2P1P/2P1K3/8 w - - 37 1", "arrows": [(chess.E2, chess.E1)]}, #95% 5 445 550

        {"name": "board1", "fen": "8/3qk3/1p6/1p2p1p1/pPp1PpPp/P1P2P1P/2P5/4K3 b - - 38 1", "arrows": [(chess.E7, chess.D6)]}, # 145 850 5    
                {"name": "board2","fen": "1r4k1/4rqpp/R4p2/1pb1p2P/3pP1Q1/1R1P2P1/1P1NKP2/8 b - - 0 1", "arrows": [(chess.B5, chess.B4)]}, # 47 446 507
                                {"name": "board3","fen": "1r4k1/4rqpp/R4p2/1pb1p2P/3pP1Q1/1R1P2P1/3NKP2/8 b - - 0 1", "arrows": [(chess.E7, chess.C7)]}, # 47 446 507
                                {"name": "board4","fen": "4rrk1/1bpR1p2/1pq1pQp1/p3P2p/P1PR3P/5N2/2P2PP1/6K1 w - - 0 1", "arrows": [(chess.G1, chess.H2), (chess.H2, chess.G3), (chess.G3, chess.F4), (chess.F4, chess.G5)]}, # 47 446 507



]

i = 0
for board_info in boards:
    fen = board_info.get("fen")
    arrows = [chess.svg.Arrow(*a, color="blue") for a in board_info.get("arrows")]

    board = chess.Board(fen)
    fig = chess.svg.board(board=board, arrows=arrows)

    os.makedirs("boards", exist_ok=True)

    with open(f"boards/board{i}.svg", "w") as f:    
        f.write(fig)
    
    i += 1