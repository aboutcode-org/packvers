packvers
==========

.. start-intro

packvers is friendly fork of packaging to work around the drop for
LegacyVersion support. See https://github.com/pypa/packaging/issues/530


Reusable core utilities for various Python Packaging
`interoperability specifications <https://packaging.python.org/specifications/>`_.

This library provides utilities that implement the interoperability
specifications which have clearly one correct behaviour (eg: :pep:`440`)
or benefit greatly from having a single shared implementation (eg: :pep:`425`).

.. end-intro

The ``packvers`` project includes the following: version handling, specifiers,
markers, requirements, tags, utilities.

Documentation
-------------

The `documentation`_ provides information and the API for the following:

- Version Handling
- Specifiers
- Markers
- Requirements
- Tags
- Utilities

Installation
------------

Use ``pip`` to install these utilities::

    pip install packvers

Discussion
----------

If you run into bugs, you can file them in our `issue tracker`_.


.. _`issue tracker`: https://github.com/aboutcode-org/packvers/issues


Code of Conduct
---------------

Everyone interacting in the packaging project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PSF Code of Conduct`_.

.. _PSF Code of Conduct: https://github.com/pypa/.github/blob/main/CODE_OF_CONDUCT.md

Contributing
------------

The ``CONTRIBUTING.rst`` file outlines how to contribute to this project as
well as how to report a potential security issue. The documentation for this
project also covers information about `project development` and `security`.


Project History
---------------

Please review the ``CHANGELOG.rst`` file or the `Changelog documentation` for
recent changes and project history.
