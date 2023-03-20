import requests
import os

api_endpoint = "https://api.openai.com/v1/completions"
api_key = # Insert API KEY
input_prompt = input("Write python script to .... ")
name_file = input("Names of the file?")

#We need to do a POST requests, which is sending the information to OpenAi
#the variables that the POST requests need is the URL, the HEADER, adn the BODY. In that order

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "+ api_key
}

#In the request data we must specify the model we choose to select (gpt-4-32k), what we will prompt, the max tokens (which is the amount of letter and punctuations we choose to output (100), ,and how creative we want the output to be (from 0 [very predictable] to 1 [very creative], we seleceted 0,5 to be in the middle)
request_data = {
"model": "text-davinci-003",
    "prompt": f"Write python script to  {str(input_prompt)}. Provide only code, no text ",
    "max_tokens": 1000,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers = request_headers, json =  request_data)


#We want to see if the response was actually succesful, and to do so, we need to do a IF loop
#The status.response code outputs a code ranging from 100-199 for informational responses,
#                                                from 200-299 when it was a ** successful response **,
#                                                from 300-399 when its redirecting messages,
#                                                from 400-499 when its a client error response,
#                                                and from 500 - 599 when its a server error response


if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(str(name_file), "w") as file:
        file.write(response_text)

else:
    print(f"Request failed with status code = {str(response.status_code)}")



