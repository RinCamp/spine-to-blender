# -----------
# CHECK
# -----------

classes = ["core"]
folders = ["spine_to_blender"]

# -----------
# CLASS
# -----------

if "bpy" in locals():
    import importlib

    for i in classes:
        importlib.reload(globals()[i])

    for i in folders:
        importlib.reload(globals()[i])
else:
    import bpy

    for i in classes:
        exec(f"from . import {i}")

    for i in folders:
        exec(f"from . import {i}")

# -----------
# REGISTER
# -----------


def register():
    for i in classes:
        if hasattr(globals()[i], "classes"):
            for c in globals()[i].classes:
                bpy.utils.register_class(c)
        if hasattr(globals()[i], "register"):
            globals()[i].register()

    for i in folders:
        if hasattr(globals()[i], "register"):
            globals()[i].register()


def unregister():
    for i in classes:
        if hasattr(globals()[i], "classes"):
            for c in globals()[i].classes:
                bpy.utils.unregister_class(c)
        if hasattr(globals()[i], "unregister"):
            globals()[i].unregister()

    for i in folders:
        if hasattr(globals()[i], "unregister"):
            globals()[i].unregister()
