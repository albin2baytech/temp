from setuptools import setup
import os

setup(
    name="FaceProject",
    version="0.1.1",
    description="attendance system based on face",
    author="albin_jegus",
    py_modules="FaceProject",
    install_requires=["numpy"],
    entry_points="""[console_scipts] face=face-recon:__main__""")