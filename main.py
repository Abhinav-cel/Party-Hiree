
MIN_QTY = 1
MAX_QTY = 500   
# --- GLOBAL DATABASE STORAGE ---
# Advanced 2D List structure to track all dynamic hire records
active_hires = []


def track_new_hire(customer_name, receipt_number, item_name, hire_quantity):
    """Appends a structured record row into the global 2D data storage array."""
    # Group the separate inputs into a single row dictionary entry packet
    hire_record = {
        "name": customer_name.strip(),
        "receipt": receipt_number.strip(),
        "item": item_name.strip(),
        "quantity": int(hire_quantity)
    }
    
    # Append the row into our tracking database collection list
    active_hires.append(hire_record)
    print(" Data Row successfully saved to memory!")
    return True


def display_current_database():
    """Prints out the current active memory collection in a simulated console table."""
    print("\n================== ACTIVE HIRE DATABASE CONSOLE ==================")
    print(f"{'Row #':<8}{'Customer Name':<20}{'Receipt #':<12}{'Item Hired':<20}{'Qty':<6}")
    print("-" * 66)
    
    # Enumerate automatically generates our Row Index numbers (0, 1, 2...)
    for index, record in enumerate(active_hires):
        print(f"{index:<8}{record['name']:<20}{record['receipt']:<12}{record['item']:<20}{record['quantity']:<6}")
    print("==================================================================\n")


# --- ISOLATED TERMINAL VERIFICATION LOOP ---
if __name__ == "__main__":
    print("--- Testing 2D List Data Tracking Array ---")
    
    # Simulate adding Entry Row 0
    track_new_hire("Aroha Smith", "HRE-101", "Studio Tripod", "15")
    # Simulate adding Entry Row 1
    track_new_hire("John Doe", "HRE-102", "Lighting Rig Set", "5")
    
    # Print out the console grid to verify indexing
    display_current_database()
    