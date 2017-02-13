import os
from nose import with_setup
from nose.tools import assert_equals
from nose.tools import assert_true
from src.python.simple_io import cat, process, write, init


INFILE = 'shared/input.txt'
OUTFILE = 'shared/output.txt'


def setup():
    if os.path.exists(OUTFILE):
        os.remove(OUTFILE)


def teardown():
    pass


def test_init():
    write(OUTFILE, process(cat(INFILE)))
    init()
    assert_true(not os.path.exists(OUTFILE))


def test_cat():
    assert_true(cat(INFILE).startswith('This is some random input'))


def test_process():
    assert_equals("UPPER CASE", process('upper case'))


@with_setup(setup, teardown)
def test_write():
    write(OUTFILE, process(cat(INFILE)))
    assert_true(cat(OUTFILE).startswith("THIS IS SOME RANDOM INPUT"))
