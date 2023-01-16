
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname vimiv-qt
%bcond_with tests

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Image viewer with vim-like keybindings
License:        GPL-3.0
URL:            https://github.com/karlch/vimiv-qt
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc make
BuildRequires: python3-qt5-devel desktop-file-utils

Requires: python3-piexif

%description
An image viewer with vim-like keybindings.

%prep
%autosetup -n %{appname}-master -p1
cp misc/Makefile .

%build
%py3_install

%install
%py3_install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%check
%if %{with tests}
%pytest
%endif

%files
/usr/share/licenses/vimiv/LICENSE
%{_bindir}/vimiv
#/usr/lib64/python3.9/site-packages
%{python3_sitearch}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/man/man1/*.1.gz
%{_datadir}/metainfo/*.xml

%changelog
