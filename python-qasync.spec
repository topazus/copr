# Created by pyp2rpm-3.3.8
%global pypi_name qasync
%global pypi_version 0.23.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Implementation of the PEP 3156 Event-Loop with Qt

License:        BSD
URL:            https://github.com/CabbageDevelopment/qasync
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Python library for using asyncio in Qt-based applications.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python library for using asyncio in Qt-based applications.


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Dec 20 2022 topazus <topazus@outlook.com> - 0.23.0-1
- Initial package.
