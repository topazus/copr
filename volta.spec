%global debug_package %{nil}
%bcond_without check
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname volta

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Volta: JS Toolchains as Code. ⚡

License:        GPL
URL:            https://github.com/volta-cli/volta
Source:         https://github.com/volta-cli/volta/archive/main/%{appname}-main.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  openssl-devel

%global _description %{expand:
The Hassle-Free JavaScript Tool Manager.}

%description %{_description}

%prep
%autosetup -n %{appname}-main -p1

%build
cargo build --release

%install
install -pDm755 target/release/{volta,volta-migrate,volta-shim} -t %{buildroot}%{_bindir}

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/volta*

%changelog
