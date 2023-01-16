%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname procs
%bcond_without check

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A modern replacement for ps written in Rust
License:        MIT
URL:            https://github.com/dalance/procs
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ git

%description
procs is a replacement for ps written in Rust.

%prep
git clone --depth 1 %{url} .

if [ ! -d $HOME/.cargo ]; then
    curl https://sh.rustup.rs -sSf | sh -s -- -y
fi

%build
$HOME/.cargo/bin/cargo build --release

%install
install -pDm0755 target/release/procs %{buildroot}%{_bindir}/procs

%if %{with check}
%check

%endif

%files
%{_bindir}/%{appname}

%changelog
