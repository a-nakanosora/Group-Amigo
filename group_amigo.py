bl_info = {
    "name": "Group Amigo",
    "description": "Show active groups & quick select group objects",
    "author": "A Nakanosora",
    "version": (1, 0),
    "blender": (2, 76, 0),
    "location": "View 3D > Toolbar (T) > Relations",
    "warning": "",
    "category": "3D View"
    }

import bpy

class GroupAmigoPanel(bpy.types.Panel):
    bl_label = "Group Amigo"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Relations"
    bl_idname = 'groupamigo.mainpanel'

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)

        for group in context.object.users_group:
            op = col.operator(GroupAmigoOperator.bl_idname, text=group.name)
            op.groupname = group.name

        if not context.object.users_group:
            col.label("No groups")

class GroupAmigoOperator(bpy.types.Operator):
    bl_idname = 'groupamigo.buttonop'
    bl_label = 'TestOp'
    groupname = bpy.props.StringProperty(default = "")

    def execute(self, context):
        group_current = bpy.data.groups[self.groupname]
        for obj in group_current.objects:
            obj.select = True

        return {'FINISHED'}

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()