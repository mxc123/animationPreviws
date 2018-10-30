# *_*coding:utf-8 *_*
import hou
import json
with open("dir.json") as file:
    dict_all = json.loads(file.read())



obj=hou.node("/obj")
#创建摄像机并导入摄像机数据
camera_alembic=obj.createNode("alembicarchive")
file_name=camera_alembic.parm("fileName")
file_name.set(dict_all["layout"])
buildHierarchy=camera_alembic.parm("buildHierarchy")
buildHierarchy.pressButton()
hou.cd("/obj/alembicarchive1/camera1/")
cameraShape=hou.node("cameraShape1")
reslution= cameraShape.parmTuple("res")
reslution.set((int(dict_all["camera_resultion_wight"]),int(dict_all["camera_resultion_hight"])))
#创建geo节点
obj.createNode("geo")
hou.cd("/obj/geo1")
pwd=hou.pwd()
file1=hou.node("./file1")
file1.destroy()
alembic=pwd.createNode("alembic")
file_name=alembic.parm("fileName")
file_name.set(dict_all["animation"])
if dict_all["animation"]==[]:
    alembic.bypass(1)
else:
    pass
alembic_1=pwd.createNode("alembic")
file_name_1=alembic_1.parm("fileName")
file_name_1.set(dict_all["FX"])
if dict_all["FX"]==[]:
    alembic_1.bypass(1)
else:
    pass
merge=pwd.createNode("merge")
merge.setFirstInput(alembic)
merge.setNextInput(alembic_1)
merge.setDisplayFlag(True)
merge.setRenderFlag(True)
pwd.layoutChildren()

#创建灯光
hou.cd("/")
obj_light=hou.node("/obj")
hight_light=obj_light.createNode("hlight")
hlight_exposure=hight_light.parm("light_exposure")
hlight_exposure.set(10)

trans=hight_light.parmTuple("t")
trans.set((0.402509,27.178,17.0904))
rotate=hight_light.parmTuple("r")
rotate.set((-56.2252,-1.49007,-2.90487e-14))


hou.cd("/obj")
pwd=hou.pwd()
pwd.layoutChildren()
geo=hou.node("geo1")
v_blur=geo.parm("geo_velocityblur")
v_blur.setPending(1)
#创建渲染器
out=hou.node("/out")
mantra=out.createNode("ifd")
range=mantra.parm("trange")
range.setPending(1)
frame=mantra.parmTuple("f")
frame.deleteAllKeyframes()
frame.set((int(dict_all["start_frame"]),int(dict_all["end_frame"]),1))
camera_name=mantra.parm("camera")
camera_name.set("/obj/alembicarchive1/camera1/cameraShape1")
render_engine=mantra.parm("vm_renderengine")
render_engine.set(dict_all["renderengine"])
blur=mantra.parm("allowmotionblur")
blur.setPending(1)

picture=mantra.parm("vm_picture")
picture.set(dict_all["save_pos"])
mantra.render()



