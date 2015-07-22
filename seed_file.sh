#!/bin/bash
TRANSDIR=/var/opt/transmission
cp -p $1 $TRANSDIR/downloaded/
chown debian-transmission:debian-transmission -R $TRANSDIR/downloaded/$1
transmission-create $TRANSDIR/downloaded/$1 -p -t http://10.0.1.77:6969/announce -o /var/www/html/$1.torrent -c $2
transmission-remote --add /var/www/html/$1.torrent
chmod a+r /var/www/html/$1.torrent
