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