#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Perl6-Export
Version  : 0.009
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Perl6-Export-0.009.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Perl6-Export-0.009.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libperl6-export-perl/libperl6-export-perl_0.009-1.debian.tar.xz
Summary  : "Implements the Perl 6 'is export(...)' trait"
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Perl6-Export-license = %{version}-%{release}
Requires: perl-Perl6-Export-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Perl6::Export version 0.009
=========================
This module prototypes the Perl 6 'exported' and 'exportable' traits
in Perl 5.

%package dev
Summary: dev components for the perl-Perl6-Export package.
Group: Development
Provides: perl-Perl6-Export-devel = %{version}-%{release}
Requires: perl-Perl6-Export = %{version}-%{release}

%description dev
dev components for the perl-Perl6-Export package.


%package license
Summary: license components for the perl-Perl6-Export package.
Group: Default

%description license
license components for the perl-Perl6-Export package.


%package perl
Summary: perl components for the perl-Perl6-Export package.
Group: Default
Requires: perl-Perl6-Export = %{version}-%{release}

%description perl
perl components for the perl-Perl6-Export package.


%prep
%setup -q -n Perl6-Export-0.009
cd %{_builddir}
tar xf %{_sourcedir}/libperl6-export-perl_0.009-1.debian.tar.xz
cd %{_builddir}/Perl6-Export-0.009
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Perl6-Export-0.009/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Perl6-Export
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Perl6-Export/c5ba815629c7483b6ac2b6c2fa255e33c4ff453e
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Perl6::Export.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Perl6-Export/c5ba815629c7483b6ac2b6c2fa255e33c4ff453e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Perl6/Export.pm
