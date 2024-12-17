def test_package_import():
    import package_name  # noqa: F401


def test_failure():
    from package_name import a_function_that_will_break

    a_function_that_will_break()
