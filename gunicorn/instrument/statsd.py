# -*- coding: utf-8 -
#
# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.

"""Bare-bones implementation of statsD's protocol, client-side
"""
import socket
from . import Instrument

# Instrumentation constants
STATSD_DEFAULT_PORT = 8125

class Statsd(Instrument):
    """statsD-based instrumentation
    """
    def __init__(self, dst):
        """host, port: statsD server
        """
        try:
            host, port = dst
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.connect((host, int(port)))
        except Exception:
            self.sock = None

    def gauge(self, name, value):
        try:
            if self.sock:
                self.sock.send("%s:%s|g\n" % (name, value))
        except Exception:
            pass

    def increment(self, name, value):
        try:
            if self.sock:
                self.sock.send("%s:%s|c\n" % (name, value))
        except Exception:
            pass

    def decrement(self, name, value):
        try:
            if self.sock:
                self.sock.send("%s:-%s|c\n" % (name, value))
        except Exception:
            pass
