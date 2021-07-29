



class TextGame():
    '''level is the, um ,level! And the width and the height.....
        Creates a game using a gridlist! Yay...
        In progress.
        
        '''
    def __init__(self,level,width,height,player = '🔶',wall = '⬛', air = '⬜',goal = '🔷',box = '🔲'):
        
        self.level = level
        self.width = width
        self.height = height
        self.gridlist = []
        #ok so i have to find some way to flip the list over
        #self.gridlist.extend(self.level.split('\n'))
        #self.gridlist.pop(0)
        #self.gridlist.reverse()
        #self.gridlist.pop(0)
        #no it wont do
        self.player = player
        self.wall = wall
        self.air = air
        self.goal = goal
        self.box = box
        try:
            from IPython.display import clear_output
        except:
            pass

        
        
        
        '''
        self.gridlist = [val for val in level if val != '\n' and val != '']
        self.gridlist.reverse()
        self.i = 0
        while not self.gridlist[self.i] == self.player:
            self.i += 1
        
        self.x = self.i % self.width
        self.y = self.i // self.width
        '''
        self.gridlist = level.split('\n')
        self.gridlist.pop()
        self.gridlist.pop(0)
        self.gridlist.reverse()
        self.gridlist = list(''.join(self.gridlist))
        self.i = 0
        while not self.gridlist[self.i] == self.player:
            self.i += 1
        
        self.x = self.i % self.width
        self.y = self.i // self.width
        self.win = False
    def __str__(self):
        aba = self.gridlist.copy()
        listgroups = []
        for i in range(self.height):
            a = ''
            for i in range(self.width):
                a += aba.pop(0)
            listgroups.append(a)
        listgroups.reverse()
        x = ''
        for i in listgroups:
            x += i
            x += '\n'
        return x
        
    def update_idx(self):
        self.i = 0
        while not self.gridlist[self.i] == self.player:
            self.i += 1
        
        self.x = self.i % self.width
        self.y = self.i // self.width
        
    def __int__(self):
        return self.idx
    def block_at_xy(self,x,y):
        """DevTool. This is for finding a block at a desired position"""
        return self.gridlist[y * self.width + x]
    
    def move(self,x=0,y=0):
        '''Moves player in a certain direction. 
        x = x value added to position
        y = y value added to position
        
        '''
        
        
        
        
        try:
            if self.block_at_xy(self.x + x,self.y + y) == self.wall:
                print('Unable to move')#pass
                return
            elif self.block_at_xy(self.x + x,self.y + y) == self.box:
                if self.block_at_xy(self.x + (x * 2),self.y + (y * 2)) != self.air:
                    return
                #move box
                if y == 0:
                    self.gridlist[self.i + x], self.gridlist[self.i + (x * 2)] = self.gridlist[self.i+ (x * 2)], self.gridlist[self.i + x]
                    self.gridlist[self.i], self.gridlist[self.i + x] = self.gridlist[self.i + x], self.gridlist[self.i]
                    self.update_idx()
                else:
                    self.gridlist[self.i+(self.width * y)], self.gridlist[self.i+(self.width * y * 2)] = self.gridlist[self.i+(self.width * y * 2)], self.gridlist[self.i+(self.width * y)]
                    self.gridlist[self.i], self.gridlist[self.i+(self.width * y)] = self.gridlist[self.i+(self.width * y)], self.gridlist[self.i]
                    self.update_idx()
            elif self.block_at_xy(self.x + x,self.y + y) == self.goal :
                self.win == True
                print('You won')
                return
            else:
                print('Moved!')
                
                if y == 0:
                    self.gridlist[self.i], self.gridlist[self.i + x] = self.gridlist[self.i + x], self.gridlist[self.i]
                    self.update_idx()
                else:
                    self.gridlist[self.i], self.gridlist[self.i+(self.width * y)] = self.gridlist[self.i+(self.width * y)], self.gridlist[self.i]
                    self.update_idx()
        except:
            pass
                
                
                
        
    def left(self):
        self.move(x = -1)
    def right(self):
        self.move(x = 1)
    def up(self):
        self.move(y = 1)
    def down(self):
        self.move(y = -1)
    def fix_direction(self,key):
        '''Function to fix player movement. Use this as an input'''
        if key == 'a':
            self.left()
        elif key == 's':
            self.down()
        elif key == 'w':
            self.up()
        elif key == 'd':
            self.right()
    def clear_output(self):
        try:
            clear_output()
        except:
            print("\n" * 100)

#lvl = Game('''
#OOOOOOOO
#OAABAAAO
#OPBOAAGO
#OOOOOOOO
#''',8,4,wall = 'O',goal = 'G',player = 'P',box = 'B',air = 'A')
#while True:
#    lvl.clear_output()
#    print(lvl)
#    d = input()
#    if d == 'q':
#        break
#    lvl.fix_direction(d)


'''
Hello,User. If you see this you have managed to break into the files of 
this module.
'''
if __name__ == '__main__':
    lvl = Game('''
⬛⬛⬛⬛⬛⬛⬛
⬛⬜⬜⬜⬜🔷⬛
⬛⬜⬛⬜⬜⬜⬛
⬛⬜⬜⬛⬜🔲⬛
⬛⬛🔲🔲🔶⬜⬛
⬛⬜🔲⬜⬜⬜⬛
⬛⬛⬛⬛⬛⬛⬛
''',7,7)
