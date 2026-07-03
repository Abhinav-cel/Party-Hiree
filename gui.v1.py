import tkinter as tk

# --- ITERATION 1: CORE FUNCTIONALITY LOGIC ---
def handle_alpha_submit():
    """Alpha Loop: Grabs raw text values and prints them directly to the console."""
    # Capture raw text string variables directly from the entry components
    name = entry_name.get()
    receipt = entry_receipt.get()
    item = entry_item.get()
    qty = entry_qty.get()
    
    # Simple terminal output stream to verify data mapping works behind the scenes
    print("\n--- [Iteration 1 Log] Form Submitted ---")
    print(f"Customer Name:     '{name}'")
    print(f"Receipt Number:    '{receipt}'")
    print(f"Item Description:  '{item}'")
    print(f"Quantity Hired:    '{qty}'")
    print("-----------------------------------------")

# --- ITERATION 1: INTERFACE INTERACTION LAYOUT ---
root = tk.Tk()
root.title("Julie's Party Hire")
root.geometry("400x300")

# Input Field Layout Fields
tk.Label(root, text="Customer Name:").pack(anchor="w", padx=20, pady=2)
entry_name = tk.Entry(root, width=40)
entry_name.pack(padx=20, pady=2)

tk.Label(root, text="Receipt Number:").pack(anchor="w", padx=20, pady=2)
entry_receipt = tk.Entry(root, width=40)
entry_receipt.pack(padx=20, pady=2)

tk.Label(root, text="Item Hired:").pack(anchor="w", padx=20, pady=2)
entry_item = tk.Entry(root, width=40)
entry_item.pack(padx=20, pady=2)

tk.Label(root, text="Quantity:").pack(anchor="w", padx=20, pady=2)
entry_qty = tk.Entry(root, width=40)
entry_qty.pack(padx=20, pady=2)

# Single Action Trigger Element
btn_submit = tk.Button(root, text="Submit Entry (Console Log)", command=handle_alpha_submit)
btn_submit.pack(pady=15)

if __name__ == "__main__":
    root.mainloop()