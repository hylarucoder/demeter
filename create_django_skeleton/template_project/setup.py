from setuptools import setup
from template_project import __version__

setup(
    version=__version__,
    name='template_project',
    packages=['template_project'],
    include_package_data=True,
    install_requires=[
        'pyyaml',
        'jinja2',
        'click',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points='''
    [console_scripts]
    template_project=template_project:main
    '''
)
