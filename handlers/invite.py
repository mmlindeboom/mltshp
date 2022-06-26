import hashlib
import random
import time

import postmark
from base import BaseHandler

from lib.utilities import email_re


class IndexHandler(BaseHandler):
    def get(self):
        return self.render("/invite-friend/index.html")

class CompletionHandler(BaseHandler):
    def get(self):
        return self.render("/invite-friend/completion.html")

class WelcomeHandler(BaseHandler):
    def get(self):
        return self.render("/invite-friend/welcome.html")
