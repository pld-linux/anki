# TODO - post?
%define		pre	rc6
Summary:	SuperMemo(tm)-like program
Summary(pl.UTF-8):	Program podobny do SuperMemo
Name:		anki
Version:	2.0
Release:	0.%{pre}.0.2
License:	GPL v3+
Group:		Applications
Source0:	http://ankisrs.net/download/mirror/%{name}-%{version}-%{pre}.tgz
# Source0-md5:	ab77dc8fb1a2435771677743282bc4ab
URL:		http://ankisrs.net/
BuildRequires:	python-PyQt4
BuildRequires:	python-SQLAlchemy
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	python-simplejson
BuildRequires:	python-sqlite
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	python-BeautifulSoup >= 3.2.1
Requires:	python-PyQt4
Requires:	python-SQLAlchemy
Requires:	python-httplib2 >= 0.7.4
Requires:	python-pyaudio >= 0.2.4
Requires:	python-simplejson
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A flash card program to make your review process more efficient.

%description -l pl.UTF-8
Program podobny w działaniu do SuperMemo(tm).

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_mandir}/man1,%{_bindir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/libanki

cp -a aqt $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a libanki/anki $RPM_BUILD_ROOT%{_datadir}/%{name}/libanki
cp -p anki $RPM_BUILD_ROOT%{_bindir}
cp -p anki.xpm anki.png $RPM_BUILD_ROOT%{_pixmapsdir}
cp -p anki.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -p anki.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%if 0
%post
xdg-mime install anki.xml
xdg-mime default anki.desktop application/x-anki
xdg-mime default anki.desktop application/x-apkg
%endif

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/anki
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/anki.1*
