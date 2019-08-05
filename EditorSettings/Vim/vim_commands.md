# VIM (**V**i **IM**proved)
VIM is a text editor. **gvim** it its GUI counterpart with menus

## Installation
```BASH
sudo apt update
sudo apt install vim

# alternatively you can use gvim
```

## Frequently used commands
**i** - insert mode. We can edit the text file in this mode.
**ESC** - switches to normal mode where commands can be issued to save file, quit editor etc
**:w** - when in normal mode, this command performs file save
**:q** - quit editor
**:q!** - quit editor without saving(writing to file)
**ZZ** or **:wq** - save(write) file and quit
**x** or **Delete key** - delete a character
**X** or **backspace key** - deletion in backspace mode.
**u** - undo
**Ctrl + R** - redo
**yy** - copy a line
**dd** - delete a line
**p** - paste buffer content
**[[** - beginning of the file
**]]** - end of the file

## References:
* [VIM common commands](https://linuxhandbook.com/basic-vim-commands/)
* [VIM commands radford](https://www.radford.edu/~mhtay/CPSC120/VIM_Editor_Commands.htm)