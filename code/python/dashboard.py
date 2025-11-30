import customtkinter as ctk
import sys
import os
import json
import subprocess

# --- CONNECT TO YOUR EXISTING BACKEND ---
# Add the templates folder to path so we can import param_manager
sys.path.append(os.path.join(os.path.dirname(__file__), '../templates'))
try:
    import param_manager
except ImportError:
    print("CRITICAL ERROR: Could not find param_manager.py")
    sys.exit(1)

# --- UI CONFIGURATION ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class CASuiteDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("CA Suite | Command Center")
        self.geometry("600x500")

        # --- LOAD DATA ---
        self.specs = param_manager.load_specs()

        # --- LAYOUT ---
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0) # Title
        self.grid_rowconfigure(1, weight=1) # Parameters
        self.grid_rowconfigure(2, weight=0) # Actions

        # 1. Header
        self.header = ctk.CTkLabel(self, text="CA SUITE PORTAL", font=("Roboto", 24, "bold"))
        self.header.grid(row=0, column=0, pady=20)

        # 2. Parameter Frame (The Inputs)
        self.param_frame = ctk.CTkScrollableFrame(self, label_text="Design Parameters")
        self.param_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.entries = {} # Store inputs to read later
        self.create_param_inputs()

        # 3. Action Frame (The Buttons)
        self.action_frame = ctk.CTkFrame(self)
        self.action_frame.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.btn_update = ctk.CTkButton(self.action_frame, text="UPDATE SYSTEM (GOD MODE)", 
                                        fg_color="green", height=40, command=self.update_system)
        self.btn_update.pack(side="left", expand=True, padx=10)

        self.btn_manim = ctk.CTkButton(self.action_frame, text="Render Animation", 
                                       fg_color="#D35400", command=self.run_manim)
        self.btn_manim.pack(side="left", expand=True, padx=10)

        self.status_label = ctk.CTkLabel(self, text="System Ready", text_color="gray")
        self.status_label.grid(row=3, column=0, pady=5)

    def create_param_inputs(self):
        """Dynamically creates input boxes based on JSON file."""
        row = 0
        for key, value in self.specs.items():
            if key == "project_name": continue # Skip non-numbers for now

            # Label
            lbl = ctk.CTkLabel(self.param_frame, text=key.replace("_", " ").title())
            lbl.grid(row=row, column=0, padx=10, pady=5, sticky="w")

            # Input Box
            entry = ctk.CTkEntry(self.param_frame, placeholder_text=str(value))
            entry.insert(0, str(value))
            entry.grid(row=row, column=1, padx=10, pady=5, sticky="e")
            
            self.entries[key] = entry
            row += 1

    def update_system(self):
        """Reads inputs and triggers the Manager."""
        self.status_label.configure(text="Updating...", text_color="yellow")
        self.update() # Force UI refresh

        changed_count = 0
        
        for key, entry in self.entries.items():
            new_val = entry.get()
            current_val = str(self.specs[key])
            
            # Only update if changed
            if new_val != current_val:
                try:
                    # Call your existing backend
                    param_manager.update_spec(key, new_val)
                    changed_count += 1
                except Exception as e:
                    print(f"Error updating {key}: {e}")

        # Reload data to ensure sync
        self.specs = param_manager.load_specs()
        
        if changed_count > 0:
            self.status_label.configure(text=f"SUCCESS: Updated {changed_count} parameters.", text_color="#00FF00")
        else:
            self.status_label.configure(text="No changes detected.", text_color="gray")

    def run_manim(self):
        """Launches the render process."""
        self.status_label.configure(text="Rendering Video...", text_color="orange")
        self.update()
        
        # Run the command we used in the terminal
        # Note: We assume we are in the root CA-Suite folder context
        subprocess.Popen(["manim", "-pql", "manim/scenes/parametric_box.py", "ParametricBox"], shell=True)
        self.status_label.configure(text="Render Launched in Background", text_color="white")

if __name__ == "__main__":
    # Ensure we run from the root directory context for paths to work
    # (Optional safety check)
    app = CASuiteDashboard()
    app.mainloop()