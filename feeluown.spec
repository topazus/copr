# Created by pyp2rpm-3.3.8
%global pypi_name feeluown
%global pypi_version 3.8.9

Name:           %{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        a robust, user-friendly and hackable music player

License:        GPL-3.0
URL:            https://github.com/feeluown/FeelUOwn
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(pylint)
BuildRequires:  python-qt5
#BuildRequires:  python3dist(pyqt5-stubs)
BuildRequires:  python3dist(pytest) >= 5.4
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-benchmark) >= 3.4.1
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-mock)
#BuildRequires:  python3dist(pytest-qt)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%description
a robust, user-friendly and hackable music player

Requires:       python3dist(fuo-kuwo) >= 0.1.1
Requires:       python3dist(fuo-netease) >= 0.4.2
Requires:       python3dist(fuo-qqmusic) >= 0.2
Requires:       python3dist(janus)
Requires:       python3dist(mutagen) >= 1.37
Requires:       python3dist(packaging)
Requires:       python3dist(pydantic) >= 1.8.1
Requires:       python3dist(pyobjc-framework-cocoa)
Requires:       python3dist(pyobjc-framework-quartz)
Requires:       python3dist(pyqtwebengine)
Requires:       python3dist(pyshortcuts)
#Requires:       python3dist(qasync)
Requires:       python3dist(requests)
Requires:       python3dist(setuptools)
Requires:       python3dist(tomlkit)
Requires:       mpv-devel

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/feeluown
%{_bindir}/feeluown-genicon
%{_bindir}/fuo
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/mpv.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Dec 20 2022 topazus <topazus@outlook.com> - 3.8.9-1
- Initial package.
