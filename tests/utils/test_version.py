from nip.utils.version import ensure_version_is_pep_compliant

def test_ensure_version_is_pep_compliant():
    expected = '1.1.0'
    actual = ensure_version_is_pep_compliant('v1.1.0').public

    assert actual == expected
