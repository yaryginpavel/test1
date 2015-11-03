<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output method="text"/>

<xsl:template match="/">
  <html>
  <body>
    <xsl:for-each select="//book"> 
      <xsl:value-of select="title"/> <xsl:text>&#xa;</xsl:text>
    </xsl:for-each>
  </body>
</html>
</xsl:template>
</xsl:stylesheet>
