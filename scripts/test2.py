# calculate sha512 of a file
import hashlib


def sha512_of_file(filename):
    sha512 = hashlib.sha512()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha512.update(chunk)
    return sha512.hexdigest()


print(sha512_of_file("/home/ruby/rpmbuild/SOURCES/MoarVM-2022.12.tar.gz"))
