%global debug_package %{nil}

Name:           microsoft-jdk11
Version:        11.0.12
Release:        1%{?dist}
Summary:        OpenJDK Java 11 development kit (Microsoft build)
License:        custom
URL:            https://www.microsoft.com/openjdk
Source:         https://aka.ms/download-jdk/microsoft-jdk-11.0.12.7.1-linux-x64.tar.gz

BuildRequires:  pkg-config

%description
Microsoft Build of OpenJDK™
Free. Open Source. Freshly Brewed!

%prep
%autosetup -n jdk-11.0.12+7 -p1

%build


%install
mkdir -p %{buildroot}%{_prefix}/lib/jvm/microsoft-jdk11
cp -a * %{buildroot}%{_prefix}/lib/jvm/microsoft-jdk11

%check


%files
%dir %{_prefix}/lib/jvm/microsoft-jdk11
%{_prefix}/lib/jvm/microsoft-jdk11/*
