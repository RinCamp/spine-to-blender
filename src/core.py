import bpy
from bpy.props import *
from bpy.types import PropertyGroup

# -----------
# Command
# -----------

SCRIPT_SCENE = "camp_scene_spine"
SCRIPT_OBJECT = "camp_object_spine"


class Camp_Scene(PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Scene.camp_scene_spine = PointerProperty(type=cls)


class Camp_Object(PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Object.camp_object_spine = PointerProperty(type=cls)


def get_context_scene_cmd():
    cmd = eval(f"bpy.context.scene.{SCRIPT_SCENE}")
    return cmd


def get_context_object_cmd(obj=None):
    cmd = None
    if obj:
        cmd = eval(f"obj.{SCRIPT_OBJECT}")
    else:
        cmd = eval(f"bpy.context.object.{SCRIPT_OBJECT}")
    return cmd


# -----------
# REGISTER
# -----------

classes = [
    Camp_Scene,
    Camp_Object,
]


def register():
    pass


def unregister():
    del bpy.types.Scene.camp_scene_spine
    del bpy.types.Object.camp_object_spine
