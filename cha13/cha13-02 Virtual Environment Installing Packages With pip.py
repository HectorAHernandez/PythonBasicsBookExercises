# *****    IMPORTANT NOTES:
# WHEN USING VIRTUAL ENVIRONMENT AND INSTALLING NEW PACKAGES, THESE PACKAGES
# WILL BE AVAILABLE WHILE EXECUTING THE PYTHON PROGRAMS FROM THE ACTIVATED
# VIRTUAL ENVIRONMENT (venv), If we try to run the program from the Python IDLE
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


# Tutorial Virtual Environment Creation and Concepts:
# """
# Python Virtual Environments: A Primer
# by Martin Breuss  Apr 13, 2022 105 Comments  devops intermediate tools
# Tweet Share Email
# Table of Contents

# How Can You Work With a Python Virtual Environment?
# Create It
# Activate It
# Install Packages Into It
# Deactivate It
# Why Do You Need Virtual Environments?
# Avoid System Pollution
# Sidestep Dependency Conflicts
# Minimize Reproducibility Issues
# Dodge Installation Privilege Lockouts
# What Is a Python Virtual Environment?
# A Folder Structure
# An Isolated Python Installation
# How Does a Virtual Environment Work?
# It Copies Structure and Files
# It Adapts the Prefix-Finding Process
# It Links Back to Your Standard Library
# It Modifies Your PYTHONPATH
# It Changes Your Shell PATH Variable on Activation
# It Runs From Anywhere With Absolute Paths
# How Can You Customize a Virtual Environment?
# Change the Command Prompt
# Overwrite Existing Environments
# Create Multiple Virtual Environments at Once
# Update the Core Dependencies
# Avoid Installing pip
# Include the System Site-Packages
# Copy or Link Your Executables
# Upgrade Your Python to Match the System Python
# What Other Popular Options Exist, Aside From venv?
# The Virtualenv Project
# The Conda Package and Environment Manager
# How Can You Manage Your Virtual Environments?
# Decide Where to Create Your Environment Folders
# Treat Them as Disposables
# Pin Your Dependencies
# Avoid Virtual Environments in Production
# Use Third-Party Tools
# Conclusion

#  Watch Now This tutorial has a related video course created by the Real Python team. Watch it together with the written tutorial to deepen your understanding: Working With Python Virtual Environments

# In this tutorial, you'll learn how to work with Python's venv module to create and manage separate virtual environments for your Python projects. Each environment can use different versions of package dependencies and Python. After you've learned to work with virtual environments, you'll know how to help other programmers reproduce your development setup, and you'll make sure that your projects never cause dependency conflicts for one another.

# By the end of this tutorial, you'll know how to:
# """

# #  Create and activate a Python virtual environment
# """Explain why you want to isolate external dependencies.
# Visualize what Python does when you create a virtual environment
# Customize your virtual environments using optional arguments to venv
# Deactivate and remove virtual environments
# Choose additional tools for managing your Python versions and virtual environments
# Virtual environments are a common and effective technique used in Python development. Gaining a better understanding of how they work, why you need them, and what you can do with them will help you master your Python programming workflow.

# Free Bonus: Click here to get access to a free 5-day class that shows you how to avoid common dependency management issues with tools like Pip, PyPI, Virtualenv, and requirements files.

# Throughout the tutorial, you can select code examples for either Windows, Ubuntu Linux, or macOS. Pick your platform at the top right of the relevant code blocks to get the commands that you need, and feel free to switch between your options if you want to learn how to work with Python virtual environments on other operating systems.

#  Take the Quiz: Test your knowledge with our interactive “Python Virtual Environments: A Primer” quiz. Upon completion you will receive a score so you can track your learning progress over time:


# How Can You Work With a Python Virtual Environment?
# If you just need to get a Python virtual environment up and running to continue working on your favorite project, then this section is the right place for you.

# The instructions in this tutorial use Python's venv module to create virtual environments. This module is part of Python's standard library, and it's the officially recommended way to create virtual environments since Python 3.5.

# Note: There are other great third-party tools for creating virtual environments, such as conda and virtualenv, that you can learn more about later in this tutorial. Any of these tools can help you set up a Python virtual environment.

# For basic usage, venv is an excellent choice because it already comes packaged with your Python installation. With that in mind, you're ready to create your first virtual environment in this tutorial.


# Create It
# Any time you're working on a Python project that uses external dependencies that you're installing with pip, it's best to first create a virtual environment:

# Windows
# Linux
# macOS
# PS> python -m venv venv
# If you're using Python on Windows and you haven't configured the PATH and PATHEXT variables, then you might need to provide the full path to your Python executable:

# PS> C:\Users\Name\AppData\Local\Programs\Python\Python310\python -m venv venv
# The system path shown above assumes that you installed Python 3.10 using the Windows installer provided by the Python downloads page. The path to the Python executable on your system might be different. Working with PowerShell, you can find the path using the where.exe python command.

# Activate It
# Great! Now your project has its own virtual environment. Generally, before you start using it, you'll first activate the environment by executing a script that comes with the installation:

# Windows
# Linux + macOS
# PS> venv\Scripts\activate
# (venv) PS>
# Before you run this command, make sure that you're in the folder that contains the virtual environment you just created.

# Note: You can also work with your virtual environment without activating it. To do this,
# you'll provide the full path to its Python interpreter when executing a command. However,
# most commonly, you'll want to activate the virtual environment after creating it to save yourself the effort of repeatedly having to type long paths.

# Once you can see the name of your virtual environment—in this case (venv)—in your command prompt, then you know that your virtual environment is active. You're all set and ready to install your external packages!

# Install Packages Into It
# After creating and activating your virtual environment, you can now install any external dependencies that you need for your project:

# Windows
# Linux + macOS
# (venv) PS> python -m pip install <package-name>
# This command is the default command that you should use to install external Python packages with pip. Because you first created and activated the virtual environment, pip will install the packages in an isolated location.

# Note: Because you've created your virtual environment using a version of Python 3, you don't need to call python3 or pip3 explicitly. As long as your virtual environment is active, python and pip link to the same executable files that python3 and pip3 do.

# Congratulations, you can now install your packages to your virtual environment. To get to this point, you began by creating a Python virtual environment named venv and then activated it in your current shell session.

# As long as you don't close your terminal, every Python package that you'll install will end up in this isolated environment instead of your global Python site-packages. That means you can now work on your Python project without worrying about dependency conflicts.

# Deactivate It
# Once you're done working with this virtual environment, you can deactivate it:

# Windows
# Linux + macOS
# (venv) PS> deactivate
# PS>
# After executing the deactivate command, your command prompt returns to normal. This change means that you've exited your virtual environment. If you interact with Python or pip now, you'll interact with your globally configured Python environment.

# If you want to go back into a virtual environment that you've created before, you again need to run the activate script of that virtual environment.

# Note: Before installing a package, look for the name of your virtual environment within parentheses just before your command prompt. In the example above, the name of the environment is venv.

# If the name shows up, then you know that your virtual environment is active, and you can install your external dependencies. If you don't see the name in your command prompt, remember to activate your Python virtual environment before installing any packages.

# At this point, you've covered the essentials of working with Python virtual environments. If that's all you need, then happy trails as you continue creating!

# However, if you want to know what exactly just happened, why so many tutorials ask you to create a virtual environment in the first place, and what a Python virtual environment really is, then keep on reading! You're about to go deep!


# Why Do You Need Virtual Environments?
# Nearly everyone in the Python community suggests that you use virtual environments for all your projects. But why? If you want to find out why you need to set up a Python virtual environment in the first place, then this is the right section for you.

# The short answer is that Python isn't great at dependency management. If you're not specific, then pip will place all the external packages that you install in a folder called site-packages/ in your base Python installation.


# Several issues can come up if all of your external packages land in the same folder. In this section, you'll learn more about them, as well as other problems that virtual environments mitigate.

# Avoid System Pollution
# Linux and macOS come preinstalled with a version of Python that the operating system uses for internal tasks.

# If you install packages to your operating system's global Python, these packages will mix with the system-relevant packages. This mix-up could have unexpected side effects on tasks crucial to your operating system's normal behavior.

# Additionally, if you update your operating system, then the packages you installed might get overwritten and lost. You don't want either of those headaches to happen!

# Sidestep Dependency Conflicts
# One of your projects might require a different version of an external library than another one. If you have only one place to install packages, then you can't work with two different versions of the same library. This is one of the most common reasons for the recommendation to use a Python virtual environment.

# To better understand why this is so important, imagine you're building Django websites for two different clients. One client is comfortable with their existing web app, which you initially built using Django 2.2.26, and that client refuses to update their project to a modern Django version. Another client wants you to include async functionality in their website, which is only available starting from Django 4.0.

# If you installed Django globally, you could only have one of the two versions installed:

# Windows
# Linux + macOS
# PS> python -m pip install django==2.2.26
# PS> python -m pip list
# Package    Version
# ---------- -------
# Django     2.2.26
# pip        22.0.4
# pytz       2022.1
# setuptools 58.1.0
# sqlparse   0.4.2

# PS> python -m pip install django==4.0.3
# PS> python -m pip list
# Package    Version
# ---------- -------
# asgiref    3.5.0
# Django     4.0.3
# pip        22.0.4
# pytz       2022.1
# setuptools 58.1.0
# sqlparse   0.4.2
# tzdata     2022.1
# If you install two different versions of the same package into your global Python environment, the second installation overwrites the first one. For the same reason, having a single virtual environment for both clients won't work either. You can't have two different versions of the same package in a single Python environment.

# Looks like you won't be able to work on one of the two projects with this setup! However, if you create a virtual environment for each of your clients' projects, then you can install a different version of Django into each of them:

# Windows
# Linux + macOS
# PS> mkdir client-old
# PS> cd client-old
# PS> python -m venv venv --prompt="client-old"
# PS> venv\Scripts\activate
# (client-old) PS> python -m pip install django==2.2.26
# (client-old) PS> python -m pip list
# Package    Version
# ---------- -------
# Django     2.2.26
# pip        22.0.4
# pytz       2022.1
# setuptools 58.1.0
# sqlparse   0.4.2
# (client-old) PS> deactivate

# PS> cd ..
# PS> mkdir client-new
# PS> cd client-new
# PS> python -m venv venv --prompt="client-new"
# PS> venv\Scripts\activate
# (client-new) PS> python -m pip install django==4.0.3
# (client-new) PS> python -m pip list
# Package    Version
# ---------- -------
# asgiref    3.5.0
# Django     4.0.3
# pip        22.0.4
# setuptools 58.1.0
# sqlparse   0.4.2
# tzdata     2022.1
# (client-new) PS> deactivate
# If you now activate either of the two virtual environments, then you'll notice that it still holds its own specific version of Django. The two environments also have different dependencies, and each only contains the dependencies necessary for that version of Django.

# With this setup, you can activate one environment when you work on one project and another when you work on another. Now you can keep any number of clients happy at the same time!


# Minimize Reproducibility Issues
# If all your packages live in one location, then it'll be difficult to only pin dependencies that are relevant for a single project.

# If you've worked with Python for a while, then your global Python environment might already include all sorts of third-party packages. If that's not the case, then pat yourself on the back! You've probably installed a new version of Python recently, or you already know how to handle virtual environments to avoid system pollution.

# To clarify what reproducibility issues you can encounter when sharing a Python environment across multiple projects, you'll look into an example situation next. Imagine you've worked on two independent projects over the past month:

# A web scraping project with Beautiful Soup
# A Flask application
# Unaware of virtual environments, you installed all necessary packages into your global Python environment:

# Windows
# Linux + macOS
# PS> python -m pip install beautifulsoup4 requests
# PS> python -m pip install flask
# Your Flask app has turned out to be quite helpful, so other developers want to work on it as well. They need to reproduce the environment that you used for working on it. You want to go ahead and pin your dependencies so that you can share your project online:

# Windows
# Linux + macOS
# PS> python -m pip freeze
# beautifulsoup4==4.10.0
# certifi==2021.10.8
# charset-normalizer==2.0.12
# click==8.0.4
# colorama==0.4.4
# Flask==2.0.3
# idna==3.3
# itsdangerous==2.1.1
# Jinja2==3.0.3
# MarkupSafe==2.1.1
# requests==2.27.1
# soupsieve==2.3.1
# urllib3==1.26.9
# Werkzeug==2.0.3
# Which of these packages are relevant for your Flask app, and which ones are here because of your web scraping project? It's hard to tell when all external dependencies live in a single bucket.

# With a single environment like this one, you'd have to manually go through the dependencies and know which are necessary for your project and which aren't. At best, this approach is tedious, but more likely, it's error prone.

# If you use a separate virtual environment for each of your projects, then it'll be more straightforward to read the project requirements from your pinned dependencies. That means you can share your success when you develop a great app, making it possible for others to collaborate with you!

# Dodge Installation Privilege Lockouts
# Finally, you may need administrator privileges on a computer to install packages into the host Python's site-packages directory. In a corporate work environment, you most likely won't have that level of access to the machine that you're working on.

# If you use virtual environments, then you create a new installation location within the scope of your user privileges, which allows you to install and work with external packages.

# Whether you're coding as a hobby on your own machine, developing websites for clients, or working in a corporate environment, using a virtual environment will save you lots of grief in the long run.

# What Is a Python Virtual Environment?
# At this point, you're convinced that you want to work with virtual environments. Great, but what are you working with when you use a virtual environment? If you want to understand what Python virtual environments are, then this is the right section for you.

# The short answer is that a Python virtual environment is a folder structure that gives you everything you need to run a lightweight yet isolated Python environment.


# A Folder Structure
# When you create a new virtual environment using the venv module, Python creates a self-contained folder structure and copies or symlinks the Python executable files into that folder structure.

# You don't need to dig deeply into this folder structure to learn more about what virtual environments are made of. In just a bit, you'll carefully scrape off the topsoil and investigate the high-level structures that you uncover.

# However, if you've already got your shovel ready and you're itching to dig, then open the collapsible section below:


# A virtual environment folder contains a lot of files and folders, but you might notice that most of what makes this tree structure so long rests inside the site-packages/ folder. If you trim down the subfolders and files in there, you end up with a tree structure that isn't too overwhelming:

# Windows
# Linux
# macOS
# venv\
# │
# ├── Include\
# │
# ├── Lib\
# │   │
# │   └── site-packages\
# │       │
# │       ├── _distutils_hack\
# │       │
# │       ├── pip\
# │       │
# │       ├── pip-22.0.4.dist-info\
# │       │
# │       ├── pkg_resources\
# │       │
# │       ├── setuptools\
# │       │
# │       ├── setuptools-58.1.0.dist-info\
# │       │
# │       └── distutils-precedence.pth
# │
# │
# ├── Scripts\
# │   ├── Activate.ps1
# │   ├── activate
# │   ├── activate.bat
# │   ├── deactivate.bat
# │   ├── pip.exe
# │   ├── pip3.10.exe
# │   ├── pip3.exe
# │   ├── python.exe
# │   └── pythonw.exe
# │
# └── pyvenv.cfg
# This reduced tree structure gives you a better overview of what's going on in your virtual environment folder:

# Windows
# Linux
# macOS
# Include\ is an initially empty folder that Python uses to include C header files for packages you might install that depend on C extensions.

# Lib\ contains the site-packages\ folder, which is one of the main reasons for creating your virtual environment. This folder is where you'll install external packages that you want to use within your virtual environment. By default, your virtual environment comes preinstalled with two dependencies, pip and setuptools. You'll learn more about them in a bit.

# Scripts\ contains the executable files of your virtual environment. Most notable are the Python interpreter (python.exe), the pip executable (pip.exe), and the activation script for your virtual environment, which comes in a couple of different flavors to allow you to work with different shells. In this tutorial, you've used activate, which handles the activation of your virtual environment for Windows across most shells.

# pyvenv.cfg is a crucial file for your virtual environment. It contains only a couple of key-value pairs that Python uses to set variables in the sys module that determine which Python interpreter and which site-packages directory the current Python session will use. You'll learn more about the settings in this file when you read about how a virtual environment works.

# From this bird's-eye view of the contents of your virtual environment folder, you can zoom out even further to discover that there are three essential parts of a Python virtual environment:

# A copy or a symlink of the Python binary
# A pyvenv.cfg file
# A site-packages directory
# The installed packages inside site-packages/ are optional but come as a reasonable default. However, your virtual environment would still be a valid virtual environment if this directory were empty, and there are ways to create it without installing any dependencies.

# With the default settings, venv will install both pip and setuptools. Using pip is the recommended way to install packages in Python, and setuptools is a dependency for pip. Because installing other packages is the most common use case for Python virtual environments, you'll want to have access to pip.

# You can double-check that Python installed both pip and setuptools into your virtual environment by using pip list:

# Windows
# Linux + macOS
# (venv) PS> python -m pip list
# Package    Version
# ---------- -------
# pip        22.0.4
# setuptools 58.1.0
# Your version numbers may differ, but this output confirms that Python installed both packages when you created the virtual environment with its default settings.

# Note: Below that output, pip might also display a warning that you're not using the latest version of the module. Don't worry about it yet. Later, you'll learn more about why this happens and how to automatically update pip when creating your virtual environment.

# These two installed packages make up most of the content of your new virtual environment. However, you'll notice that there are also a couple of other folders in the site-packages/ directory:

# The _distutils_hack/ module, in a manner true to its name, ensures that when performing package installations, Python picks the local ._distutils submodule of setuptools over the standard library's distutils module.

# The pkg_resources/ module helps applications discover plugins automatically and allows Python packages to access their resource files. It's distributed together with setuptools.

# The {name}-{version}.dist-info/ directories for pip and setuptools contain package distribution information that exists to record information about installed packages.

# Finally, there's also a file named distutils-precedence.pth. This file helps set the path precedence for distutils imports and works together with _distutils_hack to ensure that Python prefers the version of distutils that comes bundled with setuptools over the built-in one.

# Note: You're learning about these additional files and folders for the sake of completeness. You won't need to remember them to effectively work with your virtual environments. It's enough to keep in mind that any preinstalled packages in your site-packages/ directory are standard tools that make installing other packages more user-friendly.

# At this point, you've seen all the files and folders that make up a Python virtual environment if you've installed it using the built-in venv module.

# Keep in mind that your virtual environment is just a folder structure, which means that you can delete and re-create it anytime you want to. But why this specific folder structure, and what does it make possible?


# An Isolated Python Installation
# Python virtual environments aim to provide a lightweight, isolated Python environment that you can quickly create and then discard when you don't need it anymore. The folder structure that you've seen above makes that possible by providing three key pieces:

# A copy or a symlink of the Python binary
# A pyvenv.cfg file
# A site-packages directory
# You want to achieve an isolated environment so that any external packages you install won't conflict with global site-packages. What venv does to make this possible is to reproduce the folder structure that a standard Python installation creates.

# This structure accounts for the location of the copy or symlink of the Python binary and the site-packages directory, where Python installs external packages.

# Note: Whether or not the Python executable in your virtual environment is a copy or a symlink of the Python executable that you've based the environment on depends primarily on your operating system.

# Windows and Linux may create symlinks instead of copies, while macOS always creates a copy. You can try to influence the default behavior with optional arguments when creating the virtual environment. However, you won't have to worry about it in most standard cases.

# In addition to the Python binary and the site-packages directory, you get the pyvenv.cfg file. It's a small file that contains only a couple of key-value pairs. However, these settings are crucial for making your virtual environment work:

# Windows
# Linux
# macOS
# home = C:\Users\Name\AppData\Local\Programs\Python\Python310
# include-system-site-packages = false
# version = 3.10.3
# You'll learn more about this file in a later section when reading about how a virtual environment works.

# Suppose you closely inspect your newly minted virtual environment's folder structure. In that case, you might notice that this lightweight installation doesn't contain any of the trusted standard library modules. Some might say that Python without its standard library is like a toy car without batteries!

# However, if you start the Python interpreter from within your virtual environment, then you can still access all the goodies from the standard library:

# >>> import urllib
# >>> from pprint import pp
# >>> pp(dir(urllib))
# ['__builtins__',
#  '__cached__',
#  '__doc__',
#  '__file__',
#  '__loader__',
#  '__name__',
#  '__package__',
#  '__path__',
#  '__spec__']
# In the example code snippet above, you've successfully imported both the urllib module and the pp() shortcut from the pretty print module. Then you used dir() to inspect the urllib module.

# Both modules are part of the standard library, so how come you have access to them even though they're not in the folder structure of your Python virtual environment?

# You can access Python's standard library modules because your virtual environment reuses Python's built-ins and the standard library modules from the Python installation from which you created your virtual environment. In a later section, you'll learn how the virtual environment achieves linking to your base Python's standard library.

# Note: Because you always need an existing Python installation to create your virtual environment, venv opts to reuse the existing standard library modules to avoid the overhead of copying them into your new virtual environment. This intentional decision speeds up the creation of virtual environments and makes them more lightweight, as described in the motivation for PEP 405.

# In addition to the standard library modules, you can optionally give your virtual environment access to the base installation's site-packages through an argument when creating the environment:

# Windows
# Linux + macOS
# PS C:\> python -m venv venv --system-site-packages
# If you add --system-site-packages when you call venv, Python will set the value to include-system-site-packages in pyvenv.cfg to true. This setting means that you can use any external packages that you installed to your base Python as if you'd installed them into your virtual environment.

# This connection works in only one direction. Even if you give your virtual environment access to the source Python's site-packages folder, any new packages you install into your virtual environment won't mingle with the packages there. Python will respect the isolated nature of installations to your virtual environment and place them into the separate site-packages directory within the virtual environment.

# You know that a Python virtual environment is just a folder structure with a settings file. It might or might not come with pip preinstalled, and it has access to the source Python's site-packages directory while remaining isolated. But you might wonder how all of this works.


# How Does a Virtual Environment Work?
# If you know what a Python virtual environment is but wonder how it manages to create the lightweight isolation it provides, then you're in the right section. Here you'll learn how the folder structure and the settings in your pyvenv.cfg file interact with Python to provide a reproducible and isolated space for installing external dependencies.

# It Copies Structure and Files
# When you create a virtual environment using venv, the module re-creates the file and folder structure of a standard Python installation on your operating system. Python also copies or symlinks into that folder structure the Python executable with which you've called venv:

# Windows
# Linux
# macOS
# venv\
# │
# ├── Include\
# │
# ├── Lib\
# │   │
# │   └── site-packages\
# │
# ├── Scripts\
# │   ├── Activate.ps1
# │   ├── activate
# │   ├── activate.bat
# │   ├── deactivate.bat
# │   ├── pip.exe
# │   ├── pip3.10.exe
# │   ├── pip3.exe
# │   ├── python.exe
# │   └── pythonw.exe
# │
# └── pyvenv.cfg
# If you locate your system-wide Python installation on your operating system and inspect the folder structure there, then you'll see that your virtual environment resembles that structure.

# You can find the base Python installation that your virtual environment is based on by navigating to the path you can find under the home key in pyvenv.cfg.

# Note: On Windows, you may notice that python.exe in your base Python installation isn't in Scripts\ but is one folder level up. In your virtual environment, the executable is intentionally located in the Scripts\ folder.

# This small change to the folder structure means that you only need to add a single directory to your shell PATH variable to activate the virtual environment.

# While you might find some additional files and folders in your base Python installation, you'll notice that the standard folder structure is the same as in your virtual environment. venv creates this folder structure to assure that Python will work as expected in isolation, without the need to apply many additional changes.

# It Adapts the Prefix-Finding Process
# With the standard folder structure in place, the Python interpreter in your virtual environment can understand where all relevant files are located. It does this with only minor adaptations to its prefix-finding process according to the venv specification.

# Instead of looking for the os module to determine the location of the standard library, the Python interpreter first looks for a pyvenv.cfg file. If the interpreter finds this file and it contains a home key, then the interpreter will use that key to set the value for two variables:

# sys.base_prefix will hold the path to the Python executable used to create this virtual environment, which you can find at the path defined under the home key in pyvenv.cfg.
# sys.prefix will point to the directory containing pyvenv.cfg.
# If the interpreter doesn't find a pyvenv.cfg file, then it determines that it's not running within a virtual environment, and both sys.base_prefix and sys.prefix will then point to the same path.


# If these two variables have different values, then Python adapts where it'll look for modules:

# The site and sysconfig standard-library modules are modified such that the standard library and header files are found relative to sys.base_prefix […], while site-package directories […] are still found relative to sys.prefix […]. (Source)

# This change effectively allows the Python interpreter in your virtual environment to use the standard library modules from your base Python installation while pointing to its internal site-packages directory to install and access external packages.

# It Links Back to Your Standard Library
# Python virtual environments aim to be a lightweight way to provide you with an isolated Python environment that you can quickly create and then delete when you don't need it anymore. To make this possible, venv copies only the minimally necessary files:

# [A] Python virtual environment in its simplest form would consist of nothing more than a copy or symlink of the Python binary accompanied by a pyvenv.cfg file and a site-packages directory. (Source)

# The Python executable in your virtual environment has access to the standard library modules of the Python installation on which you based the environment. Python makes this possible by pointing to the file path of the base Python executable in the home setting in pyvenv.cfg:

# Windows
# Linux
# macOS
# home = C:\Users\Name\AppData\Local\Programs\Python\Python310
# include-system-site-packages = false
# version = 3.10.3
# If you navigate to the path value of the highlighted line in pyvenv.cfg and list the contents of the folder, then you find the base Python executable that you used to create your virtual environment. From there, you can navigate to find the folder that contains your standard library modules:

# Windows
# Linux
# macOS
# PS> ls C:\Users\Name\AppData\Local\Programs\Python\Python310

#  Directory: C:\Users\Name\AppData\Local\Programs\Python\Python310

# Mode              LastWriteTime      Length Name
# ----              -------------      ------ ----
# d-----     12/19/2021   5:09 PM             DLLs
# d-----     12/19/2021   5:09 PM             Doc
# d-----     12/19/2021   5:09 PM             include
# d-----     12/19/2021   5:09 PM             Lib
# d-----     12/19/2021   5:09 PM             libs
# d-----     12/21/2021   2:04 PM             Scripts
# d-----     12/19/2021   5:09 PM             tcl
# d-----     12/19/2021   5:09 PM             Tools
# -a----      12/7/2021   4:28 AM       32762 LICENSE.txt
# -a----      12/7/2021   4:29 AM     1225432 NEWS.txt
# -a----      12/7/2021   4:28 AM       98544 python.exe
# -a----      12/7/2021   4:28 AM       61680 python3.dll
# -a----      12/7/2021   4:28 AM     4471024 python310.dll
# -a----      12/7/2021   4:28 AM       97008 pythonw.exe
# -a----      12/7/2021   4:29 AM       97168 vcruntime140.dll
# -a----      12/7/2021   4:29 AM       37240 vcruntime140_1.dll

# PS> ls C:\Users\Name\AppData\Local\Programs\Python\Python310\Lib

#  Directory: C:\Users\Name\AppData\Local\Programs\Python\Python310\Lib

# Mode              LastWriteTime      Length Name
# ----              -------------      ------ ----
# d-----     12/19/2021   5:09 PM             asyncio
# d-----     12/19/2021   5:09 PM             collections

# # ...

# -a----      12/7/2021   4:27 AM        5302 __future__.py
# -a----      12/7/2021   4:27 AM          65 __phello__.foo.py
# Python is set up to find these modules by adding the relevant path to sys.path. During initialization, Python automatically imports the site module, which sets the defaults for this argument.

# The paths that your Python session has access to in sys.path determine which locations Python can import modules from.

# If you activate your virtual environment and enter a Python interpreter, then you can confirm that the path to the standard library folder of your base Python installation is available:

# Windows
# Linux
# macOS
# >>> import sys
# >>> from pprint import pp
# >>> pp(sys.path)
# ['',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\DLLs',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\lib',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310',
#  'C:\\Users\\Name\\path\\to\\venv',
#  'C:\\Users\\Name\\path\\to\\venv\\lib\\site-packages']
# Because the path to the directory that contains your standard library modules is available in sys.path, you'll be able to import any of them when you work with Python from within your virtual environment.


# It Modifies Your PYTHONPATH
# To assure that the scripts you want to run use the Python interpreter within your virtual environment, venv modifies the PYTHONPATH environment variable that you can access using sys.path.

# If you inspect that variable without an active virtual environment, you'll see the default path locations for your default Python installation:

# Windows
# Linux
# macOS
# >>> import sys
# >>> from pprint import pp
# >>> pp(sys.path)
# ['',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\DLLs',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\lib',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310',
#  'C:\\Users\\Name\\AppData\\Roaming\\Python\\Python310\\site-packages',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']
# Note the highlighted lines, which represent the path to the site-packages directory. This folder contains external modules that you'd install, for example, using pip. Without an activated virtual environment, this directory is nested within the same folder structure as the Python executable.

# Note: The Roaming folder on Windows contains an additional site-packages directory relevant for installations that use the --user flag with pip. This folder provides a small degree of virtualization, but it still collects all --user installed packages in one spot.

# However, if you activate your virtual environment before starting another interpreter session and rerun the same commands, then you'll get different output:

# Windows
# Linux
# macOS
# >>> import sys
# >>> from pprint import pp
# >>> pp(sys.path)
# ['',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\DLLs',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\lib',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310',
#  'C:\\Users\\Name\\path\\to\\venv',
#  'C:\\Users\\Name\\path\\to\\venv\\lib\\site-packages']
# Python replaced the default site-packages directory path with the one that lives inside your virtual environment. This change means that Python will load any external packages installed in your virtual environment. Conversely, because the path to your base Python's site-packages directory isn't in this list anymore, Python won't load modules from there.

# Note: On Windows systems, Python additionally adds the root folder path of your virtual environment to sys.path.

# This change in Python's path settings effectively creates the isolation of external packages in your virtual environment.

# Optionally, you can get read-only access to the system site-packages directory of your base Python installation by passing an argument when creating the virtual environment.

# It Changes Your Shell PATH Variable on Activation
# For convenience, you'll usually activate your virtual environment before working in it, even though you don't have to.

# To activate your virtual environment, you need to execute an activation script:

# Windows
# Linux + macOS
# PS> venv\Scripts\activate
# (venv) PS>
# Which activation script you'll have to run depends on your operating system and the shell that you're using.

# If you dig into your virtual environment's folder structure, then you'll find a few different activation scripts that it ships with:

# Windows
# Linux
# macOS
# venv\
# │
# ├── Include\
# │
# ├── Lib\
# │
# ├── Scripts\
# │   ├── Activate.ps1
# │   ├── activate
# │   ├── activate.bat
# │   ├── deactivate.bat
# │   ├── pip.exe
# │   ├── pip3.10.exe
# │   ├── pip3.exe
# │   ├── python.exe
# │   └── pythonw.exe
# │
# └── pyvenv.cfg
# These activation scripts all have the same purpose. However, they need to provide different ways of achieving it because of the various operating systems and shells that users are working with.

# Note: You can open any of the highlighted files in your favorite code editor to inspect the content of a virtual environment activation script. Feel free to dig into that file to get a deeper understanding of what it does, or keep reading to quickly get the gist of it.

# Two critical actions happen in the activation script:

# Path: It sets the VIRTUAL_ENV variable to the root folder path of your virtual environment and prepends the relative location of its Python executable to your PATH.
# Command prompt: It changes the command prompt to the name that you passed when creating the virtual environment. It takes that name and puts it into parentheses, for example (venv).
# These changes put the convenience of virtual environments into effect within your shell:

# Path: Because the path to all the executables in your virtual environment now lives at the front of your PATH, your shell will invoke the internal versions of pip or Python when you just type pip or python.
# Command prompt: Because the script changed your command prompt, you'll quickly know whether or not your virtual environment is activated.
# Both of these changes are minor adaptations that exist purely for your convenience. They aren't strictly necessary, but they make working with Python virtual environments more enjoyable.

# You can inspect your PATH variable before and after activation of your virtual environment. If you've activated your virtual environment, then you'll see the path to the folder containing your internal executables at the beginning of PATH:

# Windows
# Linux
# macOS
# PS> $Env:Path
# C:\Users\Name\path\to\venv\Scripts;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Users\Name\AppData\Local\Programs\Python\Python310\Scripts\;C:\Users\Name\AppData\Local\Programs\Python\Python310\;c:\users\name\.local\bin;c:\users\name\appdata\roaming\python\python310\scripts
# Keep in mind that the output of printing your PATH variable will most likely look quite different. The important point is that the activation script has added the path to your virtual environment at the beginning of the PATH variable.

# When you deactivate your virtual environment using deactivate, your shell reverses these changes and puts PATH and your command prompt back to the way they were before.

# Note: On Windows, the deactivate command executes a separate file called deactivate.bat. On UNIX systems, the same script you use for activating a virtual environment also provides the code logic for deactivating the virtual environment.

# Give it a try and inspect the changes. This small change to your PATH variable gives you the convenience of running executables in your virtual environment without the need to provide the full path.


# It Runs From Anywhere With Absolute Paths
# You don't need to activate your virtual environment to use it. You can work with your virtual environment without activating it, even though activating it is a common action that you'll often see recommended.

# If you provide only the name of an executable to your shell, it'll look through the location recorded in PATH for an executable file sporting that name. It'll then pick and run the first one that matches that criterion.

# The activation script changes your PATH variable so that the binaries folder of your virtual environment is the first place your shell looks for executables. This change allows you to type only pip or python to run the respective programs situated inside your virtual environment.

# If you don't activate your virtual environment, then you can instead pass the absolute path of the Python executable inside your virtual environment to run any script from within your virtual environment:

# Windows
# Linux
# macOS
# PS> C:\Users\Name\path\to\venv\Scripts\python.exe
# This command will start the Python interpreter within your virtual environment precisely the same way it would if you first activated the virtual environment and then called it with python.


# You'll often activate your virtual environment before working with it and deactivate it after you're done. However, there is an everyday use case where using the absolute paths is a helpful approach.

# Note: Absolute paths can be helpful for running a scheduled script on your remote server or in a Docker container. Specifically, you'll want to use absolute paths if the script requires external dependencies that you want to isolate from the rest of your server in a Python virtual environment.

# Embedding the activation of your virtual environment in your script is a fussy exercise that goes wrong more often than it doesn't. Instead, equipped with the knowledge that you've gained in this tutorial, you can use the absolute path to the Python interpreter in your virtual environment when running your script.

# You could use this, for example, if you were setting up an hourly CRON job on your remote Linux server that checks for site connectivity asynchronously using the external aiohttp package that you installed in a virtual environment:

# 0 * * * *
#     /home/name/Documents/connectivity-checker/venv/bin/python
#     -m rpchecker
#     -u google.com twitter.com
#     -a
# You don't need to fiddle with activating your virtual environment to use the right Python interpreter that has access to the dependencies that you've installed inside the virtual environment. Instead, you just pass the absolute path to the binary of that interpreter. Python takes care of the rest for you during initialization.

# As long as you provide the path to your Python executable, you don't need to activate your virtual environment to enjoy the benefits of using one.

# How Can You Customize a Virtual Environment?
# If you're confident about what a Python virtual environment is and you want to customize it for a specific use case, then you're in the right place. In this section, you'll learn about the optional arguments that you can pass when creating a virtual environment with venv, and how these customizations can help you get precisely the virtual environment you need.

# Change the Command Prompt
# You can change the folder name that contains your virtual environment when you create it by passing a name other than venv. In fact, you'll often see different names in different projects. Some of them are commonly used:

# venv
# env
# .venv
# You could name the folder that you create for your virtual environment anything you want.

# Note: Naming your virtual environment folder venv is just a convention. Sticking to this convention can help you reliably exclude your virtual environment from version control using a .gitignore file.

# Whatever name you choose will show up in your command prompt after you activate the virtual environment:

# Windows
# Linux + macOS
# PS> python -m venv your-fancy-name
# PS> your-fancy-name\Scripts\activate
# (your-fancy-name) PS>
# If you give your virtual environment folder an alternate name, you'll also need to consider that name when you want to run your activation script, as shown in the code example above.

# If you want the convenience of seeing a different command prompt, but you want to keep the folder name descriptive so that you'll know it contains a virtual environment, then you can pass your desired command prompt name to --prompt:

# Windows
# Linux + macOS
# PS> python -m venv venv --prompt="dev-env"
# PS> venv\Scripts\activate
# (dev-env) PS>
# Using the optional --prompt argument, you can set the command prompt that'll show up when your virtual environment is active to a descriptive string without changing the name of your virtual environment's folder.

# In the code snippet above, you can see that you're still calling the folder venv, which means that you'll be able to access the activate script with the familiar path. At the same time, the command prompt that shows up after activation will be whatever you passed to --prompt.


# Overwrite Existing Environments
# You might want to delete and re-create one of your virtual environments at any given time.
# If you do that often, then you might be glad to know that you can add the --clear argument
# to delete the contents of an existing environment before Python creates the new one.

# Before you try that out, it's helpful to see that running the command to create a new virtual environment without this argument won't overwrite an existing virtual environment with the same name:

# Windows
# Linux + macOS
# PS> python -m venv venv
# PS> venv\Scripts\pip.exe install requests
# PS> venv\Scripts\pip.exe list
# Package            Version
# ------------------ ---------
# certifi            2021.10.8
# charset-normalizer 2.0.12
# idna               3.3
# pip                22.0.4
# requests           2.27.1
# setuptools         58.1.0
# urllib3            1.26.9

# PS> python -m venv venv
# PS> venv\Scripts\pip.exe list
# Package            Version
# ------------------ ---------
# certifi            2021.10.8
# charset-normalizer 2.0.12
# idna               3.3
# pip                22.0.4
# requests           2.27.1
# setuptools         58.1.0
# urllib3            1.26.9
# In this code example, you first created a virtual environment called venv, then used the environment-internal pip executable to install requests into the site-packages directory of your virtual environment. You then used pip list to confirm that it had been installed, together with its dependencies.

# Note: You ran all these commands without activating the virtual environment. Instead, you used the full path to the internal pip executable to install into your virtual environment. Alternatively, you could've activated the virtual environment.

# In the highlighted line, you attempted to create another virtual environment using the same name, venv.

# You might expect venv to notify you that there's an existing virtual environment on the same path, but it doesn't. You might expect venv to automatically delete the existing virtual environment with the same name and replace it with a new one, but it doesn't do that either. Instead, when venv finds an existing virtual environment of the same name on the path you provided, it doesn't do anything—and again, it doesn't communicate this to you.

# If you list the installed packages after running the virtual environment creation command a second time, then you'll notice that requests and its dependencies still show up. This might not be what you want to achieve.

# Rather than navigating to your virtual environment folder and deleting it first, you can explicitly overwrite an existing virtual environment using --clear:

# Windows
# Linux + macOS
# PS> python -m venv venv
# PS> venv\Scripts\pip.exe install requests
# PS> venv\Scripts\pip.exe list
# Package            Version
# ------------------ ---------
# certifi            2021.10.8
# charset-normalizer 2.0.12
# idna               3.3
# pip                22.0.4
# requests           2.27.1
# setuptools         58.1.0
# urllib3            1.26.9

# PS> python -m venv venv --clear
# PS> venv\Scripts\pip.exe list
# Package    Version
# ---------- -------
# pip        22.0.4
# setuptools 58.1.0
# Using the same example as before, you added the optional --clear argument when running the creation command the second time.

# You then confirmed that Python automatically discarded the existing virtual environment with the same name and created a new default virtual environment without the previously installed packages.

# Create Multiple Virtual Environments at Once
# If one virtual environment isn't enough, you can create multiple separate virtual environments in one go by passing more than one path to the command:

# Windows
# Linux
# macOS
# PS> python -m venv venv C:\Users\Name\Documents\virtualenvs\venv-copy
# Running this command creates two separate virtual environments in two different locations. These two folders are independent virtual environment folders. Passing more than one path therefore just saves you the effort of typing the creation command more than once.

# In the example shown above, you might notice that the first argument, venv, represents a relative path. Conversely, the second argument uses an absolute path to point to a new folder location. Either option works when creating a virtual environment. You can even mix and match, as you did here.

# Note: The most common command for creating a virtual environment, python3 -m venv venv, uses a relative path from your current location in your shell and creates a new folder named venv in that directory.

# You don't have to do this. Instead, you could provide an absolute path that points anywhere on your system. If any of your path directories don't yet exist, venv will create them for you.

# You're also not limited to creating two virtual environments at once. You can pass as many valid paths as you want, separated by a whitespace character. Python will diligently set up a virtual environment at each location, even creating any missing folders on the way.


# Update the Core Dependencies
# When you've created a Python virtual environment using venv and its default settings and then installed an external package using pip, you've most likely encountered a message telling you that your installation of pip is outdated:

# Windows
# Linux + macOS
# WARNING: You are using pip version 21.2.4; however, version 22.0.4 is available.
# You should consider upgrading via the
# 'C:\Users\Name\path\to\venv\Scripts\python.exe -m pip install --upgrade pip' command.
# It can be frustrating to create something new just to see that it's already outdated! Why does this happen?

# The installation of pip that you'll receive when creating a virtual environment with the default configuration of venv is likely outdated because venv uses ensurepip to bootstrap pip into your virtual environment.

# ensurepip intentionally doesn't connect to the Internet, but instead uses a pip wheel that comes bundled with each new CPython release. Therefore, the bundled pip has a different update cycle than the independent pip project.

# Once you install an external package using pip, the program connects to PyPI and also identifies if pip itself is outdated. If pip is outdated, then you'll receive the warning shown above.

# While using the bootstrapped version of pip can be helpful in some cases, you might want to have the latest pip to avoid potential security issues or bugs that might still be around in an older version. For an existing virtual environment, you can follow the instructions that pip prints to your terminal and use pip to upgrade itself.

# If you want to save the effort of doing this manually, you can specify that you want pip to contact PyPI and update itself right after installation by passing the --upgrade-deps argument:

# Windows
# Linux + macOS
# PS> python -m venv venv --upgrade-deps
# PS> venv\Scripts\activate
# (venv) PS> python -m pip install --upgrade pip
# Requirement already satisfied: pip in c:\users\name\path\to\venv\lib\site-packages (22.0.4)
# Suppose you use the optional --upgrade-deps argument when creating your virtual environment. In that case, it'll automatically poll PyPI for the newest versions of pip and setuptools and install them if the local wheel isn't up-to-date.

# Gone is that pesky warning message, and you can rest assured that you're using the most recent version of pip.

# Avoid Installing pip
# You might wonder why it takes a while to set up a Python virtual environment when all it does is create a folder structure. The reason for the time delay is mainly the installation of pip. pip and its dependencies are large and blow up the size of your virtual environment from a few kilobytes to many megabytes!

# In most use cases, you'll want to have pip installed in your virtual environment because you'll probably use it to install external packages from PyPI. However, if you don't need pip for whatever reason, then you can use --without-pip to create a virtual environment without it:

# Windows
# Linux
# macOS
# PS> python -m venv venv --without-pip
# PS> Get-ChildItem venv | Measure-Object -Property length -Sum

# Count    : 1
# Average  :
# Sum      : 120
# Maximum  :
# Minimum  :
# Property : Length
# Your virtual environment still does everything that qualifies it as a virtual environment by providing lightweight isolation with a separate Python executable.

# Note: Even though you didn't install pip, running pip install <package-name> might still seem to work. Don't do this, though, because running the command won't give you what you're looking for. You'd be using a pip executable from somewhere else on your system, and your package will land in the site-packages folder of whichever Python installation is associated with that pip executable.

# To work with a virtual environment that doesn't have pip installed, you can manually install packages into your site-packages directory or place your ZIP files in there then import them using Python ZIP imports.

# Include the System Site-Packages
# In some situations, you might want to keep access to your base Python's site-packages directory instead of severing that tie. For example, you might have already set up a package that's compiled during installation, such as Bokeh, in your global Python environment.

# Bokeh happens to be your data exploration library of choice, and you use it for all your projects. You still want to keep your clients' projects in separate environments, but installing Bokeh into each of these can take a couple of minutes each. For quick iteration, you instead want to have access to the existing Bokeh installation without needing to redo it for every virtual environment you create.

# You can access all modules you've installed to your base Python's site-packages directory by adding the --system-site-packages flag when creating your virtual environment.

# Note: If you install any additional external packages, then Python will put them into the site-packages directory of your virtual environment. You only get read access to the system site-packages directory.

# Create a new virtual environment while passing this argument. You'll see that in addition to your local site-packages directory, the path to your base Python's site-packages directory will stick around in sys.path.

# To test this, you can create and activate a new virtual environment using the --system-site-packages argument:

# Windows
# Linux + macOS
# PS> python -m venv venv --system-site-packages
# PS> venv\Scripts\activate
# (venv) PS>
# Once again, you've created a new virtual environment named venv, but this time you passed the --system-site-packages argument. Adding this optional argument resulted in a different setting in your pyvenv.cfg file:

# Windows
# Linux
# macOS
# home = C:\Users\Name\AppData\Local\Programs\Python\Python310
# include-system-site-packages = true
# version = 3.10.3
# Instead of sporting the default value of false, the include-system-site-packages configuration is now set to true.

# This change means that you'll see an additional entry to sys.path, which allows the Python interpreter in your virtual environment to also access the system site-packages directory. Make sure your virtual environment is active, then start the Python interpreter to check the path variables:

# Windows
# Linux
# macOS
# >>> import sys
# >>> from pprint import pp
# >>> pp(sys.path)
# ['',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\DLLs',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\lib',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310',
#  'C:\\Users\\Name\\path\\to\\venv',
#  'C:\\Users\\Name\\path\\to\\venv\\lib\\site-packages',
#  'C:\\Users\\Name\\AppData\\Roaming\\Python\\Python310\\site-packages',
#  'C:\\Users\\Name\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']
# The highlighted lines show the additional paths present in a virtual environment when you've created it using --system-site-packages. They point to the site-packages directories of your base Python installation and give the interpreter inside your virtual environment access to these packages.

# Copy or Link Your Executables
# Whether you receive a copy or a symlink of your Python binaries depends on the operating system that you're working with:

# Windows may create either a symlink or a copy, but some versions don't support symlinks. Creating symlinks might require you to have administrator privileges.
# Linux distributions may create either a symlink or a copy and often opt for symlinks over copies.
# macOS always creates a copy of the binaries.
# PEP 405 mentions the advantages of creating symlinks:

# Symlinking is preferable where possible because, in the case of an upgrade to the underlying Python installation, a Python executable copied in a venv might become out-of-sync with the installed standard library and require manual upgrade. (Source)

# While it can be helpful to symlink the executables so that they'll automatically stay in sync even if you upgrade your base Python installation, the added flimsiness of this approach may outweigh its benefit. For example, when you double-click python.exe in Windows, the operating system will eagerly resolve the symlink and ignore your virtual environment.

# Most likely, you won't ever have to touch these arguments, but if you have a good reason for attempting to force either symlinks or copies over your operating system's default, then you can do so:

# --symlinks will attempt to create symlinks instead of copies. This option won't have any effect on macOS builds.
# --copies will attempt to create copies of your Python binaries instead of linking them to the base Python installation's executables.
# You can pass either one of these optional arguments when creating your virtual environment.

# Upgrade Your Python to Match the System Python
# If you've built your virtual environment using copies rather than symlinks and later updated your base Python version on your operating system, you might run into a version mismatch with standard library modules.

# The venv module offers a solution to this. The optional --upgrade argument keeps your site-packages directory intact while updating the binary files to the new versions on your system:

# Windows
# Linux + macOS
# PS> python -m venv venv --upgrade
# If you run this command and you've updated your Python version since initially creating the virtual environment, then you'll keep your installed libraries, but venv will update the executables for pip and Python.

# In this section, you've learned that you can apply a lot of customization to the virtual environments that you build with the venv module. These adaptations can be pure convenience updates, such as naming your command prompt differently from your environment folder, overwriting existing environments, or creating multiple environments with a single command. Other customizations create different functionality in your virtual environments by, for example, skipping the installation of pip and its dependencies, or linking back to the base Python's site-packages folder.

# But what if you want to do even more than that? In the next section, you'll explore alternatives to the built-in venv module.

# What Other Popular Options Exist, Aside From venv?
# The venv module is a great way to work with Python virtual environments. One of its main advantages is that venv comes preinstalled with Python starting from version 3.3. But it isn't the only option you have. You can use other tools to create and handle virtual environments in Python.

# In this section, you'll learn about two popular tools. They have different scopes but are both also commonly used for the same purpose as the venv module:

# Virtualenv is a superset of venv and provides the basis for its implementation. It's a powerful, extendable tool for creating isolated Python environments.
# Conda offers package, dependency, and environment management for Python and other languages.
# They have some advantages over venv, but they don't come with your standard Python installation, so you'll have to install them separately.

# The Virtualenv Project
# Virtualenv is a tool that was specifically made for creating isolated Python environments. It's been a long-time favorite within the Python community and precedes the built-in venv module.

# The package is a superset of venv, which allows you to do everything that you can do using venv, and more. Virtualenv allows you to:

# Create virtual environments more quickly
# Discover installed versions of Python without needing to provide the absolute path
# Upgrade the tool using pip
# Extend the functionality of the tool yourself
# Any of these additional functionalities can come in handy when you're working on your Python projects. You might even want to save a blueprint of your virtualenv in code together with your project to aid reproducibility. Virtualenv has a rich programmatic API that allows you to describe virtual environments without creating them.

# After installing virtualenv on your system, you can create and activate a new virtual environment similarly to how you do it using venv:

# Windows
# Linux
# macOS
# PS> virtualenv venv
# created virtual environment CPython3.10.3.final.0-64 in 312ms
#   creator CPython3Windows(dest=C:\Users\Name\path\to\venv, clear=False, no_vcs_ignore=False, global=False)
#   seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Name\AppData\Local\pypa\virtualenv)
#     added seed packages: pip==22.0.4, setuptools==60.10.0, wheel==0.37.1
#   activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
# PS> Set-ExecutionPolicy Unrestricted -Scope Process
# PS> venv\Scripts\activate
# (venv) PS>
# Note: To avoid running into issues with the execution policy when activating your virtual environment, you first changed the execution policy for the current PowerShell session using Set-ExecutionPolicy Unrestricted -Scope Process.

# Like with venv, you can pass a relative or an absolute path and name your virtual environment. Before working in your virtualenv, you'll usually activate it using one of the provided scripts.

# Note: You might notice that virtualenv creates the isolated environment much more quickly than the built-in venv module, which is possible because the tool caches platform-specific application data which it can quickly read from.

# There are two main user advantages with virtualenv over venv:

# Speed: Virtualenv creates environments much more quickly.
# Updates: Thanks to virtualenv's embedded wheels, you'll receive up-to-date pip and setuptools without needing to connect to the Internet right when you first set up the virtual environment.
# If you need to work with legacy versions of Python 2.x, then virtualenv can also be helpful for that. It supports building Python virtual environments using Python 2 executables, which isn't possible using venv.

# Note: If you want to try working with virtualenv, but you don't have the permissions to install it, you can use Python's zipapp module to circumvent that. Follow the instructions in the docs on installing virtualenv via zipapp.

# If you're just getting started with virtual environments in Python, then you may want to stick with the built-in venv module. However, if you've used it for a while and you're bumping into the tool's limitations, then it's a great idea to get started using virtualenv.

# The Conda Package and Environment Manager
# Conda gives you an alternative package and environment management approach. While the tool is primarily associated with the data science community and the Anaconda Python distribution, its potential use cases extend beyond that community and beyond just installing Python packages:

# Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN, and more. (Source)

# While you can also use conda to set up an isolated environment to install Python packages, this is only one feature of the tool:

# pip installs python packages within an environment; conda installs any package within conda environments. (Source)

# As you may gather from this quote, conda accomplishes this isolation differently from the venv module and virtualenv project.

# Note: A complete discussion of the conda package and environment manager is outside the scope of this tutorial. You'll gloss over the differences and look at conda specifically for creating and working with a Python virtual environment.

# Conda is its own project that's unrelated to pip. You can set it up on your system using the Miniconda installer, which brings along the minimal requirements for running conda on your system.

# In its default configuration, conda get its packages from repo.anaconda.com instead of PyPI. This alternative package index is maintained by the Anaconda project and is similar PyPI, but not identical.

# Because conda isn't limited to Python packages, you'll find other, usually data-science-related packages on conda's package index written in different languages. Conversely, there are Python packages available on PyPI that you can't install using conda because they aren't present in that package repository. If you need such a package in your conda environment, then you can instead install it there using pip.

# If you're working in the data science space and with Python alongside other data science projects, then conda is an excellent choice that works across platforms and languages.

# After installing Anaconda or Miniconda, you can create a conda environment:

# Windows
# Linux
# macOS
# PS> conda create -n <venv-name>
# Collecting package metadata (current_repodata.json): done
# Solving environment: done

# ## Package Plan ##

#   environment location: C:\Users\Name\miniconda3\envs\<venv-name>

# Proceed ([y]/n)? y

# Preparing transaction: done
# Verifying transaction: done
# Executing transaction: done
# #
# # To activate this environment, use
# #
# #     $ conda activate <venv-name>
# #
# # To deactivate an active environment, use
# #
# #     $ conda deactivate
# Suppose your standard PowerShell session doesn't recognize the conda command after successfully installing Anaconda. In that case, you can look for the Anaconda PowerShell Prompt in your programs and work with that one instead.

# This command creates a new conda environment in a central location on your computer.

# Note: Because all conda environments live in the same location, all environment names need to be unique. Therefore, it's best if you give them descriptive names instead of calling any conda environment venv.

# To work within your new conda environment, you'll need to activate it:

# Windows
# Linux + macOS
# PS> conda activate <venv-name>
# (<venv-name>) PS>
# After activating the environment, you can install packages from conda's package repository into that environment:

# Windows
# Linux + macOS
# (<venv-name>) PS> conda install numpy
# The install command installs a third-party package from conda's package repository into your active conda environment.

# When you're done working in the environment, you'll have to deactivate it:

# Windows
# Linux + macOS
# (<venv-name>) PS> conda deactivate
# PS>
# You might notice that the general idea is similar to working with Python virtual environments that you've created using venv. The commands differ slightly, but you'll receive the same benefits of working within an isolated environment that you can delete and re-create when necessary.

# If you primarily work on data science projects and already work with Anaconda, then you might never have to work with venv. In that case, you can read more about conda environments and how to work with them effectively on your machine.

# If you only have pure-Python dependencies and you haven't worked with Anaconda before, then you're better off using the more lightweight venv module directly or giving virtualenv a try.

# How Can You Manage Your Virtual Environments?
# If you've absorbed all the information from the previous sections, but you're unsure how to handle the multitude of environment folders that have started agglomerating on your system, keep reading here.

# In this section, you'll learn how to extract the essential information of your virtual environment into a single file so that you can quickly delete and re-create your virtual environment folder at any time and on any computer.

# You'll also learn about two different ways of organizing where to keep your virtual environment folders and about some popular third-party tools that can help you manage your virtual environments.

# Decide Where to Create Your Environment Folders
# A Python virtual environment is just a folder structure. You can place it anywhere on your system. However, a consistent structure can help, and there are two prominent opinions on where to create your virtual environment folders:

# Inside each individual project folder
# In a single location, for example in a subfolder of your home directory
# Both of these have merits and disadvantages, and your preference will ultimately depend on your workflow.

# In the project-folder approach approach, you create a new virtual environment in the root folder of the project that'll use this virtual environment for:

# project_name/
# │
# ├── venv/
# │
# └── src/
# The virtual environment folder then lives side by side with any code that you'll write for that project.

# This structure has the advantage that you'll know which virtual environment belongs to which project, and you can activate your virtual environment using a short relative path once you've navigated into the project folder.

# In the single-folder approach, you keep all your virtual environments in a single folder, for example in a subfolder of your home directory:

# Windows
# Linux
# macOS
# C:\USERS\USERNAME\
# │
# ├── .local\
# │
# ├── Contacts\
# │
# ├── Desktop\
# │
# ├── Documents\
# │   │
# │   └── Projects\
# │       │
# │       ├── django-project\
# │       │
# │       ├── flask-project\
# │       │
# │       └── pandas-project\
# │
# ├── Downloads\
# │
# ├── Favorites\
# │
# ├── Links\
# │
# ├── Music\
# │
# ├── OneDrive\
# │
# ├── Pictures\
# │
# ├── Searches\
# │
# ├── venvs\
# │   │
# │   ├── django-venv\
# │   │
# │   ├── flask-venv\
# │   │
# │   └── pandas-venv\
# │
# └── Videos\
# If you use this approach, it could be less effort to keep track of which virtual environments you've created. You can go to a single location on your operating system to inspect all virtual environments and decide which ones to keep and which ones to delete.

# On the other hand, you won't be able to activate your virtual environment quickly using a relative path when you've already navigated to your project folder. Instead, it's best to activate it using the absolute path to the activate script in the respective virtual environment folder.

# Note: You can use either of the two approaches and even mix and match.

# You could create your virtual environments anywhere on your system. Just keep in mind that a clear structure will make it more user-friendly for you to know where to find the folders.

# A third option is to leave this decision to your integrated development environment (IDE). Many of these programs include options to automatically create a virtual environment for you when you start a new project.

# To learn more about how your favorite IDE handles virtual environments, check out its online documentation on the topic. For example, VS Code and PyCharm have their own approaches to creating virtual environments.

# Treat Them as Disposables
# Virtual environments are disposable folder structures that you should be able to safely delete and re-create at any time without losing information about your code project.

# This means that you generally don't put any additional code or information into your virtual environment manually. Anything that goes in there should be handled by your package manager, which will usually be pip or conda.

# You also shouldn't commit your virtual environment to version control, and you shouldn't ship it with your project.

# Because virtual environments aren't entirely self-sufficient Python installations but rely on the base Python's standard library, you won't create a portable application by distributing your virtual environment together with your code.

# Note: If you want to learn how to distribute your Python project, then you can read about publishing an open-source package to PyPI or using PyInstaller to distribute Python applications.

# Virtual environments are meant to be lightweight, disposable, and isolated environments to develop your projects in.

# However, you should be able to re-create your Python environment on a different computer so that you can run your program or
# continue developing it there. How can you make that happen when you treat your virtual environment as disposable and won't
# commit it to version control?

# Pin Your Dependencies
# To make your virtual environment reproducible, you need a way to describe its contents. The most common way to do this is by
# creating a requirements.txt file while your virtual environment is active:

# Windows
# Linux + macOS
# (venv) PS> python -m pip freeze > requirements.txt
# This command pipes the output of pip freeze into a new file called requirements.txt. If you open the file, then you'll notice that
# it contains a list of the external dependencies currently installed in your virtual environment.

# This list is a recipe for pip to know which version of which package to install. As long as you keep this requirements.txt file up
# to date, you can always re-create the virtual environment that you're working in, even after deleting the venv/ folder or moving to
# a different computer altogether:

# Windows
# Linux + macOS
# (venv) PS> deactivate
# PS> python -m venv new-venv
# PS> new-venv\Scripts\activate
# (new-venv) PS> python -m pip install -r requirements.txt
# In the example code snippet above, you created a new virtual environment called new-venv, activated it, and installed all external
# dependencies that you previously recorded in your requirements.txt file.

# If you use pip list to inspect the currently installed dependencies, then you'll see that both virtual environments, venv and
# new-venv, now contain the same external packages.

# Note: By committing your requirements.txt file to version control, you can ship your project code with the recipe that allows your
# users and collaborators to re-create the same virtual environment on their machines.

# Keep in mind that while this is a widespread way to ship dependency information with a code project in Python, it isn't
# deterministic:

# Python Version: This requirements file doesn't include information about which version of Python you used as your base Python
# interpreter when creating the virtual environment.
# Sub-Dependencies: Depending on how you create your requirements file, it may not include version information about sub-dependencies
# of your dependencies. This means that someone could get a different version of a subpackage if that package was silently updated
# after you created your requirements file.
# You can't easily solve either of these issues with requirements.txt alone, but many third-party dependency management tools attempt
# to address them to guarantee deterministic builds:

# requirements.txt using pip-tools
# Pipfile.lock using Pipenv
# poetry.lock using Poetry
# Projects that integrate the virtual environment workflow into their features but go beyond that will also often include ways to create lock files that allow deterministic builds of your environments.

# Avoid Virtual Environments in Production
# You might wonder how to include and activate your virtual environment when deploying a project to production. In most cases, you don't want to include your virtual environment folder in remote online locations:

# GitHub: Don't push the venv/ folder to GitHub.
# CI/CD Pipelines: Don't include your virtual environment folder in your continuous integration or continuous delivery pipelines.
# Server Deployments: Don't set up a virtual environment on your deployment server unless you manage that server yourself and run multiple separate projects on it.
# You still want isolated environments and reproducibility for your code projects. You'll achieve that by pinning your dependencies instead of including the virtual environment folder that you've worked with locally.

# Most remote hosting providers, including CI/CD pipeline tools and Platform-as-a-Service (PaaS) providers, such as Heroku or Google App Engine (GAE), will automatically create that isolation for you.

# When you push your code project to one of these hosted services, the service will often allocate a virtual fraction of a server to your application. Such virtualized servers are isolated environments by design, which means that your code will run in its separate environment by default.

# In most hosted solutions, you won't have to deal with creating the isolation, but you'll still need to provide the information about what to install in the remote environment. For this, you'll often use the pinned dependencies in your requirements.txt file.

# Note: If you run multiple projects on a server that you host yourself, then you might benefit from setting up virtual environments on that server.

# In that case, you'll get to treat the server similarly to your local computer. Even then, you won't copy the virtual environment folder. Instead, you'll re-create the virtual environment on your remote server from your pinned dependencies.

# Most hosted platform providers will also ask you to create a settings file specific to the tool that you're working with. This file will include information that isn't recorded in requirements.txt but that the platform needs to set up a functioning environment for your code. You'll need to read up on these specific files in the documentation of the hosting service that you're planning to use.

# A popular option that takes virtualization to the next level and still allows you to create a lot of the setup yourself is Docker.

# Use Third-Party Tools
# The Python community has created many additional tools that use virtual environments as one of their features and allow you to manage multiple virtual environments in a user-friendly manner.

# Because many tools come up in online discussions and tutorials, you might wonder what each of them is about and how they can help you manage your virtual environments.

# While discussing each of them is out of the scope of this tutorial, you'll get an overview of which popular projects exist, what they do, and where you can learn more:

# virtualenvwrapper is an extension to the virtualenv project that makes creating, deleting, and otherwise managing virtual environments lower effort. It keeps all your virtual environments in one place, introduces user-friendly CLI commands for managing and switching between virtualenvs, and is also configurable and extensible. virtualenvwrapper-win is a Windows port of this project.

# Poetry is a tool for Python dependency management and packaging. With Poetry, you can declare packages that your project depends on, similar to requirements.txt but deterministic. Poetry will then install these dependencies in an auto-generated virtual environment and help you manage your virtual environment.

# Pipenv aims to improve packaging in Python. It creates and manages virtual environments for your projects using virtualenv in the back. Like Poetry, Pipenv aims to improve dependency management to allow for deterministic builds. It's a relatively slow, high-level tool that has been supported by the Python Packaging Authority (PyPA).

# pipx allows you to install Python packages that you'd habitually run as stand-alone applications in isolated environments. It creates a virtual environment for each tool and makes it globally accessible. Aside from helping with code quality tools such as black, isort, flake8, pylint, and mypy, it's also useful for installing alternative Python interpreters, such as bpython, ptpython, or ipython.

# pipx-in-pipx is a wrapper you can use for installing pipx that takes the recursive acronym for pip to the next level by allowing you to install and manage pipx using pipx itself.

# pyenv isn't inherently related to virtual environments, even though it's often mentioned in relation to this concept. You can manage multiple Python versions with pyenv, which allows you to switch between a new release and an older Python version that you need for a project you're working on. pyenv also has a Windows port called pyenv-win.

# pyenv-virtualenv is a plugin for pyenv that combines pyenv with virtualenv, allowing you to create virtual environments for the pyenv-managed Python versions on UNIX systems. There's even a plugin to mix pyenv with virtualenvwrapper, called pyenv-virtualenvwrapper.

# The Python community built a whole host of third-party projects that can help you manage your Python virtual environments in a user-friendly manner.

# Remember that these projects are meant to make the process more convenient for you and aren't necessary for working with virtual environments in Python.

# Conclusion
# Congratulations on making it through this tutorial on Python virtual environments. Throughout the tutorial, you built a thorough understanding of what virtual environments are, why you need them, how they function internally, and how you can manage them on your system.

# In this tutorial, you learned how to:

# Create and activate a Python virtual environment
# Explain why you want to isolate external dependencies
# Visualize what Python does when you create a virtual environment
# Customize your virtual environments using optional arguments to venv
# Deactivate and remove virtual environments
# Choose additional tools for managing your Python versions and virtual environments
# Next time a tutorial tells you to create and activate a virtual environment, you'll better understand why that's a good suggestion and what Python does for you behind the scenes.

#  Take the Quiz: Test your knowledge with our interactive “Python Virtual Environments: A Primer” quiz. Upon completion you will receive a score so you can track your learning progress over time:

# """
