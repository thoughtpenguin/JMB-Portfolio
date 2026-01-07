# James Berndt's Portfolio
Welcome to my portfolio!  This project contains examples of automated tests and is meant to give the viewer an idea of how I approach automation.

## Contact Information
Email: [jamesmberndt@gmail.com](mailto:jamesmberndt@gmail.com)
LinkedIn: [James Berndt](https://www.linkedin.com/in/james-berndt-a3317337/)
  
## Credentials
In the interest of security, credentials are not stored in this repository.

For Selenium tests, the credentials can be found at [https://the-internet.herokuapp.com/](https://the-internet.herokuapp.com/).

## Dependencies
All of the tests in this project are created using [pytest](https://docs.pytest.org/) library.
All of the dependencies for this project are linked in pyproject.toml using [Poetry](https://python-poetry.org/). Any library that can install dependencies from .toml files should be able to install the dependencies for this project.
## API Testing
The API tests in this project test different APIs that are freely available.

All of the API tests in this project can be executed by running the RunAPITests.py script in the root directory.Running this script will create a result HTML file in the root directory called APIResults.html.

## Selenium Testing
The Selenium tests in this project are for [https://the-internet.herokuapp.com/](https://the-internet.herokuapp.com/). This website contains a variety of different web scenarios that can be encountered when created automated web tests.

All of the Selenium tests in this project can be executed by running the RunSeleniumTests.py script in the root directory.  Running this script will create a result HTML file in the root directory called SeleniumResults.html.