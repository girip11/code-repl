# Bench Architecture

Bench is a CLI tool to install frappe based apps, sites on \*nix based systems

Quick reference guide on bench is available [here](https://github.com/frappe/bench/wiki/Quick-Reference-Guide)

## Bench useful commands

Each bench instance is a python virtual environment. `bench --help` command is used as reference for bench commands.

```Bash
#  creates a new bench. Creates a bench instance inside the directory "bench_instance_dir_name"
# init command fails if the bench instance directory already exists
bench init "bench_instance_dir_name" --python python3

#  to migrate existing bench instance which is in python 2.7 to python3
bench migrate-env python3

# adding a site
bench new-site "site_name"

# creating a new app
bench new-app "app_name"

# adding remote frappe app
bench get-app "app_name" "app_url"

# installing app to a site
bench --site "site_name" install-app "app_name"

# starting the bench with all development processes in Procfile
bench start
```

When a new bench instance is created using python3, the python virtual environment with python3 is setup. Inside the new bench instance directory, **pip** and **python** point to python3.

## Bench manager - GUI for Bench

`bench setup manager` installs bench manager. Bench manager itself is a **site**.

## Running Database migrations

```Bash
bench migrate
```

## Launching mariadb console from bench

```Bash
bench mariadb

# for postgres console use below
bench postgres
```

## Launching console

```Bash
# before executing this fix the site using `bench use site`
bench console
```

## Execute python function

```Bash
# help on execute command
bench execute --help
```

## References

- [Bench architecture](https://frappe.io/docs/user/en/tutorial/bench)
- [bench installation and usage](https://github.com/frappe/bench)
- [bench python3 migration](https://discuss.erpnext.com/t/erpnext-python-3/33492)
