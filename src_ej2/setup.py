#!/usr/bin/env python3
from distutils.core import setup, Extension
from distutils.command.build_ext import build_ext
from distutils.sysconfig import customize_compiler
import os
import numpy as np

class _build_ext(build_ext):
    def build_extensions(self):
        os.environ['CC'] = 'g++'
        customize_compiler(self.compiler)
        try:
            self.compiler.compiler_so.remove("-Wstrict-prototypes")
        except (AttributeError, ValueError):
            pass
        build_ext.build_extensions(self)

extension_mod = Extension('imfilters',
        language='c++',
        sources=['imfilters.cpp', 'blur_filter.cpp', 'gray_filter.cpp'],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'],)

setup(name='imfilters',
		cmdclass={'build_ext': _build_ext},
        version='1.0',
        include_dirs=[np.get_include()],
        ext_modules=[extension_mod],
)
