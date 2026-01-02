import tkinter as tk, random
root=tk.Tk(); root.title('Fault Detection')
lbl=tk.Label(root,font=('Arial',20)); lbl.pack(pady=30)
def update():
 f=random.choice([0,1])
 lbl.config(text='FAULT ❌' if f else 'NORMAL ✅', fg='red' if f else 'green')
 root.after(2000,update)
update(); root.mainloop()
