import tkinter as tk
from tkinter import messagebox
# Import your working boundary checker from quantity.py
from quantity import validate_quantity
# Import your help popup box from instructions.py
from instructions import show_help_guide

# --- GLOBAL DATA STRUCTURE ---
# Keeps your 2D list memory tracking active behind the scenes without rendering a table
active_hires = []

# --- MULTI-COMPONENT VALIDATION ENGINE ---
def validate_blank_inputs(customer_name, item_description):
    """Enforces non-empty string constraints to block blank submissions."""
    if not customer_name.strip():
        messagebox.showerror("Validation Error", "Customer Name cannot be left completely blank.")
        return False
    if not item_description.strip():
        messagebox.showerror("Validation Error", "Item Description cannot be left completely blank.")
        return False
    return True

def handle_submit():
    """Form submission loop linking all validation components together."""
    name = entry_name.get()
    receipt = entry_receipt.get()
    item = entry_item.get()
    qty_str = entry_qty.get()
    
    # 1. Component 3 Check: Prevent Blank Text Entries
    if not validate_blank_inputs(name, item):
        return
        
    # 2. Component 1 Check: Enforce Quantity Rules (1-500)
    if not validate_quantity(qty_str):
        messagebox.showerror("Validation Error", "Quantity must be a whole number between 1 and 500.")
        return
        
    # 3. Component 2 Check: Save to 2D List Database Matrix background array
    hire_record = {
        "name": name.strip(),
        "receipt": receipt.strip(),
        "item": item.strip(),
        "quantity": int(qty_str)
    }
    active_hires.append(hire_record)
    
    # Debug confirmation log printed to terminal workspace
    print(f"📦 Backend Database Log - Current Records Saved: {len(active_hires)}")
    
    # Reset fields and notify user
    clear_form_fields()
    messagebox.showinfo("Success", "Order Submitted Successfully!")

def clear_form_fields():
    """Resets input entry fields clean for next submission cycle."""
    entry_name.delete(0, tk.END)
    entry_receipt.delete(0, tk.END)
    entry_item.delete(0, tk.END)
    entry_qty.delete(0, tk.END)

# --- REFINED INTERFACE DESIGN MATCED TO BLUEPRINT ---
root = tk.Tk()
root.title("Hire Record Entry")
root.geometry("800x420") # Reduced window height since the lower table layout is removed
root.configure(bg="#4ba3e3")
root.resizable(False, False)

lbl_font = ("Arial", 12, "bold")
fg_color = "#001F3F"

# Form Header Banner
header_frame = tk.Frame(root, bg="#FFCC00", bd=3, relief="solid")
header_frame.pack(fill="x", padx=30, pady=15)
lbl_title = tk.Label(header_frame, text="Hire Record Entry", font=("Arial", 16, "bold"), bg="#FFCC00", fg="white")
lbl_title.pack(pady=8)

# Center Inputs Panel Box Layout
input_frame = tk.Frame(root, bg="#4ba3e3")
input_frame.pack(pady=10)

# Customer Name Input Block
tk.Label(input_frame, text="Customer's Full Name:", font=lbl_font, bg="#4ba3e3", fg=fg_color).grid(row=0, column=0, sticky="e", pady=8, padx=10)
entry_name = tk.Entry(input_frame, font=("Arial", 12, "bold"), bd=3, relief="solid", width=22)
entry_name.grid(row=0, column=1, pady=8)

# Receipt Input Block
tk.Label(input_frame, text="Receipt Number:", font=lbl_font, bg="#4ba3e3", fg=fg_color).grid(row=1, column=0, sticky="e", pady=8, padx=10)
entry_receipt = tk.Entry(input_frame, font=("Arial", 12, "bold"), bd=3, relief="solid", width=22)
entry_receipt.grid(row=1, column=1, pady=8)

# Item Hired Text Input Block
tk.Label(input_frame, text="Item Hired:", font=lbl_font, bg="#4ba3e3", fg=fg_color).grid(row=2, column=0, sticky="e", pady=8, padx=10)
entry_item = tk.Entry(input_frame, font=("Arial", 12, "bold"), bd=3, relief="solid", width=22)
entry_item.grid(row=2, column=1, pady=8)

# Quantity Hired Text Input Block
tk.Label(input_frame, text="Quantity Hired:", font=lbl_font, bg="#4ba3e3", fg=fg_color).grid(row=3, column=0, sticky="e", pady=8, padx=10)
entry_qty = tk.Entry(input_frame, font=("Arial", 12, "bold"), bd=3, relief="solid", width=22)
entry_qty.grid(row=3, column=1, pady=8)

# Action Buttons Dock Frame
btn_frame = tk.Frame(root, bg="#4ba3e3")
btn_frame.pack(pady=20)

btn_submit = tk.Button(btn_frame, text="Submit\nOrder", command=handle_submit, bg="#FFCC00", fg="white", font=("Arial", 11, "bold"), bd=3, relief="solid", width=12, height=2)
btn_submit.pack(side="left", padx=20)

btn_cancel = tk.Button(btn_frame, text="Cancel", command=clear_form_fields, bg="#FFCC00", fg="white", font=("Arial", 11, "bold"), bd=3, relief="solid", width=12, height=2)
btn_cancel.pack(side="left", padx=20)

# Help Navigation Trigger Button Element
btn_help = tk.Button(root, text="❓ Help", command=show_help_guide, bg="#008CBA", fg="white", font=("Arial", 9, "bold"))
btn_help.place(x=710, y=15)

if __name__ == "__main__":
    root.mainloop()