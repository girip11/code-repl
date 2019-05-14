# Ruby setup on VSCode in Ubuntu 18.04
This tutorial guides you to setup ruby in Ubuntu 18.04 with visual studio code as the IDE. Visual studio code can be easily installed from **Ubuntu Software Center**.

## Ruby installation on Ubuntu 18.04 using apt package manager

* Update the package manager with the below command  
    `sudo apt update` 

* Install ruby latest stable version using the following command  
    `sudo apt install ruby-full`

* Verify the ruby installation with the following command

* Install the following gems. With "ruby-debug-ide" we are installing the ruby debugger, that can be used with visual studio code. The below versions of gems will work well together.
    ```bash
    sudo gem install rake -v 12.3.2
    # Debugger
    sudo gem install ruby-debug-ide -v 0.6.0  
    sudo gem install debase -v 0.2.2

    # Static code analyzer
    sudo gem install rubocop
    sudo gem install rubocop-performance 
    ```

## Add VSCode config to Ruby project
* Install **Ruby extendsion by Peng Lv** in visual studio code to get the ruby language support.

* Create a directory **HelloRuby** and add a file **main.rb** to the directory. Type the following ruby code to the file. Save the file.
  ```ruby
    puts "Hello Ruby"
    puts "Hello World"
  ```

* Go to the debugger view of VS Code and hit the gear icon. Choose Ruby or Ruby Debugger from the prompt window, then you'll get the sample launch config in .vscode/launch.json. Json with ruby debugger configuration would look like the below json.
```JSON
{
    "version": "0.2.0",
    "configurations": [{
            "name": "Debug Local File",
            "type": "Ruby",
            "request": "launch",
            "program": "${file}"
        }

    ]
}
```

* Launch the debugging from the debugger view. Use F9 to set the breakpoints.

# References
* [Ruby on VSCode](https://medium.com/@terrenceong/ruby-development-with-vs-code-fab258db5f1d)
* [Debugger Installation](https://github.com/rubyide/vscode-ruby/wiki/1.-Debugger-Installation)