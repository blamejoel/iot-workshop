# Internet of Things workshop Spring 2017
### Workshop 6 - Outside access
Slides available [here](#)

### Requirements
* ngrok ([download ARM version!](https://ngrok.com/download))
  * If you want SSH functionality, you'll need to register with ngrok (free)
* [dweet.io](http://dweet.io/)
* Flask (see workshop 2)
* Nginx

### Step by Step
#### Download ngrok and unzip it
```
cd ~/Downloads
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
```
#### Find a better home for ngrok
```
sudo mv ~/Downloads/ngrok /opt/
```

#### Create a script to "dweet" the ngrok url
Create a file `ngrok.sh` at `/opt/` with the following contents (you will need 
to be `root`):
```
#!/usr/bin/env bash
TMP_FILE="/tmp/ngrok.dat"
DWEET_ID=[YOUR UNIQUE DWEET ID!]
NGROK_URL=""
UPDATE=$(date)

if [ -e "$TMP_FILE"  ]; then
    NGROK_URL=$(cat $TMP_FILE)
else
    touch $TMP_FILE
fi

NEW_URL=$(curl -s http://127.0.0.1:4040/status | grep -P "https://.*?ngrok.io" -oh) 

if [[ $(cat $TMP_FILE) != $NEW_URL  ]]; then
    NGROK_URL=$NEW_URL
    echo "${NGROK_URL}" > $TMP_FILE
    if [[ $NGROK_URL != *"http"*  ]]; then
        curl https://dweet.io/dweet/for/$DWEET_ID?ngrokurl=n/a
    else
        curl
        https://dweet.io/dweet/for/$DWEET_ID?ngrokurl=$NGROK_URL&updated=$UPDATE
    fi
else
    exit 0
fi
```

#### Create a cron job to run the dweet script
```
sudo crontab -e
```
Add the following to the end of your crontab file:
```
* * * * * /opt/ngrok.sh
```
Save and exit.

#### Add ngrok auth token (optional & recommended)
```
sudo /opt/ngrok authtoken [paste your auth token here]
```
#### Install Nginx and start the service
```
sudo apt install nginx -y
sudo /etc/init.d/nginx start
```
If you navigate to your RaspberryPi's IP address from a browser on your 
network, you should see a welcome page saying Nginx is setup and working.
#### Setup Flask app
```
sudo mkdir -p /opt/app
cd /opt/app
sudo chown www-data /opt/app
** create/move your Flask app to this directory **
```
#### Install and setup uWSGI
```
sudo apt install build-essential python-dev 
sudo pip install uwsgi
```
#### Test Flask app with uWSGI
```
cd /opt/app
uwsgi --socket 0.0.0.0:8000 --protocol=http -w app:app
```
If you navigate to your RaspberryPi's IP address (with port 8000, e.g. 
http://192.168.1.12:8000) from a browser on your network, you should see your 
Flask app!
#### Configure uWSGI
Create a file called `uwsgi_config.ini` at `/opt/app` with the following contents:
```
[uwsgi]

chdir = /opt/app
module = app:app

master = true
processes = 1
threads = 2

uid = www-data 
gid = www-data
socket = /tmp/flask_app.sock
chmod-socket = 664
vacuum = true

die-on-term = true
```
Then test to make sure the config works...
```
uwsgi --ini /opt/app/uwsgi_config.ini
```
#### Configure uWSGI to start on boot
Edit the file `/etc/rc.local` (you will need to be `root`)  
  
Add the following to the end of the file but *before* the `exit 0`!
```
/opt/ngrok http 80 -log=stdout > /var/log/ngrok.log &

/usr/local/bin/uwsgi --ini /opt/app/uwsgi_config.ini --uid www-data --gid www-data --daemonize /var/log/uwsgi.log
```
#### Configure Nginx to redirect traffic to uWSGI (reverse proxy)
```
sudo rm /etc/nginx/sites-enabled/default
```
Create a new file called `flask_app_proxy` in `/etc/nginx/sites-available` with
the following contents (you
will need to be `root`):
```
server {
 listen 80;
  server_name localhost;

   location / { try_files $uri @app;  }
   location @app {
    include uwsgi_params;
     uwsgi_pass unix:/tmp/flask_app.sock;
      
   }

}
```
Create a symlink to this file...
```
sudo ln -s /etc/nginx/sites-available/flask_app_proxy /etc/nginx/sites-enabled
```
Restart the Raspberry Pi
```
sudo reboot
```
That's it! The next time your Pi boots up, as long as it has Internet access, it
will dweet it's ngrok URL to [https://dweet.io/follow/[your dweet id]](#)

### Additional Resources
* [crontab](https://www.raspberrypi.org/documentation/linux/usage/cron.md)
* [IoT
  Bytes](https://iotbytes.wordpress.com/python-flask-web-application-on-raspberry-pi-with-nginx-and-uwsgi/)
