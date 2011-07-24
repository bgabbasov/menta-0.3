# Setup script for package for windows demo
#
from distutils.core import setup
import py2exe

setup(name="metafor",
      windows=["MetaforGUI.py"]
      )
