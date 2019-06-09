import diaryentry
import diarypaging
import diaryundotick

import sys

# count the arguments
arguments = len(sys.argv) - 1

# output argument-wise
position = 1  
""" while (arguments >= position):  
    print ("parameter %i: %s" % (position, sys.argv[position]))
    position = position + 1
 """
 import pickle

with open('test.pickle', 'wb') as handle:
    pickle.dump(0, handle, protocol=pickle.HIGHEST_PROTOCOL)
 
 """ date = diaryentry.timestamp_ddmmyyy(1559965269) 
entry = "jesus is my god"#input from php

#entering at a date
diaryentry.make_entry(diaryundotick.today(),entry)

#paging
print diarypaging.turnpage(date)

#undo_entry
diaryundotick.undo_entry()

#tick
diaryentry.tick(diaryundotick.today(),entry) """
