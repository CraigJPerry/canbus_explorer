Canbus Explorer: Developer Setup
================================

I use the following tools in my development environment:

* PyCharm
* Python 2.7
* Virtualenv
* PySide (Qt GUI framework bindings)
* Setuptools
* Sphinx

I also use the following online services:

* Github
* Travis CI
* readthedocs


Qt4 UI Workflow
===============

Of all the possible workflows, i'm currently using Qt4 Designer to edit
the ``src/resources/main_window.ui`` and ``pyside-uic`` to auto-generate
a Python class containing the UI elements::

    [user@host ~]$ pyside-uic src/resources/main_window.ui > src/canbus_explorer/autogen/main_window.py

This UI is then loaded in ``src/canbus_explorer/gui.py``.

