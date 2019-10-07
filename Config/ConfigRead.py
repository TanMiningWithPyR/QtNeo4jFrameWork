# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:08:21 2019

@author: Fuyou Tan
"""

import numpy as np
import pandas as pd

if __name__=='__main__':  
    class_name = pd.read_excel("config.xlsx",'ClassName').set_index('class_id')
    tblTableName = tblTableName.set_index("id")
    tbl_graph.create_nodes(tblTableName, 'Table')
    tbl_graph.graph.run("CREATE CONSTRAINT ON (c_id:Table) ASSERT c_id.id IS UNIQUE")
    
    tblTableStruction = pd.read_csv("Neo4j_files\\tblTableStruction_utf.csv",
                                    dtype = {'field_width':np.float,
                                             'field_precision':np.float,
                                             'index':np.str})
    tblTableStruction = tblTableStruction.set_index("id")
    tbl_graph.create_nodes(tblTableStruction, 'Field')
    tbl_graph.graph.run("CREATE CONSTRAINT ON (c_id:Field) ASSERT c_id.id IS UNIQUE")
    
    tbl_graph.create_relations(from_node_label='Table',
                               from_node_property='id',
                               to_node_label='Field',
                               to_node_property='table_id',
                               relation_type='Have_Field')
    
    tbl_graph.create_relations(from_node_label="Field",
                               from_node_property="referance",
                               to_node_label="Field",
                               to_node_property="id",
                               relation_type='Referance')
