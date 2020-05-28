#-*- coding:utf-8 -*-
import os
import re

import requests
from subprocess import call

proxies = {
    'http':'socks5://127.0.0.1:1080',
    'https':'socks5://127.0.0.1:1080'
} 

def BeijingAir():

  # set regular expresson to get data
  url = 'https://twitter.com/BeijingAir'
  r = requests.get(url, proxies=proxies)
  m = re.search('data-aria-label-part="0">(.*? )\(at 24-hour exposure at this level\)', r.text)

  #parse data and display with LED
  pm25_list = re.split(';', m.group(1))
  pm25_int = int(pm25_list[3])

  print "\n******"
  print "PM25 in Beijing: %d. %s" % (pm25_int, pm25_list[4])
  print "******\n"
  if(pm25_int < 100):
    # print "Green LED"
    call(["gpio", "blink", "0"])
  elif(pm25_int < 200):
    # print "Yellow LED"
    call(["gpio", "blink", "2"])
  else:
    # print "Red LED"
    call(["gpio", "blink", "3"])

# evoke the timer every one hour to record 
if __name__ == '__main__':
  BeijingAir()
