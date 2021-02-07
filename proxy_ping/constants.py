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

import os.path

DIR_NAME = 'proxy-ping'
APPLICATION_USER = 'proxy-ping'

DEFAULT_PORT=6666

API_URL = "/api"
API_REL_URL_EVENTS = "events"
API_URL_EVENTS = os.path.join(API_URL, API_REL_URL_EVENTS)

API_REL_URL_STATUS = "status"
API_URL_STATUS = os.path.join(API_URL, API_REL_URL_STATUS)

API_URL_PARAM_USERNAME = "username"

HTTP_STATUS_CODE_OK = 200
HTTP_STATUS_CODE_UNAUTHORIZED = 401
HTTP_STATUS_CODE_NOT_FOUND = 404

LANGUAGES = {
    'en': 'English',
}
