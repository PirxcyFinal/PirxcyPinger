import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="PirxcyPinger",
    version="3.2.1",
    author="Pirxcy",
    description="Async Tool For Uploading URL's To PirxcyPinger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pirxcypingerfinal.pirxcyfinal.repl.co/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'aiohttp'
      ],
)
