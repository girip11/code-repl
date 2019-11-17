# Setting up VSCode for ruby and rails projects

* Ruby installation using rbenv is recommended. Steps to install ruby using rbenv is [here](./install_ruby_ubuntu.md)

## Setting up development environment using bundler

**Gemfile** contents.

~~~ruby
# frozen_string_literal: true

source "https://rubygems.org"

ruby "2.5.1"

gem "debase", require: false
gem "ruby-debug-ide", require: false

# mry stands for - Migrate Rubocop YAML
gem "mry", require: false

# advanced ruby repl console
gem "pry", require: false
# for rails projects
# gem "pry-rails", require: false

gem "rcodetools", require: false
gem "rubocop", "~> 0.70.0", require: false
gem "rubocop-github", "~> 0.13.0", require: false
gem "rubocop-performance", "~> 1.3.0", require: false

# code formatting
gem "prettier", require: false

# For rails project
# gem "rubocop-rails", require: false

gem "solargraph", require: false
~~~

Execute `bundle install --path <GEM_INSTALLATION_PATH>` to install these dependencies. Bundler configuration will be present in `.bundle/config` file. Sample bundler configuration file

~~~Conf
---
BUNDLE_PATH: "./gem/dependencies/"
BUNDLE_DISABLE_SHARED_GEMS: "true"
~~~

## VSCode Extensions

* [Ruby vscode extension](https://marketplace.visualstudio.com/items?itemName=rebornix.Ruby) for ruby language support.

* [Solargraph extension](https://marketplace.visualstudio.com/items?itemName=castwide.solargraph) for intellisense.

* [Ruby symbols](https://marketplace.visualstudio.com/items?itemName=miguel-savignano.ruby-symbols)

* [Endwise in ruby](https://marketplace.visualstudio.com/items?itemName=kaiwood.endwise) to wisely add `end` in urby

* [Slim language support](https://marketplace.visualstudio.com/items?itemName=sianglim.slim) **if using slim templating** in rails application.

* [Prettier Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) for ruby code formatting.

* [Run On Save](https://marketplace.visualstudio.com/items?itemName=emeraldwalk.RunOnSave) to trigger ruby prettier formatting on saving the file.

## VSCode workspace configuration

~~~JSON
{
  "folders": [
    {
      "path": "."
    }
  ],
  "settings": {
    "[ruby]": {
      "editor.formatOnSave": true
    },
    "editor.tabSize": 2,
    "editor.fontSize": 16,
    "terminal.integrated.rendererType": "dom",
    //
    "ruby.useBundler": true,
    "ruby.pathToBundler": "bundle",
    "ruby.useLanguageServer": true,
    "ruby.lint": {
      "rubocop": {
        "useBundler": true
      }
    },
    "ruby.format": false,

    // format using prettier after ruby source file save
    "emeraldwalk.runonsave": {
      "commands": [
        {
          "match": "\\.rb$",
          // "cmd": "echo ${file}",
          "cmd": "bundle exec rbprettier --write '${file}'",
          "isAsync": false
        }
      ]
    },
    "ruby.lintDebounceTime": 1000,

    // intellisense
    "ruby.codeCompletion": "rcodetools",
    "ruby.intellisense": "rubyLocate",

    // solargraph intellisense
    "solargraph.useBundler": true,
    "solargraph.bundlerPath": "bundle",
    "git.autorefresh": true
  }
}
~~~

## Configuring prettier for formatting

In the root folder(ruby workspace folder) create a file `.prettierrc.json` and add the following contents to it

~~~JSON
{
  "preferSingleQuotes": false,
  "printWidth": 100,
  "addTrailingCommas": true
}
~~~

## Configuring solargraph for intellisense

* [**Ruby solargraph by castwide**](https://github.com/castwide/solargraph) extension provides intellisense, go to definitions, code completion etc.

* In the workspace root, in the terminal type `bundle exec solargraph config .` (if bundler is set to true). This command generates **.solargraph.yml** file. Given below is a sample settings for a rails application.

  ```YAML
  ---
  include:
    - "**/*.rb"
  exclude:
    - spec/**/*
    - test/**/*
    - vendor/**/*
    - ".bundle/**/*"
    - tmp/**/*
    - node_modules/**/*
    - log/**/*
  # required ges for the rails application
  require:
    - actioncable
    - actionmailer
    - actionpack
    - actionview
    - activejob
    - activemodel
    - activerecord
    - activestorage
    - activesupport
    - rails
  domains: []
  reporters:
    - rubocop
    - require_not_found
  plugins:
    - runtime
  require_paths: []
  max_files: 10000
  ```

## Configuring rubocop for linting

```YAML
# RUBOCOP configuration
---
# Reference: https://rubocop.readthedocs.io/en/latest/configuration/

inherit_gem:
  rubocop-github:
    - config/default.yml
    - config/rails.yml

AllCops:
  # The same version would be picked up from .ruby-version
  TargetRubyVersion: 2.5.1
```

## VSCode ruby debug configuration

Go to the debugger view of VS Code and hit the gear icon. Choose Ruby or Ruby Debugger from the prompt window, then you'll get the sample launch config in .vscode/launch.json. Json with ruby debugger configuration would look like the below json.

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

* Launch the debugging from the debugger view. Use **F9** to set the breakpoints.

## VSCode rails debug configuration

To debug rails application, add the following debug configuration to `launch.json` inside the `.vscode` directory in the workspace.

```JSON
{
// Use IntelliSense to learn about possible attributes.
// Hover to view descriptions of existing attributes.
// For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
"version": "0.2.0",
"configurations": [{
  "name": "Rails server",
  "type": "Ruby",
  "request": "launch",
  "program": "${workspaceRoot}/bin/rails",
  "args": [
    "server"
  ],
    "useBundler": true
  }]
}
```

---

## References

* [Ruby on VSCode](https://medium.com/@terrenceong/ruby-development-with-vs-code-fab258db5f1d)
* [Debugger Installation](https://github.com/rubyide/vscode-ruby/wiki/1.-Debugger-Installation)
