%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname s-tui

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Terminal-based CPU stress and monitoring utility
License:        GPL-2.0
URL:            https://github.com/amanusk/s-tui
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ python3-setuptools python3-devel git
BuildRequires:  python3-pytest python3-urwid python3-psutil

Requires:       python3-urwid python3-psutil

Recommends:     stress stress-ng

%description
Stress-Terminal UI, s-tui, monitors CPU temperature, frequency, power and utilization in a graphical way from the terminal.

%prep
git clone --depth=1 https://github.com/amanusk/s-tui .

%build
%py3_build

%install
%py3_install

%check

%files
%{_bindir}/%{appname}
%{python3_sitelib}/s_tui/*
%{python3_sitelib}/s_tui-*.egg-info/*

%changelog
