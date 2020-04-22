Changelog for package base ``barrier``
======================================

2.3.2-1 - 2019-10-12
--------------------

- Updated to upstream release 2.3.2_, for which there is no upstream
  changelog available (apart from the VCS history).

2.3.1-1 - 2019-09-25
--------------------

- Updated to upstream release 2.3.1_.

  Upstream release notes since version 2.1.2_:

  * Fixes for the international US keyboard (2.3.1_)
  * Misc. Fixes and Improvements (2.3.0_)

2.1.2-2 - 2018-12-29
--------------------

- The ``barrier`` package now only contains the Barrier GUI, while
  a new package ``barrier-headless`` contains the server and client
  CLI binaries. Users that don't require the GUI can now install only
  the ``barrier-headless`` package and avoid the ``qt5-base`` dependency
  required by the Barrier GUI.

  The ``barrier`` package automatically pulls in the ``barrier-headless``
  package.

2.1.2-1 - 2018-12-29
--------------------

- Updated to upstream release 2.1.2_, for which there is no upstream
  changelog available (apart from the VCS history).

**Note:** While this release has been tagged as ``2.1.2`` by upstream,
the actual version number shown by the Barrier programs is ``2.2.0``.

2.1.1-2 - 2018-05-30
--------------------

- Work around Barrier `issue 49`_.

2.1.1-1 - 2018-05-20
--------------------

- Updated to upstream release 2.1.1_, which contains the following
  changes:

  * Fixed ``.desktop`` file.


.. _2.1.1: https://github.com/debauchee/barrier/releases/tag/v2.1.1
.. _2.1.2: https://github.com/debauchee/barrier/releases/tag/v2.1.2
.. _2.3.0: https://github.com/debauchee/barrier/releases/tag/v2.3.0
.. _2.3.1: https://github.com/debauchee/barrier/releases/tag/v2.3.1
.. _2.3.2: https://github.com/debauchee/barrier/releases/tag/v2.3.2
.. _issue 49: https://github.com/debauchee/barrier/issues/49
