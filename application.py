from urllib.parse import urlparse, urljoin
import requests
from flask import Flask, render_template
from flask import request
from bs4 import BeautifulSoup
import re

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def scan():
    if request.method == 'GET':
        return render_template("home/scan-empty.html")
    elif request.method == 'POST':
        global url
        url = request.form["domain"]
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        domain_name = urlparse(url).netloc

        save = []
        secondlayer = set()

        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                # href empty tag
                continue
            # join the URL if it's relative (not absolute link)
            href = urljoin(url, href)
            if domain_name in href:
                if 'http' in href:
                    save.append(href)

        for intilink in save:
            if 'http' in intilink:
                page3 = requests.get(intilink)
                soup2 = BeautifulSoup(page3.text, 'html.parser')


            for a_tag2 in soup2.findAll("a"):
                href2 = a_tag2.attrs.get("href")
                if href2 == "" or href2 is None:
                    # href empty tag
                    continue
                # join the URL if it's relative (not absolute link)
                href2 = urljoin(url, href2)
                if domain_name in href2:
                    if 'http' in href2:
                        secondlayer.add(href2)

        counter1 = 0
        counter2 = 0
        combinedurls = []

        for list in secondlayer:
            try:
                if 'http' in list:
                    scan = requests.get(list)

                    combinedurls.append(list)

                    soup = BeautifulSoup(scan.text, "html.parser")
                    # going into each internal weblinks and getting the js script links
                    src = [sc["src"] for sc in soup.select("script[src]")]
                if len(src) > 1:
                    global internallink
                    internallink = len(src)

                    # constructing the paths
                    for checkdomainlist in src:

                        parsed = urlparse(checkdomainlist)
                        parsedurl = urlparse(url)
                        global resultdomain
                        resultdomain = parsedurl.hostname
                        replacedomain = parsed._replace(netloc=parsedurl)

                        # checking if the path format is bad or not
                        if '/' != str(replacedomain.path[0]):
                            counter1 += 1
                            combinedurls.append("%s/%s" % (url, replacedomain.path))
                        else:
                            counter2 += 1
                            combinedurls.append("%s%s" % (url, replacedomain.path))



            except Exception as e:
                print(e)



        goodurls = counter1
        badurls = counter2
        allurllist = len(combinedurls)
        dataformat = set(combinedurls)
        finalscrapinglinkcount = len(set(combinedurls))


        google_api = """AIza[0-9A-Za-z\\-_]{35}"""
        artifactory = """(?:\s|=|:|"|^)AKC[a-zA-Z0-9]{10,}"""
        artifactorypass = """(?:\s|=|:|"|^)AP[\dABCDEF][a-zA-Z0-9]{8,}"""
        authbasic = """basic [a-zA-Z0-9_\\-:\\.=]+"""
        awsclient = """(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}"""
        awsmwskey = """amzn\.mws\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"""
        awssecret = """(?i)aws(.{0,20})?(?-i)['\"][0-9a-zA-Z\/+]{40}['\"]"""
        base64 = """(eyJ|YTo|Tzo|PD[89]|aHR0cHM6L|aHR0cDo|rO0)[a-zA-Z0-9+/]+={0,2}"""
        basicauthcred = """(?<=:\/\/)[a-zA-Z0-9]+:[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+"""
        cloudanarybasicauth = """cloudinary:\/\/[0-9]{15}:[0-9A-Za-z]+@[a-z]+"""
        fbaccesstoken = """EAACEdEose0cBA[0-9A-Za-z]+"""
        fbclientid = """(?i)(facebook|fb)(.{0,20})?['\"][0-9]{13,17}"""
        fboauth = """[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].*['|\"][0-9a-f]{32}['|\"]"""
        fbsecretkey = """(?i)(facebook|fb)(.{0,20})?(?-i)['\"][0-9a-f]{32}"""
        github = """(?i)github(.{0,20})?(?-i)['\"][0-9a-zA-Z]{35,40}"""
        googlecloud = """(?i)(google|gcp|youtube|drive|yt)(.{0,20})?['\"][AIza[0-9a-z\\-_]{35}]['\"]"""
        googleoauth = """ya29\\.[0-9A-Za-z\\-_]+"""
        googleyoutubeoauth = """[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\\.com"""
        herokuapi = """[h|H][e|E][r|R][o|O][k|K][u|U].{0,30}[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}"""
        ipv4 = """\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}\b"""
        ipv6 = """(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"""
        urlshttp = """https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"""
        urlwithout = """[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"""

        regex = [google_api, artifactory, artifactorypass, authbasic, awsclient, awsmwskey, re.escape(awssecret),
                 base64, basicauthcred, cloudanarybasicauth, fbaccesstoken, fbclientid, fboauth, re.escape(fbsecretkey),
                 re.escape(github), re.escape(googlecloud), re.escape(googleoauth), re.escape(googleyoutubeoauth),
                 re.escape(herokuapi), re.escape(ipv4), re.escape(ipv6), re.escape(urlwithout), re.escape(urlshttp)]

        finaldata = []

        for linkz in set(combinedurls):

            if 'http' in linkz:

                access = requests.get(linkz).text

                reg = re.findall(regex[int(request.form["regex"])], access)
                if len(reg) < 1:
                    notfound = 'Empty'
                    finaldata.append("%s,%s" % (linkz, notfound))
                else:
                    finaldata.append("%s,%s" % (linkz, reg))

        finalurls = []
        for datanow in finaldata:
            splitdata = datanow.split(',')
            finalurls.append(splitdata)


        return render_template("home/scan.html",  finalurls=finalurls, finalscrapinglinkcount=finalscrapinglinkcount, dataformat=dataformat, goodurls=goodurls, badurls=badurls, allurllist=allurllist, resultdomain=resultdomain, internallink=internallink)


if __name__ == "__main__":
    app.run(host='0.0.0.0')