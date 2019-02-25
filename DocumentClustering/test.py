from flask import Flask, render_template
app = Flask(__name__)

import mysql.connector
from mysql.connector import Error

import datefinder
import datetime

import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean, pdist, squareform
from matplotlib import pyplot as plt
from sklearn import manifold

try:
		# set the database credentials
	conn = mysql.connector.connect(host='localhost', database='visual', user='root', password='pass')
	if conn.is_connected():
			
			# Clusters according to months in an year
		d = dict()
		d = {'1' : [], '2' : [], '3' : [], '4' : [], '5' : [], '6' : [], '7' : [], '8' : [], '9' : [], '10' : [], '11' : [], '12' : []}
		
		# create a connection with the database and query the data
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM sorting_items ORDER BY position_order")
		rows = cursor.fetchall()
		print('Total Row(s):', cursor.rowcount)
		
		data = dict()
		years_dict = dict()
		
		i=0
		j=0
		for row in rows:
#			print (row[2])
			matches = datefinder.find_dates(row[2])
#			print (matches)
			
			for match in matches:
#				print (match)
				datee = datetime.datetime.strptime(str(match), "%Y-%m-%d %H:%M:%S")
#				print (datee.month)
#				data.update({str(row[1]):str(datee.month)})
#				data[row[1]].append(datee.month)
				if datee.month == 1:
					if not row[1] in d['1']:
						d['1'].append(row[1])		
				elif datee.month == 2:
					if not row[1] in d['2']:
						d['2'].append(row[1])							
				elif datee.month == 3:
					if not row[1] in d['3']:
						d['3'].append(row[1])
				elif datee.month == 4:
					if not row[1] in d['4']:
						d['4'].append(row[1])
				elif datee.month == 5:
					if not row[1] in d['5']:
						d['5'].append(row[1])
				elif datee.month == 6:
					if not row[1] in d['6']:
						d['6'].append(row[1])
				elif datee.month == 7:
					if not row[1] in d['7']:
						d['7'].append(row[1])	
				elif datee.month == 8:
					if not row[1] in d['8']:
						d['8'].append(row[1])
				elif datee.month == 9:
					if not row[1] in d['9']:
						d['9'].append(row[1])
				elif datee.month == 10:
					if not row[1] in d['10']:
						d['10'].append(row[1])	
				elif datee.month == 11:
					if not row[1] in d['11']:
						d['11'].append(row[1])
				elif datee.month == 12:
					if not row[1] in d['12']:
						d['12'].append(row[1])

#					data[row[1]].append(datee.month)
					
#					print (row[1], "	" , datee.month)
		
#					print (row[1])
#					print ("i = " , i)
				
#				print ("j = " , j)
				
			# iterate the key value pairs and create a dictionary
#			for key, value in data.items():
##				print (key, value)
#				if value in years_dict:
#					# append the new number to the existing array at this slot
#					years_dict[value].append(key)
#				else:
#					# create a new array in this slot
#					years_dict[value] = [key]

	data = pd.read_excel("matrix.xlSx")
	def similarity_func(u, v):
		return 1/(1+euclidean(u,v))

	dists = pdist(data[data.columns[1:]], similarity_func)
	similarities = pd.DataFrame(squareform(dists))

	mds = manifold.MDS(n_components=2, max_iter=200, eps=1e-9, dissimilarity="precomputed", n_jobs=1)
	pos = mds.fit(similarities).embedding_

	plt.scatter(pos[:, 0], pos[:, 1], color='turquoise', s=111, lw=0, label='MDS')
		#plt.savefig("plot.png")
		#plt = plt.show()
	
except Error as e:
	print(e)

	# close the connection
finally:
	conn.close()