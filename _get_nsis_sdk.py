# Download NSIS SDK files from the Linux From Scratch server.
# The original script for this used Github, but would pull from the master
# repository for NSIS... and we should really stay locked to the latest
# released version.

from pathlib import Path
from urllib import request

cd = Path(__file__).parent
files = {
    cd.joinpath('nsis', 'api.h')        : "https://www.linuxfromscratch.org/~renodr/NSIS/3.11/api.h",
    cd.joinpath('nsis', 'nsis_tchar.h') : "https://www.linuxfromscratch.org/~renodr/NSIS/3.11/nsis_tchar.h",
    cd.joinpath('nsis', 'pluginapi.c')  : "https://www.linuxfromscratch.org/~renodr/NSIS/3.11/pluginapi.c",
    cd.joinpath('nsis', 'pluginapi.h')  : "https://www.linuxfromscratch.org/~renodr/NSIS/3.11/pluginapi.h",
}

download = False
for file in files:
    if not file.exists(): download = True

if download:
    print("Downloading NSIS SDK ...")
    for file, url in files.items():
        print(file.name)
        with request.urlopen(url) as http:
            file.parent.mkdir(parents=True, exist_ok=True)
            with open(file, 'wb') as outfile:
                outfile.write(http.read())
            print(f"  {http.status} {http.reason}, {http.getheader('Content-Length')} bytes")
else:
    print("Using an existing NSIS SDK ...")
