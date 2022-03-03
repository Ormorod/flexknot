import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="linf",
    version="0.2.1",
    author="Adam Neil Ormondroyd",
    author_email="adam.ormondroyd@gmail.com",
    description="Linear INterpolation Functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ormorod/linf",
    packages=["linf"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licence :: TODO",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
        "scipy",
        "pypolychord @ git+https://github.com/Ormorod/PolyChordLite@master",
    ],
)
