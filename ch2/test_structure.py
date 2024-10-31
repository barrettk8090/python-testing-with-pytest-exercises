from cards import Card


def test_to_dict():
    # GIVEN a Card object with known contents
    # Given/Arrange - a starting state. This is where you set up data or the environment to get ready for the action.
    c1 = Card("something", "brian", "todo", 123)

    # WHEN we call to_dict() on the object
    # When/Act - some action is performed. This is the focus of the test - the behavior we are trying to make sure is working right.
    c2 = c1.to_dict()

    # THEN the result will be a dictionary with known content
    # Then/Assert = some expected result or end state should happen. At the end of the test, we make sure the action resulted in the expected behavior.
    c2_expected = {
        "summary": "something",
        "owner": "brian",
        "state": "todo",
        "id": 123,
    }
    assert c2 == c2_expected
