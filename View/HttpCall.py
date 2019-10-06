# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:19:28 2019

@author: Fuyou Tan
"""

from datetime import datetime
import requests
import json

URL = 'http://127.0.0.1:5000'

def create_node(node_label_name, node_name, node):
    r = requests.post('/'.join([URL,'create_node',node_label_name,node_name]), data=node)
    return r.text
    
def read_node(node_label_name, node_name):
    r = requests.post('/'.join([URL,'read_node',node_label_name]), data={'node_name':node_name})
    return json.loads(r.text)

def update_node(node_label_name, node_name, node):
    r = requests.post('/'.join([URL,'update_node',node_label_name,node_name]) + node_label_name, data=node)
    return r.text
    
def delete_node(node_label_name, node_name):
    r = requests.post('/'.join([URL,'delete_node',node_label_name]), data={'node_name':node_name})
    return r.text
    
if __name__ == '__main__':
    node_label_name = 'cls_aaa'
    node_name = 'Mary'
    node = {'attr_aaa':'Girl','attr_aab':datetime.strptime('2019-01-10',"%Y-%m-%d")}
    # print(create_node(node_label_name,node_name,node))
    print(read_node(node_label_name,node_name))