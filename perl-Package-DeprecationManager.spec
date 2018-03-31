# Tests may fail because of circular dependencies while
# bootstrapping
%bcond_with check

%define modname	Package-DeprecationManager

Summary:	Manage deprecation warnings for your distribution
Name:		perl-%{modname}
Version:	0.17
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Package/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Carp)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Sub::Install)
%if %{with check}
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::Output)
BuildRequires:	perl(Package::Stash)
%endif
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%if %{with check}
%check
%make test
%endif

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE META.json
%{perl_vendorlib}/*
%{_mandir}/man3/*
