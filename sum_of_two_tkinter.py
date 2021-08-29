import tkinter as tk
def add():
    #fetch data from entry 
    try:
        result = eval(entry_one.get())+eval(entry_two.get())
    except Exception as e:
        result = "You need to enter only numbers"
    # print(result)
    label_result.config(text=result)

root=tk.Tk()
root.title('Sum of two numbers')
root.minsize(800,500)
label_num_one = tk.Label(root,text="Number One")
label_num_two = tk.Label(root,text="Number Two")
label_result = tk.Label(root,text="")

entry_one = tk.Entry(root)
entry_two = tk.Entry(root)
submit_button = tk.Button(root, bg="red",fg="white",text="Submit")


label_num_one.grid(row=0,column=0)
label_num_two.grid(row=1,column=0)
entry_one.grid(row=0,column=1)
entry_two.grid(row=1,column=1)
submit_button.grid(row=2,column=1)
label_result.grid(row=3,column=0)

submit_button.config(command=add)

root.mainloop()

