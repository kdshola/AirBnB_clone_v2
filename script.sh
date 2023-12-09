#!/usr/bin/env bash

sudo mkdir -p /data/web_static/releases/web_static_20231209070508
sudo tar -xzf /tmp/web_static_20231209070508.tgz -C  /data/web_static/releases/web_static_20231209070508
sudo rm /tmp/web_static_20231209070508.tgz
sudo mv /data/web_static/releases/web_static_20231209070508/web_static/* /data/web_static/releases/web_static_20231209070508/
sudo rm -rf /data/web_static/releases/web_static_20231209070508/web_static
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/web_static_20231209070508 /data/web_static/current
