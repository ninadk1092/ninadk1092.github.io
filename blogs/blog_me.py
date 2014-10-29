import sys
import datetime

today = datetime.date.today()
_NAME = "Ninad Kulkarni"
#print sys.argv[1]
with file(sys.argv[1], 'r') as original: data = original.read()
with file(sys.argv[1], 'w') as modified: modified.write( today.strftime('%d, %b %Y')+"\n"+_NAME+"\n" + data)
