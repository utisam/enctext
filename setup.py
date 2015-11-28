from setuptools import setup, find_packages

setup(
    name = 'enctext',
    version = '0.1',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    install_requires = [
        'pycrypto',
        'pbkdf2',
    ],
    entry_points = {
        'console_scripts': [
            'vienc = enctext.vienc:main',
        ],
    },
    author = 'Masatoshi Tsushima',
    author_email = 'utisam@gmail.com',
    description = 'Tools for editing encrypted text',
    license = 'License :: OSI Approved :: MIT License',
    keywords = 'Security'
)
