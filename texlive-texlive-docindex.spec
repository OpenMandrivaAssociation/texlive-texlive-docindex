# revision 27294
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-docindex
Version:	20120808
Release:	2
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
%{_texmfdir}/scripts/texlive/var/texcatalogue.keywords
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
cp -fpar texmf %{buildroot}%{_datadir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120808-1
+ Revision: 812901
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120611-1
+ Revision: 805106
- Update to latest release.

* Sat Apr 14 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120413-1
+ Revision: 790840
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120327-1
+ Revision: 787795
- Update to latest release.

* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120307-1
+ Revision: 783095
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120224-1
+ Revision: 780603
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120223-1
+ Revision: 779670
- Update to latest release.

* Wed Feb 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120208-1
+ Revision: 772175
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120131-1
+ Revision: 770297
- Update to latest upstream package

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120119-1
+ Revision: 762745
- Update to latest upstream package

* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120109-1
+ Revision: 759068
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111226-2
+ Revision: 756792
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111226-1
+ Revision: 745333
- texlive-texlive-docindex

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111217-1
+ Revision: 743343
- texlive-texlive-docindex

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111209-1
+ Revision: 739934
- texlive-texlive-docindex

* Tue Nov 22 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111122-1
+ Revision: 732612
- texlive-texlive-docindex

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111110-1
+ Revision: 729700
- texlive-texlive-docindex

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719694
- texlive-texlive-docindex
- texlive-texlive-docindex
- texlive-texlive-docindex
- texlive-texlive-docindex

