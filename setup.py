from setuptools import setup

setup(
    name='nose-descriptionfixer',
    author='Nat Williams',
    author_email='nat.williams@gmail.com',
    version='0.1',
    description=('A Nose plugin to fix the way tests are described when the '
                 'verbose flag (-v) is used'),
    entry_points={
        'nose.plugins.0.10': [
            'descriptionfixer = description_fixer:DescriptionFixer',
        ]
    },
    py_modules = ['description_fixer'],
)

