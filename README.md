# James Berndt's Portfolio
Welcome to my portfolio!  This project contains examples of automated tests and is meant to give the viewer an idea of how I approach automation.

All of the tests can be run through GitHub actions; the tests can either be run individually through the action of the kind of test (e.g. Run Selenium Test) or they can all be run at once (Run All Tests).

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

### Keanu Reeves Whoa API

The tests here show I approach testing of an API when an item can be retrieved through an API, but additional information is needed.

`test_whoa_retrieval` in [test_keanu_reeves_whoa.py](https://github.com/thoughtpenguin/JMB-Portfolio/blob/main/APITests/test_keanu_reeves_whoa.py) whos how I test it for this API: I first retrieve a random `whoa` (I promise that this is a technical term). I then retrieve the list of movies that contains a 'whoa'.  From there, I am able to retrieve a random `whoa` from each movie that occurs before the initial random `whoa`.  Since each `whoa` object contains information about the movie contains it (e.g. the count of `whoas` in the movie), I am able to calculate the `whoa` index.

### Open Library API
The tests for this API show how I approach development of the intitial tests for an API focusing on validation of the data type that is returned in the response payload.

In this case, the response to the `https://openlibrary.org/search.json` endpoint contains a root field with several fields with types documented in the `SEARCH_EXPECTED_KEYS` constant oncluding the more complicated `docs` field.  The `docs` field contains a list of objects that should contain the fields documents in the `DOC_EXPECTED_KEYS` constant.  For validation, I cycle through all of the keys and fields for each type of object to confirm they are of the correct type.

I would consider these tests to be quicker tests to write.  There is room for improvement here: it would be better to use json schemas instead of constants since schemas are more nuanced, but for quick tests, this setup works well.

## Selenium Testing
The Selenium tests in this project are for [https://the-internet.herokuapp.com/](https://the-internet.herokuapp.com/). This website contains a variety of different web scenarios that can be encountered when created automated web tests.

### Add and Remove Elements
In this test, I am testing functionality that adds and removes buttons from a web page.  I confirm the page loads, test adding a button, test removing a button, and test adding and removing buttons several times to confirm that the number of buttons at the end of the worklfow is equal to the number of actions performed.

### Basic Authentication
Included in this module are tests of basic authentication.  Since credential can be passed in through the URL with basic authentication, that is the primary means of testing for this functionality. A few different combinations of valid and invalid credentials are run through here.

Chrome does not allow Selenium to interact with the login alert for security reasons.  As a result, the alert dismissals have to be skipped in this test.

### Broken Images

On this test page, two images are intentionally broken. I took the opportunity on this test to demonstrate test failues. The first and second images are broken, so those test cases should failed. The first test confirms how many image tags are on the page and the last test confirms that the third image is not broken.