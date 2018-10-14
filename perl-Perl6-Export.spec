#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Perl6-Export
Version  : 0.009
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Perl6-Export-0.009.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Perl6-Export-0.009.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libperl6-export-perl/libperl6-export-perl_0.009-1.debian.tar.xz
Summary  : "Implements the Perl 6 'is export(...)' trait"
Group    : Development/Tools
License  : Artistic-1.0-Perl
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

%description dev
dev components for the perl-Perl6-Export package.


%prep
%setup -q -n Perl6-Export-0.009
cd ..
%setup -q -T -D -n Perl6-Export-0.009 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Perl6-Export-0.009/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.26.1/Perl6/Export.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Perl6::Export.3
