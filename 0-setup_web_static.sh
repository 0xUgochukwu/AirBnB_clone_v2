#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

if [[ "$(which nginx; echo $?)" == '1' ]]; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

sudo mkdir -p "/data/web_static/releases/test" "/data/web_static/shared"
sudo echo 'Holberton School' > "/data/web_static/releases/test/index.html"
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -hR ubuntu:ubuntu "/data"

static_block="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tindex index.html index.htm;\n\t\ttry_files \$uri \$uri/ =404;\n\t}"
sudo sed -i "/error_page 404 /a${static_block}" "/etc/nginx/sites-available/default"
sudo service nginx restart
