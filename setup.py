import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vector_library",
    version="0.0.6",
    author="dilshan97",
    author_email="projects.dilshan@gmail.com",
    description="Handle the 2D and 3D vector operations",
    long_description=long_description, 
    long_description_content_type="text/markdown",
    url="https://github.com/Dilshan1997/python-vector-operation-library",
    project_urls={
        "Bug Tracker": "https://github.com/Dilshan1997/python-vector-operation-library-issue",
        "Repository": "https://github.com/Dilshan1997/python-vector-operation-library"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.0"
)
