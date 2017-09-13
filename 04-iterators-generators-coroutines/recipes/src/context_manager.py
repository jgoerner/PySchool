import tempfile, shutil
from contextlib import contextmanager

@contextmanager
def tempdir():
    outdir = tempfile.mkdtemp()
    try:
        yield outdir
    finally:
        shutil.rmtree(outdir)
