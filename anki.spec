Summary:	SuperMemo(tm)-like program
Summary(pl.UTF-8):	Program podobny do SuperMemo
Name:		anki
Version:	1.2.8
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	http://anki.googlecode.com/files/%{name}-%{version}.tgz
# Source0-md5:	0dc5f5bad979f57cab82e3757665f6c0
URL:		http://ichi2.net/anki/
BuildRequires:	python-PyQt4
BuildRequires:	python-SQLAlchemy
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	python-simplejson
BuildRequires:	python-sqlite
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	python-BeautifulSoup
Requires:	python-PyQt4
Requires:	python-SQLAlchemy
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
cd libanki
%{__python} setup.py build
cd ..
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
cd libanki
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
cd ..
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
install anki.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README*
%attr(755,root,root) %{_bindir}/%{name}
%{py_sitescriptdir}/anki
%{py_sitescriptdir}/ankiqt
%{py_sitescriptdir}/*.egg-info
%{_desktopdir}/*.desktop
