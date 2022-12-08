from aoc_2022.day_07 import Directory, File, Filesystem


def test_filesystem_starts_with_root():
    fs = Filesystem.build_from_log(["$ cd /"])
    assert fs.cwd.name == "/"


def test_filesystem_reads_ls():
    fs = Filesystem.build_from_log(
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
    assert fs.root.child("asdf").name == "asdf"
    assert fs.root.child("b.txt").size == 14848514
    assert fs.root.child("asdf").child("c.txt").size == 1234


def test_filesystem_goes_down_and_up():
    fs = Filesystem.build_from_log(
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


def test_filesystem_enters_existing_directories():
    fs = Filesystem.build_from_log(
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


def test_directory_size_is_size_of_its_contents():
    directory = Directory(name="base")
    child_one = File(name="some.file", size=3)
    child_two = Directory(name="some dir")
    grandchild = File(name="gen-z.txt", size=9)

    child_two.children = {grandchild.name: grandchild}
    directory.children = {
        child_one.name: child_one,
        child_two.name: child_two,
    }
    assert directory.size == child_one.size + grandchild.size


def test_nodes_look_nice():
    file = File(name="some.file", size=3)
    directory = Directory(name="some dir")
    child = File(name="gen-z.txt", size=9)
    directory.children = {child.name: child}

    assert repr(file) == "File(name=some.file, size=3, parent=None, children=[])"
    assert repr(directory) == (
        "Directory(name=some dir, size=9, parent=None, children=['gen-z.txt'])"
    )
