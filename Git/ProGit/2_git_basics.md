# Git Basics

## Existing directory to Git

```Bash
# navigate to the directory
# Thsi command creates the .git directory
git init .

# add the files that needs to be version controlled.
git add LICENSE
git add Readme.md

git commit -m "adding license and readme"
```

## Cloning an existing repository

```Bash
# clones the repo in to the current directory
git clone [URL] .
```

## Recording changes to the repository

Each file in the working directory can be either **tracked** or **untracked**

* **untracked** - file in working directory not part of the last snapshot and not in the staging area.

* **tracked** - files present in the last snapshot. These files can be **modified**, **unmodified** or **staged**.

  * **modified** - file changed from its last snapshot.
  * **unmodified** - file contents are the same as in the previous snapshot.
  * **staged** - file that was modified and added to the staging area.

## Checking the status of the file

* view unstracked files and modified files in the working directory
* view changes to be committed in the staging area

```Bash
# with in the git repo directory
git status
```

## Tracking new files

`git add` command takes a path (file or directory).

* If given a file, marks a file in its **current state for commit**.
* If given a directory, then all the files in this directory are moved to staging area marking for the next commit.

## Short status

`git status -s` or `git status --short`

Output **status code** contains two columns. Left one for the staging area and the right one for the working directory.

* "??" - untracked(unknown to both staging area and working directory)
* "A " - new files added to staging area (when untracked file added to staging area)
* " M" - modified in working directory and not yet staged
* "M " - modifies file and added to the staging area
* "MM" - modified and staged and modified again in the working directory.

## Ignoring files

Define the exclusion patterns in **.gitignore** file. Patterns are relative to location of **.gitignore** file containing it. `man gitignore` for more details on **gitignore**.

> Patterns read from a .gitignore file in the same directory as the path, or in any parent directory, with patterns in the higher level files (up to the toplevel of the work tree) being overridden by those in lower level files down to the directory containing the file. - [Gitignore Doc](https://git-scm.com/docs/gitignore)

* comments in gitignore start with "#"
* standard glob patterns(shell glob patterns) work. Applied recursively throughout entire working tree.
* !(pattern) - negates the pattern
* patterns starting with "/" - not applied recursively
* patterns ending with "/" - to specify a directory

More notes on the gitignore pattern can be found [here](https://git-scm.com/docs/gitignore#_pattern_format)

NOTE: `**` used to match nested directories.

```Conf
# ignore all .a files
*.a

# but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the TODO file in the current directory, not subdir/TODO
/TODO

# ignore all files in any directory named build
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory and any of its subdirectories
doc/**/*.pdf
```

**NOTE**: [Gitignore Github repo](https://github.com/github/gitignore) exhaustive gitignore list

---

## References

* [Pro Git](https://git-scm.com/book/en/v2)
