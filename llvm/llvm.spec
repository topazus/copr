%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname llvm15

Name:           %{appname}
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        a collection of modular and reusable compiler and toolchain technologies.
License:        MIT
URL:            https://github.com/llvm/llvm-project
#Source:

BuildRequires:  gcc gcc-c++ llvm-devel libatomic cmake ninja-build python3
BuildRequires:  git wget libcxx-devel

%description
a collection of modular and reusable compiler and toolchain technologies.

%prep
#git clone --depth=1 https://github.com/llvm/llvm-project.git .
wget https://github.com/llvm/llvm-project/archive/refs/tags/llvmorg-15.0.0-rc2.tar.gz
tar xf llvmorg-*.tar.gz

%build
#export CC=clang
#export CXX=clang++

#export CXXFLAGS="$CXXFLAGS -Wno-address -Wno-nonnull -Wno-maybe-uninitialized"
#export CFLAGS="$CFLAGS -Wno-address -Wno-nonnull -Wno-maybe-uninitialized"
# or
# add `-DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++` to cmake

mkdir -p %{buildroot}/usr/local/opt/llvm-git
cd llvm-project-llvmorg-*/
mkdir build && cd build
#-DLLVM_ENABLE_PROJECTS="clang;clang-tools-extra;libcxx;libcxxabi;polly;lldb;lld;compiler-rt" \
cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr/local/opt/llvm-git \
    -DLLVM_ENABLE_PROJECTS=all \
    ../llvm
ninja

%install
cd llvm-project-llvmorg-*/
ninja install

%check

%files
%dir %{buildroot}/usr/local/opt/%{appname}
%{buildroot}/usr/local/opt/%{appname}/*

%changelog
