%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname dust

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A more intuitive version of du in rust
License:        ASL 2.0
URL:            https://github.com/bootandy/dust
Source:         https://github.com/bootandy/dust/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ make pkg-config

%description
du + rust = dust. Like du but more intuitive.

%prep
%autosetup -n %{appname}-master -p1

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
$HOME/.cargo/bin/cargo build --release

%install
install -pDm755 target/release/dust %{buildroot}%{_bindir}/%{appname}

%check


%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
