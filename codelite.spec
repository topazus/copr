%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname codelite

Name:           codelite
Version:        16.0.0
Release:        1%{?dist}
Summary:        A cross platform C/C++/PHP and Node.js IDE written in C++
License:        GPL 2.0
URL:            https://github.com/eranif/codelite
Source:         https://github.com/eranif/codelite/archive/refs/tags/%{version}.tar.gz

BuildRequires: gcc-c++ cmake pkg-config
BuildRequires: wxGTK-devel libssh-devel sqlite-devel gtk3-devel wxBase-devel wxGTK3-devel hunspell-devel glib2-devel lldb-devel

Requires:      wxGTK xterm sdl12-compat

%description
CodeLite is a free, open source, cross platform IDE specialized in C, C++, PHP and JavaScript (mainly for backend developers using Node.js) programming languages, which runs best on all major platforms (Windows, macOS and Linux).

%prep
%autosetup -n codelite-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DCOPY_WX_LIBS=1
%cmake_build

%install
%cmake_install

%files
%{_bindir}/codelite*
/usr/bin/ctagsd
/usr/bin/ctagsd-tests

%{_datadir}/applications/*.desktop

%dir %{_libdir}/codelite/
%{_libdir}/codelite/*
%dir %{_datadir}/codelite/
%{_datadir}/codelite/*

%{_datadir}/icons/hicolor/*/apps/codelite.png

/usr/share/locale/cs/LC_MESSAGES/codelite.mo
/usr/share/locale/ja_JP/LC_MESSAGES/codelite.mo
/usr/share/locale/ru_RU/LC_MESSAGES/codelite.mo
/usr/share/locale/zh_CN/LC_MESSAGES/codelite.mo

%{_datadir}/man/man1/codelite*.1.gz

%changelog
