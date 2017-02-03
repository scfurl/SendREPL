import os
from ..applescript import osascript

ITERM = os.path.join(os.path.dirname(__file__), "iterm.applescript")
ITERM_BRACKETED = os.path.join(os.path.dirname(__file__), "iterm_bracketed.applescript")


def send_to_iterm(cmd, bracketed=False):
    if bracketed:
        osascript(ITERM_BRACKETED, cmd)
    else:
        osascript(ITERM, cmd)


# def send_to_iterm(cmd, bracketed=False, ipython=False):
#     if bracketed & ipython==False:
#         osascript(ITERM_BRACKETED, cmd)
#     elif bracketed == False & ipython == False:
#         osascript(ITERM, cmd)
#     elif bracketed == False & ipython == True:
#         osascript(ITERM_IPYTHON_TEST, cmd)
#     elif bracketed == True & ipython == True:
#         pass
