import setuptools

setuptools.setup(
    name="file-base-src",
    version="1.0.0",
    install_requires=[
        "PyYaml",
    ],
    url="https://github.com/JunNakamura/file-base-python-batch",
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
)