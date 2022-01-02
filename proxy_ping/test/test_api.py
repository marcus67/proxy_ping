# -*- coding: utf-8 -*-

#    Copyright (C) 2021  Marcus Rickert
#
#    See https://github.com/marcus67/proxy_ping
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os

from python_base_app.test import base_test
from python_base_app import pinger

from proxy_ping import status_server
from proxy_ping import app


class TestApi(base_test.BaseTestCase):

    @classmethod
    def default_pinger(cls):
        return pinger.Pinger(p_config=pinger.PingerConfigModel(), p_default_port=6666)

    @classmethod
    def default_server(cls):

        config = status_server.StatusServerConfigModel()
        config.port = int(os.getenv("PING_API_SERVER_PORT", "6660"))
        server = status_server.StatusServer(p_config=config, p_pinger=cls.default_pinger(),
                                            p_package_name=app.PACKAGE_NAME)

        return server


    @base_test.skip_if_env("NO_PING")
    def test_api_one_hop_ping_success(self):

        default_server = None

        try:
            default_server = self.default_server()
            default_pinger = self.default_pinger()

            default_server.start_server()

            ping_url = "localhost:{port},web.de"
            delay = default_pinger.ping(ping_url.format(port=default_server._config.port))

            self.assertIsNotNone(delay)
            self.assertTrue(delay > 1)
            self.assertTrue(delay < 100)

        except Exception as e:
            raise e

        finally:
            if default_server is not None:
                default_server.stop_server()
                default_server.destroy()
