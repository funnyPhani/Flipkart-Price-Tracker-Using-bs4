import pyshorteners as ps

def shortit(link):
    sh = ps.Shortener()
    return sh.tinyurl.short(link)