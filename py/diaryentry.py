#convert timestamp->date
# int -> str
# >date +%s
def timestamp_ddmmyyy(t=1545730073):
    from datetime import datetime

    timestamp = int(t) #input from php
    dt_object = datetime.fromtimestamp(timestamp)

    print("dt_object =", dt_object)
    print("type(dt_object) =", type(dt_object))
    print type(dt_object.date().strftime("%d %m %y") )
    date = dt_object.date().strftime("%d-%m-%Y")
    return date

def load_diary():
    import pickle
    try:
        with open('mjkdiary.pickle', 'rb') as handle:
            d = pickle.load(handle)
    except IOError:
        d = {}
    finally:
        return d 

def make_entry(date,entry):
    import diaryundotick
    diary = load_diary()
    if date in diary:
        if diary[date] != "":
            diary[date] += '\n'+entry
            le = '\n'+entry
            diaryundotick.registerlast(le,date)
        else:
            diary[date] += entry
            diaryundotick.registerlast(entry,date)

    else:
        diary[date] = entry
        diaryundotick.registerlast(entry,date)
    diaryundotick.undoable(True)
    store_diary(diary)      
def store_diary(d):
    import pickle
    with open('mjkdiary.pickle', 'wb') as handle:
        pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)

def tick(date,entry):
    diary = load_diary()
    page = diary[date]
    page = page.replace(entry,entry+u'\u2713',1)
    diary[date] = page
    store_diary(diary)