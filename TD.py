# -*- coding: utf-8 -*-
import sys
import os
import json
from PySide import QtGui,QtCore
from qss import uiQss
path = "%s/File"%os.path.dirname(__file__)
print path
Path = os.path.dirname(os.path.realpath("render.py"))
class Example(QtGui.QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.Init()
    def Init(self):
        self.setWindowTitle(u'跨部门动画预览工具')
        self.setGeometry(500,100,500,600)
        self.label_project = QtGui.QLabel(u'项目')
        self.ComboBox_project = QtGui.QComboBox()

        self.label_sequence = QtGui.QLabel(u'场')
        self.ComboBox_sequence = QtGui.QComboBox()

        self.label_shot = QtGui.QLabel(u'镜头')
        self.ComboBox_shot = QtGui.QComboBox()

        self.label_zichan = QtGui.QLabel(u'资产')
        self.label_animation = QtGui.QLabel(u'动画')
        self.ComboBox_animation = QtGui.QComboBox()

        self.label_comp = QtGui.QLabel(u'合成')
        self.ComboBox_comp = QtGui.QComboBox()

        self.label_FX = QtGui.QLabel(u'特效')
        self.ComboBox_FX = QtGui.QComboBox()

        self.label_light = QtGui.QLabel(u"灯光")
        self.ComboBox_light = QtGui.QComboBox()

        self.label_layout = QtGui.QLabel("layout")
        self.ComboBox_layout = QtGui.QComboBox()

        self.label_engine = QtGui.QLabel(u'渲染方式')
        self.ComboBox_engine = QtGui.QComboBox()
        self.ComboBox_engine.addItems(
            ["...Choose...", "micropoly", "raytrace", "pbrmicropoly", "pbrraytrace", "photon"])
        self.treeWidget = QtGui.QTreeWidget()
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setHeaderLabels(['Name', 'Material'])
        root = QtGui.QTreeWidgetItem(self.treeWidget)
        root.setText(0, 'root')
        child1 = QtGui.QTreeWidgetItem(root)
        child1.setText(0, 'figures')
        child1.setText(1, 'The skin')
        child2 = QtGui.QTreeWidgetItem(root)
        child2.setText(0, 'scenes')
        child2.setText(1, 'Rock')
        self.label_resultion = QtGui.QLabel(u"分辨率")
        self.resultion_edit = QtGui.QLineEdit()
        self.label_hight = QtGui.QLabel("  *   ")
        self.resultion_edit1 = QtGui.QLineEdit()

        self.label_start_frame = QtGui.QLabel(u"开始帧")
        self.start_frame_edit = QtGui.QLineEdit()

        self.label_end_frame = QtGui.QLabel(u"结束帧")
        self.end_frame_edit = QtGui.QLineEdit()

        self.label_save = QtGui.QLabel(u" 输出 ")
        self.save_edit = QtGui.QLineEdit()
        Button = QtGui.QPushButton(u"选择")
        Button.clicked.connect(self.save_Button)


        label_refreshButton = QtGui.QPushButton(u"刷新")
        label_refreshButton.clicked.connect(self.refreshButton)

        label_okButton = QtGui.QPushButton(u'渲染')
        label_okButton.setGeometry(QtCore.QRect(4, 18, 31, 2))
        label_okButton.clicked.connect(self.Render_Button)

        label_cancleButton = QtGui.QPushButton(u'取消')
        label_cancleButton.clicked.connect(self.Cancle_Button)

        self.baseLayout = QtGui.QGridLayout()

        self.baseLayout.addWidget(self.label_project, 0, 0)
        self.baseLayout.addWidget(self.ComboBox_project, 0, 1)

        self.baseLayout.addWidget(self.label_sequence, 0, 2)
        self.baseLayout.addWidget(self.ComboBox_sequence, 0, 3)

        self.baseLayout.addWidget(self.label_shot, 0, 4)
        self.baseLayout.addWidget(self.ComboBox_shot, 0, 5)

        self.baseLayout.addWidget(self.label_animation, 1, 0)
        self.baseLayout.addWidget(self.ComboBox_animation, 1, 1)

        self.baseLayout.addWidget(self.label_comp, 1, 2)
        self.baseLayout.addWidget(self.ComboBox_comp, 1, 3)

        self.baseLayout.addWidget(self.label_FX, 1, 4)
        self.baseLayout.addWidget(self.ComboBox_FX, 1, 5)

        self.baseLayout.addWidget(self.label_layout, 2, 0)
        self.baseLayout.addWidget(self.ComboBox_layout, 2, 1)

        self.baseLayout.addWidget(self.label_light, 2, 2)
        self.baseLayout.addWidget(self.ComboBox_light, 2, 3)

        self.baseLayout.addWidget(self.label_zichan, 3, 0)
        self.baseLayout_engine=QtGui.QHBoxLayout()

        self.baseLayout.addWidget(self.label_engine, 2, 4)
        self.baseLayout.addWidget(self.ComboBox_engine, 2, 5)
        self.baseLayout1 = QtGui.QHBoxLayout()
        self.baseLayout1.addWidget(self.treeWidget)
        self.baseLayout.addLayout(self.baseLayout1, 4, 0, 4, 6)

        self.baseLayout_resultion=QtGui.QHBoxLayout()
        self.baseLayout_resultion.addWidget(self.label_resultion)
        self.baseLayout_resultion.addWidget(self.resultion_edit)
        self.baseLayout_resultion.addWidget(self.label_hight)
        self.baseLayout_resultion.addWidget(self.resultion_edit1)
        self.baseLayout_frame=QtGui.QHBoxLayout()
        self.baseLayout_frame.addWidget(self.label_start_frame)
        self.baseLayout_frame.addWidget(self.start_frame_edit)
        self.baseLayout_frame.addWidget(self.label_end_frame)
        self.baseLayout_frame.addWidget(self.end_frame_edit)
        self.baseLayout.addLayout(self.baseLayout_resultion,8,0,8,6)
        self.baseLayout.addLayout(self.baseLayout_frame,11,0,11,6)
        self.baseLayout_save = QtGui.QHBoxLayout()
        self.baseLayout_save.addWidget(self.label_save)
        self.baseLayout_save.addWidget(self.save_edit)
        self.baseLayout_save.addWidget(Button)

        self.baseLayout.addLayout(self.baseLayout_save,14,0,14,6)

        self.baseLayout_PushButton=QtGui.QHBoxLayout()
        self.baseLayout_PushButton.addWidget(label_refreshButton)
        self.baseLayout_PushButton.addWidget(label_okButton)
        self.baseLayout_PushButton.addWidget(label_cancleButton)
        self.baseLayout.addLayout(self.baseLayout_PushButton,18,0,18,6)
        self.setLayout(self.baseLayout)

    def refreshButton(self):
        def gci(path):
            parents = os.listdir(path)
            return parents
        project_pos = gci(path)

        project_choose = ["...Choose..."]
        project_list = project_choose + project_pos
        self.ComboBox_project.addItems(project_list)
        self.ComboBox_project.currentIndexChanged.connect(self.sequence)
    def sequence(self):
        self.project_chose=self.ComboBox_project.currentText()
        self.path_sequence=path+"/"+self.project_chose
        def gci(path):
            parents = os.listdir(path)
            return parents
        sequence_pos = gci(self.path_sequence)
        sequence_choose = ["...Choose..."]
        sequence_list = sequence_choose + sequence_pos
        self.ComboBox_sequence.addItems(sequence_list)
        self.ComboBox_sequence.currentIndexChanged.connect(self.shot)

    def shot(self):
        self.sequence=self.ComboBox_sequence.currentText()
        self.path_shot=self.path_sequence+"/"+self.sequence
        def gci(path):
            parents = os.listdir(path)
            return parents
        shot_pos = gci(self.path_shot)
        shot_choose = ["...Choose..."]
        shot_list = shot_choose + shot_pos
        self.ComboBox_shot.addItems(shot_list)
        self.ComboBox_shot.currentIndexChanged.connect(self.list_animition)
        self.ComboBox_shot.currentIndexChanged.connect(self.list_comp)
        self.ComboBox_shot.currentIndexChanged.connect(self.list_FX)
        self.ComboBox_shot.currentIndexChanged.connect(self.list_layout)
        self.ComboBox_shot.currentIndexChanged.connect(self.list_light)

    def list_animition(self):
        self.animition=self.ComboBox_shot.currentText()
        self.path_animition=self.path_shot+"/"+self.animition
        def gci(path):
            parents = os.listdir(path)
            return parents
        self.list_pos = gci(self.path_animition)
        self.animition_pos=self.path_animition+"/"+self.list_pos[0]

        def gci(path):
            parents = os.listdir(path)
            return parents
        self.Animation_pos = gci(self.animition_pos)
        animation_choose = ["...Choose..."]
        filename_list=[]
        for parent, dirnames, filenames in os.walk(str(self.animition_pos)):
            for filename in filenames:
                filename_list.append(filename)

            for i in range(0,len(filename_list)):
                animation_choose.append("Animation_00"+str(i+1))
            self.ComboBox_animation.addItems(animation_choose)
            self.ComboBox_animation.currentIndexChanged.connect(self.animation)
    def animation(self):
        self.index=self.ComboBox_animation.currentIndex()
        self.animition = self.ComboBox_shot.currentText()
        self.path_animition = self.path_shot + "/" + self.animition
        def gci(path):
            parents = os.listdir(path)
            return parents
        self.list_pos = gci(self.path_animition)
        self.animition_pos = self.path_animition + "/" + self.list_pos[0]
        filename_list = []
        for parent, dirnames, filenames in os.walk(str(self.animition_pos)):
            for filename in filenames:
                filename_list.append(filename)
            Animation_file= filename_list[self.index-1]
            self.Path_pos_animation=self.animition_pos+"/"+Animation_file
        print self.Path_pos_animation
    def list_comp(self):
        self.comp_name=self.ComboBox_shot.currentText()
        self.path_comp=self.path_shot+"/"+self.comp_name
        def gci(path):
            parents = os.listdir(path)
            return parents
        self.list_pos = gci(self.path_comp)
        self.comp_pos=self.path_comp+"/"+self.list_pos[1]
        def gci(path):
            parents = os.listdir(path)
            return parents
        self.Comp_pos = gci(self.comp_pos)
        comp_choose = ["...Choose..."]
        filename_list=[]
        for parent, dirnames, filenames in os.walk(str(self.comp_pos)):
            for filename in filenames:
                filename_list.append(filename)

            for i in range(0,len(filename_list)):
                comp_choose.append("Comp_00"+str(i+1))
            self.ComboBox_comp.addItems(comp_choose)
            self.ComboBox_comp.currentIndexChanged.connect(self.comp)
    def comp(self):
        self.index = self.ComboBox_comp.currentIndex()
        self.comp_name = self.ComboBox_shot.currentText()
        self.path_comp = self.path_shot + "/" + self.comp_name

        def gci(path):
            parents = os.listdir(path)
            return parents

        self.list_pos = gci(self.path_comp)
        self.comp_pos = self.path_comp + "/" + self.list_pos[1]
        filename_list = []
        for parent, dirnames, filenames in os.walk(str(self.comp_pos)):
            for filename in filenames:
                filename_list.append(filename)
            Comp_file = filename_list[self.index - 1]
            self.Path_pos_comp = self.animition_pos + "/" + Comp_file
        print self.Path_pos_comp
    def list_FX(self):
        self.FX_name=self.ComboBox_shot.currentText()
        self.path_FX=self.path_shot+"/"+self.FX_name

        def gci(path):
            parents = os.listdir(path)
            return parents
        self.list_pos = gci(self.path_FX)
        self.fx_pos=self.path_FX+"/"+self.list_pos[2]
        def gci(path):
            parents = os.listdir(path)
            return parents
        self.FX_pos = gci(self.fx_pos)
        Fx_choose = ["...Choose..."]
        filename_list = []
        for parent, dirnames, filenames in os.walk(str(self.fx_pos)):
            for filename in filenames:
                filename_list.append(filename)
            for i in range(0, len(filename_list)):
                Fx_choose.append("Fx_00" + str(i + 1))
            self.ComboBox_FX.addItems(Fx_choose)
            self.ComboBox_FX.currentIndexChanged.connect(self.FX)
    def FX(self):
        self.index=self.ComboBox_FX.currentIndex()
        self.FX_name = self.ComboBox_shot.currentText()
        self.path_FX = self.path_shot + "/" + self.FX_name
        def gci(path):
            parents = os.listdir(path)
            return parents

        self.list_pos = gci(self.path_FX)
        self.comp_pos = self.path_FX + "/" + self.list_pos[2]
        filename_list = []
        for parent, dirnames, filenames in os.walk(str(self.fx_pos)):
            for filename in filenames:
                filename_list.append(filename)
            Fx_file = filename_list[self.index - 1]
            self.Path_pos_FX = self.comp_pos + "/" + Fx_file
            print self.Path_pos_FX
    def list_layout(self):
        self.layout_name=self.ComboBox_shot.currentText()
        self.path_layout=self.path_shot+"/"+self.layout_name

        def gci(path):
            parents = os.listdir(path)
            return parents
        self.list_pos = gci(self.path_layout)
        self.layout_pos=self.path_layout+"/"+self.list_pos[3]
        def gci(path):
            parents = os.listdir(path)
            return parents
        self.Layout_pos = gci(self.layout_pos)
        Layout_choose = ["...Choose..."]
        filename_list = []
        for parent, dirnames, filenames in os.walk(str(self.layout_pos)):
            for filename in filenames:
                filename_list.append(filename)

            for i in range(0, len(filename_list)):


                Layout_choose.append("Layout_00" + str(i + 1))
            self.ComboBox_layout.addItems(Layout_choose)
            self.ComboBox_layout.currentIndexChanged.connect(self.layout)
    def layout(self):
        self.index = self.ComboBox_layout.currentIndex()
        self.layout_name = self.ComboBox_shot.currentText()
        self.path_layout = self.path_shot + "/" + self.layout_name
        def gci(path):
            parents = os.listdir(path)
            return parents

        self.list_pos = gci(self.path_layout)
        self.layout_pos = self.path_layout + "/" + self.list_pos[3]
        filename_list = []
        for parent, dirnames, filenames in os.walk(str(self.layout_pos)):
            for filename in filenames:
                filename_list.append(filename)
            Layout_file = filename_list[self.index - 1]
            self.Path_pos_layout = self.layout_pos + "/" + Layout_file
            print self.Path_pos_layout
    def list_light(self):
        self.light_name=self.ComboBox_shot.currentText()
        self.path_light=self.path_shot+"/"+self.light_name

        def gci(path):
            parents = os.listdir(path)
            return parents
        self.list_pos = gci(self.path_light)
        self.light_pos=self.path_light+"/"+self.list_pos[4]
        def gci(path):
            parents = os.listdir(path)
            return parents
        self.Light_pos = gci(self.light_pos)
        Light_choose = ["...Choose..."]
        filename_list = []
        for parent, dirnames, filenames in os.walk(str(self.light_pos)):
            for filename in filenames:
                filename_list.append(filename)

            for i in range(0, len(filename_list)):


                Light_choose.append("Light_00" + str(i + 1))
            self.ComboBox_light.addItems(Light_choose)
            self.ComboBox_light.currentIndexChanged.connect(self.light)
    def light(self):
        self.index = self.ComboBox_light.currentIndex()
        self.light_name = self.ComboBox_shot.currentText()
        self.path_light = self.path_shot + "/" + self.light_name

        def gci(path):
            parents = os.listdir(path)
            return parents

        self.list_pos = gci(self.path_light)
        self.light_pos = self.path_light + "/" + self.list_pos[4]
        filename_list = []
        for parent, dirnames, filenames in os.walk(str(self.light_pos)):
            for filename in filenames:
                filename_list.append(filename)
            Light_file = filename_list[self.index - 1]
            self.Path_pos_light = self.light_pos + "/" + Light_file
            print self.Path_pos_light

    def save_Button(self):
        self.save_name=QtGui.QFileDialog.getSaveFileName(self)
        self.save_edit.setText(self.save_name)

    def Cancle_Button(self):
        self.close()
    def Render_Button(self):
        start_frame = self.start_frame_edit.text()
        end_frame = self.end_frame_edit.text()
        renderengine = self.ComboBox_engine.currentText()
        resultion_wight = self.resultion_edit.text()
        resultion_hight = self.resultion_edit1.text()
        save_pos=self.save_name

        if self.ComboBox_animation.currentText() == "...Choose...":
            self.Path_pos_animation = []
        if self.ComboBox_comp.currentText() == "...Choose...":
            self.Path_pos_comp = []
        if self.ComboBox_FX.currentText() == "...Choose...":
            self.Path_pos_FX = []
        if self.ComboBox_layout.currentText() == "...Choose...":
            self.Path_pos_layout = []
        if self.ComboBox_light.currentText() == "...Choose...":
            self.Path_pos_light = []
        dict_all = {"animation": str(self.Path_pos_animation), "comp": str(self.Path_pos_comp),
                    "FX": str(self.Path_pos_FX),
                    "layout":str(self.Path_pos_layout),"light":str(self.Path_pos_light),"renderengine":str(renderengine),
                    "camera_resultion_wight":str(resultion_wight), "camera_resultion_hight":str(resultion_hight),
                    "start_frame": str(start_frame), "end_frame": str(end_frame), "save_pos": (str(self.save_name)+".$F4.exr")}

        with open("dir.json", "w") as film:

            end = json.dumps(dict_all, indent=4)
            film.write(end)
        command = ("D:\\houdini16.0.722\\bin\\hython2.7.exe" + "  " + Path + "\\" + "render.py")
        # command = str("hython2.7") + "  " + Path + "\\" + "render.py"
        os.system(command)
if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    ex=Example()
    #ex.setStyleSheet(uiQss)
    ex.show()
    app.exec_()