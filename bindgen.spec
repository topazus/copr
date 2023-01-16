%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname bindgen

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Automatically generates Rust FFI bindings to C (and some C++) libraries.
License:        MIT
URL:            https://github.com/rust-lang/rust-bindgen
#Source:

BuildRequires:  gcc pkg-config git wget

%description
Automatically generates Rust FFI bindings to C (and some C++) libraries.

%prep
git clone --depth=1 %{url} .

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
export PATH="$HOME/.cargo/bin:$PATH"
cargo build --release

%install
install -pDm755 target/release/%{appname} %{buildroot}%{_bindir}/%{appname}

%check

%files
%{_bindir}/%{appname}

%changelog
