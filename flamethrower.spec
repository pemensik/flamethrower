# SPEC file overview:
# https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/#con_rpm-spec-file-overview
# Fedora packaging guidelines:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/

%global commit v%{version}

Name:		flamethrower
Version:	0.10
Release:	1%{?dist}
Summary:	A DNS performance and functional testing utility

License:	ASL 2.0
URL:		https://github.com/DNS-OARC/flamethrower
Source0:	https://github.com/DNS-OARC/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

Patch1:		flamethrower-0.10-libuv.patch

BuildRequires:	gcc, make
BuildRequires:	cmake
BuildRequires:	libuv-devel
BuildRequires:	ldns-devel
BuildRequires:	gnutls-devel
BuildRequires:	pandoc
Requires:	ldns%{?_isa}
Requires:	libuv%{?_isa}

%description
Flamethrower is a small, fast, configurable tool for functional testing, benchmarking,
and stress testing DNS servers and networks. It supports IPv4, IPv6, UDP and TCP,
and has a modular system for generating queries used in the tests.

It was built as an alternative to dnsperf, and many of the command line options are compatible.

%prep
%autosetup -n %{name}-%{version} -p1
mkdir build

%build
pushd build
%cmake -DCMAKE_SKIP_BUILD_RPATH=TRUE ..
make %{?_smp_mflags}
popd


%install
pushd build
# does not provide install target
#%%make_install
install -pD flame ${RPM_BUILD_ROOT}%{_sbindir}/flame
install -pD libflamecore.so ${RPM_BUILD_ROOT}%{_libdir}/libflamecore.so
popd
install -pD man/flame.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/flame.1

%check
pushd build
make tests
popd

%files
%doc README.md
%license LICENSE
%{_sbindir}/flame
%{_libdir}/libflamecore.so
%{_mandir}/man1/flame.1*


%changelog
* Tue Sep 10 2019 Petr Menšík <pemensik@redhat.com> - 0.10-1
- Initial release


