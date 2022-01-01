![UnderConstruction](doc/logo_under_construction_sign_wide.png)

![ProxyPingLogo](doc/proxy_ping_logo_256x256.png)

# Ping Through Proxy Utility `ProxyPing`

## Overview

The utility `ProxyPing` is a simple tool to ping servers behind a firewall that will not let ICMP packages 
through. It provides a HTTP server answering to ping requests and returning the ping delay as a HTTP text result. The
tool will have to be deployed on a server behind the firewall that can be reached by a configurable TCP
connection (defaulting to port TCP 6666).

Suppose the tool is deployed on server `my.proxy.behind.wall` and the server to be pinged is called `some.other.server`
the required HTTP query will have to look like this:

    http://my.proxy.behind.wall/api/ping?host=some.other.server 

## Change History

See [here](CHANGES.md)

## GitHub Status

<A HREF="https://github.com/marcus67/proxy_ping">
<IMG SRC="https://img.shields.io/github/forks/marcus67/proxy_ping.svg?label=forks"></A> 
<A HREF="https://github.com/marcus67/proxy_ping/stargazers">
<IMG SRC="https://img.shields.io/github/stars/marcus67/proxy_ping.svg?label=stars"></A> 
<A HREF="https://github.com/marcus67/proxy_ping/watchers">
<IMG SRC="https://img.shields.io/github/watchers/marcus67/proxy_ping.svg?label=watchers"></A> 
<A HREF="https://github.com/marcus67/proxy_ping/issues">
<IMG SRC="https://img.shields.io/github/issues/marcus67/proxy_ping.svg"></A> 
<A HREF="https://github.com/marcus67/proxy_ping/pulls">
<IMG SRC="https://img.shields.io/github/issues-pr/marcus67/proxy_ping.svg"></A>

## SourceForge Download Status

<a href="https://sourceforge.net/projects/proxy-ping/files/latest/download">
<img alt="Download ProxyPing" src="https://img.shields.io/sourceforge/dm/proxy-ping.svg"></a>

## Continuous Integration Status Overview

| Status              | Main                                                                                                                                                                                                                                                                                                                                                                 | Release                                                                                                                                                                                                                                                                                                                                                              |
|:------------------- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CircleCI            | <A HREF="https://circleci.com/gh/marcus67/proxy_ping/tree/main"><IMG SRC="https://img.shields.io/circleci/project/github/marcus67/proxy_ping/main.svg?label=main"></A>                                                                                                                                                                                               | <A HREF="https://circleci.com/gh/marcus67/proxy_ping/tree/release"><IMG SRC="https://img.shields.io/circleci/project/github/marcus67/proxy_ping/release.svg?label=release"></A>                                                                                                                                                                                      |
| Test Coverage       | <A HREF="https://codecov.io/gh/marcus67/proxy_ping/branch/main"><IMG SRC="https://img.shields.io/codecov/c/github/marcus67/proxy_ping.svg?label=main"></A>                                                                                                                                                                                                           | <A HREF="https://codecov.io/gh/marcus67/proxy_ping/branch/release"><IMG SRC="https://img.shields.io/codecov/c/github/marcus67/proxy_ping/release.svg?label=release"></A>                                                                                                                                                                                             |
| Snyk Vulnerability  | <A href="https://snyk.io/test/github/marcus67/proxy_ping?targetFile=requirements.txt"><img src="https://snyk.io/test/github/marcus67/proxy_ping/badge.svg?targetFile=requirements.txt" alt="Known Vulnerabilities" data-canonical-src="https://snyk.io/test/github/marcus67/proxy_ping?targetFile=requirements.txt" style="max-width:100%;"></a>                     | <A href="https://snyk.io/test/github/marcus67/proxy_ping?targetFile=requirements.txt"><img src="https://snyk.io/test/github/marcus67/proxy_ping/release/badge.svg?targetFile=requirements.txt" alt="Known Vulnerabilities" data-canonical-src="https://snyk.io/test/github/marcus67/proxy_ping?targetFile=requirements.txt" style="max-width:100%;"></a>             |
| Codacy Code Quality | <A href="https://www.codacy.com/app/marcus67/proxy_ping?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=marcus67/proxy_ping&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/ecd13aa7d67b4651838b35882fe014f4"/></a>                                                                                                 | <A href="https://www.codacy.com/app/marcus67/proxy_ping?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=marcus67/proxy_ping&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/ecd13aa7d67b4651838b35882fe014f4?branch=release"/></a>                                                                                  |

Note: The vulnerability status is derived from the Python PIP packages found in `requirements.txt`.

## Features

## Tested Distributions

So far, `ProxyPing` has only been released as a Debian package. For other non-Debian based distributions 
there is some basic support using a generic installation script. 

| Distribution | Version       | Architecture | Comments                                                               | Most Recent Test |
| ------------ | ------------- | ------------ | ---------------------------------------------------------------------- | ---------------- |
| Debian       | debian/sid    | amd64        |                                                                        | 2021-02-13       |

## Quick Install (Debian Package)

This guide will take you through the steps required to install, configure, and run the `ProxyPing` application 
on your system. 

### Download the Software

The application is available as a Debian package 
from the [`release`](https://sourceforge.net/projects/proxy-ping/files/release/) directory at SourceForge. 
The latest build is available from the [`master`](https://sourceforge.net/projects/proxy-ping/files/master/) 
directory. Install it as you would install any other Debian package with

    dpkg -i PACKAGE.deb
    apt-get install -f

Note that the second command is required to install missing dependencies since `dpkg` does not run a dependency check.
Instead, it will return with an error which will then be "fixed" by `apt-get`. 

After installation use

    systemctl start proxy-ping

to start the application right away. The application will 
successfully start up provided that the default port 6666 is available on the host. 

### Configuring the Application (Mostly Optional)

The application is configured using the file [`/etc/proxy-ping/proxy-ping.config`](etc/proxy-ping.template.config).
The default values should work for most contexts. This will bring up the server on port 6666.


## Credits

*   Thanks to all the people maintaining the wonderful script language [Python](https://www.python.org/) 
    and the libraries on [PyPi](https://pypi.org/).
