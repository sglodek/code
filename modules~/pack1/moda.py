from log_setup import log

log('module __name__ = {} : start'.format(__name__))

def modafunc():
    log("executing modafunc")

log('module __name__ = {} : end'.format(__name__))
