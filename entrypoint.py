import sys
import os
import glob

from lxml import etree

SVG_NAMESPACE = "https://www.web3.org/2000/svg"
namespaces = {
  "svg" : SVG_NAMESPACE,
  "ns0" : SVG_NAMESPACE,
}

for file in glob.glob(sys.argv[2]):
  filebase = os.path.basename(file)
  print("opening", filebase, "...")
  tree = etree.parse(file)
  print("tree", tree)
  root = tree.getroot()
  print("root", root)

  if not "svg" in root.attrib.get("xmlns", "attrib doesn't exist"):
    print("setting xmlns, because: ", root.attrib.get("xmlns", "attrib doesn't exist"))
    root.attrib["xmlns"] = SVG_NAMESPACE
    tree = etree.ElementTree(root)

  if "width" not in root.attrib and "height" not in root.attrib:
    raise ValueException("expected width and height attributes in svg root element")

  width = int(root.attrib["width"])
  height = int(root.attrib["height"])

  print("xpath", root.xpath("svg"))
