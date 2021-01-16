import bpy
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete(use_global=False)


for x in range(10):
    for y in range(10):
        for z in range(10):
            bpy.ops.mesh.primitive_cube_add(location=(x*4,y*4,z*4))
