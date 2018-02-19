from nip.utils.packaging import parse_version_string


def test_parse_version_string():
    expected = '1.1.0'
    actual = parse_version_string('v1.1.0').public

    assert actual == expected
