# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 00:53:20 2019

@author: koreto
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 19:09:09 2019

@author: koreto
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:55:32 2019

@author: koreto
"""

import tkinter as tk
import os
import sys

piece_count = 0

#各変数の定義
black = 1      #黒色
white = -1     #白色
empty = 0      #無し


#画像関係の設定
board_size = 800               #ボードの画像の大きさ
piece_size = 80                #駒の画像の大きさ
candidate_size = 20            #候補の画像の大きさ
board_center = board_size / 2  #ボードの中心
cell_size = 90                 #1つのマスの大きさ
cell_line = 3                  #マスを分けている線の太さ
origin = [29,30] #[x,y]        #一番左上のマスの左上の座標 (画像の左上の座標が(0,0)で、黒い線は含まない)

dirct = [-9,-8,-7,
         -1,    1, 
          7, 8, 9]

                                    
test = ["" for i in range(1000)]                                



class Frame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
#        self.pack()
        self.cvs = tk.Canvas(self, width=800, height=800)
        self.cvs.pack()
        self.board = self.cvs.create_image(board_size/2,
                                           board_size/2,
                                           image=board_img)
        
        
        Canvas.canvas = self.cvs
        for row in range(8):
            for column in range(8):
                Canvas(column, row)
                
        
#駒の画像
class Canvas:
    canvas = None
    def __init__(self, column, row):
        global piece_count
        piece_count+=1
        
        
        
        
#        self.candidate_set(0, 1) 
        self.set_empty(column, row)
        if piece_count == 64:
            global d_id
            d_id = self.cell_id - 63 #最大のときのタグから63を引いて誤差を算出
            
        
        
    def set_empty(self, column, row):
        self.cell_id = self.canvas.create_image(
                        origin[0] + cell_size/2 + column*(cell_size + cell_line),
                        origin[1] + cell_size/2 + row*(cell_size + cell_line),
                        image=empty_img)
        self.canvas.tag_bind(self.cell_id, "<1>", self.candidate_check)
#        
        
    def candidate_check(self, event):
        if len(board.candidate_data[self.cell_id - d_id]) > 0:
#            board.put_piece(self.cell_id - d_id)
            Game(self.cell_id - d_id)
        
#        if board_data[self.cell_id - d_id] == 2:
#        if board_data[20] == 2:
#            reverse(self.cell_id - d_id)
                                
class ReversiBoard(Canvas):
    def __init__(self):
        self.black_count = 0
        self.white_count = 0
        self.candiable = [True, None ,True] #左が白が返せるか、右が黒が返せるか
        self.turn = 1                                 # ターン数
        self.order = black                           # その番の色
        self.board_data = [0, 0, 0, 0, 0, 0, 0, 0,    # 盤の状態 ([row-1][column-1])
                           0, 0, 0, 0, 0, 0, 0, 0,    # ban_data[行][列]
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0,-1, 1, 0, 0, 0,
                           0, 0, 0, 1,-1, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0,]
#        self.board_data = [1, 1, 1, 1, 1, 1, 1, 1,    # 盤の状態 ([row-1][column-1])
#                           1, 1, 1,-1, 1, 1, 1, 1,    # ban_data[行][列]
#                           1, 1, 1, 1,-1, 1, 1, 1,
#                           1, 1, 1,-1, 1,-1, 1, 1,
#                           1, 1, 1, 1,-1,-1, 1, 1,
#                           1, 1, 1,-1, 1,-1, 1, 1,
#                           1, 1, 1, 1, 1, -1, 1, 1,
#                           1, 1, 1, 1, 1, 0, 0, 0]
        self.candidate_data = [[] for j in range(64)]
        self.candidate_count()
        for num in range(64):
            self.display(num)
            
    def display(self, num):
        if self.board_data[num] == black:
            self.canvas.itemconfigure(num + d_id,
                                              image=black_img,
                                              tags="piece")
        elif self.board_data[num] == white:
            self.canvas.itemconfigure(num + d_id,
                                              image=white_img,
                                              tags="piece")
        elif len(self.candidate_data[num]) > 0:
            self.canvas.itemconfigure(num + d_id,
                                              image=candidate_img,
                                              tags="candidate")
        
        
        
    def put_piece(self, num):
        self.board_data[num] = self.order
        self.display(num)
        
    
    def candidate_count(self):
        self.candiable[self.order + 1] = False
        for num in range(64):
            #すでに入力されている候補を削除
            if len(self.candidate_data[num]) > 0:
                self.candidate_data[num].clear()
            #numにコマが存在しなければ
            if self.board_data[num] == 0:
                #方向を回す
                for direction in dirct:
                    depth = 0
                   
                    old_CC = num #元の場所、最初はnum
                    escape = False
                    while(True):
                        depth += 1
                        CC = num + depth*direction #(checked_cell) 回す先の座標
                        if (old_CC  <  8 and direction == -9) or (old_CC  <  8 and direction == -8) or (old_CC  <  8 and direction == -7):
#                            print(str(old_CC) + "," + str(CC-old_CC))
                            break
                        if (old_CC  >  55 and direction == 9) or (old_CC  >  55 and direction == 8) or (old_CC  >  55 and direction == 7):
#                            print(str(old_CC) + "," + str(CC-old_CC))
                            break
                        if (old_CC%8 == 0 and direction == -9) or (old_CC%8 == 0 and direction == -1) or (old_CC%8 == 0 and direction == 7):
#                            print(str(old_CC) + "," + str(CC-old_CC))
                            break
                        if (old_CC%8 == 7 and direction == 9) or (old_CC%8 == 7 and direction == 1) or (old_CC%8 == 7 and direction == -7):
#                            print(str(old_CC) + "," + str(CC-old_CC))
                            break
                        
#                        if num < 70:
#                            break
                        if depth == 1:
                            if self.board_data[CC] == -self.order:
                                temp = [CC]
                            else:
                                escape = True
                        else:
                            if self.board_data[CC] == self.order:
                                self.candidate_data[num].extend(temp)
                                self.display(num)
                                self.candiable[self.order + 1] = True
                                break
                            if self.board_data[CC] == empty:
                                escape = True
                                break
                            temp.append(CC)  
                            
                        if escape == True:
                            break
                        #今のCCをold_CCにして続ける
                        old_CC = CC
        
    def change_turn(self):
        self.order = -self.order
        self.turn += 1
        self.canvas.itemconfigure("candidate",
                                  image=empty_img,
                                  tags="empty")

class Game(ReversiBoard):
    def __init__(self, num):
        self.result_flag = False
        board.put_piece(num)
        for reverse_cell in board.candidate_data[num]:
            board.board_data[reverse_cell] = board.order
            board.put_piece(reverse_cell)
        board.change_turn()
        board.candidate_count()
        if board.candiable[board.order + 1] == False:
            board.order = -board.order
            self.game_check()
            board.candidate_count()
            if board.candiable[board.order + 1] == False:
                self.result_flag = True
            else:
                self.pass_display()
        if self.result_flag == True:
            self.result()
                
                
    def pass_display(self):
        self.pass_window = tk.Toplevel()
        self.pass_window.title(u"パス")
        self.pass_window.geometry("150x50+400+400")
        self.pass_label = tk.Label(self.pass_window, text="パス! 打てるところがありません!")
        self.pass_button = tk.Button(self.pass_window, text = "ok", command=self.pass_window.destroy)
        self.pass_label.pack()
        self.pass_button.pack()
            
        
#        print(board.candidate_data)
        
    def game_check(self):
        if (board.candiable[0] == False and board.candiable[2] ==False) or board.turn == 61:
            board.game_quit = True
            self.result_flag = True
            
        
            
        
    
    def result(self):
        self.result_window = tk.Toplevel()
        self.result_window.title(u"結果画面")
        self.result_window.geometry("150x90+400+400")
        self.quit_button = tk.Button( self.result_window, text=u"終了する", command=root.destroy)
        
        self.replay_button = tk.Button( self.result_window, text=u"もう一度遊ぶ", command=self.replay)
        for result in board.board_data:
            if result == black:
                board.black_count += 1
            elif result == white:
                board.white_count += 1           
        if board.black_count > board.white_count:
            self.result_label = tk.Label(self.result_window, text="黒：" + str(board.black_count) + " 白：" + str(board.white_count)+"で黒の勝ち!")
        if board.black_count < board.white_count:
            self.result_label = tk.Label(self.result_window, text="黒：" + str(board.black_count) + " 白：" + str(board.white_count)+"で白の勝ち!")
        if board.black_count == board.white_count:
            self.result_lavbel = tk.Label(self.result_window, text="黒：" + str(board.black_count) + " 白：" + str(board.white_count)+"で引き分け!")
        self.result_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
        self.quit_button.grid(row=1, column=0, padx=5, pady=5)
        self.replay_button.grid(row=1, column=1, padx=5, pady=5)
    
    
    
    
    def replay(self):
        self.result_window.destroy()
        self.canvas.itemconfigure("candidate",
                                  image=empty_img,
                                  tags="empty") 
        self.canvas.itemconfigure("piece",
                                  image=empty_img,
                                  tags="empty")
        
        global board
        board=ReversiBoard()

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':
    root = tk.Tk()

    test_img = tk.PhotoImage(file = resource_path("test.png"))
    board_img = tk.PhotoImage(file = resource_path("board.png"))
    black_img = tk.PhotoImage(file = resource_path("black.png"))
    white_img = tk.PhotoImage(file = resource_path("white.png"))
    empty_img = tk.PhotoImage(file = resource_path("empty.png"))
    candidate_img = tk.PhotoImage(file = resource_path("candidate.png"))
    
    
    root.title(u"オセロ")
    root.geometry(str(board_size)+"x"+str(board_size)+"+100+100")
    frame = Frame()
    frame.pack()
    board = ReversiBoard()
    #print(board_data)
    root.mainloop()

"""
参考文献:
    pyrhon関係:
        https://docs.python.jp/3/tutorial/classes.html
        https://qiita.com/Usek/items/a206b8e49c02f756d636
        https://www.sejuku.net/blog/67215
        https://qiita.com/shiren/items/c89e002bc44343b387dc
    tkinter関係:
        http://www.shido.info/py/tkinter9.html
        http://www.shido.info/py/tkinter2.html
    オセロ関係:
        https://uguisu.skr.jp/othello/7gyou.html
        https://katoh4u.hatenablog.com/entry/2018/03/22/130105
"""