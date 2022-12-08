from aoc_2022.day_07 import Filesystem


def test_filesystem_starts_with_root():
    fs = Filesystem.from_log(["cd /"])
    assert fs.cwd.name == "/"
