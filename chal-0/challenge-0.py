#Python script to interact with the API
import requests

API_ENDPOINT = "https://us-central1-acm-core.cloudfunctions.net/challenge"

#Defined name data value
name = "linux"

contents = "I'd just like to interject for a moment. What you're referring to as Linux is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux..."

#Defined tag data value
data = {

"name": name,
"contents": contents

}


#Define POST request's URL
POST_API_URL = API_ENDPOINT + "/tags/" + name



#Make POST request
r = requests.post(url=POST_API_URL, data =data) 

#Print the POST request's response 
print("This is the POST request")
print(r.text)



#Make GET request to retrieve the specific tag

#Retrieve the token and intialize a token variable
extracted_data = r.json()
token = extracted_data["token"]

GET_PATCH_API_URL = API_ENDPOINT + "/tags/" + f"{name}/"+ token
r = requests.get(url = GET_PATCH_API_URL) 
#Print the GET request's response 
print("This is the GET request")
print(r.text)


#Make PATCH request
#Define new contents data value and initialize a dictionary
newContents = "Something else"

new_data ={
    "contents": newContents 
}


r = requests.patch(url = GET_PATCH_API_URL, data = new_data)
print("This is the PATCH request")
print(r.text) #Print the PATCH request's reponse




#Make GET Request to see the tag's new changes
#r = requests.get(url = GET_PATCH_API_URL) 
#print(r.text)



#Make DELETE Request to delete the tag
r = requests.delete(url = GET_PATCH_API_URL) 

#Print status code
print("This is the DELETE request")
print(r.status_code)

