rem must change system language locale to utf-8
rem https://www.bing.com/search?q=administrative+language+setting+win+10&form=WNSGPH&qs=AS&cvid=7b4667c3e2804c078bbfa20f11d7eb9f&pq=administrative+language+s&cc=US&setlang=en-US&nclid=5DAC70C3F9718B3FD01438C3459AFE25&ts=1581894742795&wsso=Moderate


set sfd="SUN7_251 Font_0219.sfd"
set ver=7251
set font=times
set alias=EN
set language=english

copy ed11*.svg svg
copy e390*.svg svg
copy e37e*.svg svg


cmd /c fontforge -quiet -script primarywords.py %sfd% pw%ver%.csv

set sfd="SUN7_251 Font_0219.old.sfd"
set ver=7251
set font=times
set alias=EN
set language=english

cmd /c fontforge -quiet -script primarywordsold.py %sfd% pwold%ver%.csv