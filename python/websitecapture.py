#!/usr/bin/python3
import os
import subprocess
from datetime import datetime
from time import sleep

# _DATE=$(date '+%Y%m%d')
# /usr/local/bin/wkhtmltopdf -q https://news.naver.com/ /var/www/html/news/news_"$_DATE".pdf


def subprocess_open(command):
    popen = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdoutdata, stderrdata) = popen.communicate()
    return stdoutdata, stderrdata


def websitecapture(strurl, strname):
    strdate = datetime.now().strftime('%Y%m%d')
    # strdate = datetime.now().strftime('%Y%m%d_%H%M%S')
    command = f'/usr/local/bin/wkhtmltopdf -q {strurl} /var/www/html/news/{strname}{strdate}.pdf'
    print(command)
    stdoutdata, stderrdata = subprocess_open(command)
    # print(stdoutdata)


websitecapture('https://news.naver.com/', 'news_')
# websitecapture('https://news.google.com/topstories?hl=ko', 'gnews_')
