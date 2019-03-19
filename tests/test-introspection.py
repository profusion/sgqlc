import sgqlc.introspection


def test_variables():
    assert sgqlc.introspection.variables() == {
        'includeDescription': True,
        'includeDeprecated': True,
    }
    assert sgqlc.introspection.variables(True, False) == {
        'includeDescription': True,
        'includeDeprecated': False,
    }
    assert sgqlc.introspection.variables(False, True) == {
        'includeDescription': False,
        'includeDeprecated': True,
    }
