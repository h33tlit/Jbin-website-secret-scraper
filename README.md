# Jbin Website Secret Scraper V1.1 (Python)


Here is the online demo : <a href="https://jbin-scraper.herokuapp.com/">Jbin</a> ( This might crash because heroku doesn't supply much computing power, try it locally )

Jbin will gather all the URLs from the website and then it will try to expose the secret data from them. It collects both URLs and JS links to scrape secrets out of it. Also if you are looking for a specific string in a page or want to run custom regex then you can do that too now with the new release V1.1, It also provides you with a informative excel report.

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


<img width="1437" alt="Screenshot 2022-02-27 at 4 49 29 AM" src="https://user-images.githubusercontent.com/97327489/155858667-1966516c-c191-405d-86b5-4012af7c89ae.png">



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


<img width="1440" alt="Screenshot 2022-02-27 at 4 50 22 AM" src="https://user-images.githubusercontent.com/97327489/155858685-92b81935-7ed3-4b41-9778-582aa9dee5f6.png">



*Please do create <a href='https://github.com/h33tlit/Jbin-website-scraper/issues'>issues</a> if you face any error while using the application*

