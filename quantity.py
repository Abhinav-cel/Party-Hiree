MIN_QTY = 1
MAX_QTY = 500

def validate_quantity(quantity_input):
    """Enforces boundaries: whole numbers between 1 and 500 only."""
    try:
        # Convert input to string first to check for decimals safely
        input_str = str(quantity_input).strip()
        
        # Reject decimals straight away (like 1.5)
        if '.' in input_str:
            return False
            
        qty_num = int(input_str)
        
        # Enforce minimum and maximum range limits
        if qty_num < MIN_QTY or qty_num > MAX_QTY:
            return False
            
        return True
        
    except ValueError:
        # Catch text string inputs safely (like XLII)
        return False
    