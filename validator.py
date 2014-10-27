#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import libxml2
import libxslt
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
  res = doc.validateDtd(ctxt, dtd)
  if res == 0:
    print "VALIDATION FAILED"
  else:
    print "VALIDATED"  
  dtd.freeDtd()
  doc.freeDoc()
  return res

def query(xml_file, xpath_query):
  doc = libxml2.parseFile (xml_file)
  ctxt = doc.xpathNewContext()
  results = ctxt.xpathEval(xpath_query)
  for res in results:
    print res.content
  ctxt.xpathFreeContext ()
  doc.freeDoc ()

def transform(xml_file, xsl_file):
  xml_doc = libxml2.parseFile(xml_file)
  xsl_doc = libxml2.parseFile(xsl_file)
  xsl = libxslt.parseStylesheetDoc(xsl_doc)
  out_doc = xsl.applyStylesheet(xml_doc ,None)
  print out_doc
  xsl.freeStylesheet()
  out_doc.freeDoc()
  xml_doc.freeDoc()

def main():
  op = optparse.OptionParser(description = U"Проверка на соответствие DTD",
                             prog="dtd", version="0.1", usage=U"%prog")
  op.add_option("-x", "--xml", dest="xml", help=U"XML-документ", metavar="XML_FILE")
  op.add_option("-d", "--dtd", dest="dtd", help=U"DTD-документ", metavar="DTD_FILE")
  op.add_option("-s", "--xsd", dest="xsd", help=U"XML-схема", metavar="XSD_FILE")
  op.add_option("-q", "--xpath", dest="xpath", help=U"XPath-запрос", metavar="XPATH_QUERY")
  op.add_option("-t", "--xslt", dest="xslt", help=U"XSLT-преобразование", metavar="XSLT_FILE")

  options, arguments = op.parse_args()
  if options.xml and options.dtd:
    dtd_validation(options.xml, options.dtd)
  elif options.xml and options.xsd:
    schema_validation(options.xml, options.xsd)
  elif options.xml and options.xpath:
    query(options.xml, options.xpath)
  elif options.xml and options.xslt:
    transform(options.xml, options.xslt)
  else:
    op.print_help()
if __name__ == '__main__':
  main()
