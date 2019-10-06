# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 11:12:59 2019

@author: Fuyou Tan
"""

from flask import Flask, request, jsonify
from io import BytesIO, StringIO

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime
import json
import base64
import os

app = Flask(__name__)
# app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/get_image/<plotname>')
def get_image(plotname):
    df_data_pd = pd.DataFrame(
            {'aaa': [1,2,3],
             'aab':[4,5,6]}
            )
    plt.plot(df_data_pd)   
    # 写入内存，py3 BytesIO()
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    # img转义base64编码
    # img_base64 = base64.b64encode(img.getvalue()).decode('utf8')
    return img_buffer.getvalue()

@app.route('/send_image/<plotname>', methods=["POST"])
def send_image(plotname):
	# print(os.getcwd())
	if request.method=='POST':
		# print("Posted image: {}".format(request.files['image']))
		# image = request.files['image']
		# images = {'image': image.read()}
		# r = requests.post("http://127.0.0.1:8000/upload/", files=images)

		# if r.ok:
		# 	return "File uploaded!"
		# else:
		# 	return "Error uploading file!"

		# img_buffer = BytesIO(request.files['image'])		
		# with open(os.path.join(os.getcwd(),'test.png'), 'wb') as f:
		# 	f.write(img_buffer.getvalue())

		# img转义base64编码
		# img_base64 = base64.b64encode(img.getvalue()).decode('utf8')
		# print(type(request.files['image']))
		request.files['image'].save(os.path.join(os.getcwd(),'test.png'))
		return "Server received image!"

@app.route('/read_node/<node_label_name>', methods=['POST'])
def read_node(node_label_name):
    if request.method=='POST':         
        node_name = request.form['node_name']    
        print(node_name)
        node = {'attr_aaa':'Girl','attr_aab':'2019-01-10'}
        return_string = json.dumps(node)  
        return return_string

@app.route('/create_node/<node_label_name>/<node_name>',methods=["POST"])
def create_node(node_label_name, node_name):
    if request.method=='POST':         
        attr_aab = request.form['attr_aab'] 
        print(node_label_name + node_name + attr_aab)
        return "Server received data!"

if __name__ == '__main__':
    app.run()