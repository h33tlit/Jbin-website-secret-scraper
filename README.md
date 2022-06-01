<h1 align="center"><img src="https://img.shields.io/badge/Jbin Website Secret Scraper-Version%3A 1.5-red?style=for-the-badge"> 🎖️</h1>
<p>
 <img src="https://img.shields.io/github/issues-raw/h33tlit/Jbin-website-secret-scraper?style=for-the-badge">
 <img src="https://img.shields.io/github/stars/h33tlit/Jbin-website-secret-scraper?color=white&logo=github&style=for-the-badge">
 <img src="https://img.shields.io/github/forks/h33tlit/Jbin-website-secret-scraper?color=white&logo=github&style=for-the-badge">
 <img src="https://img.shields.io/github/commit-activity/m/h33tlit/Jbin-website-secret-scraper?style=for-the-badge">
 
</p>


Jbin will gather all the URLs from the website and then it will try to expose the secret data from them. It collects both URLs and JS links to scrape secrets out of it. Also if you are looking for a specific string in a page or want to run custom regex then you can do that too now with the new release, It also provides you with a informative excel report.

# How does it work?
![image](https://user-images.githubusercontent.com/97327489/171358851-01838996-51f8-466d-9fca-8bff824879fa.png)




# Third Party Components
* Wayback API



# Installation
Required: Python-3.8.5, Flask

1. Install flask ``` pip install Flask ```
2. Install the requirements ```pip install -r requirements.txt```
3. Now set the environment variables ```export FLASK_APP=app.py```
4. Now you can just run the application ```flask run```

[Note]: Make sure you verify that flask is installed ```flask --version```



# Testing

Url: https://peaceful-colden-270bad.netlify.app

*Copy the url and put this as a target in the tool, Select AWS Keys/IPV4/IPV6 from the options and verify it's capabilities*

# Usage

Now go to ```http://127.0.0.1:5000/``` where by default the application will be launched but if that port is in used you can run this ```flask run --host=127.0.0.1 --port=ANY PORT NUMBER```


Enter your target domain and put your custom regex or string, You can run the tool as per your requirement. 

![image](https://user-images.githubusercontent.com/97327489/171360578-dd5d8e57-d17f-4594-a653-fedf4c69c161.png)


![image](https://user-images.githubusercontent.com/97327489/171360736-3dcb2092-da40-43d6-bdcd-4df8d189794a.png)


[Note: Becareful of regex as wrong one can crash the script]

![image](https://user-images.githubusercontent.com/97327489/171361949-d6260453-3b2c-469b-b6e6-fb60749cdb2f.png)

![image](https://user-images.githubusercontent.com/97327489/171362204-4f478c7b-524c-4889-b66a-ed7c25ccebb1.png)




<br/>
<br/>

<br/>
<br/>
<br/>
<br/>

*If you are fine with the old version you can always download it from the package section*

*Please do create <a href='https://github.com/h33tlit/Jbin-website-scraper/issues'>issues</a> if you face any error while using the application*

