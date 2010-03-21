Summary:	SuperMemo(tm)-like program 
Summary(pl.UTF-8):	Program podobny do SuperMemo
Name:		anki
Version:	0.9.9.8.6
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	http://anki.googlecode.com/files/%{name}-%{version}.tgz
# Source0-md5:	744f7057cc43be7cc076e1fcb2719e4c
URL:		http://ichi2.net/anki/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	python-BeautifulSoup
Requires:	python-SQLAlchemy
Requires:	python-simplejson
Requires:	python-PyQt4
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
