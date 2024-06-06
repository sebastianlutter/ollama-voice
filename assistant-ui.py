import tkinter as tk
from tkinter import scrolledtext, ttk

def update_conversation_box(message, sender="User"):
    """Update the conversation box with messages from the user or the LLM."""
    conversation_box.configure(state='normal')
    if sender == "User":
        conversation_box.insert(tk.END, f"User: {message}\n")
    else:
        conversation_box.insert(tk.END, f"LLM: {message}\n")
    conversation_box.see(tk.END)
    conversation_box.configure(state='disabled')

def send_text():
    """Handle the 'Send' button click."""
    user_input = user_input_field.get()
    update_conversation_box(user_input)
    user_input_field.delete(0, tk.END)
    print(user_input)  # Placeholder for processing user input

def speak_to_text():
    """Handle the 'Speak' button click."""
    # Placeholder function to simulate speech-to-text conversion
    update_conversation_box("Speech-to-text function called.", sender="System")

def quit_app():
    """Exit the application."""
    root.destroy()

def configure_style():
    """Configure the appearance of the GUI to match an Apple-like design."""
    style = ttk.Style()
    style.theme_use('clam')

    # Configure style for Entry
    style.configure('TEntry', foreground="#333333", font=('Helvetica', 12))

    # Configure style for Button
    style.configure('TButton', font=('Helvetica', 12), borderwidth=1)
    style.map('TButton',
              foreground=[('pressed', 'white'), ('active', 'white')],
              background=[('pressed', '!disabled', 'gray'), ('active', 'light gray')])

# Create the main window
root = tk.Tk()
root.title("Chat Interface")
root.geometry("400x600")
configure_style()

# Configure grid for dynamic resizing
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)

# Create a scrolled text area to display the conversation
conversation_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, width=50, state='disabled', borderwidth=1, relief="flat")
conversation_box.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)

# Create an input field for the user
user_input_field = ttk.Entry(root, width=48)
user_input_field.grid(row=1, column=0, padx=10, pady=0, sticky="ew")

# Create a 'Send' button
send_button = ttk.Button(root, text="Send", command=send_text)
send_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Create a 'Speak' button
speak_button = ttk.Button(root, text="Speak", command=speak_to_text)
speak_button.grid(row=2, column=0, columnspan=2, sticky="ew")

# Create an 'Exit' button
exit_button = ttk.Button(root, text="Exit", command=quit_app)
exit_button.grid(row=2, column=2, padx=10, pady=10, sticky="ew")

root.mainloop()
