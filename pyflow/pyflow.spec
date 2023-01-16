%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname pyflow
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        An installation and dependency system for Python
License:        MIT
URL:            https://github.com/David-OConnor/pyflow
Source:         https://github.com/David-OConnor/pyflow/archive/master/%{appname}-master.tar.gz

BuildRequires: cargo pkg-config


%description
Pyflow streamlines working with Python projects and files. It's an easy-to-use CLI app with a minimalist API. Never worry about having the right version of Python or dependencies.

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release

%install
install -pDm755 target/release/pyflow %{buildroot}%{_bindir}/pyflow

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}


%changelog
