# How to set the visula studio code for ruby language

* Ruby installation using rbenv is recommended. Steps to install ruby using rbenv is [here](https://www.digitalocean.com/community/tutorials/how-to-install-ruby-on-rails-with-rbenv-on-ubuntu-18-04)

* Install the following ruby gems or add these gems to the **Gemfile** if using bundler.
  - ruby-debug-ide
  - debase
  - solargraph
  - rubocop
  Entries to add in the Gemfile under **development** group
  ```Ruby
    gem 'debase', require: false
		gem 'rubocop', require: false
		gem 'rubocop-performance', require: false
    gem 'ruby-debug-ide', require: false
    gem 'solargraph', require: false
  ```

* Install the vscode extension [**Ruby by Peng Lv**](https://marketplace.visualstudio.com/items?itemName=rebornix.Ruby). This extension provides ruby language support.

* Install [**Ruby solargraph by castwide**](https://github.com/castwide/solargraph). This extension provides intellisense, code formatting, go to definitions, code completion etc. Place the below solargraph settings in teh vscode workspace that contains the **Gemfile**. Since we use bundler for gem dependency management, useBundler setting is enabled in solargraph. Hence we need to have the Gemfile to be available in the root of the vscode workspace. So it is recommended to create a workspace for each rails project.
```
	"settings": {
		"ruby.lint": {
			// "rubocop": {
			// 	"lint": true, //enable all lint cops.
			// 	"only": [ /* array: Run only the specified cop(s) and/or cops in the specified departments. */ ],
			// 	"except": [ /* array: Run all cops enabled by configuration except the specified cop(s) and/or departments. */ ],
			// 	"forceExclusion": true, //Add --force-exclusion option
			// 	"require": [ /* array: Require Ruby files. */ ],
			// 	"rails": true //Run extra rails cops
			// }
		},
		"[ruby]": {
			"editor.formatOnSave": true
		},
		"editor.formatOnSaveTimeout": 1500,
		"editor.tabSize": 2,
		"editor.fontSize": 16,
		"terminal.integrated.rendererType": "dom",
		//"ruby.format": "rubocop", // formatting is enabled in solargraph
		"ruby.codeCompletion": false,
		"ruby.intellisense": false,
		"solargraph.useBundler": true,
		"solargraph.bundlerPath": "<PATH TO BUNDLER EXE>" //Ex: "/home/girish/.rbenv/versions/2.5.1/lib/ruby/gems/2.5.0/gems/bundler-2.0.1/exe/bundle"
		"solargraph.diagnostics": true,
		"solargraph.completion": true,
		"solargraph.definitions": true,
		"solargraph.formatting": true,  // solargraph also uses rubocop.
		"solargraph.references": true,
		"solargraph.hover": true,
		"solargraph.autoformat": true,
		"solargraph.rename": true,
		"solargraph.checkGemVersion": false,
		"solargraph.symbols": true,
		"ruby.lintDebounceTime": 500
  }
```
* To debug rails application, add the following debug configuration to launch.json inside the .vscode directory  in the workspace.
  ```
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
* In the workspace root, in the terminal type `bundle exec solargraph config .` (if bundler is set to true). This command generates **.solargraph.yml** file. Update the settings.
  ```YML
		---
		include:
		- "**/*.rb"
		exclude:
		- spec/**/*
		- test/**/*
		- vendor/**/*
		- ".bundle/**/*"
		- gem/**/*
		require: []
		domains: []
		reporters:
		- rubocop
		- require_not_found
		plugins: 
		- runtime
		require_paths: []
		max_files: 5000
	```