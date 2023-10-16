Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: E:/aErdinc/IS/Projeler/pythonProjects/http server-3.py =======
Traceback (most recent call last):
  File "E:/aErdinc/IS/Projeler/pythonProjects/http server-3.py", line 9, in <module>
    with socketserver.TCPServer(("", PORT), handler_from("web")) as httpd:
NameError: name 'socketserver' is not defined
>>> 
======== RESTART: E:/aErdinc/IS/Projeler/pythonProjects/http server-2.py =======
serving at port 8000

======== RESTART: E:/aErdinc/IS/Projeler/pythonProjects/http server-3.py =======
Traceback (most recent call last):
  File "E:/aErdinc/IS/Projeler/pythonProjects/http server-3.py", line 9, in <module>
    with socketserver.TCPServer(("", PORT), handler_from("web")) as httpd:
NameError: name 'socketserver' is not defined
>>> 
======== RESTART: E:/aErdinc/IS/Projeler/pythonProjects/http server-4.py =======
Traceback (most recent call last):
  File "E:/aErdinc/IS/Projeler/pythonProjects/http server-4.py", line 8, in <module>
    os.chdir(web_dir)
FileNotFoundError: [WinError 2] Sistem belirtilen dosyayı bulamıyor: 'E:/aErdinc/IS/Projeler/pythonProjects\\web'
>>> 
======== RESTART: E:/aErdinc/IS/Projeler/pythonProjects/http server-4.py =======
Traceback (most recent call last):
  File "E:/aErdinc/IS/Projeler/pythonProjects/http server-4.py", line 8, in <module>
    os.chdir(web_dir)
FileNotFoundError: [WinError 2] Sistem belirtilen dosyayı bulamıyor: 'E:/aErdinc/IS/Projeler/pythonProjects\\web'
>>> 