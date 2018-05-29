# import time or datetime
from datetime import*
import time
import replit
year=int(input('countdown years(say the year you want to find I.E. 2255 or 2314:)'))
months=int(input('countdown months:'))
days=int(input('countdown days:'))
hours=int(input('countdown hours:'))
now=datetime.now()-timedelta(hours=6)
months=months+now.month
while True:
	now=datetime.now()-timedelta(hours=6)
	print(str(year - now.year)+' years\n',
	str(months - now.month)+' months\n',
	str(days + now.day)+' days\n',
	str(hours - now.hour) + ' hour\n',
	str(59-now.minute)+ ' minutes\n',
	str(59-now.second) +' seconds')
	time.sleep(1)
	replit.clear()
