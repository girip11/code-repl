# Installing Ruby on Ubuntu 18.04

This tutorial guides you to setup ruby in Ubuntu 18.04 with visual studio code as the IDE. Visual studio code can be easily installed from **Ubuntu Software Center**.

## Ruby installation on Ubuntu 18.04 using apt package manager

```bash
sudo apt update
# required version can also be specified
sudo apt install ruby-full
ruby --version
gem --version
gem env home
```

## Ruby installation using rbenv

~~~bash
sudo apt update

# install rbenv
sudo apt install rbenv
rbenv --version

# install ruby version
rbenv install 2.5.1

# make the ruby version as the global version
rbenv global 2.5.1

# check ruby installation
ruby --version
gem --version
gem env home
~~~

## Globally required gems for development

Install the following gems. With "ruby-debug-ide" we are installing the ruby debugger, that can be used with visual studio code. The below versions of gems will work well together.

```bash
gem install rake
gem install bundler

# advanced ruby repl console
gem install pry
# gem install pry-rails
```

## Configuring **irb**

Inside the ruby working directory (project directory) create a file **.irbrc** and paste the following code to it.

~~~ruby
# frozen_string_literal: true

require "irb/completion"

def module?(name)
  name.class.name.to_sym == :Module
end

def class_methods(class_name, inherited_methods = false)
  class_name.public_methods(inherited_methods).sort
end

def instance_methods(name, inherited_methods = false)
  name_type = name.class.name.to_sym

  if name_type == :Class ||
     name_type == :Module
    name.instance_methods(inherited_methods).sort
  else
    name.public_methods(inherited_methods).sort
  end
end

def ri(doc_for)
  puts `ri #{doc_for}`
end
~~~

---

## References

* [Ruby installation using rbenv](https://www.digitalocean.com/community/tutorials/how-to-install-ruby-on-rails-with-rbenv-on-ubuntu-18-04)
