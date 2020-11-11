
from flask import Flask, jsonify, request
from uuid import uuid4

app = Flask(__name__)

#Empty 2D dictionary to hold the tags
tagMap = dict()


#Simple message display if server website is visited
@app.route("/")
def hello():
	return "Hello World!"

#########
#POST Request for adding tags
@app.route("/tags/<string:name>", methods=['POST'])
def addTag(name):

	rand_token = uuid4() #Create a random token
	
	data = request.get_json(force=True) #Extract the user's JSON data


	#Create a dictionary tag element to hold the tag's value 
	newTag = {'name' : data['name'], 'contents' : data['contents']}
	
	#returnTag will be displayed to the user, so they can record the token
	returnTag = {'name' : data['name'], 'contents' : data['contents'], 'token': f'{rand_token}'}

	#Key is a concantation of the name and token; ex: nvidia-bob231
	id = f'{name}-{rand_token}'

	#Check if the datapath's name matches the passed JSON's name value
	if name == data['name']:	
		tagMap.update({id: newTag}) #Update the 2D dictionary
		return (jsonify(returnTag),200) #Return the returnTag
	else:
		return ("Error. Name does not match JSON's name.",406) #Raise error if name doesn't match JSON's name value 


#########

#GET Request for displaying the 2D dictionary's contents; used for verifying new changes 
@app.route("/tags/get", methods=['GET'])
def getTestMap():
	return jsonify(tagMap)

#########

#GET Request for specific tag
@app.route("/tags/<string:name>/<string:token>", methods=['GET'])
def getTag(name, token):
	#Construct ID based on passed arguments
	id = f'{name}-{token}'

	#Condition to check if id is inside dictionary
	if (id in tagMap.keys()):

		resTag = tagMap[id]
		return (jsonify(resTag),200)
	else:
		return ("Error. Key cannot be found.",404)


#########

#PATCH Request to update specific tag's content
@app.route("/tags/<string:name>/<string:token>", methods=['PATCH'])
def updateTag(name, token):
	id = f'{name}-{token}'

	data = request.get_json(force=True)

	newContent = data['contents'] #Retrieve the new contents data value

	#Check if id is inside the dictionary
	if (id in tagMap.keys()):
		
		#Change the specified tag's contents data value and update the dictionary
		resTag = tagMap[id]
		resTag['contents'] = newContent

		tagMap[id].update(resTag)

		 
		return ("The specified key's content has been successfully modified.",200)
	else:
		return ("Error. Value cannot be found.",400)



#########

#DELETE Request to delete specific tag
@app.route("/tags/<string:name>/<string:token>", methods=['DELETE'])
def deleteTag(name, token):
	id = f'{name}-{token}'
	if (id in tagMap.keys()):


		tagMap.pop(id) 
		return ("Key and value deleted.",200)
	else:
		return ("Error. Key cannot be found.",404)



