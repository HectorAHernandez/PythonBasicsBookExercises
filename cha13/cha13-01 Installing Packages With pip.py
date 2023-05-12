# *****    IMPORTANT NOTES:
# WHEN USING VIRTUAL ENVIRONMENT AND INSTALLING NEW PACKAGES, THESE PACKAGES
# WILL BE AVAILABLE WHILE EXECUTING THE PYTHON PROGRAMS FROM THE ACTIVATED
# VIRTUAL ENVIRONMENT (venv), If we try to run the program from the Pythn IDLE
# Shell, then we will get the error: "from 'module/package' name import
#         classname ModuleNotFoundError: No module named 'module/package'". i.e:
# "from bs4 import BeautifulSoup ModuleNotFoundError: No module named 'bs4'"
# if we run the program from the activated venv directory with the command:
# python program_namy.py then it will run okay, because the package was
# installed in the venv.
# Now, if we also want to run the program in the Python IDLE shell, then we need
# to run this command in the venv to open en new IDLE from the venv and
# therefore have all the installed packages available: python -m idlelib.idle
# example:
# (web_scraping) PS C:\Python...\cha16\Web..._Project> python -m idlelib.idle


# # 13. Installing packages with pip:
# """ pip is the de facto package manager for Python.
# pip is included in the Python install after version 3.4.
# In this chapter I will learn:
# 1- How to install and manage third-party package with pip.
# 2- What the benefits and risks of third-party packages.

# pip is a command-line tool. That means we must run it from a command-line prompt
# or a Terminal program. for example, in Windows: cmd.

# To very your pip installation issue this command:
# command--> C:\Users\ssshh>python -m pip --version
# Response:
# pip 22.3.1 from C:\Users\ssshh\AppData\Local\Programs\Python\Python39\lib\site-packages\pip (python 3.9)
# This output indicates that pip version 22.3.1 is currently installed and is
# linked to the Python 3.9 installation.

# Upgrading pip to the Latest Version:
# command--> C:\Users\ssshh>python -m pip install --upgrade pip
# Response:py
# Requirement already satisfied: pip in c:\users\ssshh\appdata\local\programs\python\python39\lib\site-packages (22.3.1)
# Collecting pip
#   Downloading pip-23.0.1-py3-none-any.whl (2.1 MB)
#      ---------------------------------------- 2.1/2.1 MB 2.8 MB/s eta 0:00:00
# Installing collected packages: pip
#   Attempting uninstall: pip
#     Found existing installation: pip 22.3.1
#     Uninstalling pip-22.3.1:
#       Successfully uninstalled pip-22.3.1

# The corresponding commands in macOS are (using python3 instead of python):
# $ python3 -m pip --version
# $ python3 -m pip install --upgrade pip


# *** List all installed packages:
# C:\Users\ssshh>python -m pip list
# Response -->
# Package                Version
# ---------------------- ---------
# allure-pytest          2.8.6
# allure-python-commons  2.8.6
# ansicon                1.89.0
# atomicwrites           1.3.0
# attrs                  19.3.0
# blessed                1.19.1
# certifi                2020.12.5
# chardet                3.0.4
# charset-normalizer     2.0.12
# colorama               0.4.1
# configparser           4.0.2
# ...
# requests               2.27.1
# selenium               3.141.0
# setuptools             56.0.0
# six                    1.13.0
# toml                   0.10.2
# urllib3                1.26.6
# wcwidth                0.1.7
# webdriver-manager      3.4.0
# xlrd                   1.2.0
# zipp                   0.6.0

# setuptools: is a package used by pip to setup and install other packages.


# *** Installing a Package: "requets"
# C:\Users\ssshh>python -m pip install requests

# Notice that pip first tells you that it is "Collecting requets" You'll see the
# URL that pip is installing the package from, as well as a progress bar indicating
# the progress of the download.

# After that, you'll see taht pip install four more packages: chardet, certifi,
# idna, and urllib3. These packages are DEPENDECIES of requests. That means that
# requests requires these packages to be installed for it o work properly.

# By default, pip installs the latest version of a package. You can control which
# version of a package gets installed with some optinal version specifiers.

# Install Specific Package Version With Version Specifiers:
# There are several ways to control which version of a package gets installed.
# For example, we can:
# 1- Install the latest version greater than some version number.
# 2- Install the latest version les than some version number.
# 3- Install a specific version number.

# To install the latest version of "requests" package whose version is 2 or
# greater, we can execute:
# C:\Users\ssshh>python -m pip install requests>=2.0

# Notice the >=2.0 after the package name requests. This tells pip to install the
# latest version of requests that is greater than or equal to version 2.0

# The symbol >= is called a "version specifier" because it specifies which version
# of the package should be installed. There are different version specifiers that
# we can use. Here are the most widely used ones:
# Version
# Specifier     Description
# ---------     ------------
# <=, >=        Inclusive less than and greater specifier.
# <, >          Exclusive less than and greater specifier.
# ==            Exactly equal to specifier.

# Example:
# 1- To install the latest version that is less than or equal to some number:
# C:\Users\ssshh>python -m pip install requests<=3.0
# The system cannot find the file specified.

# 2- Install the latest verson of requests that is strictly less than version 3.0
# C:\Users\ssshh>python -m pip install requests<3.0
# The system cannot find the file specified.

# 3- We can combine version specifiers to ensure pip installs the latest version
# within a specified version reange. For example, to install the latest version of
# requests in the 1.0 series:
# C:\Users\ssshh>python -m pip install requests>=1.0,<2
# The system cannot find the file specified.

# You would use someting like the above command if your project was only compatible
# with the 1.0 series of the package and you want to make sure you install the
# lates updates to that series.
# """
# 4- Finally, we can pin dependencies to a specific version with the == version
# specifier:
# C:\Users\ssshh>python -m pip install requests==2.22.0
# Collecting requests==2.22.0
#   Using cached requests-2.22.0-py2.py3-none-any.whl (57 kB)
# Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
#   Using cached urllib3-1.25.11-py2.py3-none-any.whl (127 kB)
# Requirement already satisfied: chardet<3.1.0,>=3.0.2 in c:\users\ssshh\appdata\local\programs\python\python39\lib\site-packages (from requests==2.22.0) (3.0.4)
# Requirement already satisfied: certifi>=2017.4.17 in c:\users\ssshh\appdata\local\programs\python\python39\lib\site-packages (from requests==2.22.0) (2020.12.5)
# Requirement already satisfied: idna<2.9,>=2.5 in c:\users\ssshh\appdata\local\programs\python\python39\lib\site-packages (from requests==2.22.0) (2.8)
# Installing collected packages: urllib3, requests
#   Attempting uninstall: urllib3
#     Found existing installation: urllib3 1.26.6
#     Uninstalling urllib3-1.26.6:
#       Successfully uninstalled urllib3-1.26.6
#   Attempting uninstall: requests
#     Found existing installation: requests 2.27.1
#     Uninstalling requests-2.27.1:
#       Successfully uninstalled requests-2.27.1
# Successfully installed requests-2.22.0 urllib3-1.25.11

# Now the current versions related to requests:
# C:\Users\ssshh>python -m pip list
# Package                Version
# ---------------------- ---------
# certifi                2020.12.5
# chardet                3.0.4
# idna                   2.8
# requests               2.22.0
# urllib3                1.25.11


# Now reinstall the latest version of requests:
# C:\Users\ssshh>python -m pip install requests==2.27.1
# Collecting requests==2.27.1
#   Using cached requests-2.27.1-py2.py3-none-any.whl (63 kB)
# Requirement already satisfied: certifi>=2017.4.17 in c:\users\ssshh\appdata\local\programs\python\python39\lib\site-packages (from requests==2.27.1) (2020.12.5)
# Requirement already satisfied: charset-normalizer~=2.0.0 in c:\users\ssshh\appdata\local\programs\python\python39\lib\site-packages (from requests==2.27.1) (2.0.12)
# Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\ssshh\appdata\local\programs\python\python39\lib\site-packages (from requests==2.27.1) (1.25.11)
# Requirement already satisfied: idna<4,>=2.5 in c:\users\ssshh\appdata\local\programs\python\python39\lib\site-packages (from requests==2.27.1) (2.8)
# Installing collected packages: requests
#   Attempting uninstall: requests
#     Found existing installation: requests 2.22.0
#     Uninstalling requests-2.22.0:
#       Successfully uninstalled requests-2.22.0
# Successfully installed requests-2.27.1

# Again the current versions related to requests:
# C:\Users\ssshh>python -m pip list
# Package                Version
# ---------------------- ---------
# certifi                2020.12.5
# chardet                3.0.4
# idna                   2.8
# requests               2.27.1
# urllib3                1.25.11

# """

# *** Show Package Request:
# Now that we've installed the requests package, we canuse pip to view some
# details about the package:
# C:\Users\ssshh>python -m pip show requests
# Name: requests
# Version: 2.27.1
# Summary: Python HTTP for Humans.
# Home-page: https://requests.readthedocs.io
# Author: Kenneth Reitz
# Author-email: me@kennethreitz.org
# License: Apache 2.0
# Location: c:\users\ssshh\appdata\local\programs\python\python39\lib\site-packages
# Requires: certifi, charset-normalizer, idna, urllib3
# Required-by: webdriver-manager

# the "python -m pip show xxx" command displays information about an installed
# package, including the author's name and email and a home page you can navigate
# to in your Internet browser to learn more about what the package does.

# The requests package is used for making HTTP requests from a Python program. It
# is extremely useful in a variety of domains and i a dependency of a large
# number of other Python packages.


# *** Uninstall a Package:
# Let's uninstall the requests package:
# C:\Users\ssshh>python -m pip uninstall requests

# Found existing installation: requests 2.27.1
# Uninstalling requests-2.27.1:
#   Would remove:
#     c:\users\ssshh\appdata\local\programs\python\python39\lib\site-packages\requests-2.27.1.dist-info\*
#     c:\users\ssshh\appdata\local\programs\python\python39\lib\site-packages\requests\*
# Proceed (Y/n)? y
#   Successfully uninstalled requests-2.27.1

# Before pip actually removes anything from your computer, it asks for your
# permission first.
# Type y and press Enter to continue. You should see the confirmation message.
# """
# Notice that pip uninstalled requests, but id did not remove any of its
# dependencies! This behavior is a feature, not a bug. Imagine that you have
# installed several packages into your environment with pip, some of which share
# dependencies. If pip uninstalled a package and its dependencies, then it would
# render any other packages requiring those dependencies unusable!

# We can uninstall multiple package with one command:
# python -m pip uninstall requests certifi chardet idna urllib3


# Python's ecosystem of third-party packages is one of its greatest strengths.
# These packages allow Python programmers to be highly productive and create
# full-featured software much more quickly than can be done in, say, a language
# like C++.

# That said, using third-party packages in your code introduces several concerns
# that must be addressed with care.

# *** The Pitfalls of Third-Party Packages:
# The beauty of third-party packages is that they give you the ability to add
# functionality to your project without having to implement every-thing from
# scratch. This offers massive boosts in productivity.
# But with great power comes great responsibility. As soon as you include someone
# else's package in your project, you are placing an enormous amount of trust in
# those responsible for developing and maintaining the package.

# By using a package you did not develop, you lose control over certain aspects of
# your project. In particular, the maintainers of the package may release a new
# version that introduces changes that are incompatible with the version to use in
# your project.

# By default, pip installs the latest release of a package, so if you distribute
# your code to someone else and they install a newer version of a package required
# by your project, then they may not be able to run your code.

# This presents a significant challenge for both you and the end user.
# Fortunately, Python comes with a fix for this all-too-commons problem: virtual
# environments.

# A virtual environment creates an isolated and, most importantly, reproducible
# environment that you can use to develop a project. The environment can contain
# an specific version of Python as well as specific versions of project's
# dependencies.

# When you distribute your code to someone else, they can reproduce this
# environment and be confident that they can run your code without error.
# """
# Virtual environments are more advance topic that is outside the scope of this
# book. To learn more about virtual environments and how to use them, check out
# Real Python's Managing, Python Dependencies With Pip and Virtual Environment
# course at: https://realpython.com/products/managing-python-dependencies/ In it
# you will learn how to:
# 1- Install, use, and manage third-party Python packages with the pip package
# manager on Windows, macOS, and Linux in more details than presented here.

# 2- Isolate project dependencies wih virtual environment to avoid version
# conflicts in your Python projects.

# 3- Apply a complete serve-steps workflow for finding and identifying quality
# third-party packages to use in our own Python projects (and for justifying your
# decisions to your team or manager)

# 4- Set up repeatable development environments and application deployments using
# the pip package manager and requirements files.

# The Managing Python Dependencies With Pip and Virtual Environments course is
# a great next step for when you complete this book.

#
