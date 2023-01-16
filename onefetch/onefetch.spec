%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global _name onefetch

Name:           %{_name}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Git repository summary on your terminal
License:        MIT
URL:            https://github.com/o2sh/onefetch
Source:         %{url}/archive/master/%{_name}-master.tar.gz

BuildRequires: cargo

%description
A command-line Git information tool written in Rust.

%prep
%autosetup -n %{_name}-master -p1

%build
cargo build --release --all-features

%install
install -p -D -m755 target/release/%{_name} %{buildroot}%{_bindir}/%{_name}

%check
cargo test

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{_name}


%changelog
