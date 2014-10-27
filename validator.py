#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import libxml2
import optparse

def schema_validation(xml_file, xsd_file):
  ctxt = libxml2.schemaNewParserCtxt(xsd_file)
  schema = ctxt.schemaParse()
  validationCtxt = schema.schemaNewValidCtxt()
  res = validationCtxt.schemaValidateFile(xml_file, 0)
  if res != 0:
    print "VALIDATION FAILED"
  else:
    print "VALIDATED"  
  return res
  
def dtd_validation(xml_file, dtd_file):
  doc = libxml2.parseFile(xml_file)
  dtd = libxml2.parseDTD(None, dtd_file)
  ctxt = libxml2.newValidCtxt()
  ret = doc.validateDtd(ctxt, dtd)
  if res != 0:
    print "VALIDATION FAILED"
  else:
    print "VALIDATED"  
  dtd.freeDtd()
  doc.freeDoc()
  return ret

def main():
  op = optparse.OptionParser(description = U"Проверка на соответствие DTD",
                             prog="dtd", version="0.1", usage=U"%prog")
  op.add_option("-x", "--xml", dest="xml", help=U"XML-документ", metavar="XML_FILE")
  op.add_option("-d", "--dtd", dest="dtd", help=U"DTD-документ", metavar="DTD_FILE")
  op.add_option("-s", "--xsd", dest="xsd", help=U"XML-схема", metavar="XSD_FILE")

  options, arguments = op.parse_args()
  if options.xml and options.dtd:
    dtd_validation(options.xml, options.dtd)
  else:
    if options.xml and options.xsd:
      xsd_validation(options.xml, options.xsd)
    else:
      op.print_help()

if __name__ == '__main__':
  main()
