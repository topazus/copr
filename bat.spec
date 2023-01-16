%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname bat

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Cat(1) clone with wings

License:        ASL 2.0 or MIT
URL:            https://github.com/sharkdp/bat
#Source:

BuildRequires:  gcc-c++ pkg-config git

%description
A cat(1) clone with syntax highlighting and Git integration.

%prep
git clone --depth=1 https://github.com/sharkdp/bat .

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
export PATH="$HOME/.cargo/bin:$PATH"
cargo build --release

%install
install -pDm755 target/release/%{appname} %{buildroot}%{_bindir}/%{appname}

install -pDm644 assets/manual/bat.1.in %{buildroot}%{_mandir}/%{appname}.1

install -pDm644 assets/completions/bat.bash.in %{buildroot}%{_datadir}/bash-completion/completions/%{appname}
install -pDm644 assets/completions/bat.zsh.in %{buildroot}%{_datadir}/zsh/site-functions/_%{appname}
install -pDm644 assets/completions/bat.fish.in %{buildroot}%{_datadir}/fish/vendor_completions.d/%{appname}.fish

%check


%files
%{_bindir}/%{appname}

%{_mandir}/%{appname}.1
%{_datadir}/bash-completion/completions/%{appname}
%{_datadir}/zsh/site-functions/_%{appname}
%{_datadir}/fish/vendor_completions.d/%{appname}.fish

%changelog
