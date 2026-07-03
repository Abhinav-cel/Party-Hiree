from tkinter import messagebox

def show_help_guide():
    """Displays a clean user guide pop-up dialog box for Julie."""
    message = (
        "TO ADD A HIRE:\n"
        "• Name & Item: Required fields.\n"
        "• Quantity: Whole number 1 to 500.\n"
        "• Click 'Submit Hire Record'.\n\n"
        "TO RETURN AN ITEM:\n"
        "• Find the Row # in the table.\n"
        "• Type it in the delete box.\n"
        "• Click 'delete button'."
    )
    messagebox.showinfo("Quick User Guide", message)
