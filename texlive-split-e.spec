%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-e
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1213:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cinzel.tar.xz
Source1214:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cinzel.doc.tar.xz
Source1215:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/circ.tar.xz
Source1216:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/circ.doc.tar.xz
Source1218:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/circuitikz.tar.xz
Source1219:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/circuitikz.doc.tar.xz
Source1220:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/citeall.tar.xz
Source1221:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/citeall.doc.tar.xz
Source1222:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cite.tar.xz
Source1223:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cite.doc.tar.xz
Source1224:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cjhebrew.tar.xz
Source1225:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cjhebrew.doc.tar.xz
Source1228:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cjk-ko.tar.xz
Source1229:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cjk-ko.doc.tar.xz
Source1230:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cjkpunct.tar.xz
Source1231:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cjkpunct.doc.tar.xz
Source1233:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cjk.tar.xz
Source1234:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cjk.doc.tar.xz
Source1236:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cns.tar.xz
Source1237:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cns.doc.tar.xz
Source1251:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/classics.tar.xz
Source1252:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/classics.doc.tar.xz
Source1253:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/classicthesis.tar.xz
Source1254:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/classicthesis.doc.tar.xz
Source1255:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/classpack.tar.xz
Source1256:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/classpack.doc.tar.xz
Source1258:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cleanthesis.tar.xz
Source1259:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cleanthesis.doc.tar.xz
Source1260:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clearsans.tar.xz
Source1261:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clearsans.doc.tar.xz
Source1262:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clefval.tar.xz
Source1263:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clefval.doc.tar.xz
Source1265:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cleveref.tar.xz
Source1266:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cleveref.doc.tar.xz
Source1268:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clipboard.tar.xz
Source1269:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clipboard.doc.tar.xz
Source1270:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clock.tar.xz
Source1271:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clock.doc.tar.xz
Source1272:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cloze.tar.xz
Source1273:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cloze.doc.tar.xz
Source1275:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clrscode3e.tar.xz
Source1276:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clrscode3e.doc.tar.xz
Source1277:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clrscode.tar.xz
Source1278:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clrscode.doc.tar.xz
Source1279:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmap.tar.xz
Source1280:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmap.doc.tar.xz
Source1281:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmarrows.tar.xz
Source1282:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmarrows.doc.tar.xz
Source1283:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmbright.tar.xz
Source1284:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmbright.doc.tar.xz
Source1286:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmcyr.tar.xz
Source1287:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmcyr.doc.tar.xz
Source1288:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmdstring.tar.xz
Source1289:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmdstring.doc.tar.xz
Source1290:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmextra.tar.xz
Source1291:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cm-lgc.tar.xz
Source1292:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cm-lgc.doc.tar.xz
Source1293:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmll.tar.xz
Source1294:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmll.doc.tar.xz
Source1296:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmpica.tar.xz
Source1297:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmpica.doc.tar.xz
Source1298:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmpj.tar.xz
Source1299:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmpj.doc.tar.xz
Source1300:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmsd.tar.xz
Source1301:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmsd.doc.tar.xz
Source1302:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cm-super.tar.xz
Source1303:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cm-super.doc.tar.xz
Source1304:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmtiup.tar.xz
Source1305:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmtiup.doc.tar.xz
Source1306:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cm.tar.xz
Source1307:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cm.doc.tar.xz
Source1308:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cm-unicode.tar.xz
Source1309:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cm-unicode.doc.tar.xz
Source1310:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cnbwp.tar.xz
Source1311:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cnbwp.doc.tar.xz
Source1312:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cnltx.tar.xz
Source1313:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cnltx.doc.tar.xz
Source1314:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cntformats.tar.xz
Source1315:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cntformats.doc.tar.xz
Source1316:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cntperchap.tar.xz
Source1317:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cntperchap.doc.tar.xz
Source1318:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/codedoc.tar.xz
Source1319:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/codedoc.doc.tar.xz
Source1320:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/codepage.tar.xz
Source1321:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/codepage.doc.tar.xz
Source1323:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/codesection.tar.xz
Source1324:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/codesection.doc.tar.xz
Source1326:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/codicefiscaleitaliano.tar.xz
Source1327:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/codicefiscaleitaliano.doc.tar.xz
Source1329:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collcell.tar.xz
Source1330:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collcell.doc.tar.xz
Source1332:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collectbox.tar.xz
Source1333:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collectbox.doc.tar.xz
Source1386:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colortbl.tar.xz
Source1387:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colortbl.doc.tar.xz
Source1430:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collref.tar.xz
Source1431:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collref.doc.tar.xz
Source1433:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/compactbib.tar.xz
Source1677:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-account.tar.xz
Source1678:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-account.doc.tar.xz
Source1679:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-algorithmic.tar.xz
Source1680:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-animation.tar.xz
Source1681:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-animation.doc.tar.xz
Source1682:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-annotation.tar.xz
Source1683:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-annotation.doc.tar.xz
Source1684:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-bnf.tar.xz
Source1685:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-bnf.doc.tar.xz
Source1686:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-chromato.tar.xz
Source1687:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-chromato.doc.tar.xz
Source1688:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-construction-plan.tar.xz
Source1689:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-construction-plan.doc.tar.xz
Source1690:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-cyrillicnumbers.tar.xz
Source1691:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-cyrillicnumbers.doc.tar.xz
Source1692:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-degrade.tar.xz
Source1693:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-degrade.doc.tar.xz
Source1694:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-fancybreak.tar.xz
Source1695:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-fancybreak.doc.tar.xz
Source1696:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-filter.tar.xz
Source1697:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-filter.doc.tar.xz
Source1699:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-french.tar.xz
Source1700:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-french.doc.tar.xz
Source1701:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-fullpage.tar.xz
Source1702:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-fullpage.doc.tar.xz
Source1707:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-gantt.tar.xz
Source1708:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-gantt.doc.tar.xz
Source1711:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-gnuplot.tar.xz
Source1712:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-gnuplot.doc.tar.xz
Source1713:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-letter.tar.xz
Source1714:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-letter.doc.tar.xz
Source1715:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-lettrine.tar.xz
Source1716:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-lettrine.doc.tar.xz
Source1719:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-mathsets.tar.xz
Source1720:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-mathsets.doc.tar.xz
Source1721:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-notes-zh-cn.tar.xz
Source1722:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-notes-zh-cn.doc.tar.xz
Source1723:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-rst.tar.xz
Source1724:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-rst.doc.tar.xz
Source1725:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-ruby.tar.xz
Source1726:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-ruby.doc.tar.xz
Source1727:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-simplefonts.tar.xz
Source1728:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-simplefonts.doc.tar.xz
Source1729:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-simpleslides.tar.xz
Source1730:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-simpleslides.doc.tar.xz
Source1731:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-title.tar.xz
Source1732:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-title.doc.tar.xz
Source1733:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-transliterator.tar.xz
Source1734:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-transliterator.doc.tar.xz
Source1735:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-typearea.tar.xz
Source1736:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-typearea.doc.tar.xz
Source1737:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-typescripts.tar.xz
Source1738:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-typescripts.doc.tar.xz
Source1739:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-vim.tar.xz
Source1740:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-vim.doc.tar.xz
Source1741:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-visualcounter.tar.xz
Source1742:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-visualcounter.doc.tar.xz
Source1744:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/comfortaa.tar.xz
Source1745:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/comfortaa.doc.tar.xz
Source1747:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/comicneue.tar.xz
Source1748:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/comicneue.doc.tar.xz
Source1749:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/concmath-fonts.tar.xz
Source1750:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/concmath-fonts.doc.tar.xz
Source1751:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cookingsymbols.tar.xz
Source1752:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cookingsymbols.doc.tar.xz
Source1754:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/countriesofeurope.tar.xz
Source1755:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/countriesofeurope.doc.tar.xz
Source1756:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/courier-scaled.tar.xz
Source1757:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/courier-scaled.doc.tar.xz
Source2120:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/courier.tar.xz
Source2265:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colorsep.tar.xz
Source2370:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/covington.tar.xz
Source2371:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/covington.doc.tar.xz
Source2611:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/components-of-TeX.doc.tar.xz
Source2612:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/comprehensive.doc.tar.xz
Source3108:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/combinedgraphics.tar.xz
Source3109:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/combinedgraphics.doc.tar.xz
Source3403:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colordoc.tar.xz
Source3404:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colordoc.doc.tar.xz
Source3406:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colorinfo.tar.xz
Source3407:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colorinfo.doc.tar.xz
Source3408:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colorspace.tar.xz
Source3409:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colorspace.doc.tar.xz
Source3410:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colortab.tar.xz
Source3411:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colortab.doc.tar.xz
Source3412:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colorwav.tar.xz
Source3413:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colorwav.doc.tar.xz
Source3415:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colorweb.tar.xz
Source3416:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colorweb.doc.tar.xz
Source3418:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colourchange.tar.xz
Source3419:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/colourchange.doc.tar.xz
Source3420:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/combelow.tar.xz
Source3421:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/combelow.doc.tar.xz
Source3422:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/combine.tar.xz
Source3423:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/combine.doc.tar.xz
Source3425:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/comma.tar.xz
Source3426:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/comma.doc.tar.xz
Source3427:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/commado.tar.xz
Source3428:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/commado.doc.tar.xz
Source3430:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/comment.tar.xz
Source3431:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/comment.doc.tar.xz
Source3432:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/concepts.tar.xz
Source3433:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/concepts.doc.tar.xz
Source3434:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/concprog.tar.xz
Source3435:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/concprog.doc.tar.xz
Source3436:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/constants.tar.xz
Source3437:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/constants.doc.tar.xz
Source3439:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/contour.tar.xz
Source3440:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/contour.doc.tar.xz
Source3442:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/contracard.tar.xz
Source3443:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/contracard.doc.tar.xz
Source3445:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cooking.tar.xz
Source3446:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cooking.doc.tar.xz
Source3448:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cool.tar.xz
Source3449:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cool.doc.tar.xz
Source3451:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coollist.tar.xz
Source3452:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coollist.doc.tar.xz
Source3454:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coolstr.tar.xz
Source3455:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coolstr.doc.tar.xz
Source3457:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coolthms.tar.xz
Source3458:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coolthms.doc.tar.xz
Source3460:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cooltooltips.tar.xz
Source3461:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cooltooltips.doc.tar.xz
Source3463:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coordsys.tar.xz
Source3464:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coordsys.doc.tar.xz
Source3466:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/copyedit.tar.xz
Source3467:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/copyedit.doc.tar.xz
Source3469:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/copyrightbox.tar.xz
Source3470:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/copyrightbox.doc.tar.xz
Source3471:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coseoul.tar.xz
Source3472:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coseoul.doc.tar.xz
Source3473:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/counttexruns.tar.xz
Source3474:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/counttexruns.doc.tar.xz
Source3476:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/courseoutline.tar.xz
Source3477:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/courseoutline.doc.tar.xz
Source3478:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coursepaper.tar.xz
Source3479:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coursepaper.doc.tar.xz
Source3480:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coverpage.tar.xz
Source3481:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coverpage.doc.tar.xz
Source5824:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/commath.tar.xz
Source5825:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/commath.doc.tar.xz
Source5826:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/concmath.tar.xz
Source5827:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/concmath.doc.tar.xz
Source5829:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/concrete.tar.xz
Source5830:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/concrete.doc.tar.xz
Source5831:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/conteq.tar.xz
Source5832:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/conteq.doc.tar.xz
Source6342:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/confproc.tar.xz
Source6343:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/confproc.doc.tar.xz
Source6640:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/complexity.tar.xz
Source6641:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/complexity.doc.tar.xz
Source6642:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/computational-complexity.tar.xz
Source6643:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/computational-complexity.doc.tar.xz
Source7023:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-basic.tar.xz
Source7035:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-bibtexextra.tar.xz
Source7036:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-latex.tar.xz
Source7043:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-binextra.tar.xz
Source7101:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-context.tar.xz
Source7105:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-fontsextra.tar.xz
Source7106:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-fontsrecommended.tar.xz
Source7107:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-fontutils.tar.xz
Source7118:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-formatsextra.tar.xz
Source7123:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-games.tar.xz
Source7131:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-humanities.tar.xz
Source7134:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langarabic.tar.xz
Source7135:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langchinese.tar.xz
Source7136:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langcjk.tar.xz
Source7137:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langcyrillic.tar.xz
Source7139:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langczechslovak.tar.xz
Source7143:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langenglish.tar.xz
Source7144:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langeuropean.tar.xz
Source7145:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langfrench.tar.xz
Source7146:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langgerman.tar.xz
Source7147:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langgreek.tar.xz
Source7152:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langitalian.tar.xz
Source7153:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langjapanese.tar.xz
Source7159:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langkorean.tar.xz
Source7161:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langother.tar.xz
Source7162:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langpolish.tar.xz
Source7164:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langportuguese.tar.xz
Source7165:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-langspanish.tar.xz
Source7166:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-latexextra.tar.xz
Source7167:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-latexrecommended.tar.xz
Source7169:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-pictures.tar.xz
Source7184:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-luatex.tar.xz
Source7188:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-metapost.tar.xz
Source7189:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-music.tar.xz
Source7199:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-pstricks.tar.xz
Source7202:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-publishers.tar.xz
Source7206:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-xetex.tar.xz
Source7287:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmdtrack.tar.xz
Source7288:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmdtrack.doc.tar.xz
Source7290:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmexb.tar.xz
Source7291:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmexb.doc.tar.xz
Source7292:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cochineal.tar.xz
Source7293:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cochineal.doc.tar.xz
Source7294:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coloring.tar.xz
Source7295:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/coloring.doc.tar.xz
Source7296:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/continue.tar.xz
Source7297:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/continue.doc.tar.xz
Source7613:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-plaingeneric.tar.xz
Source7614:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-mathscience.tar.xz
Source7693:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cje.tar.xz
Source7694:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cje.doc.tar.xz
Source7695:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/collection-texworks.tar.xz
Source7696:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/combofont.tar.xz
Source7697:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/combofont.doc.tar.xz
Source7698:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-cmscbf.tar.xz
Source7699:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-cmscbf.doc.tar.xz
Source7700:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-cmttbf.tar.xz
Source7701:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-cmttbf.doc.tar.xz
Source7702:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-inifile.tar.xz
Source7703:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-inifile.doc.tar.xz
Source7704:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-layout.tar.xz
Source7705:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-layout.doc.tar.xz
Source7706:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/conv-xkv.tar.xz
Source7707:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/conv-xkv.doc.tar.xz
Source7708:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cooking-units.tar.xz
Source7709:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cooking-units.doc.tar.xz
Source7710:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cormorantgaramond.tar.xz
Source7711:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cormorantgaramond.doc.tar.xz
Source8098:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/citeref.tar.xz
Source8099:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/citeref.doc.tar.xz
Source8100:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clrdblpg.tar.xz
Source8101:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clrdblpg.doc.tar.xz
Source8102:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clrstrip.tar.xz
Source8103:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/clrstrip.doc.tar.xz
Source8104:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cm-mf-extra-bold.tar.xz
Source8106:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmsrb.tar.xz
Source8107:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cmsrb.doc.tar.xz
Source8108:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/competences.tar.xz
Source8109:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/competences.doc.tar.xz
Source8110:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-handlecsv.tar.xz
Source8111:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context-handlecsv.doc.tar.xz
Source8112:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/correctmathalign.tar.xz
Source8113:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/correctmathalign.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-cinzel
Provides:       tex-cinzel = %{tl_version}
License:        OFL
Summary:        LaTeX support for Cinzel and Cinzel Decorative fonts
Version:        svn34408.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(xkeyval.sty), tex(textcomp.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty), tex(mweights.sty)
Provides:       tex(cnzl_7luz43.enc) = %{tl_version}, tex(cnzl_7t2zcj.enc) = %{tl_version}
Provides:       tex(cnzl_aakhvz.enc) = %{tl_version}, tex(cnzl_k6z3ge.enc) = %{tl_version}
Provides:       tex(cinzel.map) = %{tl_version}, tex(Cinzel-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black.ttf) = %{tl_version}, tex(Cinzel-Bold.ttf) = %{tl_version}
Provides:       tex(Cinzel-Regular.ttf) = %{tl_version}, tex(CinzelDecorative-Black.ttf) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold.ttf) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular.ttf) = %{tl_version}
Provides:       tex(Cinzel-Black.pfb) = %{tl_version}, tex(Cinzel-Bold.pfb) = %{tl_version}
Provides:       tex(Cinzel-Regular.pfb) = %{tl_version}, tex(CinzelDecorative-Black.pfb) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold.pfb) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular.pfb) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Cinzel-LF.fd) = %{tl_version}, tex(LY1CinzelDecorative-LF.fd) = %{tl_version}
Provides:       tex(OT1Cinzel-LF.fd) = %{tl_version}, tex(OT1CinzelDecorative-LF.fd) = %{tl_version}
Provides:       tex(T1Cinzel-LF.fd) = %{tl_version}, tex(T1CinzelDecorative-LF.fd) = %{tl_version}
Provides:       tex(TS1Cinzel-LF.fd) = %{tl_version}, tex(TS1CinzelDecorative-LF.fd) = %{tl_version}
Provides:       tex(cinzel.sty) = %{tl_version}

%description -n texlive-cinzel
Cinzel and Cinzel Decorative fonts, designed by Natanael Gama
Natanael Gama), find their inspiration in first century roman
inscriptions, and are based on classical proportions. Cinzel is
all-caps (similar to Trajan and Michelangelo), but is available
in three weights (Regular, Bold, Black). There are no italic
fonts, but there are Decorative variants, which can be selected
by the usual italic-selection commands in the package's LaTeX
support.

%package -n texlive-cinzel-doc
Summary:        Documentation for cinzel
Version:        svn34408.0

Provides:       tex-cinzel-doc
AutoReqProv:    No

%description -n texlive-cinzel-doc
Documentation for cinzel

%package -n texlive-circ
Provides:       tex-circ = %{tl_version}
License:        GPL+
Summary:        Macros for typesetting circuit diagrams
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cioptic.tfm) = %{tl_version}, tex(basic.def) = %{tl_version}
Provides:       tex(box.def) = %{tl_version}, tex(circ.sty) = %{tl_version}
Provides:       tex(gate.def) = %{tl_version}, tex(ic.def) = %{tl_version}
Provides:       tex(oldgate.def) = %{tl_version}, tex(optics.def) = %{tl_version}
Provides:       tex(physics.def) = %{tl_version}

%description -n texlive-circ
Several electrical symbols like resistor, capacitor,
transistors etc., are defined. The symbols can be connected
with wires. The package also contains an American resistor
symbol for those of us on that side of the Atlantic. The
package also has simple facilities for producing optics
diagrams; however, no-one would deny that the PSTricks pst-
optic package, or the MetaPost makecirc package does the job
better.

%package -n texlive-circ-doc
Summary:        Documentation for circ
Version:        svn15878.1.1

Provides:       tex-circ-doc
AutoReqProv:    No

%description -n texlive-circ-doc
Documentation for circ

%package -n texlive-circuitikz
Provides:       tex-circuitikz = %{tl_version}
License:        LPPL
Summary:        Draw electrical networks with TikZ
Version:        svn44488
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(tikz.sty), tex(xstring.sty), tex(siunitx.sty)
Provides:       tex(t-circuitikz.tex) = %{tl_version}, tex(circuitikz.code.tex) = %{tl_version}
Provides:       tex(circuitikz1.code.tex) = %{tl_version}
Provides:       tex(pgfcircbipoles.tex) = %{tl_version}, tex(pgfcirccurrent.tex) = %{tl_version}
Provides:       tex(pgfcircinputarrows.tex) = %{tl_version}
Provides:       tex(pgfcirclabel.tex) = %{tl_version}, tex(pgfcircmath.tex) = %{tl_version}
Provides:       tex(pgfcircmonopoles.tex) = %{tl_version}
Provides:       tex(pgfcircnpoles.tex) = %{tl_version}, tex(pgfcircquadpoles.tex) = %{tl_version}
Provides:       tex(pgfcircshapes.tex) = %{tl_version}, tex(pgfcirctripoles.tex) = %{tl_version}
Provides:       tex(pgfcircutils.tex) = %{tl_version}, tex(pgfcircvoltage.tex) = %{tl_version}
Provides:       tex(circuitikz.sty) = %{tl_version}

%description -n texlive-circuitikz
The package provides a set of macros for naturally typesetting
electrical and (somewhat less naturally, perhaps) electronic
networks. It is designed as a tool that is easy to use, with a
lean syntax, native to LaTeX, and directly supporting PDF
output format. So is based on the very impressive pgf/TikZ
package.

%package -n texlive-circuitikz-doc
Summary:        Documentation for circuitikz
Version:        svn44488
Provides:       tex-circuitikz-doc
AutoReqProv:    No

%description -n texlive-circuitikz-doc
Documentation for circuitikz

%package -n texlive-citeall
Provides:       tex-citeall = %{tl_version}
License:        LPPL 1.3
Summary:        Cite all entries of a bbl created with biblatex
Version:        svn45975
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty)
Provides:       tex(citeall.sty) = %{tl_version}

%description -n texlive-citeall
This small package allows to cite all entries of a bbl-file
created with biblatex (v1.9).

%package -n texlive-citeall-doc
Summary:        Documentation for citeall
Version:        svn45975
Provides:       tex-citeall-doc
AutoReqProv:    No

%description -n texlive-citeall-doc
Documentation for citeall

%package -n texlive-cite
Provides:       tex-cite = %{tl_version}
License:        Copyright only
Summary:        Improved citation handling in LaTeX
Version:        svn36428.5.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(chapterbib.sty) = %{tl_version}, tex(cite.sty) = %{tl_version}
Provides:       tex(drftcite.sty) = %{tl_version}, tex(overcite.sty) = %{tl_version}

%description -n texlive-cite
The package supports compressed, sorted lists of numerical
citations, and also deals with various punctuation and other
issues of representation, including comprehensive management of
break points. The package is compatible with both hyperref and
backref. The package is (unsurprisingly) part of the cite
bundle of the author's citation-related packages.

%package -n texlive-cite-doc
Summary:        Documentation for cite
Version:        svn36428.5.5

Provides:       tex-cite-doc
AutoReqProv:    No

%description -n texlive-cite-doc
Documentation for cite

%package -n texlive-cjhebrew
Provides:       tex-cjhebrew = %{tl_version}
License:        LPPL
Summary:        Typeset Hebrew with LaTeX
Version:        svn43444
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Provides:       tex(cjhebltx.enc) = %{tl_version}, tex(cjhebrew.map) = %{tl_version}
Provides:       tex(cjhblsm.tfm) = %{tl_version}, tex(cjhbltx.tfm) = %{tl_version}
Provides:       tex(cjheblsm.tfm) = %{tl_version}, tex(cjhebltx.tfm) = %{tl_version}
Provides:       tex(rcjhblsm.tfm) = %{tl_version}, tex(rcjhbltx.tfm) = %{tl_version}
Provides:       tex(cjheblsm.pfb) = %{tl_version}, tex(cjhebltx.pfb) = %{tl_version}
Provides:       tex(cjhblsm.vf) = %{tl_version}, tex(cjhbltx.vf) = %{tl_version}
Provides:       tex(cjhebrew.sty) = %{tl_version}

%description -n texlive-cjhebrew
The cjhebrew package provides Adobe Type 1 fonts for Hebrew,
and LaTeX macros to support their use. Hebrew text can be
vocalised, and a few accents are also available. The package
makes it easy to include Hebrew text in other-language
documents. The package makes use of the e-TeX extensions to
TeX, so should be run using an "e-LaTeX".

%package -n texlive-cjhebrew-doc
Summary:        Documentation for cjhebrew
Version:        svn43444
Provides:       tex-cjhebrew-doc
AutoReqProv:    No

%description -n texlive-cjhebrew-doc
Documentation for cjhebrew

%package -n texlive-cjk-ko
Provides:       tex-cjk-ko = %{tl_version}
License:        GPL+ and LPPL and Public Domain
Summary:        Extension of the CJK package for Korean typesetting
Version:        svn40373

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontenc.sty), tex(textcomp.sty), tex(CJKutf8.sty), tex(ulem.sty)
Requires:       tex(CJKfntef.sty), tex(kolabels-utf.sty)
Requires:       tex(kotexutf.sty), tex(xetexko.sty), tex(luatexko.sty)
Provides:       tex(cjkutf8-josa.sty) = %{tl_version}, tex(cjkutf8-ko.sty) = %{tl_version}
Provides:       tex(cjkutf8-nanummjhanja.sty) = %{tl_version}
Provides:       tex(kolabels-utf.sty) = %{tl_version}, tex(konames-utf.sty) = %{tl_version}
Provides:       tex(kotex.sty) = %{tl_version}

%description -n texlive-cjk-ko
The package supports typesetting UTF-8-encoded modern Korean
documents with the help of the LaTeX2e CJK package. The package
requires nanumtype1 fonts.

%package -n texlive-cjk-ko-doc
Summary:        Documentation for cjk-ko
Version:        svn40373

Provides:       tex-cjk-ko-doc
AutoReqProv:    No

%description -n texlive-cjk-ko-doc
Documentation for cjk-ko

%package -n texlive-cjkpunct
Provides:       tex-cjkpunct = %{tl_version}
License:        LPPL
Summary:        Adjust locations and kerning of CJK punctuation marks
Version:        svn41119

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(CJKpunct.sty) = %{tl_version}

%description -n texlive-cjkpunct
The package serves as a companion package for CJK.

%package -n texlive-cjkpunct-doc
Summary:        Documentation for cjkpunct
Version:        svn41119

Provides:       tex-cjkpunct-doc
AutoReqProv:    No

%description -n texlive-cjkpunct-doc
Documentation for cjkpunct

%package -n texlive-cjk
Provides:       tex-cjk = %{tl_version}
License:        GPL+
Summary:        CJK language support
Version:        svn36951.4.8.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex-arphic, tex-cns, tex-garuda-c90, tex-norasi-c90
Requires:       tex-uhc, tex-wadalab, tex(CJKulem.sty), tex(ulem.sty)
Requires:       tex(ifpdf.sty), tex(inputenc.sty), tex(fontenc.sty), tex(graphicx.sty)
Provides:       tex(c42goth.fd) = %{tl_version}, tex(c42maru.fd) = %{tl_version}
Provides:       tex(c42min.fd) = %{tl_version}, tex(c52maru.fd) = %{tl_version}
Provides:       tex(c52min.fd) = %{tl_version}, tex(c70goth.fd) = %{tl_version}
Provides:       tex(c70maru.fd) = %{tl_version}, tex(c70min.fd) = %{tl_version}
Provides:       tex(Bg5.enc) = %{tl_version}, tex(HK.enc) = %{tl_version}
Provides:       tex(c00bkai.fd) = %{tl_version}, tex(c00bsmi.fd) = %{tl_version}
Provides:       tex(c00bsmir.fd) = %{tl_version}, tex(c00cns.fd) = %{tl_version}
Provides:       tex(c00fs.fd) = %{tl_version}, tex(c00kai.fd) = %{tl_version}
Provides:       tex(c00kair.fd) = %{tl_version}, tex(c00song.fd) = %{tl_version}
Provides:       tex(c01song.fd) = %{tl_version}, tex(c05song.fd) = %{tl_version}
Provides:       tex(c09song.fd) = %{tl_version}, tex(c80song.fd) = %{tl_version}
Provides:       tex(c81song.fd) = %{tl_version}, tex(CJK.enc) = %{tl_version}
Provides:       tex(CJK.sty) = %{tl_version}, tex(CJKfntef.sty) = %{tl_version}
Provides:       tex(CJKnumb.sty) = %{tl_version}, tex(CJKspace.sty) = %{tl_version}
Provides:       tex(CJKulem.sty) = %{tl_version}, tex(CJKutf8.sty) = %{tl_version}
Provides:       tex(CJKvert.sty) = %{tl_version}, tex(EUC-TW.enc) = %{tl_version}
Provides:       tex(c31song.fd) = %{tl_version}, tex(c32song.fd) = %{tl_version}
Provides:       tex(c33song.fd) = %{tl_version}, tex(c34song.fd) = %{tl_version}
Provides:       tex(c35song.fd) = %{tl_version}, tex(c36song.fd) = %{tl_version}
Provides:       tex(c37song.fd) = %{tl_version}, tex(c10fs.fd) = %{tl_version}
Provides:       tex(c10gbsn.fd) = %{tl_version}, tex(c10gkai.fd) = %{tl_version}
Provides:       tex(c10song.fd) = %{tl_version}, tex(c11song.fd) = %{tl_version}
Provides:       tex(c19song.fd) = %{tl_version}, tex(c20song.fd) = %{tl_version}
Provides:       tex(c21song.fd) = %{tl_version}, tex(EUC-JP.enc) = %{tl_version}
Provides:       tex(EUC-JPdnp.enc) = %{tl_version}, tex(JISdnp.enc) = %{tl_version}
Provides:       tex(c40song.fd) = %{tl_version}, tex(c41song.fd) = %{tl_version}
Provides:       tex(c42song.fd) = %{tl_version}, tex(c43song.fd) = %{tl_version}
Provides:       tex(c50song.fd) = %{tl_version}, tex(KSHL.enc) = %{tl_version}
Provides:       tex(c63bm.fd) = %{tl_version}, tex(c63dn.fd) = %{tl_version}
Provides:       tex(c63gr.fd) = %{tl_version}, tex(c63gs.fd) = %{tl_version}
Provides:       tex(c63gt.fd) = %{tl_version}, tex(c63jgt.fd) = %{tl_version}
Provides:       tex(c63jmj.fd) = %{tl_version}, tex(c63jnv.fd) = %{tl_version}
Provides:       tex(c63jsr.fd) = %{tl_version}, tex(c63mj.fd) = %{tl_version}
Provides:       tex(c63pg.fd) = %{tl_version}, tex(c63pga.fd) = %{tl_version}
Provides:       tex(c63ph.fd) = %{tl_version}, tex(c63pn.fd) = %{tl_version}
Provides:       tex(c63sh.fd) = %{tl_version}, tex(c63tz.fd) = %{tl_version}
Provides:       tex(c63vd.fd) = %{tl_version}, tex(c63yt.fd) = %{tl_version}
Provides:       tex(c64bm.fd) = %{tl_version}, tex(c64dn.fd) = %{tl_version}
Provides:       tex(c64gr.fd) = %{tl_version}, tex(c64gs.fd) = %{tl_version}
Provides:       tex(c64gt.fd) = %{tl_version}, tex(c64jgt.fd) = %{tl_version}
Provides:       tex(c64jmj.fd) = %{tl_version}, tex(c64jnv.fd) = %{tl_version}
Provides:       tex(c64jsr.fd) = %{tl_version}, tex(c64mj.fd) = %{tl_version}
Provides:       tex(c64pg.fd) = %{tl_version}, tex(c64pga.fd) = %{tl_version}
Provides:       tex(c64ph.fd) = %{tl_version}, tex(c64pn.fd) = %{tl_version}
Provides:       tex(c64sh.fd) = %{tl_version}, tex(c64tz.fd) = %{tl_version}
Provides:       tex(c64vd.fd) = %{tl_version}, tex(c64yt.fd) = %{tl_version}
Provides:       tex(c65bm.fd) = %{tl_version}, tex(c65dn.fd) = %{tl_version}
Provides:       tex(c65gr.fd) = %{tl_version}, tex(c65gs.fd) = %{tl_version}
Provides:       tex(c65gt.fd) = %{tl_version}, tex(c65jgt.fd) = %{tl_version}
Provides:       tex(c65jmj.fd) = %{tl_version}, tex(c65jnv.fd) = %{tl_version}
Provides:       tex(c65jsr.fd) = %{tl_version}, tex(c65mj.fd) = %{tl_version}
Provides:       tex(c65pg.fd) = %{tl_version}, tex(c65pga.fd) = %{tl_version}
Provides:       tex(c65ph.fd) = %{tl_version}, tex(c65pn.fd) = %{tl_version}
Provides:       tex(c65sh.fd) = %{tl_version}, tex(c65tz.fd) = %{tl_version}
Provides:       tex(c65vd.fd) = %{tl_version}, tex(c65yt.fd) = %{tl_version}
Provides:       tex(pshan.sty) = %{tl_version}, tex(KS.enc) = %{tl_version}
Provides:       tex(c60dr.fd) = %{tl_version}, tex(c60gr.fd) = %{tl_version}
Provides:       tex(c60gs.fd) = %{tl_version}, tex(c60gt.fd) = %{tl_version}
Provides:       tex(c60hgt.fd) = %{tl_version}, tex(c60hmj.fd) = %{tl_version}
Provides:       tex(c60hol.fd) = %{tl_version}, tex(c60hpg.fd) = %{tl_version}
Provides:       tex(c60mj.fd) = %{tl_version}, tex(c61dr.fd) = %{tl_version}
Provides:       tex(c61gr.fd) = %{tl_version}, tex(c61gs.fd) = %{tl_version}
Provides:       tex(c61gt.fd) = %{tl_version}, tex(c61hgt.fd) = %{tl_version}
Provides:       tex(c61hmj.fd) = %{tl_version}, tex(c61hol.fd) = %{tl_version}
Provides:       tex(c61hpg.fd) = %{tl_version}, tex(c61mj.fd) = %{tl_version}
Provides:       tex(c62song.fd) = %{tl_version}, tex(SJIS.enc) = %{tl_version}
Provides:       tex(SJISdnp.enc) = %{tl_version}, tex(c49song.fd) = %{tl_version}
Provides:       tex(UTF8.enc) = %{tl_version}, tex(c70bkai.fd) = %{tl_version}
Provides:       tex(c70bsmi.fd) = %{tl_version}, tex(c70gbsn.fd) = %{tl_version}
Provides:       tex(c70gkai.fd) = %{tl_version}, tex(c70mj.fd) = %{tl_version}
Provides:       tex(c70song.fd) = %{tl_version}, tex(extended.enc) = %{tl_version}
Provides:       tex(MULEenc.sty) = %{tl_version}, tex(pinyin.sty) = %{tl_version}
Provides:       tex(pmCbig.enc) = %{tl_version}, tex(pmCsmall.enc) = %{tl_version}
Provides:       tex(ruby.sty) = %{tl_version}, tex(standard.enc) = %{tl_version}
Provides:       tex(c90cmr.fd) = %{tl_version}, tex(c90cmss.fd) = %{tl_version}
Provides:       tex(c90cmtt.fd) = %{tl_version}, tex(c90enc.def) = %{tl_version}
Provides:       tex(c90gar.fd) = %{tl_version}, tex(c90nrsr.fd) = %{tl_version}
Provides:       tex(thaicjk.ldf) = %{tl_version}, tex(pinyin.ldf) = %{tl_version}

%description -n texlive-cjk
CJK is a macro package for LaTeX, providing simultaneous
support for various Asian scripts in many encodings (including
Unicode): Chinese (both traditional and simplified), Japanese,
Korean and Thai. A special add-on feature is an interface to
the Emacs editor (cjk-enc.el) which gives simultaneous, easy-to-
use support to a bunch of other scripts in addition to the
above -- Cyrillic, Greek, Latin-based scripts, Russian and
Vietnamese are supported.

%package -n texlive-cjk-doc
Summary:        Documentation for cjk
Version:        svn36951.4.8.4

Provides:       tex-cjk-doc
AutoReqProv:    No
Requires:       tex-arphic-doc, tex-cns-doc, tex-uhc-doc, tex-wadalab-doc

%description -n texlive-cjk-doc
Documentation for cjk

%package -n texlive-cns
Provides:       tex-cns = %{tl_version}
License:        LPPL
Summary:        cns package
Version:        svn45677
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(c0so1201.tfm) = %{tl_version}, tex(c0so1202.tfm) = %{tl_version}
Provides:       tex(c0so1203.tfm) = %{tl_version}, tex(c0so1204.tfm) = %{tl_version}
Provides:       tex(c0so1205.tfm) = %{tl_version}, tex(c0so1206.tfm) = %{tl_version}
Provides:       tex(c0so1207.tfm) = %{tl_version}, tex(c0so1208.tfm) = %{tl_version}
Provides:       tex(c0so1209.tfm) = %{tl_version}, tex(c0so1210.tfm) = %{tl_version}
Provides:       tex(c0so1211.tfm) = %{tl_version}, tex(c0so1212.tfm) = %{tl_version}
Provides:       tex(c0so1213.tfm) = %{tl_version}, tex(c0so1214.tfm) = %{tl_version}
Provides:       tex(c0so1215.tfm) = %{tl_version}, tex(c0so1216.tfm) = %{tl_version}
Provides:       tex(c0so1217.tfm) = %{tl_version}, tex(c0so1218.tfm) = %{tl_version}
Provides:       tex(c0so1219.tfm) = %{tl_version}, tex(c0so1220.tfm) = %{tl_version}
Provides:       tex(c0so1221.tfm) = %{tl_version}, tex(c0so1222.tfm) = %{tl_version}
Provides:       tex(c0so1223.tfm) = %{tl_version}, tex(c0so1224.tfm) = %{tl_version}
Provides:       tex(c0so1225.tfm) = %{tl_version}, tex(c0so1226.tfm) = %{tl_version}
Provides:       tex(c0so1227.tfm) = %{tl_version}, tex(c0so1228.tfm) = %{tl_version}
Provides:       tex(c0so1229.tfm) = %{tl_version}, tex(c0so1230.tfm) = %{tl_version}
Provides:       tex(c0so1231.tfm) = %{tl_version}, tex(c0so1232.tfm) = %{tl_version}
Provides:       tex(c0so1233.tfm) = %{tl_version}, tex(c0so1234.tfm) = %{tl_version}
Provides:       tex(c0so1235.tfm) = %{tl_version}, tex(c0so1236.tfm) = %{tl_version}
Provides:       tex(c0so1237.tfm) = %{tl_version}, tex(c0so1238.tfm) = %{tl_version}
Provides:       tex(c0so1239.tfm) = %{tl_version}, tex(c0so1240.tfm) = %{tl_version}
Provides:       tex(c0so1241.tfm) = %{tl_version}, tex(c0so1242.tfm) = %{tl_version}
Provides:       tex(c0so1243.tfm) = %{tl_version}, tex(c0so1244.tfm) = %{tl_version}
Provides:       tex(c0so1245.tfm) = %{tl_version}, tex(c0so1246.tfm) = %{tl_version}
Provides:       tex(c0so1247.tfm) = %{tl_version}, tex(c0so1248.tfm) = %{tl_version}
Provides:       tex(c0so1249.tfm) = %{tl_version}, tex(c0so1250.tfm) = %{tl_version}
Provides:       tex(c0so1251.tfm) = %{tl_version}, tex(c0so1252.tfm) = %{tl_version}
Provides:       tex(c0so1253.tfm) = %{tl_version}, tex(c0so1254.tfm) = %{tl_version}
Provides:       tex(c0so1255.tfm) = %{tl_version}, tex(c1so1201.tfm) = %{tl_version}
Provides:       tex(c1so1202.tfm) = %{tl_version}, tex(c1so1203.tfm) = %{tl_version}
Provides:       tex(c1so1204.tfm) = %{tl_version}, tex(c1so1205.tfm) = %{tl_version}
Provides:       tex(c1so1206.tfm) = %{tl_version}, tex(c1so1207.tfm) = %{tl_version}
Provides:       tex(c1so1208.tfm) = %{tl_version}, tex(c1so1209.tfm) = %{tl_version}
Provides:       tex(c1so1210.tfm) = %{tl_version}, tex(c1so1211.tfm) = %{tl_version}
Provides:       tex(c1so1212.tfm) = %{tl_version}, tex(c1so1213.tfm) = %{tl_version}
Provides:       tex(c1so1214.tfm) = %{tl_version}, tex(c1so1215.tfm) = %{tl_version}
Provides:       tex(c1so1216.tfm) = %{tl_version}, tex(c1so1217.tfm) = %{tl_version}
Provides:       tex(c1so1218.tfm) = %{tl_version}, tex(c1so1219.tfm) = %{tl_version}
Provides:       tex(c1so1220.tfm) = %{tl_version}, tex(c1so1221.tfm) = %{tl_version}
Provides:       tex(c1so1222.tfm) = %{tl_version}, tex(c1so1223.tfm) = %{tl_version}
Provides:       tex(c1so1224.tfm) = %{tl_version}, tex(c1so1225.tfm) = %{tl_version}
Provides:       tex(c1so1226.tfm) = %{tl_version}, tex(c1so1227.tfm) = %{tl_version}
Provides:       tex(c1so1228.tfm) = %{tl_version}, tex(c1so1229.tfm) = %{tl_version}
Provides:       tex(c1so1230.tfm) = %{tl_version}, tex(c1so1231.tfm) = %{tl_version}
Provides:       tex(c1so1232.tfm) = %{tl_version}, tex(c1so1233.tfm) = %{tl_version}
Provides:       tex(c1so1234.tfm) = %{tl_version}, tex(c2so1201.tfm) = %{tl_version}
Provides:       tex(c2so1202.tfm) = %{tl_version}, tex(c2so1203.tfm) = %{tl_version}
Provides:       tex(c2so1204.tfm) = %{tl_version}, tex(c2so1205.tfm) = %{tl_version}
Provides:       tex(c2so1206.tfm) = %{tl_version}, tex(c2so1207.tfm) = %{tl_version}
Provides:       tex(c2so1208.tfm) = %{tl_version}, tex(c2so1209.tfm) = %{tl_version}
Provides:       tex(c2so1210.tfm) = %{tl_version}, tex(c2so1211.tfm) = %{tl_version}
Provides:       tex(c2so1212.tfm) = %{tl_version}, tex(c2so1213.tfm) = %{tl_version}
Provides:       tex(c2so1214.tfm) = %{tl_version}, tex(c2so1215.tfm) = %{tl_version}
Provides:       tex(c2so1216.tfm) = %{tl_version}, tex(c2so1217.tfm) = %{tl_version}
Provides:       tex(c2so1218.tfm) = %{tl_version}, tex(c2so1219.tfm) = %{tl_version}
Provides:       tex(c2so1220.tfm) = %{tl_version}, tex(c2so1221.tfm) = %{tl_version}
Provides:       tex(c2so1222.tfm) = %{tl_version}, tex(c2so1223.tfm) = %{tl_version}
Provides:       tex(c2so1224.tfm) = %{tl_version}, tex(c2so1225.tfm) = %{tl_version}
Provides:       tex(c2so1226.tfm) = %{tl_version}, tex(c2so1227.tfm) = %{tl_version}
Provides:       tex(c2so1228.tfm) = %{tl_version}, tex(c2so1229.tfm) = %{tl_version}
Provides:       tex(c2so1230.tfm) = %{tl_version}, tex(c3so1201.tfm) = %{tl_version}
Provides:       tex(c3so1202.tfm) = %{tl_version}, tex(c3so1203.tfm) = %{tl_version}
Provides:       tex(c3so1204.tfm) = %{tl_version}, tex(c3so1205.tfm) = %{tl_version}
Provides:       tex(c3so1206.tfm) = %{tl_version}, tex(c3so1207.tfm) = %{tl_version}
Provides:       tex(c3so1208.tfm) = %{tl_version}, tex(c3so1209.tfm) = %{tl_version}
Provides:       tex(c3so1210.tfm) = %{tl_version}, tex(c3so1211.tfm) = %{tl_version}
Provides:       tex(c3so1212.tfm) = %{tl_version}, tex(c3so1213.tfm) = %{tl_version}
Provides:       tex(c3so1214.tfm) = %{tl_version}, tex(c3so1215.tfm) = %{tl_version}
Provides:       tex(c3so1216.tfm) = %{tl_version}, tex(c3so1217.tfm) = %{tl_version}
Provides:       tex(c3so1218.tfm) = %{tl_version}, tex(c3so1219.tfm) = %{tl_version}
Provides:       tex(c3so1220.tfm) = %{tl_version}, tex(c3so1221.tfm) = %{tl_version}
Provides:       tex(c3so1222.tfm) = %{tl_version}, tex(c3so1223.tfm) = %{tl_version}
Provides:       tex(c3so1224.tfm) = %{tl_version}, tex(c3so1225.tfm) = %{tl_version}
Provides:       tex(c4so1201.tfm) = %{tl_version}, tex(c4so1202.tfm) = %{tl_version}
Provides:       tex(c4so1203.tfm) = %{tl_version}, tex(c4so1204.tfm) = %{tl_version}
Provides:       tex(c4so1205.tfm) = %{tl_version}, tex(c4so1206.tfm) = %{tl_version}
Provides:       tex(c4so1207.tfm) = %{tl_version}, tex(c4so1208.tfm) = %{tl_version}
Provides:       tex(c4so1209.tfm) = %{tl_version}, tex(c4so1210.tfm) = %{tl_version}
Provides:       tex(c4so1211.tfm) = %{tl_version}, tex(c4so1212.tfm) = %{tl_version}
Provides:       tex(c4so1213.tfm) = %{tl_version}, tex(c4so1214.tfm) = %{tl_version}
Provides:       tex(c4so1215.tfm) = %{tl_version}, tex(c4so1216.tfm) = %{tl_version}
Provides:       tex(c4so1217.tfm) = %{tl_version}, tex(c4so1218.tfm) = %{tl_version}
Provides:       tex(c4so1219.tfm) = %{tl_version}, tex(c4so1220.tfm) = %{tl_version}
Provides:       tex(c4so1221.tfm) = %{tl_version}, tex(c4so1222.tfm) = %{tl_version}
Provides:       tex(c4so1223.tfm) = %{tl_version}, tex(c4so1224.tfm) = %{tl_version}
Provides:       tex(c4so1225.tfm) = %{tl_version}, tex(c4so1226.tfm) = %{tl_version}
Provides:       tex(c4so1227.tfm) = %{tl_version}, tex(c4so1228.tfm) = %{tl_version}
Provides:       tex(c4so1229.tfm) = %{tl_version}, tex(c5so1201.tfm) = %{tl_version}
Provides:       tex(c5so1202.tfm) = %{tl_version}, tex(c5so1203.tfm) = %{tl_version}
Provides:       tex(c5so1204.tfm) = %{tl_version}, tex(c5so1205.tfm) = %{tl_version}
Provides:       tex(c5so1206.tfm) = %{tl_version}, tex(c5so1207.tfm) = %{tl_version}
Provides:       tex(c5so1208.tfm) = %{tl_version}, tex(c5so1209.tfm) = %{tl_version}
Provides:       tex(c5so1210.tfm) = %{tl_version}, tex(c5so1211.tfm) = %{tl_version}
Provides:       tex(c5so1212.tfm) = %{tl_version}, tex(c5so1213.tfm) = %{tl_version}
Provides:       tex(c5so1214.tfm) = %{tl_version}, tex(c5so1215.tfm) = %{tl_version}
Provides:       tex(c5so1216.tfm) = %{tl_version}, tex(c5so1217.tfm) = %{tl_version}
Provides:       tex(c5so1218.tfm) = %{tl_version}, tex(c5so1219.tfm) = %{tl_version}
Provides:       tex(c5so1220.tfm) = %{tl_version}, tex(c5so1221.tfm) = %{tl_version}
Provides:       tex(c5so1222.tfm) = %{tl_version}, tex(c5so1223.tfm) = %{tl_version}
Provides:       tex(c5so1224.tfm) = %{tl_version}, tex(c5so1225.tfm) = %{tl_version}
Provides:       tex(c5so1226.tfm) = %{tl_version}, tex(c5so1227.tfm) = %{tl_version}
Provides:       tex(c5so1228.tfm) = %{tl_version}, tex(c5so1229.tfm) = %{tl_version}
Provides:       tex(c5so1230.tfm) = %{tl_version}, tex(c5so1231.tfm) = %{tl_version}
Provides:       tex(c5so1232.tfm) = %{tl_version}, tex(c5so1233.tfm) = %{tl_version}
Provides:       tex(c5so1234.tfm) = %{tl_version}, tex(c6so1201.tfm) = %{tl_version}
Provides:       tex(c6so1202.tfm) = %{tl_version}, tex(c6so1203.tfm) = %{tl_version}
Provides:       tex(c6so1204.tfm) = %{tl_version}, tex(c6so1205.tfm) = %{tl_version}
Provides:       tex(c6so1206.tfm) = %{tl_version}, tex(c6so1207.tfm) = %{tl_version}
Provides:       tex(c6so1208.tfm) = %{tl_version}, tex(c6so1209.tfm) = %{tl_version}
Provides:       tex(c6so1210.tfm) = %{tl_version}, tex(c6so1211.tfm) = %{tl_version}
Provides:       tex(c6so1212.tfm) = %{tl_version}, tex(c6so1213.tfm) = %{tl_version}
Provides:       tex(c6so1214.tfm) = %{tl_version}, tex(c6so1215.tfm) = %{tl_version}
Provides:       tex(c6so1216.tfm) = %{tl_version}, tex(c6so1217.tfm) = %{tl_version}
Provides:       tex(c6so1218.tfm) = %{tl_version}, tex(c6so1219.tfm) = %{tl_version}
Provides:       tex(c6so1220.tfm) = %{tl_version}, tex(c6so1221.tfm) = %{tl_version}
Provides:       tex(c6so1222.tfm) = %{tl_version}, tex(c6so1223.tfm) = %{tl_version}
Provides:       tex(c6so1224.tfm) = %{tl_version}, tex(c6so1225.tfm) = %{tl_version}
Provides:       tex(c7so1201.tfm) = %{tl_version}, tex(c7so1202.tfm) = %{tl_version}
Provides:       tex(c7so1203.tfm) = %{tl_version}, tex(c7so1204.tfm) = %{tl_version}
Provides:       tex(c7so1205.tfm) = %{tl_version}, tex(c7so1206.tfm) = %{tl_version}
Provides:       tex(c7so1207.tfm) = %{tl_version}, tex(c7so1208.tfm) = %{tl_version}
Provides:       tex(c7so1209.tfm) = %{tl_version}, tex(c7so1210.tfm) = %{tl_version}
Provides:       tex(c7so1211.tfm) = %{tl_version}, tex(c7so1212.tfm) = %{tl_version}
Provides:       tex(c7so1213.tfm) = %{tl_version}, tex(c7so1214.tfm) = %{tl_version}
Provides:       tex(c7so1215.tfm) = %{tl_version}, tex(c7so1216.tfm) = %{tl_version}
Provides:       tex(c7so1217.tfm) = %{tl_version}, tex(c7so1218.tfm) = %{tl_version}
Provides:       tex(c7so1219.tfm) = %{tl_version}, tex(c7so1220.tfm) = %{tl_version}
Provides:       tex(c7so1221.tfm) = %{tl_version}, tex(c7so1222.tfm) = %{tl_version}
Provides:       tex(c7so1223.tfm) = %{tl_version}, tex(c7so1224.tfm) = %{tl_version}
Provides:       tex(c7so1225.tfm) = %{tl_version}, tex(c7so1226.tfm) = %{tl_version}

%description -n texlive-cns
cns package

%package -n texlive-cns-doc
Summary:        Documentation for cns
Version:        svn45677
Provides:       tex-cns-doc
AutoReqProv:    No

%description -n texlive-cns-doc
Documentation for cns

%package -n texlive-classics
Provides:       tex-classics = %{tl_version}
License:        LPPL 1.3
Summary:        Cite classic works
Version:        svn29018.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(xparse.sty)
Provides:       tex(classics.sty) = %{tl_version}

%description -n texlive-classics
The package provides a basic framework to cite classic works
(specially from authors such as Homer, Plato, Aristotle,
Descartes, Hume, and Kant) in accordance with traditional
pagination systems. It may be used in conjunction with other
citation packages.

%package -n texlive-classics-doc
Summary:        Documentation for classics
Version:        svn29018.0.1

Provides:       tex-classics-doc
AutoReqProv:    No

%description -n texlive-classics-doc
Documentation for classics

%package -n texlive-classicthesis
Provides:       tex-classicthesis = %{tl_version}
License:        GPLv2+
Summary:        A "classically styled" thesis package
Version:        svn48041
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(listings.sty), tex(ifpdf.sty), tex(hyperref.sty)
Requires:       tex(ifxetex.sty), tex(xcolor.sty), tex(mathpazo.sty), tex(beramono.sty)
Requires:       tex(eulervm.sty), tex(microtype.sty), tex(typearea.sty), tex(booktabs.sty)
Requires:       tex(textcase.sty), tex(soul.sty), tex(scrlayer-scrpage.sty), tex(titlesec.sty)
Requires:       tex(tocloft.sty), tex(footmisc.sty), tex(scrtime.sty), tex(prelim2e.sty)
Requires:       tex(remreset.sty)
Provides:       tex(classicthesis.sty) = %{tl_version}

%description -n texlive-classicthesis
The classicthesis package provides an elegant layout designed
in homage to Bringhurst's "The Elements of Typographic Style".
It makes use of a range of techniques to get the best results
achievable using TeX. Included in the bundle are templates to
make thesis writing easier.

%package -n texlive-classicthesis-doc
Summary:        Documentation for classicthesis
Version:        svn48041
Provides:       tex-classicthesis-doc
AutoReqProv:    No

%description -n texlive-classicthesis-doc
Documentation for classicthesis

%package -n texlive-classpack
Provides:       tex-classpack = %{tl_version}
License:        LPPL 1.3
Summary:        XML mastering for LaTeX classes and packages
Version:        svn33101.0.77

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(classpack.sty) = %{tl_version}

%description -n texlive-classpack
The package provides an experiment in using XML (specifically
DocBook 5) to mark up and maintain LaTeX classes and packages.
XSLT 2 styleheets generate the .dtx and .ins distribution files
expected by end users.

%package -n texlive-classpack-doc
Summary:        Documentation for classpack
Version:        svn33101.0.77

Provides:       tex-classpack-doc
AutoReqProv:    No

%description -n texlive-classpack-doc
Documentation for classpack

%package -n texlive-cleanthesis
Provides:       tex-cleanthesis = %{tl_version}
License:        LPPL 1.3
Summary:        A clean LaTeX style for thesis documents
Version:        svn38221.0.3.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(xcolor.sty), tex(fontenc.sty), tex(tgheros.sty)
Requires:       tex(lmodern.sty), tex(charter.sty), tex(fixltx2e.sty), tex(microtype.sty)
Requires:       tex(setspace.sty), tex(graphicx.sty), tex(fancyhdr.sty), tex(enumitem.sty)
Requires:       tex(blindtext.sty), tex(textcomp.sty), tex(hyperref.sty), tex(caption.sty)
Requires:       tex(geometry.sty), tex(csquotes.sty), tex(biblatex.sty), tex(titlesec.sty)
Requires:       tex(tocloft.sty)
Provides:       tex(cleanthesis.sty) = %{tl_version}

%description -n texlive-cleanthesis
The package offers a clean, simple, and elegant LaTeX style for
thesis documents.

%package -n texlive-cleanthesis-doc
Summary:        Documentation for cleanthesis
Version:        svn38221.0.3.1

Provides:       tex-cleanthesis-doc
AutoReqProv:    No

%description -n texlive-cleanthesis-doc
Documentation for cleanthesis

%package -n texlive-clearsans
Provides:       tex-clearsans = %{tl_version}
License:        ASL 2.0
Summary:        Clear Sans fonts with LaTeX support
Version:        svn34405.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(xkeyval.sty), tex(textcomp.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty), tex(mweights.sty)
Provides:       tex(clr_er7w2x.enc) = %{tl_version}, tex(clr_nrghxx.enc) = %{tl_version}
Provides:       tex(clr_y7ge35.enc) = %{tl_version}, tex(clr_zjpm5y.enc) = %{tl_version}
Provides:       tex(ClearSans.map) = %{tl_version}, tex(ClearSans-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(ClearSans-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(ClearSans-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(ClearSans-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(ClearSans-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Light-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Light-lf-ly1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Light-lf-ot1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Light-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Light-lf-t1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Light-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Light-lf-ts1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Medium-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Medium-lf-ly1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Medium-lf-ot1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Medium-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Medium-lf-t1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Medium-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Medium-lf-ts1.tfm) = %{tl_version}
Provides:       tex(ClearSans-MediumItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-MediumItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(ClearSans-MediumItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(ClearSans-MediumItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-MediumItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(ClearSans-MediumItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-MediumItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Thin-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Thin-lf-ly1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Thin-lf-ot1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Thin-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Thin-lf-t1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Thin-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-Thin-lf-ts1.tfm) = %{tl_version}
Provides:       tex(ClearSans-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-lf-ly1.tfm) = %{tl_version}
Provides:       tex(ClearSans-lf-ot1.tfm) = %{tl_version}
Provides:       tex(ClearSans-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-lf-t1.tfm) = %{tl_version}
Provides:       tex(ClearSans-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ClearSans-lf-ts1.tfm) = %{tl_version}
Provides:       tex(ClearSans-Bold.ttf) = %{tl_version}, tex(ClearSans-BoldItalic.ttf) = %{tl_version}
Provides:       tex(ClearSans-Italic.ttf) = %{tl_version}
Provides:       tex(ClearSans-Light.ttf) = %{tl_version}
Provides:       tex(ClearSans-Medium.ttf) = %{tl_version}
Provides:       tex(ClearSans-MediumItalic.ttf) = %{tl_version}
Provides:       tex(ClearSans-Regular.ttf) = %{tl_version}
Provides:       tex(ClearSans-Thin.ttf) = %{tl_version}, tex(ClearSans-Bold.pfb) = %{tl_version}
Provides:       tex(ClearSans-BoldItalic.pfb) = %{tl_version}
Provides:       tex(ClearSans-Italic.pfb) = %{tl_version}
Provides:       tex(ClearSans-Light.pfb) = %{tl_version}
Provides:       tex(ClearSans-Medium.pfb) = %{tl_version}
Provides:       tex(ClearSans-MediumItalic.pfb) = %{tl_version}
Provides:       tex(ClearSans-Regular.pfb) = %{tl_version}
Provides:       tex(ClearSans-Thin.pfb) = %{tl_version}, tex(ClearSans-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(ClearSans-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(ClearSans-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(ClearSans-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(ClearSans-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(ClearSans-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(ClearSans-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(ClearSans-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(ClearSans-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(ClearSans-Light-lf-ly1.vf) = %{tl_version}
Provides:       tex(ClearSans-Light-lf-t1.vf) = %{tl_version}
Provides:       tex(ClearSans-Light-lf-ts1.vf) = %{tl_version}
Provides:       tex(ClearSans-Medium-lf-ly1.vf) = %{tl_version}
Provides:       tex(ClearSans-Medium-lf-t1.vf) = %{tl_version}
Provides:       tex(ClearSans-Medium-lf-ts1.vf) = %{tl_version}
Provides:       tex(ClearSans-MediumItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(ClearSans-MediumItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(ClearSans-MediumItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(ClearSans-Thin-lf-ly1.vf) = %{tl_version}
Provides:       tex(ClearSans-Thin-lf-t1.vf) = %{tl_version}
Provides:       tex(ClearSans-Thin-lf-ts1.vf) = %{tl_version}
Provides:       tex(ClearSans-lf-ly1.vf) = %{tl_version}
Provides:       tex(ClearSans-lf-t1.vf) = %{tl_version}, tex(ClearSans-lf-ts1.vf) = %{tl_version}
Provides:       tex(ClearSans.sty) = %{tl_version}, tex(LY1ClearSans-LF.fd) = %{tl_version}
Provides:       tex(LY1ClearSansLight-LF.fd) = %{tl_version}
Provides:       tex(LY1ClearSansThin-LF.fd) = %{tl_version}
Provides:       tex(OT1ClearSans-LF.fd) = %{tl_version}, tex(OT1ClearSansLight-LF.fd) = %{tl_version}
Provides:       tex(OT1ClearSansThin-LF.fd) = %{tl_version}
Provides:       tex(T1ClearSans-LF.fd) = %{tl_version}, tex(T1ClearSansLight-LF.fd) = %{tl_version}
Provides:       tex(T1ClearSansThin-LF.fd) = %{tl_version}
Provides:       tex(TS1ClearSans-LF.fd) = %{tl_version}, tex(TS1ClearSansLight-LF.fd) = %{tl_version}
Provides:       tex(TS1ClearSansThin-LF.fd) = %{tl_version}

%description -n texlive-clearsans
Clear Sans was designed by Daniel Ratighan at Monotype under
the direction of the User Experience team at Intel's Open
Source Technology Center. Clear Sans is available in three
weights (regular, medium, and bold) with corresponding italics,
plus light and thin upright (without italics). Clear Sans has
minimized, unambiguous characters and slightly narrow
proportions, making it ideal for UI design. Its strong,
recognizable forms avoid distracting ambiguity, making Clear
Sans comfortable for reading short UI labels and long passages
in both screen and print. The fonts are available in both
TrueType and Type 1 formats.

%package -n texlive-clearsans-doc
Summary:        Documentation for clearsans
Version:        svn34405.0

Provides:       tex-clearsans-doc
AutoReqProv:    No

%description -n texlive-clearsans-doc
Documentation for clearsans

%package -n texlive-clefval
Provides:       tex-clefval = %{tl_version}
License:        LPPL
Summary:        Key/value support with a hash
Version:        svn16549.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(clefval.sty) = %{tl_version}

%description -n texlive-clefval
This package provides only two macros viz. \TheKey and
\TheValue to define then use pairs of key/value and gives a
semblance of a hash. Syntax: \TheKey{key}{value} to define the
value associated to the key, does not produce text;
\TheValue{key} to return the value linked to the key. Both
arguments of \TheKey are 'moving' as LaTeX defines the term and
we have sometimes to protect them.

%package -n texlive-clefval-doc
Summary:        Documentation for clefval
Version:        svn16549.0

Provides:       tex-clefval-doc
AutoReqProv:    No

%description -n texlive-clefval-doc
Documentation for clefval

%package -n texlive-cleveref
Provides:       tex-cleveref = %{tl_version}
License:        LPPL
Summary:        Intelligent cross-referencing
Version:        svn47525
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(cleveref.sty) = %{tl_version}

%description -n texlive-cleveref
The package enhances LaTeX's cross-referencing features,
allowing the format of references to be determined
automatically according to the type of reference. The formats
used may be customised in the preamble of a document; babel
support is available (though the choice of languages remains
limited: currently Danish, Dutch, English, French, German,
Italian, Norwegian, Russian, Spanish and Ukranian). The package
also offers a means of referencing a list of references, each
formatted according to its type. In such lists, it can collapse
sequences of numerically-consecutive labels to a reference
range.

%package -n texlive-cleveref-doc
Summary:        Documentation for cleveref
Version:        svn47525
Provides:       tex-cleveref-doc
AutoReqProv:    No

%description -n texlive-cleveref-doc
Documentation for cleveref

%package -n texlive-clipboard
Provides:       tex-clipboard = %{tl_version}
License:        LPPL 1.3
Summary:        Copy and paste into and across documents
Version:        svn47747
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(clipboard.sty) = %{tl_version}

%description -n texlive-clipboard
The clipboard package provides a basic framework for copying
and pasting text and commands into and across multiple
documents. It replaces the copypaste package.

%package -n texlive-clipboard-doc
Summary:        Documentation for clipboard
Version:        svn47747
Provides:       tex-clipboard-doc
AutoReqProv:    No

%description -n texlive-clipboard-doc
Documentation for clipboard

%package -n texlive-clock
Provides:       tex-clock = %{tl_version}
License:        GPL+
Summary:        Graphical and textual clocks for TeX and LaTeX
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(clock.tfm) = %{tl_version}, tex(clock.sty) = %{tl_version}
Provides:       tex(clock.tex) = %{tl_version}

%description -n texlive-clock
Features graphical clocks (with a classical 12h dial and two
hands) and text clocks (in 24h format) which can show system
time or any time the user desires. Works with both TeX and
LaTeX. The clock faces (appearances of the dial) are easily
expandable; the default uses a custom Metafont font.

%package -n texlive-clock-doc
Summary:        Documentation for clock
Version:        svn15878.0

Provides:       tex-clock-doc
AutoReqProv:    No

%description -n texlive-clock-doc
Documentation for clock

%package -n texlive-cloze
Provides:       tex-cloze = %{tl_version}
License:        LPPL 1.3
Summary:        A LuaLaTeX package for creating cloze texts
Version:        svn41531
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fontspec.sty), tex(luatexbase-mcb.sty)
Requires:       tex(kvoptions.sty), tex(xcolor.sty)
Provides:       tex(cloze.sty) = %{tl_version}

%description -n texlive-cloze
This is a LuaLaTeX package for generating cloze texts. The main
feature of the package is that the formatting doesn't change
when using the hide and show options. There are three commands
and one environment to generate cloze texts: \cloze, \clozefix,
\closefil, and \closepar.

%package -n texlive-cloze-doc
Summary:        Documentation for cloze
Version:        svn41531
Provides:       tex-cloze-doc
AutoReqProv:    No

%description -n texlive-cloze-doc
Documentation for cloze

%package -n texlive-clrscode3e
Provides:       tex-clrscode3e = %{tl_version}
License:        LPPL
Summary:        Typesets pseudocode as in Introduction to Algorithms
Version:        svn34887.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty)
Provides:       tex(clrscode3e.sty) = %{tl_version}

%description -n texlive-clrscode3e
This package allows you to typeset pseudocode in the style of
Introduction to Algorithms, Third edition, by Cormen,
Leiserson, Rivest, and Stein. The package was written by the
authors. Use the commands the same way the package's author did
when writing the book, and your output will look just like the
pseudocode in the text.

%package -n texlive-clrscode3e-doc
Summary:        Documentation for clrscode3e
Version:        svn34887.0

Provides:       tex-clrscode3e-doc
AutoReqProv:    No

%description -n texlive-clrscode3e-doc
Documentation for clrscode3e

%package -n texlive-clrscode
Provides:       tex-clrscode = %{tl_version}
License:        LPPL
Summary:        Typesets pseudocode as in Introduction to Algorithms
Version:        svn15878.1.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(clrscode.sty) = %{tl_version}

%description -n texlive-clrscode
This package allows you to typeset pseudocode in the style of
Introduction to Algorithms, Second edition, by Cormen,
Leiserson, Rivest, and Stein. The package was written by the
authors. You use the commands the same way the package's author
did when writing the book, and your output will look just like
the pseudocode in the text.

%package -n texlive-clrscode-doc
Summary:        Documentation for clrscode
Version:        svn15878.1.7

Provides:       tex-clrscode-doc
AutoReqProv:    No

%description -n texlive-clrscode-doc
Documentation for clrscode

%package -n texlive-cmap
Provides:       tex-cmap = %{tl_version}
License:        LPPL
Summary:        Make PDF files searchable and copyable
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(cmap.sty) = %{tl_version}

%description -n texlive-cmap
The cmap package provides character map tables, which make PDF
files generated by pdfLaTeX both searchable and copy-able in
acrobat reader and other compliant PDF viewers. Encodings
supported are OT1, T1, T2A, T2B, T2C and T5, together with LAE
(Arabic), LFE (Farsi) and LGR (Greek) and a variant OT1tt for
cmtt-like fonts. The package's main limitation currently is the
inability to work with virtual fonts, because of limitations of
pdfTeX. This restriction may be resolved in a future version of
pdfTeX.

%package -n texlive-cmap-doc
Summary:        Documentation for cmap
Version:        svn42428
Provides:       tex-cmap-doc
AutoReqProv:    No

%description -n texlive-cmap-doc
Documentation for cmap

%package -n texlive-cmarrows
Provides:       tex-cmarrows = %{tl_version}
License:        LPPL
Summary:        MetaPost arrows and braces in the Computer Modern style
Version:        svn24378.v0.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-cmarrows
This MetaPost package contains macros to draw arrows and braces
in the Computer Modern style.

%package -n texlive-cmarrows-doc
Summary:        Documentation for cmarrows
Version:        svn24378.v0.9

Provides:       tex-cmarrows-doc
AutoReqProv:    No

%description -n texlive-cmarrows-doc
Documentation for cmarrows

%package -n texlive-cmbright
Provides:       tex-cmbright = %{tl_version}
License:        LPPL
Summary:        Computer Modern Bright fonts
Version:        svn21107.8.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cmbr10.tfm) = %{tl_version}, tex(cmbr17.tfm) = %{tl_version}
Provides:       tex(cmbr8.tfm) = %{tl_version}, tex(cmbr9.tfm) = %{tl_version}
Provides:       tex(cmbras10.tfm) = %{tl_version}, tex(cmbras8.tfm) = %{tl_version}
Provides:       tex(cmbras9.tfm) = %{tl_version}, tex(cmbrbs10.tfm) = %{tl_version}
Provides:       tex(cmbrbs8.tfm) = %{tl_version}, tex(cmbrbs9.tfm) = %{tl_version}
Provides:       tex(cmbrbx10.tfm) = %{tl_version}, tex(cmbrmb10.tfm) = %{tl_version}
Provides:       tex(cmbrmi10.tfm) = %{tl_version}, tex(cmbrmi8.tfm) = %{tl_version}
Provides:       tex(cmbrmi9.tfm) = %{tl_version}, tex(cmbrsl10.tfm) = %{tl_version}
Provides:       tex(cmbrsl17.tfm) = %{tl_version}, tex(cmbrsl8.tfm) = %{tl_version}
Provides:       tex(cmbrsl9.tfm) = %{tl_version}, tex(cmbrsy10.tfm) = %{tl_version}
Provides:       tex(cmbrsy8.tfm) = %{tl_version}, tex(cmbrsy9.tfm) = %{tl_version}
Provides:       tex(cmsltl10.tfm) = %{tl_version}, tex(cmtl10.tfm) = %{tl_version}
Provides:       tex(ebbx10.tfm) = %{tl_version}, tex(ebmo10.tfm) = %{tl_version}
Provides:       tex(ebmo17.tfm) = %{tl_version}, tex(ebmo8.tfm) = %{tl_version}
Provides:       tex(ebmo9.tfm) = %{tl_version}, tex(ebmr10.tfm) = %{tl_version}
Provides:       tex(ebmr17.tfm) = %{tl_version}, tex(ebmr8.tfm) = %{tl_version}
Provides:       tex(ebmr9.tfm) = %{tl_version}, tex(ebso10.tfm) = %{tl_version}
Provides:       tex(ebso17.tfm) = %{tl_version}, tex(ebso8.tfm) = %{tl_version}
Provides:       tex(ebso9.tfm) = %{tl_version}, tex(ebsr10.tfm) = %{tl_version}
Provides:       tex(ebsr17.tfm) = %{tl_version}, tex(ebsr8.tfm) = %{tl_version}
Provides:       tex(ebsr9.tfm) = %{tl_version}, tex(ebtl10.tfm) = %{tl_version}
Provides:       tex(ebto10.tfm) = %{tl_version}, tex(tbbx10.tfm) = %{tl_version}
Provides:       tex(tbmo10.tfm) = %{tl_version}, tex(tbmo17.tfm) = %{tl_version}
Provides:       tex(tbmo8.tfm) = %{tl_version}, tex(tbmo9.tfm) = %{tl_version}
Provides:       tex(tbmr10.tfm) = %{tl_version}, tex(tbmr17.tfm) = %{tl_version}
Provides:       tex(tbmr8.tfm) = %{tl_version}, tex(tbmr9.tfm) = %{tl_version}
Provides:       tex(tbso10.tfm) = %{tl_version}, tex(tbso17.tfm) = %{tl_version}
Provides:       tex(tbso8.tfm) = %{tl_version}, tex(tbso9.tfm) = %{tl_version}
Provides:       tex(tbsr10.tfm) = %{tl_version}, tex(tbsr17.tfm) = %{tl_version}
Provides:       tex(tbsr8.tfm) = %{tl_version}, tex(tbsr9.tfm) = %{tl_version}
Provides:       tex(tbtl10.tfm) = %{tl_version}, tex(tbto10.tfm) = %{tl_version}
Provides:       tex(cmbright.sty) = %{tl_version}, tex(omlcmbr.fd) = %{tl_version}
Provides:       tex(omlcmbrm.fd) = %{tl_version}, tex(omscmbr.fd) = %{tl_version}
Provides:       tex(omscmbrs.fd) = %{tl_version}, tex(ot1cmbr.fd) = %{tl_version}
Provides:       tex(ot1cmtl.fd) = %{tl_version}, tex(t1cmbr.fd) = %{tl_version}
Provides:       tex(t1cmtl.fd) = %{tl_version}, tex(ts1cmbr.fd) = %{tl_version}
Provides:       tex(ts1cmtl.fd) = %{tl_version}

%description -n texlive-cmbright
A family of sans serif fonts for TeX and LaTeX, based on Donald
Knuth's CM fonts. It comprises OT1, T1 and TS1 encoded text
fonts of various shapes as well as all the fonts necessary for
mathematical typesetting, including AMS symbols. This
collection provides all the necessary files for using the fonts
with LaTeX. A commercial-quality Adobe Type 1 version of these
fonts is available from Micropress. Free versions are
available, in the cm-super font bundle (the T1 and TS1 encoded
part of the set), and in the hfbright package (the OT1 encoded
part, and the maths fonts).

%package -n texlive-cmbright-doc
Summary:        Documentation for cmbright
Version:        svn21107.8.1

Provides:       tex-cmbright-doc
AutoReqProv:    No

%description -n texlive-cmbright-doc
Documentation for cmbright

%package -n texlive-cmcyr
Provides:       tex-cmcyr = %{tl_version}
License:        Public Domain
Summary:        Computer Modern fonts with cyrillic extensions
Version:        svn39273

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(cmcyr.map) = %{tl_version}, tex(cmcb10.tfm) = %{tl_version}
Provides:       tex(cmcbx10.tfm) = %{tl_version}, tex(cmcbx12.tfm) = %{tl_version}
Provides:       tex(cmcbx5.tfm) = %{tl_version}, tex(cmcbx6.tfm) = %{tl_version}
Provides:       tex(cmcbx7.tfm) = %{tl_version}, tex(cmcbx8.tfm) = %{tl_version}
Provides:       tex(cmcbx9.tfm) = %{tl_version}, tex(cmcbxsl10.tfm) = %{tl_version}
Provides:       tex(cmcbxti10.tfm) = %{tl_version}, tex(cmccsc10.tfm) = %{tl_version}
Provides:       tex(cmccsc8.tfm) = %{tl_version}, tex(cmccsc9.tfm) = %{tl_version}
Provides:       tex(cmcinch.tfm) = %{tl_version}, tex(cmcitt10.tfm) = %{tl_version}
Provides:       tex(cmcsl10.tfm) = %{tl_version}, tex(cmcsl12.tfm) = %{tl_version}
Provides:       tex(cmcsl8.tfm) = %{tl_version}, tex(cmcsl9.tfm) = %{tl_version}
Provides:       tex(cmcsltt10.tfm) = %{tl_version}, tex(cmcss10.tfm) = %{tl_version}
Provides:       tex(cmcss12.tfm) = %{tl_version}, tex(cmcss17.tfm) = %{tl_version}
Provides:       tex(cmcss8.tfm) = %{tl_version}, tex(cmcss9.tfm) = %{tl_version}
Provides:       tex(cmcssbx10.tfm) = %{tl_version}, tex(cmcssdc10.tfm) = %{tl_version}
Provides:       tex(cmcssi10.tfm) = %{tl_version}, tex(cmcssi12.tfm) = %{tl_version}
Provides:       tex(cmcssi17.tfm) = %{tl_version}, tex(cmcssi8.tfm) = %{tl_version}
Provides:       tex(cmcssi9.tfm) = %{tl_version}, tex(cmcssq8.tfm) = %{tl_version}
Provides:       tex(cmcssqi8.tfm) = %{tl_version}, tex(cmcti10.tfm) = %{tl_version}
Provides:       tex(cmcti12.tfm) = %{tl_version}, tex(cmcti7.tfm) = %{tl_version}
Provides:       tex(cmcti8.tfm) = %{tl_version}, tex(cmcti9.tfm) = %{tl_version}
Provides:       tex(cmctt10.tfm) = %{tl_version}, tex(cmctt12.tfm) = %{tl_version}
Provides:       tex(cmctt8.tfm) = %{tl_version}, tex(cmctt9.tfm) = %{tl_version}
Provides:       tex(cmcu10.tfm) = %{tl_version}, tex(cmcyr10.tfm) = %{tl_version}
Provides:       tex(cmcyr12.tfm) = %{tl_version}, tex(cmcyr17.tfm) = %{tl_version}
Provides:       tex(cmcyr5.tfm) = %{tl_version}, tex(cmcyr6.tfm) = %{tl_version}
Provides:       tex(cmcyr7.tfm) = %{tl_version}, tex(cmcyr8.tfm) = %{tl_version}
Provides:       tex(cmcyr9.tfm) = %{tl_version}, tex(kcmb10.tfm) = %{tl_version}
Provides:       tex(kcmbx10.tfm) = %{tl_version}, tex(kcmbx12.tfm) = %{tl_version}
Provides:       tex(kcmbx5.tfm) = %{tl_version}, tex(kcmbx6.tfm) = %{tl_version}
Provides:       tex(kcmbx7.tfm) = %{tl_version}, tex(kcmbx8.tfm) = %{tl_version}
Provides:       tex(kcmbx9.tfm) = %{tl_version}, tex(kcmbxsl10.tfm) = %{tl_version}
Provides:       tex(kcmbxti10.tfm) = %{tl_version}, tex(kcmcsc10.tfm) = %{tl_version}
Provides:       tex(kcmcsc8.tfm) = %{tl_version}, tex(kcmcsc9.tfm) = %{tl_version}
Provides:       tex(kcminch.tfm) = %{tl_version}, tex(kcmitt10.tfm) = %{tl_version}
Provides:       tex(kcmmi10.tfm) = %{tl_version}, tex(kcmmi12.tfm) = %{tl_version}
Provides:       tex(kcmmi5.tfm) = %{tl_version}, tex(kcmmi6.tfm) = %{tl_version}
Provides:       tex(kcmmi7.tfm) = %{tl_version}, tex(kcmmi8.tfm) = %{tl_version}
Provides:       tex(kcmmi9.tfm) = %{tl_version}, tex(kcmmib10.tfm) = %{tl_version}
Provides:       tex(kcmr10.tfm) = %{tl_version}, tex(kcmr12.tfm) = %{tl_version}
Provides:       tex(kcmr17.tfm) = %{tl_version}, tex(kcmr5.tfm) = %{tl_version}
Provides:       tex(kcmr6.tfm) = %{tl_version}, tex(kcmr7.tfm) = %{tl_version}
Provides:       tex(kcmr8.tfm) = %{tl_version}, tex(kcmr9.tfm) = %{tl_version}
Provides:       tex(kcmsl10.tfm) = %{tl_version}, tex(kcmsl12.tfm) = %{tl_version}
Provides:       tex(kcmsl8.tfm) = %{tl_version}, tex(kcmsl9.tfm) = %{tl_version}
Provides:       tex(kcmsltt10.tfm) = %{tl_version}, tex(kcmss10.tfm) = %{tl_version}
Provides:       tex(kcmss12.tfm) = %{tl_version}, tex(kcmss17.tfm) = %{tl_version}
Provides:       tex(kcmss8.tfm) = %{tl_version}, tex(kcmss9.tfm) = %{tl_version}
Provides:       tex(kcmssbx10.tfm) = %{tl_version}, tex(kcmssdc10.tfm) = %{tl_version}
Provides:       tex(kcmssi10.tfm) = %{tl_version}, tex(kcmssi12.tfm) = %{tl_version}
Provides:       tex(kcmssi17.tfm) = %{tl_version}, tex(kcmssi8.tfm) = %{tl_version}
Provides:       tex(kcmssi9.tfm) = %{tl_version}, tex(kcmssq8.tfm) = %{tl_version}
Provides:       tex(kcmssqi8.tfm) = %{tl_version}, tex(kcmti10.tfm) = %{tl_version}
Provides:       tex(kcmti12.tfm) = %{tl_version}, tex(kcmti7.tfm) = %{tl_version}
Provides:       tex(kcmti8.tfm) = %{tl_version}, tex(kcmti9.tfm) = %{tl_version}
Provides:       tex(kcmtt10.tfm) = %{tl_version}, tex(kcmtt12.tfm) = %{tl_version}
Provides:       tex(kcmtt8.tfm) = %{tl_version}, tex(kcmtt9.tfm) = %{tl_version}
Provides:       tex(kcmu10.tfm) = %{tl_version}, tex(wcmb10.tfm) = %{tl_version}
Provides:       tex(wcmbx10.tfm) = %{tl_version}, tex(wcmbx12.tfm) = %{tl_version}
Provides:       tex(wcmbx5.tfm) = %{tl_version}, tex(wcmbx6.tfm) = %{tl_version}
Provides:       tex(wcmbx7.tfm) = %{tl_version}, tex(wcmbx8.tfm) = %{tl_version}
Provides:       tex(wcmbx9.tfm) = %{tl_version}, tex(wcmbxsl10.tfm) = %{tl_version}
Provides:       tex(wcmbxti10.tfm) = %{tl_version}, tex(wcmcsc10.tfm) = %{tl_version}
Provides:       tex(wcmcsc8.tfm) = %{tl_version}, tex(wcmcsc9.tfm) = %{tl_version}
Provides:       tex(wcminch.tfm) = %{tl_version}, tex(wcmitt10.tfm) = %{tl_version}
Provides:       tex(wcmmi10.tfm) = %{tl_version}, tex(wcmmi12.tfm) = %{tl_version}
Provides:       tex(wcmmi5.tfm) = %{tl_version}, tex(wcmmi6.tfm) = %{tl_version}
Provides:       tex(wcmmi7.tfm) = %{tl_version}, tex(wcmmi8.tfm) = %{tl_version}
Provides:       tex(wcmmi9.tfm) = %{tl_version}, tex(wcmmib10.tfm) = %{tl_version}
Provides:       tex(wcmr10.tfm) = %{tl_version}, tex(wcmr12.tfm) = %{tl_version}
Provides:       tex(wcmr17.tfm) = %{tl_version}, tex(wcmr5.tfm) = %{tl_version}
Provides:       tex(wcmr6.tfm) = %{tl_version}, tex(wcmr7.tfm) = %{tl_version}
Provides:       tex(wcmr8.tfm) = %{tl_version}, tex(wcmr9.tfm) = %{tl_version}
Provides:       tex(wcmsl10.tfm) = %{tl_version}, tex(wcmsl12.tfm) = %{tl_version}
Provides:       tex(wcmsl8.tfm) = %{tl_version}, tex(wcmsl9.tfm) = %{tl_version}
Provides:       tex(wcmsltt10.tfm) = %{tl_version}, tex(wcmss10.tfm) = %{tl_version}
Provides:       tex(wcmss12.tfm) = %{tl_version}, tex(wcmss17.tfm) = %{tl_version}
Provides:       tex(wcmss8.tfm) = %{tl_version}, tex(wcmss9.tfm) = %{tl_version}
Provides:       tex(wcmssbx10.tfm) = %{tl_version}, tex(wcmssdc10.tfm) = %{tl_version}
Provides:       tex(wcmssi10.tfm) = %{tl_version}, tex(wcmssi12.tfm) = %{tl_version}
Provides:       tex(wcmssi17.tfm) = %{tl_version}, tex(wcmssi8.tfm) = %{tl_version}
Provides:       tex(wcmssi9.tfm) = %{tl_version}, tex(wcmssq8.tfm) = %{tl_version}
Provides:       tex(wcmssqi8.tfm) = %{tl_version}, tex(wcmti10.tfm) = %{tl_version}
Provides:       tex(wcmti12.tfm) = %{tl_version}, tex(wcmti7.tfm) = %{tl_version}
Provides:       tex(wcmti8.tfm) = %{tl_version}, tex(wcmti9.tfm) = %{tl_version}
Provides:       tex(wcmtt10.tfm) = %{tl_version}, tex(wcmtt12.tfm) = %{tl_version}
Provides:       tex(wcmtt8.tfm) = %{tl_version}, tex(wcmtt9.tfm) = %{tl_version}
Provides:       tex(wcmu10.tfm) = %{tl_version}, tex(xcmb10.tfm) = %{tl_version}
Provides:       tex(xcmbx10.tfm) = %{tl_version}, tex(xcmbx12.tfm) = %{tl_version}
Provides:       tex(xcmbx5.tfm) = %{tl_version}, tex(xcmbx6.tfm) = %{tl_version}
Provides:       tex(xcmbx7.tfm) = %{tl_version}, tex(xcmbx8.tfm) = %{tl_version}
Provides:       tex(xcmbx9.tfm) = %{tl_version}, tex(xcmbxsl10.tfm) = %{tl_version}
Provides:       tex(xcmbxti10.tfm) = %{tl_version}, tex(xcmcsc10.tfm) = %{tl_version}
Provides:       tex(xcmcsc8.tfm) = %{tl_version}, tex(xcmcsc9.tfm) = %{tl_version}
Provides:       tex(xcminch.tfm) = %{tl_version}, tex(xcmitt10.tfm) = %{tl_version}
Provides:       tex(xcmmi10.tfm) = %{tl_version}, tex(xcmmi12.tfm) = %{tl_version}
Provides:       tex(xcmmi5.tfm) = %{tl_version}, tex(xcmmi6.tfm) = %{tl_version}
Provides:       tex(xcmmi7.tfm) = %{tl_version}, tex(xcmmi8.tfm) = %{tl_version}
Provides:       tex(xcmmi9.tfm) = %{tl_version}, tex(xcmmib10.tfm) = %{tl_version}
Provides:       tex(xcmr10.tfm) = %{tl_version}, tex(xcmr12.tfm) = %{tl_version}
Provides:       tex(xcmr17.tfm) = %{tl_version}, tex(xcmr5.tfm) = %{tl_version}
Provides:       tex(xcmr6.tfm) = %{tl_version}, tex(xcmr7.tfm) = %{tl_version}
Provides:       tex(xcmr8.tfm) = %{tl_version}, tex(xcmr9.tfm) = %{tl_version}
Provides:       tex(xcmsl10.tfm) = %{tl_version}, tex(xcmsl12.tfm) = %{tl_version}
Provides:       tex(xcmsl8.tfm) = %{tl_version}, tex(xcmsl9.tfm) = %{tl_version}
Provides:       tex(xcmsltt10.tfm) = %{tl_version}, tex(xcmss10.tfm) = %{tl_version}
Provides:       tex(xcmss12.tfm) = %{tl_version}, tex(xcmss17.tfm) = %{tl_version}
Provides:       tex(xcmss8.tfm) = %{tl_version}, tex(xcmss9.tfm) = %{tl_version}
Provides:       tex(xcmssbx10.tfm) = %{tl_version}, tex(xcmssdc10.tfm) = %{tl_version}
Provides:       tex(xcmssi10.tfm) = %{tl_version}, tex(xcmssi12.tfm) = %{tl_version}
Provides:       tex(xcmssi17.tfm) = %{tl_version}, tex(xcmssi8.tfm) = %{tl_version}
Provides:       tex(xcmssi9.tfm) = %{tl_version}, tex(xcmssq8.tfm) = %{tl_version}
Provides:       tex(xcmssqi8.tfm) = %{tl_version}, tex(xcmti10.tfm) = %{tl_version}
Provides:       tex(xcmti12.tfm) = %{tl_version}, tex(xcmti7.tfm) = %{tl_version}
Provides:       tex(xcmti8.tfm) = %{tl_version}, tex(xcmti9.tfm) = %{tl_version}
Provides:       tex(xcmtt10.tfm) = %{tl_version}, tex(xcmtt12.tfm) = %{tl_version}
Provides:       tex(xcmtt8.tfm) = %{tl_version}, tex(xcmtt9.tfm) = %{tl_version}
Provides:       tex(xcmu10.tfm) = %{tl_version}, tex(ycmb10.tfm) = %{tl_version}
Provides:       tex(ycmbx10.tfm) = %{tl_version}, tex(ycmbx12.tfm) = %{tl_version}
Provides:       tex(ycmbx5.tfm) = %{tl_version}, tex(ycmbx6.tfm) = %{tl_version}
Provides:       tex(ycmbx7.tfm) = %{tl_version}, tex(ycmbx8.tfm) = %{tl_version}
Provides:       tex(ycmbx9.tfm) = %{tl_version}, tex(ycmbxsl10.tfm) = %{tl_version}
Provides:       tex(ycmbxti10.tfm) = %{tl_version}, tex(ycmcsc10.tfm) = %{tl_version}
Provides:       tex(ycmcsc8.tfm) = %{tl_version}, tex(ycmcsc9.tfm) = %{tl_version}
Provides:       tex(ycminch.tfm) = %{tl_version}, tex(ycmitt10.tfm) = %{tl_version}
Provides:       tex(ycmmi10.tfm) = %{tl_version}, tex(ycmmi12.tfm) = %{tl_version}
Provides:       tex(ycmmi5.tfm) = %{tl_version}, tex(ycmmi6.tfm) = %{tl_version}
Provides:       tex(ycmmi7.tfm) = %{tl_version}, tex(ycmmi8.tfm) = %{tl_version}
Provides:       tex(ycmmi9.tfm) = %{tl_version}, tex(ycmmib10.tfm) = %{tl_version}
Provides:       tex(ycmr10.tfm) = %{tl_version}, tex(ycmr12.tfm) = %{tl_version}
Provides:       tex(ycmr17.tfm) = %{tl_version}, tex(ycmr5.tfm) = %{tl_version}
Provides:       tex(ycmr6.tfm) = %{tl_version}, tex(ycmr7.tfm) = %{tl_version}
Provides:       tex(ycmr8.tfm) = %{tl_version}, tex(ycmr9.tfm) = %{tl_version}
Provides:       tex(ycmsl10.tfm) = %{tl_version}, tex(ycmsl12.tfm) = %{tl_version}
Provides:       tex(ycmsl8.tfm) = %{tl_version}, tex(ycmsl9.tfm) = %{tl_version}
Provides:       tex(ycmsltt10.tfm) = %{tl_version}, tex(ycmss10.tfm) = %{tl_version}
Provides:       tex(ycmss12.tfm) = %{tl_version}, tex(ycmss17.tfm) = %{tl_version}
Provides:       tex(ycmss8.tfm) = %{tl_version}, tex(ycmss9.tfm) = %{tl_version}
Provides:       tex(ycmssbx10.tfm) = %{tl_version}, tex(ycmssdc10.tfm) = %{tl_version}
Provides:       tex(ycmssi10.tfm) = %{tl_version}, tex(ycmssi12.tfm) = %{tl_version}
Provides:       tex(ycmssi17.tfm) = %{tl_version}, tex(ycmssi8.tfm) = %{tl_version}
Provides:       tex(ycmssi9.tfm) = %{tl_version}, tex(ycmssq8.tfm) = %{tl_version}
Provides:       tex(ycmssqi8.tfm) = %{tl_version}, tex(ycmti10.tfm) = %{tl_version}
Provides:       tex(ycmti12.tfm) = %{tl_version}, tex(ycmti7.tfm) = %{tl_version}
Provides:       tex(ycmti8.tfm) = %{tl_version}, tex(ycmti9.tfm) = %{tl_version}
Provides:       tex(ycmtt10.tfm) = %{tl_version}, tex(ycmtt12.tfm) = %{tl_version}
Provides:       tex(ycmtt8.tfm) = %{tl_version}, tex(ycmtt9.tfm) = %{tl_version}
Provides:       tex(ycmu10.tfm) = %{tl_version}, tex(cmcb10.pfb) = %{tl_version}
Provides:       tex(cmcbx10.pfb) = %{tl_version}, tex(cmcbx12.pfb) = %{tl_version}
Provides:       tex(cmcbx5.pfb) = %{tl_version}, tex(cmcbx6.pfb) = %{tl_version}
Provides:       tex(cmcbx7.pfb) = %{tl_version}, tex(cmcbx8.pfb) = %{tl_version}
Provides:       tex(cmcbx9.pfb) = %{tl_version}, tex(cmcbxsl1.pfb) = %{tl_version}
Provides:       tex(cmcbxti1.pfb) = %{tl_version}, tex(cmccsc10.pfb) = %{tl_version}
Provides:       tex(cmccsc8.pfb) = %{tl_version}, tex(cmccsc9.pfb) = %{tl_version}
Provides:       tex(cmcinch7.pfb) = %{tl_version}, tex(cmcitt10.pfb) = %{tl_version}
Provides:       tex(cmcsl10.pfb) = %{tl_version}, tex(cmcsl12.pfb) = %{tl_version}
Provides:       tex(cmcsl8.pfb) = %{tl_version}, tex(cmcsl9.pfb) = %{tl_version}
Provides:       tex(cmcsltt1.pfb) = %{tl_version}, tex(cmcss10.pfb) = %{tl_version}
Provides:       tex(cmcss12.pfb) = %{tl_version}, tex(cmcss17.pfb) = %{tl_version}
Provides:       tex(cmcss8.pfb) = %{tl_version}, tex(cmcss9.pfb) = %{tl_version}
Provides:       tex(cmcssbx1.pfb) = %{tl_version}, tex(cmcssdc1.pfb) = %{tl_version}
Provides:       tex(cmcssi10.pfb) = %{tl_version}, tex(cmcssi12.pfb) = %{tl_version}
Provides:       tex(cmcssi17.pfb) = %{tl_version}, tex(cmcssi8.pfb) = %{tl_version}
Provides:       tex(cmcssi9.pfb) = %{tl_version}, tex(cmcssq8.pfb) = %{tl_version}
Provides:       tex(cmcssqi8.pfb) = %{tl_version}, tex(cmcti10.pfb) = %{tl_version}
Provides:       tex(cmcti12.pfb) = %{tl_version}, tex(cmcti7.pfb) = %{tl_version}
Provides:       tex(cmcti8.pfb) = %{tl_version}, tex(cmcti9.pfb) = %{tl_version}
Provides:       tex(cmctt10.pfb) = %{tl_version}, tex(cmctt12.pfb) = %{tl_version}
Provides:       tex(cmctt8.pfb) = %{tl_version}, tex(cmctt9.pfb) = %{tl_version}
Provides:       tex(cmcu10.pfb) = %{tl_version}, tex(cmcyr10.pfb) = %{tl_version}
Provides:       tex(cmcyr12.pfb) = %{tl_version}, tex(cmcyr17.pfb) = %{tl_version}
Provides:       tex(cmcyr5.pfb) = %{tl_version}, tex(cmcyr6.pfb) = %{tl_version}
Provides:       tex(cmcyr7.pfb) = %{tl_version}, tex(cmcyr8.pfb) = %{tl_version}
Provides:       tex(cmcyr9.pfb) = %{tl_version}, tex(kcmb10.vf) = %{tl_version}
Provides:       tex(kcmbx10.vf) = %{tl_version}, tex(kcmbx12.vf) = %{tl_version}
Provides:       tex(kcmbx5.vf) = %{tl_version}, tex(kcmbx6.vf) = %{tl_version}
Provides:       tex(kcmbx7.vf) = %{tl_version}, tex(kcmbx8.vf) = %{tl_version}
Provides:       tex(kcmbx9.vf) = %{tl_version}, tex(kcmbxsl10.vf) = %{tl_version}
Provides:       tex(kcmbxti10.vf) = %{tl_version}, tex(kcmcsc10.vf) = %{tl_version}
Provides:       tex(kcmcsc8.vf) = %{tl_version}, tex(kcmcsc9.vf) = %{tl_version}
Provides:       tex(kcminch.vf) = %{tl_version}, tex(kcmitt10.vf) = %{tl_version}
Provides:       tex(kcmmi10.vf) = %{tl_version}, tex(kcmmi12.vf) = %{tl_version}
Provides:       tex(kcmmi5.vf) = %{tl_version}, tex(kcmmi6.vf) = %{tl_version}
Provides:       tex(kcmmi7.vf) = %{tl_version}, tex(kcmmi8.vf) = %{tl_version}
Provides:       tex(kcmmi9.vf) = %{tl_version}, tex(kcmmib10.vf) = %{tl_version}
Provides:       tex(kcmr10.vf) = %{tl_version}, tex(kcmr12.vf) = %{tl_version}
Provides:       tex(kcmr17.vf) = %{tl_version}, tex(kcmr5.vf) = %{tl_version}
Provides:       tex(kcmr6.vf) = %{tl_version}, tex(kcmr7.vf) = %{tl_version}
Provides:       tex(kcmr8.vf) = %{tl_version}, tex(kcmr9.vf) = %{tl_version}
Provides:       tex(kcmsl10.vf) = %{tl_version}, tex(kcmsl12.vf) = %{tl_version}
Provides:       tex(kcmsl8.vf) = %{tl_version}, tex(kcmsl9.vf) = %{tl_version}
Provides:       tex(kcmsltt10.vf) = %{tl_version}, tex(kcmss10.vf) = %{tl_version}
Provides:       tex(kcmss12.vf) = %{tl_version}, tex(kcmss17.vf) = %{tl_version}
Provides:       tex(kcmss8.vf) = %{tl_version}, tex(kcmss9.vf) = %{tl_version}
Provides:       tex(kcmssbx10.vf) = %{tl_version}, tex(kcmssdc10.vf) = %{tl_version}
Provides:       tex(kcmssi10.vf) = %{tl_version}, tex(kcmssi12.vf) = %{tl_version}
Provides:       tex(kcmssi17.vf) = %{tl_version}, tex(kcmssi8.vf) = %{tl_version}
Provides:       tex(kcmssi9.vf) = %{tl_version}, tex(kcmssq8.vf) = %{tl_version}
Provides:       tex(kcmssqi8.vf) = %{tl_version}, tex(kcmti10.vf) = %{tl_version}
Provides:       tex(kcmti12.vf) = %{tl_version}, tex(kcmti7.vf) = %{tl_version}
Provides:       tex(kcmti8.vf) = %{tl_version}, tex(kcmti9.vf) = %{tl_version}
Provides:       tex(kcmtt10.vf) = %{tl_version}, tex(kcmtt12.vf) = %{tl_version}
Provides:       tex(kcmtt8.vf) = %{tl_version}, tex(kcmtt9.vf) = %{tl_version}
Provides:       tex(kcmu10.vf) = %{tl_version}, tex(wcmb10.vf) = %{tl_version}
Provides:       tex(wcmbx10.vf) = %{tl_version}, tex(wcmbx12.vf) = %{tl_version}
Provides:       tex(wcmbx5.vf) = %{tl_version}, tex(wcmbx6.vf) = %{tl_version}
Provides:       tex(wcmbx7.vf) = %{tl_version}, tex(wcmbx8.vf) = %{tl_version}
Provides:       tex(wcmbx9.vf) = %{tl_version}, tex(wcmbxsl10.vf) = %{tl_version}
Provides:       tex(wcmbxti10.vf) = %{tl_version}, tex(wcmcsc10.vf) = %{tl_version}
Provides:       tex(wcmcsc8.vf) = %{tl_version}, tex(wcmcsc9.vf) = %{tl_version}
Provides:       tex(wcminch.vf) = %{tl_version}, tex(wcmitt10.vf) = %{tl_version}
Provides:       tex(wcmmi10.vf) = %{tl_version}, tex(wcmmi12.vf) = %{tl_version}
Provides:       tex(wcmmi5.vf) = %{tl_version}, tex(wcmmi6.vf) = %{tl_version}
Provides:       tex(wcmmi7.vf) = %{tl_version}, tex(wcmmi8.vf) = %{tl_version}
Provides:       tex(wcmmi9.vf) = %{tl_version}, tex(wcmmib10.vf) = %{tl_version}
Provides:       tex(wcmr10.vf) = %{tl_version}, tex(wcmr12.vf) = %{tl_version}
Provides:       tex(wcmr17.vf) = %{tl_version}, tex(wcmr5.vf) = %{tl_version}
Provides:       tex(wcmr6.vf) = %{tl_version}, tex(wcmr7.vf) = %{tl_version}
Provides:       tex(wcmr8.vf) = %{tl_version}, tex(wcmr9.vf) = %{tl_version}
Provides:       tex(wcmsl10.vf) = %{tl_version}, tex(wcmsl12.vf) = %{tl_version}
Provides:       tex(wcmsl8.vf) = %{tl_version}, tex(wcmsl9.vf) = %{tl_version}
Provides:       tex(wcmsltt10.vf) = %{tl_version}, tex(wcmss10.vf) = %{tl_version}
Provides:       tex(wcmss12.vf) = %{tl_version}, tex(wcmss17.vf) = %{tl_version}
Provides:       tex(wcmss8.vf) = %{tl_version}, tex(wcmss9.vf) = %{tl_version}
Provides:       tex(wcmssbx10.vf) = %{tl_version}, tex(wcmssdc10.vf) = %{tl_version}
Provides:       tex(wcmssi10.vf) = %{tl_version}, tex(wcmssi12.vf) = %{tl_version}
Provides:       tex(wcmssi17.vf) = %{tl_version}, tex(wcmssi8.vf) = %{tl_version}
Provides:       tex(wcmssi9.vf) = %{tl_version}, tex(wcmssq8.vf) = %{tl_version}
Provides:       tex(wcmssqi8.vf) = %{tl_version}, tex(wcmti10.vf) = %{tl_version}
Provides:       tex(wcmti12.vf) = %{tl_version}, tex(wcmti7.vf) = %{tl_version}
Provides:       tex(wcmti8.vf) = %{tl_version}, tex(wcmti9.vf) = %{tl_version}
Provides:       tex(wcmtt10.vf) = %{tl_version}, tex(wcmtt12.vf) = %{tl_version}
Provides:       tex(wcmtt8.vf) = %{tl_version}, tex(wcmtt9.vf) = %{tl_version}
Provides:       tex(wcmu10.vf) = %{tl_version}, tex(xcmb10.vf) = %{tl_version}
Provides:       tex(xcmbx10.vf) = %{tl_version}, tex(xcmbx12.vf) = %{tl_version}
Provides:       tex(xcmbx5.vf) = %{tl_version}, tex(xcmbx6.vf) = %{tl_version}
Provides:       tex(xcmbx7.vf) = %{tl_version}, tex(xcmbx8.vf) = %{tl_version}
Provides:       tex(xcmbx9.vf) = %{tl_version}, tex(xcmbxsl10.vf) = %{tl_version}
Provides:       tex(xcmbxti10.vf) = %{tl_version}, tex(xcmcsc10.vf) = %{tl_version}
Provides:       tex(xcmcsc8.vf) = %{tl_version}, tex(xcmcsc9.vf) = %{tl_version}
Provides:       tex(xcminch.vf) = %{tl_version}, tex(xcmitt10.vf) = %{tl_version}
Provides:       tex(xcmmi10.vf) = %{tl_version}, tex(xcmmi12.vf) = %{tl_version}
Provides:       tex(xcmmi5.vf) = %{tl_version}, tex(xcmmi6.vf) = %{tl_version}
Provides:       tex(xcmmi7.vf) = %{tl_version}, tex(xcmmi8.vf) = %{tl_version}
Provides:       tex(xcmmi9.vf) = %{tl_version}, tex(xcmmib10.vf) = %{tl_version}
Provides:       tex(xcmr10.vf) = %{tl_version}, tex(xcmr12.vf) = %{tl_version}
Provides:       tex(xcmr17.vf) = %{tl_version}, tex(xcmr5.vf) = %{tl_version}
Provides:       tex(xcmr6.vf) = %{tl_version}, tex(xcmr7.vf) = %{tl_version}
Provides:       tex(xcmr8.vf) = %{tl_version}, tex(xcmr9.vf) = %{tl_version}
Provides:       tex(xcmsl10.vf) = %{tl_version}, tex(xcmsl12.vf) = %{tl_version}
Provides:       tex(xcmsl8.vf) = %{tl_version}, tex(xcmsl9.vf) = %{tl_version}
Provides:       tex(xcmsltt10.vf) = %{tl_version}, tex(xcmss10.vf) = %{tl_version}
Provides:       tex(xcmss12.vf) = %{tl_version}, tex(xcmss17.vf) = %{tl_version}
Provides:       tex(xcmss8.vf) = %{tl_version}, tex(xcmss9.vf) = %{tl_version}
Provides:       tex(xcmssbx10.vf) = %{tl_version}, tex(xcmssdc10.vf) = %{tl_version}
Provides:       tex(xcmssi10.vf) = %{tl_version}, tex(xcmssi12.vf) = %{tl_version}
Provides:       tex(xcmssi17.vf) = %{tl_version}, tex(xcmssi8.vf) = %{tl_version}
Provides:       tex(xcmssi9.vf) = %{tl_version}, tex(xcmssq8.vf) = %{tl_version}
Provides:       tex(xcmssqi8.vf) = %{tl_version}, tex(xcmti10.vf) = %{tl_version}
Provides:       tex(xcmti12.vf) = %{tl_version}, tex(xcmti7.vf) = %{tl_version}
Provides:       tex(xcmti8.vf) = %{tl_version}, tex(xcmti9.vf) = %{tl_version}
Provides:       tex(xcmtt10.vf) = %{tl_version}, tex(xcmtt12.vf) = %{tl_version}
Provides:       tex(xcmtt8.vf) = %{tl_version}, tex(xcmtt9.vf) = %{tl_version}
Provides:       tex(xcmu10.vf) = %{tl_version}, tex(ycmb10.vf) = %{tl_version}
Provides:       tex(ycmbx10.vf) = %{tl_version}, tex(ycmbx12.vf) = %{tl_version}
Provides:       tex(ycmbx5.vf) = %{tl_version}, tex(ycmbx6.vf) = %{tl_version}
Provides:       tex(ycmbx7.vf) = %{tl_version}, tex(ycmbx8.vf) = %{tl_version}
Provides:       tex(ycmbx9.vf) = %{tl_version}, tex(ycmbxsl10.vf) = %{tl_version}
Provides:       tex(ycmbxti10.vf) = %{tl_version}, tex(ycmcsc10.vf) = %{tl_version}
Provides:       tex(ycmcsc8.vf) = %{tl_version}, tex(ycmcsc9.vf) = %{tl_version}
Provides:       tex(ycminch.vf) = %{tl_version}, tex(ycmitt10.vf) = %{tl_version}
Provides:       tex(ycmmi10.vf) = %{tl_version}, tex(ycmmi12.vf) = %{tl_version}
Provides:       tex(ycmmi5.vf) = %{tl_version}, tex(ycmmi6.vf) = %{tl_version}
Provides:       tex(ycmmi7.vf) = %{tl_version}, tex(ycmmi8.vf) = %{tl_version}
Provides:       tex(ycmmi9.vf) = %{tl_version}, tex(ycmmib10.vf) = %{tl_version}
Provides:       tex(ycmr10.vf) = %{tl_version}, tex(ycmr12.vf) = %{tl_version}
Provides:       tex(ycmr17.vf) = %{tl_version}, tex(ycmr5.vf) = %{tl_version}
Provides:       tex(ycmr6.vf) = %{tl_version}, tex(ycmr7.vf) = %{tl_version}
Provides:       tex(ycmr8.vf) = %{tl_version}, tex(ycmr9.vf) = %{tl_version}
Provides:       tex(ycmsl10.vf) = %{tl_version}, tex(ycmsl12.vf) = %{tl_version}
Provides:       tex(ycmsl8.vf) = %{tl_version}, tex(ycmsl9.vf) = %{tl_version}
Provides:       tex(ycmsltt10.vf) = %{tl_version}, tex(ycmss10.vf) = %{tl_version}
Provides:       tex(ycmss12.vf) = %{tl_version}, tex(ycmss17.vf) = %{tl_version}
Provides:       tex(ycmss8.vf) = %{tl_version}, tex(ycmss9.vf) = %{tl_version}
Provides:       tex(ycmssbx10.vf) = %{tl_version}, tex(ycmssdc10.vf) = %{tl_version}
Provides:       tex(ycmssi10.vf) = %{tl_version}, tex(ycmssi12.vf) = %{tl_version}
Provides:       tex(ycmssi17.vf) = %{tl_version}, tex(ycmssi8.vf) = %{tl_version}
Provides:       tex(ycmssi9.vf) = %{tl_version}, tex(ycmssq8.vf) = %{tl_version}
Provides:       tex(ycmssqi8.vf) = %{tl_version}, tex(ycmti10.vf) = %{tl_version}
Provides:       tex(ycmti12.vf) = %{tl_version}, tex(ycmti7.vf) = %{tl_version}
Provides:       tex(ycmti8.vf) = %{tl_version}, tex(ycmti9.vf) = %{tl_version}
Provides:       tex(ycmtt10.vf) = %{tl_version}, tex(ycmtt12.vf) = %{tl_version}
Provides:       tex(ycmtt8.vf) = %{tl_version}, tex(ycmtt9.vf) = %{tl_version}
Provides:       tex(ycmu10.vf) = %{tl_version}

%description -n texlive-cmcyr
These are the Computer Modern fonts extended with Russian
letters, in Metafont sources and ATM Compatible Type 1 format.
The fonts are provided in KOI-7, but virtual fonts are
available to recode them to three other Russian 8-bit
encodings.

%package -n texlive-cmcyr-doc
Summary:        Documentation for cmcyr
Version:        svn39273

Provides:       tex-cmcyr-doc
AutoReqProv:    No

%description -n texlive-cmcyr-doc
Documentation for cmcyr

%package -n texlive-cmdstring
Provides:       tex-cmdstring = %{tl_version}
License:        LPPL
Summary:        Get command name reliably
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cmdstring.sty) = %{tl_version}

%description -n texlive-cmdstring
Extracts the letters of a command's name (e.g., foo for command
\foo), in a reliable way.

%package -n texlive-cmdstring-doc
Summary:        Documentation for cmdstring
Version:        svn15878.1.1

Provides:       tex-cmdstring-doc
AutoReqProv:    No

%description -n texlive-cmdstring-doc
Documentation for cmdstring

%package -n texlive-cmextra
Provides:       tex-cmextra = %{tl_version}
License:        Knuth
Summary:        Knuth's local information
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(bible12.tfm) = %{tl_version}, tex(cmbxcd10.tfm) = %{tl_version}
Provides:       tex(cmbxti12.tfm) = %{tl_version}, tex(cmbxti7.tfm) = %{tl_version}
Provides:       tex(cmcscsl10.tfm) = %{tl_version}, tex(cmfibs8.tfm) = %{tl_version}
Provides:       tex(cmitt12.tfm) = %{tl_version}, tex(cmitt9.tfm) = %{tl_version}
Provides:       tex(cmman.tfm) = %{tl_version}, tex(cmntex10.tfm) = %{tl_version}
Provides:       tex(cmntt10.tfm) = %{tl_version}, tex(cmsl6.tfm) = %{tl_version}
Provides:       tex(cmsltt9.tfm) = %{tl_version}, tex(cmssbxo10.tfm) = %{tl_version}
Provides:       tex(cmsslu30.tfm) = %{tl_version}, tex(cmssu30.tfm) = %{tl_version}
Provides:       tex(cmsytt10.tfm) = %{tl_version}, tex(cmtim.tfm) = %{tl_version}
Provides:       tex(cmvtti10.tfm) = %{tl_version}, tex(diam12.tfm) = %{tl_version}
Provides:       tex(gen10.tfm) = %{tl_version}, tex(gen8.tfm) = %{tl_version}
Provides:       tex(gen9.tfm) = %{tl_version}

%description -n texlive-cmextra
A collection of experimental programs and developments based
on, or complementary to, the matter in his distribution
directories.

%package -n texlive-cm-lgc
Provides:       tex-cm-lgc = %{tl_version}
License:        GPL+
Summary:        Type 1 CM-based fonts for Latin, Greek and Cyrillic
Version:        svn28250.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(8r-mod.enc) = %{tl_version}, tex(cm-lgc.map) = %{tl_version}
Provides:       tex(fcmb6a.tfm) = %{tl_version}, tex(fcmb6y.tfm) = %{tl_version}
Provides:       tex(fcmb6z.tfm) = %{tl_version}, tex(fcmb7k.tfm) = %{tl_version}
Provides:       tex(fcmb7t.tfm) = %{tl_version}, tex(fcmb8a.tfm) = %{tl_version}
Provides:       tex(fcmb8c.tfm) = %{tl_version}, tex(fcmb8r.tfm) = %{tl_version}
Provides:       tex(fcmb8t.tfm) = %{tl_version}, tex(fcmbc6a.tfm) = %{tl_version}
Provides:       tex(fcmbc6y.tfm) = %{tl_version}, tex(fcmbc6z.tfm) = %{tl_version}
Provides:       tex(fcmbc7k.tfm) = %{tl_version}, tex(fcmbc7t.tfm) = %{tl_version}
Provides:       tex(fcmbc8a.tfm) = %{tl_version}, tex(fcmbc8r.tfm) = %{tl_version}
Provides:       tex(fcmbc8t.tfm) = %{tl_version}, tex(fcmbcce.tfm) = %{tl_version}
Provides:       tex(fcmbce.tfm) = %{tl_version}, tex(fcmbcgr.tfm) = %{tl_version}
Provides:       tex(fcmbcpg.tfm) = %{tl_version}, tex(fcmbgr.tfm) = %{tl_version}
Provides:       tex(fcmbi6a.tfm) = %{tl_version}, tex(fcmbi6y.tfm) = %{tl_version}
Provides:       tex(fcmbi6z.tfm) = %{tl_version}, tex(fcmbi7k.tfm) = %{tl_version}
Provides:       tex(fcmbi7t.tfm) = %{tl_version}, tex(fcmbi8a.tfm) = %{tl_version}
Provides:       tex(fcmbi8c.tfm) = %{tl_version}, tex(fcmbi8r.tfm) = %{tl_version}
Provides:       tex(fcmbi8t.tfm) = %{tl_version}, tex(fcmbice.tfm) = %{tl_version}
Provides:       tex(fcmbigr.tfm) = %{tl_version}, tex(fcmbij8a.tfm) = %{tl_version}
Provides:       tex(fcmbij8r.tfm) = %{tl_version}, tex(fcmbipg.tfm) = %{tl_version}
Provides:       tex(fcmbo6a.tfm) = %{tl_version}, tex(fcmbo6y.tfm) = %{tl_version}
Provides:       tex(fcmbo6z.tfm) = %{tl_version}, tex(fcmbo7k.tfm) = %{tl_version}
Provides:       tex(fcmbo7t.tfm) = %{tl_version}, tex(fcmbo8c.tfm) = %{tl_version}
Provides:       tex(fcmbo8r.tfm) = %{tl_version}, tex(fcmbo8t.tfm) = %{tl_version}
Provides:       tex(fcmboc8r.tfm) = %{tl_version}, tex(fcmboce.tfm) = %{tl_version}
Provides:       tex(fcmbogr.tfm) = %{tl_version}, tex(fcmbopg.tfm) = %{tl_version}
Provides:       tex(fcmbpg.tfm) = %{tl_version}, tex(fcmbu6a.tfm) = %{tl_version}
Provides:       tex(fcmbu6y.tfm) = %{tl_version}, tex(fcmbu6z.tfm) = %{tl_version}
Provides:       tex(fcmbu7k.tfm) = %{tl_version}, tex(fcmbu7t.tfm) = %{tl_version}
Provides:       tex(fcmbu8c.tfm) = %{tl_version}, tex(fcmbu8r.tfm) = %{tl_version}
Provides:       tex(fcmbu8t.tfm) = %{tl_version}, tex(fcmbuce.tfm) = %{tl_version}
Provides:       tex(fcmbugr.tfm) = %{tl_version}, tex(fcmbuj8r.tfm) = %{tl_version}
Provides:       tex(fcmbupg.tfm) = %{tl_version}, tex(fcmr6a.tfm) = %{tl_version}
Provides:       tex(fcmr6y.tfm) = %{tl_version}, tex(fcmr6z.tfm) = %{tl_version}
Provides:       tex(fcmr7k.tfm) = %{tl_version}, tex(fcmr7t.tfm) = %{tl_version}
Provides:       tex(fcmr8a.tfm) = %{tl_version}, tex(fcmr8c.tfm) = %{tl_version}
Provides:       tex(fcmr8r.tfm) = %{tl_version}, tex(fcmr8t.tfm) = %{tl_version}
Provides:       tex(fcmrc6a.tfm) = %{tl_version}, tex(fcmrc6y.tfm) = %{tl_version}
Provides:       tex(fcmrc6z.tfm) = %{tl_version}, tex(fcmrc7k.tfm) = %{tl_version}
Provides:       tex(fcmrc7t.tfm) = %{tl_version}, tex(fcmrc8a.tfm) = %{tl_version}
Provides:       tex(fcmrc8r.tfm) = %{tl_version}, tex(fcmrc8t.tfm) = %{tl_version}
Provides:       tex(fcmrcce.tfm) = %{tl_version}, tex(fcmrce.tfm) = %{tl_version}
Provides:       tex(fcmrcgr.tfm) = %{tl_version}, tex(fcmrcpg.tfm) = %{tl_version}
Provides:       tex(fcmrgr.tfm) = %{tl_version}, tex(fcmri6a.tfm) = %{tl_version}
Provides:       tex(fcmri6y.tfm) = %{tl_version}, tex(fcmri6z.tfm) = %{tl_version}
Provides:       tex(fcmri7k.tfm) = %{tl_version}, tex(fcmri7t.tfm) = %{tl_version}
Provides:       tex(fcmri8a.tfm) = %{tl_version}, tex(fcmri8c.tfm) = %{tl_version}
Provides:       tex(fcmri8r.tfm) = %{tl_version}, tex(fcmri8t.tfm) = %{tl_version}
Provides:       tex(fcmrice.tfm) = %{tl_version}, tex(fcmrigr.tfm) = %{tl_version}
Provides:       tex(fcmrij8a.tfm) = %{tl_version}, tex(fcmrij8r.tfm) = %{tl_version}
Provides:       tex(fcmripg.tfm) = %{tl_version}, tex(fcmro6a.tfm) = %{tl_version}
Provides:       tex(fcmro6y.tfm) = %{tl_version}, tex(fcmro6z.tfm) = %{tl_version}
Provides:       tex(fcmro7k.tfm) = %{tl_version}, tex(fcmro7t.tfm) = %{tl_version}
Provides:       tex(fcmro8c.tfm) = %{tl_version}, tex(fcmro8r.tfm) = %{tl_version}
Provides:       tex(fcmro8t.tfm) = %{tl_version}, tex(fcmroc8r.tfm) = %{tl_version}
Provides:       tex(fcmroce.tfm) = %{tl_version}, tex(fcmrogr.tfm) = %{tl_version}
Provides:       tex(fcmropg.tfm) = %{tl_version}, tex(fcmrpg.tfm) = %{tl_version}
Provides:       tex(fcmru6a.tfm) = %{tl_version}, tex(fcmru6y.tfm) = %{tl_version}
Provides:       tex(fcmru6z.tfm) = %{tl_version}, tex(fcmru7k.tfm) = %{tl_version}
Provides:       tex(fcmru7t.tfm) = %{tl_version}, tex(fcmru8c.tfm) = %{tl_version}
Provides:       tex(fcmru8r.tfm) = %{tl_version}, tex(fcmru8t.tfm) = %{tl_version}
Provides:       tex(fcmruce.tfm) = %{tl_version}, tex(fcmrugr.tfm) = %{tl_version}
Provides:       tex(fcmruj8r.tfm) = %{tl_version}, tex(fcmrupg.tfm) = %{tl_version}
Provides:       tex(fcsb6a.tfm) = %{tl_version}, tex(fcsb6y.tfm) = %{tl_version}
Provides:       tex(fcsb6z.tfm) = %{tl_version}, tex(fcsb7k.tfm) = %{tl_version}
Provides:       tex(fcsb7t.tfm) = %{tl_version}, tex(fcsb8a.tfm) = %{tl_version}
Provides:       tex(fcsb8c.tfm) = %{tl_version}, tex(fcsb8r.tfm) = %{tl_version}
Provides:       tex(fcsb8t.tfm) = %{tl_version}, tex(fcsbce.tfm) = %{tl_version}
Provides:       tex(fcsbgr.tfm) = %{tl_version}, tex(fcsbo6a.tfm) = %{tl_version}
Provides:       tex(fcsbo6y.tfm) = %{tl_version}, tex(fcsbo6z.tfm) = %{tl_version}
Provides:       tex(fcsbo7k.tfm) = %{tl_version}, tex(fcsbo7t.tfm) = %{tl_version}
Provides:       tex(fcsbo8a.tfm) = %{tl_version}, tex(fcsbo8c.tfm) = %{tl_version}
Provides:       tex(fcsbo8r.tfm) = %{tl_version}, tex(fcsbo8t.tfm) = %{tl_version}
Provides:       tex(fcsboce.tfm) = %{tl_version}, tex(fcsbogr.tfm) = %{tl_version}
Provides:       tex(fcsbopg.tfm) = %{tl_version}, tex(fcsbpg.tfm) = %{tl_version}
Provides:       tex(fcsr6a.tfm) = %{tl_version}, tex(fcsr6y.tfm) = %{tl_version}
Provides:       tex(fcsr6z.tfm) = %{tl_version}, tex(fcsr7k.tfm) = %{tl_version}
Provides:       tex(fcsr7t.tfm) = %{tl_version}, tex(fcsr8a.tfm) = %{tl_version}
Provides:       tex(fcsr8c.tfm) = %{tl_version}, tex(fcsr8r.tfm) = %{tl_version}
Provides:       tex(fcsr8t.tfm) = %{tl_version}, tex(fcsrce.tfm) = %{tl_version}
Provides:       tex(fcsrgr.tfm) = %{tl_version}, tex(fcsro6a.tfm) = %{tl_version}
Provides:       tex(fcsro6y.tfm) = %{tl_version}, tex(fcsro6z.tfm) = %{tl_version}
Provides:       tex(fcsro7k.tfm) = %{tl_version}, tex(fcsro7t.tfm) = %{tl_version}
Provides:       tex(fcsro8a.tfm) = %{tl_version}, tex(fcsro8c.tfm) = %{tl_version}
Provides:       tex(fcsro8r.tfm) = %{tl_version}, tex(fcsro8t.tfm) = %{tl_version}
Provides:       tex(fcsroce.tfm) = %{tl_version}, tex(fcsrogr.tfm) = %{tl_version}
Provides:       tex(fcsropg.tfm) = %{tl_version}, tex(fcsrpg.tfm) = %{tl_version}
Provides:       tex(fctr6a.tfm) = %{tl_version}, tex(fctr6y.tfm) = %{tl_version}
Provides:       tex(fctr6z.tfm) = %{tl_version}, tex(fctr7k.tfm) = %{tl_version}
Provides:       tex(fctr7t.tfm) = %{tl_version}, tex(fctr8a.tfm) = %{tl_version}
Provides:       tex(fctr8c.tfm) = %{tl_version}, tex(fctr8r.tfm) = %{tl_version}
Provides:       tex(fctr8t.tfm) = %{tl_version}, tex(fctrc6a.tfm) = %{tl_version}
Provides:       tex(fctrc6y.tfm) = %{tl_version}, tex(fctrc6z.tfm) = %{tl_version}
Provides:       tex(fctrc7k.tfm) = %{tl_version}, tex(fctrc7t.tfm) = %{tl_version}
Provides:       tex(fctrc8a.tfm) = %{tl_version}, tex(fctrc8r.tfm) = %{tl_version}
Provides:       tex(fctrc8t.tfm) = %{tl_version}, tex(fctrcce.tfm) = %{tl_version}
Provides:       tex(fctrce.tfm) = %{tl_version}, tex(fctrcgr.tfm) = %{tl_version}
Provides:       tex(fctrcpg.tfm) = %{tl_version}, tex(fctrgr.tfm) = %{tl_version}
Provides:       tex(fctri6a.tfm) = %{tl_version}, tex(fctri6y.tfm) = %{tl_version}
Provides:       tex(fctri6z.tfm) = %{tl_version}, tex(fctri7k.tfm) = %{tl_version}
Provides:       tex(fctri7t.tfm) = %{tl_version}, tex(fctri8a.tfm) = %{tl_version}
Provides:       tex(fctri8c.tfm) = %{tl_version}, tex(fctri8r.tfm) = %{tl_version}
Provides:       tex(fctri8t.tfm) = %{tl_version}, tex(fctrice.tfm) = %{tl_version}
Provides:       tex(fctrigr.tfm) = %{tl_version}, tex(fctrij8a.tfm) = %{tl_version}
Provides:       tex(fctrij8r.tfm) = %{tl_version}, tex(fctripg.tfm) = %{tl_version}
Provides:       tex(fctro6a.tfm) = %{tl_version}, tex(fctro6y.tfm) = %{tl_version}
Provides:       tex(fctro6z.tfm) = %{tl_version}, tex(fctro7k.tfm) = %{tl_version}
Provides:       tex(fctro7t.tfm) = %{tl_version}, tex(fctro8c.tfm) = %{tl_version}
Provides:       tex(fctro8r.tfm) = %{tl_version}, tex(fctro8t.tfm) = %{tl_version}
Provides:       tex(fctroc8r.tfm) = %{tl_version}, tex(fctroce.tfm) = %{tl_version}
Provides:       tex(fctrogr.tfm) = %{tl_version}, tex(fctropg.tfm) = %{tl_version}
Provides:       tex(fctrpg.tfm) = %{tl_version}, tex(fctru6a.tfm) = %{tl_version}
Provides:       tex(fctru6y.tfm) = %{tl_version}, tex(fctru6z.tfm) = %{tl_version}
Provides:       tex(fctru7k.tfm) = %{tl_version}, tex(fctru7t.tfm) = %{tl_version}
Provides:       tex(fctru8c.tfm) = %{tl_version}, tex(fctru8r.tfm) = %{tl_version}
Provides:       tex(fctru8t.tfm) = %{tl_version}, tex(fctruce.tfm) = %{tl_version}
Provides:       tex(fctrugr.tfm) = %{tl_version}, tex(fctruj8r.tfm) = %{tl_version}
Provides:       tex(fctrupg.tfm) = %{tl_version}, tex(fcmb6y.pfb) = %{tl_version}
Provides:       tex(fcmb6z.pfb) = %{tl_version}, tex(fcmb8a.pfb) = %{tl_version}
Provides:       tex(fcmbc6y.pfb) = %{tl_version}, tex(fcmbc6z.pfb) = %{tl_version}
Provides:       tex(fcmbc8a.pfb) = %{tl_version}, tex(fcmbcce.pfb) = %{tl_version}
Provides:       tex(fcmbce.pfb) = %{tl_version}, tex(fcmbcpg.pfb) = %{tl_version}
Provides:       tex(fcmbi6y.pfb) = %{tl_version}, tex(fcmbi6z.pfb) = %{tl_version}
Provides:       tex(fcmbi8a.pfb) = %{tl_version}, tex(fcmbice.pfb) = %{tl_version}
Provides:       tex(fcmbij6y.pfb) = %{tl_version}, tex(fcmbij6z.pfb) = %{tl_version}
Provides:       tex(fcmbij8a.pfb) = %{tl_version}, tex(fcmbijce.pfb) = %{tl_version}
Provides:       tex(fcmbijpg.pfb) = %{tl_version}, tex(fcmbipg.pfb) = %{tl_version}
Provides:       tex(fcmbpg.pfb) = %{tl_version}, tex(fcmr6y.pfb) = %{tl_version}
Provides:       tex(fcmr6z.pfb) = %{tl_version}, tex(fcmr8a.pfb) = %{tl_version}
Provides:       tex(fcmrc6y.pfb) = %{tl_version}, tex(fcmrc6z.pfb) = %{tl_version}
Provides:       tex(fcmrc8a.pfb) = %{tl_version}, tex(fcmrcce.pfb) = %{tl_version}
Provides:       tex(fcmrce.pfb) = %{tl_version}, tex(fcmrcpg.pfb) = %{tl_version}
Provides:       tex(fcmri6y.pfb) = %{tl_version}, tex(fcmri6z.pfb) = %{tl_version}
Provides:       tex(fcmri8a.pfb) = %{tl_version}, tex(fcmrice.pfb) = %{tl_version}
Provides:       tex(fcmrij6y.pfb) = %{tl_version}, tex(fcmrij6z.pfb) = %{tl_version}
Provides:       tex(fcmrij8a.pfb) = %{tl_version}, tex(fcmrijce.pfb) = %{tl_version}
Provides:       tex(fcmrijpg.pfb) = %{tl_version}, tex(fcmripg.pfb) = %{tl_version}
Provides:       tex(fcmrpg.pfb) = %{tl_version}, tex(fcsb6y.pfb) = %{tl_version}
Provides:       tex(fcsb6z.pfb) = %{tl_version}, tex(fcsb8a.pfb) = %{tl_version}
Provides:       tex(fcsbce.pfb) = %{tl_version}, tex(fcsbo6y.pfb) = %{tl_version}
Provides:       tex(fcsbo6z.pfb) = %{tl_version}, tex(fcsbo8a.pfb) = %{tl_version}
Provides:       tex(fcsboce.pfb) = %{tl_version}, tex(fcsbopg.pfb) = %{tl_version}
Provides:       tex(fcsbpg.pfb) = %{tl_version}, tex(fcsr6y.pfb) = %{tl_version}
Provides:       tex(fcsr6z.pfb) = %{tl_version}, tex(fcsr8a.pfb) = %{tl_version}
Provides:       tex(fcsrce.pfb) = %{tl_version}, tex(fcsro6y.pfb) = %{tl_version}
Provides:       tex(fcsro6z.pfb) = %{tl_version}, tex(fcsro8a.pfb) = %{tl_version}
Provides:       tex(fcsroce.pfb) = %{tl_version}, tex(fcsropg.pfb) = %{tl_version}
Provides:       tex(fcsrpg.pfb) = %{tl_version}, tex(fctr6y.pfb) = %{tl_version}
Provides:       tex(fctr6z.pfb) = %{tl_version}, tex(fctr8a.pfb) = %{tl_version}
Provides:       tex(fctrc6y.pfb) = %{tl_version}, tex(fctrc6z.pfb) = %{tl_version}
Provides:       tex(fctrc8a.pfb) = %{tl_version}, tex(fctrcce.pfb) = %{tl_version}
Provides:       tex(fctrce.pfb) = %{tl_version}, tex(fctrcpg.pfb) = %{tl_version}
Provides:       tex(fctri6y.pfb) = %{tl_version}, tex(fctri6z.pfb) = %{tl_version}
Provides:       tex(fctri8a.pfb) = %{tl_version}, tex(fctrice.pfb) = %{tl_version}
Provides:       tex(fctrij6y.pfb) = %{tl_version}, tex(fctrij6z.pfb) = %{tl_version}
Provides:       tex(fctrij8a.pfb) = %{tl_version}, tex(fctrijce.pfb) = %{tl_version}
Provides:       tex(fctrijpg.pfb) = %{tl_version}, tex(fctripg.pfb) = %{tl_version}
Provides:       tex(fctrpg.pfb) = %{tl_version}, tex(fcmb6a.vf) = %{tl_version}
Provides:       tex(fcmb7k.vf) = %{tl_version}, tex(fcmb7t.vf) = %{tl_version}
Provides:       tex(fcmb8c.vf) = %{tl_version}, tex(fcmb8t.vf) = %{tl_version}
Provides:       tex(fcmbc6a.vf) = %{tl_version}, tex(fcmbc7k.vf) = %{tl_version}
Provides:       tex(fcmbc7t.vf) = %{tl_version}, tex(fcmbc8t.vf) = %{tl_version}
Provides:       tex(fcmbcgr.vf) = %{tl_version}, tex(fcmbgr.vf) = %{tl_version}
Provides:       tex(fcmbi6a.vf) = %{tl_version}, tex(fcmbi7k.vf) = %{tl_version}
Provides:       tex(fcmbi7t.vf) = %{tl_version}, tex(fcmbi8c.vf) = %{tl_version}
Provides:       tex(fcmbi8t.vf) = %{tl_version}, tex(fcmbigr.vf) = %{tl_version}
Provides:       tex(fcmbo6a.vf) = %{tl_version}, tex(fcmbo7k.vf) = %{tl_version}
Provides:       tex(fcmbo7t.vf) = %{tl_version}, tex(fcmbo8c.vf) = %{tl_version}
Provides:       tex(fcmbo8t.vf) = %{tl_version}, tex(fcmbogr.vf) = %{tl_version}
Provides:       tex(fcmbu6a.vf) = %{tl_version}, tex(fcmbu7k.vf) = %{tl_version}
Provides:       tex(fcmbu7t.vf) = %{tl_version}, tex(fcmbu8c.vf) = %{tl_version}
Provides:       tex(fcmbu8t.vf) = %{tl_version}, tex(fcmbugr.vf) = %{tl_version}
Provides:       tex(fcmr6a.vf) = %{tl_version}, tex(fcmr7k.vf) = %{tl_version}
Provides:       tex(fcmr7t.vf) = %{tl_version}, tex(fcmr8c.vf) = %{tl_version}
Provides:       tex(fcmr8t.vf) = %{tl_version}, tex(fcmrc6a.vf) = %{tl_version}
Provides:       tex(fcmrc7k.vf) = %{tl_version}, tex(fcmrc7t.vf) = %{tl_version}
Provides:       tex(fcmrc8t.vf) = %{tl_version}, tex(fcmrcgr.vf) = %{tl_version}
Provides:       tex(fcmrgr.vf) = %{tl_version}, tex(fcmri6a.vf) = %{tl_version}
Provides:       tex(fcmri7k.vf) = %{tl_version}, tex(fcmri7t.vf) = %{tl_version}
Provides:       tex(fcmri8c.vf) = %{tl_version}, tex(fcmri8t.vf) = %{tl_version}
Provides:       tex(fcmrigr.vf) = %{tl_version}, tex(fcmro6a.vf) = %{tl_version}
Provides:       tex(fcmro7k.vf) = %{tl_version}, tex(fcmro7t.vf) = %{tl_version}
Provides:       tex(fcmro8c.vf) = %{tl_version}, tex(fcmro8t.vf) = %{tl_version}
Provides:       tex(fcmrogr.vf) = %{tl_version}, tex(fcmru6a.vf) = %{tl_version}
Provides:       tex(fcmru7k.vf) = %{tl_version}, tex(fcmru7t.vf) = %{tl_version}
Provides:       tex(fcmru8c.vf) = %{tl_version}, tex(fcmru8t.vf) = %{tl_version}
Provides:       tex(fcmrugr.vf) = %{tl_version}, tex(fcsb6a.vf) = %{tl_version}
Provides:       tex(fcsb7k.vf) = %{tl_version}, tex(fcsb7t.vf) = %{tl_version}
Provides:       tex(fcsb8c.vf) = %{tl_version}, tex(fcsb8t.vf) = %{tl_version}
Provides:       tex(fcsbgr.vf) = %{tl_version}, tex(fcsbo6a.vf) = %{tl_version}
Provides:       tex(fcsbo7k.vf) = %{tl_version}, tex(fcsbo7t.vf) = %{tl_version}
Provides:       tex(fcsbo8c.vf) = %{tl_version}, tex(fcsbo8t.vf) = %{tl_version}
Provides:       tex(fcsbogr.vf) = %{tl_version}, tex(fcsr6a.vf) = %{tl_version}
Provides:       tex(fcsr7k.vf) = %{tl_version}, tex(fcsr7t.vf) = %{tl_version}
Provides:       tex(fcsr8c.vf) = %{tl_version}, tex(fcsr8t.vf) = %{tl_version}
Provides:       tex(fcsrgr.vf) = %{tl_version}, tex(fcsro6a.vf) = %{tl_version}
Provides:       tex(fcsro7k.vf) = %{tl_version}, tex(fcsro7t.vf) = %{tl_version}
Provides:       tex(fcsro8c.vf) = %{tl_version}, tex(fcsro8t.vf) = %{tl_version}
Provides:       tex(fcsrogr.vf) = %{tl_version}, tex(fctr6a.vf) = %{tl_version}
Provides:       tex(fctr7k.vf) = %{tl_version}, tex(fctr7t.vf) = %{tl_version}
Provides:       tex(fctr8c.vf) = %{tl_version}, tex(fctr8t.vf) = %{tl_version}
Provides:       tex(fctrc6a.vf) = %{tl_version}, tex(fctrc7k.vf) = %{tl_version}
Provides:       tex(fctrc7t.vf) = %{tl_version}, tex(fctrc8t.vf) = %{tl_version}
Provides:       tex(fctrcgr.vf) = %{tl_version}, tex(fctrgr.vf) = %{tl_version}
Provides:       tex(fctri6a.vf) = %{tl_version}, tex(fctri7k.vf) = %{tl_version}
Provides:       tex(fctri7t.vf) = %{tl_version}, tex(fctri8c.vf) = %{tl_version}
Provides:       tex(fctri8t.vf) = %{tl_version}, tex(fctrigr.vf) = %{tl_version}
Provides:       tex(fctro6a.vf) = %{tl_version}, tex(fctro7k.vf) = %{tl_version}
Provides:       tex(fctro7t.vf) = %{tl_version}, tex(fctro8c.vf) = %{tl_version}
Provides:       tex(fctro8t.vf) = %{tl_version}, tex(fctrogr.vf) = %{tl_version}
Provides:       tex(fctru6a.vf) = %{tl_version}, tex(fctru7k.vf) = %{tl_version}
Provides:       tex(fctru7t.vf) = %{tl_version}, tex(fctru8c.vf) = %{tl_version}
Provides:       tex(fctru8t.vf) = %{tl_version}, tex(fctrugr.vf) = %{tl_version}
Provides:       tex(antcmlgc.sty) = %{tl_version}, tex(cmlgc.sty) = %{tl_version}
Provides:       tex(lgrfcm.fd) = %{tl_version}, tex(lgrfcs.fd) = %{tl_version}
Provides:       tex(lgrfct.fd) = %{tl_version}, tex(ot1fcm.fd) = %{tl_version}
Provides:       tex(ot1fcs.fd) = %{tl_version}, tex(ot1fct.fd) = %{tl_version}
Provides:       tex(ot2fcm.fd) = %{tl_version}, tex(ot2fcs.fd) = %{tl_version}
Provides:       tex(ot2fct.fd) = %{tl_version}, tex(t1fcm.fd) = %{tl_version}
Provides:       tex(t1fcs.fd) = %{tl_version}, tex(t1fct.fd) = %{tl_version}
Provides:       tex(t2afcm.fd) = %{tl_version}, tex(t2afcs.fd) = %{tl_version}
Provides:       tex(t2afct.fd) = %{tl_version}, tex(ts1fcm.fd) = %{tl_version}
Provides:       tex(ts1fcs.fd) = %{tl_version}, tex(ts1fct.fd) = %{tl_version}
Provides:       tex(ut1fcm.fd) = %{tl_version}, tex(ut1fcs.fd) = %{tl_version}
Provides:       tex(ut1fct.fd) = %{tl_version}
Obsoletes:      tex-cm-lgc < %{tl_version}

%description -n texlive-cm-lgc
The fonts are converted from Metafont sources of the Computer
Modern font families, using textrace. Supported encodings are:
T1 (Latin), T2A (Cyrillic), LGR (Greek) and TS1. The package
also includes Unicode virtual fonts for use with Omega. The
font set is not a replacement for any of the other Computer
Modern-based font sets (for example, cm-super for Latin and
Cyrillic, or cbgreek for Greek), since it is available at a
single size only; it offers a compact set for 'general'
working. The fonts themselves are encoded to external
standards, and virtual fonts are provided for use with TeX.

%package -n texlive-cm-lgc-doc
Summary:        Documentation for cm-lgc
Version:        svn28250.0.5

Provides:       tex-cm-lgc-doc
AutoReqProv:    No

%description -n texlive-cm-lgc-doc
Documentation for cm-lgc

%package -n texlive-cmll
Provides:       tex-cmll = %{tl_version}
License:        LPPL
Summary:        Symbols for linear logic
Version:        svn17964.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifthen.sty), tex(graphicx.sty), tex(relsize.sty)
Provides:       tex(cmll.map) = %{tl_version}, tex(cmllbx10.tfm) = %{tl_version}
Provides:       tex(cmllbx12.tfm) = %{tl_version}, tex(cmllbx5.tfm) = %{tl_version}
Provides:       tex(cmllbx6.tfm) = %{tl_version}, tex(cmllbx7.tfm) = %{tl_version}
Provides:       tex(cmllbx8.tfm) = %{tl_version}, tex(cmllbx9.tfm) = %{tl_version}
Provides:       tex(cmllr10.tfm) = %{tl_version}, tex(cmllr12.tfm) = %{tl_version}
Provides:       tex(cmllr17.tfm) = %{tl_version}, tex(cmllr5.tfm) = %{tl_version}
Provides:       tex(cmllr6.tfm) = %{tl_version}, tex(cmllr7.tfm) = %{tl_version}
Provides:       tex(cmllr8.tfm) = %{tl_version}, tex(cmllr9.tfm) = %{tl_version}
Provides:       tex(cmllss10.tfm) = %{tl_version}, tex(cmllss12.tfm) = %{tl_version}
Provides:       tex(cmllss17.tfm) = %{tl_version}, tex(cmllss8.tfm) = %{tl_version}
Provides:       tex(cmllss9.tfm) = %{tl_version}, tex(cmllssbx10.tfm) = %{tl_version}
Provides:       tex(eullbx10.tfm) = %{tl_version}, tex(eullbx5.tfm) = %{tl_version}
Provides:       tex(eullbx6.tfm) = %{tl_version}, tex(eullbx7.tfm) = %{tl_version}
Provides:       tex(eullbx8.tfm) = %{tl_version}, tex(eullbx9.tfm) = %{tl_version}
Provides:       tex(eullr10.tfm) = %{tl_version}, tex(eullr5.tfm) = %{tl_version}
Provides:       tex(eullr6.tfm) = %{tl_version}, tex(eullr7.tfm) = %{tl_version}
Provides:       tex(eullr8.tfm) = %{tl_version}, tex(eullr9.tfm) = %{tl_version}
Provides:       tex(cmllbx10.pfb) = %{tl_version}, tex(cmllbx12.pfb) = %{tl_version}
Provides:       tex(cmllbx5.pfb) = %{tl_version}, tex(cmllbx6.pfb) = %{tl_version}
Provides:       tex(cmllbx7.pfb) = %{tl_version}, tex(cmllbx8.pfb) = %{tl_version}
Provides:       tex(cmllbx9.pfb) = %{tl_version}, tex(cmllr10.pfb) = %{tl_version}
Provides:       tex(cmllr12.pfb) = %{tl_version}, tex(cmllr17.pfb) = %{tl_version}
Provides:       tex(cmllr5.pfb) = %{tl_version}, tex(cmllr6.pfb) = %{tl_version}
Provides:       tex(cmllr7.pfb) = %{tl_version}, tex(cmllr8.pfb) = %{tl_version}
Provides:       tex(cmllr9.pfb) = %{tl_version}, tex(cmllss10.pfb) = %{tl_version}
Provides:       tex(cmllss12.pfb) = %{tl_version}, tex(cmllss17.pfb) = %{tl_version}
Provides:       tex(cmllss8.pfb) = %{tl_version}, tex(cmllss9.pfb) = %{tl_version}
Provides:       tex(cmllssbx10.pfb) = %{tl_version}, tex(eullbx10.pfb) = %{tl_version}
Provides:       tex(eullbx5.pfb) = %{tl_version}, tex(eullbx6.pfb) = %{tl_version}
Provides:       tex(eullbx7.pfb) = %{tl_version}, tex(eullbx8.pfb) = %{tl_version}
Provides:       tex(eullbx9.pfb) = %{tl_version}, tex(eullr10.pfb) = %{tl_version}
Provides:       tex(eullr5.pfb) = %{tl_version}, tex(eullr6.pfb) = %{tl_version}
Provides:       tex(eullr7.pfb) = %{tl_version}, tex(eullr8.pfb) = %{tl_version}
Provides:       tex(eullr9.pfb) = %{tl_version}, tex(cmll.sty) = %{tl_version}
Provides:       tex(ucmllr.fd) = %{tl_version}, tex(ucmllss.fd) = %{tl_version}
Provides:       tex(ueull.fd) = %{tl_version}

%description -n texlive-cmll
This is a very small font set that contain some symbols useful
in linear logic, which are apparently not available elsewhere.
Variants are included for use with Computer Modern serif and
sans-serif and with the AMS Euler series. The font is provided
both as Metafont source, and in Adobe Type 1 format. LaTeX
support is provided.

%package -n texlive-cmll-doc
Summary:        Documentation for cmll
Version:        svn17964.0

Provides:       tex-cmll-doc
AutoReqProv:    No

%description -n texlive-cmll-doc
Documentation for cmll

%package -n texlive-cmpica
Provides:       tex-cmpica = %{tl_version}
License:        Public Domain
Summary:        A Computer Modern Pica variant
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cmpica.tfm) = %{tl_version}, tex(cmpicab.tfm) = %{tl_version}
Provides:       tex(cmpicati.tfm) = %{tl_version}

%description -n texlive-cmpica
An approximate equivalent of the Xerox Pica typeface; the font
is optimised for submitting fiction manuscripts to mainline
publishers. The font is a fixed-width one, rather less heavy
than Computer Modern typewriter. Emphasis for bold-face comes
from a wavy underline of each letter. The two fonts are
supplied as Metafont source.

%package -n texlive-cmpica-doc
Summary:        Documentation for cmpica
Version:        svn15878.0

Provides:       tex-cmpica-doc
AutoReqProv:    No

%description -n texlive-cmpica-doc
Documentation for cmpica

%package -n texlive-cmpj
Provides:       tex-cmpj = %{tl_version}
License:        LPPL
Summary:        Style for the journal Condensed Matter Physics
Version:        svn44283
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fancyhdr.sty), tex(graphicx.sty), tex(natbib.sty), tex(ifthen.sty)
Requires:       tex(hyperref.sty), tex(doi.sty), tex(url.sty), tex(txfonts.sty)
Requires:       tex(fourier.sty), tex(droidserif.sty), tex(droidsans.sty), tex(droidmono.sty)
Provides:       tex(cmpj.sty) = %{tl_version}, tex(cmpj2.sty) = %{tl_version}

%description -n texlive-cmpj
The package contains macros and some documentation for
typesetting papers for submission to the Condensed Matter
Physics journal published by the Institute for Condensed Matter
Physics of the National Academy of Sciences of Ukraine.

%package -n texlive-cmpj-doc
Summary:        Documentation for cmpj
Version:        svn44283
Provides:       tex-cmpj-doc
AutoReqProv:    No

%description -n texlive-cmpj-doc
Documentation for cmpj

%package -n texlive-cmsd
Provides:       tex-cmsd = %{tl_version}
License:        LPPL
Summary:        Interfaces to the CM Sans Serif Bold fonts
Version:        svn18787.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cmsd.sty) = %{tl_version}, tex(t1cmsd.fd) = %{tl_version}
Provides:       tex(ts1cmsd.fd) = %{tl_version}

%description -n texlive-cmsd
Thr purpose of the package is to provide an alternative
interface to the CM Sans Serif boldface fonts. The EC (T1,
Cork) encoded versions of the 'CM Sans Serif boldface extended'
fonts differ considerably from the traditionally (OT1) encoded
ones: at large sizes, >10pt, they have thinner strokes and are
much wider. At 25pt they are hardly to be recognized as being
'boldface'. This package attempts to make these T1 fonts look
like the traditional ones did. You do not need any new fonts;
the package just changes the way LaTeX makes use of the current
ones.

%package -n texlive-cmsd-doc
Summary:        Documentation for cmsd
Version:        svn18787.0

Provides:       tex-cmsd-doc
AutoReqProv:    No

%description -n texlive-cmsd-doc
Documentation for cmsd

%package -n texlive-cm-super
Provides:       tex-cm-super = %{tl_version}
License:        GPL+
Summary:        CM-Super family of fonts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(t1cmr.fd)
Provides:       tex(cm-super-t1.enc) = %{tl_version}, tex(cm-super-t2a.enc) = %{tl_version}
Provides:       tex(cm-super-t2b.enc) = %{tl_version}, tex(cm-super-t2c.enc) = %{tl_version}
Provides:       tex(cm-super-ts1.enc) = %{tl_version}, tex(cm-super-x2.enc) = %{tl_version}
Provides:       tex(cm-super-t1.map) = %{tl_version}, tex(cm-super-t2a.map) = %{tl_version}
Provides:       tex(cm-super-t2b.map) = %{tl_version}, tex(cm-super-t2c.map) = %{tl_version}
Provides:       tex(cm-super-ts1.map) = %{tl_version}, tex(cm-super-x2.map) = %{tl_version}
Provides:       tex(isflb8.pfb) = %{tl_version}, tex(isfli8.pfb) = %{tl_version}
Provides:       tex(isflo8.pfb) = %{tl_version}, tex(isflq8.pfb) = %{tl_version}
Provides:       tex(isfltt8.pfb) = %{tl_version}, tex(sfbbx10.pfb) = %{tl_version}
Provides:       tex(sfbi0500.pfb) = %{tl_version}, tex(sfbi0600.pfb) = %{tl_version}
Provides:       tex(sfbi0700.pfb) = %{tl_version}, tex(sfbi0800.pfb) = %{tl_version}
Provides:       tex(sfbi0900.pfb) = %{tl_version}, tex(sfbi1000.pfb) = %{tl_version}
Provides:       tex(sfbi1095.pfb) = %{tl_version}, tex(sfbi1200.pfb) = %{tl_version}
Provides:       tex(sfbi1440.pfb) = %{tl_version}, tex(sfbi1728.pfb) = %{tl_version}
Provides:       tex(sfbi2074.pfb) = %{tl_version}, tex(sfbi2488.pfb) = %{tl_version}
Provides:       tex(sfbi2986.pfb) = %{tl_version}, tex(sfbi3583.pfb) = %{tl_version}
Provides:       tex(sfbl0500.pfb) = %{tl_version}, tex(sfbl0600.pfb) = %{tl_version}
Provides:       tex(sfbl0700.pfb) = %{tl_version}, tex(sfbl0800.pfb) = %{tl_version}
Provides:       tex(sfbl0900.pfb) = %{tl_version}, tex(sfbl1000.pfb) = %{tl_version}
Provides:       tex(sfbl1095.pfb) = %{tl_version}, tex(sfbl1200.pfb) = %{tl_version}
Provides:       tex(sfbl1440.pfb) = %{tl_version}, tex(sfbl1728.pfb) = %{tl_version}
Provides:       tex(sfbl2074.pfb) = %{tl_version}, tex(sfbl2488.pfb) = %{tl_version}
Provides:       tex(sfbl2986.pfb) = %{tl_version}, tex(sfbl3583.pfb) = %{tl_version}
Provides:       tex(sfbm0500.pfb) = %{tl_version}, tex(sfbm0700.pfb) = %{tl_version}
Provides:       tex(sfbm0900.pfb) = %{tl_version}, tex(sfbm1000.pfb) = %{tl_version}
Provides:       tex(sfbm1095.pfb) = %{tl_version}, tex(sfbm1200.pfb) = %{tl_version}
Provides:       tex(sfbm1440.pfb) = %{tl_version}, tex(sfbm1728.pfb) = %{tl_version}
Provides:       tex(sfbm2074.pfb) = %{tl_version}, tex(sfbm2488.pfb) = %{tl_version}
Provides:       tex(sfbm2986.pfb) = %{tl_version}, tex(sfbm3583.pfb) = %{tl_version}
Provides:       tex(sfbmo10.pfb) = %{tl_version}, tex(sfbmo17.pfb) = %{tl_version}
Provides:       tex(sfbmo8.pfb) = %{tl_version}, tex(sfbmo9.pfb) = %{tl_version}
Provides:       tex(sfbmr10.pfb) = %{tl_version}, tex(sfbmr17.pfb) = %{tl_version}
Provides:       tex(sfbmr8.pfb) = %{tl_version}, tex(sfbmr9.pfb) = %{tl_version}
Provides:       tex(sfbso10.pfb) = %{tl_version}, tex(sfbso17.pfb) = %{tl_version}
Provides:       tex(sfbso8.pfb) = %{tl_version}, tex(sfbso9.pfb) = %{tl_version}
Provides:       tex(sfbsr10.pfb) = %{tl_version}, tex(sfbsr17.pfb) = %{tl_version}
Provides:       tex(sfbsr8.pfb) = %{tl_version}, tex(sfbsr9.pfb) = %{tl_version}
Provides:       tex(sfbtl10.pfb) = %{tl_version}, tex(sfbto10.pfb) = %{tl_version}
Provides:       tex(sfbx0500.pfb) = %{tl_version}, tex(sfbx0600.pfb) = %{tl_version}
Provides:       tex(sfbx0700.pfb) = %{tl_version}, tex(sfbx0800.pfb) = %{tl_version}
Provides:       tex(sfbx0900.pfb) = %{tl_version}, tex(sfbx1000.pfb) = %{tl_version}
Provides:       tex(sfbx1095.pfb) = %{tl_version}, tex(sfbx1200.pfb) = %{tl_version}
Provides:       tex(sfbx1440.pfb) = %{tl_version}, tex(sfbx1728.pfb) = %{tl_version}
Provides:       tex(sfbx2074.pfb) = %{tl_version}, tex(sfbx2488.pfb) = %{tl_version}
Provides:       tex(sfbx2986.pfb) = %{tl_version}, tex(sfbx3583.pfb) = %{tl_version}
Provides:       tex(sfcc0500.pfb) = %{tl_version}, tex(sfcc0600.pfb) = %{tl_version}
Provides:       tex(sfcc0700.pfb) = %{tl_version}, tex(sfcc0800.pfb) = %{tl_version}
Provides:       tex(sfcc0900.pfb) = %{tl_version}, tex(sfcc1000.pfb) = %{tl_version}
Provides:       tex(sfcc1095.pfb) = %{tl_version}, tex(sfcc1200.pfb) = %{tl_version}
Provides:       tex(sfcc1440.pfb) = %{tl_version}, tex(sfcc1728.pfb) = %{tl_version}
Provides:       tex(sfcc2074.pfb) = %{tl_version}, tex(sfcc2488.pfb) = %{tl_version}
Provides:       tex(sfcc2986.pfb) = %{tl_version}, tex(sfcc3583.pfb) = %{tl_version}
Provides:       tex(sfci0500.pfb) = %{tl_version}, tex(sfci0600.pfb) = %{tl_version}
Provides:       tex(sfci0700.pfb) = %{tl_version}, tex(sfci0800.pfb) = %{tl_version}
Provides:       tex(sfci0900.pfb) = %{tl_version}, tex(sfci1000.pfb) = %{tl_version}
Provides:       tex(sfci1095.pfb) = %{tl_version}, tex(sfci1200.pfb) = %{tl_version}
Provides:       tex(sfci1440.pfb) = %{tl_version}, tex(sfci1728.pfb) = %{tl_version}
Provides:       tex(sfci2074.pfb) = %{tl_version}, tex(sfci2488.pfb) = %{tl_version}
Provides:       tex(sfci2986.pfb) = %{tl_version}, tex(sfci3583.pfb) = %{tl_version}
Provides:       tex(sfdh0500.pfb) = %{tl_version}, tex(sfdh0600.pfb) = %{tl_version}
Provides:       tex(sfdh0700.pfb) = %{tl_version}, tex(sfdh0800.pfb) = %{tl_version}
Provides:       tex(sfdh0900.pfb) = %{tl_version}, tex(sfdh1000.pfb) = %{tl_version}
Provides:       tex(sfdh1095.pfb) = %{tl_version}, tex(sfdh1200.pfb) = %{tl_version}
Provides:       tex(sfdh1440.pfb) = %{tl_version}, tex(sfdh1728.pfb) = %{tl_version}
Provides:       tex(sfdh2074.pfb) = %{tl_version}, tex(sfdh2488.pfb) = %{tl_version}
Provides:       tex(sfdh2986.pfb) = %{tl_version}, tex(sfdh3583.pfb) = %{tl_version}
Provides:       tex(sffb0500.pfb) = %{tl_version}, tex(sffb0600.pfb) = %{tl_version}
Provides:       tex(sffb0700.pfb) = %{tl_version}, tex(sffb0800.pfb) = %{tl_version}
Provides:       tex(sffb0900.pfb) = %{tl_version}, tex(sffb1000.pfb) = %{tl_version}
Provides:       tex(sffb1095.pfb) = %{tl_version}, tex(sffb1200.pfb) = %{tl_version}
Provides:       tex(sffb1440.pfb) = %{tl_version}, tex(sffb1728.pfb) = %{tl_version}
Provides:       tex(sffb2074.pfb) = %{tl_version}, tex(sfff0900.pfb) = %{tl_version}
Provides:       tex(sfff1000.pfb) = %{tl_version}, tex(sfff1095.pfb) = %{tl_version}
Provides:       tex(sfff1200.pfb) = %{tl_version}, tex(sfff1440.pfb) = %{tl_version}
Provides:       tex(sfff2488.pfb) = %{tl_version}, tex(sffi0900.pfb) = %{tl_version}
Provides:       tex(sffi1000.pfb) = %{tl_version}, tex(sffi1095.pfb) = %{tl_version}
Provides:       tex(sffi1200.pfb) = %{tl_version}, tex(sffi1440.pfb) = %{tl_version}
Provides:       tex(sffi1728.pfb) = %{tl_version}, tex(sffi2074.pfb) = %{tl_version}
Provides:       tex(sffs0500.pfb) = %{tl_version}, tex(sffs0600.pfb) = %{tl_version}
Provides:       tex(sffs0700.pfb) = %{tl_version}, tex(sffs0800.pfb) = %{tl_version}
Provides:       tex(sffs0900.pfb) = %{tl_version}, tex(sffs1000.pfb) = %{tl_version}
Provides:       tex(sffs1095.pfb) = %{tl_version}, tex(sffs1200.pfb) = %{tl_version}
Provides:       tex(sffs1440.pfb) = %{tl_version}, tex(sffs1728.pfb) = %{tl_version}
Provides:       tex(sffs2074.pfb) = %{tl_version}, tex(sfit0800.pfb) = %{tl_version}
Provides:       tex(sfit0900.pfb) = %{tl_version}, tex(sfit1000.pfb) = %{tl_version}
Provides:       tex(sfit1095.pfb) = %{tl_version}, tex(sfit1200.pfb) = %{tl_version}
Provides:       tex(sfit1440.pfb) = %{tl_version}, tex(sfit1728.pfb) = %{tl_version}
Provides:       tex(sfit2074.pfb) = %{tl_version}, tex(sfit2488.pfb) = %{tl_version}
Provides:       tex(sflb8.pfb) = %{tl_version}, tex(sfli8.pfb) = %{tl_version}
Provides:       tex(sflo8.pfb) = %{tl_version}, tex(sflq8.pfb) = %{tl_version}
Provides:       tex(sfltt8.pfb) = %{tl_version}, tex(sfoc0500.pfb) = %{tl_version}
Provides:       tex(sfoc0600.pfb) = %{tl_version}, tex(sfoc0700.pfb) = %{tl_version}
Provides:       tex(sfoc0800.pfb) = %{tl_version}, tex(sfoc0900.pfb) = %{tl_version}
Provides:       tex(sfoc1000.pfb) = %{tl_version}, tex(sfoc1095.pfb) = %{tl_version}
Provides:       tex(sfoc1200.pfb) = %{tl_version}, tex(sfoc1440.pfb) = %{tl_version}
Provides:       tex(sfoc1728.pfb) = %{tl_version}, tex(sfoc2074.pfb) = %{tl_version}
Provides:       tex(sfoc2488.pfb) = %{tl_version}, tex(sfoc2986.pfb) = %{tl_version}
Provides:       tex(sfoc3583.pfb) = %{tl_version}, tex(sfocc10.pfb) = %{tl_version}
Provides:       tex(sform10.pfb) = %{tl_version}, tex(sform5.pfb) = %{tl_version}
Provides:       tex(sform6.pfb) = %{tl_version}, tex(sform7.pfb) = %{tl_version}
Provides:       tex(sform8.pfb) = %{tl_version}, tex(sform9.pfb) = %{tl_version}
Provides:       tex(sfosl10.pfb) = %{tl_version}, tex(sfosl5.pfb) = %{tl_version}
Provides:       tex(sfosl6.pfb) = %{tl_version}, tex(sfosl7.pfb) = %{tl_version}
Provides:       tex(sfosl8.pfb) = %{tl_version}, tex(sfosl9.pfb) = %{tl_version}
Provides:       tex(sfoti10.pfb) = %{tl_version}, tex(sfqi8.pfb) = %{tl_version}
Provides:       tex(sfrb0500.pfb) = %{tl_version}, tex(sfrb0600.pfb) = %{tl_version}
Provides:       tex(sfrb0700.pfb) = %{tl_version}, tex(sfrb0800.pfb) = %{tl_version}
Provides:       tex(sfrb0900.pfb) = %{tl_version}, tex(sfrb1000.pfb) = %{tl_version}
Provides:       tex(sfrb1095.pfb) = %{tl_version}, tex(sfrb1200.pfb) = %{tl_version}
Provides:       tex(sfrb1440.pfb) = %{tl_version}, tex(sfrb1728.pfb) = %{tl_version}
Provides:       tex(sfrb2074.pfb) = %{tl_version}, tex(sfrb2488.pfb) = %{tl_version}
Provides:       tex(sfrb2986.pfb) = %{tl_version}, tex(sfrb3583.pfb) = %{tl_version}
Provides:       tex(sfrm0500.pfb) = %{tl_version}, tex(sfrm0600.pfb) = %{tl_version}
Provides:       tex(sfrm0700.pfb) = %{tl_version}, tex(sfrm0800.pfb) = %{tl_version}
Provides:       tex(sfrm0900.pfb) = %{tl_version}, tex(sfrm1000.pfb) = %{tl_version}
Provides:       tex(sfrm1095.pfb) = %{tl_version}, tex(sfrm1200.pfb) = %{tl_version}
Provides:       tex(sfrm1440.pfb) = %{tl_version}, tex(sfrm1728.pfb) = %{tl_version}
Provides:       tex(sfrm2074.pfb) = %{tl_version}, tex(sfrm2488.pfb) = %{tl_version}
Provides:       tex(sfrm2986.pfb) = %{tl_version}, tex(sfrm3583.pfb) = %{tl_version}
Provides:       tex(sfsc0500.pfb) = %{tl_version}, tex(sfsc0600.pfb) = %{tl_version}
Provides:       tex(sfsc0700.pfb) = %{tl_version}, tex(sfsc0800.pfb) = %{tl_version}
Provides:       tex(sfsc0900.pfb) = %{tl_version}, tex(sfsc1000.pfb) = %{tl_version}
Provides:       tex(sfsc1095.pfb) = %{tl_version}, tex(sfsc1200.pfb) = %{tl_version}
Provides:       tex(sfsc1440.pfb) = %{tl_version}, tex(sfsc1728.pfb) = %{tl_version}
Provides:       tex(sfsc2074.pfb) = %{tl_version}, tex(sfsc2488.pfb) = %{tl_version}
Provides:       tex(sfsc2986.pfb) = %{tl_version}, tex(sfsc3583.pfb) = %{tl_version}
Provides:       tex(sfsi0500.pfb) = %{tl_version}, tex(sfsi0600.pfb) = %{tl_version}
Provides:       tex(sfsi0700.pfb) = %{tl_version}, tex(sfsi0800.pfb) = %{tl_version}
Provides:       tex(sfsi0900.pfb) = %{tl_version}, tex(sfsi1000.pfb) = %{tl_version}
Provides:       tex(sfsi1095.pfb) = %{tl_version}, tex(sfsi1200.pfb) = %{tl_version}
Provides:       tex(sfsi1440.pfb) = %{tl_version}, tex(sfsi1728.pfb) = %{tl_version}
Provides:       tex(sfsi2074.pfb) = %{tl_version}, tex(sfsi2488.pfb) = %{tl_version}
Provides:       tex(sfsi2986.pfb) = %{tl_version}, tex(sfsi3583.pfb) = %{tl_version}
Provides:       tex(sfsl0500.pfb) = %{tl_version}, tex(sfsl0600.pfb) = %{tl_version}
Provides:       tex(sfsl0700.pfb) = %{tl_version}, tex(sfsl0800.pfb) = %{tl_version}
Provides:       tex(sfsl0900.pfb) = %{tl_version}, tex(sfsl1000.pfb) = %{tl_version}
Provides:       tex(sfsl1095.pfb) = %{tl_version}, tex(sfsl1200.pfb) = %{tl_version}
Provides:       tex(sfsl1440.pfb) = %{tl_version}, tex(sfsl1728.pfb) = %{tl_version}
Provides:       tex(sfsl2074.pfb) = %{tl_version}, tex(sfsl2488.pfb) = %{tl_version}
Provides:       tex(sfsl2986.pfb) = %{tl_version}, tex(sfsl3583.pfb) = %{tl_version}
Provides:       tex(sfso0500.pfb) = %{tl_version}, tex(sfso0600.pfb) = %{tl_version}
Provides:       tex(sfso0700.pfb) = %{tl_version}, tex(sfso0800.pfb) = %{tl_version}
Provides:       tex(sfso0900.pfb) = %{tl_version}, tex(sfso1000.pfb) = %{tl_version}
Provides:       tex(sfso1095.pfb) = %{tl_version}, tex(sfso1200.pfb) = %{tl_version}
Provides:       tex(sfso1440.pfb) = %{tl_version}, tex(sfso1728.pfb) = %{tl_version}
Provides:       tex(sfso2074.pfb) = %{tl_version}, tex(sfso2488.pfb) = %{tl_version}
Provides:       tex(sfso2986.pfb) = %{tl_version}, tex(sfso3583.pfb) = %{tl_version}
Provides:       tex(sfsq8.pfb) = %{tl_version}, tex(sfss0500.pfb) = %{tl_version}
Provides:       tex(sfss0600.pfb) = %{tl_version}, tex(sfss0700.pfb) = %{tl_version}
Provides:       tex(sfss0800.pfb) = %{tl_version}, tex(sfss0900.pfb) = %{tl_version}
Provides:       tex(sfss1000.pfb) = %{tl_version}, tex(sfss1095.pfb) = %{tl_version}
Provides:       tex(sfss1200.pfb) = %{tl_version}, tex(sfss1440.pfb) = %{tl_version}
Provides:       tex(sfss1728.pfb) = %{tl_version}, tex(sfss2074.pfb) = %{tl_version}
Provides:       tex(sfss2488.pfb) = %{tl_version}, tex(sfss2986.pfb) = %{tl_version}
Provides:       tex(sfss3583.pfb) = %{tl_version}, tex(sfssdc10.pfb) = %{tl_version}
Provides:       tex(sfst0800.pfb) = %{tl_version}, tex(sfst0900.pfb) = %{tl_version}
Provides:       tex(sfst1000.pfb) = %{tl_version}, tex(sfst1095.pfb) = %{tl_version}
Provides:       tex(sfst1200.pfb) = %{tl_version}, tex(sfst1440.pfb) = %{tl_version}
Provides:       tex(sfst1728.pfb) = %{tl_version}, tex(sfst2074.pfb) = %{tl_version}
Provides:       tex(sfst2488.pfb) = %{tl_version}, tex(sfst2986.pfb) = %{tl_version}
Provides:       tex(sfst3583.pfb) = %{tl_version}, tex(sfsx0500.pfb) = %{tl_version}
Provides:       tex(sfsx0600.pfb) = %{tl_version}, tex(sfsx0700.pfb) = %{tl_version}
Provides:       tex(sfsx0800.pfb) = %{tl_version}, tex(sfsx0900.pfb) = %{tl_version}
Provides:       tex(sfsx1000.pfb) = %{tl_version}, tex(sfsx1095.pfb) = %{tl_version}
Provides:       tex(sfsx1200.pfb) = %{tl_version}, tex(sfsx1440.pfb) = %{tl_version}
Provides:       tex(sfsx1728.pfb) = %{tl_version}, tex(sfsx2074.pfb) = %{tl_version}
Provides:       tex(sfsx2488.pfb) = %{tl_version}, tex(sfsx2986.pfb) = %{tl_version}
Provides:       tex(sfsx3583.pfb) = %{tl_version}, tex(sftc0800.pfb) = %{tl_version}
Provides:       tex(sftc0900.pfb) = %{tl_version}, tex(sftc1000.pfb) = %{tl_version}
Provides:       tex(sftc1095.pfb) = %{tl_version}, tex(sftc1200.pfb) = %{tl_version}
Provides:       tex(sftc1440.pfb) = %{tl_version}, tex(sftc1728.pfb) = %{tl_version}
Provides:       tex(sftc2074.pfb) = %{tl_version}, tex(sftc2488.pfb) = %{tl_version}
Provides:       tex(sftc2986.pfb) = %{tl_version}, tex(sftc3583.pfb) = %{tl_version}
Provides:       tex(sfti0500.pfb) = %{tl_version}, tex(sfti0600.pfb) = %{tl_version}
Provides:       tex(sfti0700.pfb) = %{tl_version}, tex(sfti0800.pfb) = %{tl_version}
Provides:       tex(sfti0900.pfb) = %{tl_version}, tex(sfti1000.pfb) = %{tl_version}
Provides:       tex(sfti1095.pfb) = %{tl_version}, tex(sfti1200.pfb) = %{tl_version}
Provides:       tex(sfti1440.pfb) = %{tl_version}, tex(sfti1728.pfb) = %{tl_version}
Provides:       tex(sfti2074.pfb) = %{tl_version}, tex(sfti2488.pfb) = %{tl_version}
Provides:       tex(sfti2986.pfb) = %{tl_version}, tex(sfti3583.pfb) = %{tl_version}
Provides:       tex(sftt0800.pfb) = %{tl_version}, tex(sftt0900.pfb) = %{tl_version}
Provides:       tex(sftt1000.pfb) = %{tl_version}, tex(sftt1095.pfb) = %{tl_version}
Provides:       tex(sftt1200.pfb) = %{tl_version}, tex(sftt1440.pfb) = %{tl_version}
Provides:       tex(sftt1728.pfb) = %{tl_version}, tex(sftt2074.pfb) = %{tl_version}
Provides:       tex(sftt2488.pfb) = %{tl_version}, tex(sftt2986.pfb) = %{tl_version}
Provides:       tex(sftt3583.pfb) = %{tl_version}, tex(sfui0500.pfb) = %{tl_version}
Provides:       tex(sfui0600.pfb) = %{tl_version}, tex(sfui0700.pfb) = %{tl_version}
Provides:       tex(sfui0800.pfb) = %{tl_version}, tex(sfui0900.pfb) = %{tl_version}
Provides:       tex(sfui1000.pfb) = %{tl_version}, tex(sfui1095.pfb) = %{tl_version}
Provides:       tex(sfui1200.pfb) = %{tl_version}, tex(sfui1440.pfb) = %{tl_version}
Provides:       tex(sfui1728.pfb) = %{tl_version}, tex(sfui2074.pfb) = %{tl_version}
Provides:       tex(sfui2488.pfb) = %{tl_version}, tex(sfui2986.pfb) = %{tl_version}
Provides:       tex(sfui3583.pfb) = %{tl_version}, tex(sfvi0800.pfb) = %{tl_version}
Provides:       tex(sfvi0900.pfb) = %{tl_version}, tex(sfvi1000.pfb) = %{tl_version}
Provides:       tex(sfvi1095.pfb) = %{tl_version}, tex(sfvi1200.pfb) = %{tl_version}
Provides:       tex(sfvi1440.pfb) = %{tl_version}, tex(sfvi1728.pfb) = %{tl_version}
Provides:       tex(sfvi2074.pfb) = %{tl_version}, tex(sfvi2488.pfb) = %{tl_version}
Provides:       tex(sfvi2986.pfb) = %{tl_version}, tex(sfvi3583.pfb) = %{tl_version}
Provides:       tex(sfvt0800.pfb) = %{tl_version}, tex(sfvt0900.pfb) = %{tl_version}
Provides:       tex(sfvt1000.pfb) = %{tl_version}, tex(sfvt1095.pfb) = %{tl_version}
Provides:       tex(sfvt1200.pfb) = %{tl_version}, tex(sfvt1440.pfb) = %{tl_version}
Provides:       tex(sfvt1728.pfb) = %{tl_version}, tex(sfvt2074.pfb) = %{tl_version}
Provides:       tex(sfvt2488.pfb) = %{tl_version}, tex(sfvt2986.pfb) = %{tl_version}
Provides:       tex(sfvt3583.pfb) = %{tl_version}, tex(sfxc0500.pfb) = %{tl_version}
Provides:       tex(sfxc0600.pfb) = %{tl_version}, tex(sfxc0700.pfb) = %{tl_version}
Provides:       tex(sfxc0800.pfb) = %{tl_version}, tex(sfxc0900.pfb) = %{tl_version}
Provides:       tex(sfxc1000.pfb) = %{tl_version}, tex(sfxc1095.pfb) = %{tl_version}
Provides:       tex(sfxc1200.pfb) = %{tl_version}, tex(sfxc1440.pfb) = %{tl_version}
Provides:       tex(sfxc1728.pfb) = %{tl_version}, tex(sfxc2074.pfb) = %{tl_version}
Provides:       tex(sfxc2488.pfb) = %{tl_version}, tex(sfxc2986.pfb) = %{tl_version}
Provides:       tex(sfxc3583.pfb) = %{tl_version}, tex(type1ec.sty) = %{tl_version}

%description -n texlive-cm-super
The CM-Super family provides Adobe Type 1 fonts that replace
the T1/TS1-encoded Computer Modern (EC/TC), T1/TS1-encoded
Concrete, T1/TS1-encoded CM bright and LH Cyrillic fonts (thus
supporting all European languages except Greek), and bringing
many ameliorations in typesetting quality. The fonts exhibit
the same metrics as the Metafont-encoded originals.

%package -n texlive-cm-super-doc
Summary:        Documentation for cm-super
Version:        svn15878.0

Provides:       tex-cm-super-doc
AutoReqProv:    No

%description -n texlive-cm-super-doc
Documentation for cm-super

%package -n texlive-cmtiup
Provides:       tex-cmtiup = %{tl_version}
License:        LPPL 1.3
Summary:        Upright punctuation with CM italic
Version:        svn39728

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cmtiup10.tfm) = %{tl_version}, tex(cmtiup12.tfm) = %{tl_version}
Provides:       tex(cmtiup7.tfm) = %{tl_version}, tex(cmtiup8.tfm) = %{tl_version}
Provides:       tex(cmtiup9.tfm) = %{tl_version}, tex(cmtiup10.vf) = %{tl_version}
Provides:       tex(cmtiup12.vf) = %{tl_version}, tex(cmtiup7.vf) = %{tl_version}
Provides:       tex(cmtiup8.vf) = %{tl_version}, tex(cmtiup9.vf) = %{tl_version}
Provides:       tex(cmtiup.sty) = %{tl_version}

%description -n texlive-cmtiup
The cmtiup fonts address a problem with the appearance of
punctuation in italic text in mathematical documents. To
achieve this, all punctuation characters are upright, and
kerning between letters and punctuation is adjusted to allow
for the italic correction. The fonts are implemented as a set
of vf files; a package for support in LaTeX 2e is provided.

%package -n texlive-cmtiup-doc
Summary:        Documentation for cmtiup
Version:        svn39728

Provides:       tex-cmtiup-doc
AutoReqProv:    No

%description -n texlive-cmtiup-doc
Documentation for cmtiup

%package -n texlive-cm
Provides:       tex-cm = %{tl_version}
License:        Knuth
Summary:        Computer Modern fonts
Version:        svn45811
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex
Provides:       tex(cmtext-bsr-interpolated.map) = %{tl_version}
Provides:       tex(cmb10.tfm) = %{tl_version}, tex(cmbcsc10.tfm) = %{tl_version}
Provides:       tex(cmbsy10.tfm) = %{tl_version}, tex(cmbx10.tfm) = %{tl_version}
Provides:       tex(cmbx12.tfm) = %{tl_version}, tex(cmbx5.tfm) = %{tl_version}
Provides:       tex(cmbx6.tfm) = %{tl_version}, tex(cmbx7.tfm) = %{tl_version}
Provides:       tex(cmbx8.tfm) = %{tl_version}, tex(cmbx9.tfm) = %{tl_version}
Provides:       tex(cmbxsl10.tfm) = %{tl_version}, tex(cmbxti10.tfm) = %{tl_version}
Provides:       tex(cmcsc10.tfm) = %{tl_version}, tex(cmdunh10.tfm) = %{tl_version}
Provides:       tex(cmex10.tfm) = %{tl_version}, tex(cmff10.tfm) = %{tl_version}
Provides:       tex(cmfi10.tfm) = %{tl_version}, tex(cmfib8.tfm) = %{tl_version}
Provides:       tex(cminch.tfm) = %{tl_version}, tex(cmitt10.tfm) = %{tl_version}
Provides:       tex(cmmi10.tfm) = %{tl_version}, tex(cmmi12.tfm) = %{tl_version}
Provides:       tex(cmmi5.tfm) = %{tl_version}, tex(cmmi6.tfm) = %{tl_version}
Provides:       tex(cmmi7.tfm) = %{tl_version}, tex(cmmi8.tfm) = %{tl_version}
Provides:       tex(cmmi9.tfm) = %{tl_version}, tex(cmmib10.tfm) = %{tl_version}
Provides:       tex(cmr10.tfm) = %{tl_version}, tex(cmr12.tfm) = %{tl_version}
Provides:       tex(cmr17.tfm) = %{tl_version}, tex(cmr5.tfm) = %{tl_version}
Provides:       tex(cmr6.tfm) = %{tl_version}, tex(cmr7.tfm) = %{tl_version}
Provides:       tex(cmr8.tfm) = %{tl_version}, tex(cmr9.tfm) = %{tl_version}
Provides:       tex(cmsl10.tfm) = %{tl_version}, tex(cmsl12.tfm) = %{tl_version}
Provides:       tex(cmsl8.tfm) = %{tl_version}, tex(cmsl9.tfm) = %{tl_version}
Provides:       tex(cmsltt10.tfm) = %{tl_version}, tex(cmss10.tfm) = %{tl_version}
Provides:       tex(cmss12.tfm) = %{tl_version}, tex(cmss17.tfm) = %{tl_version}
Provides:       tex(cmss8.tfm) = %{tl_version}, tex(cmss9.tfm) = %{tl_version}
Provides:       tex(cmssbx10.tfm) = %{tl_version}, tex(cmssdc10.tfm) = %{tl_version}
Provides:       tex(cmssi10.tfm) = %{tl_version}, tex(cmssi12.tfm) = %{tl_version}
Provides:       tex(cmssi17.tfm) = %{tl_version}, tex(cmssi8.tfm) = %{tl_version}
Provides:       tex(cmssi9.tfm) = %{tl_version}, tex(cmssq8.tfm) = %{tl_version}
Provides:       tex(cmssqi8.tfm) = %{tl_version}, tex(cmsy10.tfm) = %{tl_version}
Provides:       tex(cmsy5.tfm) = %{tl_version}, tex(cmsy6.tfm) = %{tl_version}
Provides:       tex(cmsy7.tfm) = %{tl_version}, tex(cmsy8.tfm) = %{tl_version}
Provides:       tex(cmsy9.tfm) = %{tl_version}, tex(cmtcsc10.tfm) = %{tl_version}
Provides:       tex(cmtex10.tfm) = %{tl_version}, tex(cmtex8.tfm) = %{tl_version}
Provides:       tex(cmtex9.tfm) = %{tl_version}, tex(cmti10.tfm) = %{tl_version}
Provides:       tex(cmti12.tfm) = %{tl_version}, tex(cmti7.tfm) = %{tl_version}
Provides:       tex(cmti8.tfm) = %{tl_version}, tex(cmti9.tfm) = %{tl_version}
Provides:       tex(cmtt10.tfm) = %{tl_version}, tex(cmtt12.tfm) = %{tl_version}
Provides:       tex(cmtt8.tfm) = %{tl_version}, tex(cmtt9.tfm) = %{tl_version}
Provides:       tex(cmu10.tfm) = %{tl_version}, tex(cmvtt10.tfm) = %{tl_version}

%description -n texlive-cm
Knuth's final iteration of his re-interpretation of a c.19
Modern-style font from Monotype. The family is comprehensive,
offering both sans and roman styles, and a monospaced font,
together with mathematics fonts closely integrated with the
mathematical facilities of TeX itself. The base fonts are
distributed as Metafont source, but autotraced PostScript Type
1 versions are available (one version in the AMS fonts
distribution, and also the BaKoMa distribution). The Computer
Modern fonts have inspired many later families, notably the
European Computer Modern and the Latin Modern families.

%package -n texlive-cm-doc
Summary:        Documentation for cm
Version:        svn45811
Provides:       tex-cm-doc
AutoReqProv:    No

%description -n texlive-cm-doc
Documentation for cm

%package -n texlive-cm-unicode
Provides:       tex-cm-unicode = %{tl_version}
License:        OFL
Summary:        Computer Modern Unicode font family
Version:        svn19445.0.7.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cmu-ec.enc) = %{tl_version}, tex(cmu-ecsc.enc) = %{tl_version}
Provides:       tex(cmu-g.enc) = %{tl_version}, tex(cmu-gsc.enc) = %{tl_version}
Provides:       tex(cmu-la.enc) = %{tl_version}, tex(cmu-lasc.enc) = %{tl_version}
Provides:       tex(cmu-lb.enc) = %{tl_version}, tex(cmu-lc.enc) = %{tl_version}
Provides:       tex(cmu-ld.enc) = %{tl_version}, tex(cmu-rx.enc) = %{tl_version}
Provides:       tex(cmu-tc.enc) = %{tl_version}, tex(cmu-tipa.enc) = %{tl_version}
Provides:       tex(cmu-tipx.enc) = %{tl_version}, tex(cmu-ux.enc) = %{tl_version}
Provides:       tex(cmu-uxsc.enc) = %{tl_version}, tex(cmu-vn.enc) = %{tl_version}
Provides:       tex(cmu.map) = %{tl_version}, tex(cmunbbx.otf) = %{tl_version}
Provides:       tex(cmunbi.otf) = %{tl_version}, tex(cmunbl.otf) = %{tl_version}
Provides:       tex(cmunbmo.otf) = %{tl_version}, tex(cmunbmr.otf) = %{tl_version}
Provides:       tex(cmunbso.otf) = %{tl_version}, tex(cmunbsr.otf) = %{tl_version}
Provides:       tex(cmunbtl.otf) = %{tl_version}, tex(cmunbto.otf) = %{tl_version}
Provides:       tex(cmunbx.otf) = %{tl_version}, tex(cmunbxo.otf) = %{tl_version}
Provides:       tex(cmunci.otf) = %{tl_version}, tex(cmunit.otf) = %{tl_version}
Provides:       tex(cmunobi.otf) = %{tl_version}, tex(cmunobx.otf) = %{tl_version}
Provides:       tex(cmunorm.otf) = %{tl_version}, tex(cmunoti.otf) = %{tl_version}
Provides:       tex(cmunrb.otf) = %{tl_version}, tex(cmunrm.otf) = %{tl_version}
Provides:       tex(cmunsi.otf) = %{tl_version}, tex(cmunsl.otf) = %{tl_version}
Provides:       tex(cmunso.otf) = %{tl_version}, tex(cmunss.otf) = %{tl_version}
Provides:       tex(cmunssdc.otf) = %{tl_version}, tex(cmunst.otf) = %{tl_version}
Provides:       tex(cmunsx.otf) = %{tl_version}, tex(cmuntb.otf) = %{tl_version}
Provides:       tex(cmunti.otf) = %{tl_version}, tex(cmuntt.otf) = %{tl_version}
Provides:       tex(cmuntx.otf) = %{tl_version}, tex(cmunui.otf) = %{tl_version}
Provides:       tex(cmunvi.otf) = %{tl_version}, tex(cmunvt.otf) = %{tl_version}
Provides:       tex(cmunbbx.pfb) = %{tl_version}, tex(cmunbi.pfb) = %{tl_version}
Provides:       tex(cmunbl.pfb) = %{tl_version}, tex(cmunbmo.pfb) = %{tl_version}
Provides:       tex(cmunbmr.pfb) = %{tl_version}, tex(cmunbso.pfb) = %{tl_version}
Provides:       tex(cmunbsr.pfb) = %{tl_version}, tex(cmunbtl.pfb) = %{tl_version}
Provides:       tex(cmunbto.pfb) = %{tl_version}, tex(cmunbx.pfb) = %{tl_version}
Provides:       tex(cmunbxo.pfb) = %{tl_version}, tex(cmunci.pfb) = %{tl_version}
Provides:       tex(cmunit.pfb) = %{tl_version}, tex(cmunobi.pfb) = %{tl_version}
Provides:       tex(cmunobx.pfb) = %{tl_version}, tex(cmunorm.pfb) = %{tl_version}
Provides:       tex(cmunoti.pfb) = %{tl_version}, tex(cmunrb.pfb) = %{tl_version}
Provides:       tex(cmunrm.pfb) = %{tl_version}, tex(cmunsi.pfb) = %{tl_version}
Provides:       tex(cmunsl.pfb) = %{tl_version}, tex(cmunso.pfb) = %{tl_version}
Provides:       tex(cmunss.pfb) = %{tl_version}, tex(cmunssdc.pfb) = %{tl_version}
Provides:       tex(cmunst.pfb) = %{tl_version}, tex(cmunsx.pfb) = %{tl_version}
Provides:       tex(cmuntb.pfb) = %{tl_version}, tex(cmunti.pfb) = %{tl_version}
Provides:       tex(cmuntt.pfb) = %{tl_version}, tex(cmuntx.pfb) = %{tl_version}
Provides:       tex(cmunui.pfb) = %{tl_version}, tex(cmunvi.pfb) = %{tl_version}
Provides:       tex(cmunvt.pfb) = %{tl_version}

%description -n texlive-cm-unicode
Computer Modern Unicode fonts, converted from Metafont sources
using mftrace with autotrace backend and fontforge. Some
characters in several fonts are copied from Blue Sky type 1
fonts released by AMS. Currently the fonts contain glyphs from
Latin (Metafont ec, tc, vnr), Cyrillic (lh), Greek (cbgreek
when available) code sets and IPA extensions (from tipa). This
font set contains 33 fonts. This archive contains AFM, PFB and
OTF versions; the OTF version of the Computer Modern Unicode
fonts works with TeX engines that directly support OpenType
features, such as XeTeX and LuaTeX.

%package -n texlive-cm-unicode-doc
Summary:        Documentation for cm-unicode
Version:        svn19445.0.7.0

Provides:       tex-cm-unicode-doc
AutoReqProv:    No

%description -n texlive-cm-unicode-doc
Documentation for cm-unicode

%package -n texlive-cnbwp
Provides:       tex-cnbwp = %{tl_version}
License:        LPPL
Summary:        Typeset working papers of the Czech National Bank
Version:        svn32550.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(url.sty), tex(makeidx.sty), tex(multicol.sty), tex(graphicx.sty)
Requires:       tex(color.sty), tex(verbatim.sty), tex(moreverb.sty), tex(dcolumn.sty)
Requires:       tex(rotating.sty), tex(fontspec.sty), tex(polyglossia.sty), tex(zwpagelayout.sty)
Requires:       tex(hyperref.sty), tex(xevlna.sty), tex(ifpdf.sty), tex(fontenc.sty)
Requires:       tex(babel.sty), tex(mathptmx.sty), tex(natbib.sty), tex(keyval.sty)
Provides:       tex(cnbwp-manual.sty) = %{tl_version}, tex(cnbwp.cls) = %{tl_version}
Provides:       tex(cnbwpsizes.clo) = %{tl_version}

%description -n texlive-cnbwp
The package supports proper formatting of Working Papers of the
Czech National Bank (WP CNB). The package was developed for CNB
but it is also intended for authors from outside CNB.

%package -n texlive-cnbwp-doc
Summary:        Documentation for cnbwp
Version:        svn32550.0

Provides:       tex-cnbwp-doc
AutoReqProv:    No

%description -n texlive-cnbwp-doc
Documentation for cnbwp

%package -n texlive-cnltx
Provides:       tex-cnltx = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX tools and documenting facilities
Version:        svn38138.0.13

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pgfopts.sty), tex(etoolbox.sty), tex(ltxcmds.sty), tex(pdftexcmds.sty)
Requires:       tex(xcolor.sty), tex(trimspaces.sty), tex(ifxetex.sty), tex(ifluatex.sty)
Requires:       tex(fontenc.sty), tex(fontspec.sty), tex(libertine.sty), tex(superiors.sty)
Requires:       tex(microtype.sty), tex(beramono.sty), tex(fnpct.sty), tex(scrlayer-scrpage.sty)
Requires:       tex(biblatex.sty), tex(imakeidx.sty), tex(multicol.sty), tex(marginnote.sty)
Requires:       tex(ragged2e.sty), tex(hyperref.sty), tex(mdframed.sty), tex(idxcmds.sty)
Requires:       tex(textcomp.sty), tex(adjustbox.sty), tex(ulem.sty), tex(listings.sty)
Requires:       tex(catchfile.sty), tex(accsupp.sty), tex(translations.sty), tex(alphabetic.bbx)
Requires:       tex(alphabetic.cbx)
Provides:       tex(cnltx-base.sty) = %{tl_version}, tex(cnltx-doc.cls) = %{tl_version}
Provides:       tex(cnltx-example.sty) = %{tl_version}, tex(cnltx-listings.sty) = %{tl_version}
Provides:       tex(cnltx-names.sty) = %{tl_version}, tex(cnltx-tools.sty) = %{tl_version}
Provides:       tex(cnltx-translations.sty) = %{tl_version}
Provides:       tex(cnltx.bbx) = %{tl_version}, tex(cnltx.cbx) = %{tl_version}
Provides:       tex(cnltx.sty) = %{tl_version}

%description -n texlive-cnltx
This is a versatile bundle of packages and classes for
consistent formatting of control sequences, package options,
source code examples, and writing a package manual (including
an index containing the explained control sequences, options,
ldots). The bundle also provides several other small ideas of
mine such as a mechansim for providing abbreviations etc. Not
at least it provides a number of programming tools. The
intention behind this bundle mainly is a selfish one:
documenting my own packages. The bundle contains an index style
file cnltx.ist that should be placed in a directory in a TDS
makeindex directory.

%package -n texlive-cnltx-doc
Summary:        Documentation for cnltx
Version:        svn38138.0.13

Provides:       tex-cnltx-doc
AutoReqProv:    No

%description -n texlive-cnltx-doc
Documentation for cnltx

%package -n texlive-cntformats
Provides:       tex-cntformats = %{tl_version}
License:        LPPL 1.3
Summary:        A different way to read counters
Version:        svn34668.0.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(cnltx-base.sty)
Provides:       tex(cntformats.sty) = %{tl_version}

%description -n texlive-cntformats
The package offers package or class authors a way to format
counters with 'patterns'. These patterns do not affect affect
'normal' LaTeX treatment of counters.

%package -n texlive-cntformats-doc
Summary:        Documentation for cntformats
Version:        svn34668.0.7

Provides:       tex-cntformats-doc
AutoReqProv:    No

%description -n texlive-cntformats-doc
Documentation for cntformats

%package -n texlive-cntperchap
Provides:       tex-cntperchap = %{tl_version}
License:        LPPL 1.3
Summary:        Store counter values per chapter
Version:        svn37572.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(assoccnt.sty), tex(morewrites.sty), tex(xpatch.sty)
Requires:       tex(xparse.sty)
Provides:       tex(cntperchap.sty) = %{tl_version}

%description -n texlive-cntperchap
This package stores values of counters (which have been
registered beforehand) on a per chapter base and provides the
values on demand in the 2nd LaTeX compilation run. In this way
it is possible to know how many sections etc. there are lying
ahead and to react to these counter values, if needed. This is
a preliminary version that has been tested with book.cls,
memoir.cls, and scrbook.cls. The packages assoccnt (by the same
author) and xparse are needed as well.

%package -n texlive-cntperchap-doc
Summary:        Documentation for cntperchap
Version:        svn37572.0.3

Provides:       tex-cntperchap-doc
AutoReqProv:    No

%description -n texlive-cntperchap-doc
Documentation for cntperchap

%package -n texlive-codedoc
Provides:       tex-codedoc = %{tl_version}
License:        LPPL
Summary:        LaTeX code and documentation in LaTeX-format file
Version:        svn17630.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(makeidx.sty)
Provides:       tex(codedoc.cls) = %{tl_version}

%description -n texlive-codedoc
The CodeDoc class is an alternative to DocStrip (and others) to
produce LaTeX code along with its documentation without
departing from LaTeX's ordinary syntax. The documentation is
prepared like any other LaTeX document and the code to be
commented verbatim is simply delimited by an environment. When
an option is turned on in the class options, this code is
written to the desired file(s). The class also includes fully
customizable verbatim environments which provide the author
with separate commands to typeset the material and/or to
execute it.

%package -n texlive-codedoc-doc
Summary:        Documentation for codedoc
Version:        svn17630.0.3

Provides:       tex-codedoc-doc
AutoReqProv:    No

%description -n texlive-codedoc-doc
Documentation for codedoc

%package -n texlive-codepage
Provides:       tex-codepage = %{tl_version}
License:        BSD
Summary:        Support for variant code pages
Version:        svn21126.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(code437.tex) = %{tl_version}, tex(code850.tex) = %{tl_version}
Provides:       tex(codeiso1.tex) = %{tl_version}, tex(codemac.tex) = %{tl_version}
Provides:       tex(codepage.sty) = %{tl_version}, tex(initcar.tex) = %{tl_version}
Provides:       tex(shapecm.tex) = %{tl_version}, tex(shapedc.tex) = %{tl_version}

%description -n texlive-codepage
The package provides a mechanism for inputting non-ASCII text.
Nowadays, the job is mostly done by the inputenc package in the
LaTeX distribution.

%package -n texlive-codepage-doc
Summary:        Documentation for codepage
Version:        svn21126.0

Provides:       tex-codepage-doc
AutoReqProv:    No

%description -n texlive-codepage-doc
Documentation for codepage

%package -n texlive-codesection
Provides:       tex-codesection = %{tl_version}
License:        LPPL 1.3
Summary:        Provides an environment that may be conditionally included
Version:        svn34481.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty)
Provides:       tex(codesection.sty) = %{tl_version}

%description -n texlive-codesection
This package provides an environment to switch a section of
code on or off. The code may be placed anywhere in the file (it
is not limited to the document or the preamble). The motivation
for this package was to have commands which allow preselection
based on whether sections of code in a preamble of a template
are executed.

%package -n texlive-codesection-doc
Summary:        Documentation for codesection
Version:        svn34481.0.1

Provides:       tex-codesection-doc
AutoReqProv:    No

%description -n texlive-codesection-doc
Documentation for codesection

%package -n texlive-collection-langitalian
Summary:        Italian
Version:        svn30372.0
Requires:       texlive-base, texlive-collection-basic, texlive-amsldoc-it-doc, texlive-amsmath-it-doc
Requires:       texlive-amsthdoc-it-doc, tex-babel-italian
Requires:       tex-codicefiscaleitaliano, texlive-fancyhdr-it-doc
Requires:       tex-fixltxhyph, tex-frontespizio, tex-hyphen-italian, tex-itnumpar
Requires:       texlive-l2tabu-italian-doc, texlive-latex4wp-it-doc
Requires:       tex-layaureo, texlive-lshort-italian-doc
Requires:       texlive-psfrag-italian-doc, texlive-texlive-it-doc

%description -n texlive-collection-langitalian
Support for Italian.

%package -n texlive-collection-langjapanese
Summary:        Japanese
Version:        svn47703
Requires:       texlive-base, texlive-collection-langcjk
Requires:       texlive-ascmac, texlive-babel-japanese, texlive-bxbase, texlive-bxcjkjatype
Requires:       texlive-bxjalipsum, texlive-bxjaprnind, texlive-bxjscls, texlive-bxorigcapt
Requires:       texlive-convbkmk, texlive-endnotesj, texlive-gentombow, texlive-ifptex
Requires:       texlive-ifxptex, texlive-ipaex, texlive-japanese-otf, texlive-japanese-otf-uptex
Requires:       texlive-jlreq, texlive-jsclasses, texlive-lshort-japanese-doc, texlive-luatexja
Requires:       texlive-mendex-doc, texlive-morisawa, texlive-pbibtex-base, texlive-platex
Requires:       texlive-platex-tools, texlive-platexcheat-doc
Requires:       texlive-ptex, texlive-ptex-base, texlive-ptex-fonts, texlive-ptex-fontmaps
Requires:       texlive-ptex2pdf, texlive-pxbase, texlive-pxchfon, texlive-pxcjkcat
Requires:       texlive-pxjahyper, texlive-pxrubrica, texlive-pxufont, texlive-uplatex
Requires:       texlive-uptex-bin, texlive-uptex-base, texlive-uptex-fonts, texlive-wadalab
Requires:       texlive-zxjafbfont, texlive-zxjatype

%description -n texlive-collection-langjapanese
Support for Japanese; additional packages in collection-
langcjk.

%package -n texlive-codicefiscaleitaliano
Provides:       tex-codicefiscaleitaliano = %{tl_version}
License:        LPPL 1.3
Summary:        Test the consistency of the Italian personal Fiscal Code
Version:        svn29803.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(codicefiscaleitaliano.sty) = %{tl_version}

%description -n texlive-codicefiscaleitaliano
The alphanumeric string that forms the Italian personal Fiscal
Code is prone to be misspelled thus rendering a legal document
invalid. The package quickly verifies the consistency of the
fiscal code string, and can therefore be useful for lawyers and
accountants that use fiscal codes very frequently.

%package -n texlive-codicefiscaleitaliano-doc
Summary:        Documentation for codicefiscaleitaliano
Version:        svn29803.1.2

Provides:       tex-codicefiscaleitaliano-doc
AutoReqProv:    No

%description -n texlive-codicefiscaleitaliano-doc
Documentation for codicefiscaleitaliano

%package -n texlive-collcell
Provides:       tex-collcell = %{tl_version}
License:        LPPL 1.3
Summary:        Collect contents of a tabular cell as argument to a macro
Version:        svn21539.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty), tex(tabularx.sty), tex(etoolbox.sty)
Provides:       tex(collcell.sty) = %{tl_version}

%description -n texlive-collcell
The package provides macros that collect the content of a
tabular cell, and offer them as an argument to a macro. Special
care is taken to remove all aligning macros inserted by tabular
from the cell content. The macros also work in the last column
of a table, but do not support verbatim material inside the
cells.

%package -n texlive-collcell-doc
Summary:        Documentation for collcell
Version:        svn21539.0.5

Provides:       tex-collcell-doc
AutoReqProv:    No

%description -n texlive-collcell-doc
Documentation for collcell

%package -n texlive-collectbox
Provides:       tex-collectbox = %{tl_version}
License:        LPPL 1.3
Summary:        Collect and process macro arguments as boxes
Version:        svn26557.0.4b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(collectbox.sty) = %{tl_version}

%description -n texlive-collectbox
The package provides macros to collect and process a macro
argument (i.e., something which looks like a macro argument) as
a horizontal box rather than as a real macro argument. The
"arguments" are stored as if they had been saved by \savebox or
by the lrbox environment. Grouping tokens \bgroup and \egroup
may be used, which allows the user to have the beginning and
end of a group in different macro invocations, or to place them
in the begin and end code of an environment. Arguments may
contain verbatim material or other special use of characters.
The macros were designed for use within other macros.

%package -n texlive-collectbox-doc
Summary:        Documentation for collectbox
Version:        svn26557.0.4b

Provides:       tex-collectbox-doc
AutoReqProv:    No

%description -n texlive-collectbox-doc
Documentation for collectbox

%package -n texlive-collection-basic
Summary:        Essential programs and files
Version:        svn45851
Requires:       texlive-base, texlive-texlive.infra, texlive-amsfonts, texlive-bibtex
Requires:       texlive-cm, texlive-dvipdfmx, texlive-dvips, texlive-enctex
Requires:       texlive-etex, texlive-etex-pkg, texlive-glyphlist, texlive-graphics-def
Requires:       texlive-gsftopk, texlive-hyph-utf8, texlive-hyphen-base, texlive-ifluatex
Requires:       texlive-ifxetex, texlive-knuth-lib, texlive-knuth-local, texlive-kpathsea
Requires:       texlive-lua-alt-getopt, texlive-luatex, texlive-makeindex, texlive-metafont
Requires:       texlive-mflogo, texlive-mfware, texlive-pdftex, texlive-plain
Requires:       texlive-tetex, texlive-tex, texlive-tex-ini-files, texlive-texlive-common-doc
Requires:       texlive-texlive-docindex, texlive-texlive-en
Requires:       texlive-texlive-msg-translations, texlive-texlive-scripts
Requires:       texlive-unicode-data, texlive-updmap-map
Requires:       texlive-xdvi
Provides:       tex(tex) = %{tl_version}, tex = %{tl_version}
Requires:       dvipdfmx, xdvik

%description -n texlive-collection-basic
These files are regarded as basic for any TeX system, covering
plain TeX macros, Computer Modern fonts, and configuration for
common drivers; no LaTeX.

%package -n texlive-collection-bibtexextra
Summary:        BibTeX additional styles
Version:        svn47839
Requires:       texlive-base, texlive-collection-latex, texlive-aichej, texlive-ajl
Requires:       texlive-amsrefs, texlive-apacite, texlive-apalike2, texlive-archaeologie
Requires:       texlive-beebe, texlive-besjournals, texlive-bestpapers, texlive-bib2gls
Requires:       texlive-bibarts, texlive-bibexport, texlive-bibhtml, texlive-biblatex
Requires:       texlive-biblatex-abnt, texlive-biblatex-anonymous
Requires:       texlive-biblatex-archaeology, texlive-biblatex-arthistory-bonn
Requires:       texlive-biblatex-apa, texlive-biblatex-bookinarticle
Requires:       texlive-biblatex-bookinother, texlive-biblatex-bwl
Requires:       texlive-biblatex-caspervector, texlive-biblatex-chem
Requires:       texlive-biblatex-chicago, texlive-biblatex-claves
Requires:       texlive-biblatex-dw, texlive-biblatex-enc
Requires:       texlive-biblatex-fiwi, texlive-biblatex-gb7714-2015
Requires:       texlive-biblatex-gost, texlive-biblatex-historian
Requires:       texlive-biblatex-ieee, texlive-biblatex-ijsra
Requires:       texlive-biblatex-iso690, texlive-biblatex-juradiss
Requires:       texlive-biblatex-lni, texlive-biblatex-luh-ipw
Requires:       texlive-biblatex-manuscripts-philology, texlive-biblatex-mla
Requires:       texlive-biblatex-morenames, texlive-biblatex-multiple-dm
Requires:       texlive-biblatex-musuos, texlive-biblatex-nature
Requires:       texlive-biblatex-nejm, texlive-biblatex-nottsclassic
Requires:       texlive-biblatex-opcit-booktitle, texlive-biblatex-oxref
Requires:       texlive-biblatex-philosophy, texlive-biblatex-phys
Requires:       texlive-biblatex-publist, texlive-biblatex-realauthor
Requires:       texlive-biblatex-sbl, texlive-biblatex-science
Requires:       texlive-biblatex-shortfields, texlive-biblatex-socialscienceshuberlin
Requires:       texlive-biblatex-source-division, texlive-biblatex-subseries
Requires:       texlive-biblatex-swiss-legal, texlive-biblatex-trad
Requires:       texlive-biblatex-true-citepages-omit, texlive-biblist
Requires:       texlive-bibtexperllibs, texlive-bibtopic
Requires:       texlive-bibtopicprefix, texlive-bibunits
Requires:       texlive-biolett-bst, texlive-bookdb, texlive-breakcites, texlive-cell
Requires:       texlive-chbibref, texlive-chicago, texlive-chicago-annote, texlive-chembst
Requires:       texlive-chscite, texlive-citeall, texlive-citeref, texlive-collref
Requires:       texlive-compactbib, texlive-crossrefware
Requires:       texlive-custom-bib, texlive-din1505, texlive-dk-bib, texlive-doipubmed
Requires:       texlive-ecobiblatex, texlive-economic, texlive-fbs, texlive-figbib
Requires:       texlive-footbib, texlive-francais-bst, texlive-gbt7714, texlive-geschichtsfrkl
Requires:       texlive-harvard, texlive-harvmac, texlive-historische-zeitschrift, texlive-ietfbibs-doc
Requires:       texlive-ijqc, texlive-inlinebib, texlive-iopart-num, texlive-jneurosci
Requires:       texlive-jurabib, texlive-ksfh_nat, texlive-ltb2bib, texlive-listbib
Requires:       texlive-logreq, texlive-luabibentry, texlive-margbib, texlive-multibib
Requires:       texlive-multibibliography, texlive-munich
Requires:       texlive-nar, texlive-nmbib, texlive-notes2bib, texlive-notex-bst
Requires:       texlive-oscola, texlive-perception, texlive-pnas2009, texlive-rsc
Requires:       texlive-showtags, texlive-sort-by-letters
Requires:       texlive-splitbib, texlive-turabian-formatting
Requires:       texlive-uni-wtal-ger, texlive-uni-wtal-lin
Requires:       texlive-urlbst, texlive-usebib, texlive-vak, texlive-xcite

%description -n texlive-collection-bibtexextra
Additional BibTeX styles and bibliography data(bases), notably
including BibLaTeX.

%package -n texlive-collection-latex
Summary:        LaTeX fundamental packages
Version:        svn41614
Requires:       texlive-base, texlive-collection-basic, texlive-ae, texlive-amscls
Requires:       texlive-amsmath, texlive-babel, texlive-babel-english, texlive-babelbib
Requires:       texlive-carlisle, texlive-colortbl, texlive-fancyhdr, texlive-fix2col
Requires:       texlive-geometry, texlive-graphics, texlive-graphics-cfg, texlive-hyperref
Requires:       texlive-latex, texlive-latex-bin, texlive-latex-fonts, texlive-latexconfig
Requires:       texlive-ltxmisc, texlive-mfnfss, texlive-mptopdf, texlive-natbib
Requires:       texlive-oberdiek, texlive-pslatex, texlive-psnfss, texlive-pspicture
Requires:       texlive-tools, texlive-url
Provides:       tex(latex-base) = %{tl_version}

%description -n texlive-collection-latex
These packages are either mandated by the core LaTeX team, or
very widely used and strongly recommended in practice.

%package -n texlive-colortbl
Provides:       tex-colortbl = %{tl_version}
License:        LPPL
Summary:        Add colour to LaTeX tables
Version:        svn47614
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(array.sty), tex(color.sty)
Provides:       tex(colortbl.sty) = %{tl_version}

%description -n texlive-colortbl
The package allows rows and columns to be coloured, and even
individual cells.

%package -n texlive-colortbl-doc
Summary:        Documentation for colortbl
Version:        svn47614
Provides:       tex-colortbl-doc
AutoReqProv:    No

%description -n texlive-colortbl-doc
Documentation for colortbl


%package -n texlive-collref
Provides:       tex-collref = %{tl_version}
License:        LPPL 1.3
Summary:        Collect blocks of references into a single reference
Version:        svn46358
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(collref.sty) = %{tl_version}

%description -n texlive-collref
The package automatically collects multiple \bibitem
references, which always appear in the same sequence in \cite,
into a single \bibitem block.

%package -n texlive-collref-doc
Summary:        Documentation for collref
Version:        svn46358
Provides:       tex-collref-doc
AutoReqProv:    No

%description -n texlive-collref-doc
Documentation for collref

%package -n texlive-compactbib
Provides:       tex-compactbib = %{tl_version}
License:        LPPL
Summary:        Multiple thebibliography environments
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(compactbib.sty) = %{tl_version}

%description -n texlive-compactbib
Allows a second bibliography, optionally with a different
title, after the main bibliography.

%package -n texlive-collection-binextra
Summary:        TeX auxiliary programs
Version:        svn47945
Requires:       texlive-base, texlive-collection-basic, texlive-a2ping, texlive-adhocfilelist
Requires:       texlive-arara, asymptote, texlive-bibtex8, texlive-bibtexu
Requires:       texlive-bundledoc, texlive-checklistings
Requires:       texlive-chktex, texlive-ctan-o-mat, texlive-ctan_chk-doc, texlive-ctanify
Requires:       texlive-ctanupload, texlive-ctie, texlive-cweb, texlive-de-macro
Requires:       texlive-detex, texlive-dtl, texlive-dtxgen, texlive-dvi2tty
Requires:       texlive-dviasm, texlive-dvicopy, texlive-dvidvi, texlive-dviinfox
Requires:       texlive-dviljk, texlive-dvipng, texlive-dvipos, texlive-dvisvgm
Requires:       texlive-findhyph, texlive-fragmaster, texlive-hook-pre-commit-pkg-doc, texlive-hyphenex
Requires:       texlive-installfont, texlive-lacheck, texlive-latex-git-log, texlive-latex-papersize
Requires:       texlive-latex2man, texlive-latex2nemeth, texlive-latexdiff, texlive-latexfileversion
Requires:       latexmk, texlive-latexpand, texlive-latexindent, texlive-ltxfileinfo
Requires:       texlive-ltximg, texlive-listings-ext, texlive-make4ht, texlive-match_parens
Requires:       texlive-mflua, texlive-mkjobtexmf, texlive-patgen, texlive-pdfbook2
Requires:       texlive-pdfcrop, texlive-pdfjam, texlive-pdflatexpicscale, texlive-pdftools
Requires:       texlive-pdfxup, texlive-pfarrei, texlive-pkfix, texlive-pkfix-helper
Requires:       texlive-purifyeps, texlive-pythontex, texlive-seetexk, texlive-srcredact
Requires:       texlive-sty2dtx, texlive-synctex, texlive-tex4ebook, texlive-texcount
Requires:       texlive-texdef, texlive-texdiff, texlive-texdirflatten, texlive-texdoc
Requires:       texlive-texdoctk, texlive-texfot, texlive-texliveonfly, texlive-texloganalyser
Requires:       texlive-texosquery, texlive-texware, texlive-tie, texlive-tpic2pdftex
Requires:       texlive-typeoutfileinfo, texlive-web, dvipng
Obsoletes:      texlive-utils < %{tl_version}

%description -n texlive-collection-binextra
Various useful, but non-essential, support programs. Includes
programs and macros for DVI file manipulation, literate
programming, patgen, and the TeX Works Editor.

%package -n texlive-collection-context
Summary:        ConTeXt and packages
Version:        svn47139
Requires:       texlive-base, texlive-collection-basic, texlive-context, texlive-jmn
Requires:       texlive-context-account, texlive-context-algorithmic
Requires:       texlive-context-animation, texlive-context-annotation
Requires:       texlive-context-bnf, texlive-context-chromato
Requires:       texlive-context-cmscbf, texlive-context-cmttbf
Requires:       texlive-context-construction-plan, texlive-context-cyrillicnumbers
Requires:       texlive-context-degrade, texlive-context-fancybreak
Requires:       texlive-context-filter, texlive-context-french
Requires:       texlive-context-fullpage, texlive-context-gantt
Requires:       texlive-context-gnuplot, texlive-context-handlecsv
Requires:       texlive-context-inifile, texlive-context-layout
Requires:       texlive-context-letter, texlive-context-lettrine
Requires:       texlive-context-mathsets, texlive-context-notes-zh-cn
Requires:       texlive-context-rst, texlive-context-ruby
Requires:       texlive-context-simplefonts, texlive-context-simpleslides
Requires:       texlive-context-title, texlive-context-transliterator
Requires:       texlive-context-typearea, texlive-context-typescripts
Requires:       texlive-context-vim, texlive-context-visualcounter

%description -n texlive-collection-context
Hans Hagen's powerful ConTeXt system, http://pragma-ade.com.
Also includes third-party ConTeXt packages.

%package -n texlive-context-account
Provides:       tex-context-account = %{tl_version}
License:        Public Domain
Summary:        A simple accounting package
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context
Provides:       tex(t-account.tex) = %{tl_version}, tex(t-floatnumber.tex) = %{tl_version}

%description -n texlive-context-account
The package deals with "accounts" of its own specification.

%package -n texlive-context-account-doc
Summary:        Documentation for context-account
Version:        svn47085
Provides:       tex-context-account-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-account-doc
Documentation for context-account

%package -n texlive-context-algorithmic
Provides:       tex-context-algorithmic = %{tl_version}
License:        GPL+
Summary:        Algorithm handling in ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-algorithmic
Support for typesetting algorithms (a port of the LaTeX package
algorithmic, which was a predecessor of algorithmicx).

%package -n texlive-context-animation
Provides:       tex-context-animation = %{tl_version}
License:        GPLv3+
Summary:        Generate fieldstack based animation with ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-animation
The package is a port, to Context (mkvi), of the corresponding
LaTeX package.

%package -n texlive-context-animation-doc
Summary:        Documentation for context-animation
Version:        svn47085
Provides:       tex-context-animation-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-animation-doc
Documentation for context-animation

%package -n texlive-context-annotation
Provides:       tex-context-annotation = %{tl_version}
License:        LPPL
Summary:        context-annotation package
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-annotation
context-annotation package

%package -n texlive-context-annotation-doc
Summary:        Documentation for context-annotation
Version:        svn47085
Provides:       tex-context-annotation-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-annotation-doc
Documentation for context-annotation

%package -n texlive-context-bnf
Provides:       tex-context-bnf = %{tl_version}
License:        GPL+
Summary:        A BNF module for Context
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context
Provides:       tex(t-bnf.tex) = %{tl_version}

%description -n texlive-context-bnf
The module provides a simple way to write good-looking BNF-
style grammars in ConTeXt. Grammars are written using the BNF
syntax right in your ConTeXt documents, so there is a clear
separation between content and layout. This allows the user to
decide exactly how the grammar is to be displayed, while also
allowing the gist of the grammar to be understood from simply
looking at the source ConTeXt document.

%package -n texlive-context-bnf-doc
Summary:        Documentation for context-bnf
Version:        svn47085
Provides:       tex-context-bnf-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-bnf-doc
Documentation for context-bnf

%package -n texlive-context-chromato
Provides:       tex-context-chromato = %{tl_version}
License:        GPL+
Summary:        ConTeXt macros for chromatograms
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context
Provides:       tex(t-chromato.tex) = %{tl_version}

%description -n texlive-context-chromato
The module provides macros for drawing chromatograms.

%package -n texlive-context-chromato-doc
Summary:        Documentation for context-chromato
Version:        svn47085
Provides:       tex-context-chromato-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-chromato-doc
Documentation for context-chromato

%package -n texlive-context-construction-plan
Provides:       tex-context-construction-plan = %{tl_version}
License:        GPL+
Summary:        Construction plans in ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context
Provides:       tex(t-construction-plan.tex) = %{tl_version}

%description -n texlive-context-construction-plan
Generate a page with a figure at a well-defined scale.

%package -n texlive-context-construction-plan-doc
Summary:        Documentation for context-construction-plan
Version:        svn47085
Provides:       tex-context-construction-plan-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-construction-plan-doc
Documentation for context-construction-plan

%package -n texlive-context-cyrillicnumbers
Provides:       tex-context-cyrillicnumbers = %{tl_version}
License:        BSD
Summary:        Write numbers as cyrillic glyphs
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-cyrillicnumbers
The package extends Context's system of number conversion, by
adding numeration using cyrillic letters.

%package -n texlive-context-cyrillicnumbers-doc
Summary:        Documentation for context-cyrillicnumbers
Version:        svn47085
Provides:       tex-context-cyrillicnumbers-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-cyrillicnumbers-doc
Documentation for context-cyrillicnumbers

%package -n texlive-context-degrade
Provides:       tex-context-degrade = %{tl_version}
License:        GPL+
Summary:        Degrading JPEG images in ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context
Provides:       tex(t-degrade.tex) = %{tl_version}

%description -n texlive-context-degrade
context-degrade package

%package -n texlive-context-degrade-doc
Summary:        Documentation for context-degrade
Version:        svn47085
Provides:       tex-context-degrade-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-degrade-doc
Documentation for context-degrade

%package -n texlive-context-fancybreak
Provides:       tex-context-fancybreak = %{tl_version}
License:        GPL+
Summary:        Overfull pages with ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-fancybreak
The (ConTeXt) module allows insertion of thought breaks in
texts. With parameters one can adjust the spacing around the
content and set a default symbol.

%package -n texlive-context-fancybreak-doc
Summary:        Documentation for context-fancybreak
Version:        svn47085
Provides:       tex-context-fancybreak-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-fancybreak-doc
Documentation for context-fancybreak

%package -n texlive-context-filter
Provides:       tex-context-filter = %{tl_version}
License:        BSD
Summary:        Run external programs on the contents of a start-stop environment
Version:        svn48390
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context
Provides:       tex(t-module-catcodes.tex) = %{tl_version}

%description -n texlive-context-filter
The filter module provides a simple interface to run external
programs on the contents of a start-stop environment. Options
are available to run the external program only if the content
of the environment has changed, to specify how the program
output should be read back, and to choose the name of the
temporary files that are created. The module is compatible with
both MkII and MkIV.

%package -n texlive-context-filter-doc
Summary:        Documentation for context-filter
Version:        svn48390
Provides:       tex-context-filter-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-filter-doc
Documentation for context-filter

%package -n texlive-context-french
Provides:       tex-context-french = %{tl_version}
License:        GPL+
Summary:        Support for writing French in ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-french
Deals with spacing around French punctuation; the package is
distributed for ConTeXt Mark iv only.

%package -n texlive-context-french-doc
Summary:        Documentation for context-french
Version:        svn47085
Provides:       tex-context-french-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-french-doc
Documentation for context-french

%package -n texlive-context-fullpage
Provides:       tex-context-fullpage = %{tl_version}
License:        GPL+
Summary:        Overfull pages with ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-fullpage
The (ConTeXt) module copies the functionality of the fullpage,
and adds a styling parameter, given in the \usemodule command

%package -n texlive-context-fullpage-doc
Summary:        Documentation for context-fullpage
Version:        svn47085
Provides:       tex-context-fullpage-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-fullpage-doc
Documentation for context-fullpage


%package -n texlive-context-gantt
Provides:       tex-context-gantt = %{tl_version}
License:        Public Domain
Summary:        GANTT module for ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context, tex-hatching
Provides:       tex(gantt-s-mp.tex) = %{tl_version}, tex(gantt-s-tikz.tex) = %{tl_version}
Provides:       tex(t-gantt.tex) = %{tl_version}

%description -n texlive-context-gantt
Gantt is a module for drawing Gantt charts via metapost or
pgf/tikz.

%package -n texlive-context-gantt-doc
Summary:        Documentation for context-gantt
Version:        svn47085
Provides:       tex-context-gantt-doc
AutoReqProv:    No
Requires:       tex-context-doc, tex-hatching-doc

%description -n texlive-context-gantt-doc
Documentation for context-gantt


%package -n texlive-context-gnuplot
Provides:       tex-context-gnuplot = %{tl_version}
License:        GPL+
Summary:        Inclusion of Gnuplot graphs in ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-gnuplot
Enables simple creation and inclusion of graphs with Gnuplot.
The package writes a script into temporary file, runs Gnuplot
and includes the resulting graphic directly into the document.
See the ConTeXt Garden package page for further details.

%package -n texlive-context-gnuplot-doc
Summary:        Documentation for context-gnuplot
Version:        svn47085
Provides:       tex-context-gnuplot-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-gnuplot-doc
Documentation for context-gnuplot

%package -n texlive-context-letter
Provides:       tex-context-letter = %{tl_version}
License:        GPL+
Summary:        ConTeXt package for writing letters
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-letter
A means of writing 'vanilla' letters and memos is provided,
with support covering ConTeXt Mkii and Mkiv. The design of
letters may be amended by a wide range of style specifications.

%package -n texlive-context-letter-doc
Summary:        Documentation for context-letter
Version:        svn47085
Provides:       tex-context-letter-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-letter-doc
Documentation for context-letter

%package -n texlive-context-lettrine
Provides:       tex-context-lettrine = %{tl_version}
License:        Public Domain
Summary:        A ConTeXt implementation of lettrines
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context
Provides:       tex(t-lettrine.tex) = %{tl_version}

%description -n texlive-context-lettrine
This is a re-implementation of the LaTeX package lettrine.

%package -n texlive-context-lettrine-doc
Summary:        Documentation for context-lettrine
Version:        svn47085
Provides:       tex-context-lettrine-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-lettrine-doc
Documentation for context-lettrine

%package -n texlive-context-mathsets
Provides:       tex-context-mathsets = %{tl_version}
License:        BSD
Summary:        Set notation in ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context
Provides:       tex(t-mathsets.tex) = %{tl_version}

%description -n texlive-context-mathsets
Typeset good-looking set notation (e.g., {x|x \in Y}), as well
as similar things such as Dirac bra-ket notation, conditional
probabilities, etc. The package is at least inspired by braket.

%package -n texlive-context-mathsets-doc
Summary:        Documentation for context-mathsets
Version:        svn47085
Provides:       tex-context-mathsets-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-mathsets-doc
Documentation for context-mathsets

%package -n texlive-context-notes-zh-cn
Provides:       tex-context-notes-zh-cn = %{tl_version}
License:        GPL+
Summary:        Notes on using ConTeXt MkIV
Version:        svn23171.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-notes-zh-cn
An introductory tutorial on ConTeXt, in Chinese. The document
covers ConTeXt installation, fonts, layout design, cross-
reference, project structure, metafun and presentation design.

%package -n texlive-context-notes-zh-cn-doc
Summary:        Documentation for context-notes-zh-cn
Version:        svn23171.0

Provides:       tex-context-notes-zh-cn-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-notes-zh-cn-doc
Documentation for context-notes-zh-cn

%package -n texlive-context-rst
Provides:       tex-context-rst = %{tl_version}
License:        BSD
Summary:        Process reStructuredText with ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-rst
The package provides a converter and module for typesetting
reStructuredText with ConTeXt. The module uses several lua
scripts in doing its work. Documentation is supplied in rst,
which seems to be readable as text, but...

%package -n texlive-context-rst-doc
Summary:        Documentation for context-rst
Version:        svn47085
Provides:       tex-context-rst-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-rst-doc
Documentation for context-rst

%package -n texlive-context-ruby
Provides:       tex-context-ruby = %{tl_version}
License:        Public Domain
Summary:        Ruby annotations in ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-ruby
Ruby markup (aka furigana in Japan) are inline annotations
above or below a word to indicate the reading of ideographic
characters. The module implements the W3C specification for
simple ruby in ConTeXt. The position and layout of the base
text and the ruby text can becontrolled by parameters.

%package -n texlive-context-ruby-doc
Summary:        Documentation for context-ruby
Version:        svn47085
Provides:       tex-context-ruby-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-ruby-doc
Documentation for context-ruby

%package -n texlive-context-simplefonts
Provides:       tex-context-simplefonts = %{tl_version}
License:        GPL+
Summary:        Simplified font usage for ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-simplefonts
The package defines a set of commands for loading and using
fonts in ConTeXt.

%package -n texlive-context-simplefonts-doc
Summary:        Documentation for context-simplefonts
Version:        svn47085
Provides:       tex-context-simplefonts-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-simplefonts-doc
Documentation for context-simplefonts

%package -n texlive-context-simpleslides
Provides:       tex-context-simpleslides = %{tl_version}
License:        LPPL
Summary:        context-simpleslides package
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context
Provides:       tex(s-simpleslides-BigNumber.tex) = %{tl_version}
Provides:       tex(s-simpleslides-BlackBoard.tex) = %{tl_version}
Provides:       tex(s-simpleslides-BottomSquares.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Boxed.tex) = %{tl_version}
Provides:       tex(s-simpleslides-BoxedTitle.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Ellipse.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Embossed.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Framed.tex) = %{tl_version}
Provides:       tex(s-simpleslides-FramedTitle.tex) = %{tl_version}
Provides:       tex(s-simpleslides-FuzzyFrame.tex) = %{tl_version}
Provides:       tex(s-simpleslides-FuzzyTopic.tex) = %{tl_version}
Provides:       tex(s-simpleslides-HorizontalStripes.tex) = %{tl_version}
Provides:       tex(s-simpleslides-NarrowStripes.tex) = %{tl_version}
Provides:       tex(s-simpleslides-PlainCounter.tex) = %{tl_version}
Provides:       tex(s-simpleslides-RainbowStripe.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Rounded.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Shaded.tex) = %{tl_version}
Provides:       tex(s-simpleslides-SideSquares.tex) = %{tl_version}
Provides:       tex(s-simpleslides-SideToc.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Split.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Sunrise.tex) = %{tl_version}
Provides:       tex(s-simpleslides-Swoosh.tex) = %{tl_version}
Provides:       tex(s-simpleslides-ThickStripes.tex) = %{tl_version}
Provides:       tex(s-simpleslides-default.tex) = %{tl_version}

%description -n texlive-context-simpleslides
context-simpleslides package

%package -n texlive-context-simpleslides-doc
Summary:        Documentation for context-simpleslides
Version:        svn47085
Provides:       tex-context-simpleslides-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-simpleslides-doc
Documentation for context-simpleslides

%package -n texlive-context-title
Provides:       tex-context-title = %{tl_version}
License:        LPPL
Summary:        context-title package
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-title
context-title package

%package -n texlive-context-title-doc
Summary:        Documentation for context-title
Version:        svn47085
Provides:       tex-context-title-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-title-doc
Documentation for context-title

%package -n texlive-context-transliterator
Provides:       tex-context-transliterator = %{tl_version}
License:        BSD
Summary:        Transliterate text from 'other' alphabets
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context
Provides:       tex(t-transliterator.tex) = %{tl_version}

%description -n texlive-context-transliterator
The package will read text in one alphabet, and provide a
transliterated version in another; this is useful for readers
who cannot read the original alphabet. The package can make
allowance for hyphenation.

%package -n texlive-context-transliterator-doc
Summary:        Documentation for context-transliterator
Version:        svn47085
Provides:       tex-context-transliterator-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-transliterator-doc
Documentation for context-transliterator

%package -n texlive-context-typearea
Provides:       tex-context-typearea = %{tl_version}
License:        GPL+
Summary:        Something like Koma-Script typearea
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context
Provides:       tex(t-typearea.tex) = %{tl_version}

%description -n texlive-context-typearea
The module provides a command that calculates the page layout
as the LaTeX package typearea does.

%package -n texlive-context-typearea-doc
Summary:        Documentation for context-typearea
Version:        svn47085
Provides:       tex-context-typearea-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-typearea-doc
Documentation for context-typearea

%package -n texlive-context-typescripts
Provides:       tex-context-typescripts = %{tl_version}
License:        GPLv2+
Summary:        Small modules to load various fonts for use in ConTeXt
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-typescripts
The package provides files offering interfaces to 33 publicly
available fonts (or collections of fonts from the same
foundry); each is available in a .mkii and a .mkiv version.

%package -n texlive-context-typescripts-doc
Summary:        Documentation for context-typescripts
Version:        svn47085
Provides:       tex-context-typescripts-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-typescripts-doc
Documentation for context-typescripts

%package -n texlive-context-vim
Provides:       tex-context-vim = %{tl_version}
License:        BSD
Summary:        Generate Context syntax highlighting code from vim
Version:        svn48391
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context-filter, tex-context
Provides:       tex(t-syntax-groups.tex) = %{tl_version}
Provides:       tex(t-vim.tex) = %{tl_version}

%description -n texlive-context-vim
ConTeXt has excellent pretty printing capabilities for many
languages. The code for pretty printing is written in TeX, and
due to catcode juggling, such verbatim typesetting is perhaps
the trickiest part of TeX. This makes it difficult for a
"normal" user to define syntax highlighting rules for a new
language. This module takes the onus of defining syntax
highlighting rules away from the user and uses ViM editor to
generate the syntax highlighting. There is a helper
2context.vim script to do the syntax parsing in ViM.

%package -n texlive-context-vim-doc
Summary:        Documentation for context-vim
Version:        svn48391
Provides:       tex-context-vim-doc
AutoReqProv:    No
Requires:       tex-context-filter-doc, tex-context-doc

%description -n texlive-context-vim-doc
Documentation for context-vim

%package -n texlive-context-visualcounter
Provides:       tex-context-visualcounter = %{tl_version}
License:        LPPL
Summary:        context-visualcounter package
Version:        svn47085
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex-context

%description -n texlive-context-visualcounter
context-visualcounter package

%package -n texlive-context-visualcounter-doc
Summary:        Documentation for context-visualcounter
Version:        svn47085
Provides:       tex-context-visualcounter-doc
AutoReqProv:    No
Requires:       tex-context-doc

%description -n texlive-context-visualcounter-doc
Documentation for context-visualcounter

%package -n texlive-collection-fontsextra
Summary:        Additional fonts
Version:        svn47656
Requires:       texlive-base, texlive-collection-basic, texlive-asana-math, texlive-academicons
Requires:       texlive-accanthis, texlive-adforn, texlive-adfsymbols, texlive-aecc
Requires:       texlive-alegreya, texlive-algolrevived, texlive-allrunes, texlive-almfixed
Requires:       texlive-anonymouspro, texlive-antiqua, texlive-antt, texlive-archaic
Requires:       texlive-arev, texlive-arimo, texlive-asapsym, texlive-ascii-font
Requires:       texlive-aspectratio, texlive-astro, texlive-augie, texlive-auncial-new
Requires:       texlive-aurical, texlive-b1encoding, texlive-barcodes, texlive-baskervald
Requires:       texlive-baskervaldx, texlive-baskervillef
Requires:       texlive-bbding, texlive-bbm, texlive-bbm-macros, texlive-bbold
Requires:       texlive-bbold-type1, texlive-belleek, texlive-bera, texlive-berenisadf
Requires:       texlive-beuron, texlive-bguq, texlive-blacklettert1, texlive-boisik
Requires:       texlive-bookhands, texlive-boondox, texlive-braille, texlive-brushscr
Requires:       texlive-cabin, texlive-caladea, texlive-calligra, texlive-calligra-type1
Requires:       texlive-cantarell, texlive-carlito, texlive-carolmin-ps, texlive-ccicons
Requires:       texlive-cfr-initials, texlive-cfr-lm, texlive-cherokee, texlive-chivo
Requires:       texlive-cinzel, texlive-clearsans, texlive-cm-lgc, texlive-cm-mf-extra-bold
Requires:       texlive-cm-unicode, texlive-cmbright, texlive-cmexb, texlive-cmll
Requires:       texlive-cmpica, texlive-cmsrb, texlive-cmtiup, texlive-cochineal
Requires:       texlive-comfortaa, texlive-comicneue, texlive-concmath-fonts, texlive-cookingsymbols
Requires:       texlive-cormorantgaramond, texlive-countriesofeurope
Requires:       texlive-courier-scaled, texlive-crimson, texlive-cryst, texlive-cyklop
Requires:       texlive-dancers, texlive-dantelogo, texlive-dejavu, texlive-dejavu-otf
Requires:       texlive-dice, texlive-dictsym, texlive-dingbat, texlive-doublestroke
Requires:       texlive-dozenal, texlive-drm, texlive-droid, texlive-dsserif
Requires:       texlive-duerer, texlive-duerer-latex, texlive-dutchcal, texlive-ean
Requires:       texlive-ebgaramond, texlive-ebgaramond-maths
Requires:       texlive-ecc, texlive-eco, texlive-eiad, texlive-eiad-ltx
Requires:       texlive-electrum, texlive-elvish, texlive-epigrafica, texlive-epsdice
Requires:       texlive-erewhon, texlive-esrelation, texlive-esstix, texlive-esvect
Requires:       texlive-eulervm, texlive-euxm, texlive-fbb, texlive-fdsymbol
Requires:       texlive-fetamont, texlive-feyn, texlive-fge, texlive-fira
Requires:       texlive-foekfont, texlive-fonetika, texlive-fontawesome, texlive-fontawesome5
Requires:       texlive-fontmfizz, texlive-fonts-churchslavonic
Requires:       texlive-fourier, texlive-fouriernc, texlive-frcursive, texlive-frederika2016
Requires:       texlive-genealogy, texlive-gentium-tug, texlive-gfsartemisia, texlive-gfsbodoni
Requires:       texlive-gfscomplutum, texlive-gfsdidot, texlive-gfsneohellenic, texlive-gfsneohellenicmath
Requires:       texlive-gfssolomos, texlive-gillcm, texlive-gillius, texlive-gnu-freefont
Requires:       texlive-gofonts, texlive-gothic, texlive-greenpoint, texlive-grotesq
Requires:       texlive-hacm, texlive-hands, texlive-heuristica, texlive-hfbright
Requires:       texlive-hfoldsty, texlive-ifsym, texlive-imfellenglish, texlive-inconsolata
Requires:       texlive-initials, texlive-ipaex-type1, texlive-iwona, texlive-jablantile
Requires:       texlive-jamtimes, texlive-junicode, texlive-kixfont, texlive-kpfonts
Requires:       texlive-kurier, texlive-lato, texlive-lfb, texlive-libertine
Requires:       texlive-libertinegc, texlive-libertinus, texlive-libertinus-otf, texlive-libertinust1math
Requires:       texlive-librebaskerville, texlive-librebodoni
Requires:       texlive-librecaslon, texlive-libris, texlive-lineara, texlive-lobster2
Requires:       texlive-lxfonts, texlive-ly1, texlive-mathabx, texlive-mathabx-type1
Requires:       texlive-mathdesign, texlive-mdputu, texlive-mdsymbol, texlive-merriweather
Requires:       texlive-miama, texlive-mintspirit, texlive-missaali, texlive-mnsymbol
Requires:       texlive-montserrat, texlive-mweights, texlive-newpx, texlive-newtx
Requires:       texlive-newtxsf, texlive-newtxtt, texlive-niceframe-type1, texlive-nimbus15
Requires:       texlive-nkarta, texlive-noto, texlive-obnov, texlive-ocherokee
Requires:       texlive-ocr-b, texlive-ocr-b-outline, texlive-ogham, texlive-oinuit
Requires:       texlive-old-arrows, texlive-oldlatin, texlive-oldstandard, texlive-opensans
Requires:       texlive-orkhun, texlive-overlock, texlive-pacioli, texlive-paratype
Requires:       texlive-phaistos, texlive-phonetic, texlive-pigpen, texlive-playfair
Requires:       texlive-plex, texlive-plex-otf, texlive-poltawski, texlive-prodint
Requires:       texlive-punk, texlive-punk-latex, texlive-punknova, texlive-pxtxalfa
Requires:       texlive-quattrocento, texlive-raleway, texlive-recycle, texlive-roboto
Requires:       texlive-romande, texlive-rosario, texlive-rsfso, texlive-sansmathaccent
Requires:       texlive-sansmathfonts, texlive-sauter, texlive-sauterfonts, texlive-schulschriften
Requires:       texlive-semaphor, texlive-shobhika, texlive-skull, texlive-sourcecodepro
Requires:       texlive-sourcesanspro, texlive-sourceserifpro
Requires:       texlive-starfont, texlive-staves, texlive-stickstoo, texlive-stix
Requires:       texlive-stix2-otf, texlive-stix2-type1, texlive-superiors, texlive-svrsymbols
Requires:       texlive-tapir, texlive-tempora, texlive-tengwarscript, texlive-tfrupee
Requires:       texlive-tinos, texlive-tpslifonts, texlive-trajan, texlive-txfontsb
Requires:       texlive-txuprcal, texlive-typicons, texlive-umtypewriter, texlive-universa
Requires:       texlive-universalis, texlive-uppunctlm, texlive-urwchancal, texlive-venturisadf
Requires:       texlive-wsuipa, texlive-xcharter, texlive-xits, texlive-yfonts
Requires:       texlive-yfonts-t1, texlive-yinit-otf, texlive-zlmtt

%description -n texlive-collection-fontsextra
collection-fontsextra package

%package -n texlive-comfortaa
Provides:       tex-comfortaa = %{tl_version}
License:        LPPL 1.3
Summary:        Sans serif font, with LaTeX support
Version:        svn27536.2.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(keyval.sty), tex(slantsc.sty)
Provides:       tex(comfortaa-01.enc) = %{tl_version}, tex(comfortaa-02.enc) = %{tl_version}
Provides:       tex(comfortaa-03.enc) = %{tl_version}, tex(comfortaa-dotlessj.enc) = %{tl_version}
Provides:       tex(comfortaa.map) = %{tl_version}, tex(Comfortaa-Bold-01.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-02.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-03.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-01.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-02.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-03.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-dotlessj.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-lgr.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-ot1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-t1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-t2a.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-t2b.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-t2c.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-ts1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-x2.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-dotlessj.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-lgr.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-ot1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-t1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-t2a.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-t2b.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-t2c.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-ts1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold-x2.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-01.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-02.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-03.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-01.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-02.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-03.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-dotlessj.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-lgr.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-ot1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-t1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-t2a.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-t2b.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-t2c.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-ts1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-x2.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-dotlessj.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-lgr.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-ot1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-t1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-t2a.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-t2b.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-t2c.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-ts1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Light-x2.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-01.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-02.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-03.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-01.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-02.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-03.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-dotlessj.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-lgr.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-ot1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-t1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-t2a.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-t2b.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-t2c.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-ts1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-x2.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-dotlessj.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-lgr.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-ot1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-t1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-t2a.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-t2b.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-t2c.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-ts1.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Regular-x2.tfm) = %{tl_version}
Provides:       tex(Comfortaa-Bold.ttf) = %{tl_version}, tex(Comfortaa-Light.ttf) = %{tl_version}
Provides:       tex(Comfortaa-Regular.ttf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-LCDFJ.pfb) = %{tl_version}
Provides:       tex(Comfortaa-Bold.pfb) = %{tl_version}, tex(Comfortaa-Light-LCDFJ.pfb) = %{tl_version}
Provides:       tex(Comfortaa-Light.pfb) = %{tl_version}
Provides:       tex(Comfortaa-Regular-LCDFJ.pfb) = %{tl_version}
Provides:       tex(Comfortaa-Regular.pfb) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-lgr.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-ot1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-t1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-t2a.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-t2b.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-t2c.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-ts1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-Slanted-x2.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-lgr.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-ot1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-t1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-t2a.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-t2b.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-t2c.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-ts1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Bold-x2.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-lgr.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-ot1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-t1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-t2a.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-t2b.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-t2c.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-ts1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-Slanted-x2.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-lgr.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-ot1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-t1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-t2a.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-t2b.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-t2c.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-ts1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Light-x2.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-lgr.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-ot1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-t1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-t2a.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-t2b.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-t2c.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-ts1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-Slanted-x2.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-lgr.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-ot1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-t1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-t2a.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-t2b.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-t2c.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-ts1.vf) = %{tl_version}
Provides:       tex(Comfortaa-Regular-x2.vf) = %{tl_version}
Provides:       tex(comfortaa.sty) = %{tl_version}, tex(lgrfco.fd) = %{tl_version}
Provides:       tex(ot1fco.fd) = %{tl_version}, tex(t1fco.fd) = %{tl_version}
Provides:       tex(t2afco.fd) = %{tl_version}, tex(t2bfco.fd) = %{tl_version}
Provides:       tex(t2cfco.fd) = %{tl_version}, tex(ts1fco.fd) = %{tl_version}
Provides:       tex(x2fco.fd) = %{tl_version}

%description -n texlive-comfortaa
Comfortaa is a sans-serif font, comfortable in every aspect,
designed by Johan Aakerlund. The font, which includes three
weights (thin, regular and bold), is available on Johan's
deviantArt web page as TrueType files under the Open Font
License version 1.1. This package provides support for this
font in LaTeX, and includes both the TrueType fonts, and
conversions to Adobe Type 1 format.

%package -n texlive-comfortaa-doc
Summary:        Documentation for comfortaa
Version:        svn27536.2.3

Provides:       tex-comfortaa-doc
AutoReqProv:    No

%description -n texlive-comfortaa-doc
Documentation for comfortaa

%package -n texlive-comicneue
Provides:       tex-comicneue = %{tl_version}
License:        OFL
Summary:        Use Comic Neue with TeX(-alike) systems
Version:        svn42851
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(l3keys2e.sty)
Requires:       tex(xparse.sty), tex(fontspec.sty), tex(fontenc.sty), tex(mweights.sty)
Provides:       tex(a_bs6yxn.enc) = %{tl_version}, tex(a_lfux4u.enc) = %{tl_version}
Provides:       tex(a_t3s7zg.enc) = %{tl_version}, tex(a_yvpaqy.enc) = %{tl_version}
Provides:       tex(ComicNeue.map) = %{tl_version}, tex(ComicNeueAngular.map) = %{tl_version}
Provides:       tex(ComicNeue-Angular_Bold.otf) = %{tl_version}
Provides:       tex(ComicNeue-Angular_Bold_Oblique.otf) = %{tl_version}
Provides:       tex(ComicNeue-Angular_Light.otf) = %{tl_version}
Provides:       tex(ComicNeue-Angular_Light_Oblique.otf) = %{tl_version}
Provides:       tex(ComicNeue-Angular_Regular.otf) = %{tl_version}
Provides:       tex(ComicNeue-Angular_Regular_Oblique.otf) = %{tl_version}
Provides:       tex(ComicNeue_Bold.otf) = %{tl_version}, tex(ComicNeue_Bold_Oblique.otf) = %{tl_version}
Provides:       tex(ComicNeue_Light.otf) = %{tl_version}
Provides:       tex(ComicNeue_Light_Oblique.otf) = %{tl_version}
Provides:       tex(ComicNeue_Regular.otf) = %{tl_version}
Provides:       tex(ComicNeue_Regular_Oblique.otf) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeue-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeue-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(ComicNeue-Bold.pfb) = %{tl_version}, tex(ComicNeue-BoldLCDFJ.pfb) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique.pfb) = %{tl_version}
Provides:       tex(ComicNeue-BoldObliqueLCDFJ.pfb) = %{tl_version}
Provides:       tex(ComicNeue-Light.pfb) = %{tl_version}
Provides:       tex(ComicNeue-LightLCDFJ.pfb) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique.pfb) = %{tl_version}
Provides:       tex(ComicNeue-LightObliqueLCDFJ.pfb) = %{tl_version}
Provides:       tex(ComicNeue-Oblique.pfb) = %{tl_version}
Provides:       tex(ComicNeue-ObliqueLCDFJ.pfb) = %{tl_version}
Provides:       tex(ComicNeue.pfb) = %{tl_version}, tex(ComicNeueAngular-Bold.pfb) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldLCDFJ.pfb) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique.pfb) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldObliqueLCDFJ.pfb) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light.pfb) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightLCDFJ.pfb) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique.pfb) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightObliqueLCDFJ.pfb) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique.pfb) = %{tl_version}
Provides:       tex(ComicNeueAngular-ObliqueLCDFJ.pfb) = %{tl_version}
Provides:       tex(ComicNeueAngular.pfb) = %{tl_version}
Provides:       tex(ComicNeueAngularLCDFJ.pfb) = %{tl_version}
Provides:       tex(ComicNeueLCDFJ.pfb) = %{tl_version}, tex(ComicNeue-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(ComicNeue-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-ly1.vf) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-ot1.vf) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-t1.vf) = %{tl_version}
Provides:       tex(ComicNeue-BoldOblique-tlf-ts1.vf) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-ot1.vf) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(ComicNeue-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-ly1.vf) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-ot1.vf) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-t1.vf) = %{tl_version}
Provides:       tex(ComicNeue-LightOblique-tlf-ts1.vf) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-ly1.vf) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-ot1.vf) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-t1.vf) = %{tl_version}
Provides:       tex(ComicNeue-Oblique-tlf-ts1.vf) = %{tl_version}
Provides:       tex(ComicNeue-tlf-ly1.vf) = %{tl_version}
Provides:       tex(ComicNeue-tlf-ot1.vf) = %{tl_version}
Provides:       tex(ComicNeue-tlf-t1.vf) = %{tl_version}
Provides:       tex(ComicNeue-tlf-ts1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-ly1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-ot1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-t1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-BoldOblique-tlf-ts1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-ot1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-ly1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-ot1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-t1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-LightOblique-tlf-ts1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-ly1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-ot1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-t1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-Oblique-tlf-ts1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-ot1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-t1.vf) = %{tl_version}
Provides:       tex(ComicNeueAngular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LY1ComicNeue-TLF.fd) = %{tl_version}
Provides:       tex(LY1ComicNeueAngular-TLF.fd) = %{tl_version}
Provides:       tex(OT1ComicNeue-TLF.fd) = %{tl_version}
Provides:       tex(OT1ComicNeueAngular-TLF.fd) = %{tl_version}
Provides:       tex(T1ComicNeue-TLF.fd) = %{tl_version}, tex(T1ComicNeueAngular-TLF.fd) = %{tl_version}
Provides:       tex(TS1ComicNeue-TLF.fd) = %{tl_version}
Provides:       tex(TS1ComicNeueAngular-TLF.fd) = %{tl_version}
Provides:       tex(comicneue.sty) = %{tl_version}

%description -n texlive-comicneue
Comic Neue is a well-known redesign of the (in)famous Comic
Sans font. The package provides the original OpenType font for
XeTeX and LuaTeX users, and also has converted Type1 files for
pdfTeX users. Issues with this package can be reported on
GitHub or emailed to tex@slxh.nl.

%package -n texlive-comicneue-doc
Summary:        Documentation for comicneue
Version:        svn42851
Provides:       tex-comicneue-doc
AutoReqProv:    No

%description -n texlive-comicneue-doc
Documentation for comicneue

%package -n texlive-concmath-fonts
Provides:       tex-concmath-fonts = %{tl_version}
License:        LPPL
Summary:        Concrete mathematics fonts
Version:        svn17218.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(xccam10.tfm) = %{tl_version}, tex(xccam5.tfm) = %{tl_version}
Provides:       tex(xccam6.tfm) = %{tl_version}, tex(xccam7.tfm) = %{tl_version}
Provides:       tex(xccam8.tfm) = %{tl_version}, tex(xccam9.tfm) = %{tl_version}
Provides:       tex(xccbm10.tfm) = %{tl_version}, tex(xccbm5.tfm) = %{tl_version}
Provides:       tex(xccbm6.tfm) = %{tl_version}, tex(xccbm7.tfm) = %{tl_version}
Provides:       tex(xccbm8.tfm) = %{tl_version}, tex(xccbm9.tfm) = %{tl_version}
Provides:       tex(xccex10.tfm) = %{tl_version}, tex(xccex7.tfm) = %{tl_version}
Provides:       tex(xccex8.tfm) = %{tl_version}, tex(xccex9.tfm) = %{tl_version}
Provides:       tex(xccmi10.tfm) = %{tl_version}, tex(xccmi5.tfm) = %{tl_version}
Provides:       tex(xccmi6.tfm) = %{tl_version}, tex(xccmi7.tfm) = %{tl_version}
Provides:       tex(xccmi8.tfm) = %{tl_version}, tex(xccmi9.tfm) = %{tl_version}
Provides:       tex(xccsy10.tfm) = %{tl_version}, tex(xccsy5.tfm) = %{tl_version}
Provides:       tex(xccsy6.tfm) = %{tl_version}, tex(xccsy7.tfm) = %{tl_version}
Provides:       tex(xccsy8.tfm) = %{tl_version}, tex(xccsy9.tfm) = %{tl_version}

%description -n texlive-concmath-fonts
The fonts are derived from the computer modern mathematics
fonts and from Knuth's Concrete Roman fonts; they are
distributed as Metafont source. LaTeX support is offered by the
concmath package.

%package -n texlive-concmath-fonts-doc
Summary:        Documentation for concmath-fonts
Version:        svn17218.0

Provides:       tex-concmath-fonts-doc
AutoReqProv:    No

%description -n texlive-concmath-fonts-doc
Documentation for concmath-fonts

%package -n texlive-cookingsymbols
Provides:       tex-cookingsymbols = %{tl_version}
License:        LPPL
Summary:        Symbols for recipes
Version:        svn35929.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cookingsymbols.tfm) = %{tl_version}, tex(cookingsymbols.sty) = %{tl_version}

%description -n texlive-cookingsymbols
The package provides 11 symbols for typesetting recipes: oven,
gasstove, topheat, fanoven, gloves and dish symbol (among
others). The symbols are defined using Metafont.

%package -n texlive-cookingsymbols-doc
Summary:        Documentation for cookingsymbols
Version:        svn35929.1.1

Provides:       tex-cookingsymbols-doc
AutoReqProv:    No

%description -n texlive-cookingsymbols-doc
Documentation for cookingsymbols

%package -n texlive-countriesofeurope
Provides:       tex-countriesofeurope = %{tl_version}
License:        LPPL
Summary:        A font with the images of the countries of Europe
Version:        svn26042.0.21

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(keyval.sty)
Provides:       tex(CountriesOfEurope.enc) = %{tl_version}
Provides:       tex(CountriesOfEurope.map) = %{tl_version}
Provides:       tex(CountriesOfEurope.tfm) = %{tl_version}
Provides:       tex(CountriesOfEurope.pfb) = %{tl_version}
Provides:       tex(CountriesOfEurope.sty) = %{tl_version}

%description -n texlive-countriesofeurope
The bundle provides a font "CountriesOfEurope" (in Adobe Type 1
format) and the necessary metrics, together with LaTeX macros
for its use. The font provides glyphs with a filled outline of
the shape of each country; each glyph is at the same
cartographic scale.

%package -n texlive-countriesofeurope-doc
Summary:        Documentation for countriesofeurope
Version:        svn26042.0.21

Provides:       tex-countriesofeurope-doc
AutoReqProv:    No

%description -n texlive-countriesofeurope-doc
Documentation for countriesofeurope

%package -n texlive-courier-scaled
Provides:       tex-courier-scaled = %{tl_version}
License:        LPPL 1.2
Summary:        Provides a scaled Courier font
Version:        svn24940.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(8rpcrs.fd) = %{tl_version}, tex(couriers.sty) = %{tl_version}
Provides:       tex(il2pcrs.fd) = %{tl_version}, tex(ly1pcrs.fd) = %{tl_version}
Provides:       tex(omlpcrs.fd) = %{tl_version}, tex(omspcrs.fd) = %{tl_version}
Provides:       tex(ot1pcrs.fd) = %{tl_version}, tex(t1pcrs.fd) = %{tl_version}
Provides:       tex(t5pcrs.fd) = %{tl_version}, tex(ts1pcrs.fd) = %{tl_version}
Provides:       tex(xl2pcrs.fd) = %{tl_version}

%description -n texlive-courier-scaled
This package sets the default typewriter font to Courier with a
possible scale factor (in the same way as the helvet package
for Helvetica works for sans serif).

%package -n texlive-courier-scaled-doc
Summary:        Documentation for courier-scaled
Version:        svn24940.0

Provides:       tex-courier-scaled-doc
AutoReqProv:    No

%description -n texlive-courier-scaled-doc
Documentation for courier-scaled

%package -n texlive-collection-fontsrecommended
Summary:        Recommended fonts
Version:        svn35830.0
Requires:       texlive-base, texlive-collection-basic, tex-avantgar, tex-bookman
Requires:       tex-charter, tex-cm-super, tex-cmextra, tex-courier
Requires:       tex-ec, tex-euro, texlive-euro-ce, tex-eurosym
Requires:       tex-fpl, tex-helvetic, tex-lm, tex-lm-math
Requires:       tex-marvosym, tex-mathpazo, tex-manfnt-font, tex-mflogo-font
Requires:       tex-ncntrsbk, tex-palatino, tex-pxfonts, tex-rsfs
Requires:       tex-symbol, tex-tex-gyre, tex-tex-gyre-math, tex-times
Requires:       tex-tipa, tex-txfonts, tex-utopia, tex-wasy
Requires:       tex-wasy2-ps, tex-wasysym, tex-zapfchan, tex-zapfding
Provides:       tetex-fonts = 3.1-99
Obsoletes:      tetex-fonts < 3.1-99
Provides:       texlive-texmf-fonts = %{tl_version}
Obsoletes:      texlive-texmf-fonts < %{tl_version}

%description -n texlive-collection-fontsrecommended
Recommended fonts, including the base 35 PostScript fonts,
Latin Modern, TeX Gyre, and T1 and other encoding support for
Computer Modern, in outline form.

%package -n texlive-courier
Provides:       tex-courier = %{tl_version}
License:        GPL+
Summary:        URW "Base 35" font pack for LaTeX
Version:        svn35058.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(ucr.map) = %{tl_version}, tex(pcrb.tfm) = %{tl_version}
Provides:       tex(pcrb7t.tfm) = %{tl_version}, tex(pcrb8c.tfm) = %{tl_version}
Provides:       tex(pcrb8r.tfm) = %{tl_version}, tex(pcrb8t.tfm) = %{tl_version}
Provides:       tex(pcrbc.tfm) = %{tl_version}, tex(pcrbc7t.tfm) = %{tl_version}
Provides:       tex(pcrbc8t.tfm) = %{tl_version}, tex(pcrbo.tfm) = %{tl_version}
Provides:       tex(pcrbo7t.tfm) = %{tl_version}, tex(pcrbo8c.tfm) = %{tl_version}
Provides:       tex(pcrbo8r.tfm) = %{tl_version}, tex(pcrbo8t.tfm) = %{tl_version}
Provides:       tex(pcrr.tfm) = %{tl_version}, tex(pcrr7t.tfm) = %{tl_version}
Provides:       tex(pcrr8c.tfm) = %{tl_version}, tex(pcrr8r.tfm) = %{tl_version}
Provides:       tex(pcrr8t.tfm) = %{tl_version}, tex(pcrrc.tfm) = %{tl_version}
Provides:       tex(pcrrc7t.tfm) = %{tl_version}, tex(pcrrc8t.tfm) = %{tl_version}
Provides:       tex(pcrro.tfm) = %{tl_version}, tex(pcrro7t.tfm) = %{tl_version}
Provides:       tex(pcrro8c.tfm) = %{tl_version}, tex(pcrro8r.tfm) = %{tl_version}
Provides:       tex(pcrro8t.tfm) = %{tl_version}, tex(ucrb7t.tfm) = %{tl_version}
Provides:       tex(ucrb8c.tfm) = %{tl_version}, tex(ucrb8r.tfm) = %{tl_version}
Provides:       tex(ucrb8t.tfm) = %{tl_version}, tex(ucrbc7t.tfm) = %{tl_version}
Provides:       tex(ucrbc8t.tfm) = %{tl_version}, tex(ucrbo7t.tfm) = %{tl_version}
Provides:       tex(ucrbo8c.tfm) = %{tl_version}, tex(ucrbo8r.tfm) = %{tl_version}
Provides:       tex(ucrbo8t.tfm) = %{tl_version}, tex(ucrr7t.tfm) = %{tl_version}
Provides:       tex(ucrr8c.tfm) = %{tl_version}, tex(ucrr8r.tfm) = %{tl_version}
Provides:       tex(ucrr8t.tfm) = %{tl_version}, tex(ucrrc7t.tfm) = %{tl_version}
Provides:       tex(ucrrc8t.tfm) = %{tl_version}, tex(ucrro7t.tfm) = %{tl_version}
Provides:       tex(ucrro8c.tfm) = %{tl_version}, tex(ucrro8r.tfm) = %{tl_version}
Provides:       tex(ucrro8t.tfm) = %{tl_version}, tex(pcrb8a.pfb) = %{tl_version}
Provides:       tex(pcrbi8a.pfb) = %{tl_version}, tex(pcrbo8a.pfb) = %{tl_version}
Provides:       tex(pcri8a.pfb) = %{tl_version}, tex(pcrr8a.pfb) = %{tl_version}
Provides:       tex(pcrro8a.pfb) = %{tl_version}, tex(ucrb8a.pfb) = %{tl_version}
Provides:       tex(ucrbo8a.pfb) = %{tl_version}, tex(ucrr8a.pfb) = %{tl_version}
Provides:       tex(ucrro8a.pfb) = %{tl_version}, tex(pcrb.vf) = %{tl_version}
Provides:       tex(pcrb7t.vf) = %{tl_version}, tex(pcrb8c.vf) = %{tl_version}
Provides:       tex(pcrb8t.vf) = %{tl_version}, tex(pcrbc.vf) = %{tl_version}
Provides:       tex(pcrbc7t.vf) = %{tl_version}, tex(pcrbc8t.vf) = %{tl_version}
Provides:       tex(pcrbo.vf) = %{tl_version}, tex(pcrbo7t.vf) = %{tl_version}
Provides:       tex(pcrbo8c.vf) = %{tl_version}, tex(pcrbo8t.vf) = %{tl_version}
Provides:       tex(pcrr.vf) = %{tl_version}, tex(pcrr7t.vf) = %{tl_version}
Provides:       tex(pcrr8c.vf) = %{tl_version}, tex(pcrr8t.vf) = %{tl_version}
Provides:       tex(pcrrc.vf) = %{tl_version}, tex(pcrrc7t.vf) = %{tl_version}
Provides:       tex(pcrrc8t.vf) = %{tl_version}, tex(pcrro.vf) = %{tl_version}
Provides:       tex(pcrro7t.vf) = %{tl_version}, tex(pcrro8c.vf) = %{tl_version}
Provides:       tex(pcrro8t.vf) = %{tl_version}, tex(ucrb7t.vf) = %{tl_version}
Provides:       tex(ucrb8c.vf) = %{tl_version}, tex(ucrb8t.vf) = %{tl_version}
Provides:       tex(ucrbc7t.vf) = %{tl_version}, tex(ucrbc8t.vf) = %{tl_version}
Provides:       tex(ucrbo7t.vf) = %{tl_version}, tex(ucrbo8c.vf) = %{tl_version}
Provides:       tex(ucrbo8t.vf) = %{tl_version}, tex(ucrr7t.vf) = %{tl_version}
Provides:       tex(ucrr8c.vf) = %{tl_version}, tex(ucrr8t.vf) = %{tl_version}
Provides:       tex(ucrrc7t.vf) = %{tl_version}, tex(ucrrc8t.vf) = %{tl_version}
Provides:       tex(ucrro7t.vf) = %{tl_version}, tex(ucrro8c.vf) = %{tl_version}
Provides:       tex(ucrro8t.vf) = %{tl_version}, tex(8rucr.fd) = %{tl_version}
Provides:       tex(omlucr.fd) = %{tl_version}, tex(omsucr.fd) = %{tl_version}
Provides:       tex(ot1ucr.fd) = %{tl_version}, tex(t1ucr.fd) = %{tl_version}
Provides:       tex(ts1ucr.fd) = %{tl_version}

%description -n texlive-courier
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: Century Schoolbook (substituting for
Adobe's New Century Schoolbook); Dingbats (substituting for
Adobe's Zapf Dingbats); Nimbus Mono L (substituting for Abobe's
Courier); Nimbus Roman No9 L (substituting for Adobe's Times);
Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW
Chancery L Medium Italic (substituting for Adobe's Zapf
Chancery); URW Gothic L Book (substituting for Adobe's Avant
Garde); and URW Palladio L (substituting for Adobe's Palatino).

%package -n texlive-collection-fontutils
Summary:        Graphics and font utilities
Version:        svn37105.0
Requires:       texlive-base, texlive-collection-basic, tex-accfonts, tex-afm2pl
Requires:       tex-dosepsbin, tex-epstopdf, tex-fontware, tex-lcdftypetools
Requires:       tex-ps2pk, tex-pstools, tex-dvipsconfig, tex-fontinst
Requires:       tex-fontools, tex-mf2pt1, tex-ttfutils, t1utils, psutils

%description -n texlive-collection-fontutils
Programs for conversion between font formats, testing fonts,
virtual fonts, .gf and .pk manipulation, mft, fontinst, etc.
Manipulating OpenType, TrueType, Type 1,and for manipulation of
PostScript and other image formats.

%package -n texlive-collection-formatsextra
Summary:        Additional formats
Version:        svn44177
Provides:       texlive-collection-htmlxml = %{epoch}:svn35743.0.obsolete
Obsoletes:      texlive-collection-htmlxml <= 6:svn35743.0
Provides:       texlive-collection-omega = %{epoch}:svn30388.0.obsolete
Obsoletes:      texlive-collection-omega <= 6:svn30388.0
Requires:       texlive-aleph, texlive-antomega, texlive-base, texlive-collection-basic
Requires:       texlive-collection-latex, texlive-edmac, texlive-eplain, texlive-jadetex
Requires:       texlive-lambda, texlive-lollipop, texlive-mltex, texlive-mxedruli
Requires:       texlive-omega, texlive-omegaware, texlive-otibet, texlive-passivetex
Requires:       texlive-psizzl, texlive-startex, texlive-texsis, texlive-xmltex
Requires:       texlive-xmltexconfig

%description -n texlive-collection-formatsextra
Collected TeX `formats', i.e., large-scale macro packages
designed to be dumped into .fmt files -- excluding the most
common ones, such as latex and context, which have their own
package(s).

%package -n texlive-collection-games
Summary:        Games typesetting
Version:        svn47828
Requires:       texlive-base, texlive-collection-latex, texlive-bartel-chess-fonts, texlive-chess
Requires:       texlive-chess-problem-diagrams, texlive-chessboard
Requires:       texlive-chessfss, texlive-crossword, texlive-crosswrd, texlive-egameps
Requires:       texlive-gamebook, texlive-go, texlive-hanoi, texlive-havannah
Requires:       texlive-hexgame, texlive-horoscop, texlive-labyrinth, texlive-logicpuzzle
Requires:       texlive-musikui, texlive-onedown, texlive-othello, texlive-othelloboard
Requires:       texlive-pas-crosswords, texlive-psgo, texlive-reverxii-doc, texlive-rubik
Requires:       texlive-schwalbe-chess, texlive-sgame, texlive-skak, texlive-skaknew
Requires:       texlive-soup, texlive-sudoku, texlive-sudokubundle, texlive-xq
Requires:       texlive-xskak

%description -n texlive-collection-games
Setups for typesetting various games, including chess.

%package -n texlive-colorsep
Provides:       tex-colorsep = %{tl_version}
License:        Public Domain
Summary:        Color separation
Version:        svn13293.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-colorsep
Support for colour separation when using dvips.

%package -n texlive-collection-humanities
Summary:        Humanities packages
Version:        svn45363
Requires:       texlive-base, texlive-collection-latex, texlive-adtrees, texlive-bibleref
Requires:       texlive-bibleref-lds, texlive-bibleref-mouth
Requires:       texlive-bibleref-parse, texlive-covington
Requires:       texlive-diadia, texlive-dramatist, texlive-dvgloss, texlive-ecltree
Requires:       texlive-edfnotes, texlive-ednotes, texlive-eledform, texlive-eledmac
Requires:       texlive-expex, texlive-gb4e, texlive-gmverse, texlive-jura
Requires:       texlive-juraabbrev, texlive-juramisc, texlive-jurarsp, texlive-ledmac
Requires:       texlive-lexikon, texlive-lexref, texlive-ling-macros, texlive-linguex
Requires:       texlive-liturg, texlive-metrix, texlive-parallel, texlive-parrun
Requires:       texlive-phonrule, texlive-plari, texlive-play, texlive-poemscol
Requires:       texlive-poetry, texlive-poetrytex, texlive-qobitree, texlive-qtree
Requires:       texlive-reledmac, texlive-rrgtrees, texlive-rtklage, texlive-screenplay
Requires:       texlive-screenplay-pkg, texlive-sides, texlive-stage, texlive-textglos
Requires:       texlive-thalie, texlive-tree-dvips, texlive-verse, texlive-xyling

%description -n texlive-collection-humanities
Packages for law, linguistics, social sciences, humanities,
etc.

%package -n texlive-covington
Provides:       tex-covington = %{tl_version}
License:        Public Domain
Summary:        Linguistic support
Version:        svn44501
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(covington.sty) = %{tl_version}

%description -n texlive-covington
Numerous minor LaTeX enhancements for linguistics, including
multiple accents on the same letter, interline glosses (word-by-
word translations), Discourse Representation Structures, and
example numbering.

%package -n texlive-covington-doc
Summary:        Documentation for covington
Version:        svn44501
Provides:       tex-covington-doc
AutoReqProv:    No

%description -n texlive-covington-doc
Documentation for covington

%package -n texlive-collection-langarabic
Summary:        Arabic
Version:        svn47518
Requires:       texlive-base, texlive-collection-basic, texlive-alkalami, texlive-amiri
Requires:       texlive-arabi, texlive-arabi-add, texlive-arabluatex, texlive-arabtex
Requires:       texlive-bidi, texlive-bidihl, texlive-dad, texlive-ghab
Requires:       texlive-hyphen-arabic, texlive-hyphen-farsi
Requires:       texlive-imsproc, texlive-kurdishlipsum, texlive-lshort-persian-doc, texlive-luabidi
Requires:       texlive-na-box, texlive-persian-bib, texlive-sexam, texlive-simurgh
Requires:       texlive-tram, texlive-xepersian

%description -n texlive-collection-langarabic
Support for Arabic and Persian.

%package -n texlive-collection-langchinese
Summary:        Chinese
Version:        svn47408
Requires:       texlive-base, texlive-collection-langcjk
Requires:       texlive-arphic, texlive-arphic-ttf, texlive-asymptote-by-example-zh-cn-doc, texlive-asymptote-faq-zh-cn-doc
Requires:       texlive-asymptote-manual-zh-cn-doc, texlive-cns
Requires:       texlive-ctex, texlive-ctex-faq-doc, texlive-fandol, texlive-fduthesis
Requires:       texlive-hyphen-chinese, texlive-impatient-cn-doc
Requires:       texlive-latex-notes-zh-cn-doc, texlive-lshort-chinese-doc
Requires:       texlive-pgfornament-han, texlive-texlive-zh-cn-doc
Requires:       texlive-texproposal-doc, texlive-upzhkinsoku
Requires:       texlive-xpinyin, texlive-xtuthesis, texlive-zhlipsum, texlive-zhmetrics
Requires:       texlive-zhmetrics-uptex, texlive-zhnumber
Requires:       texlive-zhspacing

%description -n texlive-collection-langchinese
Support for Chinese; additional packages in collection-langcjk.

%package -n texlive-collection-langcjk
Summary:        Chinese/Japanese/Korean (base)
Version:        svn45194
Requires:       texlive-base, texlive-collection-basic, texlive-adobemapping, texlive-c90
Requires:       texlive-cjk, texlive-cjkpunct, texlive-cjkutils, texlive-dnp
Requires:       texlive-fixjfm, texlive-garuda-c90, texlive-jfmutil, texlive-norasi-c90
Requires:       texlive-pxtatescale, texlive-xcjk2uni, texlive-zxjafont
Provides:       tex(japanese) = %{tl_version}, tex(east-asian) = %{tl_version}
Obsoletes:      texlive-east-asian < %{tl_version}, texlive-texmf-east-asian < %{tl_version}

%description -n texlive-collection-langcjk
Packages supporting a combination of Chinese, Japanese, Korean,
including macros, fonts, documentation.  Also Thai in the c90
encoding, since there is some overlap in those fonts; standard
Thai support is in collection-langother.  Additional packages
for CJK are in their individual language collections.

%package -n texlive-collection-langcyrillic
Summary:        Cyrillic
Version:        svn44895
Requires:       texlive-base, texlive-collection-basic, texlive-collection-latex, texlive-babel-belarusian
Requires:       texlive-babel-bulgarian, texlive-babel-russian
Requires:       texlive-babel-serbian, texlive-babel-serbianc
Requires:       texlive-babel-ukrainian, texlive-churchslavonic
Requires:       texlive-cmcyr, texlive-cyrillic, texlive-cyrillic-bin, texlive-cyrplain
Requires:       texlive-disser, texlive-eskd, texlive-eskdx, texlive-gost
Requires:       texlive-hyphen-belarusian, texlive-hyphen-bulgarian
Requires:       texlive-hyphen-churchslavonic, texlive-hyphen-mongolian
Requires:       texlive-hyphen-russian, texlive-hyphen-serbian
Requires:       texlive-hyphen-ukrainian, texlive-lcyw, texlive-lh, texlive-lhcyr
Requires:       texlive-lshort-bulgarian-doc, texlive-lshort-mongol-doc
Requires:       texlive-lshort-russian-doc, texlive-lshort-ukr-doc
Requires:       texlive-mongolian-babel, texlive-montex, texlive-mpman-ru-doc, texlive-numnameru
Requires:       texlive-pst-eucl-translation-bg-doc, texlive-ruhyphen
Requires:       texlive-russ, texlive-serbian-apostrophe
Requires:       texlive-serbian-date-lat, texlive-serbian-def-cyr
Requires:       texlive-serbian-lig, texlive-t2, texlive-texlive-ru-doc, texlive-texlive-sr-doc
Requires:       texlive-ukrhyph

%description -n texlive-collection-langcyrillic
Support for Cyrillic scripts (Bulgarian, Russian, Serbian,
Ukrainian), even if Latin alphabets may also be used.


%package -n texlive-collection-langczechslovak
Summary:        Czech/Slovak
Version:        svn32550.0
Requires:       texlive-base, texlive-collection-basic, texlive-collection-latex, tex-babel-czech
Requires:       tex-babel-slovak, tex-cnbwp, tex-cs, tex-csbulletin
Requires:       tex-cslatex, tex-csplain, texlive-cstex-doc, tex-hyphen-czech
Requires:       tex-hyphen-slovak, tex-vlna, texlive-lshort-czech-doc, texlive-lshort-slovak-doc
Requires:       texlive-texlive-cz-doc

%description -n texlive-collection-langczechslovak
Support for Czech/Slovak.

%package -n texlive-collection-langenglish
Summary:        US and UK English
Version:        svn46126
Requires:       texlive-base, texlive-collection-basic, texlive-hyphen-english, texlive-FAQ-en-doc
Requires:       texlive-MemoirChapStyles-doc, texlive-Type1fonts-doc
Requires:       texlive-amscls-doc, texlive-amslatex-primer-doc
Requires:       texlive-around-the-bend-doc, texlive-ascii-chart-doc
Requires:       texlive-biblatex-cheatsheet-doc, texlive-components-of-TeX-doc
Requires:       texlive-comprehensive-doc, texlive-dickimaw-doc
Requires:       texlive-docsurvey-doc, texlive-dtxtut-doc
Requires:       texlive-first-latex-doc-doc, texlive-forest-quickstart-doc
Requires:       texlive-gentle-doc, texlive-guide-to-latex-doc
Requires:       texlive-happy4th-doc, texlive-impatient-doc
Requires:       texlive-intro-scientific-doc, texlive-knuth-doc
Requires:       texlive-l2tabu-english-doc, texlive-latex-brochure-doc
Requires:       texlive-latex-course-doc, texlive-latex-doc-ptr-doc
Requires:       texlive-latex-graphics-companion-doc, texlive-latex-refsheet-doc
Requires:       texlive-latex-veryshortguide-doc, texlive-latex-web-companion-doc
Requires:       texlive-latex2e-help-texinfo, texlive-latex4wp-doc
Requires:       texlive-latexcheat-doc, texlive-latexcourse-rug-doc
Requires:       texlive-latexfileinfo-pkgs, texlive-lshort-english-doc
Requires:       texlive-macros2e-doc, texlive-math-e-doc
Requires:       texlive-math-into-latex-4-doc, texlive-maths-symbols-doc
Requires:       texlive-memdesign-doc, texlive-metafont-beginners-doc
Requires:       texlive-metapost-examples-doc, texlive-patgen2-tutorial-doc
Requires:       texlive-pictexsum-doc, texlive-plain-doc-doc
Requires:       texlive-presentations-en-doc, texlive-short-math-guide
Requires:       texlive-simplified-latex-doc, texlive-svg-inkscape-doc
Requires:       texlive-tabulars-e-doc, texlive-tamethebeast-doc
Requires:       texlive-tds-doc, texlive-tex-font-errors-cheatsheet-doc
Requires:       texlive-tex-overview-doc, texlive-tex-refs-doc
Requires:       texlive-texbytopic-doc, texlive-titlepages-doc
Requires:       texlive-tlc2-doc, texlive-undergradmath-doc
Requires:       texlive-visualfaq-doc, texlive-webguide-doc
Requires:       texlive-xetexref-doc

%description -n texlive-collection-langenglish
Support for (and documentation in) English.

%package -n texlive-components-of-TeX-doc
Summary:        Documentation for components-of-TeX
Version:        svn15878.0

Provides:       tex-components-of-TeX-doc
AutoReqProv:    No

%description -n texlive-components-of-TeX-doc
Documentation for components-of-TeX

%package -n texlive-comprehensive-doc
Summary:        Documentation for comprehensive
Version:        svn43001
Provides:       tex-comprehensive-doc
AutoReqProv:    No

%description -n texlive-comprehensive-doc
Documentation for comprehensive

%package -n texlive-collection-langeuropean
Summary:        Other European languages
Version:        svn46803
Requires:       texlive-base, texlive-collection-basic, texlive-armtex, texlive-babel-albanian
Requires:       texlive-babel-bosnian, texlive-babel-breton
Requires:       texlive-babel-croatian, texlive-babel-danish
Requires:       texlive-babel-dutch, texlive-babel-estonian
Requires:       texlive-babel-finnish, texlive-babel-friulan
Requires:       texlive-babel-hungarian, texlive-babel-icelandic
Requires:       texlive-babel-irish, texlive-babel-kurmanji
Requires:       texlive-babel-latin, texlive-babel-latvian
Requires:       texlive-babel-macedonian, texlive-babel-norsk
Requires:       texlive-babel-occitan, texlive-babel-piedmontese
Requires:       texlive-babel-romanian, texlive-babel-romansh
Requires:       texlive-babel-samin, texlive-babel-scottish
Requires:       texlive-babel-slovenian, texlive-babel-swedish
Requires:       texlive-babel-turkish, texlive-babel-welsh
Requires:       texlive-finbib, texlive-gloss-occitan, texlive-hrlatex, texlive-hulipsum
Requires:       texlive-hyphen-croatian, texlive-hyphen-danish
Requires:       texlive-hyphen-dutch, texlive-hyphen-estonian
Requires:       texlive-hyphen-finnish, texlive-hyphen-friulan
Requires:       texlive-hyphen-hungarian, texlive-hyphen-icelandic
Requires:       texlive-hyphen-irish, texlive-hyphen-kurmanji
Requires:       texlive-hyphen-latin, texlive-hyphen-latvian
Requires:       texlive-hyphen-lithuanian, texlive-hyphen-norwegian
Requires:       texlive-hyphen-occitan, texlive-hyphen-piedmontese
Requires:       texlive-hyphen-romanian, texlive-hyphen-romansh
Requires:       texlive-hyphen-slovenian, texlive-hyphen-swedish
Requires:       texlive-hyphen-turkish, texlive-hyphen-uppersorbian
Requires:       texlive-hyphen-welsh, texlive-lithuanian
Requires:       texlive-lshort-dutch-doc, texlive-lshort-estonian-doc
Requires:       texlive-lshort-finnish-doc, texlive-lshort-slovenian-doc
Requires:       texlive-lshort-turkish-doc, texlive-nevelok
Requires:       texlive-swebib, texlive-turkmen

%description -n texlive-collection-langeuropean
Support for a number of European languages; others (Greek,
German, French, ...) have their own collections, depending
simply on the size of the support.

%package -n texlive-collection-langfrench
Summary:        French
Version:        svn40375
Requires:       texlive-base, texlive-collection-basic, tex-aeguill, texlive-apprends-latex-doc
Requires:       tex-babel-basque, tex-babel-french, tex-basque-book, tex-basque-date
Requires:       tex-bib-fr, tex-bibleref-french, texlive-booktabs-fr-doc, tex-droit-fr
Requires:       tex-e-french, texlive-epslatex-fr-doc, tex-facture, texlive-formation-latex-ul
Requires:       tex-frletter, tex-hyphen-basque, tex-hyphen-french, texlive-impatient-fr-doc
Requires:       tex-impnattypo, texlive-l2tabu-french-doc
Requires:       tex-latex2e-help-texinfo-fr-doc, texlive-lshort-french-doc
Requires:       tex-mafr, tex-tabvar, tex-tdsfrmath, texlive-texlive-fr-doc
Requires:       texlive-translation-array-fr-doc, texlive-translation-dcolumn-fr-doc
Requires:       texlive-translation-natbib-fr-doc, texlive-translation-tabbing-fr-doc
Requires:       tex-variations, tex-visualtikz-doc

%description -n texlive-collection-langfrench
Support for French and Basque.

%package -n texlive-collection-langgerman
Summary:        German
Version:        svn44952
Requires:       texlive-base, texlive-collection-basic, texlive-apalike-german, texlive-babel-german
Requires:       texlive-bibleref-german, texlive-booktabs-de-doc
Requires:       texlive-csquotes-de-doc, texlive-dehyph-exptl
Requires:       texlive-dhua, texlive-einfuehrung-doc, texlive-einfuehrung2-doc, texlive-etdipa-doc
Requires:       texlive-etoolbox-de-doc, texlive-fifinddo-info-doc
Requires:       texlive-geometry-de-doc, texlive-german, texlive-germbib, texlive-germkorr
Requires:       texlive-hausarbeit-jura, texlive-hyphen-german
Requires:       texlive-koma-script-examples-doc, texlive-l2picfaq-doc
Requires:       texlive-l2tabu-doc, texlive-latex-bib-ex-doc
Requires:       texlive-latex-bib2-ex-doc, texlive-latex-referenz-doc
Requires:       texlive-latex-tabellen-doc, texlive-latexcheat-de-doc
Requires:       texlive-lshort-german-doc, texlive-lualatex-doc-de-doc
Requires:       texlive-microtype-de-doc, texlive-milog, texlive-presentations-doc, texlive-r_und_s
Requires:       texlive-templates-fenn-doc, texlive-templates-sommer-doc
Requires:       texlive-termcal-de, texlive-texlive-de-doc
Requires:       texlive-tipa-de-doc, texlive-translation-arsclassica-de-doc
Requires:       texlive-translation-biblatex-de-doc, texlive-translation-chemsym-de-doc
Requires:       texlive-translation-ecv-de-doc, texlive-translation-enumitem-de-doc
Requires:       texlive-translation-europecv-de-doc, texlive-translation-filecontents-de-doc
Requires:       texlive-translation-moreverb-de-doc, texlive-udesoftec
Requires:       texlive-uhrzeit, texlive-umlaute, texlive-voss-mathcol-doc

%description -n texlive-collection-langgerman
Support for German.

%package -n texlive-collection-langgreek
Summary:        Greek
Version:        svn44192
Requires:       texlive-base, texlive-collection-basic, texlive-babel-greek, texlive-begingreek
Requires:       texlive-betababel, texlive-bgreek, texlive-cbfonts, texlive-cbfonts-fd
Requires:       texlive-gfsbaskerville, texlive-gfsporson
Requires:       texlive-greek-fontenc, texlive-greek-inputenc
Requires:       texlive-greekdates, texlive-greektex, texlive-greektonoi, texlive-hyphen-greek
Requires:       texlive-hyphen-ancientgreek, texlive-ibycus-babel
Requires:       texlive-ibygrk, texlive-kerkis, texlive-levy, texlive-lgreek
Requires:       texlive-mkgrkindex, texlive-teubner, texlive-xgreek, texlive-yannisgr

%description -n texlive-collection-langgreek
Support for Greek.

%package -n texlive-collection-langkorean
Summary:        Korean
Version:        svn42106
Requires:       texlive-base, texlive-baekmuk, texlive-cjk-ko, texlive-collection-langcjk
Requires:       texlive-kotex-oblivoir, texlive-kotex-plain
Requires:       texlive-kotex-utf, texlive-kotex-utils, texlive-lshort-korean-doc, texlive-nanumtype1
Requires:       texlive-uhc, texlive-unfonts-core, texlive-unfonts-extra

%description -n texlive-collection-langkorean
Support for Korean; additional packages in collection-langcjk.

Provides:       tex(nanummjmad.pfb) = %{tl_version}, tex(nanummjmae.pfb) = %{tl_version}
Provides:       tex(nanummjmaf.pfb) = %{tl_version}, tex(nanummjmb0.pfb) = %{tl_version}
Provides:       tex(nanummjmb1.pfb) = %{tl_version}, tex(nanummjmb2.pfb) = %{tl_version}
Provides:       tex(nanummjmb3.pfb) = %{tl_version}, tex(nanummjmb4.pfb) = %{tl_version}
Provides:       tex(nanummjmb5.pfb) = %{tl_version}, tex(nanummjmb6.pfb) = %{tl_version}
Provides:       tex(nanummjmb7.pfb) = %{tl_version}, tex(nanummjmb8.pfb) = %{tl_version}
Provides:       tex(nanummjmb9.pfb) = %{tl_version}, tex(nanummjmba.pfb) = %{tl_version}
Provides:       tex(nanummjmbb.pfb) = %{tl_version}, tex(nanummjmbc.pfb) = %{tl_version}
Provides:       tex(nanummjmbd.pfb) = %{tl_version}, tex(nanummjmbe.pfb) = %{tl_version}
Provides:       tex(nanummjmbf.pfb) = %{tl_version}, tex(nanummjmc0.pfb) = %{tl_version}
Provides:       tex(nanummjmc1.pfb) = %{tl_version}, tex(nanummjmc2.pfb) = %{tl_version}
Provides:       tex(nanummjmc3.pfb) = %{tl_version}, tex(nanummjmc4.pfb) = %{tl_version}
Provides:       tex(nanummjmc5.pfb) = %{tl_version}, tex(nanummjmc6.pfb) = %{tl_version}
Provides:       tex(nanummjmc7.pfb) = %{tl_version}, tex(nanummjmc8.pfb) = %{tl_version}
Provides:       tex(nanummjmc9.pfb) = %{tl_version}, tex(nanummjmca.pfb) = %{tl_version}
Provides:       tex(nanummjmcb.pfb) = %{tl_version}, tex(nanummjmcc.pfb) = %{tl_version}
Provides:       tex(nanummjmcd.pfb) = %{tl_version}, tex(nanummjmce.pfb) = %{tl_version}
Provides:       tex(nanummjmcf.pfb) = %{tl_version}, tex(nanummjmd0.pfb) = %{tl_version}
Provides:       tex(nanummjmd1.pfb) = %{tl_version}, tex(nanummjmd2.pfb) = %{tl_version}
Provides:       tex(nanummjmd3.pfb) = %{tl_version}, tex(nanummjmd4.pfb) = %{tl_version}
Provides:       tex(nanummjmd5.pfb) = %{tl_version}, tex(nanummjmd6.pfb) = %{tl_version}
Provides:       tex(nanummjmd7.pfb) = %{tl_version}, tex(nanummjmff.pfb) = %{tl_version}
Provides:       tex(t1nanumgtb.pfb) = %{tl_version}, tex(t1nanumgtm.pfb) = %{tl_version}
Provides:       tex(t1nanummjb.pfb) = %{tl_version}, tex(t1nanummjm.pfb) = %{tl_version}
Provides:       tex(ts1nanumgtb.vf) = %{tl_version}, tex(ts1nanumgtbo.vf) = %{tl_version}
Provides:       tex(ts1nanumgtm.vf) = %{tl_version}, tex(ts1nanumgtmo.vf) = %{tl_version}
Provides:       tex(ts1nanummjb.vf) = %{tl_version}, tex(ts1nanummjbo.vf) = %{tl_version}
Provides:       tex(ts1nanummjm.vf) = %{tl_version}, tex(ts1nanummjmo.vf) = %{tl_version}
Provides:       tex(c70nanumgt.fd) = %{tl_version}, tex(c70nanummj.fd) = %{tl_version}
Provides:       tex(c70uhcmj.fd) = %{tl_version}, tex(lucnanumgt.fd) = %{tl_version}
Provides:       tex(lucnanummj.fd) = %{tl_version}, tex(t1nanumgt.fd) = %{tl_version}
Provides:       tex(t1nanummj.fd) = %{tl_version}, tex(ts1nanumgt.fd) = %{tl_version}
Provides:       tex(ts1nanummj.fd) = %{tl_version}

%package -n texlive-collection-langother
Summary:        Other languages
Version:        svn46722
Provides:       texlive-collection-langafrica = svn30372.0.obsolete
Obsoletes:      texlive-collection-langafrica <= svn30372.0
Provides:       texlive-collection-langindic = svn35737.0.obsolete
Obsoletes:      texlive-collection-langindic <= svn35737.0
Requires:       texlive-base, texlive-collection-basic, texlive-amsldoc-vn-doc, texlive-aramaic-serto
Requires:       texlive-babel-azerbaijani, texlive-babel-esperanto
Requires:       texlive-babel-georgian, texlive-babel-hebrew
Requires:       texlive-babel-indonesian, texlive-babel-interlingua
Requires:       texlive-babel-malay, texlive-babel-sorbian
Requires:       texlive-babel-thai, texlive-babel-vietnamese
Requires:       texlive-bangtex, texlive-bengali, texlive-burmese, texlive-cjhebrew
Requires:       texlive-ctib, texlive-ebong, texlive-ethiop, texlive-ethiop-t1
Requires:       texlive-fc, texlive-fonts-tlwg, texlive-hyphen-afrikaans, texlive-hyphen-armenian
Requires:       texlive-hyphen-coptic, texlive-hyphen-esperanto
Requires:       texlive-hyphen-ethiopic, texlive-hyphen-georgian
Requires:       texlive-hyphen-indic, texlive-hyphen-indonesian
Requires:       texlive-hyphen-interlingua, texlive-hyphen-sanskrit
Requires:       texlive-hyphen-thai, texlive-hyphen-turkmen
Requires:       texlive-latex-mr-doc, texlive-latexbangla
Requires:       texlive-lshort-thai-doc, texlive-lshort-vietnamese-doc
Requires:       texlive-ntheorem-vn-doc, texlive-padauk, texlive-sanskrit, texlive-sanskrit-t1
Requires:       texlive-thaienum, texlive-thaispec, texlive-velthuis, texlive-vntex
Requires:       texlive-wnri, texlive-wnri-latex, texlive-xetex-devanagari

%description -n texlive-collection-langother
Support for languages not otherwise listed, including Thai,
Vietnamese, Hebrew, Indonesian, and plenty more.  The split is
made simply on the basis of the size of the support, to keep
both collection sizes and the number of collections reasonable.


%package -n texlive-collection-langpolish
Summary:        Polish
Version:        svn44371
Requires:       texlive-base, texlive-collection-latex, texlive-collection-basic, texlive-babel-polish
Requires:       texlive-bredzenie, texlive-cc-pl, texlive-gustlib, texlive-gustprog-doc
Requires:       texlive-hyphen-polish, texlive-lshort-polish-doc
Requires:       texlive-mex, texlive-mwcls, texlive-pl, texlive-polski
Requires:       texlive-przechlewski-book, texlive-qpxqtx
Requires:       texlive-tap, texlive-tex-virtual-academy-pl-doc
Requires:       texlive-texlive-pl-doc, texlive-utf8mex

%description -n texlive-collection-langpolish
Support for Polish.

%package -n texlive-collection-langportuguese
Summary:        Portuguese
Version:        svn47524
Requires:       texlive-base, texlive-collection-basic, tex-babel-portuges, texlive-beamer-tut-pt-doc
Requires:       texlive-cursolatex-doc, tex-feupphdteses
Requires:       tex-hyphen-portuguese, texlive-latex-via-exemplos
Requires:       texlive-latexcheat-ptbr-doc, texlive-lshort-portuguese-doc
Requires:       tex-ordinalpt, texlive-xypic-tut-pt-doc

%description -n texlive-collection-langportuguese
Support for Portuguese.

%package -n texlive-collection-langspanish
Summary:        Spanish
Version:        svn40587
Requires:       texlive-base, texlive-collection-basic, tex-babel-catalan, tex-babel-galician
Requires:       tex-babel-spanglish, tex-babel-spanish, texlive-es-tex-faq-doc, tex-hyphen-catalan
Requires:       tex-hyphen-galician, tex-hyphen-spanish, texlive-l2tabu-spanish-doc, tex-latex2e-help-texinfo-spanish
Requires:       texlive-latexcheat-esmx-doc, texlive-lshort-spanish-doc
Requires:       tex-spanish-mx, tex-texlive-es-doc

%description -n texlive-collection-langspanish
Support for Spanish.

%package -n texlive-collection-latexextra
Summary:        LaTeX additional packages
Version:        svn48313
Requires:       texlive-base, texlive-collection-latexrecommended
Requires:       texlive-collection-pictures, texlive-2up
Requires:       texlive-ESIEEcv, texlive-GS1, texlive-HA-prosper, texlive-Tabbing
Requires:       texlive-a0poster, texlive-a4wide, texlive-a5comb, texlive-abraces
Requires:       texlive-abstract, texlive-achemso, texlive-acro, texlive-acronym
Requires:       texlive-acroterm, texlive-actuarialangle
Requires:       texlive-actuarialsymbol, texlive-addfont
Requires:       texlive-addlines, texlive-adjmulticol, texlive-adjustbox, texlive-adrconv
Requires:       texlive-advdate, texlive-akktex, texlive-akletter, texlive-alertmessage
Requires:       texlive-alnumsec, texlive-alterqcm, texlive-altfont, texlive-amsaddr
Requires:       texlive-animate, texlive-anonchap, texlive-answers, texlive-anyfontsize
Requires:       texlive-appendix, texlive-appendixnumberbeamer
Requires:       texlive-apptools, texlive-arcs, texlive-arrayjobx, texlive-arraysort
Requires:       texlive-arydshln, texlive-assignment, texlive-assoccnt, texlive-attachfile
Requires:       texlive-aurl, texlive-authoraftertitle, texlive-authorarchive, texlive-authorindex
Requires:       texlive-autonum, texlive-autopdf, texlive-avremu, texlive-background
Requires:       texlive-bankstatement, texlive-bashful, texlive-basicarith, texlive-bchart
Requires:       texlive-beamer2thesis, texlive-beameraudience
Requires:       texlive-beamercolorthemeowl, texlive-beamerdarkthemes
Requires:       texlive-beamerposter, texlive-beamersubframe
Requires:       texlive-beamertheme-cuerna, texlive-beamertheme-detlevcm
Requires:       texlive-beamertheme-epyt, texlive-beamertheme-focus
Requires:       texlive-beamertheme-metropolis, texlive-beamertheme-phnompenh
Requires:       texlive-beamertheme-saintpetersburg, texlive-beamertheme-upenn-bc
Requires:       texlive-beamerthemejltree, texlive-beamerthemenirma
Requires:       texlive-beton, texlive-bewerbung, texlive-bez123, texlive-bezos
Requires:       texlive-bhcexam, texlive-bibletext, texlive-bigfoot, texlive-bigints
Requires:       texlive-biochemistry-colors, texlive-bizcard
Requires:       texlive-blindtext, texlive-blkarray, texlive-block, texlive-bnumexpr
Requires:       texlive-boites, texlive-bold-extra, texlive-bookcover, texlive-bookest
Requires:       texlive-booklet, texlive-boolexpr, texlive-bophook, texlive-boxedminipage
Requires:       texlive-boxedminipage2e, texlive-boxhandler
Requires:       texlive-bracketkey, texlive-braket, texlive-breakurl, texlive-bullcntr
Requires:       texlive-bussproofs, texlive-bxcalc, texlive-bxdpx-beamer, texlive-bxdvidriver
Requires:       texlive-bxenclose, texlive-bxnewfont, texlive-bxpapersize, texlive-bxpdfver
Requires:       texlive-calcage, texlive-calctab, texlive-calculator, texlive-calrsfs
Requires:       texlive-cals, texlive-calxxxx-yyyy, texlive-cancel, texlive-canoniclayout
Requires:       texlive-capt-of, texlive-captcont, texlive-captdef, texlive-carbohydrates
Requires:       texlive-cases, texlive-casyl, texlive-catchfilebetweentags, texlive-catechis
Requires:       texlive-catoptions, texlive-cbcoptic, texlive-ccaption, texlive-cclicenses
Requires:       texlive-cd, texlive-cd-cover, texlive-cdpbundl, texlive-cellprops
Requires:       texlive-cellspace, texlive-censor, texlive-changebar, texlive-changelayout
Requires:       texlive-changepage, texlive-changes, texlive-chappg, texlive-chapterfolder
Requires:       texlive-cheatsheet, texlive-chet, texlive-chextras, texlive-childdoc
Requires:       texlive-chkfloat, texlive-chletter, texlive-chngcntr, texlive-chronology
Requires:       texlive-circ, texlive-classics, texlive-classpack, texlive-clrdblpg
Requires:       texlive-clefval, texlive-cleveref, texlive-clipboard, texlive-clock
Requires:       texlive-cloze, texlive-clrstrip, texlive-cmdstring, texlive-cmdtrack
Requires:       texlive-cmsd, texlive-cnltx, texlive-cntformats, texlive-cntperchap
Requires:       texlive-codedoc, texlive-codepage, texlive-codesection, texlive-collcell
Requires:       texlive-collectbox, texlive-colordoc, texlive-colorinfo, texlive-coloring
Requires:       texlive-colorspace, texlive-colortab, texlive-colorwav, texlive-colorweb
Requires:       texlive-colourchange, texlive-combelow, texlive-combine, texlive-comma
Requires:       texlive-commado, texlive-comment, texlive-competences, texlive-concepts
Requires:       texlive-concprog, texlive-constants, texlive-continue, texlive-contour
Requires:       texlive-contracard, texlive-conv-xkv, texlive-cooking, texlive-cooking-units
Requires:       texlive-cool, texlive-coollist, texlive-coolstr, texlive-coolthms
Requires:       texlive-cooltooltips, texlive-coordsys, texlive-copyedit, texlive-copyrightbox
Requires:       texlive-coseoul, texlive-counttexruns, texlive-courseoutline, texlive-coursepaper
Requires:       texlive-coverpage, texlive-cprotect, texlive-crbox, texlive-crossreference
Requires:       texlive-crossreftools, texlive-csquotes, texlive-css-colors, texlive-csvsimple
Requires:       texlive-cuisine, texlive-currency, texlive-currfile, texlive-currvita
Requires:       texlive-cutwin, texlive-cv, texlive-cv4tw, texlive-cweb-latex
Requires:       texlive-cyber, texlive-cybercic, texlive-dashbox, texlive-dashrule
Requires:       texlive-dashundergaps, texlive-dataref, texlive-datatool, texlive-dateiliste
Requires:       texlive-datenumber, texlive-datetime, texlive-datetime2, texlive-datetime2-bahasai
Requires:       texlive-datetime2-basque, texlive-datetime2-breton
Requires:       texlive-datetime2-bulgarian, texlive-datetime2-catalan
Requires:       texlive-datetime2-croatian, texlive-datetime2-czech
Requires:       texlive-datetime2-danish, texlive-datetime2-dutch
Requires:       texlive-datetime2-en-fulltext, texlive-datetime2-english
Requires:       texlive-datetime2-esperanto, texlive-datetime2-estonian
Requires:       texlive-datetime2-finnish, texlive-datetime2-french
Requires:       texlive-datetime2-galician, texlive-datetime2-german
Requires:       texlive-datetime2-greek, texlive-datetime2-hebrew
Requires:       texlive-datetime2-icelandic, texlive-datetime2-irish
Requires:       texlive-datetime2-italian, texlive-datetime2-it-fulltext
Requires:       texlive-datetime2-latin, texlive-datetime2-lsorbian
Requires:       texlive-datetime2-magyar, texlive-datetime2-norsk
Requires:       texlive-datetime2-polish, texlive-datetime2-portuges
Requires:       texlive-datetime2-romanian, texlive-datetime2-russian
Requires:       texlive-datetime2-samin, texlive-datetime2-scottish
Requires:       texlive-datetime2-serbian, texlive-datetime2-slovak
Requires:       texlive-datetime2-slovene, texlive-datetime2-spanish
Requires:       texlive-datetime2-swedish, texlive-datetime2-turkish
Requires:       texlive-datetime2-ukrainian, texlive-datetime2-usorbian
Requires:       texlive-datetime2-welsh, texlive-dblfloatfix
Requires:       texlive-decimal, texlive-decorule, texlive-delimtxt, texlive-denisbdoc
Requires:       texlive-diagbox, texlive-diagnose, texlive-dialogl, texlive-dichokey
Requires:       texlive-dinbrief, texlive-directory, texlive-dirtytalk, texlive-dlfltxb
Requires:       texlive-dnaseq, texlive-doclicense, texlive-docmfp, texlive-docmute
Requires:       texlive-doctools, texlive-documentation, texlive-doi, texlive-dotarrow
Requires:       texlive-dotseqn, texlive-download, texlive-dox, texlive-dpfloat
Requires:       texlive-dprogress, texlive-drac, texlive-draftcopy, texlive-draftfigure
Requires:       texlive-draftwatermark, texlive-dtk, texlive-dtxdescribe, texlive-dtxgallery-doc
Requires:       texlive-ducksay, texlive-dvdcoll, texlive-dynamicnumber, texlive-dynblocks
Requires:       texlive-ean13isbn, texlive-easy, texlive-easy-todo, texlive-easyfig
Requires:       texlive-easyformat, texlive-easylist, texlive-easyreview, texlive-ebezier
Requires:       texlive-ecclesiastic, texlive-ecv, texlive-ed, texlive-edmargin
Requires:       texlive-eemeir, texlive-efbox, texlive-egplot, texlive-elements
Requires:       texlive-ellipsis, texlive-elmath, texlive-elocalloc, texlive-elpres
Requires:       texlive-elzcards, texlive-emarks, texlive-embedall, texlive-embrac
Requires:       texlive-emptypage, texlive-emulateapj, texlive-endfloat, texlive-endheads
Requires:       texlive-endnotes, texlive-engpron, texlive-engrec, texlive-enotez
Requires:       texlive-enumitem, texlive-enumitem-zref, texlive-envbig, texlive-environ
Requires:       texlive-envlab, texlive-epigraph, texlive-epiolmec, texlive-eqell
Requires:       texlive-eqlist, texlive-eqnalign, texlive-eqname, texlive-eqparbox
Requires:       texlive-errata, texlive-erw-l3, texlive-esami, texlive-esdiff
Requires:       texlive-esint, texlive-esint-type1, texlive-etaremune, texlive-etextools
Requires:       texlive-etoc, texlive-eukdate, texlive-eulerpx, texlive-europasscv
Requires:       texlive-europecv, texlive-everyhook, texlive-everypage, texlive-exam
Requires:       texlive-exam-n, texlive-examdesign, texlive-example, texlive-examplep
Requires:       texlive-exceltex, texlive-excludeonly, texlive-exercise, texlive-exercisebank
Requires:       texlive-exercises, texlive-exp-testopt, texlive-expdlist, texlive-export
Requires:       texlive-exsheets, texlive-exsol, texlive-extract, texlive-facsimile
Requires:       texlive-factura, texlive-fancylabel, texlive-fancynum, texlive-fancypar
Requires:       texlive-fancyslides, texlive-fancytabs, texlive-fancytooltips, texlive-fcolumn
Requires:       texlive-fetchcls, texlive-ffslides, texlive-fgruler, texlive-fibeamer
Requires:       texlive-fifo-stack, texlive-figsize, texlive-filecontents, texlive-filecontentsdef
Requires:       texlive-filedate, texlive-fileinfo, texlive-filemod, texlive-fink
Requires:       texlive-finstrut, texlive-fithesis, texlive-fixcmex, texlive-fixfoot
Requires:       texlive-fixme, texlive-fixmetodonotes, texlive-fjodor, texlive-flabels
Requires:       texlive-flacards, texlive-flagderiv, texlive-flashcards, texlive-flashmovie
Requires:       texlive-flipbook, texlive-flippdf, texlive-floatflt, texlive-floatrow
Requires:       texlive-flowfram, texlive-fmp, texlive-fmtcount, texlive-fn2end
Requires:       texlive-fnbreak, texlive-fncychap, texlive-fncylab, texlive-fnpara
Requires:       texlive-fnpct, texlive-fnumprint, texlive-foilhtml, texlive-fontaxes
Requires:       texlive-fonttable, texlive-footmisc, texlive-footmisx, texlive-footnotebackref
Requires:       texlive-footnotehyper, texlive-footnoterange
Requires:       texlive-footnpag, texlive-forarray, texlive-foreign, texlive-forloop
Requires:       texlive-formlett, texlive-forms16be, texlive-formular, texlive-fragments
Requires:       texlive-frame, texlive-framed, texlive-frankenstein, texlive-frege
Requires:       texlive-ftcap, texlive-ftnxtra, texlive-fullblck, texlive-fullminipage
Requires:       texlive-fullwidth, texlive-fundus-calligra
Requires:       texlive-fundus-cyr, texlive-fundus-sueterlin
Requires:       texlive-fvextra, texlive-fwlw, texlive-g-brief, texlive-gatherenum
Requires:       texlive-gauss, texlive-gcard, texlive-gcite, texlive-gender
Requires:       texlive-genmpage, texlive-getfiledate, texlive-getitems, texlive-ginpenc
Requires:       texlive-gitfile-info, texlive-gitinfo, texlive-gitinfo2, texlive-gitlog
Requires:       texlive-gloss, texlive-glossaries, texlive-glossaries-danish, texlive-glossaries-dutch
Requires:       texlive-glossaries-english, texlive-glossaries-extra
Requires:       texlive-glossaries-finnish, texlive-glossaries-french
Requires:       texlive-glossaries-german, texlive-glossaries-irish
Requires:       texlive-glossaries-italian, texlive-glossaries-magyar
Requires:       texlive-glossaries-polish, texlive-glossaries-portuges
Requires:       texlive-glossaries-serbian, texlive-glossaries-spanish
Requires:       texlive-gmdoc, texlive-gmdoc-enhance, texlive-gmiflink, texlive-gmutils
Requires:       texlive-gmverb, texlive-graphbox, texlive-graphicx-psmin, texlive-graphicxbox
Requires:       texlive-grayhints, texlive-grfpaste, texlive-grid, texlive-grid-system
Requires:       texlive-gridset, texlive-guitlogo, texlive-halloweenmath, texlive-hackthefootline
Requires:       texlive-handin, texlive-handout, texlive-hang, texlive-hanging
Requires:       texlive-hardwrap, texlive-harnon-cv, texlive-harpoon, texlive-hc
Requires:       texlive-he-she, texlive-hhtensor, texlive-histogr, texlive-hitec
Requires:       texlive-hletter, texlive-hpsdiss, texlive-hrefhide, texlive-hvindex
Requires:       texlive-hypdvips, texlive-hyper, texlive-hyperbar, texlive-hypernat
Requires:       texlive-hyperxmp, texlive-hyphenat, texlive-idxcmds, texlive-idxlayout
Requires:       texlive-iffont, texlive-ifmslide, texlive-ifmtarg, texlive-ifnextok
Requires:       texlive-ifoddpage, texlive-ifplatform, texlive-ifthenx, texlive-iitem
Requires:       texlive-image-gallery, texlive-imakeidx, texlive-import, texlive-incgraph
Requires:       texlive-indextools, texlive-inlinedef, texlive-inputtrc, texlive-interactiveworkbook
Requires:       texlive-interfaces, texlive-intopdf, texlive-inversepath, texlive-invoice
Requires:       texlive-invoice2, texlive-iso, texlive-iso10303, texlive-isodate
Requires:       texlive-isodoc, texlive-isonums, texlive-isopt, texlive-isorot
Requires:       texlive-isotope, texlive-issuulinks, texlive-iwhdp, texlive-jlabels
Requires:       texlive-jslectureplanner, texlive-jumplines
Requires:       texlive-jvlisting, texlive-kantlipsum, texlive-kerntest, texlive-keycommand
Requires:       texlive-keyfloat, texlive-keyreader, texlive-keystroke, texlive-keyval2e
Requires:       texlive-keyvaltable, texlive-kix, texlive-knowledge, texlive-koma-moderncvclassic
Requires:       texlive-koma-script-sfs, texlive-komacv, texlive-komacv-rg, texlive-ktv-texdata
Requires:       texlive-l3build, texlive-labbook, texlive-labels, texlive-labelschanged
Requires:       texlive-lastpackage, texlive-lastpage, texlive-latex-tds-doc, texlive-latexdemo
Requires:       texlive-latexgit, texlive-layouts, texlive-lazylist, texlive-lccaps
Requires:       texlive-lcd, texlive-lcg, texlive-leading, texlive-leaflet
Requires:       texlive-leftidx, texlive-leipzig, texlive-lengthconvert, texlive-lettre
Requires:       texlive-lettrine, texlive-lewis, texlive-lhelp, texlive-libgreek
Requires:       texlive-limap, texlive-linegoal, texlive-linop, texlive-lipsum
Requires:       texlive-lisp-on-tex, texlive-listing, texlive-listlbls, texlive-listliketab
Requires:       texlive-listofsymbols, texlive-lkproof, texlive-lmake, texlive-locality
Requires:       texlive-localloc, texlive-logbox, texlive-logical-markup-utils, texlive-logpap
Requires:       texlive-longfbox, texlive-longfigure, texlive-longnamefilelist, texlive-loops
Requires:       texlive-lsc, texlive-lstaddons, texlive-lt3graph, texlive-ltablex
Requires:       texlive-ltabptch, texlive-ltxdockit, texlive-ltxindex, texlive-ltxkeys
Requires:       texlive-ltxnew, texlive-ltxtools, texlive-lua-check-hyphen, texlive-luatodonotes
Requires:       texlive-macroswap, texlive-magaz, texlive-mailing, texlive-mailmerge
Requires:       texlive-makebarcode, texlive-makebase, texlive-makebox, texlive-makecell
Requires:       texlive-makecirc, texlive-makecmds, texlive-makedtx, texlive-makeglos
Requires:       texlive-mandi, texlive-manfnt, texlive-manuscript, texlive-manyind
Requires:       texlive-marginfit, texlive-marginfix, texlive-marginnote, texlive-markdown
Requires:       texlive-mathalfa, texlive-mathastext, texlive-mathexam, texlive-mathfam256
Requires:       texlive-mathfont, texlive-maybemath, texlive-mbenotes, texlive-mcaption
Requires:       texlive-mceinleger, texlive-mcexam, texlive-mcite, texlive-mciteplus
Requires:       texlive-mdframed, texlive-media9, texlive-medstarbeamer, texlive-meetingmins
Requires:       texlive-memexsupp, texlive-memory, texlive-mensa-tex, texlive-menu
Requires:       texlive-menukeys, texlive-method, texlive-metre, texlive-mfirstuc
Requires:       texlive-mftinc, texlive-midpage, texlive-minibox, texlive-minidocument
Requires:       texlive-minifp, texlive-minipage-marginpar
Requires:       texlive-minitoc, texlive-minorrevision, texlive-minted, texlive-minutes
Requires:       texlive-mla-paper, texlive-mlist, texlive-mmap, texlive-mnotes
Requires:       texlive-moderncv, texlive-modernposter, texlive-moderntimeline, texlive-modref
Requires:       texlive-modroman, texlive-modular, texlive-monofill, texlive-moodle
Requires:       texlive-moreenum, texlive-morefloats, texlive-morehype, texlive-moresize
Requires:       texlive-moreverb, texlive-morewrites, texlive-mparhack, texlive-mpostinl
Requires:       texlive-msc, texlive-msg, texlive-mslapa, texlive-mtgreek
Requires:       texlive-multenum, texlive-multiaudience, texlive-multibbl, texlive-multicap
Requires:       texlive-multidef, texlive-multienv, texlive-multiexpand, texlive-multilang
Requires:       texlive-multirow, texlive-mversion, texlive-mwe, texlive-mycv
Requires:       texlive-mylatexformat, texlive-nag, texlive-nameauth, texlive-namespc
Requires:       texlive-ncclatex, texlive-ncctools, texlive-needspace, texlive-nestquot
Requires:       texlive-newcommand-doc, texlive-newenviron
Requires:       texlive-newfile, texlive-newlfm, texlive-newspaper, texlive-newunicodechar
Requires:       texlive-newvbtm, texlive-newverbs, texlive-nextpage, texlive-nfssext-cfr
Requires:       texlive-nicefilelist, texlive-niceframe, texlive-nicetext, texlive-nidanfloat
Requires:       texlive-nlctdoc, texlive-noconflict, texlive-noindentafter, texlive-noitcrul
Requires:       texlive-nolbreaks, texlive-nomencl, texlive-nomentbl, texlive-nonfloat
Requires:       texlive-nonumonpart, texlive-nopageno, texlive-normalcolor, texlive-notes
Requires:       texlive-notespages, texlive-notestex, texlive-notoccite, texlive-nowidow
Requires:       texlive-nox, texlive-ntheorem, texlive-numberedblock, texlive-numname
Requires:       texlive-numprint, texlive-numspell, texlive-ocg-p, texlive-ocgx
Requires:       texlive-ocgx2, texlive-ocr-latex, texlive-octavo, texlive-oldstyle
Requires:       texlive-onlyamsmath, texlive-opcit, texlive-optidef, texlive-optional
Requires:       texlive-options, texlive-outline, texlive-outliner, texlive-outlines
Requires:       texlive-outlining, texlive-overlays, texlive-overpic, texlive-padcount
Requires:       texlive-pagecolor, texlive-pagecont, texlive-pagenote, texlive-pagerange
Requires:       texlive-pageslts, texlive-paper, texlive-papercdcase, texlive-papermas
Requires:       texlive-papertex, texlive-paracol, texlive-parades, texlive-paralist
Requires:       texlive-paresse, texlive-parnotes, texlive-parselines, texlive-pas-cours
Requires:       texlive-pas-cv, texlive-pas-tableur, texlive-patchcmd, texlive-pauldoc
Requires:       texlive-pawpict, texlive-pax, texlive-pbox, texlive-pbsheet
Requires:       texlive-pdf14, texlive-pdfcomment, texlive-pdfcprot, texlive-pdfmarginpar
Requires:       texlive-pdfoverlay, texlive-pdfpagediff, texlive-pdfpc-movie, texlive-pdfprivacy
Requires:       texlive-pdfreview, texlive-pdfscreen, texlive-pdfslide, texlive-pdfsync
Requires:       texlive-pdfwin, texlive-pdfx, texlive-pecha, texlive-perltex
Requires:       texlive-permute, texlive-petiteannonce, texlive-phffullpagefigure, texlive-phfnote
Requires:       texlive-phfparen, texlive-phfqit, texlive-phfquotetext, texlive-phfsvnwatermark
Requires:       texlive-phfthm, texlive-philex, texlive-phonenumbers, texlive-photo
Requires:       texlive-piff, texlive-pkgloader, texlive-placeins, texlive-plantslabels
Requires:       texlive-plates, texlive-plweb, texlive-polynom, texlive-polynomial
Requires:       texlive-polytable, texlive-postcards, texlive-poster-mac, texlive-ppr-prv
Requires:       texlive-preprint, texlive-pressrelease, texlive-prettyref, tex-preview
Requires:       texlive-printlen, texlive-probsoln, texlive-program, texlive-progress
Requires:       texlive-progressbar, texlive-proofread, texlive-properties, texlive-prosper
Requires:       texlive-protex, texlive-protocol, texlive-psfragx, texlive-pstool
Requires:       texlive-pstring, texlive-pxgreeks, texlive-pygmentex, texlive-python
Requires:       texlive-qcm, texlive-qstest, texlive-qsymbols, texlive-quicktype
Requires:       texlive-quotchap, texlive-quoting, texlive-quotmark, texlive-ran_toks
Requires:       texlive-randtext, texlive-rccol, texlive-rcs-multi, texlive-rcsinfo
Requires:       texlive-readarray, texlive-realboxes, texlive-recipe, texlive-recipebook
Requires:       texlive-recipecard, texlive-rectopma, texlive-refcheck, texlive-refenums
Requires:       texlive-reflectgraphics, texlive-refman, texlive-refstyle, texlive-regcount
Requires:       texlive-regexpatch, texlive-register, texlive-regstats, texlive-relenc
Requires:       texlive-relsize, texlive-repeatindex, texlive-repltext, texlive-rjlparshap
Requires:       texlive-rlepsf, texlive-rmpage, texlive-robustcommand, texlive-robustindex
Requires:       texlive-romanbar, texlive-romanbarpagenumber
Requires:       texlive-romanneg, texlive-romannum, texlive-rotfloat, texlive-rotpages
Requires:       texlive-roundbox, texlive-rterface, texlive-rtkinenc, texlive-rulercompass
Requires:       texlive-rvwrite, texlive-sanitize-umlaut
Requires:       texlive-sauerj, texlive-savefnmark, texlive-savesym, texlive-savetrees
Requires:       texlive-scale, texlive-scalebar, texlive-scalerel, texlive-scanpages
Requires:       texlive-scrlttr2copy, texlive-sdrt, texlive-secdot, texlive-sectionbox
Requires:       texlive-sectionbreak, texlive-sectsty, texlive-seealso, texlive-selectp
Requires:       texlive-semantic, texlive-semantic-markup
Requires:       texlive-semioneside, texlive-semproc, texlive-sepfootnotes, texlive-seqsplit
Requires:       texlive-sesstime, texlive-sf298, texlive-sffms, texlive-sfmath
Requires:       texlive-shadethm, texlive-shadow, texlive-shadowtext, texlive-shapepar
Requires:       texlive-shdoc, texlive-shipunov, texlive-shorttoc, texlive-show2e
Requires:       texlive-showcharinbox, texlive-showdim, texlive-showexpl, texlive-showhyphens
Requires:       texlive-showlabels, texlive-sidecap, texlive-sidenotes, texlive-silence
Requires:       texlive-simplecd, texlive-simplecv, texlive-simpleinvoice, texlive-sitem
Requires:       texlive-skb, texlive-skdoc, texlive-skeycommand, texlive-skeyval
Requires:       texlive-skrapport, texlive-slantsc, texlive-smalltableof, texlive-smartunits
Requires:       texlive-smartref, texlive-snapshot, texlive-snotez, texlive-soul
Requires:       texlive-spark-otf, texlive-sparklines, texlive-sphack, texlive-splitindex
Requires:       texlive-spot, texlive-spotcolor, texlive-spreadtab, texlive-spverbatim
Requires:       texlive-srbook-mem, texlive-srcltx, texlive-sseq, texlive-sslides
Requires:       texlive-stack, texlive-stackengine, texlive-standalone, texlive-stdclsdv
Requires:       texlive-stdpage, texlive-stealcaps, texlive-stex, texlive-storebox
Requires:       texlive-storecmd, texlive-stringstrings, texlive-sttools, texlive-stubs
Requires:       texlive-studenthandouts, texlive-subdepth
Requires:       texlive-subeqn, texlive-subeqnarray, texlive-subfigmat, texlive-subfigure
Requires:       texlive-subfiles, texlive-subfloat, texlive-substitutefont, texlive-substr
Requires:       texlive-supertabular, texlive-svg, texlive-svgcolor, texlive-svn
Requires:       texlive-svn-multi, texlive-svn-prov, texlive-svninfo, texlive-syntax
Requires:       texlive-syntrace, texlive-synttree, texlive-tabfigures, texlive-tableaux
Requires:       texlive-tablefootnote, texlive-tableof, texlive-tablestyles, texlive-tablists
Requires:       texlive-tabls, texlive-tabstackengine, texlive-tabto-ltx, texlive-tabu
Requires:       texlive-tabularborder, texlive-tabularcalc
Requires:       texlive-tabularew, texlive-tabulary, texlive-tagging, texlive-tagpair
Requires:       texlive-tagpdf, texlive-talk, texlive-tamefloats, texlive-tasks
Requires:       texlive-tcldoc, texlive-tcolorbox, texlive-tdclock, texlive-technics
Requires:       texlive-ted, texlive-templatetools, texlive-termcal, texlive-termlist
Requires:       texlive-testhyphens, texlive-testidx, texlive-tex-label, texlive-texlogos
Requires:       texlive-texmate, texlive-texments, texlive-texpower, texlive-texshade
Requires:       texlive-textualicomma, texlive-texvc, texlive-textfit, texlive-textmerg
Requires:       texlive-textpos, texlive-theoremref, texlive-thinsp, texlive-thmtools
Requires:       texlive-threadcol, texlive-threeparttable
Requires:       texlive-threeparttablex, texlive-thumb, texlive-thumbs, texlive-thumby
Requires:       texlive-ticket, texlive-titlecaps, texlive-titlefoot, texlive-titlepic
Requires:       texlive-titleref, texlive-titlesec, texlive-titling, texlive-tocbibind
Requires:       texlive-tocdata, texlive-tocloft, texlive-tocvsec2, texlive-todo
Requires:       texlive-todonotes, texlive-tokenizer, texlive-toolbox, texlive-topfloat
Requires:       texlive-totcount, texlive-totpages, texlive-translations, texlive-trfsigns
Requires:       texlive-trimspaces, texlive-trivfloat, texlive-trsym, texlive-truncate
Requires:       texlive-tucv, texlive-turnthepage, texlive-twoinone, texlive-twoup
Requires:       texlive-txgreeks, texlive-type1cm, texlive-typed-checklist, texlive-typeface
Requires:       texlive-typoaid, texlive-typogrid, texlive-uassign, texlive-ucs
Requires:       texlive-uebungsblatt, texlive-umoline, texlive-underlin, texlive-underoverlap
Requires:       texlive-undolabl, texlive-units, texlive-unravel, texlive-upmethodology
Requires:       texlive-upquote, texlive-uri, texlive-ushort, texlive-uspace
Requires:       texlive-variablelm, texlive-varindex, texlive-varsfromjobname, texlive-varwidth
Requires:       texlive-vdmlisting, texlive-verbasef, texlive-verbatimbox, texlive-verbatimcopy
Requires:       texlive-verbdef, texlive-verbments, texlive-version, texlive-versions
Requires:       texlive-versonotes, texlive-vertbars, texlive-vgrid, texlive-vhistory
Requires:       texlive-vmargin, texlive-volumes, texlive-vpe, texlive-vruler
Requires:       texlive-vwcol, texlive-wallcalendar, texlive-wallpaper, texlive-warning
Requires:       texlive-warpcol, texlive-was, texlive-widetable, texlive-williams
Requires:       texlive-withargs, texlive-wordcount, texlive-wordlike, texlive-wrapfig
Requires:       texlive-wtref, texlive-xargs, texlive-xassoccnt, texlive-xcntperchap
Requires:       texlive-xcolor-material, texlive-xcolor-solarized
Requires:       texlive-xcomment, texlive-xdoc, texlive-xellipsis, texlive-xfakebold
Requires:       texlive-xfor, texlive-xhfill, texlive-xifthen, texlive-xint
Requires:       texlive-xltabular, texlive-xmpincl, texlive-xnewcommand, texlive-xoptarg
Requires:       texlive-xpatch, texlive-xpeek, texlive-xprintlen, texlive-xpunctuate
Requires:       texlive-xsavebox, texlive-xsim, texlive-xstring, texlive-xtab
Requires:       texlive-xurl, texlive-xwatermark, texlive-xytree, texlive-yafoot
Requires:       texlive-yagusylo, texlive-yaletter, texlive-ycbook, texlive-ydoc
Requires:       texlive-yplan, texlive-zebra-goodies, texlive-zed-csp, texlive-ziffer
Requires:       texlive-zwgetfdate, texlive-zwpagelayout

%description -n texlive-collection-latexextra
A very large collection of add-on packages for LaTeX.

%package -n texlive-collection-latexrecommended
Summary:        LaTeX recommended packages
Version:        svn45955
Requires:       texlive-base, texlive-collection-latex, texlive-anysize, texlive-beamer
Requires:       texlive-booktabs, texlive-breqn, texlive-caption, texlive-cite
Requires:       texlive-cmap, texlive-crop, texlive-ctable, texlive-eso-pic
Requires:       texlive-euenc, texlive-euler, texlive-etoolbox, texlive-extsizes
Requires:       texlive-fancybox, texlive-fancyref, texlive-fancyvrb, texlive-filehook
Requires:       texlive-float, texlive-fontspec, texlive-fp, texlive-index
Requires:       texlive-jknapltx, texlive-koma-script, texlive-latexbug, texlive-l3experimental
Requires:       texlive-l3kernel, texlive-l3packages, texlive-lineno, texlive-listings
Requires:       texlive-lwarp, texlive-mathspec, texlive-mathtools, texlive-mdwtools
Requires:       texlive-memoir, texlive-metalogo, texlive-microtype, texlive-ms
Requires:       texlive-ntgclass, texlive-parskip, texlive-pdfpages, texlive-polyglossia
Requires:       texlive-powerdot, texlive-psfrag, texlive-rcs, texlive-sansmath
Requires:       texlive-section, texlive-seminar, texlive-sepnum, texlive-setspace
Requires:       texlive-subfig, texlive-textcase, texlive-thumbpdf, texlive-translator
Requires:       texlive-typehtml, texlive-ucharcat, texlive-underscore, texlive-unicode-math
Requires:       texlive-xcolor, texlive-xkeyval, texlive-xltxtra, texlive-xunicode
Provides:       tex(latex) = %{tl_version}, texlive-latex = %{tl_version}
Requires:       texlive-collection-fontsrecommended

%description -n texlive-collection-latexrecommended
A collection of recommended add-on packages for LaTeX which
have widespread use.

%package -n texlive-collection-pictures
Summary:        Graphics, pictures, diagrams
Version:        svn48314
Requires:       texlive-base, texlive-collection-basic, texlive-adigraph, texlive-aobs-tikz
Requires:       texlive-askmaps, texlive-asyfig, texlive-asypictureb, texlive-autoarea
Requires:       texlive-bardiag, texlive-beamerswitch, texlive-binarytree, texlive-blochsphere
Requires:       texlive-bloques, texlive-blox, texlive-bodegraph, texlive-bondgraph
Requires:       texlive-bondgraphs, texlive-braids, texlive-bxeepic, texlive-cachepic
Requires:       texlive-callouts, texlive-celtic, texlive-chemfig, texlive-combinedgraphics
Requires:       texlive-circuitikz, texlive-curve, texlive-curve2e, texlive-curves
Requires:       texlive-dcpic, texlive-diagmac2, texlive-doc-pictex-doc, texlive-dottex
Requires:       texlive-dot2texi, texlive-dratex, texlive-drs, texlive-duotenzor
Requires:       texlive-dynkin-diagrams, texlive-ecgdraw
Requires:       texlive-eepic, texlive-ellipse, texlive-endofproofwd, texlive-epspdf
Requires:       texlive-epspdfconversion, texlive-esk, texlive-fast-diagram, texlive-fig4latex
Requires:       texlive-fitbox, texlive-flowchart, texlive-forest, texlive-genealogytree
Requires:       texlive-getmap, texlive-gincltex, texlive-gnuplottex, texlive-gradientframe
Requires:       texlive-grafcet, texlive-graph35, texlive-graphicxpsd, texlive-graphviz
Requires:       texlive-gtrlib-largetrees, texlive-harveyballs
Requires:       texlive-here, texlive-hf-tikz, texlive-hobby, texlive-hvfloat
Requires:       texlive-istgame, texlive-knitting, texlive-knittingpattern, texlive-ladder
Requires:       texlive-lapdf, texlive-latex-make, texlive-lpic, texlive-lroundrect
Requires:       texlive-luamesh, texlive-luasseq, texlive-maker, texlive-makeshape
Requires:       texlive-mathspic, texlive-milsymb, texlive-miniplot, texlive-mkpic
Requires:       texlive-modiagram, texlive-neuralnetwork
Requires:       texlive-numericplots, texlive-pb-diagram
Requires:       texlive-penrose, texlive-petri-nets, texlive-pgf, texlive-pgf-blur
Requires:       texlive-pgf-soroban, texlive-pgf-spectra
Requires:       texlive-pgf-umlcd, texlive-pgf-umlsd, texlive-pgfgantt, texlive-pgfkeyx
Requires:       texlive-pgfmolbio, texlive-pgfopts, texlive-pgfornament, texlive-pgfplots
Requires:       texlive-picinpar, texlive-pict2e, texlive-pictex, texlive-pictex2
Requires:       texlive-pinlabel, texlive-pixelart, texlive-pmgraph, texlive-postage
Requires:       texlive-prerex, texlive-productbox, texlive-pxpgfmark, texlive-qcircuit
Requires:       texlive-qrcode, texlive-randbild, texlive-randomwalk, texlive-reotex
Requires:       texlive-rviewport, texlive-sa-tikz, texlive-schemabloc, texlive-scsnowman
Requires:       texlive-scratch, texlive-setdeck, texlive-signchart, texlive-smartdiagram
Requires:       texlive-spath3, texlive-spectralsequences
Requires:       texlive-swimgraf, texlive-table-fct, texlive-texdraw, texlive-ticollege
Requires:       texlive-tipfr-doc, texlive-tikz-3dplot, texlive-tikz-bayesnet, texlive-tikz-cd
Requires:       texlive-tikz-dependency, texlive-tikz-dimline
Requires:       texlive-tikz-feynman, texlive-tikz-inet, texlive-tikz-kalender, texlive-tikz-karnaugh
Requires:       texlive-tikz-ladder, texlive-tikz-layers
Requires:       texlive-tikz-nef, texlive-tikz-network, texlive-tikz-opm, texlive-tikz-optics
Requires:       texlive-tikz-page, texlive-tikz-palattice
Requires:       texlive-tikz-qtree, texlive-tikz-relay, texlive-tikz-sfc, texlive-tikz-timing
Requires:       texlive-tikzcodeblocks, texlive-tikzducks
Requires:       texlive-tikzinclude, texlive-tikzmark, texlive-tikzmarmots, texlive-tikzorbital
Requires:       texlive-tikzpagenodes, texlive-tikzpfeile
Requires:       texlive-tikzpeople, texlive-tikzposter, texlive-tikzscale, texlive-tikzsymbols
Requires:       texlive-timing-diagrams, texlive-tqft, texlive-tkz-base, texlive-tkz-berge
Requires:       texlive-tkz-doc, texlive-tkz-euclide, texlive-tkz-fct, texlive-tkz-graph
Requires:       texlive-tkz-kiviat, texlive-tkz-linknodes
Requires:       texlive-tkz-orm, texlive-tkz-tab, texlive-tsemlines, texlive-tufte-latex
Requires:       texlive-venndiagram, texlive-visualpstricks-doc
Requires:       texlive-xpicture, texlive-xypic

%description -n texlive-collection-pictures
Including TikZ, pict, etc., but MetaPost and PStricks are
separate.

%package -n texlive-combinedgraphics
Provides:       tex-combinedgraphics = %{tl_version}
License:        GPL+
Summary:        Include graphic (EPS or PDF)/LaTeX combinations
Version:        svn27198.0.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(graphicx.sty), tex(color.sty)
Provides:       tex(combinedgraphics.sty) = %{tl_version}

%description -n texlive-combinedgraphics
This package provides a macro (\includecombinedgraphics) for
the inclusion of combined EPS/LaTeX and PDF/LaTeX graphics (an
export format of Gnuplot, Xfig, and maybe other programs).
Instead of including the graphics with a simple \input, the
\includecombinedgraphics macro has some comforts: changing the
font and color of the text of the LaTeX part; rescaling the
graphics without affecting the font of the LaTeX part;
automatic inclusion of the vector graphics part, as far as
LaTeX part does not do it (e.g., for files exported from
Gnuplot before version 4.2); and rescaling and rotating of
complete graphics (similar to \includegraphics from the
graphicx package).

%package -n texlive-combinedgraphics-doc
Summary:        Documentation for combinedgraphics
Version:        svn27198.0.2.2

Provides:       tex-combinedgraphics-doc
AutoReqProv:    No

%description -n texlive-combinedgraphics-doc
Documentation for combinedgraphics


%package -n texlive-colordoc
Provides:       tex-colordoc = %{tl_version}
License:        LPPL
Summary:        Coloured syntax highlights in documentation
Version:        svn18270.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty), tex(fixltx2e.sty)
Provides:       tex(colordoc.sty) = %{tl_version}

%description -n texlive-colordoc
The package is used in documentation files (that use the doc
package); with it the code listings will highlight (for
example) pairs of curly braces with matching colors. Other
delimiters like \if ... \fi, are highlighted, as are the names
of new commands. All this makes code a little more readable,
and helps during process of writing. Three options are
provided, including a non-color option designed for printing
(which numbers delimiters and underlines new commands).

%package -n texlive-colordoc-doc
Summary:        Documentation for colordoc
Version:        svn18270.0

Provides:       tex-colordoc-doc
AutoReqProv:    No

%description -n texlive-colordoc-doc
Documentation for colordoc

%package -n texlive-colorinfo
Provides:       tex-colorinfo = %{tl_version}
License:        LPPL
Summary:        Retrieve colour model and values for defined colours
Version:        svn15878.0.3c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(colorinfo.sty) = %{tl_version}

%description -n texlive-colorinfo
colorinfo package

%package -n texlive-colorinfo-doc
Summary:        Documentation for colorinfo
Version:        svn15878.0.3c

Provides:       tex-colorinfo-doc
AutoReqProv:    No

%description -n texlive-colorinfo-doc
Documentation for colorinfo

%package -n texlive-colorspace
Provides:       tex-colorspace = %{tl_version}
License:        LPPL 1.3
Summary:        Provides PDF color spaces
Version:        svn42228
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xcolor.sty)
Provides:       tex(colorspace.sty) = %{tl_version}

%description -n texlive-colorspace
The package provides PDF color spaces. Currently, only spot
colors and overprinting are supported. It requires xcolor, and
supports pdfTeX and luaTeX.

%package -n texlive-colorspace-doc
Summary:        Documentation for colorspace
Version:        svn42228
Provides:       tex-colorspace-doc
AutoReqProv:    No

%description -n texlive-colorspace-doc
Documentation for colorspace

%package -n texlive-colortab
Provides:       tex-colortab = %{tl_version}
License:        LPPL
Summary:        Shade cells of tables and halign
Version:        svn22155.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pstricks.sty), tex(fancybox.sty)
Provides:       tex(colortab.sty) = %{tl_version}, tex(colortab.tex) = %{tl_version}

%description -n texlive-colortab
The package lets you shade or colour the cells in the alignment
environments such as \halign and LaTeX's tabular and array
environments. The colortbl package is to be preferred today
with LaTeX (it assures compatibility with the longtable
package, which is no longer true with colortab); another modern
option is the table-colouring option of the xcolor. However,
colortab remains an adequate solution for use with Plain TeX.

%package -n texlive-colortab-doc
Summary:        Documentation for colortab
Version:        svn22155.1.0

Provides:       tex-colortab-doc
AutoReqProv:    No

%description -n texlive-colortab-doc
Documentation for colortab

%package -n texlive-colorwav
Provides:       tex-colorwav = %{tl_version}
License:        LGPLv2+
Summary:        Colours by wavelength of visible light
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(fp.sty)
Provides:       tex(colorwav.sty) = %{tl_version}

%description -n texlive-colorwav
The package allows the user to obtain an RGB value (suitable
for use in the color package) from a wavelength of light. The
default unit is nanometres, but other units may be used. Note
that this function is also available within the xcolor.

%package -n texlive-colorwav-doc
Summary:        Documentation for colorwav
Version:        svn15878.1.0

Provides:       tex-colorwav-doc
AutoReqProv:    No

%description -n texlive-colorwav-doc
Documentation for colorwav

%package -n texlive-colorweb
Provides:       tex-colorweb = %{tl_version}
License:        LPPL 1.3
Summary:        Extend the color package colour space
Version:        svn31490.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty)
Provides:       tex(colorweb.sty) = %{tl_version}

%description -n texlive-colorweb
The package makes the 216 "web-safe colours" available to the
standard color package.

%package -n texlive-colorweb-doc
Summary:        Documentation for colorweb
Version:        svn31490.1.3

Provides:       tex-colorweb-doc
AutoReqProv:    No

%description -n texlive-colorweb-doc
Documentation for colorweb

%package -n texlive-colourchange
Provides:       tex-colourchange = %{tl_version}
License:        GPLv3+
Summary:        colourchange
Version:        svn21741.1.22

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(calc.sty)
Provides:       tex(colourchange.sty) = %{tl_version}

%description -n texlive-colourchange
The package allows you to change the colour of the structural
elements (inner theme and outer theme) of your beamer
presentation during the presentation. There is a manual option
but there is also the option to have your structure colour
change from one colour to another as a function of how far
through the presentation you are.

%package -n texlive-colourchange-doc
Summary:        Documentation for colourchange
Version:        svn21741.1.22

Provides:       tex-colourchange-doc
AutoReqProv:    No

%description -n texlive-colourchange-doc
Documentation for colourchange

%package -n texlive-combelow
Provides:       tex-combelow = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset "comma-below" letters, as in Romanian
Version:        svn18462.0.99f

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(combelow.sty) = %{tl_version}

%description -n texlive-combelow
The package defines a command \cb that positions a comma below
a letter, as required (for example) in Romanian typesetting.
The command is robust, but interferes with hyphenation.

%package -n texlive-combelow-doc
Summary:        Documentation for combelow
Version:        svn18462.0.99f

Provides:       tex-combelow-doc
AutoReqProv:    No

%description -n texlive-combelow-doc
Documentation for combelow

%package -n texlive-combine
Provides:       tex-combine = %{tl_version}
License:        LPPL 1.3
Summary:        Bundle individual documents into a single document
Version:        svn19361.0.7a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(cite.sty), tex(keyval.sty), tex(natbib.sty)
Provides:       tex(combcite.sty) = %{tl_version}, tex(combine.cls) = %{tl_version}
Provides:       tex(combinet.sty) = %{tl_version}, tex(combnat.sty) = %{tl_version}

%description -n texlive-combine
The combine class lets you bundle individual documents into a
single document, such as when preparing a conference
proceedings. The auxiliary combinet package puts the titles and
authors from \maketitle commands into the main document's Table
of Contents. The package cooperates with the abstract and
titling packages.

%package -n texlive-combine-doc
Summary:        Documentation for combine
Version:        svn19361.0.7a

Provides:       tex-combine-doc
AutoReqProv:    No

%description -n texlive-combine-doc
Documentation for combine

%package -n texlive-comma
Provides:       tex-comma = %{tl_version}
License:        LPPL
Summary:        Formats a number by inserting commas
Version:        svn18259.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(comma.sty) = %{tl_version}

%description -n texlive-comma
A flexible package that allows commas (or anything else) to be
inserted every three digits in a number, as in 1,234.

%package -n texlive-comma-doc
Summary:        Documentation for comma
Version:        svn18259.1.2

Provides:       tex-comma-doc
AutoReqProv:    No

%description -n texlive-comma-doc
Documentation for comma

%package -n texlive-commado
Provides:       tex-commado = %{tl_version}
License:        LPPL 1.3
Summary:        Expandable iteration on comma-separated and filename lists
Version:        svn38875

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(commado.sty) = %{tl_version}, tex(filesdo.sty) = %{tl_version}

%description -n texlive-commado
The bundle provides two packages: commado and filesdo. The
package commado provides the command \DoWithCSL:
\DoWithCSL{<cmd>}{<list>} applies an existing one-parameter
macro <cmd> to each item in a list <list> in which terms are
separated by commas. The package filesdo provides the command
\DoWithBasesExts: \DoWithBasesExts{<cmd>}{<bases>}{<exts>}
which runs the single parameter command <cmd> on each file
whose base and extension are respectively from the comma-
separated lists <bases> and <exts>. These 'loop'-like commands
are (themselves) entirely expandable. The packages rely on
packages plainpkg, and stacklet

%package -n texlive-commado-doc
Summary:        Documentation for commado
Version:        svn38875

Provides:       tex-commado-doc
AutoReqProv:    No

%description -n texlive-commado-doc
Documentation for commado

%package -n texlive-comment
Provides:       tex-comment = %{tl_version}
License:        GPL+
Summary:        Selectively include/excludes portions of text
Version:        svn41927
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(comment.sty) = %{tl_version}

%description -n texlive-comment
Selectively include/exclude pieces of text, allowing the user
to define new, separately controlled, comment versions. All
text between \comment ... \endcomment or \begin{comment} ...
\end{comment} is discarded. The opening and closing commands
should appear on a line of their own. No starting spaces,
nothing after it. This environment should work with arbitrary
amounts of comment, and the comment can be arbitrary text.
Other 'comment' environments are defined and
selected/deselected with \includecomment{versiona} and
\excludecoment{versionb} These environments are used as
\versiona ... \endversiona or \begin{versiona} ...
\end{versiona} with the opening and closing commands again on a
line of their own.

%package -n texlive-comment-doc
Summary:        Documentation for comment
Version:        svn41927
Provides:       tex-comment-doc
AutoReqProv:    No

%description -n texlive-comment-doc
Documentation for comment

%package -n texlive-concepts
Provides:       tex-concepts = %{tl_version}
License:        LPPL
Summary:        Keeping track of formal 'concepts' for a particular field
Version:        svn29020.0.0.5_r1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etextools.sty), tex(nth.sty), tex(xspace.sty), tex(xparse.sty)
Requires:       tex(ltxkeys.sty), tex(xstring.sty)
Provides:       tex(concepts.sty) = %{tl_version}

%description -n texlive-concepts
The package helps to keep track of formal 'concepts' for a
specific field or document. This is particularly useful for
scientific papers (for example, in physics, mathematics or
computer science), which may introduce several concepts (with
their own symbols). The package's commands allow the user to
define a concept (typically, near its first use), and will
ensure consistent use throughout the document. The package
depends on several other packages; while these are fairly
common packages, the user should check the package's README
file for the complete list.

%package -n texlive-concepts-doc
Summary:        Documentation for concepts
Version:        svn29020.0.0.5_r1

Provides:       tex-concepts-doc
AutoReqProv:    No

%description -n texlive-concepts-doc
Documentation for concepts

%package -n texlive-concprog
Provides:       tex-concprog = %{tl_version}
License:        GPL+
Summary:        Concert programmes
Version:        svn18791.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ConcProg.cls) = %{tl_version}

%description -n texlive-concprog
A class which provides the necessary macros to prepare a
(classical) concert programme; a sample is provided.

%package -n texlive-concprog-doc
Summary:        Documentation for concprog
Version:        svn18791.0

Provides:       tex-concprog-doc
AutoReqProv:    No

%description -n texlive-concprog-doc
Documentation for concprog

%package -n texlive-constants
Provides:       tex-constants = %{tl_version}
License:        LPPL
Summary:        Automatic numbering of constants
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(constants.sty) = %{tl_version}

%description -n texlive-constants
The package provides a way to number constants in a
mathematical proof automatically, with a system for
labelling/referencing. In addition, several families of
constants (with different symbols) may be defined.

%package -n texlive-constants-doc
Summary:        Documentation for constants
Version:        svn15878.1.0

Provides:       tex-constants-doc
AutoReqProv:    No

%description -n texlive-constants-doc
Documentation for constants

%package -n texlive-contour
Provides:       tex-contour = %{tl_version}
License:        LPPL
Summary:        Print a coloured contour around text
Version:        svn18950.2.14

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty), tex(trig.sty)
Provides:       tex(contour.cfg) = %{tl_version}, tex(contour.sty) = %{tl_version}

%description -n texlive-contour
This package generates a coloured contour around a given text
in order to enable printing text over a background without the
need of a coloured box around the text.

%package -n texlive-contour-doc
Summary:        Documentation for contour
Version:        svn18950.2.14

Provides:       tex-contour-doc
AutoReqProv:    No

%description -n texlive-contour-doc
Documentation for contour

%package -n texlive-contracard
Provides:       tex-contracard = %{tl_version}
License:        LPPL 1.3
Summary:        Generate calling cards for dances
Version:        svn48250
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(geometry.sty), tex(titlesec.sty)
Provides:       tex(contracard.cls) = %{tl_version}

%description -n texlive-contracard
A package and a class used to typeset traditional country
dances, such as contra and square dances, and to create calling
cards for the same.

%package -n texlive-contracard-doc
Summary:        Documentation for contracard
Version:        svn48250
Provides:       tex-contracard-doc
AutoReqProv:    No

%description -n texlive-contracard-doc
Documentation for contracard

%package -n texlive-cooking
Provides:       tex-cooking = %{tl_version}
License:        GPL+
Summary:        Typeset recipes
Version:        svn15878.0.9b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cooking.sty) = %{tl_version}

%description -n texlive-cooking
The package typesets recipes according to the style used in a
well-respected German cookery book.

%package -n texlive-cooking-doc
Summary:        Documentation for cooking
Version:        svn15878.0.9b

Provides:       tex-cooking-doc
AutoReqProv:    No

%description -n texlive-cooking-doc
Documentation for cooking

%package -n texlive-cool
Provides:       tex-cool = %{tl_version}
License:        LGPLv2+
Summary:        COntent-Oriented LaTeX
Version:        svn15878.1.35

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(coollist.sty), tex(coolstr.sty), tex(forloop.sty)
Requires:       tex(amsmath.sty), tex(amssymb.sty), tex(bbm.sty)
Provides:       tex(cool.sty) = %{tl_version}

%description -n texlive-cool
The package (COntent Oriented LaTeX) gives LaTeX the power to
retain mathematical meaning of its expressions in addition to
the typsetting instructions; essentially separating style from
the content of the math. One advantage of keeping mathematical
meaning is that conversion of LaTeX documents to other
executable formats (such as Content MathML or Mathematica code)
is greatly simplified. The package requires the coolstr,
coollist and forloop packages.

%package -n texlive-cool-doc
Summary:        Documentation for cool
Version:        svn15878.1.35

Provides:       tex-cool-doc
AutoReqProv:    No

%description -n texlive-cool-doc
Documentation for cool

%package -n texlive-coollist
Provides:       tex-coollist = %{tl_version}
License:        LGPLv2+
Summary:        Manipulate COntent Oriented LaTeX Lists
Version:        svn15878.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(amsmath.sty), tex(amssymb.sty), tex(coolstr.sty)
Requires:       tex(forloop.sty)
Provides:       tex(coollist.sty) = %{tl_version}

%description -n texlive-coollist
Lists are defined as a sequence of tokens separated by a comma.
The coollist package allows the user to access certain elements
of the list while neglecting others--essentially turning lists
into a sort of array. List elements are accessed by specifying
the position of the object within the list (the index of the
item).

%package -n texlive-coollist-doc
Summary:        Documentation for coollist
Version:        svn15878.1.4

Provides:       tex-coollist-doc
AutoReqProv:    No

%description -n texlive-coollist-doc
Documentation for coollist

%package -n texlive-coolstr
Provides:       tex-coolstr = %{tl_version}
License:        LGPLv2+
Summary:        String manipulation in LaTeX
Version:        svn15878.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(amsmath.sty), tex(amssymb.sty)
Provides:       tex(coolstr.sty) = %{tl_version}

%description -n texlive-coolstr
Coolstr is a subpackage of the cool bundle that deals with the
manipulation of strings. A string is defined as a sequence of
characters (not tokens). The package provides the ability to
access a specific character of a string, as well as determine
if the string contains numeric or integer data.

%package -n texlive-coolstr-doc
Summary:        Documentation for coolstr
Version:        svn15878.2.2

Provides:       tex-coolstr-doc
AutoReqProv:    No

%description -n texlive-coolstr-doc
Documentation for coolstr

%package -n texlive-coolthms
Provides:       tex-coolthms = %{tl_version}
License:        LPPL
Summary:        Reference items in a theorem environment
Version:        svn29062.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amssymb.sty), tex(hyperref.sty), tex(etoolbox.sty), tex(scrbase.sty)
Requires:       tex(letltxmacro.sty), tex(ifthen.sty), tex(xargs.sty), tex(kvoptions.sty)
Requires:       tex(ntheorem.sty), tex(cleveref.sty)
Provides:       tex(coolthms.sty) = %{tl_version}

%description -n texlive-coolthms
The package provides the means to directly reference items of
lists nested in theorem-like environments (e.g., as 'Theorem 1
a'). The package extends the ntheorem and cleveref packages.
The package also provides other theorem markup commands.

%package -n texlive-coolthms-doc
Summary:        Documentation for coolthms
Version:        svn29062.1.2

Provides:       tex-coolthms-doc
AutoReqProv:    No

%description -n texlive-coolthms-doc
Documentation for coolthms

%package -n texlive-cooltooltips
Provides:       tex-cooltooltips = %{tl_version}
License:        LPPL
Summary:        Associate a pop-up window and tooltip with PDF hyperlinks
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifpdf.sty)
Provides:       tex(cooltooltips.sty) = %{tl_version}

%description -n texlive-cooltooltips
The cooltooltips package enables a document to contain
hyperlinks that pop up a brief tooltip when the mouse moves
over them and also open a small window containing additional
text. cooltooltips provides the mechanism used by the Visual
LaTeX FAQ to indicate the question that each hyperlink answers.

%package -n texlive-cooltooltips-doc
Summary:        Documentation for cooltooltips
Version:        svn15878.1.0

Provides:       tex-cooltooltips-doc
AutoReqProv:    No

%description -n texlive-cooltooltips-doc
Documentation for cooltooltips

%package -n texlive-coordsys
Provides:       tex-coordsys = %{tl_version}
License:        LPPL
Summary:        Draw cartesian coordinate systems
Version:        svn15878.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(coordsys.sty) = %{tl_version}, tex(logsys.sty) = %{tl_version}

%description -n texlive-coordsys
The package provides commands for typesetting number lines
(coordinate axes), coordinate systems and grids in the picture
environment. The package may be integrated with other drawing
mechanisms: the documentation shows examples of drawing graphs
(coordinate tables created by Maple), using the eepic package's
drawing capabilities.

%package -n texlive-coordsys-doc
Summary:        Documentation for coordsys
Version:        svn15878.1.4

Provides:       tex-coordsys-doc
AutoReqProv:    No

%description -n texlive-coordsys-doc
Documentation for coordsys

%package -n texlive-copyedit
Provides:       tex-copyedit = %{tl_version}
License:        LPPL 1.3
Summary:        Copyediting support for LaTeX documents
Version:        svn37928.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(acronym.sty), tex(l3str.sty), tex(l3keys2e.sty)
Requires:       tex(xparse.sty), tex(enumitem.sty)
Provides:       tex(copyedit.sty) = %{tl_version}

%description -n texlive-copyedit
This package implements copyediting support for LaTeX
documents. Authors can enjoy the freedom of using, for example,
words with US or UK or Canadian or Australian spelling in a
mixed way, yet, they can choose any one of the usage forms for
their entire document irrespective of kinds of spelling they
have adopted. In the same fashion, the users can have the
benefit of the following features available in the package:
Localization -- British-American-Australian-Canadian Close-up,
Hyphenation, and Spaced words Latin abbreviations Acronyms and
Abbreviations Itemization, nonlocal lists and labels
Parenthetical and serial commas Non-local tokenization in
language through Abbreviations and pronouns.

%package -n texlive-copyedit-doc
Summary:        Documentation for copyedit
Version:        svn37928.1.6

Provides:       tex-copyedit-doc
AutoReqProv:    No

%description -n texlive-copyedit-doc
Documentation for copyedit

%package -n texlive-copyrightbox
Provides:       tex-copyrightbox = %{tl_version}
License:        LPPL
Summary:        Provide copyright notices for images in a document
Version:        svn24829.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(ifthen.sty)
Provides:       tex(copyrightbox.sty) = %{tl_version}

%description -n texlive-copyrightbox
The package command \copyrightbox[<placement>]{<image
command>}{<text>}, which places the text as a copyright notice
relating to the matter created by the image command.

%package -n texlive-copyrightbox-doc
Summary:        Documentation for copyrightbox
Version:        svn24829.0.1

Provides:       tex-copyrightbox-doc
AutoReqProv:    No

%description -n texlive-copyrightbox-doc
Documentation for copyrightbox

%package -n texlive-coseoul
Provides:       tex-coseoul = %{tl_version}
License:        LPPL 1.3
Summary:        Context sensitive outline elements
Version:        svn23862.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(coseoul.sty) = %{tl_version}

%description -n texlive-coseoul
The package provides "relative" commands that may be used in
place of \chapter, \section, etc. The documentation shows a
number of document-management scenarios in which such commands
are valuable.

%package -n texlive-coseoul-doc
Summary:        Documentation for coseoul
Version:        svn23862.1.1

Provides:       tex-coseoul-doc
AutoReqProv:    No

%description -n texlive-coseoul-doc
Documentation for coseoul

%package -n texlive-counttexruns
Provides:       tex-counttexruns = %{tl_version}
License:        LPPL 1.3
Summary:        Count compilations of a document
Version:        svn27576.1.00a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty)
Provides:       tex(counttexruns.sty) = %{tl_version}

%description -n texlive-counttexruns
The package counts how often a LaTeX document is compiled,
keeping the data in an external file. To print the count, can
use the macro \thecounttexruns.

%package -n texlive-counttexruns-doc
Summary:        Documentation for counttexruns
Version:        svn27576.1.00a

Provides:       tex-counttexruns-doc
AutoReqProv:    No

%description -n texlive-counttexruns-doc
Documentation for counttexruns

%package -n texlive-courseoutline
Provides:       tex-courseoutline = %{tl_version}
License:        Copyright only
Summary:        Prepare university course outlines
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(courseoutline.cls) = %{tl_version}

%description -n texlive-courseoutline
Courseoutline is a class designed to minimise markup in a
tedious task that needs to be repeated often.

%package -n texlive-courseoutline-doc
Summary:        Documentation for courseoutline
Version:        svn15878.1.0

Provides:       tex-courseoutline-doc
AutoReqProv:    No

%description -n texlive-courseoutline-doc
Documentation for courseoutline

%package -n texlive-coursepaper
Provides:       tex-coursepaper = %{tl_version}
License:        Copyright only
Summary:        Prepare university course papers
Version:        svn15878.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(coursepaper.cls) = %{tl_version}

%description -n texlive-coursepaper
Coursepaper is a class with which students can provide simple
course papers, in a uniform design to ease the task of marking.

%package -n texlive-coursepaper-doc
Summary:        Documentation for coursepaper
Version:        svn15878.2.0

Provides:       tex-coursepaper-doc
AutoReqProv:    No

%description -n texlive-coursepaper-doc
Documentation for coursepaper

%package -n texlive-coverpage
Provides:       tex-coverpage = %{tl_version}
License:        LPPL 1.2
Summary:        Automatic cover page creation for scientific papers
Version:        svn15878.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty), tex(textcomp.sty), tex(url.sty), tex(verbatim.sty)
Provides:       tex(CoverPage.cfg) = %{tl_version}, tex(CoverPage.sty) = %{tl_version}

%description -n texlive-coverpage
The package CoverPage was created to supplement scientific
papers with a cover page containing bibliographical
information, a copyright notice, and/or some logos of the
author's institution. The cover page is created (almost)
automatically; this is done by parsing BibTeX information
corresponding to the main document and reading a configuration
file in which the author can set information like the
affiliation he or she is associated with. The cover page
consists of header, body and footer; all three are macros which
can be redefined using \renewcommand, thus allowing easy
customization of the package. Additionally, it should be
stressed that the cover page layout is totally independent of
the main document and its page layout. This package requires
four other packages (keyval, url, textcomp, and verbatim), but
all of them are standard packages and should be part of every
LaTeX installation.

%package -n texlive-coverpage-doc
Summary:        Documentation for coverpage
Version:        svn15878.1.01

Provides:       tex-coverpage-doc
AutoReqProv:    No

%description -n texlive-coverpage-doc
Documentation for coverpage

%package -n texlive-collection-luatex
Summary:        LuaTeX packages
Version:        svn48052
Requires:       texlive-base, texlive-collection-basic, texlive-auto-pst-pdf-lua, texlive-bezierplot
Requires:       texlive-checkcites, texlive-chickenize, texlive-combofont, texlive-cstypo
Requires:       texlive-ctablestack, texlive-enigma, texlive-fontloader-luaotfload, texlive-interpreter
Requires:       texlive-kanaparser, texlive-lua-visual-debug
Requires:       texlive-lua2dox, texlive-luacode, texlive-luahyphenrules, texlive-luaindex
Requires:       texlive-luainputenc, texlive-luaintro-doc
Requires:       texlive-lualatex-doc-doc, texlive-lualatex-math
Requires:       texlive-lualatex-truncate, texlive-lualibs
Requires:       texlive-luamplib, texlive-luaotfload, texlive-luapackageloader, texlive-luatex85
Requires:       texlive-luatexbase, texlive-luatexko, texlive-luatextra, texlive-luavlna
Requires:       texlive-luaxml, texlive-nodetree, texlive-odsfile, texlive-placeat
Requires:       texlive-plantuml, texlive-selnolig, texlive-spelling, texlive-typewriter

%description -n texlive-collection-luatex
Packages for LuaTeX, a Unicode-aware extension of pdfTeX, using
Lua as an embedded scripting and extension language.
http://luatex.org/

%package -n texlive-commath
Provides:       tex-commath = %{tl_version}
License:        LPPL
Summary:        Mathematics typesetting support
Version:        svn15878.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(amsmath.sty)
Provides:       tex(commath.sty) = %{tl_version}

%description -n texlive-commath
Provides a range of differential, partial differential and
delimiter commands, together with a \fullfunction (function,
with both domain and range, and function operation) and various
reference commands.

%package -n texlive-commath-doc
Summary:        Documentation for commath
Version:        svn15878.0.3

Provides:       tex-commath-doc
AutoReqProv:    No

%description -n texlive-commath-doc
Documentation for commath

%package -n texlive-concmath
Provides:       tex-concmath = %{tl_version}
License:        LPPL
Summary:        Concrete Math fonts
Version:        svn17219.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(exscale.sty), tex(amsfonts.sty), tex(amssymb.sty)
Provides:       tex(concmath.sty) = %{tl_version}, tex(omlccm.fd) = %{tl_version}
Provides:       tex(omlccr.fd) = %{tl_version}, tex(omsccr.fd) = %{tl_version}
Provides:       tex(omsccsy.fd) = %{tl_version}, tex(omxccex.fd) = %{tl_version}
Provides:       tex(ot1ccr.fd) = %{tl_version}, tex(ucca.fd) = %{tl_version}
Provides:       tex(uccb.fd) = %{tl_version}

%description -n texlive-concmath
A LaTeX package and font definition files to access the
Concrete mathematics fonts, which were derived from Computer
Modern math fonts using parameters from Concrete Roman text
fonts.

%package -n texlive-concmath-doc
Summary:        Documentation for concmath
Version:        svn17219.0

Provides:       tex-concmath-doc
AutoReqProv:    No

%description -n texlive-concmath-doc
Documentation for concmath

%package -n texlive-concrete
Provides:       tex-concrete = %{tl_version}
License:        Knuth
Summary:        Concrete Roman fonts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cccsc10.tfm) = %{tl_version}, tex(ccmi10.tfm) = %{tl_version}
Provides:       tex(ccmic9.tfm) = %{tl_version}, tex(ccr10.tfm) = %{tl_version}
Provides:       tex(ccr5.tfm) = %{tl_version}, tex(ccr6.tfm) = %{tl_version}
Provides:       tex(ccr7.tfm) = %{tl_version}, tex(ccr8.tfm) = %{tl_version}
Provides:       tex(ccr9.tfm) = %{tl_version}, tex(ccsl10.tfm) = %{tl_version}
Provides:       tex(ccsl9.tfm) = %{tl_version}, tex(ccslc9.tfm) = %{tl_version}
Provides:       tex(ccti10.tfm) = %{tl_version}

%description -n texlive-concrete
Concrete Roman fonts, designed by Donald E. Knuth, originally
for use with Euler mathematics fonts. Alternative mathematics
fonts, based on the concrete 'parameter set' are available as
the concmath fonts bundle. LaTeX support is offered by the
beton, concmath and ccfonts packages. T1- and TS1-encoded
versions of the fonts are available in the ecc bundle, and
Adobe Type 1 versions of the ecc fonts are part of the cm-super
bundle.

%package -n texlive-concrete-doc
Summary:        Documentation for concrete
Version:        svn15878.0

Provides:       tex-concrete-doc
AutoReqProv:    No

%description -n texlive-concrete-doc
Documentation for concrete

%package -n texlive-conteq
Provides:       tex-conteq = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset multiline continued equalities
Version:        svn37868.0.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(amsmath.sty), tex(environ.sty)
Provides:       tex(conteq.sty) = %{tl_version}

%description -n texlive-conteq
The package provides an environment conteq, which will lay out
systems of continued equalities (or inequalities). Several
variant layouts of the equalities are provided, and the user
may define their own. The package is written using LaTeX 3
macros.

%package -n texlive-conteq-doc
Summary:        Documentation for conteq
Version:        svn37868.0.1.1

Provides:       tex-conteq-doc
AutoReqProv:    No

%description -n texlive-conteq-doc
Documentation for conteq

%package -n texlive-collection-metapost
Summary:        MetaPost and Metafont packages
Version:        svn44297
Requires:       texlive-base, texlive-collection-basic, tex-automata, tex-bbcard
Requires:       tex-blockdraw_mp, tex-bpolynomial, tex-cmarrows, tex-drv
Requires:       tex-dviincl, tex-emp, tex-epsincl, tex-expressg
Requires:       tex-exteps, tex-featpost, tex-feynmf, tex-feynmp-auto
Requires:       tex-garrigues, tex-gmp, tex-hatching, tex-latexmp
Requires:       tex-mcf2graph, tex-metago, tex-metaobj, tex-metaplot
Requires:       tex-metapost, tex-metauml, tex-mfpic, tex-mfpic4ode
Requires:       tex-mp3d, tex-mparrows, tex-mpcolornames, tex-mpattern
Requires:       tex-mpgraphics, texlive-mptrees, tex-piechartmp, tex-repere
Requires:       tex-roex, tex-roundrect, tex-shapes, tex-slideshow
Requires:       tex-splines, tex-suanpan, tex-textpath, tex-threeddice

%description -n texlive-collection-metapost
collection-metapost package

%package -n texlive-collection-music
Summary:        Music packages
Version:        svn48102
Requires:       texlive-base, texlive-collection-latex, texlive-abc, texlive-autosp
Requires:       texlive-bagpipe, texlive-figbas, texlive-gchords, texlive-gregoriotex
Requires:       texlive-gtrcrd, texlive-guitar, texlive-guitarchordschemes, texlive-harmony
Requires:       texlive-leadsheets, texlive-lilyglyphs, texlive-lyluatex, texlive-m-tx
Requires:       texlive-musicography, texlive-musixguit, texlive-musixtex, texlive-musixtex-fonts
Requires:       texlive-musixtnt, texlive-octave, texlive-piano, texlive-pmx
Requires:       texlive-pmxchords, texlive-songbook, texlive-songs, texlive-xpiano

%description -n texlive-collection-music
Music-related fonts and packages.


%package -n texlive-collection-pstricks
Summary:        PSTricks
Version:        svn48230
Requires:       texlive-base, texlive-collection-basic, texlive-collection-plaingeneric, texlive-auto-pst-pdf
Requires:       texlive-bclogo, texlive-dsptricks, texlive-makeplot, texlive-pdftricks
Requires:       texlive-pdftricks2, texlive-pedigree-perl
Requires:       texlive-psbao, texlive-pst-2dplot, texlive-pst-3d, texlive-pst-3dplot
Requires:       texlive-pst-abspos, texlive-pst-am, texlive-pst-antiprism, texlive-pst-arrow
Requires:       texlive-pst-asr, texlive-pst-bar, texlive-pst-barcode, texlive-pst-bezier
Requires:       texlive-pst-blur, texlive-pst-bspline, texlive-pst-calculate, texlive-pst-calendar
Requires:       texlive-pst-cie, texlive-pst-circ, texlive-pst-coil, texlive-pst-contourplot
Requires:       texlive-pst-cox, texlive-pst-dart, texlive-pst-dbicons, texlive-pst-diffraction
Requires:       texlive-pst-electricfield, texlive-pst-eps
Requires:       texlive-pst-eucl, texlive-pst-exa, texlive-pst-fill, texlive-pst-fit
Requires:       texlive-pst-fr3d, texlive-pst-fractal, texlive-pst-fun, texlive-pst-func
Requires:       texlive-pst-gantt, texlive-pst-geo, texlive-pst-geometrictools, texlive-pst-ghsb
Requires:       texlive-pst-gr3d, texlive-pst-grad, texlive-pst-graphicx, texlive-pst-infixplot
Requires:       texlive-pst-intersect, texlive-pst-jtree
Requires:       texlive-pst-knot, texlive-pst-labo, texlive-pst-layout, texlive-pst-lens
Requires:       texlive-pst-light3d, texlive-pst-magneticfield
Requires:       texlive-pst-math, texlive-pst-mirror, texlive-pst-node, texlive-pst-ob3d
Requires:       texlive-pst-ode, texlive-pst-optexp, texlive-pst-optic, texlive-pst-osci
Requires:       texlive-pst-ovl, texlive-pst-pad, texlive-pst-pdf, texlive-pst-pdgr
Requires:       texlive-pst-perspective, texlive-pst-platon
Requires:       texlive-pst-plot, texlive-pst-poker, texlive-pst-poly, texlive-pst-pulley
Requires:       texlive-pst-qtree, texlive-pst-rputover, texlive-pst-rubans, texlive-pst-shell
Requires:       texlive-pst-sigsys, texlive-pst-slpe, texlive-pst-solarsystem, texlive-pst-solides3d
Requires:       texlive-pst-soroban, texlive-pst-spectra
Requires:       texlive-pst-spinner, texlive-pst-spirograph
Requires:       texlive-pst-stru, texlive-pst-support-doc
Requires:       texlive-pst-text, texlive-pst-thick, texlive-pst-tools, texlive-pst-tree
Requires:       texlive-pst-tvz, texlive-pst-uml, texlive-pst-vectorian, texlive-pst-vehicle
Requires:       texlive-pst-vowel, texlive-pst-vue3d, texlive-pst2pdf, texlive-pstricks
Requires:       texlive-pstricks-add, texlive-pstricks_calcnotes-doc
Requires:       texlive-uml, texlive-vaucanson-g, texlive-vocaltract

%description -n texlive-collection-pstricks
PSTricks core and all add-on packages.

%package -n texlive-collection-publishers
Summary:        Publisher styles, theses, etc
Version:        svn48360
Requires:       texlive-base, texlive-collection-latex, texlive-IEEEconf, texlive-IEEEtran
Requires:       texlive-aastex, texlive-abnt, texlive-abntex2, texlive-acmart
Requires:       texlive-acmconf, texlive-active-conf, texlive-adfathesis, texlive-afparticle
Requires:       texlive-afthesis, texlive-aguplus, texlive-aiaa, texlive-ametsoc
Requires:       texlive-anufinalexam-doc, texlive-aomart
Requires:       texlive-apa, texlive-apa6, texlive-apa6e, texlive-arsclassica
Requires:       texlive-articleingud, texlive-asaetr, texlive-ascelike, texlive-aucklandthesis
Requires:       texlive-bangorcsthesis, texlive-bangorexam
Requires:       texlive-bath-bst, texlive-beamer-FUBerlin
Requires:       texlive-beamer-verona, texlive-beilstein
Requires:       texlive-bgteubner, texlive-br-lex, texlive-brandeis-dissertation, texlive-cascadilla
Requires:       texlive-cesenaexam, texlive-chem-journal
Requires:       texlive-cje, texlive-classicthesis, texlive-cleanthesis, texlive-cmpj
Requires:       texlive-confproc, texlive-cquthesis, texlive-dccpaper, texlive-dithesis
Requires:       texlive-ebook, texlive-ebsthesis, texlive-ejpecp, texlive-ekaia
Requires:       texlive-elbioimp, texlive-elsarticle, texlive-elteikthesis, texlive-emisa
Requires:       texlive-erdc, texlive-estcpmm, texlive-etsvthor, texlive-fbithesis
Requires:       texlive-fcavtex, texlive-fcltxdoc, texlive-fei, texlive-gaceta
Requires:       texlive-gatech-thesis, texlive-gradstudentresume
Requires:       texlive-grant, texlive-gsemthesis, texlive-gzt, texlive-h2020proposal
Requires:       texlive-hagenberg-thesis, texlive-har2nat
Requires:       texlive-hecthese, texlive-hithesis, texlive-hobete, texlive-hustthesis
Requires:       texlive-icsv, texlive-ieeepes, texlive-ijmart, texlive-ijsra
Requires:       texlive-imac, texlive-imtekda, texlive-iscram, texlive-jacow
Requires:       texlive-jmlr, texlive-jnuexam, texlive-jpsj, texlive-kdgdocs
Requires:       texlive-kluwer, texlive-ksp-thesis, texlive-ku-template, texlive-langsci
Requires:       texlive-limecv, texlive-lion-msc, texlive-llncsconf, texlive-lni
Requires:       texlive-lps, texlive-matc3, texlive-matc3mem, texlive-mcmthesis
Requires:       texlive-mentis, texlive-mnras, texlive-msu-thesis, texlive-mucproc
Requires:       texlive-mugsthesis, texlive-musuos, texlive-muthesis, texlive-mynsfc
Requires:       texlive-nature, texlive-navydocs, texlive-nddiss, texlive-ndsu-thesis
Requires:       texlive-novel, texlive-nwejm, texlive-nih, texlive-nihbiosketch
Requires:       texlive-nostarch, texlive-nrc, texlive-onrannual, texlive-opteng
Requires:       texlive-philosophersimprint, texlive-pittetd
Requires:       texlive-pkuthss, texlive-powerdot-FUBerlin
Requires:       texlive-powerdot-tuliplab, texlive-pracjourn
Requires:       texlive-procIAGssymp, texlive-proposal, texlive-ptptex, texlive-psu-thesis
Requires:       texlive-resphilosophica, texlive-resumecls
Requires:       texlive-revtex, texlive-revtex4, texlive-rutitlepage, texlive-ryethesis
Requires:       texlive-sageep, texlive-sapthesis, texlive-scrjrnl, texlive-schule
Requires:       texlive-scientific-thesis-cover, texlive-sduthesis
Requires:       texlive-seuthesis, texlive-seuthesix, texlive-soton, texlive-sphdthesis
Requires:       texlive-spie, texlive-sr-vorl, texlive-stellenbosch, texlive-suftesi
Requires:       texlive-sugconf, texlive-tabriz-thesis, texlive-texilikechaps, texlive-texilikecover
Requires:       texlive-thesis-ekf, texlive-thesis-gwu, texlive-thesis-titlepage-fhac, texlive-thucoursework
Requires:       texlive-thuthesis, texlive-timbreicmc, texlive-tlc-article, texlive-topletter
Requires:       texlive-toptesi, texlive-tudscr, texlive-tugboat, texlive-tugboat-plain
Requires:       texlive-turabian, texlive-tui, texlive-uaclasses, texlive-uafthesis
Requires:       texlive-uantwerpendocs, texlive-ucbthesis
Requires:       texlive-ucdavisthesis, texlive-ucsmonograph
Requires:       texlive-ucthesis, texlive-uestcthesis, texlive-uhhassignment, texlive-uiucredborder
Requires:       texlive-uiucthesis, texlive-ulthese, texlive-umbclegislation, texlive-umthesis
Requires:       texlive-umich-thesis, texlive-unamth-template-doc
Requires:       texlive-unamthesis, texlive-unitn-bimrep
Requires:       texlive-univie-ling, texlive-unswcover, texlive-uothesis, texlive-urcls
Requires:       texlive-uowthesis, texlive-uowthesistitlepage
Requires:       texlive-uspatent, texlive-ut-thesis, texlive-uwthesis, texlive-vancouver
Requires:       texlive-wsemclassic, texlive-xcookybooky
Requires:       texlive-xduthesis, texlive-yathesis, texlive-york-thesis

%description -n texlive-collection-publishers
collection-publishers package

%package -n texlive-confproc
Provides:       tex-confproc = %{tl_version}
License:        LPPL
Summary:        A set of tools for generating conference proceedings
Version:        svn29349.0.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(kvoptions-patch.sty)
Requires:       tex(xifthen.sty), tex(graphicx.sty), tex(pdfpages.sty), tex(fancyhdr.sty)
Requires:       tex(tocbibind.sty), tex(titletoc.sty), tex(multitoc.sty), tex(index.sty)
Requires:       tex(multicol.sty), tex(sectsty.sty), tex(color.sty), tex(hyperref.sty)
Requires:       tex(bookmark.sty)
Provides:       tex(confproc.cfg) = %{tl_version}, tex(confproc.cls) = %{tl_version}
Provides:       tex(newapave.sty) = %{tl_version}

%description -n texlive-confproc
The confproc collection comprises a class, a BibTeX style, and
some scripts for generating conference proceedings. It derives
from LaTeX scripts written for the DAFx-06 conference
proceedings, largely based on the pdfpages package for
including the proceedings papers and the hyperref package for
creating a proper table of contents, bookmarks and general
bibliography back-references. Confproc also uses many other
packages for fine tuning of the table of contents, bibliography
and index of authors. The added value of the class resides in
its time-saving aspects when designing conference proceedings.

%package -n texlive-confproc-doc
Summary:        Documentation for confproc
Version:        svn29349.0.8

Provides:       tex-confproc-doc
AutoReqProv:    No

%description -n texlive-confproc-doc
Documentation for confproc

%package -n texlive-complexity
Provides:       tex-complexity = %{tl_version}
License:        LPPL
Summary:        Computational complexity class names
Version:        svn45322
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(complexity.sty) = %{tl_version}, tex(mycomplexity.sty) = %{tl_version}

%description -n texlive-complexity
Complexity is a LaTeX package that defines commands to typeset
Computational Complexity Classes such as $\P$ and $\NP$ (as
well as hundreds of others). It also offers several options
including which font classes are typeset in and how many are
defined (all of them or just the basic, most commonly used
ones). The package has no dependencies other than the standard
ifthen package.

%package -n texlive-complexity-doc
Summary:        Documentation for complexity
Version:        svn45322
Provides:       tex-complexity-doc
AutoReqProv:    No

%description -n texlive-complexity-doc
Documentation for complexity

%package -n texlive-computational-complexity
Provides:       tex-computational-complexity = %{tl_version}
License:        LPPL
Summary:        Class for the journal Computational Complexity
Version:        svn44847
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fontenc.sty), tex(babel.sty), tex(inputenc.sty), tex(amsmath.sty)
Requires:       tex(amsfonts.sty), tex(amssymb.sty), tex(url.sty), tex(cc2cite.sty)
Requires:       tex(multicol.sty), tex(ccthm.sty), tex(ccalgo.sty), tex(natbib.sty)
Requires:       tex(ccreltx.sty), tex(relabel.sty), tex(theorem.sty), tex(environ.sty)
Requires:       tex(xkeyval.sty), tex(lineno.sty), tex(draftcopy.sty), tex(hyperref.sty)
Requires:       tex(breakurl.sty), tex(graphics.sty), tex(xcolor.sty)
Provides:       tex(cc-cls.sty) = %{tl_version}, tex(cc.cls) = %{tl_version}
Provides:       tex(cc2cite.sty) = %{tl_version}, tex(cc4amsart.sty) = %{tl_version}
Provides:       tex(cc4apjrnl.sty) = %{tl_version}, tex(cc4elsart.sty) = %{tl_version}
Provides:       tex(cc4jT.sty) = %{tl_version}, tex(cc4llncs.sty) = %{tl_version}
Provides:       tex(cc4siamltex.sty) = %{tl_version}, tex(cc4svjour.sty) = %{tl_version}
Provides:       tex(ccalgo.sty) = %{tl_version}, tex(ccaux.sty) = %{tl_version}
Provides:       tex(cccite.sty) = %{tl_version}, tex(ccdbs.sty) = %{tl_version}
Provides:       tex(cclayout.sty) = %{tl_version}, tex(ccproof.sty) = %{tl_version}
Provides:       tex(ccqed.sty) = %{tl_version}, tex(ccref.sty) = %{tl_version}
Provides:       tex(ccreltx.sty) = %{tl_version}, tex(ccthm.sty) = %{tl_version}
Provides:       tex(relabel.sty) = %{tl_version}, tex(thcc.sty) = %{tl_version}

%description -n texlive-computational-complexity
The LaTeX2e class cc was written for the journal Computational
Complexity, and it can also be used for a lot of other
articles. You may like it since it contains a lot of features
as more intelligent references, a set of theorem definitions,
an algorithm environment, ... The class requires natbib.

%package -n texlive-computational-complexity-doc
Summary:        Documentation for computational-complexity
Version:        svn44847
Provides:       tex-computational-complexity-doc
AutoReqProv:    No

%description -n texlive-computational-complexity-doc
Documentation for computational-complexity


%package -n texlive-collection-xetex
Summary:        XeTeX and packages
Version:        svn47630
Requires:       texlive-base, texlive-collection-basic, texlive-arabxetex, texlive-awesomebox
Requires:       texlive-bidi-atbegshi, texlive-bidicontour
Requires:       texlive-bidipagegrid, texlive-bidishadowtext
Requires:       texlive-bidipresentation, texlive-cqubeamer
Requires:       texlive-fixlatvian, texlive-font-change-xetex
Requires:       texlive-fontbook, texlive-fontwrap, texlive-interchar, texlive-na-position
Requires:       texlive-philokalia, texlive-ptext, texlive-quran, texlive-realscripts
Requires:       texlive-simple-resume-cv, texlive-simple-thesis-dissertation
Requires:       texlive-ucharclasses, texlive-unicode-bidi
Requires:       texlive-unisugar, texlive-xebaposter, texlive-xechangebar, texlive-xecjk
Requires:       texlive-xecolor, texlive-xecyr, texlive-xeindex, texlive-xesearch
Requires:       texlive-xespotcolor, texlive-xetex, texlive-xetex-itrans, texlive-xetex-pstricks
Requires:       texlive-xetex-tibetan, texlive-xetexconfig
Requires:       texlive-xetexfontinfo, texlive-xetexko, texlive-xevlna
Provides:       tex(xetex) = %{tl_version}
Obsoletes:      texlive-texmf-xetex < %{tl_version}

%description -n texlive-collection-xetex
Packages for XeTeX, the Unicode/OpenType-enabled TeX by
Jonathan Kew, http://tug.org/xetex.


%package -n texlive-cmdtrack-doc
Provides:       tex-cmdtrack-doc = %{tl_version}
License:        LPPL
Summary:        doc files of cmdtrack
Version:        svn28910

AutoReqProv:    No

%description -n texlive-cmdtrack-doc
Documentation for cmdtrack

%package -n texlive-cmdtrack
Provides:       tex-cmdtrack = %{tl_version}
License:        LPPL
Summary:        Check used commands
Version:        svn28910

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cmdtrack.sty) = %{tl_version}

%description -n texlive-cmdtrack
The package keeps track of whether a command defined in a
document preamble is actually used somewhere in the document.
After the package is loaded in the preamble of a document, all
\newcommand (and similar command definitions) between that
point and the beginning of the document will be marked for
logging. At the end of the document a report of command usage
will be printed in the TeX log, for example: "mdash was used on
line 25"; "ndash was never used".

%package -n texlive-cmexb-doc
Provides:       tex-cmexb-doc = %{tl_version}
License:        Public Domain
Summary:        doc files of cmexb
Version:        svn45677
AutoReqProv:    No

%description -n texlive-cmexb-doc
Documentation for cmexb

%package -n texlive-cmexb
Provides:       tex-cmexb = %{tl_version}
License:        Public Domain
Summary:        PFB font support
Version:        svn45677
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(cmexb.map) = %{tl_version}, tex(cmexb10.pfb) = %{tl_version}
Provides:       tex(cmexb10.tfm) = %{tl_version}

%description -n texlive-cmexb
This package implements PFB font which is accessible normally by Sauter
extrapolation only as bitmap font.

%package -n texlive-cochineal-doc
Provides:       tex-cochineal-doc = %{tl_version}
License:        LPPL and OFL
Summary:        doc files of cochineal
Version:        svn47902
AutoReqProv:    No

%description -n texlive-cochineal-doc
Documentation for cochineal

%package -n texlive-cochineal
Provides:       tex-cochineal = %{tl_version}
License:        LPPL and OFL
Summary:        Cochineal fonts with LaTeX support
Version:        svn47902
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(cochineal.sty) = %{tl_version}, tex(Cochineal.map) = %{tl_version}
Provides:       tex(T1Cochineal-Dnom.fd) = %{tl_version}
Provides:       tex(OT2Cochineal-TLF.fd) = %{tl_version}
Provides:       tex(T1Cochineal-OsF.fd) = %{tl_version}, tex(LY1Cochineal-Sup.fd) = %{tl_version}
Provides:       tex(T1Cochineal-LF.fd) = %{tl_version}, tex(OT1Cochineal-TLF.fd) = %{tl_version}
Provides:       tex(OT1Cochineal-Dnom.fd) = %{tl_version}
Provides:       tex(T2ACochineal-OsF.fd) = %{tl_version}
Provides:       tex(LY1Cochineal-TLF.fd) = %{tl_version}
Provides:       tex(T2ACochineal-Sup.fd) = %{tl_version}
Provides:       tex(omlzcochmi.fd) = %{tl_version}, tex(OT2Cochineal-TOsF.fd) = %{tl_version}
Provides:       tex(LY1Cochineal-OsF.fd) = %{tl_version}
Provides:       tex(T2ACochineal-TLF.fd) = %{tl_version}
Provides:       tex(OT2Cochineal-LF.fd) = %{tl_version}, tex(OT2Cochineal-OsF.fd) = %{tl_version}
Provides:       tex(LY1Cochineal-TOsF.fd) = %{tl_version}
Provides:       tex(T2ACochineal-TOsF.fd) = %{tl_version}
Provides:       tex(T1Cochineal-TLF.fd) = %{tl_version}, tex(OT1Cochineal-Sup.fd) = %{tl_version}
Provides:       tex(LGRCochineal-OsF.fd) = %{tl_version}
Provides:       tex(OT1Cochineal-LF.fd) = %{tl_version}, tex(LGRCochineal-TLF.fd) = %{tl_version}
Provides:       tex(LY1Cochineal-Dnom.fd) = %{tl_version}
Provides:       tex(T1Cochineal-TOsF.fd) = %{tl_version}
Provides:       tex(TS1Cochineal-TLF.fd) = %{tl_version}
Provides:       tex(T1Cochineal-Sup.fd) = %{tl_version}, tex(LGRCochineal-LF.fd) = %{tl_version}
Provides:       tex(TS1Cochineal-LF.fd) = %{tl_version}, tex(LY1Cochineal-LF.fd) = %{tl_version}
Provides:       tex(OT1Cochineal-OsF.fd) = %{tl_version}
Provides:       tex(OT1Cochineal-TOsF.fd) = %{tl_version}
Provides:       tex(OT1Cochineal-Inf.fd) = %{tl_version}
Provides:       tex(TS1Cochineal-TOsF.fd) = %{tl_version}
Provides:       tex(T2ACochineal-LF.fd) = %{tl_version}, tex(uzcochmia.fd) = %{tl_version}
Provides:       tex(LY1Cochineal-Inf.fd) = %{tl_version}
Provides:       tex(T1Cochineal-Inf.fd) = %{tl_version}, tex(LGRCochineal-TOsF.fd) = %{tl_version}
Provides:       tex(TS1Cochineal-OsF.fd) = %{tl_version}
Provides:       tex(Cochineal-Italic.pfb) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Cochineal-Roman.pfb) = %{tl_version}
Provides:       tex(Cochineal-Bold.pfb) = %{tl_version}, tex(coch_nyeh65.enc) = %{tl_version}
Provides:       tex(coch_ecpkno.enc) = %{tl_version}, tex(coch_jdigbj.enc) = %{tl_version}
Provides:       tex(coch_puycuv.enc) = %{tl_version}, tex(cochtosf-lgr.enc) = %{tl_version}
Provides:       tex(coch_bqgjgh.enc) = %{tl_version}, tex(coch_4csisi.enc) = %{tl_version}
Provides:       tex(coch_ejj76u.enc) = %{tl_version}, tex(coch_aa3d23.enc) = %{tl_version}
Provides:       tex(coch_qgajns.enc) = %{tl_version}, tex(coch_bbsuch.enc) = %{tl_version}
Provides:       tex(coch_aawves.enc) = %{tl_version}, tex(coch_ep5tp7.enc) = %{tl_version}
Provides:       tex(coch_iszb2q.enc) = %{tl_version}, tex(coch_zrngc7.enc) = %{tl_version}
Provides:       tex(coch_4gkh24.enc) = %{tl_version}, tex(coch_axmhrg.enc) = %{tl_version}
Provides:       tex(coch_tub2zn.enc) = %{tl_version}, tex(coch_jdlm2x.enc) = %{tl_version}
Provides:       tex(coch_ykcvhy.enc) = %{tl_version}, tex(coch_aazvtb.enc) = %{tl_version}
Provides:       tex(coch_t4kqf4.enc) = %{tl_version}, tex(coch_e56gw4.enc) = %{tl_version}
Provides:       tex(coch_sechmf.enc) = %{tl_version}, tex(cochtabosf.enc) = %{tl_version}
Provides:       tex(cochlf-ot2.enc) = %{tl_version}, tex(cochosf-lgr.enc) = %{tl_version}
Provides:       tex(coch_kbcokb.enc) = %{tl_version}, tex(coch_o5hvxo.enc) = %{tl_version}
Provides:       tex(coch_lnloax.enc) = %{tl_version}, tex(coch_jf7qqq.enc) = %{tl_version}
Provides:       tex(coch_tt64gu.enc) = %{tl_version}, tex(coch_e2lzvu.enc) = %{tl_version}
Provides:       tex(coch_ckzf3x.enc) = %{tl_version}, tex(coch_zlykb2.enc) = %{tl_version}
Provides:       tex(coch_wjhowa.enc) = %{tl_version}, tex(cochtlf-lgr.enc) = %{tl_version}
Provides:       tex(coch_t6yhmv.enc) = %{tl_version}, tex(coch_zbxipy.enc) = %{tl_version}
Provides:       tex(coch_427ufi.enc) = %{tl_version}, tex(coch_ghlqiw.enc) = %{tl_version}
Provides:       tex(coch_r6dow3.enc) = %{tl_version}, tex(coch_ky4gz4.enc) = %{tl_version}
Provides:       tex(coch_ggrwt7.enc) = %{tl_version}, tex(coch_zi6j5g.enc) = %{tl_version}
Provides:       tex(coch_bhg4oq.enc) = %{tl_version}, tex(coch_th53gy.enc) = %{tl_version}
Provides:       tex(coch_av27fu.enc) = %{tl_version}, tex(coch_h3bzlq.enc) = %{tl_version}
Provides:       tex(coch_qanc24.enc) = %{tl_version}, tex(coch_swy4oa.enc) = %{tl_version}
Provides:       tex(coch_7r32ge.enc) = %{tl_version}, tex(coch_jax2k7.enc) = %{tl_version}
Provides:       tex(coch_bwegky.enc) = %{tl_version}, tex(cochtlf-ot2.enc) = %{tl_version}
Provides:       tex(coch_k5ugti.enc) = %{tl_version}, tex(cochalph.enc) = %{tl_version}
Provides:       tex(coch_xp3h6g.enc) = %{tl_version}, tex(coch_zetixv.enc) = %{tl_version}
Provides:       tex(coch_yj5kmj.enc) = %{tl_version}, tex(coch_hflk7g.enc) = %{tl_version}
Provides:       tex(coch_6ycxmb.enc) = %{tl_version}, tex(coch_wpmcrv.enc) = %{tl_version}
Provides:       tex(coch_mnx4cz.enc) = %{tl_version}, tex(cochosf-ot2.enc) = %{tl_version}
Provides:       tex(coch_qnto7n.enc) = %{tl_version}, tex(coch_xmqc3h.enc) = %{tl_version}
Provides:       tex(coch_apxmko.enc) = %{tl_version}, tex(coch_4n5rlh.enc) = %{tl_version}
Provides:       tex(coch_yqw2ok.enc) = %{tl_version}, tex(coch-t2a.enc) = %{tl_version}
Provides:       tex(coch_nlntf7.enc) = %{tl_version}, tex(coch_q5rvqt.enc) = %{tl_version}
Provides:       tex(coch_esig5c.enc) = %{tl_version}, tex(coch_br6git.enc) = %{tl_version}
Provides:       tex(coch_dm4e5q.enc) = %{tl_version}, tex(coch_5to7wu.enc) = %{tl_version}
Provides:       tex(coch_ts1.enc) = %{tl_version}, tex(coch_ajitlz.enc) = %{tl_version}
Provides:       tex(coch_v7zunk.enc) = %{tl_version}, tex(coch_eluacw.enc) = %{tl_version}
Provides:       tex(coch_ddcf5y.enc) = %{tl_version}, tex(coch_ikqf75.enc) = %{tl_version}
Provides:       tex(coch_zmd4fr.enc) = %{tl_version}, tex(coch_wgmzd5.enc) = %{tl_version}
Provides:       tex(coch_p2k67b.enc) = %{tl_version}, tex(coch_rmihs3.enc) = %{tl_version}
Provides:       tex(coch_asaeuh.enc) = %{tl_version}, tex(coch_t24fhx.enc) = %{tl_version}
Provides:       tex(cochtosf-ot2.enc) = %{tl_version}, tex(coch_7xhkhe.enc) = %{tl_version}
Provides:       tex(coch_h42wts.enc) = %{tl_version}, tex(coch_bzchxc.enc) = %{tl_version}
Provides:       tex(coch_no5pci.enc) = %{tl_version}, tex(coch_rxim6w.enc) = %{tl_version}
Provides:       tex(coch_7h3ywq.enc) = %{tl_version}, tex(coch_qu2c3y.enc) = %{tl_version}
Provides:       tex(coch_mzcfhr.enc) = %{tl_version}, tex(coch_pvjnx4.enc) = %{tl_version}
Provides:       tex(coch_7qxkxr.enc) = %{tl_version}, tex(coch_yatyip.enc) = %{tl_version}
Provides:       tex(coch_qsfb2d.enc) = %{tl_version}, tex(coch_4ymbww.enc) = %{tl_version}
Provides:       tex(coch_jxzuzf.enc) = %{tl_version}, tex(coch_ixqghx.enc) = %{tl_version}
Provides:       tex(coch_ofxlj7.enc) = %{tl_version}, tex(coch_s35xpx.enc) = %{tl_version}
Provides:       tex(coch_say5ae.enc) = %{tl_version}, tex(coch_he5a7w.enc) = %{tl_version}
Provides:       tex(coch_4b5cze.enc) = %{tl_version}, tex(coch_gccjw3.enc) = %{tl_version}
Provides:       tex(coch_obm4y4.enc) = %{tl_version}, tex(coch_3zwcy7.enc) = %{tl_version}
Provides:       tex(coch_ffxtzy.enc) = %{tl_version}, tex(coch_nrtjg6.enc) = %{tl_version}
Provides:       tex(coch_dodygp.enc) = %{tl_version}, tex(coch_uowgga.enc) = %{tl_version}
Provides:       tex(coch_v37ibe.enc) = %{tl_version}, tex(coch_hl6u4r.enc) = %{tl_version}
Provides:       tex(coch_uhgdpa.enc) = %{tl_version}, tex(coch_hozeef.enc) = %{tl_version}
Provides:       tex(coch_yhwuat.enc) = %{tl_version}, tex(coch_bikv6i.enc) = %{tl_version}
Provides:       tex(coch_t5kc3u.enc) = %{tl_version}, tex(coch_fidreu.enc) = %{tl_version}
Provides:       tex(coch_jykc3v.enc) = %{tl_version}, tex(coch_hmxcc2.enc) = %{tl_version}
Provides:       tex(coch_7bfc6o.enc) = %{tl_version}, tex(coch_z5rngk.enc) = %{tl_version}
Provides:       tex(coch_lhuxe4.enc) = %{tl_version}, tex(coch_cwqdxq.enc) = %{tl_version}
Provides:       tex(coch_7nwgwv.enc) = %{tl_version}, tex(coch_sqxi2m.enc) = %{tl_version}
Provides:       tex(coch_sm5q6n.enc) = %{tl_version}, tex(cochlf-lgr.enc) = %{tl_version}
Provides:       tex(coch_wndpsq.enc) = %{tl_version}, tex(coch_wasnq6.enc) = %{tl_version}
Provides:       tex(coch_dyebox.enc) = %{tl_version}, tex(coch_w4afvi.enc) = %{tl_version}
Provides:       tex(coch_fuig2f.enc) = %{tl_version}, tex(coch_gff4qk.enc) = %{tl_version}
Provides:       tex(coch_3led4x.enc) = %{tl_version}, tex(coch_7if63h.enc) = %{tl_version}
Provides:       tex(coch_sciel5.enc) = %{tl_version}, tex(coch_lqv5u7.enc) = %{tl_version}
Provides:       tex(coch_6nfbiu.enc) = %{tl_version}, tex(coch_xzomwc.enc) = %{tl_version}
Provides:       tex(coch_2lyzki.enc) = %{tl_version}, tex(coch_sd4a6a.enc) = %{tl_version}
Provides:       tex(coch_4u6kmt.enc) = %{tl_version}, tex(coch_wytr2o.enc) = %{tl_version}
Provides:       tex(coch_uy5zmp.enc) = %{tl_version}, tex(coch_xxmc7z.enc) = %{tl_version}
Provides:       tex(coch_x4y5r2.enc) = %{tl_version}, tex(coch_yska2a.enc) = %{tl_version}
Provides:       tex(coch_35syhy.enc) = %{tl_version}, tex(coch_panfjf.enc) = %{tl_version}
Provides:       tex(coch_3cbpzp.enc) = %{tl_version}, tex(coch_5zktny.enc) = %{tl_version}
Provides:       tex(coch_r66ddu.enc) = %{tl_version}, tex(coch_7lcsbt.enc) = %{tl_version}
Provides:       tex(coch_r7lidj.enc) = %{tl_version}, tex(coch_tmv2ur.enc) = %{tl_version}
Provides:       tex(coch_34w5p5.enc) = %{tl_version}, tex(coch_etswjd.enc) = %{tl_version}
Provides:       tex(coch_in37z4.enc) = %{tl_version}, tex(coch_652ay2.enc) = %{tl_version}
Provides:       tex(Cochineal-Bold.otf) = %{tl_version}, tex(Cochineal-Roman.otf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic.otf) = %{tl_version}
Provides:       tex(Cochineal-Italic.otf) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-sup-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-th-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(zcochbmia.vf) = %{tl_version}, tex(Cochineal-BoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-sup-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-dnom-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-th-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-swash-t2a.vf) = %{tl_version}
Provides:       tex(zcochmi.vf) = %{tl_version}, tex(Cochineal-BoldItalic-tosf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-th-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-dnom-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-inf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-sup-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-inf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-th-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-th-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-dnom-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-dnom-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-sup-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(zcochbmi.vf) = %{tl_version}, tex(Cochineal-Italic-osf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-th-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-sup-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-dnom-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-swash-ly1.vf) = %{tl_version}
Provides:       tex(zcochmia.vf) = %{tl_version}, tex(Cochineal-Roman-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-th-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-th-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-swash-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-inf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-swash-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-sup-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-sup-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-ly1.vf) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-swash-t2a.vf) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-th-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bol-alph.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-sup-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-th-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-sup-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-dnom-t1.tfm) = %{tl_version}
Provides:       tex(zcochmi.tfm) = %{tl_version}, tex(Cochineal-Roman-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-th-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BolIta-alph.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-sup-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-th-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-inf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-th-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-th-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-alph.tfm) = %{tl_version}, tex(Cochineal-Roman-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-th-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-th-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-th-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-th-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(zcochbmia.tfm) = %{tl_version}, tex(Cochineal-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-osf.tfm) = %{tl_version}, tex(Cochineal-Bolditalic-lf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-th-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-th-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-th-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Ita-alph.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-th-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-dnom-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-dnom-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-th-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-th-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bolditalic-tosf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(zcochbmi.tfm) = %{tl_version}, tex(Cochineal-Roman-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bol-osf.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-inf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-th-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-th-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-sup-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-sup-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-dnom-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(zcochmia.tfm) = %{tl_version}, tex(Cochineal-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-sup-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-lf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-swash-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-dnom-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-lf-th-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bolditalic-osf-lgr.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-dnom-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-osf-swash-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-lf-swash-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-swash-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-ot2.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-osf-swash-t2a.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-th-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-swash-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-sup-t2a--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-osf-swash-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Roman-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cochineal-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Cochineal-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(Cochineal-BoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}

%description -n texlive-cochineal
Cochineal is a fork from the Crimson fonts (Roman, Italic,
Bold, BoldItalic only) released under the OFL by Sebastian
Kosch. These remarkable fonts are inspired by the famous
oldstyle fonts in the garalde family (Garamond, Bembo) but, in
the end, look more similar to Minion, though with smaller
xheight and less plain in detail. The Crimson fonts on which
these were based had roughly 4200 glyphs in the four styles
mentioned above. Cochineal adds more than 1500 glyphs in those
styles so that it is possible to make a TeX support collection
that contains essentially all glyphs in all styles. Bringing
the Semibold styles up the same level would have required
adding about 2000 additional glyphs, which I could not even
contemplate. The fonts are provided in OpenType and PostScript
formats.

%package -n texlive-coloring-doc
Provides:       tex-coloring-doc = %{tl_version}
License:        LPPL
Summary:        doc files of coloring
Version:        svn41042

AutoReqProv:    No

%description -n texlive-coloring-doc
Documentation for coloring

%package -n texlive-coloring
Provides:       tex-coloring = %{tl_version}
License:        LPPL
Summary:        Define missing colors by their names
Version:        svn41042

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(coloring.sty) = %{tl_version}

%description -n texlive-coloring
This package makes it possible to define colors automatically
by their names. This can be useful in drawing TikZ pictures and
designing beamer themes. Using the package, you don't need to
write \definecolor before using a color.

%package -n texlive-continue-doc
Provides:       tex-continue-doc = %{tl_version}
License:        LPPL
Summary:        doc files of continue
Version:        svn39308

AutoReqProv:    No

%description -n texlive-continue-doc
Documentation for continue

%package -n texlive-continue
Provides:       tex-continue = %{tl_version}
License:        LPPL
Summary:        Prints 'continuation' marks on recto pages of multipage documents
Version:        svn39308

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(continue.sty) = %{tl_version}

%description -n texlive-continue
The package is an amalgam of Donald Arseneau's fwlw package and
Luca Merciadri's turnthepage package. For multipage twoside
documents it puts a `continuation' mark near the foot of each
odd-numbered page that is followed by another page. The
position and form of the continuation mark may be altered.


%package -n texlive-collection-mathscience
Summary:        Mathematics, natural sciences, computer science packages
Version:        svn48252
Provides:       texlive-collection-science = %{epoch}:svn39074.obsolete
Obsoletes:      texlive-collection-science <= 6:svn39074
Provides:       texlive-collection-mathextra = %{epoch}:svn40076.obsolete
Obsoletes:      texlive-collection-mathextra <= 6:svn40076
Requires:       texlive-base, texlive-collection-fontsrecommended
Requires:       texlive-collection-latex, texlive-12many
Requires:       texlive-SIstyle, texlive-SIunits, texlive-alg, texlive-algobox
Requires:       texlive-algorithm2e, texlive-algorithmicx
Requires:       texlive-algorithms, texlive-aligned-overset
Requires:       texlive-amstex, texlive-apxproof, texlive-autobreak, texlive-axodraw2
Requires:       texlive-backnaur, texlive-begriff, texlive-binomexp, texlive-biocon
Requires:       texlive-bitpattern, texlive-bohr, texlive-boldtensors, texlive-bosisio
Requires:       texlive-bpchem, texlive-bropd, texlive-bytefield, texlive-calculation
Requires:       texlive-cascade, texlive-ccfonts, texlive-chemarrow, texlive-chemcompounds
Requires:       texlive-chemcono, texlive-chemexec, texlive-chemformula, texlive-chemgreek
Requires:       texlive-chemmacros, texlive-chemnum, texlive-chemschemex, texlive-chemsec
Requires:       texlive-chemstyle, texlive-clrscode, texlive-clrscode3e, texlive-commath
Requires:       texlive-complexity, texlive-computational-complexity
Requires:       texlive-concmath, texlive-concrete, texlive-conteq, texlive-correctmathalign
Requires:       texlive-cryptocode, texlive-delim, texlive-delimset, texlive-delimseasy
Requires:       texlive-diffcoeff, texlive-digiconfigs, texlive-dijkstra, texlive-drawmatrix
Requires:       texlive-drawstack, texlive-dyntree, texlive-ebproof, texlive-econometrics
Requires:       texlive-eltex, texlive-emf, texlive-endiagram, texlive-engtlc
Requires:       texlive-eqnarray, texlive-eqnnumwarn, texlive-extarrows, texlive-extpfeil
Requires:       texlive-faktor, texlive-fnspe, texlive-fouridx, texlive-functan
Requires:       texlive-galois, texlive-gastex, texlive-gene-logic, texlive-ghsystem
Requires:       texlive-gotoh, texlive-grundgesetze, texlive-gu, texlive-hep
Requires:       texlive-hepnames, texlive-hepparticles, texlive-hepthesis, texlive-hepunits
Requires:       texlive-includernw, texlive-interval, texlive-ionumbers, texlive-isomath
Requires:       texlive-karnaugh, texlive-karnaugh-map, texlive-karnaughmap, texlive-logicproof
Requires:       texlive-longdivision, texlive-lpform, texlive-lplfitch, texlive-lstbayes
Requires:       texlive-mathcomp, texlive-mathfixs, texlive-mathpartir, texlive-mathpunctspace
Requires:       texlive-matlab-prettifier, texlive-mattens
Requires:       texlive-mgltex, texlive-mhchem, texlive-mhequ, texlive-miller
Requires:       texlive-multiobjective, texlive-mychemistry
Requires:       texlive-natded, texlive-nath, texlive-nicematrix, texlive-nuc
Requires:       texlive-nucleardata, texlive-objectz, texlive-oplotsymbl, texlive-ot-tableau
Requires:       texlive-oubraces, texlive-perfectcut, texlive-physics, texlive-pm-isomath
Requires:       texlive-polexpr, texlive-prftree, texlive-proba, texlive-prooftrees
Requires:       texlive-pseudocode, texlive-pygmentex, texlive-pythonhighlight, texlive-rec-thy
Requires:       texlive-revquantum, texlive-ribbonproofs
Requires:       texlive-rmathbr, texlive-sasnrdisplay, texlive-sciposter, texlive-sclang-prettifier
Requires:       texlive-scratchx, texlive-sesamanuel, texlive-sfg, texlive-shuffle
Requires:       texlive-simpler-wick, texlive-simplewick
Requires:       texlive-siunitx, texlive-skmath, texlive-spalign, texlive-stanli
Requires:       texlive-statex, texlive-statex2, texlive-statistics, texlive-statistik
Requires:       texlive-statmath, texlive-steinmetz, texlive-stmaryrd, texlive-structmech
Requires:       texlive-struktex, texlive-substances, texlive-subsupscripts, texlive-susy
Requires:       texlive-syllogism, texlive-sympytexpackage
Requires:       texlive-synproof, texlive-t-angles, texlive-tablor, texlive-tensor
Requires:       texlive-tex-ewd, texlive-textgreek, texlive-textopo, texlive-thmbox
Requires:       texlive-turnstile, texlive-ulqda, texlive-unitsdef, texlive-venn
Requires:       texlive-witharrows, texlive-xymtex, texlive-yhmath, texlive-youngtab
Requires:       texlive-ytableau

%description -n texlive-collection-mathscience
Mathematics, natural sciences, computer science packages

%package -n texlive-collection-plaingeneric
Summary:        Plain (La)TeX packages
Version:        svn47878
Provides:       texlive-collection-genericrecommended = svn35655.0.obsolete
Obsoletes:      texlive-collection-genericrecommended <= svn35655.0
Provides:       texlive-collection-genericextra = svn39964.obsolete
Obsoletes:      texlive-collection-genericextra <= svn39964
Provides:       texlive-collection-plainextra = svn37156.0.obsolete
Obsoletes:      texlive-collection-plainextra <= svn37156.0
Requires:       texlive-base, texlive-collection-basic, texlive-abbr, texlive-abstyles
Requires:       texlive-apnum, texlive-autoaligne, texlive-barr, texlive-bitelist
Requires:       texlive-borceux, texlive-c-pascal, texlive-catcodes, texlive-chronosys
Requires:       texlive-colorsep, texlive-dinat, texlive-dirtree, texlive-docbytex
Requires:       texlive-dowith, texlive-eijkhout, texlive-encxvlna, texlive-epigram
Requires:       texlive-epsf, texlive-epsf-dvipdfmx, texlive-fenixpar, texlive-figflow
Requires:       texlive-fixpdfmag, texlive-fltpoint, texlive-fntproof, texlive-font-change
Requires:       texlive-fontch, texlive-fontname, texlive-gates, texlive-genmisc
Requires:       texlive-getoptk, texlive-gfnotation, texlive-gobble, texlive-graphics-pln
Requires:       texlive-gtl, texlive-hlist, texlive-hyplain, texlive-ifetex
Requires:       texlive-iftex, texlive-insbox, texlive-js-misc, texlive-kastrup
Requires:       texlive-lambda-lists, texlive-langcode, texlive-lecturer, texlive-librarian
Requires:       texlive-listofitems, texlive-mathdots, texlive-metatex, texlive-midnight
Requires:       texlive-mkpattern, texlive-modulus, texlive-multido, texlive-navigator
Requires:       texlive-newsletr, texlive-ofs, texlive-olsak-misc, texlive-path
Requires:       texlive-pdf-trans, texlive-pitex, texlive-placeins-plain, texlive-plainpkg
Requires:       texlive-plipsum, texlive-plnfss, texlive-plstmary, texlive-present
Requires:       texlive-randomlist, texlive-resumemac, texlive-schemata, texlive-shade
Requires:       texlive-simplekv, texlive-systeme, texlive-tabto-generic, texlive-termmenu
Requires:       texlive-tex-ps, texlive-tex4ht, texlive-texapi, texlive-texdate
Requires:       texinfo-tex, texlive-timetable, texlive-tracklang, texlive-treetex
Requires:       texlive-trigonometry, texlive-ulem, texlive-upca, texlive-varisize
Requires:       texlive-xii-doc, texlive-xii-lat, texlive-xlop, texlive-yax

%description -n texlive-collection-plaingeneric
Add-on packages and macros that work with plain TeX, often LaTeX, and 
occasionally other formats.

%package -n texlive-cje
Summary:        LaTeX document class for CJE articles
Version:        svn46721
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(cje.cls) = %{tl_version}, tex(cjenatbib.sty) = %{tl_version}
Provides:       tex(cjeupmath.sty) = %{tl_version}

%description -n texlive-cje
The cje article class allows authors to format their papers to
Canadian Journal of Economics style with minimum effort. The
class includes options for two other formats: "review" (double
spaced, for use at the submission stage) and "proof" (used by
the typesetters to prepare the proof authors will receive for
approval).

%package -n texlive-collection-texworks
Summary:        TeXworks editor; TL includes only the Windows binary
Version:        svn36934
License:        LPPL
Requires:       texlive-base texlive-kpathsea, texlive-collection-basic
Requires:       texlive-texworks-doc

%description -n texlive-collection-texworks
See http://tug.org/texworks.

%package -n texlive-combofont
Summary:        Add NFSS-declarations of combo fonts to LuaLaTeX documents
Version:        svn44746
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(combofont.sty) = %{tl_version}

%description -n texlive-combofont
This highly experimental package can be used to add
NFSS-declarations of combo fonts to LuaLaTeX documents. This
package may disappear without notice, e.g. if luaotfload
changes in a way so that it no longer works, or if LuaTeX
changes, or if fontspec itself includes the code. It is also
possible that the package's syntax and commands may change in
an incompatible way. So if you use it in a production
environment: You have been warned.

%package -n texlive-context-cmscbf
Summary:        Use Computer Modern bold Caps and Small-caps in ConTeXt
Version:        svn47085
License:        GPL+
Requires:       texlive-base texlive-kpathsea, texlive-context
Provides:       tex(t-cmscbf.tex) = %{tl_version}

%description -n texlive-context-cmscbf
The module makes provision for bold caps and small caps CM
fonts, in ConTeXt. Such a font may be found in the Computer
Modern 'extras' font set.

%package -n texlive-context-cmttbf
Summary:        Use Computer Modern Typewriter bold font in ConTeXt
Version:        svn47085
License:        GPL+
Requires:       texlive-base texlive-kpathsea, texlive-context
Provides:       tex(t-cmttbf.tex) = %{tl_version}

%description -n texlive-context-cmttbf
The module makes provision for bold typewriter CM fonts, in
ConTeXt. Such a font may be found in the Computer Modern
'extras' font set.

%package -n texlive-context-inifile
Summary:        An ini-file pretty-printer, using ConTeXt
Version:        svn47085
License:        GPL+
Requires:       texlive-base texlive-kpathsea, texlive-context
Provides:       tex(t-inifile.tex) = %{tl_version}

%description -n texlive-context-inifile
The module parses an ini-file and prints the contents with a
user-defined layout. The entries of the file may be sorted by
up to three sort keys. The format of a simple ini-file would
be: [key1] symbol1 = value1 symbol2 = value2 [key2] symbol1 =
value3 symbol2 = value4 The module only works with ConTeXt
MkIV, and uses Lua to help process the input.

%package -n texlive-context-layout
Summary:        Shows layout of current page
Version:        svn47085
License:        GPL+
Requires:       texlive-base texlive-kpathsea, texlive-context
Provides:       tex(t-layout.tex) = %{tl_version}

%description -n texlive-context-layout
Context module to show the layout of the current page.

%package -n texlive-conv-xkv
Summary:        Create new key-value syntax
Version:        svn43558
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(conv-xkv.sty) = %{tl_version}

%description -n texlive-conv-xkv
This small package supports key-value syntax other than the
standard LaTeX syntax of <key>=<value>. Using this package,
create key-values of the form <key>:<value> or <key>-><value>,
for example. The package converts the new notation to xkeyval
notation and passes it on to xkeyval.

%package -n texlive-cooking-units
Summary:        Typeset and convert units for cookery books and recipes
Version:        svn47943
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(cooking-units.sty) = %{tl_version}

%description -n texlive-cooking-units
The package provides commands to typeset amounts and units
consistently and offers an easy to use key-value-syntax to
convert one unit into another (for example 'dag' to 'g'; see
the documentation for more examples).

%package -n texlive-cormorantgaramond
Summary:        Cormorant Garamond family of fonts
Version:        svn41865
License:        OFL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(cgrm_26xgja.enc) = %{tl_version}, tex(cgrm_3urj7q.enc) = %{tl_version}
Provides:       tex(cgrm_5bvaob.enc) = %{tl_version}, tex(cgrm_5dp753.enc) = %{tl_version}
Provides:       tex(cgrm_5eibsx.enc) = %{tl_version}, tex(cgrm_5fi625.enc) = %{tl_version}
Provides:       tex(cgrm_5iz3qq.enc) = %{tl_version}, tex(cgrm_7cbfyt.enc) = %{tl_version}
Provides:       tex(cgrm_baamnb.enc) = %{tl_version}, tex(cgrm_bay3j6.enc) = %{tl_version}
Provides:       tex(cgrm_beooxx.enc) = %{tl_version}, tex(cgrm_bvfij3.enc) = %{tl_version}
Provides:       tex(cgrm_bya7bs.enc) = %{tl_version}, tex(cgrm_cfmksg.enc) = %{tl_version}
Provides:       tex(cgrm_d4lowr.enc) = %{tl_version}, tex(cgrm_d5lut3.enc) = %{tl_version}
Provides:       tex(cgrm_fgdmu7.enc) = %{tl_version}, tex(cgrm_fwfywj.enc) = %{tl_version}
Provides:       tex(cgrm_g6ttj3.enc) = %{tl_version}, tex(cgrm_g7anru.enc) = %{tl_version}
Provides:       tex(cgrm_govhzk.enc) = %{tl_version}, tex(cgrm_hku26s.enc) = %{tl_version}
Provides:       tex(cgrm_hrazmi.enc) = %{tl_version}, tex(cgrm_iergss.enc) = %{tl_version}
Provides:       tex(cgrm_igtdz2.enc) = %{tl_version}, tex(cgrm_isz43y.enc) = %{tl_version}
Provides:       tex(cgrm_jzrauo.enc) = %{tl_version}, tex(cgrm_ktrj5x.enc) = %{tl_version}
Provides:       tex(cgrm_od3ly4.enc) = %{tl_version}, tex(cgrm_pcjf72.enc) = %{tl_version}
Provides:       tex(cgrm_pgha5c.enc) = %{tl_version}, tex(cgrm_qbhsri.enc) = %{tl_version}
Provides:       tex(cgrm_qes6gh.enc) = %{tl_version}, tex(cgrm_qnrqqg.enc) = %{tl_version}
Provides:       tex(cgrm_rdmvvp.enc) = %{tl_version}, tex(cgrm_rqn3dj.enc) = %{tl_version}
Provides:       tex(cgrm_sowbon.enc) = %{tl_version}, tex(cgrm_tiy3fr.enc) = %{tl_version}
Provides:       tex(cgrm_tj5gps.enc) = %{tl_version}, tex(cgrm_vh2m2v.enc) = %{tl_version}
Provides:       tex(cgrm_vuc6nl.enc) = %{tl_version}, tex(cgrm_vvuep5.enc) = %{tl_version}
Provides:       tex(cgrm_x4eod7.enc) = %{tl_version}, tex(cgrm_xg77ac.enc) = %{tl_version}
Provides:       tex(cgrm_xj3e4i.enc) = %{tl_version}, tex(cgrm_zcfdr3.enc) = %{tl_version}
Provides:       tex(CormorantGaramond.map) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold.otf) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic.otf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light.otf) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic.otf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium.otf) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic.otf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular.otf) = %{tl_version}
Provides:       tex(CormorantGaramond-RegularItalic.otf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold.otf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic.otf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-inf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-inf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-inf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-sup-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-sup-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-sup-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-inf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-inf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-inf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-sup-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-sup-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-sup-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-inf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-inf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-inf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-sup-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-sup-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-sup-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-inf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-sup-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold.pfb) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic.pfb) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic.pfb) = %{tl_version}
Provides:       tex(CormorantGaramond-Light.pfb) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic.pfb) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium.pfb) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic.pfb) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular.pfb) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold.pfb) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic.pfb) = %{tl_version}
Provides:       tex(CormorantGaramond.sty) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-inf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-lf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-osf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-sup-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Light-tosf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-LightItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-inf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-lf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-osf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-sup-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Medium-tosf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-MediumItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-inf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-osf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-sup-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-Regular-tosf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-inf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-lf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-osf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-sup-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-sc-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(CormorantGaramond-SemiBoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LY1CormorantGaramond-Inf.fd) = %{tl_version}
Provides:       tex(LY1CormorantGaramond-LF.fd) = %{tl_version}
Provides:       tex(LY1CormorantGaramond-OsF.fd) = %{tl_version}
Provides:       tex(LY1CormorantGaramond-Sup.fd) = %{tl_version}
Provides:       tex(LY1CormorantGaramond-TLF.fd) = %{tl_version}
Provides:       tex(LY1CormorantGaramond-TOsF.fd) = %{tl_version}
Provides:       tex(OT1CormorantGaramond-Inf.fd) = %{tl_version}
Provides:       tex(OT1CormorantGaramond-LF.fd) = %{tl_version}
Provides:       tex(OT1CormorantGaramond-OsF.fd) = %{tl_version}
Provides:       tex(OT1CormorantGaramond-Sup.fd) = %{tl_version}
Provides:       tex(OT1CormorantGaramond-TLF.fd) = %{tl_version}
Provides:       tex(OT1CormorantGaramond-TOsF.fd) = %{tl_version}
Provides:       tex(T1CormorantGaramond-Inf.fd) = %{tl_version}
Provides:       tex(T1CormorantGaramond-LF.fd) = %{tl_version}
Provides:       tex(T1CormorantGaramond-OsF.fd) = %{tl_version}
Provides:       tex(T1CormorantGaramond-Sup.fd) = %{tl_version}
Provides:       tex(T1CormorantGaramond-TLF.fd) = %{tl_version}
Provides:       tex(T1CormorantGaramond-TOsF.fd) = %{tl_version}
Provides:       tex(TS1CormorantGaramond-LF.fd) = %{tl_version}
Provides:       tex(TS1CormorantGaramond-OsF.fd) = %{tl_version}
Provides:       tex(TS1CormorantGaramond-TLF.fd) = %{tl_version}
Provides:       tex(TS1CormorantGaramond-TOsF.fd) = %{tl_version}

%description -n texlive-cormorantgaramond
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Cormorant Garamond family of fonts, designed by
Christian Thalman of Catharsis Fonts. The family includes
light, regular, medium, semi-bold and bold weights, with
italics.


%package -n texlive-citeref
Summary:        Add reference-page-list to bibliography-items
Version:        svn47407
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(citeref.sty) = %{tl_version}

%description -n texlive-citeref
The package does its job without using the indexing facilities,
and needs no special \cite-replacement package.

%package -n texlive-clrdblpg
Summary:        Control pagestyle of pages left blank by \cleardoublepage
Version:        svn47511
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(clrdblpg.sty) = %{tl_version}

%description -n texlive-clrdblpg
This tiny package allows easy manipulation of the headers and
footers on pages left blank by \cleardoublepage. By default,
LaTeX has no easy facilities for this. This package uses more
or less the algorithm listed in the fancyhdr package
documentation, with some better indentation and added
flexibility.

%package -n texlive-clrstrip
Summary:        Place contents into a full width colour strip
Version:        svn48313
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(clrstrip.sty) = %{tl_version}

%description -n texlive-clrstrip
This lightweight package provides the colorstrip environment,
that places its contents into a full page width colour strip.

%package -n texlive-cm-mf-extra-bold
Summary:        Extra Metafont files for CM
Version:        svn45796
License:        GPL+ and Public Domain
Requires:       texlive-base texlive-kpathsea
Provides:       tex(cmbcsc10.mf) = %{tl_version}, tex(cmbtex10.mf) = %{tl_version}
Provides:       tex(cmbtt10.mf) = %{tl_version}, tex(cmbtt8.mf) = %{tl_version}
Provides:       tex(cmbtt9.mf) = %{tl_version}, tex(cmexb10.mf) = %{tl_version}
Provides:       tex(cmttb10.mf) = %{tl_version}, tex(cmbcsc10.tfm) = %{tl_version}
Provides:       tex(cmbtex10.tfm) = %{tl_version}, tex(cmbtt10.tfm) = %{tl_version}
Provides:       tex(cmbtt8.tfm) = %{tl_version}, tex(cmbtt9.tfm) = %{tl_version}
Provides:       tex(cmttb10.tfm) = %{tl_version}

%description -n texlive-cm-mf-extra-bold
The bundle provides bold versions of cmcsc, cmex, cmtex and
cmtt fonts (all parts of the standard computer modern font
distribution), as Metafont base files.

%package -n texlive-cmsrb
Summary:        Computer Modern for Serbian and Macedonian
Version:        svn46588
License:        GPL+
Requires:       texlive-base texlive-kpathsea
Provides:       tex(cmsrbrb.afm) = %{tl_version}, tex(cmsrbrc.afm) = %{tl_version}
Provides:       tex(cmsrbrd.afm) = %{tl_version}, tex(cmsrbri.afm) = %{tl_version}
Provides:       tex(cmsrbrr.afm) = %{tl_version}, tex(cmsrbrs.afm) = %{tl_version}
Provides:       tex(cmsrbrx.afm) = %{tl_version}, tex(cmsrbry.afm) = %{tl_version}
Provides:       tex(cmsrbsb.afm) = %{tl_version}, tex(cmsrbsr.afm) = %{tl_version}
Provides:       tex(cmsrbss.afm) = %{tl_version}, tex(cmsrbst.afm) = %{tl_version}
Provides:       tex(cmsrbtc.afm) = %{tl_version}, tex(cmsrbti.afm) = %{tl_version}
Provides:       tex(cmsrbtr.afm) = %{tl_version}, tex(cmsrbts.afm) = %{tl_version}
Provides:       tex(cmsrbot2.enc) = %{tl_version}, tex(cmsrbt1.enc) = %{tl_version}
Provides:       tex(cmsrbt2a.enc) = %{tl_version}, tex(cmsrbts1.enc) = %{tl_version}
Provides:       tex(cmsrbx2.enc) = %{tl_version}, tex(cmsrb.map) = %{tl_version}
Provides:       tex(ot2cmsrbrb-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbrb.tfm) = %{tl_version}, tex(ot2cmsrbrc-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbrc.tfm) = %{tl_version}, tex(ot2cmsrbrd-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbrd.tfm) = %{tl_version}, tex(ot2cmsrbri-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbri.tfm) = %{tl_version}, tex(ot2cmsrbrr-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbrr.tfm) = %{tl_version}, tex(ot2cmsrbrs-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbrs.tfm) = %{tl_version}, tex(ot2cmsrbrx-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbrx.tfm) = %{tl_version}, tex(ot2cmsrbry-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbry.tfm) = %{tl_version}, tex(ot2cmsrbsb-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbsb.tfm) = %{tl_version}, tex(ot2cmsrbsr-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbsr.tfm) = %{tl_version}, tex(ot2cmsrbss-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbss.tfm) = %{tl_version}, tex(ot2cmsrbst-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbst.tfm) = %{tl_version}, tex(ot2cmsrbtc-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbtc.tfm) = %{tl_version}, tex(ot2cmsrbti-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbti.tfm) = %{tl_version}, tex(ot2cmsrbtr-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbtr.tfm) = %{tl_version}, tex(ot2cmsrbts-base.tfm) = %{tl_version}
Provides:       tex(ot2cmsrbts.tfm) = %{tl_version}, tex(t1cmsrbrb-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbrb.tfm) = %{tl_version}, tex(t1cmsrbrc-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbrc.tfm) = %{tl_version}, tex(t1cmsrbrd-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbrd.tfm) = %{tl_version}, tex(t1cmsrbri-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbri.tfm) = %{tl_version}, tex(t1cmsrbrr-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbrr.tfm) = %{tl_version}, tex(t1cmsrbrs-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbrs.tfm) = %{tl_version}, tex(t1cmsrbrx-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbrx.tfm) = %{tl_version}, tex(t1cmsrbry-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbry.tfm) = %{tl_version}, tex(t1cmsrbsb-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbsb.tfm) = %{tl_version}, tex(t1cmsrbsr-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbsr.tfm) = %{tl_version}, tex(t1cmsrbss-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbss.tfm) = %{tl_version}, tex(t1cmsrbst-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbst.tfm) = %{tl_version}, tex(t1cmsrbtc-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbtc.tfm) = %{tl_version}, tex(t1cmsrbti-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbti.tfm) = %{tl_version}, tex(t1cmsrbtr-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbtr.tfm) = %{tl_version}, tex(t1cmsrbts-base.tfm) = %{tl_version}
Provides:       tex(t1cmsrbts.tfm) = %{tl_version}, tex(t2acmsrbrb-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbrb.tfm) = %{tl_version}, tex(t2acmsrbrc-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbrc.tfm) = %{tl_version}, tex(t2acmsrbrd-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbrd.tfm) = %{tl_version}, tex(t2acmsrbri-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbri.tfm) = %{tl_version}, tex(t2acmsrbrr-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbrr.tfm) = %{tl_version}, tex(t2acmsrbrs-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbrs.tfm) = %{tl_version}, tex(t2acmsrbrx-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbrx.tfm) = %{tl_version}, tex(t2acmsrbry-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbry.tfm) = %{tl_version}, tex(t2acmsrbsb-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbsb.tfm) = %{tl_version}, tex(t2acmsrbsr-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbsr.tfm) = %{tl_version}, tex(t2acmsrbss-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbss.tfm) = %{tl_version}, tex(t2acmsrbst-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbst.tfm) = %{tl_version}, tex(t2acmsrbtc-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbtc.tfm) = %{tl_version}, tex(t2acmsrbti-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbti.tfm) = %{tl_version}, tex(t2acmsrbtr-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbtr.tfm) = %{tl_version}, tex(t2acmsrbts-base.tfm) = %{tl_version}
Provides:       tex(t2acmsrbts.tfm) = %{tl_version}, tex(ts1cmsrbrb-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbrb.tfm) = %{tl_version}, tex(ts1cmsrbrc-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbrc.tfm) = %{tl_version}, tex(ts1cmsrbrd-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbrd.tfm) = %{tl_version}, tex(ts1cmsrbri-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbri.tfm) = %{tl_version}, tex(ts1cmsrbrr-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbrr.tfm) = %{tl_version}, tex(ts1cmsrbrs-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbrs.tfm) = %{tl_version}, tex(ts1cmsrbrx-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbrx.tfm) = %{tl_version}, tex(ts1cmsrbry-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbry.tfm) = %{tl_version}, tex(ts1cmsrbsb-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbsb.tfm) = %{tl_version}, tex(ts1cmsrbsr-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbsr.tfm) = %{tl_version}, tex(ts1cmsrbss-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbss.tfm) = %{tl_version}, tex(ts1cmsrbst-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbst.tfm) = %{tl_version}, tex(ts1cmsrbtc-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbtc.tfm) = %{tl_version}, tex(ts1cmsrbti-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbti.tfm) = %{tl_version}, tex(ts1cmsrbtr-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbtr.tfm) = %{tl_version}, tex(ts1cmsrbts-base.tfm) = %{tl_version}
Provides:       tex(ts1cmsrbts.tfm) = %{tl_version}, tex(x2cmsrbrb-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbrb.tfm) = %{tl_version}, tex(x2cmsrbrc-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbrc.tfm) = %{tl_version}, tex(x2cmsrbrd-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbrd.tfm) = %{tl_version}, tex(x2cmsrbri-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbri.tfm) = %{tl_version}, tex(x2cmsrbrr-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbrr.tfm) = %{tl_version}, tex(x2cmsrbrs-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbrs.tfm) = %{tl_version}, tex(x2cmsrbrx-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbrx.tfm) = %{tl_version}, tex(x2cmsrbry-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbry.tfm) = %{tl_version}, tex(x2cmsrbsb-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbsb.tfm) = %{tl_version}, tex(x2cmsrbsr-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbsr.tfm) = %{tl_version}, tex(x2cmsrbss-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbss.tfm) = %{tl_version}, tex(x2cmsrbst-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbst.tfm) = %{tl_version}, tex(x2cmsrbtc-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbtc.tfm) = %{tl_version}, tex(x2cmsrbti-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbti.tfm) = %{tl_version}, tex(x2cmsrbtr-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbtr.tfm) = %{tl_version}, tex(x2cmsrbts-base.tfm) = %{tl_version}
Provides:       tex(x2cmsrbts.tfm) = %{tl_version}, tex(cmsrbrb.pfb) = %{tl_version}
Provides:       tex(cmsrbrc.pfb) = %{tl_version}, tex(cmsrbrd.pfb) = %{tl_version}
Provides:       tex(cmsrbri.pfb) = %{tl_version}, tex(cmsrbrr.pfb) = %{tl_version}
Provides:       tex(cmsrbrs.pfb) = %{tl_version}, tex(cmsrbrx.pfb) = %{tl_version}
Provides:       tex(cmsrbry.pfb) = %{tl_version}, tex(cmsrbsb.pfb) = %{tl_version}
Provides:       tex(cmsrbsr.pfb) = %{tl_version}, tex(cmsrbss.pfb) = %{tl_version}
Provides:       tex(cmsrbst.pfb) = %{tl_version}, tex(cmsrbtc.pfb) = %{tl_version}
Provides:       tex(cmsrbti.pfb) = %{tl_version}, tex(cmsrbtr.pfb) = %{tl_version}
Provides:       tex(cmsrbts.pfb) = %{tl_version}, tex(ot2cmsrbrb.vf) = %{tl_version}
Provides:       tex(ot2cmsrbrc.vf) = %{tl_version}, tex(ot2cmsrbrd.vf) = %{tl_version}
Provides:       tex(ot2cmsrbri.vf) = %{tl_version}, tex(ot2cmsrbrr.vf) = %{tl_version}
Provides:       tex(ot2cmsrbrs.vf) = %{tl_version}, tex(ot2cmsrbrx.vf) = %{tl_version}
Provides:       tex(ot2cmsrbry.vf) = %{tl_version}, tex(ot2cmsrbsb.vf) = %{tl_version}
Provides:       tex(ot2cmsrbsr.vf) = %{tl_version}, tex(ot2cmsrbss.vf) = %{tl_version}
Provides:       tex(ot2cmsrbst.vf) = %{tl_version}, tex(ot2cmsrbtc.vf) = %{tl_version}
Provides:       tex(ot2cmsrbti.vf) = %{tl_version}, tex(ot2cmsrbtr.vf) = %{tl_version}
Provides:       tex(ot2cmsrbts.vf) = %{tl_version}, tex(t1cmsrbrb.vf) = %{tl_version}
Provides:       tex(t1cmsrbrc.vf) = %{tl_version}, tex(t1cmsrbrd.vf) = %{tl_version}
Provides:       tex(t1cmsrbri.vf) = %{tl_version}, tex(t1cmsrbrr.vf) = %{tl_version}
Provides:       tex(t1cmsrbrs.vf) = %{tl_version}, tex(t1cmsrbrx.vf) = %{tl_version}
Provides:       tex(t1cmsrbry.vf) = %{tl_version}, tex(t1cmsrbsb.vf) = %{tl_version}
Provides:       tex(t1cmsrbsr.vf) = %{tl_version}, tex(t1cmsrbss.vf) = %{tl_version}
Provides:       tex(t1cmsrbst.vf) = %{tl_version}, tex(t1cmsrbtc.vf) = %{tl_version}
Provides:       tex(t1cmsrbti.vf) = %{tl_version}, tex(t1cmsrbtr.vf) = %{tl_version}
Provides:       tex(t1cmsrbts.vf) = %{tl_version}, tex(t2acmsrbrb.vf) = %{tl_version}
Provides:       tex(t2acmsrbrc.vf) = %{tl_version}, tex(t2acmsrbrd.vf) = %{tl_version}
Provides:       tex(t2acmsrbri.vf) = %{tl_version}, tex(t2acmsrbrr.vf) = %{tl_version}
Provides:       tex(t2acmsrbrs.vf) = %{tl_version}, tex(t2acmsrbrx.vf) = %{tl_version}
Provides:       tex(t2acmsrbry.vf) = %{tl_version}, tex(t2acmsrbsb.vf) = %{tl_version}
Provides:       tex(t2acmsrbsr.vf) = %{tl_version}, tex(t2acmsrbss.vf) = %{tl_version}
Provides:       tex(t2acmsrbst.vf) = %{tl_version}, tex(t2acmsrbtc.vf) = %{tl_version}
Provides:       tex(t2acmsrbti.vf) = %{tl_version}, tex(t2acmsrbtr.vf) = %{tl_version}
Provides:       tex(t2acmsrbts.vf) = %{tl_version}, tex(ts1cmsrbrb.vf) = %{tl_version}
Provides:       tex(ts1cmsrbrc.vf) = %{tl_version}, tex(ts1cmsrbrd.vf) = %{tl_version}
Provides:       tex(ts1cmsrbri.vf) = %{tl_version}, tex(ts1cmsrbrr.vf) = %{tl_version}
Provides:       tex(ts1cmsrbrs.vf) = %{tl_version}, tex(ts1cmsrbrx.vf) = %{tl_version}
Provides:       tex(ts1cmsrbry.vf) = %{tl_version}, tex(ts1cmsrbsb.vf) = %{tl_version}
Provides:       tex(ts1cmsrbsr.vf) = %{tl_version}, tex(ts1cmsrbss.vf) = %{tl_version}
Provides:       tex(ts1cmsrbst.vf) = %{tl_version}, tex(ts1cmsrbtc.vf) = %{tl_version}
Provides:       tex(ts1cmsrbti.vf) = %{tl_version}, tex(ts1cmsrbtr.vf) = %{tl_version}
Provides:       tex(ts1cmsrbts.vf) = %{tl_version}, tex(x2cmsrbrb.vf) = %{tl_version}
Provides:       tex(x2cmsrbrc.vf) = %{tl_version}, tex(x2cmsrbrd.vf) = %{tl_version}
Provides:       tex(x2cmsrbri.vf) = %{tl_version}, tex(x2cmsrbrr.vf) = %{tl_version}
Provides:       tex(x2cmsrbrs.vf) = %{tl_version}, tex(x2cmsrbrx.vf) = %{tl_version}
Provides:       tex(x2cmsrbry.vf) = %{tl_version}, tex(x2cmsrbsb.vf) = %{tl_version}
Provides:       tex(x2cmsrbsr.vf) = %{tl_version}, tex(x2cmsrbss.vf) = %{tl_version}
Provides:       tex(x2cmsrbst.vf) = %{tl_version}, tex(x2cmsrbtc.vf) = %{tl_version}
Provides:       tex(x2cmsrbti.vf) = %{tl_version}, tex(x2cmsrbtr.vf) = %{tl_version}
Provides:       tex(x2cmsrbts.vf) = %{tl_version}, tex(cmsrb.sty) = %{tl_version}
Provides:       tex(ot2cmsrbr.fd) = %{tl_version}, tex(ot2cmsrbs.fd) = %{tl_version}
Provides:       tex(ot2cmsrbt.fd) = %{tl_version}, tex(t1cmsrbr.fd) = %{tl_version}
Provides:       tex(t1cmsrbs.fd) = %{tl_version}, tex(t1cmsrbt.fd) = %{tl_version}
Provides:       tex(t2acmsrbr.fd) = %{tl_version}, tex(t2acmsrbs.fd) = %{tl_version}
Provides:       tex(t2acmsrbt.fd) = %{tl_version}, tex(ts1cmsrbr.fd) = %{tl_version}
Provides:       tex(ts1cmsrbs.fd) = %{tl_version}, tex(ts1cmsrbt.fd) = %{tl_version}
Provides:       tex(x2cmsrbr.fd) = %{tl_version}, tex(x2cmsrbs.fd) = %{tl_version}
Provides:       tex(x2cmsrbt.fd) = %{tl_version}

%description -n texlive-cmsrb
This package provides provides Adobe Type 1 Computer Modern
fonts for the Serbian and Macedonian languages. Although the
cm-super package provides great support for cyrillic script in
various languages, there remains a problem with italic variants
of some letters for Serbian and Macedonian. This package
includes the correct shapes for italic letters \cyrb, \cyrg,
\cyrd, \cyrp, and \cyrt. It also offers some improvements in
letters and accents used in the Serbian language. Supported
encodings are: T1, T2A, TS1, X2 and OT2. The OT2 encoding is
modified so that it is now easy to transcribe Latin text to
Cyrillic.

%package -n texlive-competences
Summary:        Track skills of classroom checks
Version:        svn47573
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(competences.sty) = %{tl_version}

%description -n texlive-competences
This package is an attempt to track skills assessed during a
classroom check. Each question can be associated with one or
more skills and be assigned a number of points to be earned. At
the end of the text, a table set summarizes the skills
assessed, and in what proportions.

%package -n texlive-context-handlecsv
Summary:        Data merging for automatic document creation
Version:        svn47403
License:        GPLv3
Requires:       texlive-base texlive-kpathsea
Provides:       tex(t-handlecsv-extra.lua) = %{tl_version}
Provides:       tex(t-handlecsv-tools.lua) = %{tl_version}
Provides:       tex(t-handlecsv.lua) = %{tl_version}, tex(t-handlecsv.tex) = %{tl_version}

%description -n texlive-context-handlecsv
The package handles csv data merging for automatic document
creation.

%package -n texlive-correctmathalign
Summary:        Correct spacing of the alignment in expressions
Version:        svn44131
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(correctmathalign.sty) = %{tl_version}

%description -n texlive-correctmathalign
This package realigns the horizontal spacing of the alignments
in some mathematical environments.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD

cd %{buildroot}%{_texdir}/texmf-dist/

install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="public/cm-unicode rozynski/comicneue"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-cinzel
%license ofl.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/cinzel/
%{_texdir}/texmf-dist/fonts/map/dvips/cinzel/
%{_texdir}/texmf-dist/fonts/tfm/ndiscovered/cinzel/
%{_texdir}/texmf-dist/fonts/truetype/ndiscovered/cinzel/
%{_texdir}/texmf-dist/fonts/type1/ndiscovered/cinzel/
%{_texdir}/texmf-dist/fonts/vf/ndiscovered/cinzel/
%{_texdir}/texmf-dist/tex/latex/cinzel/

%files -n texlive-cinzel-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/cinzel/

%files -n texlive-circ
%license gpl.txt
%{_texdir}/texmf-dist/fonts/source/public/circ/
%{_texdir}/texmf-dist/fonts/tfm/public/circ/
%{_texdir}/texmf-dist/tex/latex/circ/

%files -n texlive-circ-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/circ/

%files -n texlive-circuitikz
%license lppl1.txt
%{_texdir}/texmf-dist/tex/context/third/circuitikz/
%{_texdir}/texmf-dist/tex/generic/circuitikz/
%{_texdir}/texmf-dist/tex/latex/circuitikz/

%files -n texlive-circuitikz-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/context/third/circuitikz/
%{_texdir}/texmf-dist/doc/generic/circuitikz/
%{_texdir}/texmf-dist/doc/latex/circuitikz/

%files -n texlive-citeall
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/citeall/

%files -n texlive-citeall-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/citeall/

%files -n texlive-cite
%{_texdir}/texmf-dist/tex/latex/cite/

%files -n texlive-cite-doc
%{_texdir}/texmf-dist/doc/latex/cite/

%files -n texlive-cjhebrew
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/cjhebrew/
%{_texdir}/texmf-dist/fonts/enc/dvips/cjhebrew/
%{_texdir}/texmf-dist/fonts/map/dvips/cjhebrew/
%{_texdir}/texmf-dist/fonts/tfm/public/cjhebrew/
%{_texdir}/texmf-dist/fonts/type1/public/cjhebrew/
%{_texdir}/texmf-dist/fonts/vf/public/cjhebrew/
%{_texdir}/texmf-dist/tex/latex/cjhebrew/

%files -n texlive-cjhebrew-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cjhebrew/

%files -n texlive-cjk-ko
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/cjk-ko/

%files -n texlive-cjk-ko-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/cjk-ko/

%files -n texlive-cjkpunct
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/cjkpunct/

%files -n texlive-cjkpunct-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cjkpunct/

%files -n texlive-cjk
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/cjk/

%files -n texlive-cjk-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/cjk/

%files -n texlive-cns
%{_texdir}/texmf-dist/fonts/misc/cns/
%{_texdir}/texmf-dist/fonts/tfm/cns/

%files -n texlive-cns-doc
%{_texdir}/texmf-dist/doc/fonts/cns/

%files -n texlive-classics
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/classics/

%files -n texlive-classics-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/classics/

%files -n texlive-classicthesis
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/classicthesis/

%files -n texlive-classicthesis-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/classicthesis/

%files -n texlive-classpack
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/classpack/

%files -n texlive-classpack-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/support/classpack/

%files -n texlive-cleanthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/cleanthesis/

%files -n texlive-cleanthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/cleanthesis/

%files -n texlive-clearsans
%license apache2.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/clearsans/
%{_texdir}/texmf-dist/fonts/map/dvips/clearsans/
%{_texdir}/texmf-dist/fonts/tfm/intel/clearsans/
%{_texdir}/texmf-dist/fonts/truetype/intel/clearsans/
%{_texdir}/texmf-dist/fonts/type1/intel/clearsans/
%{_texdir}/texmf-dist/fonts/vf/intel/clearsans/
%{_texdir}/texmf-dist/tex/latex/clearsans/

%files -n texlive-clearsans-doc
%license apache2.txt
%{_texdir}/texmf-dist/doc/fonts/clearsans/

%files -n texlive-clefval
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/clefval/

%files -n texlive-clefval-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/clefval/

%files -n texlive-cleveref
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/cleveref/

%files -n texlive-cleveref-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cleveref/

%files -n texlive-clipboard
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/clipboard/

%files -n texlive-clipboard-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/clipboard/

%files -n texlive-clock
%{_texdir}/texmf-dist/fonts/source/public/clock/
%{_texdir}/texmf-dist/fonts/tfm/public/clock/
%{_texdir}/texmf-dist/tex/latex/clock/

%files -n texlive-clock-doc
%{_texdir}/texmf-dist/doc/latex/clock/

%files -n texlive-cloze
%license lppl1.3.txt
%{_texdir}/texmf-dist/scripts/cloze/
%{_texdir}/texmf-dist/tex/lualatex/cloze/

%files -n texlive-cloze-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/lualatex/cloze/

%files -n texlive-clrscode3e
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/clrscode3e/

%files -n texlive-clrscode3e-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/clrscode3e/

%files -n texlive-clrscode
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/clrscode/

%files -n texlive-clrscode-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/clrscode/

%files -n texlive-cmap
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/cmap/

%files -n texlive-cmap-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cmap/

%files -n texlive-cmarrows
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/cmarrows/

%files -n texlive-cmarrows-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/cmarrows/

%files -n texlive-cmbright
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/cmbright/
%{_texdir}/texmf-dist/fonts/tfm/public/cmbright/
%{_texdir}/texmf-dist/tex/latex/cmbright/

%files -n texlive-cmbright-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/cmbright/
%{_texdir}/texmf-dist/doc/latex/cmbright/

%files -n texlive-cmcyr
%license pd.txt
%{_texdir}/texmf-dist/fonts/map/dvips/cmcyr/
%{_texdir}/texmf-dist/fonts/source/public/cmcyr/
%{_texdir}/texmf-dist/fonts/tfm/public/cmcyr/
%{_texdir}/texmf-dist/fonts/type1/public/cmcyr/
%{_texdir}/texmf-dist/fonts/vf/public/cmcyr/

%files -n texlive-cmcyr-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/cmcyr/

%files -n texlive-cmdstring
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/cmdstring/

%files -n texlive-cmdstring-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cmdstring/

%files -n texlive-cmextra
%license knuth.txt
%{_texdir}/texmf-dist/fonts/source/public/cmextra/
%{_texdir}/texmf-dist/fonts/tfm/public/cmextra/

%files -n texlive-cm-lgc
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/cm-lgc/
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-lgc/
%{_texdir}/texmf-dist/fonts/map/dvips/cm-lgc/
%{_texdir}/texmf-dist/fonts/ofm/public/cm-lgc/
%{_texdir}/texmf-dist/fonts/ovf/public/cm-lgc/
%{_texdir}/texmf-dist/fonts/tfm/public/cm-lgc/
%{_texdir}/texmf-dist/fonts/type1/public/cm-lgc/
%{_texdir}/texmf-dist/fonts/vf/public/cm-lgc/
%{_texdir}/texmf-dist/tex/latex/cm-lgc/

%files -n texlive-cm-lgc-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/cm-lgc/

%files -n texlive-cmll
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/cmll/
%{_texdir}/texmf-dist/fonts/source/public/cmll/
%{_texdir}/texmf-dist/fonts/tfm/public/cmll/
%{_texdir}/texmf-dist/fonts/type1/public/cmll/
%{_texdir}/texmf-dist/tex/latex/cmll/

%files -n texlive-cmll-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/cmll/

%files -n texlive-cmpica
%license pd.txt
%{_texdir}/texmf-dist/fonts/source/public/cmpica/
%{_texdir}/texmf-dist/fonts/tfm/public/cmpica/

%files -n texlive-cmpica-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/cmpica/

%files -n texlive-cmpj
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/cmpj/
%{_texdir}/texmf-dist/tex/latex/cmpj/

%files -n texlive-cmpj-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cmpj/

%files -n texlive-cmsd
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/cmsd/

%files -n texlive-cmsd-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cmsd/

%files -n texlive-cm-super
%license gpl.txt
%{_texdir}/texmf-dist/dvips/cm-super/
%{_texdir}/texmf-dist/fonts/afm/public/cm-super/
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-super/
%{_texdir}/texmf-dist/fonts/map/dvips/cm-super/
%{_texdir}/texmf-dist/fonts/map/vtex/cm-super/
%{_texdir}/texmf-dist/fonts/type1/public/cm-super/
%{_texdir}/texmf-dist/tex/latex/cm-super/

%files -n texlive-cm-super-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/cm-super/

%files -n texlive-cmtiup
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/source/public/cmtiup/
%{_texdir}/texmf-dist/fonts/tfm/public/cmtiup/
%{_texdir}/texmf-dist/fonts/vf/public/cmtiup/
%{_texdir}/texmf-dist/tex/latex/cmtiup/

%files -n texlive-cmtiup-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/cmtiup/

%files -n texlive-cm
%license knuth.txt
%{_texdir}/texmf-dist/fonts/map/dvips/cm/
%{_texdir}/texmf-dist/fonts/pk/ljfour/public/cm/
%{_texdir}/texmf-dist/fonts/source/public/cm/
%{_texdir}/texmf-dist/fonts/tfm/public/cm/

%files -n texlive-cm-doc
%license knuth.txt
%{_texdir}/texmf-dist/doc/fonts/cm/

%files -n texlive-cm-unicode
%{_datadir}/fonts/cm-unicode
%{_texdir}/texmf-dist/fonts/afm/public/cm-unicode/
%{_texdir}/texmf-dist/fonts/enc/dvips/cm-unicode/
%{_texdir}/texmf-dist/fonts/map/dvips/cm-unicode/
%{_texdir}/texmf-dist/fonts/opentype/public/cm-unicode/
%{_texdir}/texmf-dist/fonts/type1/public/cm-unicode/

%files -n texlive-cm-unicode-doc
%{_texdir}/texmf-dist/doc/fonts/cm-unicode/

%files -n texlive-cnbwp
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/cnbwp/
%{_texdir}/texmf-dist/makeindex/cnbwp/
%{_texdir}/texmf-dist/tex/latex/cnbwp/

%files -n texlive-cnbwp-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cnbwp/

%files -n texlive-cnltx
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bib/cnltx/
%{_texdir}/texmf-dist/makeindex/cnltx/
%{_texdir}/texmf-dist/tex/latex/cnltx/

%files -n texlive-cnltx-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/cnltx/

%files -n texlive-cntformats
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/cntformats/

%files -n texlive-cntformats-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/cntformats/

%files -n texlive-cntperchap
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/cntperchap/

%files -n texlive-cntperchap-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/cntperchap/

%files -n texlive-codedoc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/codedoc/

%files -n texlive-codedoc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/codedoc/

%files -n texlive-codepage
%{_texdir}/texmf-dist/tex/latex/codepage/

%files -n texlive-codepage-doc
%{_texdir}/texmf-dist/doc/latex/codepage/

%files -n texlive-codesection
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/codesection/

%files -n texlive-codesection-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/codesection/

%files -n texlive-codicefiscaleitaliano
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/codicefiscaleitaliano/

%files -n texlive-codicefiscaleitaliano-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/codicefiscaleitaliano/

%files -n texlive-collcell
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/collcell/

%files -n texlive-collcell-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/collcell/

%files -n texlive-collectbox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/collectbox/

%files -n texlive-collectbox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/collectbox/

%files -n texlive-collection-basic

%files -n texlive-collection-bibtexextra

%files -n texlive-collection-latex

%files -n texlive-colortbl
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/colortbl/

%files -n texlive-colortbl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/colortbl/

%files -n texlive-collref
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/collref/

%files -n texlive-collref-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/collref/

%files -n texlive-compactbib
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/compactbib/

%files -n texlive-collection-binextra

%files -n texlive-collection-context

%files -n texlive-context-account
%license pd.txt
%{_texdir}/texmf-dist/tex/context/interface/third/t-account.xml
%{_texdir}/texmf-dist/tex/context/third/account/

%files -n texlive-context-account-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/context/third/account/

%files -n texlive-context-algorithmic
%license gpl.txt
%{_texdir}/texmf-dist/tex/context/third/algorithmic/

%files -n texlive-context-animation
%license gpl3.txt
%{_texdir}/texmf-dist/tex/context/interface/third/t-animation.xml
%{_texdir}/texmf-dist/tex/context/third/animation/

%files -n texlive-context-animation-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/context/third/animation/

%files -n texlive-context-annotation
%{_texdir}/texmf-dist/tex/context/interface/third/t-annotation.xml
%{_texdir}/texmf-dist/tex/context/third/annotation/

%files -n texlive-context-annotation-doc
%{_texdir}/texmf-dist/doc/context/third/annotation/

%files -n texlive-context-bnf
%license gpl.txt
%{_texdir}/texmf-dist/tex/context/third/bnf/

%files -n texlive-context-bnf-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/context/third/bnf/

%files -n texlive-context-chromato
%license gpl.txt
%{_texdir}/texmf-dist/tex/context/third/chromato/

%files -n texlive-context-chromato-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/context/third/chromato/

%files -n texlive-context-construction-plan
%license gpl.txt
%{_texdir}/texmf-dist/tex/context/third/construction-plan/

%files -n texlive-context-construction-plan-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/context/third/construction-plan/

%files -n texlive-context-cyrillicnumbers
%license bsd.txt
%{_texdir}/texmf-dist/tex/context/interface/third/t-cyrillicnumbers.xml
%{_texdir}/texmf-dist/tex/context/third/cyrillicnumbers/

%files -n texlive-context-cyrillicnumbers-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/context/third/cyrillicnumbers/

%files -n texlive-context-degrade
%license gpl.txt
%{_texdir}/texmf-dist/tex/context/third/degrade/

%files -n texlive-context-degrade-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/context/third/degrade/

%files -n texlive-context-fancybreak
%license gpl.txt
%{_texdir}/texmf-dist/tex/context/interface/third/t-fancybreak.xml
%{_texdir}/texmf-dist/tex/context/third/fancybreak/

%files -n texlive-context-fancybreak-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/context/third/fancybreak/

%files -n texlive-context-filter
%{_texdir}/texmf-dist/tex/context/third/filter/

%files -n texlive-context-filter-doc
%{_texdir}/texmf-dist/doc/context/third/filter/

%files -n texlive-context-french
%license gpl.txt
%{_texdir}/texmf-dist/tex/context/third/french/

%files -n texlive-context-french-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/context/third/french/

%files -n texlive-context-fullpage
%license gpl.txt
%{_texdir}/texmf-dist/tex/context/interface/third/t-fullpage.xml
%{_texdir}/texmf-dist/tex/context/third/fullpage/

%files -n texlive-context-fullpage-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/context/third/fullpage/

%files -n texlive-context-gantt
%license pd.txt
%{_texdir}/texmf-dist/tex/context/third/gantt/

%files -n texlive-context-gantt-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/context/third/gantt/

%files -n texlive-context-gnuplot
%license gpl.txt
%{_texdir}/texmf-dist/metapost/context/third/gnuplot/mp-gnuplot.mp
%{_texdir}/texmf-dist/tex/context/third/gnuplot/

%files -n texlive-context-gnuplot-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/context/third/gnuplot/

%files -n texlive-context-letter
%license gpl.txt
%{_texdir}/texmf-dist/tex/context/interface/third/t-letter.xml
%{_texdir}/texmf-dist/tex/context/interface/third/t-memo.xml
%{_texdir}/texmf-dist/tex/context/third/letter/

%files -n texlive-context-letter-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/context/third/letter/

%files -n texlive-context-lettrine
%license pd.txt
%{_texdir}/texmf-dist/tex/context/interface/third/lettrine.xml
%{_texdir}/texmf-dist/tex/context/third/lettrine/

%files -n texlive-context-lettrine-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/context/third/lettrine/

%files -n texlive-context-mathsets
%{_texdir}/texmf-dist/tex/context/interface/third/t-mathsets.xml
%{_texdir}/texmf-dist/tex/context/third/mathsets/

%files -n texlive-context-mathsets-doc
%{_texdir}/texmf-dist/doc/context/third/mathsets/

%files -n texlive-context-notes-zh-cn
%license gpl.txt

%files -n texlive-context-notes-zh-cn-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/context/third/context-notes-zh-cn/

%files -n texlive-context-rst
%{_texdir}/texmf-dist/tex/context/interface/third/t-rst.xml
%{_texdir}/texmf-dist/scripts/context/lua/third/rst/
%{_texdir}/texmf-dist/tex/context/third/rst/

%files -n texlive-context-rst-doc
%{_texdir}/texmf-dist/doc/context/third/rst/

%files -n texlive-context-ruby
%license pd.txt
%{_texdir}/texmf-dist/tex/context/third/ruby/

%files -n texlive-context-ruby-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/context/third/ruby/

%files -n texlive-context-simplefonts
%license gpl.txt
%{_texdir}/texmf-dist/tex/context/third/simplefonts/

%files -n texlive-context-simplefonts-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/context/third/simplefonts/

%files -n texlive-context-simpleslides
%{_texdir}/texmf-dist/tex/context/interface/third/t-simpleslides.xml
%{_texdir}/texmf-dist/scripts/context/lua/third/simpleslides/
%{_texdir}/texmf-dist/tex/context/third/simpleslides/

%files -n texlive-context-simpleslides-doc
%{_texdir}/texmf-dist/doc/context/third/simpleslides/

%files -n texlive-context-title
%{_texdir}/texmf-dist/tex/context/interface/third/t-title.xml
%{_texdir}/texmf-dist/tex/context/third/title/

%files -n texlive-context-title-doc
%{_texdir}/texmf-dist/doc/context/third/title/

%files -n texlive-context-transliterator
%license bsd.txt
%{_texdir}/texmf-dist/tex/context/interface/third/t-transliterator.xml
%{_texdir}/texmf-dist/tex/context/third/transliterator/

%files -n texlive-context-transliterator-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/context/third/transliterator/

%files -n texlive-context-typearea
%license gpl.txt
%{_texdir}/texmf-dist/tex/context/third/typearea/

%files -n texlive-context-typearea-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/context/third/typearea/

%files -n texlive-context-typescripts
%license gpl2.txt
%{_texdir}/texmf-dist/tex/context/third/typescripts/

%files -n texlive-context-typescripts-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/context/third/typescripts/

%files -n texlive-context-vim
%{_texdir}/texmf-dist/tex/context/third/vim/

%files -n texlive-context-vim-doc
%{_texdir}/texmf-dist/doc/context/third/vim/

%files -n texlive-context-visualcounter
%{_texdir}/texmf-dist/tex/context/third/visualcounter/

%files -n texlive-context-visualcounter-doc
%{_texdir}/texmf-dist/doc/context/third/visualcounter/

%files -n texlive-collection-fontsextra

%files -n texlive-comfortaa
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/afm/public/comfortaa/
%{_texdir}/texmf-dist/fonts/enc/dvips/comfortaa/
%{_texdir}/texmf-dist/fonts/map/dvips/comfortaa/
%{_texdir}/texmf-dist/fonts/tfm/public/comfortaa/
%{_texdir}/texmf-dist/fonts/truetype/public/comfortaa/
%{_texdir}/texmf-dist/fonts/type1/public/comfortaa/
%{_texdir}/texmf-dist/fonts/vf/public/comfortaa/
%{_texdir}/texmf-dist/tex/latex/comfortaa/

%files -n texlive-comfortaa-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/comfortaa/

%files -n texlive-comicneue
%license ofl.txt
%{_datadir}/fonts/comicneue
%{_texdir}/texmf-dist/fonts/enc/dvips/comicneue/
%{_texdir}/texmf-dist/fonts/map/dvips/comicneue/
%{_texdir}/texmf-dist/fonts/opentype/rozynski/comicneue/
%{_texdir}/texmf-dist/fonts/tfm/rozynski/comicneue/
%{_texdir}/texmf-dist/fonts/type1/rozynski/comicneue/
%{_texdir}/texmf-dist/fonts/vf/rozynski/comicneue/
%{_texdir}/texmf-dist/tex/latex/comicneue/

%files -n texlive-comicneue-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/latex/comicneue/

%files -n texlive-concmath-fonts
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/concmath-fonts/
%{_texdir}/texmf-dist/fonts/tfm/public/concmath-fonts/

%files -n texlive-concmath-fonts-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/concmath-fonts/

%files -n texlive-cookingsymbols
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/cookingsymbols/
%{_texdir}/texmf-dist/fonts/tfm/public/cookingsymbols/
%{_texdir}/texmf-dist/tex/latex/cookingsymbols/

%files -n texlive-cookingsymbols-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cookingsymbols/

%files -n texlive-countriesofeurope
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/countriesofeurope/
%{_texdir}/texmf-dist/fonts/afm/public/countriesofeurope/
%{_texdir}/texmf-dist/fonts/enc/dvips/countriesofeurope/
%{_texdir}/texmf-dist/fonts/map/dvips/countriesofeurope/
%{_texdir}/texmf-dist/fonts/tfm/public/countriesofeurope/
%{_texdir}/texmf-dist/fonts/type1/public/countriesofeurope/
%{_texdir}/texmf-dist/tex/latex/countriesofeurope/

%files -n texlive-countriesofeurope-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/countriesofeurope/

%files -n texlive-courier-scaled
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/courier-scaled/

%files -n texlive-courier-scaled-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/fonts/courier-scaled/

%files -n texlive-collection-fontsrecommended

%files -n texlive-courier
%license gpl.txt
%{_texdir}/texmf-dist/dvips/courier/
%{_texdir}/texmf-dist/fonts/afm/adobe/courier/
%{_texdir}/texmf-dist/fonts/afm/urw/courier/
%{_texdir}/texmf-dist/fonts/map/dvips/courier/
%{_texdir}/texmf-dist/fonts/tfm/adobe/courier/
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/courier/
%{_texdir}/texmf-dist/fonts/type1/adobe/courier/
%{_texdir}/texmf-dist/fonts/type1/urw/courier/
%{_texdir}/texmf-dist/fonts/vf/adobe/courier/
%{_texdir}/texmf-dist/fonts/vf/urw35vf/courier/
%{_texdir}/texmf-dist/tex/latex/courier/

%files -n texlive-collection-fontutils

%files -n texlive-collection-formatsextra

%files -n texlive-collection-games

%files -n texlive-colorsep
%license pd.txt
%{_texdir}/texmf-dist/dvips/colorsep/

%files -n texlive-collection-humanities

%files -n texlive-covington
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/covington/

%files -n texlive-covington-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/covington/

%files -n texlive-collection-langarabic

%files -n texlive-collection-langchinese

%files -n texlive-collection-langcjk

%files -n texlive-collection-langcyrillic

%files -n texlive-collection-langczechslovak

%files -n texlive-collection-langenglish

%files -n texlive-components-of-TeX-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/generic/components-of-TeX/

%files -n texlive-comprehensive-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/comprehensive/

%files -n texlive-collection-langeuropean

%files -n texlive-collection-langfrench

%files -n texlive-collection-langgerman

%files -n texlive-collection-langgreek

%files -n texlive-collection-langitalian

%files -n texlive-collection-langjapanese

%files -n texlive-collection-langkorean

%files -n texlive-collection-langother

%files -n texlive-collection-langpolish

%files -n texlive-collection-langportuguese

%files -n texlive-collection-langspanish

%files -n texlive-collection-latexextra

%files -n texlive-collection-latexrecommended

%files -n texlive-collection-pictures

%files -n texlive-combinedgraphics
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/combinedgraphics/

%files -n texlive-combinedgraphics-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/combinedgraphics/

%files -n texlive-colordoc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/colordoc/

%files -n texlive-colordoc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/colordoc/

%files -n texlive-colorinfo
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/colorinfo/

%files -n texlive-colorinfo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/colorinfo/

%files -n texlive-colorspace
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/colorspace/

%files -n texlive-colorspace-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/colorspace/

%files -n texlive-colortab
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/colortab/

%files -n texlive-colortab-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/colortab/

%files -n texlive-colorwav
%license lgpl2.1.txt
%{_texdir}/texmf-dist/tex/latex/colorwav/

%files -n texlive-colorwav-doc
%license lgpl2.1.txt
%{_texdir}/texmf-dist/doc/latex/colorwav/

%files -n texlive-colorweb
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/colorweb/

%files -n texlive-colorweb-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/colorweb/

%files -n texlive-colourchange
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/colourchange/

%files -n texlive-colourchange-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/colourchange/

%files -n texlive-combelow
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/combelow/

%files -n texlive-combelow-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/combelow/

%files -n texlive-combine
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/combine/

%files -n texlive-combine-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/combine/

%files -n texlive-comma
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/comma/

%files -n texlive-comma-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/comma/

%files -n texlive-commado
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/commado/

%files -n texlive-commado-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/commado/

%files -n texlive-comment
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/comment/

%files -n texlive-comment-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/comment/

%files -n texlive-concepts
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/concepts/

%files -n texlive-concepts-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/concepts/

%files -n texlive-concprog
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/concprog/

%files -n texlive-concprog-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/concprog/

%files -n texlive-constants
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/constants/

%files -n texlive-constants-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/constants/

%files -n texlive-contour
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/contour/

%files -n texlive-contour-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/contour/

%files -n texlive-contracard
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/contracard/

%files -n texlive-contracard-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/contracard/

%files -n texlive-cooking
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/cooking/

%files -n texlive-cooking-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/cooking/

%files -n texlive-cool
%license lgpl2.1.txt
%{_texdir}/texmf-dist/tex/latex/cool/

%files -n texlive-cool-doc
%license lgpl2.1.txt
%{_texdir}/texmf-dist/doc/latex/cool/

%files -n texlive-coollist
%license lgpl2.1.txt
%{_texdir}/texmf-dist/tex/latex/coollist/

%files -n texlive-coollist-doc
%license lgpl2.1.txt
%{_texdir}/texmf-dist/doc/latex/coollist/

%files -n texlive-coolstr
%license lgpl2.1.txt
%{_texdir}/texmf-dist/tex/latex/coolstr/

%files -n texlive-coolstr-doc
%license lgpl2.1.txt
%{_texdir}/texmf-dist/doc/latex/coolstr/

%files -n texlive-coolthms
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/coolthms/

%files -n texlive-coolthms-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/coolthms/

%files -n texlive-cooltooltips
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/cooltooltips/

%files -n texlive-cooltooltips-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cooltooltips/

%files -n texlive-coordsys
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/coordsys/

%files -n texlive-coordsys-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/coordsys/

%files -n texlive-copyedit
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/copyedit/

%files -n texlive-copyedit-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/copyedit/

%files -n texlive-copyrightbox
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/copyrightbox/

%files -n texlive-copyrightbox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/copyrightbox/

%files -n texlive-coseoul
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/coseoul/

%files -n texlive-coseoul-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/coseoul/

%files -n texlive-counttexruns
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/counttexruns/

%files -n texlive-counttexruns-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/counttexruns/

%files -n texlive-courseoutline
%{_texdir}/texmf-dist/tex/latex/courseoutline/

%files -n texlive-courseoutline-doc
%{_texdir}/texmf-dist/doc/latex/courseoutline/

%files -n texlive-coursepaper
%{_texdir}/texmf-dist/tex/latex/coursepaper/

%files -n texlive-coursepaper-doc
%{_texdir}/texmf-dist/doc/latex/coursepaper/

%files -n texlive-coverpage
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/coverpage/

%files -n texlive-coverpage-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/coverpage/

%files -n texlive-collection-luatex

%files -n texlive-commath
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/commath/

%files -n texlive-commath-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/commath/

%files -n texlive-concmath
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/concmath/

%files -n texlive-concmath-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/concmath/

%files -n texlive-concrete
%license knuth.txt
%{_texdir}/texmf-dist/fonts/source/public/concrete/
%{_texdir}/texmf-dist/fonts/tfm/public/concrete/

%files -n texlive-concrete-doc
%license knuth.txt
%{_texdir}/texmf-dist/doc/fonts/concrete/

%files -n texlive-conteq
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/conteq/

%files -n texlive-conteq-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/conteq/

%files -n texlive-collection-metapost

%files -n texlive-collection-music

%files -n texlive-collection-pstricks

%files -n texlive-collection-publishers

%files -n texlive-confproc
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/confproc/
%{_texdir}/texmf-dist/makeindex/confproc/
%{_texdir}/texmf-dist/tex/latex/confproc/

%files -n texlive-confproc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/confproc/

%files -n texlive-complexity
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/complexity/

%files -n texlive-complexity-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/complexity/

%files -n texlive-computational-complexity
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/computational-complexity/
%{_texdir}/texmf-dist/tex/latex/computational-complexity/

%files -n texlive-computational-complexity-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/computational-complexity/

%files -n texlive-collection-xetex

%files -n texlive-cmdtrack-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cmdtrack/

%files -n texlive-cmdtrack
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/cmdtrack/

%files -n texlive-cmexb-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/cmexb/

%files -n texlive-cmexb
%license pd.txt
%{_texdir}/texmf-dist/fonts/map/dvips/cmexb/
%{_texdir}/texmf-dist/fonts/tfm/public/cmexb/
%{_texdir}/texmf-dist/fonts/type1/public/cmexb/

%files -n texlive-cochineal-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/cochineal/

%files -n texlive-cochineal
%license ofl.txt
%{_texdir}/texmf-dist/tex/latex/cochineal/
%{_texdir}/texmf-dist/fonts/opentype/public/cochineal/
%{_texdir}/texmf-dist/fonts/map/dvips/cochineal/
%{_texdir}/texmf-dist/fonts/tfm/public/cochineal/
%{_texdir}/texmf-dist/fonts/vf/public/cochineal/
%{_texdir}/texmf-dist/fonts/enc/dvips/cochineal/
%{_texdir}/texmf-dist/fonts/afm/public/cochineal/
%{_texdir}/texmf-dist/fonts/type1/public/cochineal/

%files -n texlive-coloring-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/coloring/

%files -n texlive-coloring
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/coloring/

%files -n texlive-continue-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/continue/

%files -n texlive-continue
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/continue/

%files -n texlive-collection-plaingeneric

%files -n texlive-collection-mathscience

%files -n texlive-cje
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/cje/
%{_texdir}/texmf-dist/bibtex/bst/cje/
%{_texdir}/texmf-dist/tex/latex/cje/

%files -n texlive-collection-texworks

%files -n texlive-combofont
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/lualatex/combofont/
%{_texdir}/texmf-dist/tex/lualatex/combofont/

%files -n texlive-context-cmscbf
%license gpl.txt
%doc %{_texdir}/texmf-dist/doc/context/third/cmscbf/
%{_texdir}/texmf-dist/tex/context/third/cmscbf/

%files -n texlive-context-cmttbf
%license gpl.txt
%doc %{_texdir}/texmf-dist/doc/context/third/cmttbf/
%{_texdir}/texmf-dist/tex/context/third/cmttbf/

%files -n texlive-context-inifile
%license gpl.txt
%doc %{_texdir}/texmf-dist/doc/context/third/inifile/
%{_texdir}/texmf-dist/tex/context/third/inifile/

%files -n texlive-context-layout
%doc %{_texdir}/texmf-dist/doc/context/third/layout/
%{_texdir}/texmf-dist/tex/context/third/layout/

%files -n texlive-conv-xkv
%license lppl1.2.txt
%doc %{_texdir}/texmf-dist/doc/latex/conv-xkv/
%{_texdir}/texmf-dist/tex/latex/conv-xkv/

%files -n texlive-cooking-units
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/latex/cooking-units/
%{_texdir}/texmf-dist/tex/latex/cooking-units/

%files -n texlive-cormorantgaramond
%license ofl.txt
%doc %{_texdir}/texmf-dist/doc/fonts/cormorantgaramond/
%{_texdir}/texmf-dist/fonts/enc/dvips/cormorantgaramond/
%{_texdir}/texmf-dist/fonts/map/dvips/cormorantgaramond/
%{_texdir}/texmf-dist/fonts/opentype/catharsis/cormorantgaramond/
%{_texdir}/texmf-dist/fonts/tfm/catharsis/cormorantgaramond/
%{_texdir}/texmf-dist/fonts/type1/catharsis/cormorantgaramond/
%{_texdir}/texmf-dist/fonts/vf/catharsis/cormorantgaramond/
%{_texdir}/texmf-dist/tex/latex/cormorantgaramond/

%files -n texlive-citeref
%license bsd.txt
%{_texdir}/texmf-dist/tex/latex/citeref/
%doc %{_texdir}/texmf-dist/doc/latex/citeref/

%files -n texlive-clrdblpg
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/clrdblpg/
%doc %{_texdir}/texmf-dist/doc/latex/clrdblpg/

%files -n texlive-clrstrip
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/clrstrip/
%doc %{_texdir}/texmf-dist/doc/latex/clrstrip/

%files -n texlive-cm-mf-extra-bold
%license gpl.txt
%{_texdir}/texmf-dist/fonts/source/public/cm-mf-extra-bold/
%{_texdir}/texmf-dist/fonts/tfm/public/cm-mf-extra-bold/

%files -n texlive-cmsrb
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/public/cmsrb/
%{_texdir}/texmf-dist/fonts/enc/dvips/cmsrb/
%{_texdir}/texmf-dist/fonts/map/dvips/cmsrb/
%{_texdir}/texmf-dist/fonts/tfm/public/cmsrb/
%{_texdir}/texmf-dist/fonts/type1/public/cmsrb/
%{_texdir}/texmf-dist/fonts/vf/public/cmsrb/
%{_texdir}/texmf-dist/tex/latex/cmsrb/
%doc %{_texdir}/texmf-dist/doc/fonts/cmsrb/

%files -n texlive-competences
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/competences/
%doc %{_texdir}/texmf-dist/doc/latex/competences/

%files -n texlive-context-handlecsv
%license gpl3.txt
%{_texdir}/texmf-dist/tex/context/third/handlecsv/
%doc %{_texdir}/texmf-dist/doc/context/third/handlecsv/

%files -n texlive-correctmathalign
%license bsd.txt
%{_texdir}/texmf-dist/tex/latex/correctmathalign/
%doc %{_texdir}/texmf-dist/doc/latex/correctmathalign/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
