from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Kenworthy',
    url='https://github.com/mkenworthy/kenworthy',
    author='Matthew Kenworthy',
    author_email='matthew.kenworthy@gmail.com',
    # Needed to actually package something
    packages=['kenworthy'],
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Mostly astronomy routines for extrasolar planets and exoring',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
