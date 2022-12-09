"""
--- Day 7: No Space Left On Device ---

You can hear birds chirping and raindrops hitting leaves as the
expedition proceeds. Occasionally, you can even hear much louder sounds
in the distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its
communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device

Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the
resulting terminal output (your puzzle input). For example:

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k

The filesystem consists of a tree of files (plain data) and directories
(which can contain other directories or files). The outermost directory
is called /. You can navigate around the filesystem, moving into or out
of directories and listing the contents of the directory you're
currently in.

Within the terminal output, lines that begin with $ are commands you
executed, very much like some modern computers:

    cd means change directory. This changes which directory is the
    current directory, but the specific result depends on the argument:
        cd x moves in one level: it looks in the current directory
            for the directory named x and makes it the current
            directory.
        cd .. moves out one level: it finds the directory that contains
            the current directory, then makes that directory the current
            directory.
        cd / switches the current directory to the outermost directory,
            /.
    ls means list. It prints out all of the files and directories
    immediately contained by the current directory:
        123 abc means that the current directory contains a file named
            abc with size 123.
        dir xyz means that the current directory contains a directory
            named xyz.

Given the commands and output in the example above, you can determine
that the filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)

Here, there are four directories: / (the outermost directory), a and d
(which are in /), and e (which is in a). These directories also contain
files of various sizes.

Since the disk is full, your first step should probably be to find
directories that are good candidates for deletion. To do this, you need
to determine the total size of each directory. The total size of a
directory is the sum of the sizes of the files it contains, directly or
indirectly. (Directories themselves do not count as having any intrinsic
size.)

The total sizes of the directories above can be found as follows:

    The total size of directory e is 584 because it contains a single
        file i of size 584 and no other directories.
    The directory a has total size 94853 because it contains files f
        (size 29116), g (size 2557), and h.lst (size 62596), plus file i
        indirectly (a contains e which contains i).
    Directory d has total size 24933642.
    As the outermost directory, / contains every file. Its total size is
        48381165, the sum of the size of every file.

To begin, find all of the directories with a total size of at most
100000, then calculate the sum of their total sizes. In the example
above, these directories are a and e; the sum of their total sizes is
95437 (94853 + 584). (As in this example, this process can count files
more than once!)

Find all of the directories with a total size of at most 100000. What is
the sum of the total sizes of those directories?
"""
from typing import Dict, List, Optional, Union


class Node:
    """One point in a tree."""

    def __init__(
        self,
        name: str,
        size: int = 0,
        parent: Optional["Node"] = None,
        children: Optional[Dict[str, "Node"]] = None,
    ):
        self.name = name
        self.parent = parent
        self.children = children or {}
        self._size = size

    def __repr__(self) -> str:
        """Return repr."""
        class_name = self.__class__.__name__
        name = self.name
        size = str(self.size)
        parent = self.parent.name if self.parent else None
        children = list(name for name in self.children.keys())
        return (
            f"{class_name}(name={name}, "
            f"size={size}, parent={parent}, children={children})"
        )

    @property
    def size(self) -> int:
        return self._size

    def child(self, node_name: str) -> "Node":
        """Return a child node by name."""
        return self.children[node_name]


class File(Node):
    """Data in bytes."""


class Directory(Node):
    """A container for directories and files."""

    @property
    def size(self) -> int:
        """Return size of all directory's contents."""
        return sum(content.size for content in self.children.values())


class ContentFactory:
    @staticmethod
    def make(log_line: str, cwd: Directory) -> Union[Directory, File]:
        if "dir" in log_line:
            _, name = log_line.split()
            return Directory(name=name, parent=cwd)

        size, name = log_line.split()
        return File(name=name, size=int(size), parent=cwd)


class Filesystem:
    """Filesystem of an Elven device."""

    size: int = 70000000

    def __init__(self, root: Directory) -> None:
        self.root = root
        self.cwd = self.root

    @classmethod
    def build_from_log(cls, log: List[str]) -> "Filesystem":
        """Map a filesystem from a log."""
        fs = cls(root=Directory(name="/"))
        i = 1
        while i < len(log):
            line = log[i]
            if "cd" in line:
                _, _, target = line.split()
                if ".." in target:
                    fs.cwd = fs.cwd.parent  # type: ignore
                    i += 1
                else:
                    fs.cwd = fs.cwd.children[target]  # type: ignore
                    i += 1

            if "ls" in line:
                i += 1
                while fs.has_content(log, i):
                    content = ContentFactory.make(log[i], fs.cwd)
                    fs.cwd.children[content.name] = content
                    i += 1

        return fs

    def has_content(self, log: List[str], i: int) -> bool:
        try:
            log_line = log[i]
            return "$" not in log_line
        except IndexError:
            return False

    def size_up_to_limit(self, limit: int = 100000) -> int:
        """Return total size of directories up to a size limit."""
        return self._calculate_up_to_limit(self.root, limit)

    def free_storage(self, minimum: int = 30000000) -> Directory:
        """Return name of smallest directory for minimum freedom."""
        target = minimum - (self.size - self.root.size)

        dirs = self.check_for_best(self.root, target)
        return min(dirs, key=lambda d: d.size)

    def _calculate_up_to_limit(self, directory: Directory, limit: int) -> int:
        if directory.size <= limit:
            return directory.size + sum(
                self._calculate_up_to_limit(content, limit)
                for content in directory.children.values()
                if type(content) == Directory
            )

        return sum(
            self._calculate_up_to_limit(content, limit)
            for content in directory.children.values()
            if type(content) == Directory
        )

    def check_for_best(self, directory: Directory, target: int) -> List[Directory]:
        if directory.size < target:
            return []

        return [directory] + [
            best
            for child in directory.children.values()
            if type(child) == Directory
            for best in self.check_for_best(child, target)
        ]


if __name__ == "__main__":
    with open("aoc_2022/inputs/day_07.txt") as data:
        log = [line[:-1] for line in data]

        fs = Filesystem.build_from_log(log)

        print(f"Part One: {fs.size_up_to_limit()}")
        # print(f"Part Two: {}")
