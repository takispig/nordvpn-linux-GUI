#!/bin/sh

# I had to split them, cause before the 'Status' i experienced some weird symbols that i couldn't resolve
# Later i'll try to find a more effective/cleaner way to do it
nordvpn status | grep -o "Status.*"
nordvpn status | sed -n '2,9p'
