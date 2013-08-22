from pprint import pprint

class ShowVars(object):
    def __init__(self, lcls):
        self.hideall(lcls)

    def hide(self, k, v):
        self.lcls[k] = hash(repr(v))

    def hideall(self, lcls):
        self.lcls = {k: hash(repr(v)) for k, v in lcls.items()}

    def showvars(self, lcls):
        showdict = {}
        for k, v in lcls.items():
            if k not in self.lcls or self.lcls[k] != hash(repr(v)):
                showdict[k] = v
                self.hide(k, v)
        pprint(showdict)
        print
