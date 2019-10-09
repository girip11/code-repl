# Command substitution

## Arithmetic Expansion

**(())** - This is arithmetic expression. **\$(())** is arithmetic expansion. In arithmetic expansion, **\$(())** is replaced with the result of the arithmetic expression.

```Bash
declare -i a=5 b=10 c=6
# arithmetic expansion
result=$(($a + $b * $c - 100))
echo "Computation result : $result"
echo $((a + b * c - 100)) # within arithmetic expression $ is option for referencing variable values.
unset a b c
```

Bash performs only **integer math**. Bash **doesnot** know about floats, long, doubles. For floating point arithmetic, we need to use external library like **bc**.

## Brace expansion

**{}** expands the character sequence present inside the braces. Can expand the sequences in ascending as well as descending order.

```Bash
echo {a..z}

# can be thought of like range function in programming languages.
for i in {0..20}
do
  echo $i
done

# character combination
echo {a..z}{a..z}
echo {1..2}{1..2}

echo {1,2}{1..3}

# empty item with {,}
echo {,1}{a..c} # outputs a b c 1a 1b 1c

# expand string with multiple prefixes
echo {a..z}hello
# above can be used with wildcard characters to expand to pathnames
echo {/etc,/lib}/*.so*
for file in {/etc,/lib}/*.so*
do
echo $file
done
```

## Command Substitution

**$()** or **``** - command substitution.

* creates a **subshell**, passes the expression inside **$()** or **``**, replaces the same with the stdout of the evaluated expression.
* **``** usage not recommended. Not POSIX compatible.

```Bash
echo $(pwd)
echo $(whoami)

# nesting in command substitution
# in the above command echo "user:$(whoami)" is
# executed in a subshell and the result user:xyz
# is returned and after replacement the statement looks like echo "user:xyz"
echo "$(echo "user:$(whoami)")"

# Inner echo prints the PID of the subshell and the BASHPID in the outer echo prints the PID of the current shell
echo $(echo $BASHPID) $BASHPID
```

---

## References

* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)
