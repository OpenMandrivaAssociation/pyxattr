Name:		pyxattr
Version:	0.8.1
Release:	2
Summary:	Extended attributes library wrapper for Python
License:	LGPLv2+
Group:		Development/Python
URL:		https://pyxattr.k1024.org/
# URL:		https://github.com/iustin/pyxattr
Source:		https://pyxattr.k1024.org/downloads/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libattr)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
#### from looking at it, I'm pretty sure we are conflictiong with python-xattr :-(
#### same namespace, differenct functions...
## confirmed - https://github.com/iustin/pyxattr/issues/49
Conflicts:	python-xattr


%description
Python extension module wrapper for libattr. It allows to query, list,
add and remove extended attributes from files and directories.

%prep
%autosetup -p1
# Remove bundled egg-info
rm -rf %{name}.egg-info
sed -i -e "s/-Werror//g" setup.py

%build
%py_build

%install
%py_install

%files
%doc COPYING NEWS.md README.md PKG-INFO
%{python_sitearch}/*
