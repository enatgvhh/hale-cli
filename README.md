#

INSPIRE Transformation der LoD2-Daten per HALE Studio java command
==================================================================

## Inhalt
* [Einleitung](#einleitung)
* [HALE Studio java command](#hale-studio-java-command)
* [Python subprocess](#python-subprocess)
* [Summary](#summary)


## Einleitung
Bei den LoD2-Daten handelt es sich um **3D-Gebäudedaten** im AdV City-GML-Profil, einer Reduktion des CityGML 1.0 Schemas. Wir haben es also wiederum mit AdV-Daten zu tun, mit denen wir uns schon im Repository [hale-adv](https://github.com/enatgvhh/hale-adv) beschäftigten. Das entsprechende Transformationsmodell ist deshalb auch Bestandteil des dort vorgestellten [gradle Projekts](https://github.com/wetransform/adv-inspire-alignments). Wir werden die INSPIRE Transformation in diesem Fall allerdings nicht über das gradle Projekt ausführen, sondern per HALE Studio java command. Alternativ bietet sich auch das HALE [command line interface](https://builds.wetransform.to/job/hale/job/hale~publish(master)/) an.


## HALE Studio java command
Als Ausgangsbasis stehen uns ca. 900 LoD2-XML-Files mit einer Größe von 8 GB zur Verfügung, die einmal jährlich mit dem tridicon CityModeller erzeugt werden. Diese werden wir nun in  900 INSPIRE bu-core3d-GML-Files transformieren, die dann als Atom Feed (Download-Service) bereitzustellen sind. Möglicherweise könnte dies auch über einen [3DCityDB-WFS](https://www.3dcitydb.org/3dcitydb/documentation/) erfolgen.

Nachfolgend sehen wir uns den [java command](http://help.halestudio.org/latest/index.jsp?topic=%2Feu.esdihumboldt.hale.doc.user%2Fhtml%2Ftasks%2Ftransform_cli.html) für ein einzelnes LoD2-File etwas genauer an.
```
java
	-Xmx16384m 
	-Dcache.level1.enabled=false -Dcache.level1.size=0 -Dcache.level2.enabled=false -Dcache.level2.size=0 
	-Dlog.hale.level=INFO -Dlog.root.level=WARN
	-Dhttp.proxyHost=111.11.111.111 -Dhttp.proxyPort=80                                  
	-jar C:\inspire\hale-studio-4.0.0.SNAPSHOT-win32.win32.x86_64\plugins\org.eclipse.equinox.launcher_1.5.0.v20180512-1130.jar
	-application hale.transform
	-project E:\Program\gradle\adv-inspire-alignments\annex-2-3\mappings\Buildings\3D\3A2INSPIRE_BU3D_v2.halex
	-source E:\Data\LoD2\LoD2-TestFolder\LoD2_548_5937_1_HH.xml
	-providerId eu.esdihumboldt.hale.io.gml.reader -Scharset UTF-8
	-target E:\Program\gradle\adv-inspire-alignments\transformiert\bu-3d\LoD2_548_5937_1_HH.gml
	-providerId eu.esdihumboldt.hale.io.wfs.fc.write-2.0 -Sxml.pretty true
	-validate eu.esdihumboldt.hale.io.xml.validator
	-reportsOut E:\Program\gradle\adv-inspire-alignments\transformiert\bu-3d\reports.log
	-stacktrace
	-trustGroovy
```
Wir verwenden einen HALE Studio [GML WFS 2.0 FeatureCollection Writer](http://help.halestudio.org/latest/index.jsp?topic=%2Feu.esdihumboldt.hale.doc.user.ioproviders%2Foverview%2FInstanceWriter.html&cp%3D0_6_2_1_0) und schreiben das GML-File in einem human-readable Format (*-Sxml.pretty true*). Das vorherige Einlesen erfolgt mit einem [GML Features Reader](http://help.halestudio.org/latest/index.jsp?topic=%2Feu.esdihumboldt.hale.doc.user.ioproviders%2Foverview%2FInstanceReader.html), bei dem wir kein Default SRS angegeben haben. Das führt allerdings dazu, dass im Output GML-File kein *srsName* angegeben wird, da dieser auch in den Input LoD2-Files nicht vorhanden ist. Die richtige Notation wäre hier _srsName="urn:adv:crs:ETRS89_UTM32*DE_DHHN2016_NH"_. Diese kann so aber nicht als Parameter *-SdefaultSrs* übergeben werden. Über diesen Parameter könnten wir nur das Koordinatensystem für die 2D-Geometrie übergeben (z.B. *-SdefaultSrs code:EPSG:25832*).


## Python subprocess
Den java command führen wir letztendlich über einen Python *subprocess* aus. Dazu iterieren wir über die 900 Lod2-Files und rufen jeweils die Funktion *callHaleCliProcess* der Klasse *HaleCliProcess* auf. Das kleine python-package 'lod2' ist zusammen mit einem Client im Ordner [src](src) zu finden.


## Summary
Mit dem hier vorgestellten Ansatz können wir die INSPIRE Anforderungen mit minimallem Aufwand erfüllen. Man kann das natürlich auch etwas professioneller angehen. Es fragt sich nur wie sinnvoll das ist, wenn ich meine originären 3D-Gebäudedaten bereits über einen 3D-View und Download-Service anbiete. Wer zum Himmels Willen braucht dann noch einen zweiten INSPIRE 3D-View und Download-Service.
