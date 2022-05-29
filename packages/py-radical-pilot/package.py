# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRadicalPilot(PythonPackage):
    """RADICAL-Pilot is a Pilot system specialized in executing applications
    composed of many computational tasks on high performance computing (HPC)
    platforms."""

    homepage = 'https://radical-cybertools.github.io'
    git      = 'https://github.com/radical-cybertools/radical.pilot.git'
    pypi     = 'radical.pilot/radical.pilot-1.11.2.tar.gz'

    maintainers = ['andre-merzky']

    version('develop', branch='devel')
    version('1.11.2',  sha256='9d239f747589b8ae5d6faaea90ea5304b6f230a1edfd8d4efb440bc3799c8a9d')
    version('1.10.2',  sha256='56e9d8b1ce7ed05eff471d7df660e4940f485027e5f353aa36fd17425846a499')
    version('1.10.1',  sha256='003f4c519b991bded31693026b69dd51547a5a69a5f94355dc8beff766524b3c')
    version('1.9.2',   sha256='7c872ac9103a2aed0c5cd46057048a182f672191e194e0fd42794b0012e6e947')
    version('1.8.0',   sha256='a4c3bca163db61206e15a2d820d9a64e888da5c72672448ae975c26768130b9d')
    version('1.6.8',   sha256='fa8fd3f348a68b54ee8338d5c5cf1a3d99c10c0b6da804424a839239ee0d313d')
    version('1.6.7',   sha256='6ca0a3bd3cda65034fa756f37fa05681d5a43441c1605408a58364f89c627970')

    depends_on('py-radical-utils',        type=('build', 'run'))
    depends_on('py-radical-saga',         type=('build', 'run'))

    depends_on('py-radical-utils@1.8.4:', type=('build', 'run'), when='@1.11:')
    depends_on('py-radical-saga@1.8.0:',  type=('build', 'run'), when='@1.11:')

    depends_on('python@3.6:',             type=('build', 'run'))
    depends_on('py-pymongo@:3',           type=('build', 'run'))
    depends_on('py-setproctitle',         type=('build', 'run'))
    depends_on('py-setuptools',           type='build')
