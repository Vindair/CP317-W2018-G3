# CP317-W2018-G3

### Requirements Document
* Located at `documents/Subby-Requirements.md`
* Viewable at: https://rawgit.com/Kuresov/CP317-W2018-G3/master/documents/Subby-Requirements.md.html

### Developer Notes
#### Running Subby (Development)
  * Install PostgreSQL with the default admin user settings, reachable at localhost:
    * DB Name: subby
    * User: postgres
    * Password: postgres
    * Port: 5432
  * Ensure `python` and `pip` are installed (or the appropriate python 3.X and python3-pip for your platform). From the project directory, run `pip install -r requirements.txt`
  * From the project directory, run `python manage.py runserver --settings=subby_project.settings.development`. Subby will be running at `http://localhost:8000`

#### Required dependencies:
  * PostgreSQL
  * Python3 and supporting packages

#### Optional Dependencies:
  * Node + npm (for Markdown generation)

#### Tasks
  * `gulp markdown` will generate clean HTML from the .md files in `documents/`. Use this instead of editing the HTML directly to avoid losing changes.
