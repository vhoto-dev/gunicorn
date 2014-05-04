# -*- coding: utf-8 -
#
# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.

INSTRUMENT_INTERVAL = 5 # publish stats every ... seconds

class Instrument(object):
    """Abstract class for instrumentation"""
    def gauge(self, name, value):
        "Sample a gauge"
        raise NotImplementedError()

    def increment(self, name, value):
        "Increment a counter"
        raise NotImplementedError()

    def decrement(self, name, value):
        "Decrement a counter"
        raise NotImplementedError()
