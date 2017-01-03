#! usr/bin/env python3
# Coded by: AbdulMuaz Aqeel
# Social Media: facebook.com/AbdulMuaz.Aqeel.SSP

from time import sleep

def Terminal_ProgressBar(Text="Downloading", Symbol='#', Speed=0.5):
    precent_limit = 0
    p_symbol = ''
    while precent_limit < 101:
        print(Text +' {0}% ['.format(precent_limit) + p_symbol + ']\r', end='')
        if precent_limit % 2 == 0:
            p_symbol = p_symbol + Symbol
        precent_limit = precent_limit + 1
        sleep(Speed)
    print('\n')

if __name__ == '__main__':
    Terminal_ProgressBar()


