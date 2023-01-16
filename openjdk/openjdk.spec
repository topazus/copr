%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname openjdk

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        a free and open-source implementation of the Java Platform, Standard Edition
License:        ASL 2.0
URL:            https://openjdk.java.net/
Source:         https://github.com/openjdk/jdk/archive/master/jdk-master.tar.gz

BuildRequires:  gcc gcc-c++ make autoconf pkg-config unzip
BuildRequires:  wget git
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel cups-devel alsa-lib-devel libffi-devel
BuildRequires:  libXtst-devel libXt-devel libXrender-devel libXrandr-devel libXi-devel
#BuildRequires:  java-17-openjdk

%description
OpenJDK is a free and open-source implementation of the Java Platform, Standard Edition.

%prep
git clone https://git.openjdk.java.net/jdk/ .

# set boot JDK
cd $HOME && wget https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.tar.gz
tar xvf jdk-*.tar.gz
mv $HOME/jdk-*/ $HOME/jdk

%build
export JAVA_HOME=$HOME/jdk
bash configure \
    --disable-warnings-as-errors
make images

%install
mkdir -p %{buildroot}/opt/%{name}
cp -r build/linux-x86_64-server-release/images/jdk/* %{buildroot}/opt/%{name}

%check


%files
%license LICENSE*
%doc README*
/opt/%{name}/*

%changelog
