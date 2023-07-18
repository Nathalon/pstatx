from setuptools import *

kwargs = {
    "author" : "Nathalon",
    "description" : "pstatx",
    "entry_points" : {"console_scripts" : ["pstatx=pstatx.pstatx:main"]},
    "license" : "GPL v3",
    "name" : "pstatx",
    "packages" : ["pstatx"],
    "version" : "V0.0.1",
    "url" : "https://github.com/Nathalon/pstatx.git"
}

setup(**kwargs)
