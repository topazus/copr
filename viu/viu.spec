%global debug_package %{nil}
%define build_date %{lua: print(os.date("%Y%m%d"))}
%global appname viu
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_date}%{?dist}
Summary:        Simple terminal image viewer written in Rust
License:        MIT
URL:            https://github.com/atanunq/viu
Source0:        %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ cargo

%description
Simple terminal image viewer written in Rust.

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release

%install
install -pDm755 target/release/viu %{buildroot}%{_bindir}/%{appname}

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE-MIT
%doc README.md
%{_bindir}/%{appname}

%changelog
