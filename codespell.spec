# Created by pyp2rpm-3.3.8
%global pypi_name codespell
%global pypi_version 2.2.2

Name:          %{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        check code for common misspellings

License:        GPL v2
URL:            None
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(chardet)
BuildRequires:  python3dist(check-manifest)
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
#BuildRequires:  python3dist(pytest-dependency)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tomli)
BuildRequires:  python3dist(tomli)

%description
check code for common misspellings

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(chardet)
Requires:       python3dist(setuptools)
Requires:       python3dist(tomli)
%description -n python3-%{pypi_name}
check code for common misspellings


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

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/codespell
%{python3_sitelib}/bin
%{python3_sitelib}/codespell_lib
%{python3_sitelib}/%{pypi_name}-0.0.0-py%{python3_version}.egg-info


%changelog
* Tue Dec 20 2022 topazus <topazus@outlook.com> - 2.2.2-1
- Initial package.
