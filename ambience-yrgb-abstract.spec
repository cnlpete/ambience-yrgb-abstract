Name:          ambience-yrgb-abstract
Version:       0.2.0
Release:       1
Summary:       Four different colored ambiences
Group:         System/Tools
Vendor:        eson
Distribution:  SailfishOS
Packager:      eson
URL:           https://openrepos.net/content/eson/ambience-yrgb-abstract

License:       GPL

%description
Four different colored ambiences based on abstract background images.

%files
%defattr(-,root,root,-)
/usr/share/ambience/*

%post
chmod 755 /usr/share/ambience/{name}
chmod 755 /usr/share/ambience/{name}/images
chmod 755 /usr/share/ambience/{name}/sounds
chmod 644 /usr/share/ambience/{name}/*.*
chmod 644 /usr/share/ambience/{name}/images/*.*
chmod 644 /usr/share/ambience/{name}/sounds/*.*
systemctl-user restart ambienced.service

%postun
if [ $1 = 0 ]; then
rm -rf /usr/share/ambience/{name}
systemctl-user restart ambienced.service
else
if [ $1 = 1 ]; then
echo "Upgrading"
systemctl-user restart ambienced.service
fi
fi

%changelog
* Wed Jun 24 2017 0.2
- Initial release.
