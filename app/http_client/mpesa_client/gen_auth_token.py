from typing import Union

from fastapi import APIRouter
from fastapi import Response, status, Header
from app.http_client.http import Http

from app.http_client import Http
from mpesa_client.settings import MpesaSandboxSettings
from mpesa_client.models import MpesaAuthTokenResponseModel

# Create an API router
router = APIRouter()
# Initialize settings
settings = MpesaSandboxSettings()
# BASE_URL = settings.MPESA_BASE_URL

# Set the sandbox URL for generating auth token
server = sandbox.sandbox_url
# server = settings.MPESA_BASE_URL
auth_resource = "oauth/v1/"
token_end_point = "generate?grant_type=client_credentials"

# Define summary and description for the endpoint
summary = "Generate Mpesa Auth Token"
description = "This endpoint generates an access token for the Mpesa API using client credentials."

# Define the route for generating auth token
@router.get("/mpesa/generate/auth/token", tags=["Mpesa Authentication Token"], summary= summary,
            description= description, response_model=MpesaTokenResponseModel)

async def generate_mpesa_auth_token(response: Response, username: str, password : str, 
                                    user_agent: Union[str, None] = Header(default="None", include_in_schema=False)):
    
    # Initialize the MpesaTokenResponseModel
    mpesa_token_response_model = MpesaTokenResponseModel

    # call the function to generate the Mpesa token
    mpesa_token_response = await mpesa_generate_oauth_token(username=username, password=password)

    # Assign the response to the model 
    mpesa_token_response_model = mpesa_token_response

    # Set the Http response status  code based on the success of the tokem generation 
    if mpesa_token_response.sucess:
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    # Print the user agent header
    print(user_agent)

    return mpesa_token_response_model
 

# Fuction to generate Mpesa OAuth token
async def mpesa_generate_oauth_token(username: str, password:str):
    url = server + oauth_resource + token_end_point #url for the token generation

    # Set the headers for the request 
    headers = {}

    # Make a request to generate the Mpesa token
    
