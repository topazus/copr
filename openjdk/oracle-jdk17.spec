%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}

Name:           oracle-jdk17
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        OpenJDK Java 17 development kit
License:        custom
URL:            https://www.oracle.com/java/
Source:         https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.tar.gz

BuildRequires:  pkg-config wget

%description
OpenJDK Java 17 development kit

%prep
cd $HOME && wget https://download.oracle.com/java/17/latest/jdk-17_linux-x64_bin.tar.gz
tar xvf jdk-*.tar.gz
mv $HOME/jdk-*/ $HOME/jdk

%build


%install
mkdir -p %{buildroot}%{_prefix}/lib/jvm/oracle-jdk17
cp -a $HOME/jdk/* %{buildroot}%{_prefix}/lib/jvm/oracle-jdk17

%check


%files
%{_prefix}/lib/jvm/oracle-jdk17/*

%changelog
