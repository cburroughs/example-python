# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# A macro that turns every entry in this directory's requirements.txt into a
# `python_requirement_library` target. Refer to
# https://www.pantsbuild.org/docs/python-third-party-dependencies.
python_requirements(name="reqs")

__defaults__(
    {
        (python_test, python_tests): dict(
            interpreter_constraints=parametrize(
                py37=["CPython==3.7.*"],
                py38=["CPython==3.8.*"],
                py39=["CPython==3.9.*"],
                py310=["CPython==3.10.*"],
                py311=["CPython==3.11.*"],
            )
        ),
    }
)
