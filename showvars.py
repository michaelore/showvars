from pprint import pprint

class ShowVars(object):
    def __init__(self, lcls = {}):
        self.hideall(lcls)
        self.blacklist = set()

    def ban(self, varname):
        self.blacklist.add(varname)

    def hide(self, k, v):
        self.hashdict[k] = hash(repr(v))

    def hideall(self, lcls):
        self.hashdict = {k: hash(repr(v)) for k, v in lcls.items()}

    def showvars(self, lcls):
        showdict = {}
        for k, v in lcls.items():
            if k not in self.blacklist and \
              (k not in self.hashdict or \
               self.hashdict[k] != hash(repr(v))):
                showdict[k] = v
                self.hide(k, v)
        pprint(showdict)
        print
