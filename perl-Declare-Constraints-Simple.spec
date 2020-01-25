#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Declare
%define	pnam	Constraints-Simple
Summary:	Declare::Constraints::Simple - Declarative Validation of Data Structures
Summary(pl.UTF-8):	Declare::Constraints::Simple - deklaratywne sprawdzanie poprawności struktur danych
Name:		perl-Declare-Constraints-Simple
Version:	0.03
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/P/PH/PHAYLON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	abcd5e9f2dd034deed975601b38d684e
URL:		http://search.cpan.org/dist/Declare-Constraints-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Carp-Clan
BuildRequires:	perl-Class-Inspector
BuildRequires:	perl-aliased
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl(Declare::Constraints::Simple-Library)

%description
The main purpose of this module is to provide an easy way to build a
profile to validate a data structure. It does this by giving you a set
of declarative keywords in the importing namespace.

%description -l pl.UTF-8
Głównym celem tego modułu jest dostarczenie prostego sposobu budowania
profili służących do sprawdzania poprawności sktruktur danych.
Zapewnia to udostępniając zbiór deklaratywnych słów kluczowych w
importowanej przestrzeni nazw.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Declare
%dir %{perl_vendorlib}/Declare/Constraints
%{perl_vendorlib}/Declare/Constraints/Simple.pm
%{perl_vendorlib}/Declare/Constraints/Simple
%{_mandir}/man3/Declare::Constraints::Simple*.3pm*
