%include	/usr/lib/rpm/macros.perl
Summary:	File::Remove - remove files and directories
Summary(pl):	File::Remove - usuwanie plików i katalogów
Name:		perl-File-Remove
Version:	0.20
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/File-Remove%{version}.tar.gz
# Source0-md5:	11514a468dbdde199c611389ec13f269
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Remove removes files and directories. It acts like rm for the
most part.  Although unlink can be given a list of files it will not
remove directories.  This module remedies that.  It also accepts
wildcards, * and ?, as arguments for filenames.

%description -l pl
File::Remove usuwa pliki i katalogi. Dzia³a w zasadzie jak rm.
Jednak¿e, funkcji unlink mo¿na przekazaæ tylko listê plików, nie usuwa
ona katalogów. Ten modu³ ma na to lekarstwo. Akceptuje równie¿
metaznaki: * i ? jako argumenty dla nazw plików.

%prep
%setup -q -n File-Remove%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/File/Remove.pm
%{_mandir}/man3/*
