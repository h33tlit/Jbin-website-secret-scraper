from flask import Flask, jsonify, render_template, json, Markup, url_for, request, session, redirect, send_file
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import os
import asyncio
from aiohttp import ClientSession
import re

###
app = Flask(__name__)

@app.route('/')
def index():
    path = str(os.getcwd()) + '/internalurls'
    text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
    return render_template('index.html', files=len(text_files))

total = 0
@app.route('/linkscraper', methods=['GET', 'POST'])
def linkscrape():
    if request.method == 'POST':
        # initialize the set of links (unique links)
        domain = request.form['domain'].lower()
        if request.form['maxpage'].isnumeric() == True:
            if int(request.form['maxpage']) > 101:
                return "Sorry we cannot scan that many pages! Our limit is 100 now!"
            max_urls = int(request.form['maxpage'])
        else:
            return 'Error! Something went wrong!'

        if request.form['maxlinks'].isnumeric() == True:
            if int(request.form['maxlinks']) > 101:
                return "Sorry we cannot work with that many links!"
            max_links = int(request.form['maxlinks'])
        else:
            return 'Error! Something went wrong!'


        url = 'http://' + str(domain)

        try:
            requests.get(url, timeout=2)
        except:
            return "Couldn't reach the host!"

        internal_urls = set()
        external_urls = set()
        crawled_urls = set()

        def check_valid(url):
            parsed = urlparse(url)
            return bool(parsed.netloc) and bool(parsed.scheme)

        async def get_website_links(url):
            urls = set()
            domain_name = urlparse(url).netloc
            try:
                content = requests.get(url, timeout=4).content
                soup = BeautifulSoup(content, "html.parser")
            except:
                pass

            for ahref in soup.findAll("a"):
                href = ahref.attrs.get("href")
                if href == "" or href is None:
                    pass
                href = urljoin(url, href)
                parsed_href = urlparse(href)
                href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
                if not check_valid(href):
                    continue
                if href in internal_urls:
                    continue
                if domain_name not in href:
                    if href not in external_urls:
                        external_urls.add(href)
                    continue
                urls.add(href)
                internal_urls.add(href)
            return urls

        async def crawl(url, max_urls):
            global total
            total += 1
            crawled_urls.add(url)

            if doname == urlparse(url).netloc:
                links = await get_website_links(url)
                for link in links:
                    if total > max_urls:
                        break
                    await crawl(link, max_urls=max_urls)
            else:
                pass

        doname = urlparse(url).netloc

        asyncio.run(crawl(url, max_urls=max_urls))

        parseddomain = urlparse(url).netloc


        try:
            # Taking extra URLs from archive.org
            get_wayback = requests.get("http://web.archive.org/cdx/search/cdx?url=" + parseddomain + "*&output=text&fl=original&collapse=urlkey&filter=statuscode%3A200", timeout=5)
            for ex_urls in get_wayback.text.split('\n'):
                internal_urls.add(ex_urls)
        except:
            pass



        #If we find new links by scraping this will get added to the file

        path = str(os.getcwd()) + '/internalurls'
        text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
        if str(parseddomain)+'.txt' in text_files:
            read_internal = open("internalurls/%s.txt" % parseddomain, "r")
            for lines in read_internal.readlines():
                internal_urls.add(lines.replace('\n',''))
            internal = open("internalurls/%s.txt" % parseddomain, "w")
            for int_urls in internal_urls:
                    internal.write("%s\n" % int_urls)
            internal.close()

        else:
            internal = open("internalurls/%s.txt" % parseddomain, "w")

            entry = 0
            for int_urls in internal_urls:
                internal.write("%s\n" % int_urls)
                entry += 1
                if entry == max_links:
                    break
            internal.close()



        #If we fail to scrape any links it will show a message
        if len(internal_urls) != 0:
            return redirect(url_for('linkscrape'))
        else:
            return 'Jbin could not find anything!'

    elif request.method == 'GET':
        path = str(os.getcwd()) + '/internalurls'
        text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
        return render_template('linkscrape.html', text_files=text_files)

@app.route('/download/<string:filename>')
def downloadFile(filename):
    path = str(os.getcwd()) + '/internalurls/' + str(filename)
    return send_file(path, as_attachment=True)

@app.route('/delete/<string:filename>')
def deletefile(filename):
    path = str(os.getcwd()) + '/internalurls/' + str(filename)
    os.remove(path)
    return redirect(url_for('linkscrape'))


@app.route('/bulksecretscanner', methods=['GET','POST'])
def bulkscanner():

    if request.method == 'POST':
        select = request.form['select_file']
        regex_form = request.form['regex']


        path = str(os.getcwd()) + '/foundsecrets'
        text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
        if str(select) in text_files:
            exact_path = str(path)+'/'+str(select)
            os.remove(exact_path)

        def fetch_async(urls):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            future = asyncio.ensure_future(fetch_all(urls))
            loop.run_until_complete(future)

        async def fetch_all(urls):
            tasks = []
            fetch.start_time = dict()
            async with ClientSession() as session:
                for url in urls:
                    task = asyncio.ensure_future(fetch(url, session))
                    tasks.append(task)
                _ = await asyncio.gather(*tasks)

        async def fetch(url, session):
            try:
                async with session.get(url) as response:
                    regex_pattern = re.compile(regex_form)
                    regex = re.findall(regex_pattern, await response.text())
                    secrets_found = []
                    if len(regex) > 0:
                        secrets_found.append('%s |*| Found |*| %s' % (str(url), "  ,  ".join(map(str,regex))))
                    else:
                        secrets_found.append('%s |*| Not Found |*| Empty' % url)

                    secretfile = open("foundsecrets/%s" % select, "a")
                    secretfile.write('%s\n' % str(secrets_found[0]))
                    secretfile.close()

            except:
                pass

        urls = []
        read_internal = open("internalurls/%s" % select, "r")
        for lines in read_internal.readlines():
            if lines != "\n":
                urls.append(lines.strip('\n'))

        fetch_async(urls)

        path = str(os.getcwd()) + '/internalurls'
        text_files = [f for f in os.listdir(path) if f.endswith('.txt')]

        path2 = str(os.getcwd()) + '/foundsecrets'
        secret_files = [f for f in os.listdir(path2) if f.endswith('.txt')]
        return render_template('bulkscanner.html', text_files=text_files, secret_files=secret_files)

    else:
        path = str(os.getcwd()) + '/internalurls'
        text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
        path2 = str(os.getcwd()) + '/foundsecrets'
        secret_files = [f for f in os.listdir(path2) if f.endswith('.txt')]
        return render_template('bulkscanner.html', text_files=text_files, secret_files=secret_files)

@app.route('/secrets/<string:filename>')
def bulkdownloadFile(filename):
    path = str(os.getcwd()) + '/foundsecrets/' + str(filename)
    return send_file(path, as_attachment=True)

@app.route('/delete-secret/<string:filename>')
def bulkdeletefile(filename):
    path = str(os.getcwd()) + '/foundsecrets/' + str(filename)
    os.remove(path)
    return redirect(url_for('bulkscanner'))

@app.route('/view/<string:filename>')
def viewfile(filename):
    data = []
    try:
        read_now = open("foundsecrets/%s" % filename, "r")
        for lines in read_now.readlines():
            if lines != "\n":
                data.append(lines.split('|*|'))

    except:
        pass

    return render_template('view.html', data=data, filename=filename)

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/about')
def about():
    return render_template('about.html')