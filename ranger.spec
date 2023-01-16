%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname ranger
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A VIM-inspired filemanager for the console
License:        GPL-3.0
URL:            https://github.com/ranger/ranger
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ desktop-file-utils make
BuildRequires:  python3-devel python3-setuptools python3-pytest
BuildRequires:  python3-astroid python3-pylint
Requires:  python3-chardet python3-filetype

Recommends:  caca-utils ImageMagick poppler
Recommends:  highlight python3-pygments
Recommends:  w3m-img

%description
ranger is a console file manager with VI key bindings. It provides a minimalistic and nice curses interface with a view on the directory hierarchy. It ships with rifle, a file launcher that is good at automatically finding out which program to use for what file type.

%prep
%autosetup -n %{appname}-master -p1
	
# Replace python shebangs to make them compatible with fedora
find -type f -name "*.py" -exec sed -e 's|/usr/bin/env python|%{__python3}|g'   \
                                    -i "{}" \;

%build
%py3_build

%install
%py3_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%if %{with check}
%check
%pytest
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_bindir}/rifle
%{python3_sitelib}/%{appname}/*
%{python3_sitelib}/*.egg-info/*
%{_datadir}/applications/*.desktop
%{_datadir}/doc/ranger/*
%{_datadir}/man/man1/ranger.1.gz
%{_datadir}/man/man1/rifle.1.gz

%changelog
