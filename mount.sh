#!/usr/bin/bash
a=$(blkid | grep 930C-F16B| cut -c1-9)  
echo $a
sudo umount $a
sudo mount -o umask=000 $a /home/snm/server/data

