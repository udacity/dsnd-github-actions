def test_package_import():
    import package_name  # noqa: F401


def test_function_that_will_break():
    from package_name import function_that_will_break

    function_that_will_break()
