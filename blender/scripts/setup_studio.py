import bpy
import math

def clean_scene():
    """Removes all objects from the scene to start fresh."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def setup_lighting():
    """Sets up a standard 3-point lighting for engineering products."""
    # Key Light
    bpy.ops.object.light_add(type='AREA', location=(5, -5, 10))
    key_light = bpy.context.object
    key_light.data.energy = 1000
    
    # Fill Light
    bpy.ops.object.light_add(type='AREA', location=(-5, -5, 5))
    fill_light = bpy.context.object
    fill_light.data.energy = 500
    
    # Rim Light (Back light)
    bpy.ops.object.light_add(type='SPOT', location=(0, 5, 8))
    rim_light = bpy.context.object
    rim_light.data.energy = 2000
    rim_light.rotation_euler = (math.radians(-45), 0, 0)

def setup_camera():
    """Places camera in an isometric-like view."""
    bpy.ops.object.camera_add(location=(7, -7, 5))
    cam = bpy.context.object
    # Point camera at origin (0,0,0) roughly
    cam.rotation_euler = (math.radians(60), 0, math.radians(45))
    bpy.context.scene.camera = cam

if __name__ == "__main__":
    clean_scene()
    setup_lighting()
    setup_camera()
    print("--- Studio Environment Setup Complete ---")