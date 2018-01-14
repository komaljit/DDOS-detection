# DDOS-detection

Place the FlaskApp in folder /var/www/FlaskApp/ in which flaskapp.wsgi is the web server gateway interface file to host 
website on the apache2 server.

FlaskApp.conf is the confirguartion file for apache2 in folder /etc/apache2/sites-available


In the project, python script is used to detect the slow loris attack. The logic of python script is very simple,
which is to count the number of keep-alive that a given connection is sending. An upper-bound of 10 is set on the
number of keep-alive that a connection can send in a single request. If the server receives more than 10 keep-alive
it will be detected a slow loris attack against the server and will be logged in ‘warning.log’ file.

The components of the project are described below-

1.	Web server (Apache2 server)- First, Apache server is used to host a local website, against which slow loris attack will be detected.
As we can see in the configuration of apache server, it is set to handle 25 connections at a single time. So, the 26th 
request will not be able connect to the server. We have intentionally set the no of concurrent connection low, to
keep the demo simple.On the apache server keep-alive are on. Using this weakness, hackers conducts the slow loris attack, 
as server allows them to send the keep-alive. The timeout for the keep-alive is 10 second, that a hacker needs to send a
single keep-alive packet with in 10 second. Thus, for this attack attacker needs ver low amount of bandwidth.

              StartServers 1
  
              MaxReqWorkers 25


2.	Website- The following is the website which is hosted on the apache2 server, which is written flask framework, whose
WSGI file is shown below.                           
                          
3.	Detection of Slow Loris-
For the detection of the sow loris attack, raw socket is used. Using python, a raw socket is built, in which all the traffic
for the apache2 server, which is listening on the 80 port is captured. All the incoming traffic is then parsed using “binsacii”
module of the python to get information about the IP and TCP headers of the incoming requests. A python dictionary is used to 
record information about the incoming connections and the keep alive they have sent with in a single request. The value of the
dictionary is incremented every time a connection sends a keep-alive to the server. When that value increases more than 10, that
is detected as slow loris attack against the server. The code for the detection script is provided in the code section.

                         
                  
