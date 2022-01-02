# -*- coding: utf-8 -*-

# Copyright (C) 2021  Marcus Rickert
#
# See https://github.com/marcus67/proxy_ping
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

settings = {
    "name": "proxy-ping",
    "url": "https://github.com/marcus67/proxy_ping",
    "version": "0.1.1",
    "description": "Tool to ping hosts behind a proxy blocking ICMP packages.",
    "author": "Marcus Rickert",
    "author_email": "proxy-ping@web.de",
}

extended_settings = {
    "display_url": "github.com/marcus67/proxy_ping",
    "debian_package_revision": "3",
    "debian_package_architecture": "all",
}

RELEASE_BRANCH_NAME = "release"
MASTER_BRANCH_NAME = "main"

SOURCEFORGE_CHANNELS = [
    MASTER_BRANCH_NAME,
    RELEASE_BRANCH_NAME
]

DOCKER_CHANNELS = [
    MASTER_BRANCH_NAME,
    RELEASE_BRANCH_NAME
]
