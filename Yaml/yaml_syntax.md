# YAML syntax

* Document start, end and comments
  ```YAML
  --- # YAML document start
    # Comments in YAML start with "#"
  ... # YAML document end
  ```

* Defining simple key value configuration settings using scalar values
  ```YAML
  ---
  thread_count: 5 # Integer value
  should_retry: true # boolean value
  description: 'This is a string value'
  text: "Double quotes can also be used to enclose string value"
  name: Girish # Quotes are optional

  100: 'Number can also be a key' # key can be anything and not restricted just to string
  3.14: pi
  ...
  ```

* String literal blocks and folded block
  ```YAML
  ---
  literal_block: |
      Whatever text goes inside this block retains its formatting, spacing and line breaks.
        In this value text, we can observer the formatting being retained.

  folded_block: >
      In the folded block, line breaks are converted to single spaces and blank lines to new line.

        More indented lines retains the new line as
          we can see with this text.
  ...
  ```

* Defining list, map and set
  ```YAML
  ---
  list_collection:
    - list_item1
    - list_item2
    - 100   # list is heterogeneous (supports different data types)
    - key: value  # key value pair is also an entry in the list
    - - - nested_list_item1
        - nested_list_item2
    - 
      - another_nested_list_item1
      - another_nested_list_item2

  map_collection:   # map is a collection of key value pairs.
    map_key1: map_value1
    map_key2: map_value2
    nested_map:
      nested_map_key1: value
      nested_map_key2: value

  # set contains only unique items.
  set_collection:
    ? set_item1
    ? set_item2

  # Set is a map with null value. So a set can also be defined as below
  another_set_collection:
    set_item1: null
    set_item2: null
  ...
  ```

* JSON style list, maps and sets.
  ```YAML
  ---
  # quotes are optional for strings
  json_list: ["a", b, 1 , 2]
  json_set: {"entry1", entry2, 'entry3'}
  json_map: {"key" : "value"}
  ... 
  ```

* Datetime type support
  ```YAML
  ---
  # YAML can understand ISO format datetime
  datetime: 2019-05-23T23:01:00.1Z
  date: 23-05-2019
  ...
  ```

* Specifying explicit types for values is possible YAML.
  ```YAML
  ---
  default_integer_data: 100 # value is integer type
  string_data: !!str 100  # value is a string type
  float_data: !!float 100 # value is a float now

  # alternate syntax
  integer_value: 100 # value is integer type
  string_value: (str) 100  # value is a string type
  float_value: (float) 100 # value is a float now
  float_as_int: (int) 123.45
  ...
  ```

* Anchor is one of the very salient features of YAML. Define anchor once for a value and use the anchor at otehr places which will substitute the original value.
  ```YAML
  ---
  # Anchor example.
  # Anchor is very handy when a particular setting value needs to be used at various places and when that value needs to be changed, instead of changing at all places changing the value at anchor definition would suffice
  default_city_value: &default_city Hyderabad

  student1:
    name: ABC
    city: *default_city # city will have the value "HYDERABAD"
  
  student2:
    name: XYZ
    city: *default_city # city will have the value "HYDERABAD"
  ...
  ```

* Using anchor for complex substitution. Very useful in reusing blocks of configuration
  ```YAML
  ---
  # defaults contain environment independent values
  defaults: &defaults
    key1: value
    key2: value

  # staging account credentials for instance
  staging: &staging
    staging_key1: value
    staging_key2: value

  # production account credentials
  prod: &staging
    prod_key1: value
    prod_key2: value
  
  # Development environment
  development:
    <<: *defaults # development map will have the key value entries from defaults map
    <<: *staging  # development map will have all the key value entries under staging map
    db_url: 'development_db_url'

  # Testing environment
  test:
    <<: *defaults
    <<: *staging
    db_url: 'test_db_url'

  # Production environment
  production:
    <<: *defaults
    <<: *prod
    db_url: 'prod_db_url'
  ...
  ```

* Complex types as key are usually prefixed with `?` followed by space. Not all language parsers support this.
  ```YAML
  ---
  # list as key
  ? - Item1
    - Item2
  : list items
  ...
  ```

## Reference:
* [YAML syntax](https://learnxinyminutes.com/docs/yaml/)
* [YAML type casting](https://github.com/yaml/YAML2/wiki/Type-casting)
* [YAML tryout online editor](https://codebeautify.org/yaml-validator)