
Name:		flamethrower
Version:	0.10
Release:	3%{?dist}
Summary:	A DNS performance and functional testing utility

License:	ASL 2.0
URL:		https://github.com/DNS-OARC/flamethrower
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/DNS-OARC/flamethrower/pull/19
Patch1:		flamethrower-0.10-libuv.patch
# https://github.com/DNS-OARC/flamethrower/pull/20
Patch2:		flamethrower-0.10-install.patch

BuildRequires:	gcc-c++, make
BuildRequires:	cmake
BuildRequires:	libuv-devel
BuildRequires:	ldns-devel
BuildRequires:	gnutls-devel
BuildRequires:	pandoc

%description
Flamethrower is a small, fast, configurable tool for
functional testing, benchmarking, and stress testing
DNS servers and networks. It supports IPv4, IPv6, UDP and TCP,
and has a modular system for generating queries used in the tests.

It was built as an alternative to dnsperf, and many
of the command line options are compatible.

%prep
%autosetup -n %{name}-%{version} -p1
mkdir build

%build
pushd build
%cmake -DCMAKE_SKIP_BUILD_RPATH=TRUE ..
%make_build
popd


%install
pushd build
%make_install
popd
install -m 0644 -pD man/flame.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/flame.1

%check
pushd build
make tests
popd

%files
%doc README.md
%license LICENSE
%{_bindir}/flame
%{_libdir}/libflamecore.so
%{_mandir}/man1/flame.1*


%changelog
* Mon Oct 07 2019 Petr Menšík <pemensik@redhat.com> - 0.10-3
- Remove explicit library requires

* Wed Oct 02 2019 Petr Menšík <pemensik@redhat.com> - 0.10-2
- Use make install, improve descriptions
- Correct permissions of manual
- Use bindir

* Tue Sep 10 2019 Petr Menšík <pemensik@redhat.com> - 0.10-1
- Initial release


