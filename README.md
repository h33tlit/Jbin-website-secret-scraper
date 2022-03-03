# Jbin Website Secret Scraper V1.4 (Python)


Here is the online demo : <a href="https://jbin-scraper.herokuapp.com/">Jbin</a> ( This might crash because heroku doesn't supply much computing power, try it locally )

Jbin will gather all the URLs from the website and then it will try to expose the secret data from them. It collects both URLs and JS links to scrape secrets out of it. Also if you are looking for a specific string in a page or want to run custom regex then you can do that too now with the new release, It also provides you with a informative excel report.

# How does it work?
<img width="1345" alt="Screenshot 2022-03-01 at 3 59 35 AM" src="https://user-images.githubusercontent.com/97327489/156050326-48f38c29-1023-4e9a-b9db-ae7b4863c111.png">


# New Features For V1.4?

1. Directory bruteforce to get more URLs
2. Custom wordlist
3. Added realtime task monitoring

# Third Party Components
* Wayback API



# Installation
Required: Python-3.8.5, Flask

1. Install flask ``` pip install Flask ```
2. Install the requirements ```pip install -r requirements.txt```
3. Now set the environment variables ```export FLASK_APP=wsgi.py``` and ```export FLASK_ENV=debug```
4. Now you can just run the application ```flask run```

[Note]: Make sure you verify that flask is installed ```flask --version```



# Testing

Url: https://peaceful-colden-270bad.netlify.app

*Copy the url and put this as a target in the tool, Select AWS Keys/IPV4/IPV6 from the options and verify it's capabilities*

# Usage

Now go to ```http://127.0.0.1:5000/``` where by default the application will be launched but if that port is in used you can run this ```flask run --host=127.0.0.1 --port=ANY PORT NUMBER```


Enter your target domain and put your custom regex or string, You can run all the existing scans if you keep the Regex/String field empty.
![image](https://user-images.githubusercontent.com/97327489/155925531-391b641f-0454-4004-93b6-46ac20b8b828.png)


Currently we are scraping these secrets by default if you keep the field empty for Regex/String:

```
 Google Maps API 
 Artifactory API 
 Artifactory Pass 
 Auth Tokens 
 AWS Access Keys 
 AWS MWS Auth Token 
 Base 64 
 Basic Auth Credentials 
 Cloudanary Basic Auth Tokens 
 Facebook Access Tokens 
 Facebook Oauth Tokens 
 Github Secrets 
 Google Cloud API 
 Google Oauth Tokens 
 Youtube Oauth Tokens 
 Heroku API Keys 
 IPV4 
 IPV6 
 URL Without http 
 URL With http 
 Generic API 
 RSA Private Keys 
 PGP Private Keys 
 Mailchamp API key 
 Mailgun API key 
 Picatic API 
 Slack Token 
 Slack Webhook 
 Stripe API Keys 
 Square Access Token 
 Square Oauth Secret 
 Twilio API key 
 Twitter Client ID 
 Twitter Oauth 
 Twitter Secret Keys 
 Vault Token 
 Firebase Secrets 
 Paypal Braintree Tokens 

```
The result will be like this and you can download the excel to find all the organized links and secrets:
![image](https://user-images.githubusercontent.com/97327489/155925624-88ff9f28-6fc9-40d0-9acd-faabfb4b7530.png)

# Issues & Fixes

1. You might notice that the loading bar is already appearing before you started running any tasks, Go to "Settings" and click on "Fix it" if you face this issue
![image](https://user-images.githubusercontent.com/97327489/155925460-1fc24315-e5de-4734-aa8e-5a9fd83751f7.png)


*Please do create <a href='https://github.com/h33tlit/Jbin-website-scraper/issues'>issues</a> if you face any error while using the application*

