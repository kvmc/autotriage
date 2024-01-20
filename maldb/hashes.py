from hashlib import md5, sha1, sha256, sha512

def md5sum(data):
    return md5(data).hexdigest()

def sha1sum(data):
    return sha1(data).hexdigest()   

def sha256sum(data):  
    return sha256(data).hexdigest()

def sha512sum(data):
    return sha512(data).hexdigest()

#hash checks

def hash_is_md5(_hash) -> bool:
    return len(_hash) == 32


def hash_is_sha1(_hash) -> bool:
    return len(_hash) == 40

def hash_is_sha256(_hash) -> bool:
    return len(_hash) == 64

def hash_is_sha512(_hash) -> bool:
    return len(_hash) == 128
