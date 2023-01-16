%global debug_package %{nil}

Name:           crystal
Version:        0.17.1
Release:        1%{?dist}
Summary:        Dependency manager for the Crystal language
License:        Apache
URL:            https://github.com/crystal-lang/shards
Source:         https://github.com/crystal-lang/shards/archive/v%{version}.tar.gz

BuildRequires:  gcc make crystal
BuildRequires:  libevent-devel pcre-devel gc-devel openssl-devel zlib-devel libyaml-devel
BuildRequires:  wget tar

%description
Dependency manager for the Crystal language

%prep
%autosetup -n %{name}-%{version} -p1

%build
make release=1

%install

%check

%files


%changelog
