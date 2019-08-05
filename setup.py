import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
        name="example-pkg-martin-py",
        version="0.0.1",
        author="Martín Belda",
        author_email="mbelda@gmail.com",
        description="A small example package",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/alu0100832211/pypi-example",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            ],
        )
