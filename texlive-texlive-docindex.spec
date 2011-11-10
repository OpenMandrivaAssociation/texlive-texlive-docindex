# revision 24542
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-docindex
Version:	20111110
Release:	1
Summary:	top-level TeX Live doc.html, etc
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-docindex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-docindex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
These files are regenerated as needed, which is often, so we
make them a separate package.  See the tl-update-auto script
for the process.

#-----------------------------------------------------------------------
%files
%doc %{_tlpkgdir}/doc.html
%doc %{_tlpkgdir}/texmf
%doc %{_tlpkgdir}/texmf-dist
%doc %{_texmfdir}/scripts/texlive/var/texcatalogue.keywords
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
cp -fpa doc.html %{buildroot}%{_tlpkgdir}
pushd %{buildroot}%{_tlpkgdir}
    # create symlinks so that links in doc.html (should) work
    ln -sf %{_texmfdir} texmf
    ln -sf %{_texmfdistdir} texmf-dist
popd
