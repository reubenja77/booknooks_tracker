# booknooks_tracker







## MoSCoW Prioritisation

| Priority           |  User Story (summary)                         |   Notes/Acceptance Highlights                                         |
|--------------------|-----------------------------------------------|-----------------------------------------------------------------------|
| **Must**           |   Register & log in                           |   Users can sign up, log in/out; secure auth; redirect after log in.  |
| **Must**           |   Add a new book (title, author, notes)       |   Required fields validated; links books to the logged-in owner.      |
| **Must**           |   View my book list                           |   Only shows books owned by current user.                             |
| **Must**           |   Edit a book                                 |   Update title,/author/notes; redirects back to list on success.      |
| **Must**           |   Delete a book                               |   Owner-only delete with confirmation; redirects after delete.        |
| **Must**           |   Admin access                                |   Staff can manage users/books via Django Admin.                      |
| **Should**         |   Search my books (title/author)              |   Search bar filters current user's books.                            |
| **Should**         |   Set stauts: To Read / Reading / Finished    |   Status field on form; persisted per books.                          |
| **Should**         |   Filter by status                            |   Lists can be filtered by status; works with search.                 |
| **Could**          |   Upload a cover image                        |   Optional image; placeholder if missing; thumbnail in list.          |
| **Could**          |   Rate books (1-5)                            |   Rating stored per user; display list/detail.                        |
| **Could**          |   Export my books as CSV                      |   CSV contains key fields for current user's collection only.         |
| **Won't**          |   In-App purchasing / bookstore integration   |   Out of scope: payments/e-commerce not needed for this project.      |
| **Won't**          |   Social sharing of book lists                |   Out of scope: social integrations reserved for future versions.     |
| **Won't**          |   Goodreads / Kindle import / export          |   Out of scope: third-party API integration not needed for project.   |
| **Won't**          |   AI recommendation                           |   Out of scope: ML/AI recommendations not required for project.       |




## Testing

The **BookNooks Tracker App** includes automated tests for all *Must-Have* user stories.
Tests are written using Django's built-in test framework and includes unit tests for MUST_HAVE features (add, list, edit, delete books; authentication; ownership checks).

### How to Run Tests

From the project root (same level as `manage.py`):

```bash
python3 manage.py test books -v 2


Example test run:

Ran 11 tests in 16.706s

OK

Other tests conducted were:

# Create flow
python3 manage.py test books.tests.test_book_create -v 2

# List flow
python3 manage.py test books.tests.test_book_list -v 2

# Update/Delete flow
python3 manage.py test books.tests.test_book_update_delete -v 2