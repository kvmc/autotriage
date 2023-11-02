import file
import hashes
import yara

import sys


if (len(sys.argv) == 1):
    print("usage: <autotriage.py> <file>")
else:
    filepath = sys.argv[1]
    print(file.file_on_path(filepath))
    print("MD5:    " + hashes.md5sum(filepath))
    print("SHA256: " + hashes.sha256sum(filepath)) 
    print("SHA512: " + hashes.sha512sum(filepath))
    #print("telfhash: " + hashes.telfhash_run(filepath))


