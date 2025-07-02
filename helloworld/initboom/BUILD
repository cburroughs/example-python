python_sources(
    sources=[*python_sources.sources.default, "!hello.py"],
)

python_sources(
    name="hello",
    sources=["hello.py"],
    overrides={
        "hello.py": {"dependencies": ["!./__init__.py"]},
    },
)
