#!/usr/bin/env python

from os import path

from cffi import FFI


ffi = FFI()
ffi.set_source('pyrure.ffi', None)
ffi.cdef(
    '\n'.join(
        # skip some lines that will break cdef :(
        filter(
            lambda x: not x.startswith(
                ("#ifndef","#include","#ifdef", 'extern "C"', '#endif', '}\n', '#define')
            ),
            open(
                path.join(path.dirname(path.abspath(__file__)), "..", "include", "rure.h")
            ).readlines()
        )
    )
)


if __name__ == '__main__':
    ffi.compile(verbose=True)
