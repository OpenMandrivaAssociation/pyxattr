Name:		pyxattr
Version:	0.8.1
Release:	1
Summary:	Extended attributes library wrapper for Python
License:	LGPLv2+
Group:		Development/Python
URL:		https://pyxattr.k1024.org/
Source:		https://pyxattr.k1024.org/downloads/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(libattr)
#### from looking at it, I'm pretty sure we are conflictiong with python-xattr :-(
#### same namespace, differenct functions...
Conflicts:	python-xattr
Provides:	python-%{name} = %{EVRD}

%description
Python extension module wrapper for libattr. It allows to query, list,
add and remove extended attributes from files and directories.

%prep
%autosetup -p1

sed -i -e "s/-Werror//g" setup.py

%build
%py_build

%install
%py_install

%files
%doc COPYING NEWS.md README.md PKG-INFO
%{python_sitearch}/*
