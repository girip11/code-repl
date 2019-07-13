# Migration generation, deletion, rollback notes


## How to delete/revert generated migrations?
* To revert the changes introduced by `rails generate model` using the below command
  ```Bash
  # To undo all changes made by raisl generate model command
  rails destroy model ModelName column1:type Column2:type
  ```

## How to apply a specific migration?
* To **apply** a specific migration
  ```Bash
  rake db:migrate:up VERSION=20100627185630
  ```
* To revert the last two migrations and then migrate to the most current version:
  ```Bash
  rake db:migrate:redo STEP=2
  ```

## How to rollback migrations?

* To **rollback** a specific migration. Helps to rollback a migration thats out of order.
  ```bash
  # version contains the migration version to rollback
  rake db:migrate:down VERSION=20100905201547
  ```

* To rollback last n migrations.
  ```Bash
  # rollsback the last migration
  rake db:rollback STEP=1

  # rollsback the last n migrations
  # n is the number of migrations to rollback from the latest migration.
  rake db:rollback STEP=5
  ```

* Rollback all migrations till a specific migration (rollsback the target migration as well).
  ```bash
  rake db:migrate VERSION=20100905201547
  ```


## Reference
* [Rollback migration Stackoverflow](https://stackoverflow.com/questions/3647685/how-to-rollback-a-specific-migration)
* [Migrate or revert only some migrations](https://makandracards.com/makandra/845-migrate-or-revert-only-some-migrations)
* [Undoing things in rails](https://www.learneroo.com/modules/137/nodes/769)