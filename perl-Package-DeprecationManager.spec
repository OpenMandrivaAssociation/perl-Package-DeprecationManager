%define upstream_name    Package-DeprecationManager
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Manage deprecation warnings for your distribution
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Package/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Carp)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module allows you to manage a set of deprecations for one or more
modules.

When you import 'Package::DeprecationManager', you must provide a set of
'-deprecations' as a hash ref. The keys are "feature" names, and the values
are the version when that feature was deprecated.

In many cases, you can simply use the fully qualified name of a subroutine
or method as the feature name. This works for cases where the whole
subroutine is deprecated. However, the feature names can be any string.
This is useful if you don't want to deprecate an entire subroutine, just a
certain usage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.110.0-3mdv2012.0
+ Revision: 765549
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.110.0-2
+ Revision: 764066
- rebuilt for perl-5.14.x

* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.110.0-1
+ Revision: 686644
- update to new version 0.11

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2
+ Revision: 657811
- rebuild for updated spec-helper

* Sat Nov 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 594298
- new version

* Tue Oct 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 586816
- new version

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 561573
- import perl-Package-DeprecationManager


* Tue Jul 27 2010 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
