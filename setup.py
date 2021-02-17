import setuptools

setuptools.setup(
    name='fileDuplicator',
    version='1.0.0',
    description='Duplicates files a certain number of times. Can use tokens to populate random person data.',
    # long_description=README,
    url='https://github.com/alexeby/FileDuplicator',
    author='Alex Eby',
    include_package_data=True,
    install_requires=[
        "requests"
    ],
    entry_points={'console_scripts': ['fileDuplicator=file_duplicator.__main__:main']},
)