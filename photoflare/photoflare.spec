%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global _name photoflare

Name:          %{_name}-git
Version:       0.0.0
Release:       %{build_timestamp}%{?dist}
Summary:       Fast static site generator in a single binary with everything built-in
License:       MIT and ASL 2.0
URL:           https://github.com/PhotoFlare/photoflare
Source0:       %{url}/archive/master/%{_name}-master.tar.gz

BuildRequires: gcc

%global _description %{expand:
A fast static site generator in a single binary with everything built-in.}

%description %{_description}

%prep
%autosetup -n %{_name}-master -p1

%build

cargo build --release

%install
install -p -D -m755 target/release/dutree %{buildroot}%{_bindir}/dutree

%check
$HOME/.cargo/bin/cargo test

%files
%license LICENSE
%doc README.md
%{_bindir}/dutree

%changelog
