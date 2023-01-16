%global debug_package %{nil}
%global build_timestamp %(date +%Y.%m.%d)
%global appname hyperfine

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A command-line benchmarking tool

License:        MIT
URL:            https://github.com/sharkdp/hyperfine
#Source:

BuildRequires:  gcc pkg-config git

%description
A command-line benchmarking tool

%prep
git clone --depth=1 https://github.com/sharkdp/hyperfine .

# install rust
if [ ! -d $HOME/.cargo ]; then
    curl https://sh.rustup.rs -sSf | sh -s -- -y
fi

%build
$HOME/.cargo/bin/cargo build --release

%install
install -pDm755 target/release/%{appname} %{buildroot}%{_bindir}/%{appname}
install -pDm644 target/release/build/hyperfine-*/out/hyperfine.bash %{buildroot}/usr/share/bash-completion/completions/hyperfine
install -pDm644 target/release/build/hyperfine-*/out/hyperfine.fish %{buildroot}/usr/share/fish/vendor_completions.d/hyperfine.fish
install -pDm644 target/release/build/hyperfine-*/out/_hyperfine %{buildroot}/usr/share/zsh/site-functions/_hyperfine

install -pDm644 doc/hyperfine.1 %{buildroot}%{_mandir}/man1/hyperfine.1.gz

%check


%files
%{_bindir}/%{appname}
%{_mandir}/man1/hyperfine.1.gz
%{_datadir}/bash-completion/completions/hyperfine
%{_datadir}/fish/vendor_completions.d/hyperfine.fish
%{_datadir}/zsh/site-functions/_hyperfine

%changelog
