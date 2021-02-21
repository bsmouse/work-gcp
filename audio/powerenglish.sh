#!/bin/sh

_DATE=$(date '+%Y%m%d')
#_DATE=$(date '+%Y%m%d_%H%M%S')
#printf "Today is %s\n" "$_DATE"

/usr/bin/ffmpeg -i http://ebsonair.ebs.co.kr/fmradiobandiaod/bandiappaac/playlist.m3u8 -t 1170 -vn -ab 128k /var/www/html/audio/PE_"$_DATE".mp3 

#crontab -e
#40 7 * * 1,2,3,4,5,6 /home/bsmouse/work/audio/powerenglish.sh
