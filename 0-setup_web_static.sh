#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install -y nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
echo "Deploy static" >> /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubntu:ubuntu /data
str='\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}'
sed -i "38i $str" /etc/nginx/sites-available/default
sudo service nginx restart
