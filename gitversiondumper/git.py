from datetime import datetime
import subprocess
import pathlib


GIT_DESCRIBE = [
    "git", "describe", "--dirty", "--tags", "--long", "--match", "*.*"]


class Git:
    def __init__(self, encoding='utf-8'):
        self.encoding = encoding
        args = ["git", "rev-parse", "--show-toplevel"]
        out = subprocess.check_output(args, encoding=encoding)
        self.path = pathlib.Path(out.strip())

    def get_version(self):
        out = subprocess.check_output(
            GIT_DESCRIBE, encoding=self.encoding, cwd=self.path)
        parts = out.strip().split('-')
        rev = dict(
            tag=parts[0],
            distance=int(parts[1]),
            rev=parts[2],
            dirty=bool(parts[3] if len(parts) > 3 else None)
        )

        return self.dump_version(rev)

    def dump_version(self, rev):
        version = rev["tag"]
        if rev["distance"]:
            version += ".dev{rev[distance]}+{rev[rev]}".format(rev=rev)
        if rev["dirty"]:
            version += "-{d:%Y%m%d}".format(d=datetime.now())
        return version
