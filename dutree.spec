%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global _name dutree

Name:          %{_name}-git
Version:       0.0.0
Release:       %{build_timestamp}%{?dist}
Summary:       tool to analyze file system usage written in Rust
License:       GNU General Public License v3.0
URL:           https://github.com/nachoparker/dutree
Source0:       %{url}/archive/master/%{_name}-master.tar.gz

BuildRequires: cargo

%description
a tool to analyze file system usage written in Rust.

%prep
%autosetup -n %{_name}-master -p1

%build

cargo build --release

%install
install -p -D -m755 target/release/dutree %{buildroot}%{_bindir}/dutree

%check
cargo test

%files
%license LICENSE
%doc README.md
%{_bindir}/dutree

%changelog
