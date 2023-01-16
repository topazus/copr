# We are not using this as the system libc,
# so this remains disabled by default.
%bcond_with system_libc

# Fedora uses multilib with /usr/lib64
# This switch changes it to multiarch, with /usr/lib/[arch]-linux-musl
# This switch only has effect if system_libc is disabled.
# This switch is disabled by default.
%bcond_with multiarch

# Fedora uses glibc as the standard libc.
# This means any packages that would use musl would be treated
# as a cross-compilation target. Cross-mode sets it up for this application.
# In cross-mode, a prefix root is created with a new child FHS area.
# This switch only has effect if system_libc is disabled.
# This switch is enabled by default.
%bcond_without crossmode


# Ensure the value is set correctly
%ifarch %{ix86}
%global _musl_target_cpu i386
%endif

%ifarch %{arm}
# ARM is... complicated...
%ifarch armv3l armv4b armv4l armv4tl armv5tl armv5tel armv5tejl armv6l armv7l
%global _musl_target_cpu arm
%else
%global _musl_target_cpu armhf
%endif
%global _musl_platform_suffix eabi
%endif

%ifarch %{mips64}
%global _musl_target_cpu mips64
%endif

%ifarch %{mips32}
%global _musl_target_cpu mips
%endif

%ifarch ppc
%global _musl_target_cpu powerpc
%endif

%ifarch %{power64}
# POWER architectures have a different name if little-endian
%ifarch ppc64le
%global _musl_target_cpu powerpc64le
%else
%global _musl_target_cpu powerpc64
%endif
%endif

%ifnarch %{ix86} %{arm} %{mips} %{power64} ppc
%global _musl_target_cpu %{_target_cpu}
%endif

# Define the platform name
%global _musl_platform %{_musl_target_cpu}-linux-musl%{?_musl_platform_suffix}

# Paths to use when not set up in cross-mode
%if %{without crossmode}
# Set up alternate paths when not using as system libc
%if %{without system_libc}
# Set up libdir path for when using multilib
%if %{without multiarch}
%global _libdir %{_prefix}/%{_lib}/%{_musl_platform}
%else
# Set up libdir path for when using multiarch
%global _libdir %{_prefix}/lib/%{_musl_platform}
%endif
%global _includedir %{_prefix}/include/%{_musl_platform}
%endif
%else
# Cross-mode paths
%global _libdir %{_prefix}/%{_musl_platform}/%{_lib}
%global _includedir %{_prefix}/%{_musl_platform}/include
%endif

%if %{without multiarch}
# We need to be multilib aware
%global _syslibdir /%{_lib}
%else
%global _syslibdir /lib
%endif


Name:           musl
Version:        1.2.3
Release:        2%{?dist}
Summary:        Fully featured lightweight standard C library for Linux
License:        MIT
URL:            https://musl.libc.org
Source0:        https://musl.libc.org/releases/%{name}-%{version}.tar.gz

BuildRequires:  gcc make

%description
musl is a C standard library to power a new generation
of Linux-based devices. It is lightweight, fast, simple,
free, and strives to be correct in the sense of standards
conformance and safety.


%prep
%autosetup -p1


%build
# musl is known not to work with LTO
# Disable LTO
%define _lto_cflags %{nil}

%ifarch %{power64}
# Deal with ABI mismatch on long double between glibc and musl
export CC="gcc -mlong-double-64"
%endif

# Set linker flags to get correct soname...
export LDFLAGS="%{?build_ldflags} -Wl,-soname,ld-musl-%{_musl_target_cpu}.so.1"
%configure --enable-debug --enable-wrapper=all
%make_build


%install
%make_install

# Swap the files around for libc.so, making libc.so a symlink to the real file
rm %{buildroot}/lib/ld-musl-%{_musl_target_cpu}.so.1
mv %{buildroot}%{_libdir}/libc.so %{buildroot}/lib/ld-musl-%{_musl_target_cpu}.so.1
ln -sr %{buildroot}/lib/ld-musl-%{_musl_target_cpu}.so.1 %{buildroot}%{_libdir}/ld-musl-%{_musl_target_cpu}.so.1
ln -sr %{buildroot}%{_libdir}/ld-musl-%{_musl_target_cpu}.so.1 %{buildroot}%{_libdir}/libc.so

# Write search path for dynamic linker
mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/ld-musl-%{_musl_target_cpu}.path
cat > %{buildroot}%{_sysconfdir}/ld-musl-%{_musl_target_cpu}.path <<EOF
%{_libdir}
EOF

%if %{without multiarch}
# Write symlink for syslib to /lib64 for compatibility with Fedora standards, where applicable
mkdir -p %{buildroot}%{_syslibdir}
%if "%{_lib}" == "lib64"
ln -sr %{buildroot}/lib/ld-musl-%{_musl_target_cpu}.so.1 %{buildroot}%{_syslibdir}/ld-musl-%{_musl_target_cpu}.so.1
%endif
%endif

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
touch %{buildroot}%{_rpmconfigdir}/macros.d/macros.musl
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.musl <<EOF
%%_musl_libdir %{_libdir}
%%_musl_includedir %{_includedir}
EOF

%files
/etc/ld-musl-x86_64.path
/lib/ld-musl-x86_64.so.1
/lib64/ld-musl-x86_64.so.1

/usr/bin/ld.musl-clang
/usr/bin/musl-clang
/usr/bin/musl-gcc

/usr/lib/rpm/macros.d/macros.musl

/usr/x86_64-linux-musl/include/
/usr/x86_64-linux-musl/lib64/


%changelog
