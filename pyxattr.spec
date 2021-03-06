Name:           pyxattr
Version:        0.4.0
Release:        3
Summary:        Extended attributes library wrapper for Python
License:        LGPLv2+
Group:          Development/Python
URL:            http://pyxattr.sourceforge.net/
Source:         http://downloads.sourceforge.net/pyxattr/pyxattr-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools attr-devel
#### from looking at it, I'm pretty sure we are conflictiong with python-xattr :-(
#### same namespace, differenct functions...
Conflicts:      python-xattr

%description
Python extension module wrapper for libattr. It allows to query, list,
add and remove extended attributes from files and directories.

%prep
%setup -q

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__python} setup.py install --root %{buildroot} --install-purelib=%{python_sitearch}

%files 
%doc COPYING NEWS README PKG-INFO
%{python_sitearch}/*



%changelog
* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 0.4.0-1mdv2011.0
+ Revision: 683280
- import pyxattr


* Wed Jun 8 2011 Antoine Ginies <aginies@mandriva.com> 0.4.0
- first release for Mandriva based on OpenSUSE SRPM
