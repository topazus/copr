%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname bottom

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Yet another cross-platform graphical process/system monitor
License:        MIT
URL:            https://github.com/ClementTsang/bottom
Source0:        %{url}/archive/master/%{appname}-master.tar.gz
#Source1:

BuildRequires:  gcc-c++ pkg-config git wget

%description
Yet another cross-platform graphical process/system monitor.

%prep
git clone --depth=1 https://github.com/ClementTsang/bottom .

wget https://github.com/ClementTsang/bottom/releases/download/nightly/completion.tar.gz
tar xvf completion.tar.gz

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
$HOME/.cargo/bin/cargo build --release

%install
install -pDm755 target/release/btm %{buildroot}%{_bindir}/%{appname}

install -pDm644 btm.bash %{buildroot}%{_datadir}/bash-completion/completions/%{appname}
install -pDm644 _btm %{buildroot}%{_datadir}/zsh/site-functions/_%{appname}
install -pDm644 btm.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{appname}.fish

%check

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%{_datadir}/bash-completion/completions/%{appname}
%{_datadir}/zsh/site-functions/_%{appname}
%{_datadir}/fish/vendor_completions.d/%{appname}.fish

%changelog
