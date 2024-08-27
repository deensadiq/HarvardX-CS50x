from tkinter.dialog import askopenfilename
class Demo:
    def __init__(self, d):
        self.d = d
        
    def print(self):
        print(self.d)
        
a = Demo('Hello')
a.print()

s1 = set({1, 2, 3})
print(s1)

files = [('All Files', '*.*'), ('Python Files', '*.py'), ('Text Files', '*.txt')]

fileName = askopenfilename()