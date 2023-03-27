import json
from setuptools import setup, find_packages

NAME = "isilon-sdk"
VERSION = ""
REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
SETUP_README_PATH = "/sdkbuilder/SETUP_README.rst"

with open('version_config.json') as f:
    VERSION = json.load(f).get("sdk_version")

with open(SETUP_README_PATH, "r", encoding="utf-8") as readme_file:
    README = readme_file.read()

setup(
    name=NAME,
    version=VERSION,
    description="Python language bindings for managing OneFS clusters.",
    maintainer="Isilon SDK",
    maintainer_email="sdk@isilon.com",
    author="Isilon SDK",
    author_email="sdk@isilon.com",
    url="https://github.com/Isilon/isilon_sdk_python",
    keywords=["Swagger", "Isilon SDK", "OneFS", "PowerScale"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=README,
    project_urls={
        "Source code": "https://github.com/Isilon/isilon_sdk",
        "Documentation": "https://github.com/Isilon/isilon_sdk_python",
    },
    license='MIT',
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=2.7',
)
