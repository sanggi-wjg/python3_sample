from datetime import datetime

import pytz

target = 'Fri, 13 Nov 2020 15:46:00 +0900'

gmt = datetime.strptime(target, '%a, %d %b %Y %H:%M:%S %z')
gmt = gmt.strftime('%Y-%m-%d %H:%M:%S')
est = datetime.strptime(gmt, '%Y-%m-%d %H:%M:%S')
print(est)
