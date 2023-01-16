# Created by pyp2rpm-3.3.8
%global pypi_name archey4
%global pypi_version 4.14.0.1

#if 0%{?fedora}
#%global debug_package %{nil}
#%endif

Name:           %{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        a simple system information tool written in Python

License:        GPLv3
URL:            https://github.com/HorlogeSkynet/archey4
# https://pypi.io/packages/source/<package_name_first_letter>/<package_name>/<package_name>-<package_version>.tar.gz
%if 0%{?fedora}
Source0:        %{pypi_source}
%elif 0%{?suse_version}
source0:        https://pypi.io/packages/source/a/%{pypi_name}/%{pypi_name}-%{pypi_version}.tar.gz
%endif
#Source0:        https://files.pythonhosted.org/packages/source/a/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  (python3dist(distro) >= 1.3 with python3dist(distro) < 2)
BuildRequires:  (python3dist(netifaces) >= 0.10 with python3dist(netifaces) < 1)
BuildRequires:  python3dist(setuptools)

%if 0%{?fedora}
Requires:       lm_sensors procps-ng
%elif 0%{?suse_version}
Requires:       sensors procps
%endif
Requires:       python3-distro python3-netifaces
Requires:       pciutils bind-utils wmctrl virt-what

%description
a simple system information tool written in Python

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%license LICENSE
%doc README.md
/usr/share/doc/archey4/CHANGELOG.md
/usr/share/doc/archey4/COPYRIGHT.md
/usr/share/doc/archey4/README.md
%{_bindir}/archey
%{python3_sitelib}/archey
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%{_mandir}/man1/archey.1.gz

%changelog
