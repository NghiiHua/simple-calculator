import tkinter as tk

root = tk.Tk()
root.title("GUI Calculator")
root.geometry("200x250")

string = "" # to use eval function
def nums(i):
    global string
    tk.Label(root, text=str(i) + "     ").grid(column=0, row=0) # display numbers/ops selected
    string += str(i)
    if "C" in string:
        string = ""
        tk.Label(root, text="C      ").grid(column=0, row=0)
    elif string[-1] == "=":
        tk.Label(root, text="      ").grid(column=0, row=0)
        string = string[:-1]
        string = str(eval(string))
        tk.Label(root, text=" " + string[0:5] + " ").grid(column=0, row=0)
        string = ""

rownum = 0
columnnum = 0
count = 0
for i in range(1, 10):
    if count % 3 == 0:
        rownum += 1
        columnnum = 0
    tk.Button(root, text=str(i), height=2, command=lambda i=i: nums(i)).grid(row=rownum, column=columnnum, sticky="nesw")
    columnnum += 1
    count += 1

# add operations buttons
operations = {"+", "-", "*", "/"}
rownum = 1
count = 0
for i in operations:
    tk.Button(root, text=i, height=2, command=lambda i=i: nums(i)).grid(row=rownum, column=4, sticky="nesw")
    rownum += 1

# add "0, =, C, ."
tk.Button(root, text="0", height=2, command=lambda: nums("0")).grid(row=4, column=0, sticky="nesw")
tk.Button(root, text="=", height=2, command=lambda: nums("=")).grid(row=4, column=1, sticky="nesw")
tk.Button(root, text="C", height=2, command=lambda: nums("C")).grid(row=4, column=2, sticky="nesw")
tk.Button(root, text=".", height=2, command=lambda: nums(".")).grid(row=5, column=0, sticky="nesw")

root.mainloop()