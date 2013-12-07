%define modname	Package-DeprecationManager
%define modver	0.13

Summary:	Manage deprecation warnings for your distribution
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Package/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Carp)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::Output)
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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{perl_vendorlib}/*
%{_mandir}/man3/*

