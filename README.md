# PSQL_py
Assignment I had to do for my database course I attended in University. The instructions were:

Create a java program, or a python if you prefer, that connects to your database and performs the following operations
in order:
1. Drops the two tables from the database if they already exist.
2. Creates the two tables as described above.
3. Generates 1 million (random) tuples, so that each tuple has a different value for the height attribute, and insert
them into the table Professor. Make sure that the last inserted tuple, and only that, has the value 185 for the
height attribute.
4. Generates 1 more million (random) tuples and inserts them in the table Course.
5. Retrieves from the database and prints to stderr all the id of the 1 million professors.
6. Updates all tuples that have value 185 as height and makes them to have a height equal to 200 – (your query
should work even if there are many tuples that have value 185 in the attribute height).
7. Selects from the table Professor and prints to the stderr the id and the address of the professors with
height 200.
8. Creates a B+tree index on the attribute height.
9. Retrieves from the database and prints to the stderr the id of the 1 million professors.
10. Updates all the tuples that have value 200 as height and makes them to have a height equal to 210 -- (your
query should work even if there are many tuples that have value 200 in the attribute height).
11. Selects from the table Professor and prints to the stderr the id and the address of the professor with height
210.
