#-*- coding: UTF-8 -*-
#File: ClientLod2.py
import os
import sys
import logging
from lod2 import haleCliProcess

def main():
    jarPath = r"C:\inspire\hale-studio-4.0.0.SNAPSHOT-win32.win32.x86_64_org\plugins\org.eclipse.equinox.launcher_1.5.0.v20180512-1130.jar"
    projectPath = r"E:\Program\gradle\adv-inspire-alignments\annex-2-3\mappings\Buildings\3D\3A2INSPIRE_BU3D_v2.halex"
    sourcePath = r"E:\Data\LoD2\LoD2-DE_HH_2020-04-01"
    targetPath = r"E:\Program\gradle\adv-inspire-alignments\transformiert\bu-3d"
    reportsPath = r"E:\Program\gradle\adv-inspire-alignments\transformiert\bu-3d"
    
    logFile = r"E:\logs\loggerLOD2.log"
    logging.basicConfig(filename=logFile, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
    logger = logging.getLogger('loggerLOD2')
    logger.info('Start')
    
    haleCliProc = haleCliProcess.HaleCliProcess(jarPath, projectPath, sourcePath, targetPath, reportsPath, logger)
    
    if os.path.exists(sourcePath) == True:
        if os.path.isdir(sourcePath) == True:
            objects = os.listdir(sourcePath)
            if objects:
                for objectElement in objects:
                    try:
                        haleCliProc.callHaleCliProcess(objectElement)
                    except:
                        message = str(sys.exc_info()[0]) + "; " + str(sys.exc_info()[1])
                        logger.error(message)
    
    logger.info('End')
    
if __name__ == '__main__':
    main()