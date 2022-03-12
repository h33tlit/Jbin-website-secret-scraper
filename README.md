<h1 align="center"><img src="https://img.shields.io/badge/Jbin Website Secret Scraper-Version%3A 1.5-red?style=for-the-badge"> 🎖️</h1>
<p>
 <img src="https://img.shields.io/github/issues-raw/h33tlit/Jbin-website-secret-scraper?style=for-the-badge">
 <img src="https://img.shields.io/github/stars/h33tlit/Jbin-website-secret-scraper?color=white&logo=github&style=for-the-badge">
 <img src="https://img.shields.io/github/forks/h33tlit/Jbin-website-secret-scraper?color=white&logo=github&style=for-the-badge">
 <img src="https://img.shields.io/github/commit-activity/m/h33tlit/Jbin-website-secret-scraper?style=for-the-badge">
 
</p>


Here is the online demo : <a href="https://jbin-scraper.herokuapp.com/">Jbin</a> ( This might crash because heroku doesn't supply much computing power, try it locally )

Jbin will gather all the URLs from the website and then it will try to expose the secret data from them. It collects both URLs and JS links to scrape secrets out of it. Also if you are looking for a specific string in a page or want to run custom regex then you can do that too now with the new release, It also provides you with a informative excel report.

# How does it work?
<img width="1345" alt="Screenshot 2022-03-01 at 3 59 35 AM" src="https://user-images.githubusercontent.com/97327489/156050326-48f38c29-1023-4e9a-b9db-ae7b4863c111.png">


# New Features?

1. Directory bruteforce to get more URLs
2. Custom wordlist
3. Added realtime task monitoring
4. Added the option to reduce power

# Third Party Components
* Wayback API



# Installation
Required: Python-3.8.5, Flask

1. Install flask ``` pip install Flask ```
2. Install the requirements ```pip install -r requirements.txt```
3. Now set the environment variables ```export FLASK_APP=wsgi.py```
4. Now you can just run the application ```flask run```

[Note]: Make sure you verify that flask is installed ```flask --version```



# Testing

Url: https://peaceful-colden-270bad.netlify.app

*Copy the url and put this as a target in the tool, Select AWS Keys/IPV4/IPV6 from the options and verify it's capabilities*

# Usage

Now go to ```http://127.0.0.1:5000/``` where by default the application will be launched but if that port is in used you can run this ```flask run --host=127.0.0.1 --port=ANY PORT NUMBER```


Enter your target domain and put your custom regex or string, You can run the tool as per your requirement. 

<img width="1439" alt="Screenshot 2022-03-12 at 6 17 48 PM" src="https://user-images.githubusercontent.com/97327489/158014080-eab15e17-a7ac-4433-a609-4cf97a85b9fa.png">




Currently we can scrape these secrets!

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


<img width="1440" alt="Screenshot 2022-03-07 at 2 32 05 AM" src="https://user-images.githubusercontent.com/97327489/156936992-c9dc961f-54be-4322-8b33-3c3d4b5d9c70.png">


Demo Excel report:

<img width="649" alt="Screenshot 2022-03-07 at 2 33 11 AM" src="https://user-images.githubusercontent.com/97327489/156937047-eddfc9c2-34dc-484f-8db4-0bfdfe8cae04.png">



# Issues & Fixes

1. Large scopes should be tested locally, Heroku doesn't supply enough computing power since the application does not store any data and does the entire process without any database.

# Ongoing Development

1. Making the script asynchronous to make it even more faster.

<br/>
<br/>
*Please do create <a href='https://github.com/h33tlit/Jbin-website-scraper/issues'>issues</a> if you face any error while using the application*

