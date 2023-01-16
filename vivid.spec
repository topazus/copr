%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname vivid

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A themeable LS_COLORS generator with a rich filetype datebase
License:        ASL 2.0 or MIT
URL:            https://github.com/sharkdp/vivid
Source:         https://github.com/sharkdp/vivid/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ make pkg-config

%description
vivid is a generator for the LS_COLORS environment variable that controls the colorized output of ls, tree, fd, bfs, dust and many other tools.

%prep
%autosetup -n %{appname}-master -p1

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
$HOME/.cargo/bin/cargo build --release

%install
install -pDm755 target/release/vivid %{buildroot}%{_bindir}/%{appname}
install -pDm644 themes/*.yml -t %{buildroot}%{_datadir}/%{appname}

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%dir %{_datadir}/%{appname}
%{_datadir}/%{appname}/*.yml

%changelog
