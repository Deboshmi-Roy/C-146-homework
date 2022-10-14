from tkinter import*

root=Tk()

root.title("Fibonacci")
root.geometry("400x400")

label_series=Label(root, text="Fibonacci Series:")
label_flower=Label(root)
label_spiral=Label(root)
label_total=Label(root,text= "total=")

def Fibonacci():
    num=10
    first_no=0
    second_no=1
    total=0
    sum=0
    counter=1
    while(counter<=num):
      label_series["text"]+=str(sum)+""
      counter=counter+1
      first_no=second_no
      second_no= sum
      sum=first_no+second_no
      total=total+sum
    label_flower['text']="flower is fully bloomed"
    label_total["text"]+=str(total)
    label_spiral["text"]="Spiral in right direction are" + str(first_no) + "and spirals in left direction are" + str(second_no) + "\n Total spiral are" + str(sum)
btn=Button(root,text="show Fibonacci Series",command=Fibonacci)
btn.pack()

label_series.pack()
label_flower.pack()
label_spiral.pack()
label_total.pack()
root.mainloop()