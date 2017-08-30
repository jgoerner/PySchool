# Weekend Project "Boilerplating" :globe_with_meridians:

## Technical Requirements
This weekend's project should wrap up the topic of boilerplating with Python.
Since the two major subtopics are around Jjinja/Flas and Cookiecutter, two separate
mini-projects shall be implemented:

### Flask Templating
In order to get more familiar with the Jinja syntax, the Flask template should contain the majority of Jinja features, such as:
- [x] Statements (for loop)
- [x] Variables (users)
- [ ] Filters (backend via `request.args`)
- [ ] Tests
- [ ] Comments
- [ ] Template inheritance
- [ ] Super Blocks
- [ ] Control Structures `for` and `if`
- [ ] Macros

### Cookiecutter for containerized Flask App
The cookicutter template should aim to put the Flask app above into a containerized 
CI environment, where the user should be asked about the following Parameter:
- [ ] project name
- [ ] author
- [ ] description
- [ ] CI (Building, Testing, Coverage, Styling, Documentation, Hosting)
- [ ] (optional) Backend (e.g. via PostgreSQL vs. SQLite)
