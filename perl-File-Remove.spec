%include	/usr/lib/rpm/macros.perl
Summary:	File::Remove perl module
Summary(pl):	Modu³ perla File::Remove
Name:		perl-File-Remove
Version:	0.20
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/File-Remove%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Remove removes files and directories.

%description -l pl
File::Remove usuwa pliki i katalogi.

%prep
%setup -q -n File-Remove%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/File/Remove.pm
%{_mandir}/man3/*
