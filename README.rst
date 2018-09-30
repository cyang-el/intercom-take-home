.. image:: https://app.wercker.com/status/9518b1e95693c07b71cc0bcd4dae1db6/s/master
   :target: https://app.wercker.com/project/byKey/9518b1e95693c07b71cc0bcd4dae1db6
   :alt: Build Status

.. image:: https://api.codeclimate.com/v1/badges/c0ff9e1efc89ec245066/maintainability
   :target: https://codeclimate.com/github/showjackyang/intercom-take-home/maintainability
   :alt: Maintainability

.. image:: https://api.codeclimate.com/v1/badges/c0ff9e1efc89ec245066/test_coverage
   :target: https://codeclimate.com/github/showjackyang/intercom-take-home/test_coverage
   :alt: Test Coverage


Prerequisite
============

- Docker


TLDR
====

Setup
-----
1. Copy ``.env.example`` to ``.env``, this includes default file path setup.
2. Install dependancies via docker:

.. code:: bash

   make install

Test
----
.. code:: bash

   make test

Run
---
.. code:: bash

   make run

 
To change IO file path
======================
1. This can be accomplished by changing corresponding environment variable value in the copied ``.env``.
2. *Please note this path setting has only been tested with POSIX systems.*
