# TodoApplication

Todo application with Postgres SQL database, Flask, SQLAlchemy ORM, psycopg2

### Challenge 

Finish implementing the ability to create, update (mark complete), and delete To-Do Lists on the app.

Create a List: Implement a Create List form above the list of To-Do Lists, much like we did for an individual To-Do item, to enable the user to create Lists.

Update a List (and all of its children items): Implement a Checkbox next to a To-Do List, and allow the user to mark an entire list as completed. When the list is marked completed, implement the controller so that all of its child items are also marked as completed. (hint: you can use list.todos and what we know about bulk deletions off the Query object to bulk delete all todo items for a given list).

Delete a List (and all of its children items): Implement an "x" remove button next to each List, and allow a user to click it in order to remove a List. When a list is removed, all of its child items should also be removed. We can set the cascade option to do this. See the SQLAlchemy Docs on Cascades. (Hint: you'll want to look into the all and delete-orphan cascade options).
