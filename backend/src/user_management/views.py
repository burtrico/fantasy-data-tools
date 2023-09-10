from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests_oauthlib import OAuth1Session
from django.contrib.sessions.models import Session
from src.settings.development import YAHOO_CLIENT_ID, YAHOO_CLIENT_SECRET, YAHOO_APP_ID

# Your OAuth 1.0 credentials
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
BASE_AUTHORIZATION_URL = "https://api.twitter.com/oauth/authorize"
CALLBACK_URL = "http://localhost:8000/oauth1_callback"  # Adjust the host and port as necessary
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"


def oauth1_start(request):
    oauth = OAuth1Session(YAHOO_CLIENT_ID, client_secret=YAHOO_CLIENT_SECRET)
    fetch_response = oauth.fetch_request_token(REQUEST_TOKEN_URL)
    resource_owner_key = fetch_response.get('oauth_token')
    resource_owner_secret = fetch_response.get('oauth_token_secret')

    # Save the resource owner credentials in session
    request.session['resource_owner_key'] = resource_owner_key
    request.session['resource_owner_secret'] = resource_owner_secret

    authorization_url = oauth.authorization_url(BASE_AUTHORIZATION_URL)
    return redirect(authorization_url)


def oauth1_callback(request):
    resource_owner_key = request.session.get('resource_owner_key')
    resource_owner_secret = request.session.get('resource_owner_secret')
    verifier = request.GET.get('oauth_verifier')

    oauth = OAuth1Session(YAHOO_CLIENT_ID,
                          client_secret=YAHOO_CLIENT_SECRET,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret,
                          verifier=verifier)

    oauth_tokens = oauth.fetch_access_token(ACCESS_TOKEN_URL)

    request.session['resource_owner_key'] = oauth_tokens.get('oauth_token')
    request.session['resource_owner_secret'] = oauth_tokens.get('oauth_token_secret')

    return HttpResponse("OAuth1 process completed!")
