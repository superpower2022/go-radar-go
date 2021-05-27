r"""Wrapper for RM_Client_UI.h

Generated with:
/home/radar/miniconda3/envs/radar/bin/ctypesgen -l build/libRoboMasterUILib.so RM_Client_UI.h -o RM_Client_UI.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python v(3, 2)

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):

    _fields_ = [("raw", POINTER(c_char)), ("data", c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup(object):
        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            try:
                return self.Lookup(path)
            except:
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # then we search the directory where the generated python interface is stored
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, libname):
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser("~/lib"), "/usr/local/lib", "/usr/lib"]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        if hasattr(sys, "frozen") and sys.frozen == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    class _Directories(dict):
        def __init__(self):
            self.order = 0

        def add(self, directory):
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            o = self.setdefault(directory, self.order)
            if o == self.order:
                self.order += 1

        def extend(self, directories):
            for d in directories:
                self.add(d)

        def ordered(self):
            return (i[0] for i in sorted(self.items(), key=lambda D: D[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive funtion to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as f:
                for D in f:
                    D = D.strip()
                    if not D:
                        continue

                    m = self._include.match(D)
                    if not m:
                        dirs.add(D)
                    else:
                        for D2 in glob.glob(m.group("pattern")):
                            self._get_ld_so_conf_dirs(D2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HPUX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/x86_64-linux-gnu", "/usr/lib/x86_64-linux-gnu"]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        ext_re = re.compile(r"\.s[ol]$")
        for dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(F)
        load_library.other_dirs.append(F)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["build/libRoboMasterUILib.so"] = load_library("build/libRoboMasterUILib.so")

# 1 libraries
# End libraries

# No modules

u8 = c_uint8# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 14

u16 = c_uint16# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 15

u32 = c_uint32# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 16

Uint8_t = c_ubyte# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 96

U8 = c_ubyte# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 97

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 106
class struct_anon_2(Structure):
    pass

struct_anon_2._pack_ = 1
struct_anon_2.__slots__ = [
    'SOF',
    'Data_Length',
    'Seq',
    'CRC8',
    'CMD_ID',
]
struct_anon_2._fields_ = [
    ('SOF', u8),
    ('Data_Length', u16),
    ('Seq', u8),
    ('CRC8', u8),
    ('CMD_ID', u16),
]

UI_Packhead = struct_anon_2# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 106

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 113
class struct_anon_3(Structure):
    pass

struct_anon_3._pack_ = 1
struct_anon_3.__slots__ = [
    'Data_ID',
    'Sender_ID',
    'Receiver_ID',
]
struct_anon_3._fields_ = [
    ('Data_ID', u16),
    ('Sender_ID', u16),
    ('Receiver_ID', u16),
]

UI_Data_Operate = struct_anon_3# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 113

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 119
class struct_anon_4(Structure):
    pass

struct_anon_4._pack_ = 1
struct_anon_4.__slots__ = [
    'Delete_Operate',
    'Layer',
]
struct_anon_4._fields_ = [
    ('Delete_Operate', u8),
    ('Layer', u8),
]

UI_Data_Delete = struct_anon_4# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 119

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 134
class struct_anon_5(Structure):
    pass

struct_anon_5._pack_ = 1
struct_anon_5.__slots__ = [
    'graphic_name',
    'operate_tpye',
    'graphic_tpye',
    'layer',
    'color',
    'start_angle',
    'end_angle',
    'width',
    'start_x',
    'start_y',
    'graph_Float',
]
struct_anon_5._fields_ = [
    ('graphic_name', c_uint8 * int(3)),
    ('operate_tpye', c_uint32, 3),
    ('graphic_tpye', c_uint32, 3),
    ('layer', c_uint32, 4),
    ('color', c_uint32, 4),
    ('start_angle', c_uint32, 9),
    ('end_angle', c_uint32, 9),
    ('width', c_uint32, 10),
    ('start_x', c_uint32, 11),
    ('start_y', c_uint32, 11),
    ('graph_Float', c_int32),
]

Float_Data = struct_anon_5# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 134

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 151
class struct_anon_6(Structure):
    pass

struct_anon_6._pack_ = 1
struct_anon_6.__slots__ = [
    'graphic_name',
    'operate_tpye',
    'graphic_tpye',
    'layer',
    'color',
    'start_angle',
    'end_angle',
    'width',
    'start_x',
    'start_y',
    'radius',
    'end_x',
    'end_y',
]
struct_anon_6._fields_ = [
    ('graphic_name', c_uint8 * int(3)),
    ('operate_tpye', c_uint32, 3),
    ('graphic_tpye', c_uint32, 3),
    ('layer', c_uint32, 4),
    ('color', c_uint32, 4),
    ('start_angle', c_uint32, 9),
    ('end_angle', c_uint32, 9),
    ('width', c_uint32, 10),
    ('start_x', c_uint32, 11),
    ('start_y', c_uint32, 11),
    ('radius', c_uint32, 10),
    ('end_x', c_uint32, 11),
    ('end_y', c_uint32, 11),
]

Graph_Data = struct_anon_6# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 151

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 157
class struct_anon_7(Structure):
    pass

struct_anon_7._pack_ = 1
struct_anon_7.__slots__ = [
    'Graph_Control',
    'show_Data',
]
struct_anon_7._fields_ = [
    ('Graph_Control', Graph_Data),
    ('show_Data', c_uint8 * int(30)),
]

String_Data = struct_anon_7# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 157

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 159
class struct_MinimapData(Structure):
    pass

struct_MinimapData._pack_ = 1
struct_MinimapData.__slots__ = [
    'x',
    'y',
    'z',
    'key',
    'id',
]
struct_MinimapData._fields_ = [
    ('x', c_float),
    ('y', c_float),
    ('z', c_float),
    ('key', c_uint8),
    ('id', c_uint16),
]

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 168
class struct_MinimapData305(Structure):
    pass

struct_MinimapData305._pack_ = 1
struct_MinimapData305.__slots__ = [
    'id',
    'x',
    'y',
    'dir',
]
struct_MinimapData305._fields_ = [
    ('id', c_uint16),
    ('x', c_float),
    ('y', c_float),
    ('dir', c_float),
]

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 182
class struct_anon_8(Structure):
    pass

struct_anon_8._pack_ = 1
struct_anon_8.__slots__ = [
    'sof',
    'data_length',
    'seq',
    'crc8',
]
struct_anon_8._fields_ = [
    ('sof', c_uint8),
    ('data_length', c_uint16),
    ('seq', c_uint8),
    ('crc8', c_uint8),
]

ext_frame_header_t = struct_anon_8# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 182

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 189
class struct_anon_9(Structure):
    pass

struct_anon_9._pack_ = 1
struct_anon_9.__slots__ = [
    'target_robot_ID',
    'target_position_x',
    'target_position_y',
]
struct_anon_9._fields_ = [
    ('target_robot_ID', c_uint16),
    ('target_position_x', c_float),
    ('target_position_y', c_float),
]

ext_client_map_command_t = struct_anon_9# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 189

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 206
class struct_anon_10(Structure):
    pass

struct_anon_10._pack_ = 1
struct_anon_10.__slots__ = [
    'graphic_name',
    'operate_tpye',
    'graphic_tpye',
    'layer',
    'color',
    'start_angle',
    'end_angle',
    'width',
    'start_x',
    'start_y',
    'radius',
    'end_x',
    'end_y',
]
struct_anon_10._fields_ = [
    ('graphic_name', c_uint8 * int(3)),
    ('operate_tpye', c_uint32, 3),
    ('graphic_tpye', c_uint32, 3),
    ('layer', c_uint32, 4),
    ('color', c_uint32, 4),
    ('start_angle', c_uint32, 9),
    ('end_angle', c_uint32, 9),
    ('width', c_uint32, 10),
    ('start_x', c_uint32, 11),
    ('start_y', c_uint32, 11),
    ('radius', c_uint32, 10),
    ('end_x', c_uint32, 11),
    ('end_y', c_uint32, 11),
]

ext_client_graphic_draw_t = struct_anon_10# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 206

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 216
class struct_anon_11(Structure):
    pass

struct_anon_11._pack_ = 1
struct_anon_11.__slots__ = [
    'header',
    'cmd_id',
    'data',
    'crc16',
]
struct_anon_11._fields_ = [
    ('header', ext_frame_header_t),
    ('cmd_id', c_uint16),
    ('data', ext_client_map_command_t),
    ('crc16', c_uint16),
]

ext_client_map_data_t = struct_anon_11# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 216

enum_anon_12 = c_int# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

game_state = 1# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

game_result = 2# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

game_robot_survivors = 3# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

event_data = 257# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

supply_projectile_action = 258# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

supply_projectile_booking = 259# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

game_robot_state = 513# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

power_heat_data = 514# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

game_robot_pos = 515# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

buff_musk = 516# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

aerial_robot_energy = 517# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

robot_hurt = 518# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

shoot_data = 519# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

robot_interactive_data = 769# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

ext_cmd_id_t = enum_anon_12# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 235

enum_anon_13 = c_int# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_red_hero = 1# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_red_engineer = 2# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_red_infantry_1 = 3# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_red_infantry_2 = 4# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_red_infantry_3 = 5# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_red_aerial = 6# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_red_sentry = 7# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_blue_hero = 11# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_blue_engineer = 12# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_blue_infantry_1 = 13# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_blue_infantry_2 = 14# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_blue_infantry_3 = 15# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_blue_aerial = 16# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

robotid_blue_sentry = 17# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

clientid_red_hero = 257# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

clientid_red_engineer = 258# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

clientid_red_infantry_1 = 259# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

clientid_red_infantry_2 = 260# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

clientid_red_infantry_3 = 261# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

clientid_red_aerial = 262# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

clientid_blue_hero = 273# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

clientid_blue_engineer = 274# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

clientid_blue_infantry_1 = 275# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

clientid_blue_infantry_2 = 276# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

clientid_blue_infantry_3 = 277# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

clientid_blue_aerial = 278# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

ext_id_t = enum_anon_13# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 265

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 271
class struct_anon_14(Structure):
    pass

struct_anon_14._pack_ = 1
struct_anon_14.__slots__ = [
    'graphic_data_struct',
    'data',
]
struct_anon_14._fields_ = [
    ('graphic_data_struct', ext_client_graphic_draw_t),
    ('data', c_uint8 * int(30)),
]

ext_client_custom_character_t = struct_anon_14# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 271

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 284
class struct_anon_15(Structure):
    pass

struct_anon_15._pack_ = 1
struct_anon_15.__slots__ = [
    'header',
    'cmd_id',
    'data_id',
    'sender_id',
    'robot_id',
    'character_data',
    'crc16',
]
struct_anon_15._fields_ = [
    ('header', ext_frame_header_t),
    ('cmd_id', c_uint16),
    ('data_id', c_uint16),
    ('sender_id', c_uint16),
    ('robot_id', c_uint16),
    ('character_data', ext_client_custom_character_t),
    ('crc16', c_uint16),
]

ext_robot_character_data_t = struct_anon_15# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 284

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 289
class struct_anon_16(Structure):
    pass

struct_anon_16._pack_ = 1
struct_anon_16.__slots__ = [
    'graphic_data_struct',
]
struct_anon_16._fields_ = [
    ('graphic_data_struct', ext_client_graphic_draw_t * int(7)),
]

ext_client_custom_graphic_seven_t = struct_anon_16# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 289

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 301
class struct_anon_17(Structure):
    pass

struct_anon_17._pack_ = 1
struct_anon_17.__slots__ = [
    'header',
    'cmd_id',
    'data_id',
    'sender_id',
    'robot_id',
    'graphic_data',
    'crc16',
]
struct_anon_17._fields_ = [
    ('header', ext_frame_header_t),
    ('cmd_id', c_uint16),
    ('data_id', c_uint16),
    ('sender_id', c_uint16),
    ('robot_id', c_uint16),
    ('graphic_data', ext_client_custom_graphic_seven_t),
    ('crc16', c_uint16),
]

ext_robot_sev_graphic_data_t = struct_anon_17# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 301

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 303
if _libs["build/libRoboMasterUILib.so"].has("UI_Delete", "cdecl"):
    UI_Delete = _libs["build/libRoboMasterUILib.so"].get("UI_Delete", "cdecl")
    UI_Delete.argtypes = [String, u8, u8]
    UI_Delete.restype = None

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 304
if _libs["build/libRoboMasterUILib.so"].has("Line_Draw", "cdecl"):
    Line_Draw = _libs["build/libRoboMasterUILib.so"].get("Line_Draw", "cdecl")
    Line_Draw.argtypes = [POINTER(Graph_Data), c_char * int(3), u32, u32, u32, u32, u32, u32, u32, u32]
    Line_Draw.restype = None

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 307
if _libs["build/libRoboMasterUILib.so"].has("UI_ReFresh", "cdecl"):
    _func = _libs["build/libRoboMasterUILib.so"].get("UI_ReFresh", "cdecl")
    _restype = c_int
    _errcheck = None
    _argtypes = [String, c_int]
    UI_ReFresh = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 308
if _libs["build/libRoboMasterUILib.so"].has("Get_CRC8_Check_Sum_UI", "cdecl"):
    Get_CRC8_Check_Sum_UI = _libs["build/libRoboMasterUILib.so"].get("Get_CRC8_Check_Sum_UI", "cdecl")
    Get_CRC8_Check_Sum_UI.argtypes = [POINTER(c_ubyte), c_uint, c_ubyte]
    Get_CRC8_Check_Sum_UI.restype = c_ubyte

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 311
if _libs["build/libRoboMasterUILib.so"].has("Get_CRC16_Check_Sum_UI", "cdecl"):
    Get_CRC16_Check_Sum_UI = _libs["build/libRoboMasterUILib.so"].get("Get_CRC16_Check_Sum_UI", "cdecl")
    Get_CRC16_Check_Sum_UI.argtypes = [POINTER(c_uint8), c_uint32, c_uint16]
    Get_CRC16_Check_Sum_UI.restype = c_uint16

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 313
if _libs["build/libRoboMasterUILib.so"].has("Circle_Draw", "cdecl"):
    Circle_Draw = _libs["build/libRoboMasterUILib.so"].get("Circle_Draw", "cdecl")
    Circle_Draw.argtypes = [POINTER(Graph_Data), c_char * int(3), u32, u32, u32, u32, u32, u32, u32]
    Circle_Draw.restype = None

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 316
if _libs["build/libRoboMasterUILib.so"].has("Rectangle_Draw", "cdecl"):
    Rectangle_Draw = _libs["build/libRoboMasterUILib.so"].get("Rectangle_Draw", "cdecl")
    Rectangle_Draw.argtypes = [POINTER(Graph_Data), c_char * int(3), u32, u32, u32, u32, u32, u32, u32, u32]
    Rectangle_Draw.restype = None

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 319
if _libs["build/libRoboMasterUILib.so"].has("Float_Draw", "cdecl"):
    Float_Draw = _libs["build/libRoboMasterUILib.so"].get("Float_Draw", "cdecl")
    Float_Draw.argtypes = [POINTER(Float_Data), c_char * int(3), u32, u32, u32, u32, u32, u32, u32, u32, c_float]
    Float_Draw.restype = None

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 323
if _libs["build/libRoboMasterUILib.so"].has("Char_Draw", "cdecl"):
    Char_Draw = _libs["build/libRoboMasterUILib.so"].get("Char_Draw", "cdecl")
    Char_Draw.argtypes = [POINTER(String_Data), c_char * int(3), u32, u32, u32, u32, u32, u32, u32, u32, String]
    Char_Draw.restype = None

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 327
if _libs["build/libRoboMasterUILib.so"].has("Char_ReFresh", "cdecl"):
    Char_ReFresh = _libs["build/libRoboMasterUILib.so"].get("Char_ReFresh", "cdecl")
    Char_ReFresh.argtypes = [String, String_Data]
    Char_ReFresh.restype = c_int

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 328
if _libs["build/libRoboMasterUILib.so"].has("Arc_Draw", "cdecl"):
    Arc_Draw = _libs["build/libRoboMasterUILib.so"].get("Arc_Draw", "cdecl")
    Arc_Draw.argtypes = [POINTER(Graph_Data), c_char * int(3), u32, u32, u32, u32, u32, u32, u32, u32, u32, u32]
    Arc_Draw.restype = None

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 332
if _libs["build/libRoboMasterUILib.so"].has("UI_SendMinimap", "cdecl"):
    UI_SendMinimap = _libs["build/libRoboMasterUILib.so"].get("UI_SendMinimap", "cdecl")
    UI_SendMinimap.argtypes = [String, c_uint16, c_float, c_float]
    UI_SendMinimap.restype = c_int

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 333
if _libs["build/libRoboMasterUILib.so"].has("UI_SendMinimap305", "cdecl"):
    UI_SendMinimap305 = _libs["build/libRoboMasterUILib.so"].get("UI_SendMinimap305", "cdecl")
    UI_SendMinimap305.argtypes = [String, c_uint16, c_float, c_float]
    UI_SendMinimap305.restype = c_int

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 335
if _libs["build/libRoboMasterUILib.so"].has("UI_DrawCircle", "cdecl"):
    UI_DrawCircle = _libs["build/libRoboMasterUILib.so"].get("UI_DrawCircle", "cdecl")
    UI_DrawCircle.argtypes = [String, u32, u32, u32, u32, u32, u32, u32, u32]
    UI_DrawCircle.restype = c_int

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 339
if _libs["build/libRoboMasterUILib.so"].has("referee_send_map", "cdecl"):
    referee_send_map = _libs["build/libRoboMasterUILib.so"].get("referee_send_map", "cdecl")
    referee_send_map.argtypes = [String, c_uint16, c_float, c_float]
    referee_send_map.restype = None

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 341
if _libs["build/libRoboMasterUILib.so"].has("UI_DrawFloat", "cdecl"):
    UI_DrawFloat = _libs["build/libRoboMasterUILib.so"].get("UI_DrawFloat", "cdecl")
    UI_DrawFloat.argtypes = [String, c_char * int(3), u32, u32, u32, u32, u32, u32, u32, u32, c_float]
    UI_DrawFloat.restype = None

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 346
if _libs["build/libRoboMasterUILib.so"].has("send_str", "cdecl"):
    send_str = _libs["build/libRoboMasterUILib.so"].get("send_str", "cdecl")
    send_str.argtypes = [String]
    send_str.restype = None

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 347
if _libs["build/libRoboMasterUILib.so"].has("send_multi_graphic", "cdecl"):
    send_multi_graphic = _libs["build/libRoboMasterUILib.so"].get("send_multi_graphic", "cdecl")
    send_multi_graphic.argtypes = [String]
    send_multi_graphic.restype = None

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 4
try:
    Robot_ID = UI_Data_RobotID_RStandard3
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 5
try:
    Cilent_ID = UI_Data_CilentID_RStandard3
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 21
try:
    __FALSE = 100
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 24
try:
    UI_SOF = 165
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 26
try:
    UI_CMD_Robo_Exchange = 769
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 27
try:
    UI_CMD_Minimap = 771
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 28
try:
    UI_CMD_Minimap305 = 773
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 30
try:
    UI_Data_ID_Del = 256
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 31
try:
    UI_Data_ID_Draw1 = 257
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 32
try:
    UI_Data_ID_Draw2 = 258
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 33
try:
    UI_Data_ID_Draw5 = 259
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 34
try:
    UI_Data_ID_Draw7 = 260
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 35
try:
    UI_Data_ID_DrawChar = 272
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 37
try:
    UI_Data_RobotID_RHero = 1
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 38
try:
    UI_Data_RobotID_REngineer = 2
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 39
try:
    UI_Data_RobotID_RStandard1 = 3
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 40
try:
    UI_Data_RobotID_RStandard2 = 4
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 41
try:
    UI_Data_RobotID_RStandard3 = 5
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 42
try:
    UI_Data_RobotID_RAerial = 6
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 43
try:
    UI_Data_RobotID_RSentry = 7
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 44
try:
    UI_Data_RobotID_RRadar = 9
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 46
try:
    UI_Data_RobotID_BHero = 101
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 47
try:
    UI_Data_RobotID_BEngineer = 102
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 48
try:
    UI_Data_RobotID_BStandard1 = 103
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 49
try:
    UI_Data_RobotID_BStandard2 = 104
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 50
try:
    UI_Data_RobotID_BStandard3 = 105
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 51
try:
    UI_Data_RobotID_BAerial = 106
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 52
try:
    UI_Data_RobotID_BSentry = 107
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 53
try:
    UI_Data_RobotID_BRadar = 109
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 55
try:
    UI_Data_CilentID_RHero = 257
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 56
try:
    UI_Data_CilentID_REngineer = 258
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 57
try:
    UI_Data_CilentID_RStandard1 = 259
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 58
try:
    UI_Data_CilentID_RStandard2 = 260
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 59
try:
    UI_Data_CilentID_RStandard3 = 261
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 60
try:
    UI_Data_CilentID_RAerial = 262
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 62
try:
    UI_Data_CilentID_BHero = 357
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 63
try:
    UI_Data_CilentID_BEngineer = 358
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 64
try:
    UI_Data_CilentID_BStandard1 = 359
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 65
try:
    UI_Data_CilentID_BStandard2 = 360
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 66
try:
    UI_Data_CilentID_BStandard3 = 361
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 67
try:
    UI_Data_CilentID_BAerial = 362
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 69
try:
    UI_Data_Del_NoOperate = 0
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 70
try:
    UI_Data_Del_Layer = 1
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 71
try:
    UI_Data_Del_ALL = 2
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 73
try:
    UI_Graph_ADD = 1
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 74
try:
    UI_Graph_Change = 2
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 75
try:
    UI_Graph_Del = 3
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 77
try:
    UI_Graph_Line = 0
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 78
try:
    UI_Graph_Rectangle = 1
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 79
try:
    UI_Graph_Circle = 2
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 80
try:
    UI_Graph_Ellipse = 3
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 81
try:
    UI_Graph_Arc = 4
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 82
try:
    UI_Graph_Float = 5
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 83
try:
    UI_Graph_Int = 6
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 84
try:
    UI_Graph_Char = 7
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 86
try:
    UI_Color_Main = 0
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 87
try:
    UI_Color_Yellow = 1
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 88
try:
    UI_Color_Green = 2
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 89
try:
    UI_Color_Orange = 3
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 90
try:
    UI_Color_Purplish_red = 4
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 91
try:
    UI_Color_Pink = 5
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 92
try:
    UI_Color_Cyan = 6
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 93
try:
    UI_Color_Black = 7
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 94
try:
    UI_Color_White = 8
except:
    pass

# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 218
try:
    REFEREE_FRAME_HEADER_SOF = (c_uint8 (ord_if_char(165))).value
except:
    pass

MinimapData = struct_MinimapData# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 159

MinimapData305 = struct_MinimapData305# /home/radar/Desktop/go-radar-go/communicator/rm_ui/RM_Client_UI.h: 168

# No inserted files

# No prefix-stripping

