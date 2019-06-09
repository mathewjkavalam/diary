def turnpage(date):
    import diaryentry
    diary = diaryentry.load_diary()
    if date in diary:
        return diary[date]
    else:
        return "NIL"