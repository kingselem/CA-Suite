import adsk.core, adsk.fusion, traceback
import json
import os

# INSTRUCTIONS:
# 1. Copy this script content.
# 2. In Fusion 360, press Shift+S (Scripts).
# 3. Create a new script, paste this code, and run.

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        
        # --- PATH TO YOUR BRAIN ---
        # You must update this path to match your actual folder!
        json_path = r"C:\CA-Suite-Project\CA-Suite\config\design_specs.json"
        
        if not os.path.exists(json_path):
            ui.messageBox(f"Could not find config at: {json_path}")
            return

        with open(json_path, 'r') as f:
            specs = json.load(f)
            
        # Update Fusion User Parameters
        userParams = design.userParameters
        
        def set_param(name, val, unit="mm"):
            param = userParams.itemByName(name)
            expression = str(val) + " " + unit
            if param:
                param.expression = expression
            else:
                userParams.add(name, adsk.core.ValueInput.createByString(expression), unit, "")
                
        # Update the parameters defined in JSON
        set_param("SideLength", specs["side_length"])
        set_param("HoleDia", specs["hole_diameter"])
        
        ui.messageBox("Success! Parameters updated from JSON.")
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
