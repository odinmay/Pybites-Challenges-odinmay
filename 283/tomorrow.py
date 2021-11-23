import datetime

def tomorrow(date = None):
    if date:
        tmrw = date + datetime.timedelta(days=1)
        return tmrw
    else:
        tmrw = datetime.datetime.today() + datetime.timedelta(days=1)
        return tmrw.date()
