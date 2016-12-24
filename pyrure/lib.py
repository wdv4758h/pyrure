#!/usr/bin/env python


from ._ffi import ffi


DEFAULT_FLAGS = 32

_lib = ffi.dlopen("./librure.so")


class Rure(object):
    def __init__(self, pattern):
        self.re = self.make_compiled_re(pattern)

    @staticmethod
    def make_rure_options():
        return ffi.gc(_lib.rure_options_new(), _lib.rure_options_free)

    @staticmethod
    def make_rure_error():
        return ffi.gc(_lib.rure_error_new(), _lib.rure_error_free)

    @classmethod
    def make_compiled_re(cls, pattern):
        return ffi.gc(
            _lib.rure_compile(pattern.encode(),
                              len(pattern),
                              DEFAULT_FLAGS,
                              cls.make_rure_options(),
                              cls.make_rure_error()),
            _lib.rure_free
        )

    def is_match(self, string, start=0):
        string = string.encode()
        return bool(_lib.rure_is_match(self.re, string, len(string), start))


# --------------------------------------------------------------------
# Public Interface


# --------------------------------------------------------------------
# Extended Public Interface

def is_match(pattern, string, start=0):
    return Rure(pattern).is_match(string, start)
