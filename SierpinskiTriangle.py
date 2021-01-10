from tkinter import *

def display_triangle():
     ## clears the output frame in case there was already something there
     global output_frame
     output_frame.destroy()
     output_frame = Frame()
     output_frame.grid(row=4,columnspan=3)
     ## the sierpinski triangle of order n needs to be inscribed in a pascal's triangle of order 2^n, so the order of pascal's triangle is 2**order of sierpinski
     pascorder = 2**int(size.get())
     ## it gets too big after n = 5
     if int(size.get()) > 5:
          out_label.configure(text="Please choose a lower order (n < 6). "+size.get()+" is too computationally heavy.")
          return
     ## get the pascal triangle of order n
     triangle = [[1],[1,1]]
     while len(triangle) < pascorder:
          triangle.append([1] + [triangle[-1][i-1] + triangle[-1][i] for i in range(1,len(triangle[-1]))] + [1])
     ## populate a matrix such that it forms a square matrix (this helps with outputting)
     for k in triangle:
          i = 1
          while i < len(k):
               k.insert(i,0)
               i+=2
     triangle = [[0]*(pascorder-1-i) + triangle[i] + [0]*(pascorder-i-1) for i in range(pascorder)]
     ## this is just outputting the triangle
     out_label.configure(text="Order "+size.get()+" triangle:")
     output = [[0]*(2*pascorder-1) for i in range(pascorder)]
     for i in range(len(output)):
          for j in range(len(output[i])):
               output[i][j] = Label(output_frame,text=str(triangle[i][j]) if triangle[i][j]!=0 else "",bg=(root.cget("background") if triangle[i][j]%2==0 else "red"))
               output[i][j].grid(row=i+4,column=j,ipadx=5,ipady=5)

## initialize the frame and get the user input
root = Tk()
size_label = Label(text="Order of Sierpinski Triangle?", font=("Verdana",16))
size = Entry(font=("Verdana",16),width=5)
output_frame = Frame()
out_label = Label(font=("Verdana",16))
compute = Button(text="compute",font=("Verdana",16),command=display_triangle)

size_label.grid(row=0,column=0,columnspan=3)
size.grid(row=1,column=0,columnspan=3)
compute.grid(row=2,column=0,columnspan=3)
out_label.grid(row=3,column=0,columnspan=3)

mainloop()
