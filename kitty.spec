# Created by pyp2rpm-3.3.8
%global pypi_name kitty
%global pypi_version 1.2.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        nested list printer program

License:        None
URL:            http://www.headfirstlabs.com
Source0:        %{pypi_source %{pypi_name} %{version} zip}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
UNKNOWN

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
UNKNOWN


%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Dec 20 2022 topazus <topazus@outlook.com> - 1.2.0-1
- Initial package.
