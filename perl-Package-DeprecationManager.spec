%define upstream_name    Package-DeprecationManager
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Manage deprecation warnings for your distribution
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Package/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Sub::Install)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(Test::Requires)
BuildRequires: perl(Test::Fatal)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%perl_vendorlib/*


