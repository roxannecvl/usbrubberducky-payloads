import tkinter as tk

class LockScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lock Screen")
        self.attributes('-fullscreen', True)
        
        # Load the background image
        self.background_image = tk.PhotoImage(file="skull.png")  # Replace with your image path
        self.canvas = tk.Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight())
        self.canvas.pack(fill="both", expand=True)
        
        # Center the background image
        self.canvas.create_image(self.winfo_screenwidth() // 2, self.winfo_screenheight() // 2, anchor="center", image=self.background_image)

        # Instruction label
        self.instruction_label = tk.Label(self, text="Password needed to gain access back", font=("Helvetica", 18), bg='black', fg='white')
        self.canvas.create_window(self.winfo_screenwidth() // 2, self.winfo_screenheight() // 2 - 50, window=self.instruction_label)
        
        # Password entry field with placeholder
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self, textvariable=self.password_var, show='*', font=("Helvetica", 24), bg='black', fg='grey')
        self.canvas.create_window(self.winfo_screenwidth() // 2, self.winfo_screenheight() // 2, window=self.password_entry)
        self.password_entry.focus_set()  # Automatically focus the password entry field
        
        # Bind the Return key to check password
        self.password_entry.bind('<Return>', self.check_password)
        
        # Capture all key and mouse events
        self.bind_all("<Key>", self.disable_event)
        self.bind_all("<Button-1>", self.disable_event)
   
    def check_password(self, event):
        password = self.password_var.get()
        if password == "test":  # Replace with your desired password
            self.destroy()  # Unlock the screen by destroying the window
        else:
            self.password_var.set("")  # Clear the password field if incorrect
            
    def disable_event(self, event):
        # Prevent all key and mouse events except for the password entry
        if event.widget != self.password_entry:
            return "break"

if __name__ == "__main__":
    lock_screen = LockScreen()
    lock_screen.mainloop()
