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
