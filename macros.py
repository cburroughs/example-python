def python_310_and_37_sources(**kwargs):
    kwargs.pop("interpreter_constraints", None)
    kwargs.pop("resolve", None)

    name = kwargs.pop("name", "")
    if name:
        name = name + "_"

    python_sources(
        name=f"{name}py37",
        resolve="def37",
        interpreter_constraints=["CPython>=3.7.1,<3.8"],
        **kwargs,
    )

    python_sources(
        name=f"{name}py310",
        resolve="default",
        interpreter_constraints=["CPython==3.10.*"],
        **kwargs,
    )


def python_310_and_37_tests(**kwargs):
    kwargs.pop("interpreter_constraints", None)
    kwargs.pop("resolve", None)

    name = kwargs.pop("name", "")
    if name:
        name = name + "_"

    python_tests(
        name=f"{name}py37",
        resolve="def37",
        interpreter_constraints=["CPython>=3.7.1,<3.8"],
        **kwargs,
    )

    python_tests(
        name=f"{name}py310",
        resolve="default",
        interpreter_constraints=["CPython==3.10.*"],
        **kwargs,
    )
