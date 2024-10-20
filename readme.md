
# Run demo Server
poetry run flask --app server.py run


# Run Tavern Test

## Using PyTest
poetry run tavern-ci test_server.tavern.yaml

## Using Tavern CLI
poetry run pytest

## Using Python
`
from tavern.core import run
from pytest import ExitCode

exit_code = run("test_server.tavern.yaml")

if exit_code != ExitCode.OK:
    print("Error running tests")
`

# Run Locust
poetry run locust -f locustfile.py --host http://localhost

