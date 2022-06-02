from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk

root=Tk()
root.title("juice center")
root.geometry("800x600")
root.config(bg="orange2")

lbl_head=Label(root,text="juice center",font=("Bahnschrift Light",12),bg="orange")
lbl_head.place(relx=0.05,rely=0.1,anchor=W)

image_juice=ImageTk.PhotoImage(Image.open("logo.png"))

lbl_image_juice=Label(root,image=image_juice,bg="orange")
lbl_image_juice.place(relx=0.2,rely=0.4,anchor=CENTER)

lbl_select_frt=Label(root,text="select fruit",font=("Bahnschrift Light",12),bg="orange")
lbl_select_frt.place(relx=0.96,rely=0.2,anchor=E)

fruit_name=["apple","orange","mango"]
fruit_drop=ttk.Combobox(root,state="readonly",value=fruit_name,justify="right")
fruit_drop.place(relx=0.95,rely=0.25,anchor=E)

lbl_quantity=Label(root,text="Enter quantity",font=("Bahnschrift Light",12),bg="orange")
lbl_quantity.place(relx=0.96,rely=0.35,anchor=E)

input_quantity=Entry(root)
input_quantity.place(relx=0.96,rely=0.45,anchor=E)

lbl_show_amt=Label(root,bg="orange")
lbl_show_amt.place(relx=0.96,rely=0.7,anchor=E)

lbl_show_quantity=Label(root,bg="orange")
lbl_show_quantity.place(relx=0.96,rely=0.8,anchor=E)

image_apple=ImageTk.PhotoImage(Image.open("apple_img.png"))

image_orange=ImageTk.PhotoImage(Image.open("orange.png"))

image_mango=ImageTk.PhotoImage(Image.open("mango_img.png"))



fruit_image=Label(root,bg="orange")
fruit_image.place(relx=0.75,rely=0.8,anchor=CENTER)




class juice():
    def __init__(self,fruit_name,quantity):
        self.fruit=fruit_name
        self.qty=int(quantity)
        self.__cost=250
        
    def __calculatecost(self):
        total_cost=self.qty*self.__cost
        
        lbl_show_amt["text"]="you have to pay "+str(total_cost)+"USD"
        if(self.fruit=="orange"):
            calorie=47*self.qty
            fruit_image["image"]=image_orange
            
        elif(self.fruit=="mango"):
            calorie=60*self.qty
            fruit_image["image"]=image_mango
        elif(self.fruit=="apple"):
            calorie=52*self.qty
            fruit_image["image"]=image_apple
        lbl_show_quantity["text"]="x"+str(self.qty)+"="+str(calorie)+"calories"
        
        
    def getcost(self):
        self.__calculatecost()
        
        

def orderjuice():
    fruit=fruit_drop.get()
    quantity=input_quantity.get()
    obj1=juice(fruit,quantity)
    obj1.getcost()
    
    
    

btn_fruit_total=Button(root,text="Total",command=orderjuice,bg="red",fg="white",padx=10,pady=1,font=("Arial",10,"bold"),relief=FLAT)
btn_fruit_total.place(relx=0.95,rely=0.5,anchor=E)
    

root.mainloop()