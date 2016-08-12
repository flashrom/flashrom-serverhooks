#!/usr/bin/env python
# Metadata filter.
# Fix up a bug in irker 1.14 which adds an extra newline
# 
import sys, json
metadata = json.loads(sys.argv[1])

metadata['logmsg'] = metadata['logmsg'].rstrip('\n ')

print json.dumps(metadata)
# end
