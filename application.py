import datetime
import threading
from urllib.parse import urlparse, urljoin
import requests
from flask import Flask, render_template, send_from_directory
from flask import request
from bs4 import BeautifulSoup
import re
from threading import Thread
from flask import Flask, render_template, Response, request
import xlsxwriter
import os
import glob
import pandas as pd
import json
import time

app = Flask(__name__)
os.chdir("reports")
basedomain = set()

@app.route('/', methods=['POST', 'GET'])
def scan():
    if request.method == 'POST':
        global url
        url = request.form["domain"]
        basedomain.add(url)
        regexselect = request.form["regex"]
        th = Thread(target=task, args=(url,regexselect))
        th.name = urlparse(url).hostname
        th.start()
        thr = []
        finalthread = []
        for thread in threading.enumerate():
            thr.append(thread.name)
            for domain in thr:
                if urlparse(url).hostname in domain:
                    finalthread.append(domain)
        return render_template("home/scan-empty.html", count=threading.active_count(), threadcount=len(finalthread))

    elif request.method == 'GET':
        thr = []
        finalthread = []
        for thread in threading.enumerate():
            thr.append(thread.name)
            for domain in thr:
                for maindomain in set(basedomain):
                    if urlparse(maindomain).hostname in domain:
                        finalthread.append(domain)
        return render_template("home/scan-empty.html", count=threading.active_count(), threadcount=len(finalthread))


def task(url, regexselect):
    global allurlcount
    combinedurls = []
    page = requests.get(url)
    combinedurls.append(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    domain_name = urlparse(url).hostname

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
                combinedurls.append(href)

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
                    combinedurls.append(href2)


    counter1 = 0
    counter2 = 0


    internallink = 0
    for list in secondlayer:
        try:
            if 'http' in list:
                scan = requests.get(list)

                combinedurls.append(list)

                soup = BeautifulSoup(scan.text, "html.parser")
                # going into each internal weblinks and getting the js script links
                src = [sc["src"] for sc in soup.select("script[src]")]

            if len(src) > 1:

                internallink += 1

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
    base64 = """(eyJ|YTo|Tzo|PD[89]|aHR0cHM6L|aHR0cDo|rO0)[a-zA-Z0-9+/]+={0,2}"""
    basicauthcred = """(?<=:\/\/)[a-zA-Z0-9]+:[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+"""
    cloudanarybasicauth = """cloudinary:\/\/[0-9]{15}:[0-9A-Za-z]+@[a-z]+"""
    fbaccesstoken = """EAACEdEose0cBA[0-9A-Za-z]+"""
    fboauth = """[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].*['|\"][0-9a-f]{32}['|\"]"""
    github = """[g|G][i|I][t|T][h|H][u|U][b|B].*['|\"][0-9a-zA-Z]{35,40}['|\"]"""
    googlecloud = """AIza[0-9A-Za-z\\-_]{35}"""
    googleoauth = """ya29\\.[0-9A-Za-z\\-_]+"""
    googleyoutubeoauth = """[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\\.com"""
    herokuapi = """[h|H][e|E][r|R][o|O][k|K][u|U].{0,30}[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}"""
    ipv4 = """\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"""
    ipv6 = """(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"""
    urlshttp = """https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"""
    urlwithout = """[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"""
    genericapi = """[a|A][p|P][i|I][_]?[k|K][e|E][y|Y].*['|\"][0-9a-zA-Z]{32,45}['|\"]"""
    rsaprivatekey = """-----BEGIN RSA PRIVATE KEY-----"""
    pgpprivatekey = """-----BEGIN PGP PRIVATE KEY BLOCK-----"""
    mailchampapikey = """[0-9a-f]{32}-us[0-9]{1,2}"""
    mailgunapikey = """key-[0-9a-zA-Z]{32}"""
    picaticapikey = """sk_live_[0-9a-z]{32}"""
    slacktoken = """xox[baprs]-([0-9a-zA-Z]{10,48})?"""
    slackwebhook = """https://hooks.slack.com/services/T[a-zA-Z0-9_]{10}/B[a-zA-Z0-9_]{10}/[a-zA-Z0-9_]{24}"""
    stripeapikey = """sk_live_[0-9a-zA-Z]{24}"""
    squareaccesstoken = """sqOatp-[0-9A-Za-z\\-_]{22}"""
    squareoauthsecret = """sq0csp-[ 0-9A-Za-z\\-_]{43}"""
    twilioapikey = """SK[0-9a-fA-F]{32}"""
    twitterclientid = """(?i)twitter(.{0,20})?['\"][0-9a-z]{18,25}"""
    twitteroauth = """[t|T][w|W][i|I][t|T][t|T][e|E][r|R].{0,30}['\"\\s][0-9a-zA-Z]{35,44}['\"\\s]"""
    twittersecretkey = """[t|T][w|W][i|I][t|T][t|T][e|E][r|R].*[1-9][0-9]+-[0-9a-zA-Z]{40}"""
    vaulttoken = """[sb]\.[a-zA-Z0-9]{24}"""
    firebase = """.*firebaseio\.com"""
    braintree = """access_token\\$production\\$[0-9a-z]{16}\\$[0-9a-f]{32}"""




    regex = [google_api, artifactory, artifactorypass, authbasic, awsclient, awsmwskey,
             base64, basicauthcred, cloudanarybasicauth, fbaccesstoken, fboauth,
             github, googlecloud, googleoauth, googleyoutubeoauth,
             herokuapi, ipv4, ipv6, urlwithout, urlshttp,
             genericapi, rsaprivatekey, pgpprivatekey, mailchampapikey,
             mailgunapikey, picaticapikey, slacktoken,
             slackwebhook, stripeapikey, squareaccesstoken, squareoauthsecret,
             twilioapikey, twitterclientid, twitteroauth, twittersecretkey,
             vaulttoken, firebase, braintree]

    #Using Directory Bruteforce
    f = open('dir.txt', 'r')

    domain = urlparse(url).hostname

    for list in f.readlines():

        resp = requests.get("https://" + str(domain) + "/" + str(list)).status_code
        if resp == 200:
            combinedurls.append("https://" + str(domain) + "/" + str(list))
        else:
            pass
    f.close()
    #Taking extra URLs from archive.org
    getwayback = requests.get("http://web.archive.org/cdx/search/cdx?url=" + domain_name + "*&output=text&fl=original&collapse=urlkey&filter=statuscode%3A200")

    for d in getwayback.text.split('\n'):
        combinedurls.append(d)
    #######################################################################


    #Regex matching

    finaldata = []

    for linkz in set(combinedurls):

        if 'http' in linkz:

            access = requests.get(linkz).text

            if len(regexselect) < 1:
                for allregex in regex:
                    reg = re.findall(str(allregex), access)
                    if len(reg) < 1:
                        notfound = 'Empty'
                        finaldata.append("%s,%s" % (linkz, notfound))
                    else:
                        finaldata.append("%s,%s" % (linkz, reg))
            elif len(regexselect) > 1:
                reg = re.findall(str(regexselect), access)
                if len(reg) < 1:
                    notfound = 'Empty'
                    finaldata.append("%s,%s" % (linkz, notfound))
                else:
                    finaldata.append("%s,%s" % (linkz, reg))

    finalurls = []
    for datanow in set(finaldata):
        splitdata = datanow.split(',')
        finalurls.append(splitdata)

    #converting it to an excel report

    workbook = xlsxwriter.Workbook('%s.xlsx' % (urlparse(url).hostname))
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    for url, *data in (finalurls):
        worksheet.write(row, col, str(url))
        worksheet.write(row, col + 1, str(data).replace(',','\n').replace(']','').replace('[','').replace("'","").replace('"',''))
        row += 1

    workbook.close()


@app.route('/download/<string:filename>', methods=['GET', 'POST'])
def download_link(filename):
   directory='reports'
   return send_from_directory(path=os.getcwd(), directory=directory, filename=filename)



@app.route('/reports')
def reports():
    alldata = []
    directory = []
    for dirs in glob.glob("*.xlsx"):
        excel_data = pd.read_excel('%s' % dirs)
        data = pd.DataFrame(excel_data)
        count = re.findall('Empty', str(data))

        directory.append('%s,%d,%d' % (dirs, len(data), len(count)))
    ########
    for x in directory:
        y = x.split(',')
        alldata.append(y)


    return render_template('home/reports.html', count=threading.active_count(), alldata=alldata)


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    return render_template('home/settings.html', count=threading.active_count())

@app.route('/wordlist', methods=['GET', 'POST'])
def wordlist():
    if request.method == 'GET':
        return render_template('home/settings.html', count=threading.active_count())
    if request.method == 'POST':
        wordlist = request.form['wordlist']
        fd = open("dir.txt", "w")
        fd.write(wordlist)
        fd.close()
    return render_template('home/settings.html', count=threading.active_count())


@app.route('/listen/<string:domain>')
def listen(domain):
    def respond_to_client():
        while True:
                global counter
                thr = []
                for thread in threading.enumerate():
                    thr.append(thread.name)
                    if domain in thr:
                        doing = """<label class="badge badge-danger"><span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Running</label>"""
                    else:
                        doing = """<label class="badge badge-success">Finished</label>"""
                _data = json.dumps({"process": doing})
                yield f"id: 1\ndata: {_data}\nevent: online\n\n"
                time.sleep(0.5)

    return Response(respond_to_client(), mimetype='text/event-stream')


@app.route('/list')
def list():
    thr = []
    list = []
    for thread in threading.enumerate():
        thr.append(thread.name)
        if 'MainThread' in thread.name:
            pass
        elif 'Thread-' in thread.name:
            pass
        elif 'ThreadPoolExecutor-' in thread.name:
            pass
        else:
            list.append(thread.name)

    return render_template('home/list.html', threadprocess=list)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('home/error.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('home/error.html'), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0')
