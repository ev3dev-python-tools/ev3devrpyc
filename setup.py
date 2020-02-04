from setuptools import setup
import os.path
import sys


setup(
      name="ev3devrpyc",
      version="1.0.0",
      description="Library to remotely steer the EV3: using the RPyC protocol it forwards ev3dev(2) API calls from the PC to the EV3",
      long_description="""
The ev3devrpyc package allows you to remotely steer a real EV3 from your PC.

You only need to import the 'ev3devrpyc' module at the beginning of your python program 
before the ev3dev or ev3dev2 api is loaded.

Then the 'ev3devrpyc' module loads a special importer which instead of loading the ev3dev 
modules from the simulator it proxies the ev3dev(2) modules on a remote EV3. So when doing 
API calls to this proxied module all these calls are forwarded to the EV3. The RPyC library 
is used to implement this proxy, hence the name ev3devrpyc.
     
For more info: https://github.com/ev3dev-python-tools/ev3devrpyc
""",
      url="https://github.com/ev3dev-python-tools/ev3devrpyc",
      author="Harco Kuppens",
      author_email="h.kuppens@cs.ru.nl",
      license="MIT",
      classifiers=[
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: Freeware",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Education",
        "Topic :: Software Development",
      ],
      keywords="IDE education programming EV3 mindstorms lego",
      platforms=["Windows", "macOS", "Linux"],
      python_requires=">=3.6",
      install_requires=['rpyc==4.1.2'],
      py_modules=["ev3devrpyc"]
)
