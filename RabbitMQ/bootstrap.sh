#!/usr/bin/env bash

apt-get update
apt-get install -y git rabbitmq-server

git config --global user.name "jialutu"
git config --global user.email jialutu@gmail.com

cd /usr/lib/rabbitmq/bin
rabbitmq-plugins enable rabbitmq_management
service rabbitmq-server restart

cd ~

apt-get update