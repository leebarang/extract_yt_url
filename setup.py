import setuptools

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="extract_yt_url",
    version="0.0.1",
    author="leebarang", # author_email="xxx@xxx.com",
    description="A training package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leebarang/extract_yt_url",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.12.1",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows 11 64bit",
    ],
    python_requires='>=3.6',
)