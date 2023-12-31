from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests_oauthlib import OAuth2Session
from django.conf import settings
from rest_framework_jwt.settings import api_settings
# from settings.development import YAHOO_CLIENT_ID, YAHOO_CLIENT_SECRET, YAHOO_APP_ID

# OAuth 2.0 credentials and endpoints
BASE_URL = "https://fantasysports.yahooapis.com/"
AUTHORIZATION_URL = "https://api.login.yahoo.com/oauth2/request_auth"
ACCESS_TOKEN_URL = "https://api.login.yahoo.com/oauth2/get_token"
CALLBACK_URL = "http://localhost:8000/oauth2_callback"
TEAM_URI = "fantasy/v2/team/"
PROTECTED_RESOURCE_URL = BASE_URL + TEAM_URI + "nfl.l.511.t.1/roster/players"

def oauth2_start(request):
    yahoo = OAuth2Session(settings.YAHOO_CLIENT_ID, redirect_uri=CALLBACK_URL)
    authorization_url, state = yahoo.authorization_url(AUTHORIZATION_URL)
    
    # Store state in session for later validation (recommended)
    request.session['oauth_state'] = state

    return redirect(authorization_url)

def oauth2_callback(request):
    yahoo = OAuth2Session(settings.YAHOO_CLIENT_ID, state=request.session['oauth_state'], redirect_uri=CALLBACK_URL)
    yahoo.fetch_token(ACCESS_TOKEN_URL, client_secret=settings.YAHOO_CLIENT_SECRET, authorization_response=request.get_full_path())

    # At this point, yahoo is a fully authorized session
    request.session['oauth_token'] = yahoo.token

    # Create JWT
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)  # You would need to get or create a Django user object here
    token = jwt_encode_handler(payload)

    response_data = {
        'token': token,
        # ... (any other data you want to include in the response)
    }

    return JsonResponse(response_data)

def access_protected_resource(request):
    oauth_token = request.session.get('oauth_token')
    
    if oauth_token:
        yahoo = OAuth2Session(settings.YAHOO_CLIENT_ID, token=oauth_token)
        response = yahoo.get(PROTECTED_RESOURCE_URL)
        
        return HttpResponse(response.content)
    else:
        return HttpResponse("No OAuth credentials stored in session", status=401)
