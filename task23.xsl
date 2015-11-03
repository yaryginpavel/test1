<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="text"/>


<xsl:template match="/">
	  <html>
	  <body>
	    <xsl:for-each select="//book"> 
	      <xsl:value-of select="title"/> 
	      <xsl:choose>
	        <xsl:when test="price &gt; 30">
	          <xsl:text>&gt;30</xsl:text>
	        </xsl:when>
        	<xsl:otherwise>
	          <xsl:choose>
	            <xsl:when test="price &lt; 30">
	              <xsl:text>&lt;30</xsl:text>
	            </xsl:when>
	            <xsl:otherwise>
	              <xsl:text>=30</xsl:text>
	            </xsl:otherwise>
	          </xsl:choose>
	        </xsl:otherwise>
	      </xsl:choose>
	      <xsl:text>&#xa;</xsl:text>
	    </xsl:for-each>
	  </body>
	</html>
</xsl:template>
</xsl:stylesheet>
