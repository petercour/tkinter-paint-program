#!/usr/bin/python3
from tkinter import *

class application(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()

    def createWidget(self):

        self.canvas = Canvas(
        self,width=200,height=200,bg='white')
        self.canvas.pack()
        self.canvas.bind('<Button-1>',self.mouseTest)
        self.canvas.bind('<B1-Motion>',self.test_drag)
        self.canvas.bind('<KeyPress>',self.keyboard_test)
        self.canvas.bind('<KeyPress-a>',self.press_a_test)
        self.canvas.bind('KeyRelease-a',self.release_a_test)

    def mouseTest(self,event):
        print('{0},{1}'.format(event.x,event.y))
        print('{0},{1}'.format(event.x_root,event.y_root))
        print('{0}'.format(event.widget))

    def test_drag(self,event):
        self.canvas.create_oval(event.x,event.y,event.x+10,event.y+10)

    def keyboard_test(self,event):
        print('keycode:{0},char:{1},keysym:{2}'.format(event.keycode,event.char,event.keysym))

    def press_a_test(self,event):
        print('press a')

    def release_a_test(self):
        print('release a')

if __name__ == '__main__':
    root = Tk()
    root.geometry('200x200')
    app=application(root)
    root.mainloop() 
