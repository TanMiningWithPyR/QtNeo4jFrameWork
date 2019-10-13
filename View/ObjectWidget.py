# -*- coding: utf-8 -*-
"""
Created on Wes Oct 2 09:45:21 2019

@author: Fuyou Tan
"""
import sys
from datetime import datetime 
from PyQt5.QtCore import QDate, QDateTime, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QLabel, QLineEdit, QDateEdit,\
                            QComboBox, QTextEdit, QListWidget, QGridLayout, QHBoxLayout, QVBoxLayout,\
                            QSpinBox, QDoubleSpinBox, QGroupBox, QRadioButton, QCheckBox, QTimeEdit, QDateTimeEdit,\
                            QPushButton
                           
class FieldEditWidget(QWidget):
    field_name = ''
    field_widget_type = ''
    field_widget_context = dict() # In terms of different widget type, context has different key and value
    
    def __init__(self, field_name, field_widget_type, field_widget_context): 
        self.field_name = field_name
        self.field_widget_type = field_widget_type
        self.field_widget_context = field_widget_context
        
        super(FieldEditWidget, self).__init__()   
        
        self.field_label = QLabel(field_name, self)        
        self.field_edit = self.__edit_widget_init()
        
        self.field_layout = QHBoxLayout()
        self.field_layout.addWidget(self.field_label)
        self.field_layout.addWidget(self.field_edit)
        
        self.setLayout(self.field_layout)       
     
    # according field_widget_type to set widget type
    def __edit_widget_init(self):
        if self.field_widget_type == 'QLineEdit':
            edit_widget = QLineEdit()
            edit_widget.setText(self.field_widget_context['default'])  
        elif self.field_widget_type == 'QComboBox':
            edit_widget = QComboBox()
            edit_widget.addItems(self.field_widget_context['value_list'])
            edit_widget.setCurrentText(self.field_widget_context['default'])
        elif self.field_widget_type == 'QSpinBox':
            edit_widget = QSpinBox()
            edit_widget.setRange(self.field_widget_context['min_value'], self.field_widget_context['max_value'])                                                      
            edit_widget.setSingleStep(self.field_widget_context['single_step'])                                                       
            edit_widget.setValue(self.field_widget_context['default'])                 
        elif self.field_widget_type == 'QDoubleSpinBox':
            edit_widget = QDoubleSpinBox()
            edit_widget.setRange(self.field_widget_context['min_value'], self.field_widget_context['max_value'])                                                      
            edit_widget.setSingleStep(self.field_widget_context['single_step'])                                                       
            edit_widget.setValue(self.field_widget_context['default'])              
        elif self.field_widget_type == 'QCheckBox':
            edit_widget = QCheckBox()
            edit_widget.setChecked(self.field_widget_context['default'])
        elif self.field_widget_type == 'QDateTimeEdit':
            edit_widget = QDateTimeEdit(QDateTime.currentDateTime())
            edit_widget.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
            edit_widget.setCalendarPopup(True)
        elif self.field_widget_type == 'QDateEdit':
            edit_widget = QDateEdit(QDate.currentDate())
            edit_widget.setDisplayFormat('yyyy-MM-dd')
            edit_widget.setCalendarPopup(True)
        elif self.field_widget_type == 'QTimeEdit':
            edit_widget = QTimeEdit(QTime.currentTime())
            edit_widget.setDisplayFormat('HH:mm:ss')
        else:
            print('could not handle type edit type: %s' % self.field_widget_type) 
            edit_widget = QLineEdit()
        
        return edit_widget
    
    def value(self):
        if self.field_widget_type == 'QComboBox':
            re_value = self.field_edit.currentText()
        elif self.field_widget_type == 'QCheckBox':
            re_value = self.field_edit.isChecked()
        elif self.field_widget_type == 'QDateTimeEdit':
            re_value = self.field_edit.datetime()
        elif self.field_widget_type == 'QDateEdit':
            re_value = self.field_edit.date()
        elif self.field_widget_type == 'QTimeEdit':
            re_value = self.field_edit.time()
        elif self.field_widget_type == 'QLineEdit':
            re_value = self.field_edit.text()            
        else:
            re_value = self.field_edit.value()
        
        return re_value
    
    def set_value(self, value):
        if self.field_widget_type == 'QComboBox':
            self.field_edit.setCurrentText(value)
        elif self.field_widget_type == 'QCheckBox':
            self.field_edit.setChecked(value)
        elif self.field_widget_type == 'QDateTimeEdit':            
            self.field_edit.setDateTime(value)
        elif self.field_widget_type == 'QDateEdit':
            self.field_edit.setDate(value)
        elif self.field_widget_type == 'QTimeEdit':
            self.field_edit.setTime(value)
        elif self.field_widget_type == 'QLineEdit':
            self.field_edit.setText(value)          
        else:
            self.field_edit.setValue(value)      
        
# This ObjectWidget widget is to show a class((objects instance from the class, objects in Neo4j), 
# The widget is divide into two parts, the left part is a list of objects, the right is the detail for one object            

class ObjectWidget(QWidget):
    class_name = dict()
    class_structure = dict()
    objects = dict()
    detail_widgets = dict()
    
    def __init__(self, class_name, class_structure, objects): 
        self.class_name = class_name
        self.class_structure = class_structure
        self.objects = objects        
        super(ObjectWidget, self).__init__()
        # left part -- object list
        self.list_widget = QListWidget(self)
        self.__list_widget_init()
        # right part -- field list
        self.detail_widget = QWidget()
        self.__detail_widget_init()
        # tool bar part
        self.search_combobox = QComboBox()
        self.create_button = QPushButton('Create', self)
        self.update_button = QPushButton('Update', self)
        self.delete_button = QPushButton('Delete', self)
        
        # Horizontal Layout of Object
        self.h_layout_obj = QHBoxLayout()
        self.h_layout_obj.addWidget(self.list_widget)
        self.h_layout_obj.addWidget(self.detail_widget)
        #self.setLayout(self.h_layout_obj)
        # Horizontal layout of Tool bar(CRUD)
        self.h_layout_tool = QHBoxLayout()
        self.h_layout_tool.addWidget(self.search_combobox)
        self.h_layout_tool.addWidget(self.create_button)
        self.h_layout_tool.addWidget(self.update_button)
        self.h_layout_tool.addWidget(self.delete_button)
        #self.setLayout(self.h_layout_tool)
        # Vertial Layout
        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.h_layout_obj)
        self.v_layout.addLayout(self.h_layout_tool)
        self.setLayout(self.v_layout)
        
    def __list_widget_init(self):
        for object in self.objects:            
            self.list_widget.addItem(object)

        self.list_widget.clicked.connect(self.change_func)    
        
    def __detail_widget_init(self):    
        detail_layout = QVBoxLayout()
        for field_id in self.class_structure:
            self.detail_widgets[field_id] = FieldEditWidget(self.class_structure[field_id]['field_name'], 
                          self.class_structure[field_id]['field_widget_type'], 
                          self.class_structure[field_id]['field_widget_context'])
            detail_layout.addWidget(self.detail_widgets[field_id])
            
        self.detail_widget.setLayout(detail_layout)

    def set_object(self, object_name):
        object = self.objects[object_name]
        for field_id in self.class_structure:
            self.detail_widgets[field_id].set_value(object[field_id])
        
    def change_func(self):
        select_object = self.list_widget.currentItem()
        self.set_object(select_object.text())
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    class_name = {'label_id':'cls_aaa','label_name':'People'}
    class_structure = {
            'attr_aaa':{'field_name':'Sex',
                                  'field_widget_type':'QLineEdit',
                                  'field_widget_context':{'default':'Boy'}},
            'attr_aab':{'field_name':'Birth Date',
                        'field_widget_type':'QDateEdit',
                        'field_widget_context':{}}
    }
    objects = {'Mary':{'attr_aaa':'Girl','attr_aab': QDate(datetime.strptime('2019-01-10',"%Y-%m-%d"))},
             'Joe':{'attr_aaa':'Boy','attr_aab':QDate(datetime.strptime('2019-02-10',"%Y-%m-%d"))}            
            }
    demo = ObjectWidget(class_name,class_structure,objects)
    demo.show()
    
#    demo = FieldEditWidget('aaa','QComboBox',{'value_list':['a','b','c','d','e']})
#    demo = FieldEditWidget('aaa','QSpinBox',
#                           {'min_value':0,
#                            'max_value':100,
#                            'single_step':2,
#                            'default':60})
    
#    demo = FieldEditWidget('aaa','QDoubleSpinBox',
#                           {'min_value':0,
#                            'max_value':1,
#                            'single_step':0.02,
#                            'default':0.1})

#    demo = FieldEditWidget('aaa','QCheckBo',{'default':True})
#    demo = FieldEditWidget('aaa','QTimeEdit', {})    
#    demo.show()
#    print(demo.value())
    sys.exit(app.exec_())