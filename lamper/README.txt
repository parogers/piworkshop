Add a handler for python cgi scripts: (to mods-enabled/mime.conf)

    AddHandler cgi-script .cgi .py

Enable cgi scripts: (in sites-enabled/...)

       <Directory />

       		  ...
       		  Options +ExecCGI
		  ...

       </Directory>
