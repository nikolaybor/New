import tkinter as tk

window = tk.Tk()
window.geometry("800x600")
window.title("home/dashboard")
window.state("zoomed")

#window.config(bg= 'red')

#frame =tk.Frame(window,height=800,width=1600)
leftFrame = tk.Frame(window,bd=10,height=840,width=534,bg="blue")
middleFrame = tk.Frame(window,bd=10,height=840,width=534,bg="red")
rightFrame = tk.Frame(window,bd=10,height=840,width=534,bg="orange")

canvas = tk.Canvas(leftFrame, height = 534,width=0,bd=5,)
canvas.pack()
myCanvas = tk.Canvas(window, bg="white", height=300, width=300)



# coord = 10, 10, 300, 300
# arc = myCanvas.create_arc(coord, start=0, extent=150, fill="red")
# arv2 = myCanvas.create_arc(coord, start=150, extent=215, fill="green")

#myCanvas.pack(pady=100,padx=100)


leftFrame.grid(row=0,column=0)
middleFrame.grid(row=0,column=1)
rightFrame.grid(row=0,column=2)
#middleFrame.pack(side="top")
#rightFrame.pack(side="right")
window.mainloop()
