#!/bin/sh

_DATE=$(date '+%Y%m%d')
#_DATE=$(date '+%Y%m%d_%H%M%S')
#printf "Today is %s\n" "$_DATE"

/usr/local/bin/wkhtmltopdf -q https://news.naver.com/ /var/www/html/news/news_"$_DATE".pdf
#/usr/local/bin/wkhtmltopdf -q --footer-left "[date] [time]" https://news.naver.com/ /var/www/html/news/"$_DATE"_n.pdf
#/usr/local/bin/wkhtmltopdf -q https://news.daum.net/ /var/www/html/news/"$_DATE"_d.pdf
#/usr/local/bin/wkhtmltoimage https://news.naver.com/ /var/www/html/news/"$_DATE"_n.png
#/usr/local/bin/wkhtmltoimage https://news.daum.net/ /var/www/html/news/"$_DATE"_d.png

#crontab -e
#00 9 * * * /home/bsmouse/work/audio/websitecapture.sh
