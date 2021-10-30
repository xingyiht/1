from tkinter import*
def answer():   
    import os
    os.system('动态图.py')
    
root=Tk()
button=Button(root,text="你是靓仔吗",command=answer)
button.pack()
root.mainloop()
