# Chapter-6: Arrays

## Indexed Arrays

### Declaration and initialization
Array index starts from 0.
```Bash
# declares an empty array
array=()

# The below statement also declares an empty array
declare -a array

# declare and initialize array
environments=('development' 'test' 'production')

# declare and initialize with specific index
env=([1]="development" [2]="test" [3]="production")

# modifying/setting values in the array
array[0]="Item1"
array[1]="Item2"

# append elements to array
array+=('Item3' 'Item4')
echo $array
```

### Accessing array elements

Accessing array elements is done with the syntax `${array_name[index]}`
```Bash
# Various ways to access array elements
array=('Item1' 'Item2' 'Item3' 'Item4')
array[4]=' '
array[5]="Item5"

# prints the first item
echo ${array[0]}

# print the whole array
echo ${array[@]}
echo ${array[*]}

# print elements from starting index
# Syntax: ${array[@]:offset:num} or ${array[*]:offset:num}
# Start from offset index and print "num" of array elements.
echo ${array[@]:1:2}  # echo ${array[@]:1} prints all array elements starting from index 1
echo ${array[*]:1:2}

# difference between @ and * can be observed when quoted
declare -i count=0
# expands each item in the array and encloses it within quotes
for i in "${array[@]}"
do
echo "$i"
count+=1
done
# count should be same value as array size.
echo $count

count=0
# converts entire array content to one string enclosed within quotes with whitespace(empty elements) truncated
for i in "${array[*]}"
do
echo "$i"
count+=1
done
# count should always be 1.
echo $count
```

### Metadata (length and indexes)
```Bash
array=('Hello' 'foo' 'bar' 'welcome' 'home')

# print length of particular element in the array
echo ${#array[0]} # prints 5 which is length of 'Hello'

# print length of the array
echo ${#array[@]}
echo ${#array[*]}

# list all indexes in an array
echo ${!array[@]}
echo ${!array[*]}
```

### Deletion
```Bash
# all three below does unset the entire array
unset -v array
unset -v array[@]
unset -v array[*]

# unset/delete individual element
unset -v array[i]
```

## Associative arrays
key is a string in associative arrays. Key can be quoted or unquoted while using with associative arrays.

### Declaration
```bash
# declares assosiative array
declare -A array

# setting values
array['foo']='bar'

# setting multiple values
array=(['foo']='bar' ['key']='value')

```

### Accessing elements
```Bash
# access a particular element
echo "${array[foo]}"
echo "${array['foo']}"

# get associative array length
echo ${#array[@]}
echo ${#array[*]}

# access all the values 
echo "${array[@]}" # separate string
echo "${array[*]}" # combine to single string

# iterate through all the values
for value in "${array[@]}"
do
echo $value
done

# use * without quotes to iterate individually
for value in ${array[*]}
do
echo $value
done

# we cant use * when quoted to iterate through all the values, because all the values are combined to one big string.
declare -i count=0
for value in "${array[*]}"
do
echo $value
count+=1
done
echo $count

# get all the keys
for key in "${!array[@]}"
do
echo "$key:${array[$key]}"
echo "Key length: ${#key}"
echo "Value length: ${#array[$key]}"
done

# get all keys as single string
key_string=${!array[*]}
echo "$key_string"

# get length of value
echo "${#array['foo']}"
```

### Deletion
```Bash
# 
unset -v array
unset -v array[@]
unset -v array[*]

# delete particular element
unset -v array[foo]
unset -v array['foo']
```

---

## References:
* [Bash Guide by Joseph Deveau](https://www.amazon.in/BASH-Guide-Joseph-DeVeau-ebook/dp/B01F8AZ1LE/ref=sr_1_4?keywords=bash&qid=1564983319&s=digital-text&sr=1-4)