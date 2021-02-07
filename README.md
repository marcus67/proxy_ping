![UnderConstruction](doc/logo_under_construction_sign_wide.png)

# Ping Through Proxy Utility `ProxyPing`

## Overview

## Contact

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

| Status              | Master                                                                                                                                                                                                                                                                                                                                                               | Mac OS Test                                                                                                                                                                                       | Release                                                                                                                                                                                                                                                                                                                                                              |
|:------------------- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CircleCI            | <A HREF="https://circleci.com/gh/marcus67/proxy_ping/tree/master"><IMG SRC="https://img.shields.io/circleci/project/github/marcus67/proxy_ping/master.svg?label=master"></A>                                                                                                                                                                                 | <A HREF="https://circleci.com/gh/marcus67/proxy_ping/tree/master"><IMG SRC="https://img.shields.io/circleci/project/github/marcus67/proxy_ping/fb-rickert-beethoven.svg?label=MacOS"></A> | <A HREF="https://circleci.com/gh/marcus67/proxy_ping/tree/release"><IMG SRC="https://img.shields.io/circleci/project/github/marcus67/proxy_ping/release.svg?label=release"></A>                                                                                                                                                                              |
| Test Coverage       | <A HREF="https://codecov.io/gh/marcus67/proxy_ping/branch/master"><IMG SRC="https://img.shields.io/codecov/c/github/marcus67/proxy_ping.svg?label=master"></A>                                                                                                                                                                                               | <A HREF="https://codecov.io/gh/marcus67/proxy_ping/branch/release"><IMG SRC="https://img.shields.io/codecov/c/github/marcus67/proxy_ping/fb-rickert-beethoven.svg?label=MacOS"></A>       | <A HREF="https://codecov.io/gh/marcus67/proxy_ping/branch/release"><IMG SRC="https://img.shields.io/codecov/c/github/marcus67/proxy_ping/release.svg?label=release"></A>                                                                                                                                                                                     |
| Snyk Vulnerability  | <A href="https://snyk.io/test/github/marcus67/proxy_ping?targetFile=requirements.txt"><img src="https://snyk.io/test/github/marcus67/proxy_ping/badge.svg?targetFile=requirements.txt" alt="Known Vulnerabilities" data-canonical-src="https://snyk.io/test/github/marcus67/proxy_ping?targetFile=requirements.txt" style="max-width:100%;"></a>         | not available                                                                                                                                                                                     | <A href="https://snyk.io/test/github/marcus67/proxy_ping?targetFile=requirements.txt"><img src="https://snyk.io/test/github/marcus67/proxy_ping/release/badge.svg?targetFile=requirements.txt" alt="Known Vulnerabilities" data-canonical-src="https://snyk.io/test/github/marcus67/proxy_ping?targetFile=requirements.txt" style="max-width:100%;"></a> |
| Codacy Code Quality | <A href="https://www.codacy.com/app/marcus67/proxy_ping?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=marcus67/proxy_ping&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/3e3130c1c450404db9b16e10ab8af7fd"/></a>                                                                                         | not available                                                                                                                                                                                     | <A href="https://www.codacy.com/app/marcus67/proxy_ping?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=marcus67/proxy_ping&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/3e3130c1c450404db9b16e10ab8af7fd?branch=release"/></a>                                                                          |

Note: The vulnerability status is derived from the Python PIP packages found in `requirements.txt`.

## Features

## Tested Distributions

So far, `ProxyPing` has only been released as a Debian package. For other non-Debian based distributions 
there is some basic support using a generic installation script. 

| Distribution | Version       | Architecture | Comments                                                               | Most Recent Test |
| ------------ | ------------- | ------------ | ---------------------------------------------------------------------- | ---------------- |
| Debian       | 10.3 (buster) | amd64        | Feedback from a user as regular install with Mate desktop              |  |

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

### Troubleshooting

## Caveats

## Credits
