from setuptools import setup, find_packages

setup(
    name='gumt',
    version='0.0.1',
    description=(
        'Gnome Ubuntu Mac Tweaks: Simple collection of tweaks to make using '
        'a macbook with gnome ubuntu a little easier.'),
    author='Jose A. Idar',
    author_email='jose.idar@gmail.com',
    url='code.thatjoseguy.com',
    packages=find_packages(),
    install_requires=open('pip-requires').read(),
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
    entry_points = {
        'console_scripts':
        ['gumt = gumt.cli:entry_point']}
    )
