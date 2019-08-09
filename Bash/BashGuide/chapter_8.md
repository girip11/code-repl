# Chapetr-8: Globs
Globs are not regular expressions. These are wildcards for searching files. Glob characters helps in pathname expansion.
If one of the below characters appear, then the word is considered as a pattern and is replaced with matching files sorted alphabetically.

## Glob characters
* **?** - matches a single character (wildcard character)
* **\*** - matches any number of characters (wildcard string)
* **[]** - matches for a list of characters or ranges (wildcard list)

## **?** glob
```Bash
# list all the file in the current directory
ls 'doc?.md'
```

## **\*** glob
```Bash
# prints all files/folders in the current folder
echo *

# removes all the files in the current directory
rm *
```

**NOTE**: Neither of the above mentioned wilcards match **/**.

## **[]** glob
```Bash
# any number of individual characters
# match any file/folder inside /usr/bin starting with either e or g or p followed by any number of characters
ls /usr/bin/[egp]*

# range example. range also matches a single character only with a range of values
ls /usr/bin/[a-z]*

# negation. Matches files/folders beginning with any characters(not just alphabets) other than from e-l. 
ls /usr/bin/[^e-l]*

# special characters like itself in the pattern [] requires escaping
ls /usr/bin/*[\[]
```

## null globs
when a glob doesnot match a filenames, glob matches itself (i.e) glob expands to itself. But if nullglob shell option is enabled, **the glob incase fo no match expands to null instead of itself.**
```Bash
for file in *.txt
do
  echo "$file"
done

# when no files match *.txt found, still *.txt itself is printed.
# problematic in conditions, loops where we check if atleast one file exists.
```

**nullglob** can be enabled/set using the shell option `shopt -s nullglob`

**nullglob** can be disabled/unset using the shell option `shopt -u nullglob`

## dot glob
if this shell option is set, bash includes the files startgin with **.** in the results of pathname expansion.
```Bash
# enabling dotglob
shopt -s dotglob

# disabling dotglob
shopt -u dotglob
```

## Extended globs
Extended globs allow for pattern matching, while normal globs allow for matching individual characters.
```Bash
# enabling extglob
shopt -s extglob

# disabling dotglob
shopt -u extglob
```

Extended glob matching patterns
* **?(list)** - matches zero or one occurence of the patterns
* **\*(list)** - matches zero or many occurence of the patterns
* **+(list)** - matches atleast one occurence of the patterns
* **@(list)** - matches exactly one occurence of the patterns
* **!(list)** - matches anything other than the patterns mentioned.

---

## References:
* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)
* [nullglob](https://www.cyberciti.biz/faq/bash-shell-check-for-any-mp3-files-in-directory/)
