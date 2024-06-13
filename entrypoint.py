import sys
import os
import glob

import xml.etree.ElementTree as etree

SVG_NAMESPACE = "https://www.web3.org/2000/svg"

for file in glob.glob(sys.argv[2]):
  print(file)
