# Jbin Website Secret Scraper (Python)


Here is the online demo : <a href="https://jbin-scraper.herokuapp.com/">Jbin</a> ( This might crash because heroku doesn't supply much computing power, try it locally )

Jbin will gather all the URLs from the website and then it will try to expose the secret data from them. It collects both URLs and JS links to scrape secrets out of it.

# Installation
1. Install flask ``` pip install Flask ```
2. Now set the environment variables ```export FLASK_APP=wsgi.py``` and ```export FLASK_ENV=debug```
3. Now you can just run the application ```flask run```

[Note]: Make sure you verify that flask is installed ```flask --version```



# Usage

Now go to ```http://127.0.0.1:5000/``` where by default the application will be launched but if that port is in used you can run this ```flask run --port=ANY PORT NUMBER```


Enter your target domain and select the regex which will scrape out the secrets.

<img width="1194" alt="Screenshot 2022-02-23 at 11 57 06 PM" src="https://user-images.githubusercontent.com/97327489/155356609-40bc7933-8bc2-4a06-a20a-dc04542e0dfe.png">

Currently we are scraping these secrets:
```
Google API
Artifactory API
Artifactory Pass
Auth Tokens
AWS Client ID
AWS Secret Keys
AWS Keys
Base 64 Data
Basic Auth Credentials
Cloudanary Basic Auth Tokens
Facebook Access Tokens, Client ID, Oauth Tokens and Secret keys
Github Secrets
Google Cloud Tokens, Oauth Tokens
Youtube Oauth Tokens
Heroku API
IPV4
IPV6
URL without http
URL with http

```
The result will be like this:
<img width="1196" alt="Screenshot 2022-02-24 at 12 05 46 AM" src="https://user-images.githubusercontent.com/97327489/155358392-06a7b50d-cf4a-4457-93b2-d898f474f390.png">

If we find a valid secret it will show like this:
<img width="1098" alt="Screenshot 2022-02-24 at 12 11 51 AM" src="https://user-images.githubusercontent.com/97327489/155359593-752bacb0-b4a8-4ecf-bd85-a5b54795ba28.png">



*Please do create <a href='https://github.com/h33tlit/Jbin-website-scraper/issues'>issues</a> if you face any error while using the application*

