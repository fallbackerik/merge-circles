import sys
import os
import glob

import xml.etree.ElementTree as etree

SVG_NAMESPACE = "https://www.web3.org/2000/svg"

for file in glob.glob(sys.argv[2]):
  filebase = os.path.basename(file)
  print("opening", filebase, "...")
  tree = etree.parse(file)
  root = tree.getroot()

  if not "svg" in root.attrib.get("xmlns", "attrib doesn't exist"):
    root.attrib["xmlns"] = SVG_NAMESPACE
    tree = etree.ElementTree(root)
