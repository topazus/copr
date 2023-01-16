%global debug_package %{nil}
%global appname powershell
%bcond_without check

Name:           %{appname}-git
Version:        7.3.0
Release:        1%{?dist}
Summary:        cross-platform (Windows, Linux, and macOS) automation and configuration tool/framework
License:        MIT
URL:            https://github.com/PowerShell/PowerShell
#Source:

BuildRequires:  pkg-config

%description
PowerShell is a cross-platform (Windows, Linux, and macOS) automation and configuration tool/framework
that works well with your existing tools and is optimized for dealing with structured data
(e.g. JSON, CSV, XML, etc.), REST APIs, and object models. It includes a command-line shell,
an associated scripting language and a framework for processing cmdlets.

%prep
rm -rf powershell && mkdir powershell && cd powershell
git clone --branch=master https://github.com/PowerShell/PowerShell.git .



%build
cd powershell

echo 'Import-Module ./build.psm1
Start-PSBuild' > build-src.ps
pwsh build-src.ps

%install
cd powershell
export QA_RPATHS=$[ 0x0001|0x0002 ]
mkdir -p %{buildroot}/opt/%{appname}
# output dir:
# /home/ruby/build-ps/PowerShell/src/powershell-unix/bin/Debug/net7.0/linux-x64/publish/pwsh
# src/powershell-unix/bin/Debug/net7.0/linux-x64/publish/
cp -r src/powershell-unix/bin/Debug/net7.0/linux-x64/publish/* %{buildroot}/opt/%{appname}

%if %{with check}
%check

%endif

%files
%dir /opt/%{appname}
/opt/%{appname}/*

%ghost /usr/bin/%{appname}

%post
ln -s /opt/%{appname}/pwsh /usr/bin/%{appname}

%changelog
