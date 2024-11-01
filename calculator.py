import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("เครื่องคิดเลข")
        self.window.geometry("300x400")
        
        # สร้างช่องแสดงผล
        self.display = tk.Entry(self.window, width=20, font=('Arial', 20), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # ปุ่มตัวเลขและเครื่องหมาย
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # สร้างปุ่มกด
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(self.window, text=button, width=5, height=2, command=cmd).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1
                
        # ปุ่มล้างข้อมูล (Clear)
        tk.Button(self.window, text='C', width=5, height=2, command=self.clear).grid(row=5, column=0)
        
    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, key)
            
    def clear(self):
        self.display.delete(0, tk.END)
        
    def run(self):
        self.window.mainloop()

# สร้างและรันโปรแกรม
calc = Calculator()
calc.run()
