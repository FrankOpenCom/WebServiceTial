# WebServiceTial

Folers: http://exploreflask.com/en/latest/organizing.html

How to read sqlite3 data? https://sqliteonline.com/

How to handle favicon request? http://www.webweaver.nu/html-tips/favicon.shtml

How to use Sqlite3 in Python Flask: https://www.tutorialspoint.com/flask/flask_sqlite.htm

How to deploy this in NI Linux-64bits target?
1. install latest firmware - stay in safemode
2. opkg update 
3. opkg install python3 ; please make sure there is not pre-installed 
4. opkg install sqlite3 sqlite3-dev
5. opkg install python3-setuptool
6. easy_install flask
7. easy_install waitress


TODO:
1. Add a "Cancel" in topic view to go to the root page
2. delete a topic in many (Frank: Can not reproduce)