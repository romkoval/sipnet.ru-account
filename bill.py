# -*- coding: utf-8 -*-

__author__ = 'Roman Kovalev'

import grab
import sys

g = grab.Grab()
g.setup(debug=True)

BASE_URL="https://customer.sipnet.ru/cabinet/"

def get_user_info(user, passwd):
    g.setup(post={'CabinetAction': 'login', \
                  'Name':          user,    \
                  'Password':      passwd   })
    res = g.go(BASE_URL)

    amount   = g.xpath_list("//table[@class='user']/tr/td[2]/div")
    currency = g.xpath_list("//table[@class='user']/tr/td[2]/div/span")
    redirect = g.xpath_list("//meta[@http-equiv='Refresh']/@content")

    if len(amount) > 0 and len(currency) > 0:
        print amount[0].text, currency[0].text
    else:
        if len(redirect) > 0 and redirect[0] == '0; URL=/index.m':
            print >> sys.stderr, 'Invalid userame/password'
        else:
            print >> sys.stderr, 'Unable to parse sipnet.ru answer'



def usage(appname):
    print >> sys.stderr, "Usage: %s 'username' 'password'" % appname
    return -1

if __name__ == '__main__':
    if len(sys.argv) != 3:
        exit ( usage(sys.argv[0]) )
    get_user_info(sys.argv[1], sys.argv[2])

