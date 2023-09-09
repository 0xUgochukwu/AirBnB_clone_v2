#!/usr/bin/env bash
# Prep web server

if [[ "$(which nginx; echo $?)" == '0' ]];
then
	sudo apt-get update
	sudo apt-get -y nginx
fi

sudo mkdir /data/web_static/shared/ /data/web_static/releases/test/
echo 'HBNB is coming!' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

hbnb="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tindex index.html index.htm;\n\t\ttry_files \$uri \$uri/ =404;\n\t}"
sudo sed -i "/error_page 404 /a${hbnb}" "/etc/nginx/sites-available/default"
sudo service nginx restart
