# Created by pyp2rpm-3.3.8
%global pypi_name semver
%global pypi_version 3.0.0.dev3

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python helper for Semantic Versioning

License:        BSD
URL:            https://github.com/python-semver/python-semver
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tox)
BuildRequires:  python3dist(virtualenv)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(tox-current-env)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)

%description
Python helper for Semantic Versioning

%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files
%{_bindir}/pysemver
%{python3_sitelib}/semver
%{python3_sitelib}/semver-*.dist-info

%changelog
