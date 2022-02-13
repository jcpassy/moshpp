import platform

import numpy
from setuptools import find_packages, setup, Extension
from Cython.Distutils import build_ext
#from setup_helpers import Extension, setup_extended

sourcefiles = ['sample2meshdist.pyx']
additional_options = {'include_dirs': [numpy.get_include(), '/usr/local/include']}

if platform.system().lower() in ['darwin', 'linux']:
    import sysconfig

    extra_compile_args = sysconfig.get_config_var('CFLAGS').split()
    extra_compile_args += ["-std=c++11"]
    additional_options['extra_compile_args'] = extra_compile_args

setup(
    name='scan2mesh',
    version='1.0',
    description='chumpy based library to calculate scan to mesh distance',
    packages=find_packages(),
    install_requires=['chumpy'],
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("sample2meshdist", sourcefiles, language="c++", **additional_options)],
    include_dirs=['.'],
)
