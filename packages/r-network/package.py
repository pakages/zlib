# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RNetwork(RPackage):
    """Classes for Relational Data.

    Tools to create and modify network objects. The network class can represent
    a range of relational data types, and supports arbitrary vertex/edge/graph
    attributes."""

    cran = "network"

    version('1.17.1', sha256='fc3c3a0014f8895a11c33994c9b44c6ef6cc49c7d026cd41ae6bba5ef63005a7')
    version('1.16.1', sha256='eb6435794cacc81abe1664391e8dcf1c10112bbb76fff9016dd6dbb8e83efeb1')
    version('1.15', sha256='5cbe5c0369e5f8363e33a86f14fd33ce8727166106381627ecd13b7452e14cb3')
    version('1.14-377', sha256='013c02f8d97f1f87f2c421760534df9353d2a8c2277f20b46b59fb79822d3e46')
    version('1.13.0', sha256='7a04ea89261cdf32ccb52222810699d5fca59a849053e306b5ec9dd5c1184f87')

    depends_on('r@2.10:', type=('build', 'run'))
    depends_on('r-tibble', type=('build', 'run'), when='@1.14-377:')
    depends_on('r-magrittr', type=('build', 'run'), when='@1.14-377:')
    depends_on('r-statnet-common@4.5:', type=('build', 'run'), when='@1.17.1:')