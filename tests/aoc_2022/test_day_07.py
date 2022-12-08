from aoc_2022.day_07 import Filesystem


def test_filesystem_starts_with_root():
    fs = Filesystem.from_log(["cd /"])
    assert fs.cwd.name == "/"


def test_filesystem_reads_ls():
    fs = Filesystem.from_log(
        [
            "$ cd /",
            "$ ls",
            "dir asdf",
            "14848514 b.txt",
            "$ cd asdf",
            "$ ls",
            "1234 c.txt",
        ]
    )
    assert fs.tree["/"].children["asdf"].name == "asdf"
    assert fs.tree["/"].children["b.txt"].size == 14848514
    assert fs.tree["/"].children["asdf"].children["c.txt"].size == 1234


def test_filesystem_goes_down_and_up():
    fs = Filesystem.from_log(
        [
            "$ cd /",
            "$ ls",
            "dir asdf",
            "$ cd asdf",
            "$ ls",
            "1234 c.txt",
            "$ cd ..",
            "$ cd asdf",
        ]
    )
    assert fs.cwd.name == "/"


def test_filesystem_enters_existing_directories():
    fs = Filesystem.from_log(
        [
            "$ cd /",
            "$ ls",
            "dir asdf",
            "$ cd asdf",
            "$ ls",
            "1234 c.txt",
            "$ cd ..",
            "$ cd asdf",
        ]
    )
    assert fs.cwd.name == "asdf"
