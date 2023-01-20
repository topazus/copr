%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname fd

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A simple, fast and user-friendly alternative to 'find'

License:        ASL 2.0 or MIT
URL:            https://github.com/sharkdp/fd
#Source:

BuildRequires:  gcc-c++ pkg-config git

%description
A simple, fast and user-friendly alternative to 'find'

%prep
git clone --depth=1 %{url} .

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
export PATH="$HOME/.cargo/bin:$PATH"
cargo build --release

%install
install -pDm755 target/release/fd %{buildroot}%{_bindir}/%{appname}

make completions
install -pDm644 autocomplete/fd.bash %{buildroot}%{_datadir}/bash-completion/completions/%{appname}
install -pDm644 autocomplete/_fd %{buildroot}%{_datadir}/zsh/site-functions/_%{appname}
install -pDm644 autocomplete/fd.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{appname}.fish

install -pDm644 doc/fd.1 %{buildroot}%{_mandir}/man1/%{appname}.1

%check

%files
%{_bindir}/%{appname}

%{_datadir}/bash-completion/completions/%{appname}
%{_datadir}/zsh/site-functions/_%{appname}
%{_datadir}/fish/vendor_completions.d/%{appname}.fish

%changelog
