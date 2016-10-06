#!/usr/bin/env bash

add-apt-repository ppa:webupd8team/java -y
apt-get update
apt-get install -y git 
apt-get install oracle-java8-set-default -y
# need to run sudo apt-get install oracle-java8-installer -y

git config --global user.name "jialutu"
git config --global user.email jialutu@gmail.com

wget https://orientdb.com/download.php?file=orientdb-community-2.2.10.tar.gz

tar -xf download.php?file=orientdb-community-2.2.10.tar.gz
rm download.php?file=orientdb-community-2.2.10.tar.gz
mv orientdb-community-2.2.10 orientdb