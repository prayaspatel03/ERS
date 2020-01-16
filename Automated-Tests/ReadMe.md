# Automated-tests

Automated test framework for the API testing

## Prepare to run tests

### Install dependencies (on the host machine for tests, not the target API server)

1. python 3

   check you have right version installed using `python3 --version` and you should have `Python 3.x`, and install otherwise

2. behave
    `pip3 install behave`
    @todo figure out how to get this into path, but for now
    (find better way; note your path may vary depending on output from pip3 install behave)

    ~~~cmd
    set PATH=C:\Users\lewis\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\LocalCache\local-packages\Python37\Scripts;%PATH%
    ~~~

### Prepare the API server

- you must have a username (for now with Admin privileges) enabled in the json config list of users on that server. 
  That username must correspond to the configuration (for now behave.ini) field username
- Be sure to enable the TestMode::Enabled flag to true

## Running tests

### Run all tests

1. Setup CONFIGURATION to say what server to target (HOW TODO - DISCUSS). PROBABLY CREATE CONFIG FILES AND MAKE THAT ARGUMENT TO runtests.bat

2. `runtests.bat` to run list of tests mentioned in "runtests.bat" file or use `behave` to run all tests

### Run specific test

1. `behave features/slides.feature`

   (or whatever feature you find in the features folder)
