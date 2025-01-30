# pytest-
pytest as a testing framework.

Tests are defined as functions prefixed with test_ and contain one or more statements that assert.

Tests are put in files of the form test_example.py or example_test.py, and are usually placed in a directory called tests in a root.

pip install pytest

To run = python -m pytest

*Pytest Fixture = decorating it with @pytest.fixture
Fixtures define the steps and data that constitute the arrange phase of a test. 
In pytest, they are functions you define that purpose. They can also be used to define a test’s act.

