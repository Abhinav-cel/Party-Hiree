import tkinter as tk
from tkinter import ttk, messagebox
from quantity import validate_quantity
from instructions import show_help_guide

# --- GLOBAL DATA STRUCTURE ---
active_hires = []

# --- FUNCTIONS ---
def validate_blank_inputs(customer_name, item_description):
    if not customer_name.strip():
        messagebox.showerror("Validation Error", "Customer Name cannot be left completely blank.")
        return False
    if not item_description.strip():
        messagebox.showerror("Validation Error", "Item Description cannot be left completely blank.")
        return False
    return True

def handle_submit():
    name = entry_name.get()
    receipt = entry_receipt.get()
    item = entry_item.get()  # Pulls from plain entry block (No arrow dropdown)
    qty_str = entry_qty.get() # Pulls from plain entry block (No arrow spinbox)
    
    if not validate_blank_inputs(name, item):
        return
        
    # Standard backend logic still completely protects your 1-500 rules!
    if not validate_quantity(qty_str):
        messagebox.showerror("Validation Error", "Quantity must be a whole number between 1 and 500.")
        return
        
    active_hires.append({"name": name.strip(), "receipt": receipt.strip(), "item": item.strip(), "quantity": int(qty_str)})
    refresh_table_display()
    clear_form_fields()
    messagebox.showinfo("Success", "Order Submitted Successfully!")

def handle_delete():
    del_idx_str = entry_delete.get().strip()
    try:
        idx = int(del_idx_str)
        if 0 <= idx < len(active_hires):
            active_hires.pop(idx)
            refresh_table_display()
            entry_delete.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Invalid Row Number.")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid row index number.")

def refresh_table_display():
    for row in tree.get_children():
        tree.delete(row)
    for index, record in enumerate(active_hires):
        tree.insert("", tk.END, values=(index, record["name"], record["receipt"], record["item"], record["quantity"]))

def clear_form_fields():
    entry_name.delete(0, tk.END)
    entry_receipt.delete(0, tk.END)
    entry_item.delete(0, tk.END)
    entry_qty.delete(0, tk.END)

# --- REFINED INTERFACE DESIGN (NO ARROWS) ---
root = tk.Tk()
root.title("Hire Record Entry")
root.geometry("800x620")
root.configure(bg="#4ba3e3")

lbl_font = ("Arial", 12, "bold")
fg_color = "#001F3F"

# Form Header Banner
header_frame = tk.Frame(root, bg="#FFCC00", bd=3, relief="solid")
header_frame.pack(fill="x", padx=30, pady=15)
lbl_title = tk.Label(header_frame, text="Hire Record Entry", font=("Arial", 16, "bold"), bg="#FFCC00", fg="white")
lbl_title.pack(pady=8)

# Center Inputs Panel Box
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

# Item Hired Text Entry (Swapped to clear out arrow widgets)
tk.Label(input_frame, text="Item Hired:", font=lbl_font, bg="#4ba3e3", fg=fg_color).grid(row=2, column=0, sticky="e", pady=8, padx=10)
entry_item = tk.Entry(input_frame, font=("Arial", 12, "bold"), bd=3, relief="solid", width=22)
entry_item.grid(row=2, column=1, pady=8)

# Quantity Hired Text Entry (Swapped to clear out arrow widgets)
tk.Label(input_frame, text="Quantity Hired:", font=lbl_font, bg="#4ba3e3", fg=fg_color).grid(row=3, column=0, sticky="e", pady=8, padx=10)
entry_qty = tk.Entry(input_frame, font=("Arial", 12, "bold"), bd=3, relief="solid", width=22)
entry_qty.grid(row=3, column=1, pady=8)

# Action Buttons Dock Frame
btn_frame = tk.Frame(root, bg="#4ba3e3")
btn_frame.pack(pady=15)

btn_submit = tk.Button(btn_frame, text="Submit\nOrder", command=handle_submit, bg="#FFCC00", fg="white", font=("Arial", 11, "bold"), bd=3, relief="solid", width=12, height=2)
btn_submit.pack(side="left", padx=20)

btn_cancel = tk.Button(btn_frame, text="Cancel", command=clear_form_fields, bg="#FFCC00", fg="white", font=("Arial", 11, "bold"), bd=3, relief="solid", width=12, height=2)
btn_cancel.pack(side="left", padx=20)

# Help Navigation Trigger
btn_help = tk.Button(root, text="❓ Help", command=show_help_guide, bg="#008CBA", fg="white", font=("Arial", 9, "bold"))
btn_help.place(x=710, y=15)

# Visual Table Treeview Section Base
db_frame = tk.LabelFrame(root, text=" Live Order Database Matrix ", font=("Arial", 9, "bold"), bg="#4ba3e3")
db_frame.pack(fill="both", expand=True, padx=30, pady=10)

columns = ("row_num", "name", "receipt", "item", "qty")
tree = ttk.Treeview(db_frame, columns=columns, show="headings", height=4)
tree.heading("row_num", text="Row #")
tree.heading("name", text="Name")
tree.heading("receipt", text="Receipt #")
tree.heading("item", text="Item")
tree.heading("qty", text="Qty")
tree.column("row_num", width=50, anchor="center")
tree.column("qty", width=50, anchor="center")
tree.pack(fill="both", expand=True)

# Delete Footer Action Controller Frame
del_frame = tk.Frame(root, bg="#4ba3e3")
del_frame.pack(fill="x", padx=30, pady=10)
tk.Label(del_frame, text="Return Row #:", font=("Arial", 10, "bold"), bg="#4ba3e3").pack(side="left")
entry_delete = tk.Entry(del_frame, width=5, font=("Arial", 10, "bold"), bd=2, relief="solid")
entry_delete.pack(side="left", padx=5)
btn_del = tk.Button(del_frame, text="Delete", command=handle_delete, bg="#f44336", fg="white", font=("Arial", 9, "bold"))
btn_del.pack(side="left", padx=5)

if __name__ == "__main__":
    root.mainloop()