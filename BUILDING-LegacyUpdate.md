## Building a new copy of NSXfer for LegacyUpdate.

The build process for this is deceptively complex. The best approach I've found
is to use a modern version of Windows. When compiling against NSIS 3.11, I used
Windows Server 2012 R2, but any version after 8.1/Server 2012 R2 should work.

The first step is to download some required software:

- Python 3.13.11 (or 3.14.2 if you're on Server 2016 / Windows 10 and later)
- Git for Windows (for cloning the repository)
- Cygwin (add GCC, MinGW GCC for i686 and x86_64, Make, and Tar)

Next, we'll need to clone a copy of the repository:

```
git clone https://github.com/LegacyUpdate/nsis-nsxfer
```

Next, we'll want to build the project itself.

```
_build_Release_mingw.bat
```

After this batch file runs, you'll have an NSXfer.dll in the Release-mingw-x86-unicode
directory. This is the version of the DLL that you'll want to use for LegacyUpdate.

During the build process, a copy of the NSIS SDK will be downloaded from my webspace
on the Linux From Scratch server. If you want to use a local copy, place the following
files into a new 'nsis' directory prior to running the batch file:

```
Source/exehead/api.h
Contrib/ExDLL/nsis_tchar.h
Contrib/ExDLL/pluginapi.c
Contrib/ExDLL/pluginapi.h
```

These files can be obtained from the NSIS source tree. The ones used at the moment
come from NSIS 3.11.

Next, copy this into your local tree of LegacyUpdate and run a build. Test it on a
VM to make sure that you're able to download files. When that's done, give a copy of
the DLL to Kirb to be signed and included in the next version of LegacyUpdate!
