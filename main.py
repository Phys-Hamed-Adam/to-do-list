from tkinter import *  
from tkinter import  filedialog
from tkinter.font import Font
import pickle


root=Tk()
root.geometry("700x500")

my_font= Font(
    family="times new roman",
    size=25,
    weight="bold",
)

my_frame= Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(my_frame,
                 font=my_font,
                 width=25,
                 height=8,
                 bg="#3d3c3c",
                 bd=0,
                 fg="white",
                 highlightthickness=0,
                 selectbackground="#a6a6a6",
                 activestyle="none",
                 )


my_list.pack(side=LEFT, fill= BOTH)

dummylist=["Get it done "]


for i in dummylist:
    my_list.insert(END,i)
    
    
my_scrollbar= Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill= BOTH)

my_list.config(yscrollcommand=my_scrollbar)
my_scrollbar.config(command=my_list.yview)


my_item= Entry(root, font=("Arial",24))
my_item.pack(pady=20)

btn_frame= Frame(root)
btn_frame.pack(pady=20)

def delete_me():
    my_list.delete(ANCHOR)
    
    
def add_me():
    new_item=my_item.get()
    my_list.insert(END,new_item)
    
    my_item.delete(1, END)
    
def cross_me():
    
    #cross off the item
    my_list.itemconfig(
        my_list.curselection(),fg="#7a7878")
    
    #gets rid of selection
    my_list.selection_clear(0, END)
    
    
def uncross_me():   
        #cross off the item
    my_list.itemconfig(
        my_list.curselection(),fg="white")
    
    #gets rid of selection
    my_list.selection_clear(0, END)



def delete_crossed():
    
    count=0
    
    while count < my_list.size():
        if my_list.itemcget(count, "fg")=="#7a7878":
            my_list.delete(my_list.index(count))
        else:
            count+=1
    
            
def save_list():
    file_name= filedialog.asksaveasfilename(
        initialdir="/Users/knight/tk-todo_list",
        title="save File",
        filetypes=(("dat Files", "*.dat"), 
                   ("All Files", "*.*" )
                   ))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name =f'{file_name}.dat'
            
            
            
            count=0
    
    
    #deletes crossed off items before saving.
        while count < my_list.size():
            if my_list.itemcget(count, "fg")=="#7a7878":
                my_list.delete(my_list.index(count))
            else:
                count+=1
                
        # grab all the stuff from list
        stuff= my_list.get(0,END)
        
        #open the file 
        output_file = open(file_name, 'wb')
        
        #add stuff to file
        pickle.dump(stuff, output_file)

def clear_list():
    my_list.delete(0, END)

def open_list():
    file_name= filedialog.askopenfilename(
        initialdir="/Users/knight/tk-todo_list",
        title="open File",
        filetypes=(("dat Files", "*.dat"), 
                   ("All Files", "*.*" )
                   )
        )
    
    if file_name:
        #delete currently open list
        my_list.delete(0, END)
        
        # open the file
        input_filE= open(file_name, 'rb')
        
        # load the data from the file
        stuff = pickle.load(input_filE)
        
        #output stuff to the screen
        
        for item in stuff:
            my_list.insert(END,item)
            
            
my_menu = Menu(root)    
root.config(menu=my_menu)   


file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="file ", menu=file_menu)
 
#dropdown items

file_menu.add_command(label="save List", command= save_list)
file_menu.add_command(label="open List", command= open_list)
file_menu.add_separator()
file_menu.add_command(label="clear List", command= clear_list)          

delete_btn= Button(btn_frame, text="delete item", command= delete_me)
add_btn= Button(btn_frame, text="add item", command= add_me)
cross_me_btn= Button(btn_frame, text="cross itme", command=cross_me )
uncross_me_btn= Button(btn_frame, text="uncross item", command=uncross_me )
delete_crossed_btn= Button(btn_frame, text="delete_crossed", command=delete_crossed)

delete_btn.grid(row=0, column=0)
add_btn.grid(row=0, column=1, padx=20)
cross_me_btn.grid(row=0, column=2)
uncross_me_btn.grid(row=0, column=3, padx=20)
delete_crossed_btn.grid(row=0, column=4)

root.mainloop()
