Name: myrepos
Version: 1.20140831.1
Release: alt1

Summary: A tool to manage all your version control repos
License: GPL-2+
Group: Development/Tools
Url: http://myrepos.branchable.com/
Packager: Pavel Nakonechny <pavel.nakonechny@skitlab.ru>

Provides: mr

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: perl-podlators

%description
The mr(1) command can checkout, update, or perform other actions on
a set of repositories as if they were one combined respository. It
supports any combination of git, svn, mercurial, bzr, darcs, cvs, vcsh,
fossil, and veracity repositories, and support for other version control
systems can easily be added. (There are extensions adding support for unison
and git-svn, among others.)

It is extremely configurable via simple shell scripting. Some examples
of things it can do include:
 * Update a repository no more frequently than once every twelve hours.
 * Run an arbitrary command before committing to a repository.
 * When updating a git repository, pull from two different upstreams
   and merge the two together.
 * Run several repository updates in parallel, greatly speeding up
   the update process.
 * Remember actions that failed due to a laptop being offline, so they
   can be retried when it comes back online.

# webcheckout script needs perl(LWP/Simple.pm),
# there is no such module in Alt Linux currently, so comment out it..
%if 0
%package -n myrepos-webcheckout
Summary: Check out repositories referenced on a web page
Group: Development/Tools
Requires: perl-HTML-Parser

%description -n myrepos-webcheckout
webcheckout downloads an url and parses it, looking for version control
repositories referenced by the page. It checks out each repository into
a subdirectory of the current directory, using whatever VCS program is
appropriate for that repository (git, svn, etc).

The information about the repositories is embedded in the web page using
the rel=vcs-* microformat, which is documented at
<http://kitenet.net/~joey/rfc/rel-vcs/>.

If the optional destdir parameter is specified, VCS programs will be asked
to check out repositories into that directory. If there are multiple
repositories to check out, each will be checked out into a separate
subdirectory of the destdir.
%endif

%prep
%setup -q
%patch -p1

%build
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/mr
%_man1dir/mr*
%_datadir/mr

%if 0
%files -n myrepos-webcheckout
%_bindir/webcheckout
%_man1dir/webcheckout*
%endif

%changelog
* Fri Sep 11 2014 Pavel Nakonechny <pavel.nakonechny@skitlab.ru> 1.20140831.1-alt1
- initial build, based on 1.20140831.1 (2a044e2)
