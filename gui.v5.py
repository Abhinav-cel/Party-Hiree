import tkinter as tk
from tkinter import ttk, messagebox
# Import your working boundary checker from quantity.py
from quantity import validate_quantity
# Import your help popup box from instructions.py
from instructions import show_help_guide

# --- GLOBAL DATA STRUCTURE ---
# Advanced 2D List tracking matrix to store live records dynamically
active_hires = []

# --- MULTI-COMPONENT CASCADING VALIDATION ENGINE ---
def validate_inputs_cascading(name, receipt, item, qty_str):
    """Cascading Validation Chain: Verifies every field step-by-step."""
    
    # 1. Check Customer Name
    if not name.strip():
        messagebox.showerror("Validation Error", "Please enter a customer name.")
        return False
        
    # 2. Check Receipt Number
    if not receipt.strip():
        messagebox.showerror("Validation Error", "Please enter a receipt number.")
        return False
        
    # 3. Check Item Name
    if not item.strip():
        messagebox.showerror("Validation Error", "Please enter the item name.")
        return False
        
    # 4. Check Quantity Input Presence
    if not qty_str.strip():
        messagebox.showerror("Validation Error", "Please enter a quantity.")
        return False
        
    # 5. Check Quantity Constraints (Runs your background 1-500 rules)
    if not validate_quantity(qty_str):
        messagebox.showerror("Validation Error", "Quantity must be a whole number between 1 and 500.")
        return False
        
    return True

def handle_submit():
    """Form submission loop triggered by the Submit Order button."""
    name = entry_name.get()
    receipt = entry_receipt.get()
    item = entry_item.get()
    qty_str = entry_qty.get()
    
    # Run the strict cascading validation waterfall check
    if not validate_inputs_cascading(name, receipt, item, qty_str):
        return # Stops immediately right where the error happened!
        
    # Append the row packet into our tracking database collection list
    hire_record = {
        "name": name.strip(),
        "receipt": receipt.strip(),
        "item": item.strip(),
        "quantity": int(qty_str)
    }
    active_hires.append(hire_record)
    
    # Refresh frontend display and reset input boxes
    refresh_table_display()
    clear_form_fields()
    messagebox.showinfo("Success", "Order Submitted Successfully!")

def handle_delete():
    """Removes a row record packet and archives it to an external text file."""
    del_idx_str = entry_delete.get().strip()
    try:
        idx = int(del_idx_str)
        if 0 <= idx < len(active_hires):
            # 1. Grab the specific target record before popping it out of memory
            archived_record = active_hires[idx]
            
            # 2. FILE ARCHIVING LOGIC (Addresses Requirement 1 & 2)
            # Opening with 'a' (Append mode) guarantees it adds to the end instead of wiping old data!
            with open("archive.txt", "a") as file:
                file.write(
                    f"Archived/Returned - Name: {archived_record['name']}, "
                    f"Receipt: {archived_record['receipt']}, "
                    f"Item: {archived_record['item']}, "
                    f"Qty: {archived_record['quantity']}\n"
                )
            
            # 3. Complete the standard list removal and visual refresh
            active_hires.pop(idx)
            refresh_table_display()
            entry_delete.delete(0, tk.END)
            messagebox.showinfo("Success", f"Row #{idx} removed and archived to text file successfully.")
        else:
            messagebox.showerror("Error", "Invalid Row Number. This row index does not exist.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid whole number for the row index.")

def refresh_table_display():
    """Wipes and updates the visible frontend spreadsheet data table rows."""
    for row in tree.get_children():
        tree.delete(row)
    
    # Auto-assign index values dynamically to each active hire packet
    for index, record in enumerate(active_hires):
        tree.insert("", tk.END, values=(index, record["name"], record["receipt"], record["item"], record["quantity"]))

def clear_form_fields():
    """Resets input entry fields clean for next submission cycle."""
    entry_name.delete(0, tk.END)
    entry_receipt.delete(0, tk.END)
    entry_item.delete(0, tk.END)
    entry_qty.delete(0, tk.END)

# --- REFINED INTERFACE DESIGN MATCHED TO BLUEPRINT ---
root = tk.Tk()
root.title("Hire Record Entry")
root.geometry("800x640") # Increased window height to safely anchor lower table components
root.configure(bg="#4ba3e3")
root.resizable(False, False)

lbl_font = ("Arial", 12, "bold")
fg_color = "#001F3F"

# Form Header Banner Section
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
btn_frame.pack(pady=15)

btn_submit = tk.Button(btn_frame, text="Submit\nOrder", command=handle_submit, bg="#FFCC00", fg="white", font=("Arial", 11, "bold"), bd=3, relief="solid", width=12, height=2)
btn_submit.pack(side="left", padx=20)

btn_cancel = tk.Button(btn_frame, text="Cancel", command=clear_form_fields, bg="#FFCC00", fg="white", font=("Arial", 11, "bold"), bd=3, relief="solid", width=12, height=2)
btn_cancel.pack(side="left", padx=20)

# Help Navigation Trigger Button Element
btn_help = tk.Button(root, text="❓ Help", command=show_help_guide, bg="#008CBA", fg="white", font=("Arial", 9, "bold"))
btn_help.place(x=710, y=15)

# Visual Table Treeview Database Grid Section
db_frame = tk.LabelFrame(root, text=" Live Order Database Matrix ", font=("Arial", 9, "bold"), bg="#4ba3e3")
db_frame.pack(fill="both", expand=True, padx=30, pady=5)

columns = ("row_num", "name", "receipt", "item", "qty")
tree = ttk.Treeview(db_frame, columns=columns, show="headings", height=4)
tree.heading("row_num", text="Row #")
tree.heading("name", text="Name")
tree.heading("receipt", text="Receipt #")
tree.heading("item", text="Item")
tree.heading("qty", text="Qty")

tree.column("row_num", width=60, anchor="center")
tree.column("name", width=190, anchor="w")
tree.column("receipt", width=110, anchor="center")
tree.column("item", width=190, anchor="w")
tree.column("qty", width=60, anchor="center")
tree.pack(fill="both", expand=True)

# Delete Footer Action Controller Return Frame
del_frame = tk.Frame(root, bg="#4ba3e3")
del_frame.pack(fill="x", padx=30, pady=15)
tk.Label(del_frame, text="Return Row #:", font=("Arial", 10, "bold"), bg="#4ba3e3").pack(side="left")
entry_delete = tk.Entry(del_frame, width=5, font=("Arial", 10, "bold"), bd=2, relief="solid")
entry_delete.pack(side="left", padx=5)
btn_del = tk.Button(del_frame, text="Delete", command=handle_delete, bg="#f44336", fg="white", font=("Arial", 9, "bold"))
btn_del.pack(side="left", padx=5)

if __name__ == "__main__":
    root.mainloop()