# Loops

SIGINT -  Keyboard interrupt. `ctrl + c`
`kill -2 PID`

## While
```Bash
# Syntax
while condition
do 
  # Statements
done
```

## Until
until success(exit code 0) continues execution.
```Bash
until condition
do
  # Statements
done
```

## For
```Bash
for (( initial; condition; increment ))
do
  # statements
done

# iterate through al characters of a string
str="Hello"
for ((i=0; i< ${#str}; i++))
do
  echo "${str:$i:1}"
done

# Syntax for looping through a list
for item in list
do
  # statements
done

# example
for i in {0..9}
do
  echo $i
done
```

## Break
To jump out of loop (exit loop) use the **break** statement.

## Continue
To skip a loop iteration use the **continue** statement.

---

## References:
* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)