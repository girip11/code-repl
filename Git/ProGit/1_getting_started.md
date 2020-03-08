# Git Getting started

## Git

Git is a distributed version control system. Git stores the changes as snapshots with every commit.

* Most of the operations are local
* Provides integrity through checksum. SHA-1 hash a 40 character string computed based on the contents of the file or directory structure. Git stores evrything in its database by this hash.
* Most operations on git add data to its database.

## Three states in git

* **committed** - data in git's local database
* **modified** - changes made in the file but not yet committed.
* **staged** - marked the current version of the file for commit.

## Three sections of git project

Based on the above states, git contains the following sections

* **working directory** - data in this section will be usually in the modified(ex: existing file got change) or untracked state(ex: new files got created)

* **staging area or the index** - data in this section will be in the staged state

* **.git directory** - data in this section will be in the committed state.

### **.git** directory

* contain metadata and object database.
* copied to target on `git clone`

### Working directory

* Checkout version of the project. contains files pulled from git's compressed database.

### Staging area

* File stored in the **.git** directory that stores information on what will be committed on next commit.

## Installation on Linux

```bash
sudo apt install -y git-all
git --version
```

## Git configuration

## System wide configuration

* applies to all users and git repositories
* accessed with command `git config --system`
* configuration file can be found at **/etc/gitconfig**

### User specific configuration

* applies to all repositories of the user
* accessed with command `git config --global`
* configuration file can be found at **$HOME/.gitconfig** or at **$HOME/.config/git/config**

### Repository level configuration

* applies only to that repository
* accessed with command `git config --local`
* configuration file can be found at **.git/config**
* Without any scope specified, this is the default place where the configuration is stored

Settings precedence

* repo level
* user level
* system level

```Bash
git config --list --show-origin

# to get a specific setting value
git config user.email

# to know the source of the setting
git config --show-origin core.editor
```

## Basic configuration settings

```Bash
git config --global user.name "John Doe"
git config --global user.email "johndoe@example.com"

# On Ubuntu
git config --global core.editor "gedit --wait"

# On 64-bit Windows usnig notepad++
git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe'
-multiInst -nosession"
```

## Git help

```Bash
# git help <verb>
git help config

# or man git-<verb>
man git-config

# for concise help using -h or --help
git config -h
```

---

## References

* [Pro Git](https://git-scm.com/book/en/v2)
