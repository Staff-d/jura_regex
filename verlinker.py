import re

# Kann in ein Python Skript kopiert werden


#Dictionary. keys=Gesetzesabkürzung in lowercase. Value = Liste mit Eintrag[0]="Korrekte" Darstellung und Eintrag[1]=Abkürzung für die
# gesetze-im-internet.de URL
gesetze = {"aatv" : ["AATV" , "aatv"],
"aaüg" : ["AAÜG" , "aa_g"],
"abmg" : ["ABMG" , "abmg"],
"adr" : ["ADR" , "adr"],
"aentg" : ["AEntG" , "aentg"],
"afbg" : ["AFBG" , "afbg"],
"afkg" : ["AFKG" , "afkg"],
"afwog" : ["AFWoG" , "afwog"],
"afuv" : ["AFuV" , "afuv_2005"],
"agbg" : ["AGBG" , "agbg"],
"akostg" : ["AKostG" , "akostg"],
"akostv" : ["AKostV" , "akostv_2002"],
"amg" : ["AMG" , "amg_1976"],
"arv" : ["ARV" , "arv_1991"],
"asig" : ["ASiG" , "asig"],
"astg" : ["AStG" , "astg"],
"atzv" : ["ATZV" , "atzv"],
"avbeltv" : ["AVBEltV" , "avbeltv"],
"avbgasv" : ["AVBGasV" , "avbgasv"],
"avv" : ["AVV" , "avv"],
"awg" : ["AWG" , "awg"],
"awaffv" : ["AWaffV" , "awaffv"],
"azrg" : ["AZRG" , "azrg"],
"abfablv" : ["AbfAblV" , "abfablv"],
"abfbeauftrv" : ["AbfBeauftrV" , "abfbeauftrv"],
"abfkobiv" : ["AbfKoBiV" , "abfkobiv"],
"abfverbrg" : ["AbfVerbrG" , "abfverbrg"],
"abgg" : ["AbgG" , "abgg"],
"absfondsg" : ["AbsFondsG" , "absfondsg"],
"agrstruktg" : ["AgrStruktG" , "agrstruktg"],
"aktg" : ["AktG" , "aktg"],
"alhiv" : ["AlhiV" , "alhiv_2002"],
"alkov" : ["AlkoV" , "alkov"],
"altschg" : ["AltSchG" , "altschg"],
"altfahrzeugv" : ["AltfahrzeugV" , "altautov"],
"altholzv" : ["AltholzV" , "altholzv"],
"apog" : ["ApoG" , "apog"],
"argv" : ["ArGV" , "argv"],
"arbgbeschlg" : ["ArbGBeschlG" , "arbgbeschlg"],
"arbplschg" : ["ArbPlSchG" , "arbplschg"],
"arbplschgabschn3v" : ["ArbPlSchGAbschn3V" , "arbplschgabschn3v"],
"arbschg" : ["ArbSchG" , "arbschg"],
"arbstättv" : ["ArbStättV" , "arbst_ttv_2004"],
"arbzabsichg" : ["ArbZAbsichG" , "arbzabsichg"],
"arbzg" : ["ArbZG" , "arbzg"],
"arbzv" : ["ArbZV" , "arbzv"],
"arbnerfg" : ["ArbnErfG" , "arbnerfg"],
"asylblg" : ["AsylbLG" , "asylblg"],
"asylg" : ["AsylG", "asylvfg_1992"],
"atg" : ["AtG" , "atg"],
"aufenthg" : ["AufenthG" , "aufenthg_2004"],
"aufenthv" : ["AufenthV" , "aufenthv"],
"ausübsiedwog" : ["AusÜbsiedWOG" , "aus_bsiedwog"],
"aüg" : ["AÜG" , "a_g"],
"bafög" : ["BAföG" , "baf_g"],
"barchbv" : ["BArchBV" , "barchbv"],
"barchg" : ["BArchG" , "barchg"],
"bbg" : ["BBG" , "bbg"],
"bbkg" : ["BBKG" , "bbkg"],
"bbaug" : ["BBauG" , "bbaug"],
"bbergg" : ["BBergG" , "bbergg"],
"bbesg" : ["BBesG" , "bbesg"],
"bbig" : ["BBiG" , "bbig_2005"],
"bdg" : ["BDG" , "bdg"],
"bdsg" : ["BDSG" , "bdsg_1990"],
"beg" : ["BEG" , "beg"],
"berzgg" : ["BErzGG" , "berzgg"],
"bgb" : ["BGB" , "bgb"],
"bgg" : ["BGG" , "bgg"],
"bgleig" : ["BGleiG" , "bgleig"],
"bgrembg" : ["BGremBG" , "bgrembg"],
"bho" : ["BHO" , "bho"],
"bitv" : ["BITV" , "bitv"],
"bimschg" : ["BImSchG" , "bimschg"],
"bjagdg" : ["BJagdG" , "bjagdg"],
"bkleingg" : ["BKleingG" , "bkleingg"],
"bkombesv" : ["BKomBesV" , "bkombesv"],
"blg" : ["BLG" , "blg"],
"blgabv" : ["BLGABV" , "blgabv"],
"bming" : ["BMinG" , "bming"],
"bnv" : ["BNV" , "bnv"],
"bnatschg" : ["BNatSchG" , "bnatschg_2002"],
"bnoto" : ["BNotO" , "bnoto"],
"bpersvg" : ["BPersVG" , "bpersvg"],
"bpolbg" : ["BPolBG" , "bpolbg"],
"bpolzv" : ["BPolZV" , "bpolzv"],
"bpolzollv" : ["BPolZollV" , "bpolzollv"],
"bpräswahlg" : ["BPräsWahlG" , "bpr_swahlg"],
"brao" : ["BRAO" , "brao"],
"brkg" : ["BRKG" , "brkg_2005"],
"brrg" : ["BRRG" , "brrg"],
"bseuntersv" : ["BSEUntersV" , "bseuntersv"],
"bsevorsorgv" : ["BSEVorsorgV" , "bsevorsorgv"],
"bsig" : ["BSIG" , "bsig"],
"bswag" : ["BSWAG" , "bswag"],
"bschg" : ["BSchG" , "bschg"],
"bseeschg" : ["BSeeSchG" , "bseeschg"],
"btoeltv" : ["BTOEltV" , "btoeltv"],
"bukg" : ["BUKG" , "bukg"],
"burlg" : ["BUrlG" , "burlg"],
"burlv" : ["BUrlV" , "burlv"],
"bvfg" : ["BVFG" , "bvfg"],
"bverfgg" : ["BVerfGG" , "bverfgg"],
"bverfschg" : ["BVerfSchG" , "bverfschg"],
"bvwag" : ["BVwAG" , "bvwag"],
"bwahlg" : ["BWahlG" , "bwahlg"],
"bwahlgv" : ["BWahlGV" , "bwahlgv"],
"bwaldg" : ["BWaldG" , "bwaldg"],
"bwildschv" : ["BWildSchV" , "bwildschv"],
"bzrg" : ["BZRG" , "bzrg"],
"baugb" : ["BauGB" , "bbaug"],
"baunvo" : ["BauNVO" , "baunvo"],
"baupg" : ["BauPG" , "baupg"],
"baustellv" : ["BaustellV" , "baustellv"],
"beamtvg" : ["BeamtVG" , "beamtvg"],
"beamtvüv" : ["BeamtVÜV" , "beamtv_v"],
"bedggstv" : ["BedGgstV" , "bedggstv"],
"befbezg" : ["BefBezG" , "befbezg"],
"beitragsüv" : ["BeitragsÜV" , "beitr_v"],
"berrehag" : ["BerRehaG" , "berrehag"],
"berathig" : ["BeratHiG" , "berathig"],
"beschg" : ["BeschG" , "beschg"],
"betravg" : ["BetrAVG" , "betravg"],
"betrkv" : ["BetrKV" , "betrkv"],
"betrsichv" : ["BetrSichV" , "betrsichv"],
"betrvg" : ["BetrVG" , "betrvg"],
"betrvgdv1wo" : ["BetrVGDV1WO" , "betrvgdv1wo"],
"beurkg" : ["BeurkG" , "beurkg"],
"bevstatg" : ["BevStatG" , "bevstatg"],
"bewg" : ["BewG" , "bewg"],
"bgsg" : ["BGSG" , "bgsg"],
"bierstg" : ["BierStG" , "bierstg_1993"],
"bierstv" : ["BierStV" , "bierstv"],
"bildscharbv" : ["BildscharbV" , "bildscharbv"],
"binschg" : ["BinSchG" , "binschg"],
"binschprg" : ["BinSchPRG" , "binschprg"],
"biostoffv" : ["BioStoffV" , "biostoffv"],
"biomassev" : ["BiomasseV" , "biomassev"],
"blv" : ["BLV" , "blv_2009"],
"bkag" : ["BKAG" , "bkag_1997"],
"bkgg" : ["BKGG" , "bkgg_1996"],
"bpolg" : ["BPolg" , "bgsg_1994"],
"brmv" : ["BrMV" , "brmv"],
"brstv" : ["BrStV" , "brstv"],
"branntwmong" : ["BranntwMonG" , "branntwmong"],
"branntwmonvwg" : ["BranntwMonVwG" , "branntwmonvwg"],
"brenno" : ["BrennO" , "brenno_1998"],
"btg" : ["BtG" , "btg"],
"btmg" : ["BtMG" , "btmg_1981"],
"buchprg" : ["BuchPrG" , "buchprg"],
"börsg" : ["BörsG" , "b_rsg_2002"],
"börszulv" : ["BörsZulV" , "b_rszulv"],
"bwo" : ["BWO" , "bwo_1985"],
"chemg" : ["ChemG" , "chemg"],
"dbgrg" : ["DBGrG" , "dbgrg"],
"dbeglg" : ["DBeglG" , "dbeglg"],
"dbiblg" : ["DBiblG" , "dbiblg"],
"defg" : ["DEFG" , "defg"],
"designg" : ["DesignG" , "geschmmg_2004"],
"deüv" : ["DEÜV" , "de_v"],
"dohg" : ["DOHG" , "dohg"],
"drig" : ["DRiG" , "drig"],
"depv" : ["DepV" , "depv"],
"depotg" : ["DepotG" , "wpapg"],
"diätv" : ["DiätV" , "di_tv"],
"drittelbg" : ["DrittelbG" , "drittelbg"],
"drucklv" : ["DruckLV" , "drucklv"],
"dublübk" : ["DublÜbk" , "dubl_bk"],
"ebo" : ["EBO" , "ebo"],
"ebrg" : ["EBRG" , "ebrg"],
"eeg" : ["EEG" , "eeg_2004"],
"egbgb" : ["EGBGB" , "bgbeg"],
"eggentdurchfg" : ["EGGenTDurchfG" , "eggentdurchfg"],
"ekrg" : ["EKrG" , "ebkrg"],
"emvbeitrv" : ["EMVBeitrV" , "emvbeitrv"],
"emvg" : ["EMVG" , "emvg_1998"],
"erbstg" : ["ErbStG" , "erbstg_1974"],
"eschg" : ["ESchG" , "eschg"],
"estdv" : ["EStDV" , "estdv_1955"],
"estg" : ["EStG" , "estg"],
"eubestg" : ["EUBestG" , "eubestg"],
"eurlv" : ["EUrlV" , "burlv"],
"efbv" : ["EfbV" , "efbv"],
"ehfg" : ["EhfG" , "ehfg"],
"eichg" : ["EichG" , "eichg"],
"eigzulg" : ["EigZulG" , "eigzulg"],
"eneg" : ["EnEG" , "eneg"],
"enev" : ["EnEV" , "enev"],
"envhv" : ["EnVHV" , "envhv_2002"],
"envkv" : ["EnVKV" , "envkv"],
"enwg" : ["EnWG" , "enwg_2005"],
"entgfg" : ["EntgFG" , "entgfg"],
"erbbauv" : ["ErbbauV" , "erbbauv"],
"ersdig" : ["ErsDiG" , "ersdig"],
"erzurlv" : ["ErzUrlV" , "erzurlv"],
"eurag" : ["EuRAG" , "eurag"],
"euwg" : ["EuWG" , "euwg"],
"eüg" : ["EÜG" , "e_g"],
"eügv" : ["EÜGV" , "e_gv"],
"famfg" : ["FamFG" , "famfg"],
"fbeitrv" : ["FBeitrV" , "fbeitrv_2000"],
"fgg" : ["FGG" , "fgg"],
"fgo" : ["FGO" , "fgo"],
"fgebv" : ["FGebV" , "fgebv"],
"fhbleistbv" : ["FHBLeistBV" , "fhbleistbv"],
"frg" : ["FRG" , "frg"],
"fsjg" : ["FSJG" , "f_jfg"],
"fstrprivfing" : ["FStrPrivFinG" , "fstrprivfing"],
"fteg" : ["FTEG" , "fteg"],
"fernusg" : ["FernUSG" , "fernusg"],
"feuerschstg" : ["FeuerschStG" , "feuerschstg_1979"],
"fischetikettg" : ["FischEtikettG" , "fischetikettg"],
"fischhv" : ["FischHV" , "fischhv"],
"flaggrg" : ["FlaggRG" , "flaggrg"],
"flurbg" : ["FlurbG" , "flurbg"],
"frsaftv" : ["FrSaftV" , "frsaftv_2004"],
"freqbzpv" : ["FreqBZPV" , "freqbzpv_2004"],
"freqnpav" : ["FreqNPAV" , "freqnpav"],
"freqzutv" : ["FreqZutV" , "freqzutv"],
"frhentzg" : ["FrhEntzG" , "frhentzg"],
"fögbg" : ["FöGbG" , "f_gbg"],
"gad" : ["GAD" , "gad"],
"gg" : ["GG" , "gg"],
"ggav" : ["GGAV" , "ggav_2002"],
"ggkontrollv" : ["GGKontrollV" , "ggkontrollv"],
"ggkostv" : ["GGKostV" , "ggkostv"],
"ggvbinsch" : ["GGVBinSch" , "ggvbinsch"],
"ggvse" : ["GGVSE" , "ggvse"],
"gkg" : ["GKG" , "gkg_2004"],
"gpsg" : ["GPSG" , "gpsg"],
"gvfg" : ["GVFG" , "gvfg"],
"gvg" : ["GVG" , "gvg"],
"gwb" : ["GWB" , "gwb"],
"gastg" : ["GastG" , "gastg"],
"gbv" : ["GbV" , "gbv"],
"gebrmg" : ["GebrMG" , "gebrmg"],
"gefstoffv" : ["GefStoffV" , "gefstoffv_2005"],
"geflpestv" : ["GeflPestV" , "geflpestv"],
"geng" : ["GenG" , "geng"],
"genregv" : ["GenRegV" , "genregv"],
"gewabfv" : ["GewAbfV" , "gewabfv"],
"gewo" : ["GewO" , "gewo"],
"gewschg" : ["GewSchG" , "gewschg"],
"gewstg" : ["GewStG" , "gewstg"],
"gleibwv" : ["GleibWV" , "gleibwv"],
"gmbhg" : ["GmbHG" , "gmbhg"],
"gwg" : ["GwG" , "gwg"],
"hag" : ["HAG" , "hag"],
"hgb" : ["HGB" , "hgb"],
"hgrg" : ["HGRG" , "hgrg"],
"hhg" : ["HHG" , "hhg"],
"hkstg" : ["HKStG" , "hkstg"],
"hoai" : ["HOAI" , "aihono"],
"hrg" : ["HRG" , "hrg"],
"hrv" : ["HRV" , "hdlregvfg"],
"hschulbg" : ["HSchulBG" , "hschulbg"],
"hwg" : ["HWG" , "heilmwerbg"],
"haftpflg" : ["HaftPflG" , "haftpflg"],
"hausratsv" : ["HausratsV" , "hausratsv"],
"heimg" : ["HeimG" , "heimg"],
"heimmindbauv" : ["HeimMindBauV" , "heimmindbauv"],
"heimmitwirkungsv" : ["HeimMitwirkungsV" , "heimmitwirkungsv"],
"heimpersv" : ["HeimPersV" , "heimpersv"],
"heimsicherungsv" : ["HeimsicherungsV" , "heimsicherungsv"],
"heizkostenv" : ["HeizkostenV" , "heizkostenv"],
"honigv" : ["HonigV" , "honigv_2004"],
"hundverbreinfg" : ["HundVerbrEinfG" , "hundverbreinfg"],
"hundverbreinfvo" : ["HundVerbrEinfVO" , "hundverbreinfvo"],
"hwo" : ["HwO" , "hwo"],
"irg" : ["IRG" , "irg"],
"ifsg" : ["IfSG" , "ifsg"],
"inso" : ["InsO" , "inso"],
"intbestg" : ["IntBestG" , "intbestg"],
"intv" : ["IntV" , "intv"],
"jarbschg" : ["JArbSchG" , "jarbschg"],
"jgg" : ["JGG" , "jgg"],
"jveg" : ["JVEG" , "jveg"],
"jagdzeitv" : ["JagdzeitV" , "jagdzeitv_1977"],
"juschg" : ["JuSchG" , "juschg"],
"kav" : ["KAV" , "kav"],
"kdvg" : ["KDVG" , "kdvg_2003"],
"khv" : ["KHV" , "khv"],
"ksvg" : ["KSVG" , "ksvg"],
"kschg" : ["KSchG" , "kschg"],
"kwg" : ["KWG" , "kredwg"],
"kaffeestg" : ["KaffeeStG" , "kaffeestg_1993"],
"kaffeestv" : ["KaffeeStV" , "kaffeestv"],
"kaffeev" : ["KaffeeV" , "kaffeev_2001"],
"kakaov" : ["KakaoV" , "kakaov_2003"],
"kindarbschv" : ["KindArbSchV" , "kindarbschv"],
"konfv" : ["KonfV" , "konfv_2003"],
"konsg" : ["KonsG" , "konsg"],
"kosmetikv" : ["KosmetikV" , "kosmetikv"],
"kosto" : ["KostO" , "kosto"],
"krwaffkontrg" : ["KrWaffKontrG" , "krwaffkontrg"],
"kraftstg" : ["KraftStG" , "kraftstg"],
"kultgschg" : ["KultgSchG" , "kultgschg"],
"kunsturhg" : ["KunstUrhG" , "kunsturhg"],
"käsev" : ["KäseV" , "k_sev"],
"lag" : ["LAG" , "lag"],
"lanpg" : ["LAnpG" , "lanpg"],
"lfgb" : ["LFGB" , "lfgb"],
"lhmv" : ["LHmV" , "lhmv"],
"lmhv" : ["LMHV" , "lmhv"],
"lmkv" : ["LMKV" , "lmkv"],
"lpzv" : ["LPZV" , "lpzv"],
"lpartg" : ["LPartG" , "lpartg"],
"lstuv" : ["LStuV" , "lstuv"],
"ladschlg" : ["LadSchlG" , "ladschlg"],
"lasthandhabv" : ["LasthandhabV" , "lasthandhabv"],
"luftsig" : ["LuftSiG" , "luftsig"],
"luftvg" : ["LuftVG" , "luftvg"],
"lwg" : ["LwG" , "lwg"],
"madg" : ["MADG" , "madg"],
"mbplg" : ["MBPlG" , "mbplg"],
"mpg" : ["MPG" , "mpg"],
"mrrg" : ["MRRG" , "mrrg"],
"markeng" : ["MarkenG" , "markeng"],
"mauthv" : ["MautHV" , "mauthv"],
"mbbo" : ["MbBO" , "mbbo"],
"mindschrübkg" : ["MindSchRÜbkG" , "mindschr_bkg"],
"minöstv" : ["MinöStV" , "min_stv"],
"montanmitbestg" : ["MontanMitbestG" , "montanmitbestg"],
"montanmitbestgergg" : ["MontanMitbestGErgG" , "montanmitbestgergg"],
"muschbv" : ["MuSchBV" , "muschbv"],
"muschg" : ["MuSchG" , "muschg"],
"ndkontrg" : ["NDKontrG" , "ndkontrg"],
"nkv" : ["NKV" , "nkv"],
"nlv" : ["NLV" , "nlv"],
"nzv" : ["NZV" , "nzv"],
"nachwg" : ["NachwG" , "nachwg"],
"namändg" : ["NamÄndG" , "nam_ndg"],
"nemv" : ["NemV" , "nemv"],
"nichtanpg" : ["NichtAnpG" , "nichtanpg"],
"owig" : ["OWiG" , "owig_1968"],
"pangv" : ["PAngV" , "pangv"],
"pbefg" : ["PBefG" , "pbefg"],
"pcbabfallv" : ["PCBAbfallV" , "pcbabfallv"],
"pdsv" : ["PDSV" , "pdsv"],
"pentgv" : ["PEntgV" , "pentgv"],
"pudlv" : ["PUDLV" , "pudlv"],
"partg" : ["PartG" , "partg"],
"partgg" : ["PartGG" , "partgg"],
"passv" : ["PassV" , "passv_2004"],
"patanwo" : ["PatAnwO" , "patanwo"],
"patg" : ["PatG" , "patg"],
"persauswg" : ["PersAuswG" , "persauswg"],
"persstdg" : ["PersStdG" , "persstdg"],
"persstdgav" : ["PersStdGAV" , "persstdgav"],
"pflstv" : ["PflStV" , "pflstv"],
"pflvg" : ["PflVG" , "pflvg"],
"prodhaftg" : ["ProdHaftG" , "prodhaftg"],
"rog" : ["ROG" , "rog"],
"rvg" : ["RVG" , "rvg"],
"regg" : ["RegG" , "regg"],
"rennwlottg" : ["RennwLottG" , "rennwlottg"],
"rennwlottgab" : ["RennwLottGAB" , "rennwlottgabest"],
"rohrfltgv" : ["RohrFLtgV" , "rohrfltgv"],
"rpflg" : ["RPflG" , "rpflg_1969"],
"rustag" : ["RuStAG" , "rustag"],
"sbg" : ["SBG" , "sbg"],
"seddiktstiftg" : ["SEDDiktStiftG" , "seddiktstiftg"],
"sg" : ["SG" , "sg"],
"sgb i" : ["SGB I" , "sgb_1"],
"sgb ii" : ["SGB II" , "sgb_2"],
"sgb iii" : ["SGB III" , "sgb_3"],
"sgb iv" : ["SGB IV" , "sgb_4"],
"sgb v" : ["SGB V" , "sgb_5"],
"sgb vi" : ["SGB VI" , "sgb_6"],
"sgb vii" : ["SGB VII" , "sgb_7"],
"sgb viii" : ["SGB VIII" , "sgb_8"],
"sgb ix" : ["SGB IX" , "sgb_9"],
"sgb x" : ["SGB X" , "sgb_10"],
"sgb xi" : ["SGB XI" , "sgb_11"],
"sgb xii" : ["SGB XII" , "sgb_12"],
"sgbwehrpflv" : ["SGBWehrpflV" , "sgbwehrpflv"],
"shmv" : ["SHmV" , "shmv_2003"],
"solzg" : ["SolzG" , "solzg_1995"],
"surlv" : ["SUrlV" , "surlv"],
"svg" : ["SVG" , "svg"],
"svüv" : ["SVÜV" , "sv_v"],
"sanoaausbgv" : ["SanOAAusbgV" , "sanoaausbgv"],
"schberg" : ["SchBerG" , "schberg"],
"schsg" : ["SchSG" , "schsg"],
"schaumwzwstg" : ["SchaumwZwStG" , "schaumwzwstg"],
"schaumwzwstv" : ["SchaumwZwStV" , "schaumwzwstv"],
"scheckg" : ["ScheckG" , "scheckg"],
"schuldranpg" : ["SchuldRAnpG" , "schuldranpg"],
"schwarzarbg" : ["SchwarzArbG" , "schwarzarbg_2004"],
"schwbawv" : ["SchwbAwV" , "schwbawv"],
"schwbbag" : ["SchwbBAG" , "schwbbag"],
"schwbnv" : ["SchwbNV" , "schwbnv"],
"schwbwo" : ["SchwbWO" , "schwbwo"],
"schwbwv" : ["SchwbWV" , "schwbwv"],
"seefischg" : ["SeeFischG" , "seefischg"],
"seelotg" : ["SeelotG" , "seelotg"],
"sigg" : ["SigG" , "sigg_2001"],
"sigv" : ["SigV" , "sigv_2001"],
"sozuwg" : ["SoZuwG" , "sozuwg"],
"solidarfabfv" : ["SolidarfAbfV" , "solidarfabfv"],
"sozdig" : ["SozDiG" , "sozdig"],
"sozhidav" : ["SozhiDAV" , "sozhidav"],
"spielzsiv" : ["SpielzSiV" , "spielzsiv"],
"spraug" : ["SprAuG" , "spraug"],
"spraugwo" : ["SprAuGWO" , "wospraug"],
"sprengg" : ["SprengG" , "sprengg_1976"],
"stag" : ["StAG" , "rustag"],
"stangregg" : ["StAngRegG" , "stangregg"],
"stgb" : ["StGB" , "stgb"],
"stpo" : ["StPO" , "stpo"],
"stug" : ["StUG" , "stug"],
"stukostv" : ["StUKostV" , "stukostv"],
"stvg" : ["StVG" , "stvg"],
"stvo" : ["StVO" , "stvo_2013"],
"stvzo" : ["StVZO" , "stvzo"],
"stvollzg" : ["StVollzG" , "stvollzg"],
"stzg" : ["StZG" , "stzg"],
"staatenlmindübkag" : ["StaatenlMindÜbkAG" , "staatenlmind_bkag"],
"streg" : ["StrEG" , "streg"],
"strrehag" : ["StrRehaG" , "strrehag"],
"strlschv" : ["StrlSchV" , "strlschv_2001"],
"stromstg" : ["StromStG" , "stromstg"],
"stromstv" : ["StromStV" , "stromstv"],
"süfv" : ["SÜFV" , "s_fv"],
"süg" : ["SÜG" , "s_g"],
"tddsg" : ["TDDSG" , "tddsg"],
"tdg" : ["TDG" , "tdg"],
"tentgv" : ["TEntgV" , "tentgv"],
"tfg" : ["TFG" , "tfg"],
"tfgmv" : ["TFGMV" , "tfgmv"],
"tkg" : ["TKG" , "tkg_2004"],
"tlmv" : ["TLMV" , "tlmv"],
"tngebv" : ["TNGebV" , "tngebv"],
"tpg" : ["TPG" , "tpg"],
"tsg" : ["TSG" , "tsg"],
"tudlv" : ["TUDLV" , "tudlv"],
"tvg" : ["TVG" , "tvg"],
"tabstg" : ["TabStG" , "tabstg_1993"],
"tabstv" : ["TabStV" , "tabstv"],
"textilkennzg" : ["TextilKennzG" , "textilkennzg"],
"tgv" : ["TgV" , "transgv"],
"tiersg" : ["TierSG" , "viehseuchg"],
"tierschg" : ["TierSchG" , "tierschg"],
"tierschhuv" : ["TierSchHuV" , "tierschhuv"],
"tierschnutztv" : ["TierSchNutztV" , "tierschnutztv"],
"tierschtrv" : ["TierSchTrV" , "tierschtrv"],
"trinkwv" : ["TrinkWV" , "trinkwv_2001"],
"tähav" : ["TÄHAV" , "t_hav"],
"uag" : ["UAG" , "uag"],
"uagzvv" : ["UAGZVV" , "uagzvv"],
"uig" : ["UIG" , "uig_2005"],
"uklag" : ["UKlaG" , "uklag"],
"usg" : ["USG" , "usg"],
"ustg" : ["UStG" , "ustg_1980"],
"uvpg" : ["UVPG" , "uvpg"],
"uwg" : ["UWG" , "uwg_2004"],
"uzwbwg" : ["UZwBwG" , "uzwbwg"],
"uzwg" : ["UZwG" , "uzwg"],
"uhvorschg" : ["UhVorschG" , "uhvorschg"],
"ukv" : ["UkV" , "ukv_2005"],
"umwelthg" : ["UmweltHG" , "umwelthg"],
"urhg" : ["UrhG" , "urhg"],
"urhwahrng" : ["UrhWahrnG" , "urhwahrng"],
"urlgg" : ["UrlGG" , "urlgg"],
"vbd" : ["VBD" , "vbd"],
"vstgb" : ["VStGB" , "vstgb"],
"vvg" : ["VVG" , "vvg"],
"verbrkrg" : ["VerbrKrG" , "verbrkrg"],
"vereinsg" : ["VereinsG" , "vereinsg"],
"verkflberg" : ["VerkFlBerG" , "verkflberg"],
"vermg" : ["VermG" , "vermg"],
"verpflg" : ["VerpflG" , "verpflg"],
"versrücklg" : ["VersRücklG" , "versr_cklg"],
"versstdv" : ["VersStDV" , "versstgdb"],
"versstg" : ["VersStG" , "versstg"],
"versg" : ["VersG" , "versammlg"],
"versatzv" : ["VersatzV" , "versatzv"],
"vgv" : ["VgV" , "vgv_2001"],
"viehverkv" : ["ViehVerkV" , "viehverkv"],
"vig" : ["VIG", "vig"],
"vwgo" : ["VwGO" , "vwgo"],
"vwkostg" : ["VwKostG" , "vwkostg"],
"vwrehag" : ["VwRehaG" , "vwrehag"],
"vwvg" : ["VwVG" , "vwvg"],
"vwvfg" : ["VwVfG" , "vwvfg"],
"vwzg" : ["VwZG" , "vwzg"],
"wg" : ["WG" , "wg"],
"wos" : ["WOS" , "wos_2002"],
"wospraug" : ["WOSprAuG" , "wospraug"],
"wpersav" : ["WPersAV" , "wpersav"],
"wpflv" : ["WPflV" , "wpflv"],
"wsg" : ["WSG" , "wsg"],
"wstatg" : ["WStatG" , "wstatg"],
"wstrg" : ["WStrG" , "wstrg"],
"waffg" : ["WaffG" , "waffg_2002"],
"waffv6üv" : ["WaffV6ÜV" , "waffv6_v"],
"wahlprg" : ["WahlPrG" , "wahlprg"],
"wassig" : ["WasSiG" , "wassig"],
"wehrpflerfv" : ["WehrPflErfV" , "wehrpflerfv"],
"wehrpflg" : ["WehrPflG" , "wehrpflg"],
"wehrbbtg" : ["WehrbBTG" , "wehrbbtg"],
"weing" : ["WeinG" , "weinv_1994"],
"weinrv" : ["WeinRV" , "weinrv"],
"weinv" : ["WeinV" , "weinv_1995"],
"weinüv" : ["WeinÜV" , "wein_v_1995"],
"wipro" : ["WiPrO" , "wipro"],
"wobindg" : ["WoBindG" , "wobindg"],
"woeigg" : ["WoEigG" , "woeigg"],
"wofg" : ["WoFG" , "wofg"],
"woflv" : ["WoFlV" , "woflv"],
"wogg" : ["WoGG" , "wogg_2"],
"wogv" : ["WoGV" , "wogv"],
"wopg" : ["WoPG" , "wopg"],
"wphg" : ["WpHG" , "wphg"],
"wpüg" : ["WpÜG" , "wp_g"],
"zesv" : ["ZESV" , "zesv"],
"zpo" : ["ZPO" , "zpo"],
"zsg" : ["ZSG" , "zsg"],
"zshg" : ["ZSHG" , "zshg"],
"zvg" : ["ZVG" , "zvg"],
"zverkv" : ["ZVerkV" , "zverkv_1998"],
"zzulv" : ["ZZulV" , "zzulv_1998"],
"zollv" : ["ZollV" , "zollv"],
"zollvg" : ["ZollVG" , "zollvg"],
"zuckartv" : ["ZuckArtV" , "zuckartv_2003"],
"zwvwv" : ["ZwVwV" , "zwvwv"],
"rhmv" : ["rhmv" , "rhmv_1994"],
"ölg" : ["ÖLG" , "_lg"],
"ökokennzg" : ["ÖkoKennzG" , "_kokennzg"]}

gesetze_string = "|".join(x for x in gesetze) #Erstellt einen String, in dem die keys durch ein | getrennt sind (für regex)


def replacement(match): #Erstellt einen Link zu https://www.gesetze-im-internet.de/ aus einer gefundenen Norm im Asciidoc-Format
                        # also URL[Link-Beschreibung], vgl. https://asciidoctor.org/docs/asciidoc-syntax-quick-reference/#links
    if match.group("gesetz").lower() == "gg": #Erforderlich, weil URLs zum GG auf der Website eine andere Struktur haben
        return r"https://www.gesetze-im-internet.de/" + gesetze[match.group("gesetz").lower()][1] + rf"/art_{match.group('norm')}.html[{match.group()}]"
    else:
        return r"https://www.gesetze-im-internet.de/" + gesetze[match.group("gesetz").lower()][1] + rf"/__{match.group('norm')}.html[{match.group()}]"

def gesetze_verlinken(text, regex):
    treffer_liste = re.finditer(regex, text) # Iterator mit allen Treffern
    ergebnis = re.subn(p, replacement, text) #Ersetzt und gibt Tuple zurück mit Zahl der Änderungen und geändertem String
    print(f"{ergebnis[1]} Änderungen vorgenommen!") #Anzahl der Änderungen anzeigen
    for m in treffer_liste:
        print(f"Match {m.group()} in Position {m.start()}")
    return ergebnis[0] #Geänderten String zurückgeben


# Für Erläuterung der Regex siehe README.md
p = re.compile(r""" # Die Regex wird in p kompiliert
(§+|Art|Artikel)\.?\s*
(?P<norm>\d+(?:\w\b)?)\s*
(?:Abs\.\s*(?P<absatz>\d+(?:\w\b)?))?\s*
(?:S\.\s*(?P<satz>\d+))?\s*
(?:Nr\.\s*(?P<nr>\d+(?:\w\b)?))?\s*
(?:lit\.\s*(?P<lit>[a-z]?))?
.{0,10}?
(?P<gesetz>%s)(?![\w-])
""" % gesetze_string, re.IGNORECASE | re.VERBOSE)

test_string = """Hier zu überprüfenden Text einfügen"""

neu = gesetze_verlinken(test_string, p)
print(neu)
