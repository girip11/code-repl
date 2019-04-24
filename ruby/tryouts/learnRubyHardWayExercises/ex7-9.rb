# prints the string n times
puts '.' * 10
puts 'Girish' * 5

# print prints to console without new line at the end
print 'H' + 'e' + 'l' + 'l' + 'o' * 3
print 'H' + 'e' + 'l' + 'l' + 'o'

# Prints to console with new line after printing
puts 'H' + 'e' + 'l' + 'l' + 'o'
puts 'H' + 'e' + 'l' + 'l' + 'o'

# formatting %{} inside "".
# When format needs to be reused across messages, you define this
formatter = '%{one} %{two}'
puts format(formatter, one: 'one', two: 2.0)
puts format(formatter, one: 'First', two: 'Second')

# New line in the string
strWithNewLine = "Hello\nWorld"
puts strWithNewLine

# print as is. #{} inline expression wont work.
puts %q(
    This
    prints
    whatever
    the content
    inside
    as it is
    #{formatter}
)

# """ """ can be used to enclose string.
# behaves similar to double quotes,
# which means #{}, %{} would work
str = '' "
 This
   \"prints\"
    whatever
    the content
    inside
    as it is
    #{formatter}
" ''
puts str
puts format(str, one: 'G', two: 'P')
