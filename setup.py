from setuptools import setup
from create_django_skeleton import __version__

setup(
    version=__version__,
    name='create-django-skeleton',
    packages=['create_django_skeleton'],
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
    create-django-skeleton=create_django_skeleton:main
    '''
)
