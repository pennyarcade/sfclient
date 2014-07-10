#!/usr/bin/python

import sys
from time import time

result = []
for i in range(16):
    result.append('foo')

result[0] = str(int(time()))

report = False

for line in sys.stdin:
    if line.strip() == 'Report':
        report = True

    if report:
        if line.find('statements analysed.') > -1:
            result[1] = line.split(' ')[0].strip()

        if line.find('|code') == 0:
            result[6] = line.split('|')[2].strip()

        if line.find('|docstring') == 0:
            result[3] = line.split('|')[2].strip()

        if line.find('|comment') == 0:
            result[4] = line.split('|')[2].strip()

        if line.find('|empty') == 0:
            result[5] = line.split('|')[2].strip()

        if line.find('|nb duplicated lines') == 0:
            result[6] = line.split('|')[2].strip()

        if line.find('|convention') == 0:
            result[7] = line.split('|')[2].strip()

        if line.find('|refactor') == 0:
            result[8] = line.split('|')[2].strip()

        if line.find('|warning') == 0:
            result[9] = line.split('|')[2].strip()

        if line.find('|error') == 0:
            result[10] = line.split('|')[2].strip()

        if (line.find('|module') == 0) and (line.find('|error') == -1):
            result[12] = line.split('|')[2].strip()

        if line.find('|method') == 0:
            result[13] = line.split('|')[2].strip()

        if line.find('|class') == 0:
            result[14] = line.split('|')[2].strip()

        if line.find('|function') == 0:
            result[15] = line.split('|')[2].strip()

        if line.find('Your code has been rated at') > -1:
            result[11] = line.split(' ')[6].split('/')[0].replace('.', ',')

print ';'.join(result)
