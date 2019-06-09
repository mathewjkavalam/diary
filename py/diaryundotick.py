def registerlast(le,ld):
    registerentry(le)
    registerdate(ld)

def lastentry():
    import pickle
    with open('lastentry.pickle', 'rb') as handle:
        le = pickle.load(handle)
    return le
def lastdate():
    import pickle
    with open('lastdate.pickle', 'rb') as handle:
        ld = pickle.load(handle)
    return ld
def registerdate(ld):
    import pickle
    with open('lastdate.pickle', 'wb') as handle:
        pickle.dump(ld, handle, protocol=pickle.HIGHEST_PROTOCOL)

def registerentry(le):
    import pickle
    with open('lastentry.pickle', 'wb') as handle:
        pickle.dump(le, handle, protocol=pickle.HIGHEST_PROTOCOL)

def today():
    import time
    import diaryentry
    return diaryentry.timestamp_ddmmyyy( int( time.time() )  ) 
#print today()        
def undo_entry():
    import diaryentry
    if(undoable()):
        diary = diaryentry.load_diary()
        page = diary[lastdate()]
        revpage = page[::-1]
        revpage = revpage.replace(lastentry()[::-1],"",1)
        page = revpage[::-1]#reverse of reverse
        diary[lastdate()] = page
        undoable(False)
        diaryentry.store_diary(diary)

def undoable(getorset='get'):
    import pickle
    if(getorset=='get'):
        try:
            with open('undoable.pickle', 'rb') as handle:
                undo = pickle.load(handle)
        except IOError:
            undo = False
        finally:
            return undo
    else:
        with open('undoable.pickle', 'wb') as handle:
            if(getorset == False):
                pickle.dump(False, handle, protocol=pickle.HIGHEST_PROTOCOL)
            if(getorset == True):
                pickle.dump(True, handle, protocol=pickle.HIGHEST_PROTOCOL)
