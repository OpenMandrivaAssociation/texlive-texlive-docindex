# revision 34308
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-docindex
Version:	20140621
Release:	3
Summary:	top-level TeX Live doc.html, etc
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-docindex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-docindex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These files are regenerated as needed, which is often, so we
make them a separate package.  See the tl-update-auto script
for the process.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%doc %{_tlpkgdir}/texmf
%doc %{_tlpkgdir}/texmf-dist
%{_texmfdistdir}/scripts/texlive/var/texcatalogue.keywords
%doc %{_tlpkgdir}/doc.html

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_tlpkgdir}
cp -fpa doc.html %{buildroot}%{_tlpkgdir}
pushd %{buildroot}%{_tlpkgdir}
    # create symlinks so that links in doc.html (should) work
    ln -sf %{_texmfdir} texmf
    ln -sf %{_texmfdistdir} texmf-dist
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
