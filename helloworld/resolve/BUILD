python_source(
    name='foo', # no error if this is 'resolve'
    source='foo.py')


python_source(
    name='bar',
    source='bar.py',
    dependencies=['!./foo.py'] # no error if this line is removed
)
