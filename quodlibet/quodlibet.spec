%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname quodlibet
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Music player and music library manager for Linux, Windows, and macOS
License:        GPL-2.0
URL:            https://github.com/quodlibet/quodlibet
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ desktop-file-utils make
BuildRequires: python3-devel python3-setuptools
BuildRequires: gettext-devel sphinx sphinxbase-devel
BuildRequires: python3-pytest python3-flake8 python3-polib

Requires: pygobject2 python3-cairo python3-mutagen gtk3 libsoup
Requires: python3-feedparser

Requires: gstreamer1-devel gstreamer1-plugins-base-tools gstreamer1-plugins-base-devel gstreamer1-plugins-good gstreamer1-plugins-good-extras gstreamer1-plugins-ugly-free gstreamer1-plugins-bad-free gstreamer1-plugins-bad-free-devel gstreamer1-plugins-bad-free-extras

Recommends: python3-dbus keybinder3

%description

%prep
%autosetup -n %{appname}-master -p1

%build
%py3_build

%install
%py3_install


desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license COPYING
%{_bindir}/%{appname}
%{_bindir}/exfalso
%{_bindir}/operon
%{_datadir}/applications/*.desktop

%{_datadir}/icons/hicolor/*/apps/io.github.quodlibet.ExFalso.png
%{_datadir}/icons/hicolor/*/apps/io.github.quodlibet.QuodLibet.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg

%{_datadir}/locale/*/LC_MESSAGES/quodlibet.mo

%{python3_sitelib}/%{appname}/*
%{python3_sitelib}/*.egg-info

%{_datadir}/bash-completion/completions/operon
%{_datadir}/bash-completion/completions/quodlibet
%{_datadir}/zsh/site-functions/_quodlibet
%{_datadir}/man/man1/exfalso.1.gz
%{_datadir}/man/man1/operon.1.gz
%{_datadir}/man/man1/quodlibet.1.gz

%{_datadir}/dbus-1/services/net.sacredchao.QuodLibet.service
%{_datadir}/gnome-shell/search-providers/io.github.quodlibet.QuodLibet-search-provider.ini

%{_datadir}/appdata/*.appdata.xml


%changelog
