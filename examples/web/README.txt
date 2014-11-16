Web server tutorial
-------------------

* Install apache2 on your pi
* Setup the document root to something more convenient
* Edit /etc/apache2/sites-available/default

<VirtualHost *:80>
        ServerAdmin webmaster@localhost

        DocumentRoot /home/pi/htdocs/
        <Directory />
                Options FollowSymLinks
                AllowOverride None
                Options +ExecCGI
        </Directory>

	...

* Copy the script 'test.py' into /home/pi/htdocs/
* Make sure it's executable by running: chmod +x /home/pi/htdocs/test.py
* Point your web browser to: localhost/test.py

