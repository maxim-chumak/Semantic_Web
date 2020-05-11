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
                  <li><p> <xsl:value-of select="characteristics/char[1]"/></p></li>
                  <li><p> <xsl:value-of select="characteristics/char[2]"/></p></li>
                  <li><p> <xsl:value-of select="characteristics/char[3]"/></p></li>
                  <li><p> <xsl:value-of select="characteristics/char[4]"/></p></li>
                  <li><p> <xsl:value-of select="characteristics/char[5]"/></p></li>
                  <li><p> <xsl:value-of select="characteristics/char[6]"/></p></li>
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