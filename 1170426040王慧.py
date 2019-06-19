def toFullPath(sub,parent):
    if isFullPath(sub):
        return sub
    if sub == "/":
        return "http://%s" % (getDomain(parent))
    if sub[:1] == "/":
        baseUrl = getDomain(parent)
    else:
        baseUrl = getBaseUrl(parent)
    relPath = getRelPath(sub)
    return "http://%s/%s" % (baseUrl,relPath)