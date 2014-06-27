'''
    Decode URL

'''

import sys, urlparse


parts = urlparse.urlparse(sys.argv[1])

#print parts.query

query = urlparse.parse_qs(parts.query)

#print query

print 'sessionid', query['req'][0][:32]
print 'action', query['req'][0][32:]

