%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}

Name:           joshuto-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        ranger-like terminal file manager written in Rust
License:        MIT
URL:            https://github.com/kamiyaa/joshuto
#Source:

BuildRequires:  gcc-c++ make pkg-config git

%description
ranger-like terminal file manager written in Rust.

%prep
git clone --depth=1 https://github.com/kamiyaa/joshuto .

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
export PATH="$HOME/.cargo/bin:$PATH"
cargo build --release

%install
install -pDm755 target/release/joshuto %{buildroot}%{_bindir}/joshuto

%check

%files
%{_bindir}/joshuto

%changelog
