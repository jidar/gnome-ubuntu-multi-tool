from setuptools import setup, find_packages

setup(
    name='gumtool',
    version='0.0.1',
    description=(
        "A simple collection of tools that make running Gnome (3.10+) "
        "Ubuntu (14.04+) a little easier, especially on high-dpi hardware "
        "like the Retina MacbookPro."),
    author='Jose A. Idar',
    author_email='jose.idar@gmail.com',
    url='blog.thatjoseguy.com',
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
        ['gumtool = gumtool.cli:entry_point']}
    )
