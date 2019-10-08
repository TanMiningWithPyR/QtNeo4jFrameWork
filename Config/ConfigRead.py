# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:08:21 2019

@author: Fuyou Tan
"""

#import numpy as np
import pandas as pd

class ClassConfig():
    def __init__(self):
        self.class_name = pd.read_excel("config.xlsx",'ClassName').set_index('class_id')
        self.class_structure = pd.read_excel("config.xlsx",'ClassStructure').set_index(['class_id','attribute_id'])
    
    def getClassInfo(self, class_id):
        return self.class_name.loc[class_id].to_dict()
        
    def getClassAttributes(self, class_id):
        return self.class_structure.loc[class_id].to_dict(orient='index')
        
    def getAttributeInfo(self, class_id, attribute_id):
        return self.class_structure.loc[class_id].loc[attribute_id].to_dict()
        
if __name__=='__main__':  
    class_config = ClassConfig()
    cls_ent_aaa = class_config.getClassInfo('cls_ent_aaa')
    print(cls_ent_aaa)
    attr_of_cls_ent_aaa = class_config.getClassAttributes('cls_ent_aaa')
    print(attr_of_cls_ent_aaa)
    attr_info = class_config.getAttributeInfo('cls_ent_aaa','attr_aaa')
    print(attr_info)
