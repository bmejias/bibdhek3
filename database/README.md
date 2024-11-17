# Database schema definition

First create the database `bibdhek` and the user `bibdhek`. The database is own
by user `bibdhek`. This is e.g. running with a unix user with the attribute to
create users and databases.

```bash
psql -p 5417 create_user_db
```

Connect to the database and set password with

```sql
\password bibdhek
```

Copy the password and database, username configuration to `.pgpass`

Create the schema with the `create_schema.sql` script.

```bash
psql -h localhost -p 5417 -d bibdhek -U bibdhek -f create_schema.sql 2> errors_schema.log
```

Verify that there are no errors in that log file

If you have some data for testing, run it with:

```bash
psql -h localhost -p 5417 -d bibdhek -U bibdhek -f test_data.sql 2> errors_data.log
```
