# submission

- I decided I am only interested in joining the new projects team.


#Note for challenge 1
Windows:
Start two command prompts. In command prompt #1, move to the directory holding the challenge-1.py. In the terminal, sequentially run "set FLASK_APP=challenge-1.py" and "flask run". Use the server's url for the different requests.

In command prompt #2, you can create your POST, GET, PATCH, and DELETE requests. 

Here are some sample commands:
- curl -X POST  http://{server_url}/tags/{tag_name} -d “{ \\"name\\": \\"{tag_name}\\", \\"contents\\": \\"{message}\\" }”
- curl -X GET  http://{server_url}/tags/{tag_name}/{tag_token}
- curl -X PATCH  http://{server_url}/tags/{tag_name}/{tag_token} -d “{ \"contents\": \"Goodbyte\" }”
- curl -X DELETE  http://{server_url}/tags/{tag_name}/{tag_token} 

Debugging purpose (used to display the dictionary of tags):
- curl -X GET  http://{server_url}/tags/get


Example:
- curl -X POST  http://127.0.0.1:5000/tags/linux -d “{ \\"name\\": \\"linux\\", \\"contents\\": \\"Hello\\" }”


