<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <div class="data">
            <ul>
                <xsl:apply-templates/>
            </ul>
        </div>
    </xsl:template>
    <xsl:template match="phone">
        <li>
            <div class="description">
                <p>Название: <xsl:value-of select="name"/></p>
                <p>Цена: <xsl:value-of select="price"/></p>
                <p>Характеристики:</p>
                <ul>
                  <li><p> <xsl:value-of select="characteristics/characteristics1"/></p></li>
                  <li><p> <xsl:value-of select="characteristics/characteristics2"/></p></li>
                  <li><p> <xsl:value-of select="characteristics/characteristics3"/></p></li>
                  <li><p> <xsl:value-of select="characteristics/characteristics4"/></p></li>
                  <li><p> <xsl:value-of select="characteristics/characteristics5"/></p></li>
                  <li><p> <xsl:value-of select="characteristics/characteristics6"/></p></li>
                </ul>
                <p>Страна производителя:</p>
                <ul>
                  <li><p> <xsl:value-of select="country/country1"/></p></li>
                  <li><p> <xsl:value-of select="country/country2"/></p></li>
                  <li><p> <xsl:value-of select="country/country3"/></p></li>
                </ul>
            </div>
        </li>
    </xsl:template>
</xsl:stylesheet>
