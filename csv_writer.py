import csv
import sys

f = open(sys.argv[1], 'wt')
try:
    writer = csv.writer(f, quoting=csv.QUOTE_NONE)
    writer.writerow( ('Serial No.     ',  '    Alfa   ',  '     Date') )
    for i in range(26):
        if i<9:
            writer.writerow( ('     0'+str(i+1)+'        ','     '+chr(ord('A') + i)+'     ','    '+'%02d/04/2014' % (i+1)) )
        else:
            writer.writerow( ('     '+str(i+1)+'        ','     '+chr(ord('A') + i)+'     ','    '+'%02d/04/2014' % (i+1)) )
finally:
    f.close()

print open(sys.argv[1], 'rt').read()
