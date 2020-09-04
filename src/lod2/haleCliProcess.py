# -*- coding: UTF-8 -*-
#File: haleCliProcess.py
import subprocess

class HaleCliProcess(object):
    '''Klasse HaleCliProcess laesst selbiegen ueber einen Subprocess laufen'''

    def __init__(self, jarPath, projectPath, sourcePath, targetPath, reportsPath, logger):
        '''Konstruktor der Klasse HaleCliProcess.
        
        Args:
            jarPath: String mit Path zum launcher JAR file
            projectPath: String mit Path zum halex bzw. haelz file
            sourcePath: String mit Path zum Source Folder
            targetPath: String mit Path zum Target Folder
            reportsPath: String zum Path zum HALE Reports Folder
            logger: Object logging.Logger
        '''
        
        self.__jarPath = jarPath
        self.__projectPath = projectPath
        self.__sourcePath = sourcePath
        self.__targetPath = targetPath
        self.__reportsPath = reportsPath
        self.__logger = logger
        
    def callHaleCliProcess(self, nameSourceFile):
        '''Methode startet den HALE Cli Subprocess.
        
        Args:
            nameSourceFile: String mit Namen des Source XML-Files
        '''
        
        nameTargetFile = nameSourceFile.replace(".xml", ".gml")
        writerFile = self.__reportsPath + "/out.log"
        writer = open(writerFile, "a")
        
        completed = subprocess.run("java -Xmx16384m -Dcache.level1.enabled=false -Dcache.level1.size=0 -Dcache.level2.enabled=false -Dcache.level2.size=0 -Dlog.hale.level=INFO -Dlog.root.level=WARN" +
                                   " -Dhttp.proxyHost=111.11.111.111 -Dhttp.proxyPort=80" +
                                   " -jar " + self.__jarPath +
                                   " -application hale.transform" +
                                   " -project " + self.__projectPath +
                                   " -source " + self.__sourcePath + "/" + nameSourceFile +
                                   " -providerId eu.esdihumboldt.hale.io.gml.reader -Scharset UTF-8" +
                                   " -target " + self.__targetPath + "/" + nameTargetFile +
                                   " -providerId eu.esdihumboldt.hale.io.wfs.fc.write-2.0 -Sxml.pretty true" +
                                   " -validate eu.esdihumboldt.hale.io.xml.validator" +
                                   " -reportsOut " + self.__reportsPath + "/" + "reports.log" +
                                   " -stacktrace -trustGroovy", stdout=writer, stderr=subprocess.PIPE)
        
        writer.close()
        
        if completed.returncode != 0:
            message = "transform " + nameSourceFile + " failed: <"+ str(completed.stderr) + ">"
            raise Exception(message)
        else:
            message = "transform " + nameSourceFile + " successfully"
            self.__logger.info(message)
            
    def callHaleCliProcess2(self, nameSourceFile):
        '''Methode startet den HALE Cli Subprocess.
        
        Args:
            nameSourceFile: String mit Namen des Source XML-Files
        '''
        
        nameTargetFile = nameSourceFile.replace(".xml", ".gml")
        writerFile = self.__reportsPath + "/out.log"
        writer = open(writerFile, "a")
        
        completed = subprocess.run("java -Xmx16384m -Dcache.level1.enabled=false -Dcache.level1.size=0 -Dcache.level2.enabled=false -Dcache.level2.size=0 -Dlog.hale.level=INFO -Dlog.root.level=WARN" +
                                   " -Dhttp.proxyHost=111.11.111.111 -Dhttp.proxyPort=80" +
                                   " -jar " + self.__jarPath +
                                   " -application hale.transform" +
                                   " -project " + self.__projectPath +
                                   " -source " + self.__sourcePath + "/" + nameSourceFile +
                                   " -providerId eu.esdihumboldt.hale.io.gml.reader -Scharset UTF-8 -SdefaultSrs code:EPSG:25832" +
                                   " -target " + self.__targetPath + "/" + nameTargetFile +
                                   " -providerId eu.esdihumboldt.hale.io.wfs.fc.write-2.0 -Sxml.pretty true -Scrs.epsg.prefix http://www.opengis.net/def/crs/EPSG/0/" +
                                   " -validate eu.esdihumboldt.hale.io.xml.validator" +
                                   " -reportsOut " + self.__reportsPath + "/" + "reports.log" +
                                   " -stacktrace -trustGroovy", stdout=writer, stderr=subprocess.PIPE)
        
        writer.close()
        
        if completed.returncode != 0:
            message = "transform " + nameSourceFile + " failed: <"+ str(completed.stderr) + ">"
            raise Exception(message)
        else:
            message = "transform " + nameSourceFile + " successfully"
            self.__logger.info(message)
            