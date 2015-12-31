from flask import Flask, render_template, request
from flask_table import Table, Col
from bs4 import BeautifulSoup
import json
app = Flask(__name__)



def isNumerical(string):
	try:
		float(string)
		return True
	except ValueError:
		return False

def returnData(dictionary):
	data = []
	for i in dictionary.keys():
		json =  "'" + i + "': "
		retrieveKey = dictionary[i]
		if type(retrieveKey) == str:
			json = json + "'" + retrieveKey + "'"
		else:
			json = json + str(retrieveKey)
		data.append(json)
	return "%s({" % str(request.args.get('callback')) + str(','.join(data)) + "})"

def returnListData(listt):
	data = []
	for i in listt:
		data.append(json.dumps(i))
	print listt
	print data
	print "%s({data: [" % str(request.args.get('callback')) + str(','.join(listt)) + "]})"
	return "%s({data: [" % str(request.args.get('callback')) + str(','.join(data)) + "]})"

@app.route("/")
def hello():
	return render_template('form.html')


coordinateDict = [] # list to contain tuples of coordinates
@app.route("/sendCoordinates")
def sendCoordinates():
	latitude = request.args.get('latitude', '')
	longitude = request.args.get('longitude', '')
	if isNumerical(longitude) == False or isNumerical(latitude) == False:
		return returnData({'status' : 'failed'})
	temp = float(latitude), float(longitude)
	coordinateDict.append(temp)
	return returnData({'status' : 'success'})

@app.route("/table")
def populateTable():
	tableList = []
	for i in coordinateDict:
		tableList.append({i[0] : i[1]})
	return returnListData(tableList)

		

if __name__ == "__main__":
    app.run()