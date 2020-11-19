import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="concept_drift",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="concept drift detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blablahaha/concept-drift",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
