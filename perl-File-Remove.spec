Summary:	File::Remove - remove files and directories
Summary(pl.UTF-8):	File::Remove - usuwanie plików i katalogów
Name:		perl-File-Remove
Version:	1.58
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/File-Remove-%{version}.tar.gz
# Source0-md5:	f2d3959c7a8982bbdd03bb27f8b76891
URL:		http://search.cpan.org/dist/File-Remove/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.36
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Cwd) >= 3.29
BuildRequires:	perl(File::Spec) >= 3.29
BuildRequires:	perl-Test-Simple >= 0.42
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Remove removes files and directories. It acts like rm for the
most part. Although unlink can be given a list of files it will not
remove directories. This module remedies that. It also accepts
wildcards, * and ?, as arguments for filenames.

%description -l pl.UTF-8
File::Remove usuwa pliki i katalogi. Działa w zasadzie jak rm.
Jednakże, funkcji unlink można przekazać tylko listę plików, nie usuwa
ona katalogów. Ten moduł ma na to lekarstwo. Akceptuje również
metaznaki: * i ? jako argumenty dla nazw plików.

%prep
%setup -q -n File-Remove-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/File/Remove.pm
%{_mandir}/man3/File::Remove.3pm*
