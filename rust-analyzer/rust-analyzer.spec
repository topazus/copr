%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname rust-analyzer

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A Rust compiler front-end for IDEs
License:        ASL 2.0
URL:            https://rust-analyzer.github.io/
Source:         https://github.com/rust-analyzer/rust-analyzer/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ cargo

%description
rust-analyzer is a modular compiler frontend for the Rust language. It is a part of a larger rls-2.0 effort to create excellent IDE support for Rust.

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release

%install
install -pDm755 target/release/rust-analyzer %{buildroot}%{_bindir}/rust-analyzer

%check

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
