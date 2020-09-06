import os, sys
import yara

rules = yara.compile(filepaths={

	'namespace1':r'./malware/000_common_rules.yar',
	'namespace2':r'./malware/APT_APT1.yar',
	'namespace3':r'./malware/APT_APT10.yar',
	'namespace4':r'./malware/APT_APT15.yar',
	'namespace5':r'./malware/APT_APT17.yar',
	'namespace6':r'./malware/APT_APT29_Grizzly_Steppe.yar',
	'namespace7':r'./malware/APT_APT3102.yar',
	'namespace8':r'./malware/APT_APT9002.yar',
	'namespace9':r'./malware/APT_Backspace.yar',
	'namespace10':r'./malware/APT_Bestia.yar',
	'namespace11':r'./malware/APT_Blackenergy.yar',
	'namespace12':r'./malware/APT_Bluetermite_Emdivi.yar',
	'namespace13':r'./malware/APT_C16.yar',
	'namespace14':r'./malware/APT_Carbanak.yar',
	'namespace15':r'./malware/APT_Careto.yar',
	'namespace16':r'./malware/APT_Casper.yar',
	'namespace17':r'./malware/APT_CheshireCat.yar',
	'namespace18':r'./malware/APT_Cloudduke.yar',
	'namespace19':r'./malware/APT_Cobalt.yar',
	'namespace20':r'./malware/APT_Codoso.yar',
	'namespace22':r'./malware/APT_DeepPanda_Anthem.yar',
	'namespace23':r'./malware/APT_DeputyDog.yar',
	'namespace24':r'./malware/APT_Derusbi.yar',
	'namespace25':r'./malware/APT_DPRK_ROKRAT.yar',
	'namespace26':r'./malware/APT_Dubnium.yar',
	'namespace27':r'./malware/APT_Duqu2.yar',
	'namespace28':r'./malware/APT_Emissary.yar',
	'namespace29':r'./malware/APT_EnergeticBear_backdoored_ssh.yar',
	'namespace30':r'./malware/APT_eqgrp_apr17.yar',
	'namespace31':r'./malware/APT_Equation.yar',
	'namespace32':r'./malware/APT_EQUATIONGRP.yar',
	'namespace33':r'./malware/APT_fancybear_dnc.yar',
	'namespace34':r'./malware/APT_fancybear_downdelph.yar',
	'namespace35':r'./malware/APT_FiveEyes.yar',
	'namespace36':r'./malware/APT_furtim.yar',
	'namespace37':r'./malware/APT_FVEY_ShadowBrokers_Jan17_Screen_Strings.yar',
	'namespace39':r'./malware/APT_Greenbug.yar',
	'namespace40':r'./malware/APT_Grizzlybear_uscert.yar',
	'namespace41':r'./malware/APT_HackingTeam.yar',
	'namespace42':r'./malware/APT_Hellsing.yar',
	'namespace43':r'./malware/APT_HiddenCobra.yar',
	'namespace44':r'./malware/APT_Hikit.yar',
	'namespace45':r'./malware/APT_Industroyer.yar',
	'namespace46':r'./malware/APT_Irontiger.yar',
	'namespace47':r'./malware/APT_Kaba.yar',
	'namespace48':r'./malware/APT_Ke3Chang_TidePool.yar',
	'namespace49':r'./malware/APT_KeyBoy.yar',
	'namespace50':r'./malware/APT_LotusBlossom.yar',
	'namespace51':r'./malware/APT_Minidionis.yar',
	'namespace52':r'./malware/APT_Mirage.yar',
	'namespace53':r'./malware/APT_Molerats.yar',
	'namespace54':r'./malware/APT_Mongall.yar',
	'namespace55':r'./malware/APT_MoonlightMaze.yar',
	'namespace56':r'./malware/APT_NGO.yar',
	'namespace57':r'./malware/APT_Oilrig.yar',
	'namespace58':r'./malware/APT_OpClandestineWolf.yar',
	'namespace59':r'./malware/APT_OPCleaver.yar',
	'namespace60':r'./malware/APT_OpDustStorm.yar',
	'namespace61':r'./malware/APT_OpPotao.yar',
	'namespace62':r'./malware/APT_Passcv.yar',
	'namespace63':r'./malware/APT_PCclient.yar',
	'namespace64':r'./malware/APT_Pipcreat.yar',
	'namespace65':r'./malware/APT_Platinum.yar',
	'namespace66':r'./malware/APT_Poseidon_Group.yar',
	'namespace67':r'./malware/APT_Prikormka.yar',
	'namespace68':r'./malware/APT_PutterPanda.yar',
	'namespace69':r'./malware/APT_RedLeaves.yar',
	'namespace70':r'./malware/APT_Regin.yar',
	'namespace71':r'./malware/APT_RemSec.yar',
	'namespace72':r'./malware/APT_Sauron.yar',
	'namespace73':r'./malware/APT_Sauron_extras.yar',
	'namespace74':r'./malware/APT_Scarab_Scieron.yar',
	'namespace75':r'./malware/APT_Seaduke.yar',
	'namespace77':r'./malware/APT_Snowglobe_Babar.yar',
	'namespace78':r'./malware/APT_Sofacy_Bundestag.yar',
	'namespace79':r'./malware/APT_Sofacy_Fysbis.yar',
	'namespace80':r'./malware/APT_Sofacy_Jun16.yar',
	'namespace81':r'./malware/APT_Sphinx_Moth.yar',
	'namespace82':r'./malware/APT_Stuxnet.yar',
	'namespace83':r'./malware/APT_Terracota.yar',
	'namespace84':r'./malware/APT_ThreatGroup3390.yar',
	'namespace85':r'./malware/APT_TradeSecret.yar',
	'namespace86':r'./malware/APT_Turla_Neuron.yar',
	'namespace87':r'./malware/APT_Turla_RUAG.yar',
	'namespace88':r'./malware/APT_Unit78020.yar',
	'namespace89':r'./malware/APT_UP007_SLServer.yar',
	'namespace91':r'./malware/APT_Waterbug.yar',
	'namespace92':r'./malware/APT_WildNeutron.yar',
	'namespace93':r'./malware/APT_Windigo_Onimiki.yar',
	'namespace94':r'./malware/APT_Winnti.yar',
	'namespace95':r'./malware/APT_WoolenGoldfish.yar',
	'namespace96':r'./malware/EXPERIMENTAL_Beef.yar',
	'namespace97':r'./malware/GEN_PowerShell.yar',
	'namespace98':r'./malware/MalConfScan.yar',
	'namespace99':r'./malware/MALW_adwind_RAT.yar',
	'namespace100':r'./malware/MALW_AgentTesla.yar',
	'namespace101':r'./malware/MALW_AgentTesla_SMTP.yar',
	'namespace102':r'./malware/MALW_Alina.yar',
	'namespace103':r'./malware/MALW_AlMashreq.yar',
	'namespace104':r'./malware/MALW_Andromeda.yar',
	'namespace105':r'./malware/MALW_Arkei.yar',
	'namespace106':r'./malware/MALW_Athena.yar',
	'namespace107':r'./malware/MALW_Atmos.yar',
	'namespace108':r'./malware/MALW_ATMPot.yar',
	'namespace109':r'./malware/MALW_ATM_HelloWorld.yar',
	'namespace111':r'./malware/MALW_BackdoorSSH.yar',
	'namespace112':r'./malware/MALW_Backoff.yar',
	'namespace113':r'./malware/MALW_Bangat.yar',
	'namespace114':r'./malware/MALW_Batel.yar',
	'namespace115':r'./malware/MALW_BlackRev.yar',
	'namespace116':r'./malware/MALW_BlackWorm.yar',
	'namespace117':r'./malware/MALW_Boouset.yar',
	'namespace118':r'./malware/MALW_Bublik.yar',
	'namespace119':r'./malware/MALW_Buzus_Softpulse.yar',
	'namespace120':r'./malware/MALW_CAP_HookExKeylogger.yar',
	'namespace121':r'./malware/MALW_Chicken.yar',
	'namespace122':r'./malware/MALW_Citadel.yar',
	'namespace123':r'./malware/MALW_Cloaking.yar',
	'namespace124':r'./malware/MALW_Cookies.yar',
	'namespace125':r'./malware/MALW_Corkow.yar',
	'namespace126':r'./malware/MALW_Cxpid.yar',
	'namespace127':r'./malware/MALW_Cythosia.yar',
	'namespace128':r'./malware/MALW_DDoSTf.yar',
	'namespace129':r'./malware/MALW_Derkziel.yar',
	'namespace130':r'./malware/MALW_Dexter.yar',
	'namespace131':r'./malware/MALW_DiamondFox.yar',
	'namespace132':r'./malware/MALW_DirtJumper.yar',
	'namespace133':r'./malware/MALW_Eicar.yar',
	'namespace134':r'./malware/MALW_Elex.yar',
	'namespace135':r'./malware/MALW_Elknot.yar',
	'namespace136':r'./malware/MALW_Emotet.yar',
	'namespace137':r'./malware/MALW_Empire.yar',
	'namespace138':r'./malware/MALW_Enfal.yar',
	'namespace139':r'./malware/MALW_Exploit_UAC_Elevators.yar',
	'namespace140':r'./malware/MALW_Ezcob.yar',
	'namespace141':r'./malware/MALW_F0xy.yar',
	'namespace142':r'./malware/MALW_FakeM.yar',
	'namespace143':r'./malware/MALW_FALLCHILL.yar',
	'namespace144':r'./malware/MALW_Fareit.yar',
	'namespace145':r'./malware/MALW_Favorite.yar',
	'namespace146':r'./malware/MALW_FUDCrypt.yar',
	'namespace147':r'./malware/MALW_Furtim.yar',
	'namespace148':r'./malware/MALW_Gafgyt.yar',
	'namespace149':r'./malware/MALW_Genome.yar',
	'namespace150':r'./malware/MALW_Glasses.yar',
	'namespace151':r'./malware/MALW_Gozi.yar',
	'namespace152':r'./malware/MALW_Grozlex.yar',
	'namespace154':r'./malware/MALW_hancitor.yar',
	'namespace155':r'./malware/MALW_Hsdfihdf_banking.yar',
	'namespace157':r'./malware/MALW_IcedID.yar',
	'namespace158':r'./malware/MALW_Iexpl0ree.yar',
	'namespace159':r'./malware/MALW_IMuler.yar',
	'namespace160':r'./malware/MALW_Install11.yar',
	'namespace161':r'./malware/MALW_Intel_Virtualization.yar',
	'namespace162':r'./malware/MALW_IotReaper.yar',
	'namespace163':r'./malware/MALW_Jolob_Backdoor.yar',
	'namespace164':r'./malware/MALW_Kelihos.yar',
	'namespace165':r'./malware/MALW_KeyBase.yar',
	'namespace166':r'./malware/MALW_KINS.yar',
	'namespace167':r'./malware/MALW_kirbi_mimikatz.yar',
	'namespace168':r'./malware/MALW_Korlia.yar',
	'namespace169':r'./malware/MALW_Korplug.yar',
	'namespace170':r'./malware/MALW_Kovter.yar',
	'namespace171':r'./malware/MALW_kpot.yar',
	'namespace172':r'./malware/MALW_Kraken.yar',
	'namespace173':r'./malware/MALW_Kwampirs.yar',
	'namespace174':r'./malware/MALW_Lateral_Movement.yar',
	'namespace175':r'./malware/MALW_Lenovo_Superfish.yar',
	'namespace176':r'./malware/MALW_LinuxBew.yar',
	'namespace177':r'./malware/MALW_LinuxHelios.yar',
	'namespace178':r'./malware/MALW_LinuxMoose.yar',
	'namespace179':r'./malware/MALW_LostDoor.yar',
	'namespace180':r'./malware/MALW_LuaBot.yar',
	'namespace181':r'./malware/MALW_LuckyCat.yar',
	'namespace182':r'./malware/MALW_LURK0.yar',
	'namespace183':r'./malware/MALW_MacControl.yar',
	'namespace184':r'./malware/MALW_Madness.yar',
	'namespace185':r'./malware/MALW_Magento_backend.yar',
	'namespace186':r'./malware/MALW_Magento_frontend.yar',
	'namespace187':r'./malware/MALW_Magento_suspicious.yar',
	'namespace188':r'./malware/MALW_Mailers.yar',
	'namespace189':r'./malware/MALW_marap.yar',
	'namespace190':r'./malware/MALW_MedusaHTTP_2019.yar',
	'namespace191':r'./malware/MALW_Miancha.yar',
	'namespace192':r'./malware/MALW_MiniAsp3_mem.yar',
	'namespace196':r'./malware/MALW_Miscelanea.yar',
	'namespace197':r'./malware/MALW_Miscelanea_Linux.yar',
	'namespace198':r'./malware/MALW_Monero_Miner_installer.yar',
	'namespace199':r'./malware/MALW_MSILStealer.yar',
	'namespace200':r'./malware/MALW_Naikon.yar',
	'namespace201':r'./malware/MALW_Naspyupdate.yar',
	'namespace202':r'./malware/MALW_NetTraveler.yar',
	'namespace203':r'./malware/MALW_NionSpy.yar',
	'namespace204':r'./malware/MALW_Notepad.yar',
	'namespace205':r'./malware/MALW_NSFree.yar',
	'namespace206':r'./malware/MALW_Odinaff.yar',
	'namespace207':r'./malware/MALW_Olyx.yar',
	'namespace208':r'./malware/MALW_OSX_Leverage.yar',
	'namespace209':r'./malware/MALW_PE_sections.yar',
	'namespace210':r'./malware/MALW_PittyTiger.yar',
	'namespace211':r'./malware/MALW_PolishBankRat.yar',
	'namespace212':r'./malware/MALW_Ponmocup.yar',
	'namespace213':r'./malware/MALW_Pony.yar',
	'namespace214':r'./malware/MALW_Predator.yar',
	'namespace215':r'./malware/MALW_PubSab.yar',
	'namespace216':r'./malware/MALW_Pyinstaller.yar',
	'namespace217':r'./malware/MALW_PyPI.yar',
	'namespace218':r'./malware/MALW_Quarian.yar',
	'namespace220':r'./malware/MALW_Regsubdat.yar',
	'namespace221':r'./malware/MALW_Retefe.yar',
	'namespace222':r'./malware/MALW_Rockloader.yar',
	'namespace223':r'./malware/MALW_Rooter.yar',
	'namespace224':r'./malware/MALW_Rovnix.yar',
	'namespace225':r'./malware/MALW_Safenet.yar',
	'namespace226':r'./malware/MALW_Sakurel.yar',
	'namespace227':r'./malware/MALW_Sayad.yar',
	'namespace228':r'./malware/MALW_Scarhikn.yar',
	'namespace229':r'./malware/MALW_Sendsafe.yar',
	'namespace230':r'./malware/MALW_Shamoon.yar',
	'namespace231':r'./malware/MALW_Shifu.yar',
	'namespace232':r'./malware/MALW_shifu_shiz.yar',
	'namespace233':r'./malware/MALW_sitrof_fortis_scar.yar',
	'namespace234':r'./malware/MALW_Skeleton.yar',
	'namespace235':r'./malware/MALW_Spora.yar',
	'namespace236':r'./malware/MALW_Sqlite.yar',
	'namespace237':r'./malware/MALW_Stealer.yar',
	'namespace238':r'./malware/MALW_Surtr.yar',
	'namespace239':r'./malware/MALW_T5000.yar',
	'namespace240':r'./malware/MALW_Tedroo.yar',
	'namespace241':r'./malware/MALW_Tinba.yar',
	'namespace244':r'./malware/MALW_TreasureHunt.yar',
	'namespace245':r'./malware/MALW_TrickBot.yar',
	'namespace246':r'./malware/MALW_TRITON_HATMAN.yar',
	'namespace247':r'./malware/MALW_TRITON_ICS_FRAMEWORK.yar',
	'namespace248':r'./malware/MALW_Trumpbot.yar',
	'namespace249':r'./malware/MALW_Upatre.yar',
	'namespace250':r'./malware/MALW_Urausy.yar',
	'namespace251':r'./malware/MALW_Vidgrab.yar',
	'namespace252':r'./malware/MALW_viotto_keylogger.yar',
	'namespace253':r'./malware/MALW_Virut_FileInfector_UNK_VERSION.yar',
	'namespace254':r'./malware/MALW_Volgmer.yar',
	'namespace255':r'./malware/MALW_Wabot.yar',
	'namespace256':r'./malware/MALW_Warp.yar',
	'namespace257':r'./malware/MALW_Wimmie.yar',
	'namespace258':r'./malware/MALW_xDedic_marketplace.yar',
	'namespace259':r'./malware/MALW_XHide.yar',
	'namespace260':r'./malware/MALW_XMRIG_Miner.yar',
	'namespace261':r'./malware/MALW_XOR_DDos.yar',
	'namespace262':r'./malware/MALW_Yayih.yar',
	'namespace263':r'./malware/MALW_Yordanyan_ActiveAgent.yar',
	'namespace264':r'./malware/MALW_Zegost.yar',
	'namespace265':r'./malware/MALW_Zeus.yar',
	'namespace266':r'./malware/POS.yar',
	'namespace267':r'./malware/POS_Bernhard.yar',
	'namespace268':r'./malware/POS_BruteforcingBot.yar',
	'namespace269':r'./malware/POS_Easterjack.yar',
	'namespace270':r'./malware/POS_FastPOS.yar',
	'namespace271':r'./malware/POS_LogPOS.yar',
	'namespace272':r'./malware/POS_MalumPOS.yar',
	'namespace273':r'./malware/POS_Mozart.yar',
	'namespace274':r'./malware/RANSOM_.CRYPTXXX.yar',
	'namespace275':r'./malware/RANSOM_777.yar',
	'namespace276':r'./malware/RANSOM_acroware.yar',
	'namespace277':r'./malware/RANSOM_Alpha.yar',
	'namespace279':r'./malware/RANSOM_Cerber.yar',
	'namespace280':r'./malware/RANSOM_Comodosec.yar',
	'namespace281':r'./malware/RANSOM_Crypren.yar',
	'namespace282':r'./malware/RANSOM_Cryptolocker.yar',
	'namespace283':r'./malware/RANSOM_CryptoNar.yar',
	'namespace284':r'./malware/RANSOM_DMALocker.yar',
	'namespace285':r'./malware/RANSOM_DoublePulsar_Petya.yar',
	'namespace286':r'./malware/RANSOM_Erebus.yar',
	'namespace287':r'./malware/RANSOM_GoldenEye.yar',
	'namespace288':r'./malware/RANSOM_GPGQwerty.yar',
	'namespace289':r'./malware/RANSOM_jeff_dev.yar',
	'namespace290':r'./malware/RANSOM_locdoor.yar',
	'namespace291':r'./malware/RANSOM_Locky.yar',
	'namespace292':r'./malware/RANSOM_Maze.yar',
	'namespace293':r'./malware/RANSOM_MS17-010_Wannacrypt.yar',
	'namespace294':r'./malware/RANSOM_PetrWrap.yar',
	'namespace295':r'./malware/RANSOM_Petya.yar',
	'namespace296':r'./malware/RANSOM_Petya_MS17_010.yar',
	'namespace297':r'./malware/RANSOM_Pico.yar',
	'namespace299':r'./malware/RANSOM_Satana.yar',
	'namespace300':r'./malware/RANSOM_screenlocker_5h311_1nj3c706.yar',
	'namespace301':r'./malware/RANSOM_Shiva.yar',
	'namespace302':r'./malware/RANSOM_shrug2.yar',
	'namespace303':r'./malware/RANSOM_Sigma.yar',
	'namespace304':r'./malware/RANSOM_Snake.yar',
	'namespace305':r'./malware/RANSOM_Stampado.yar',
	'namespace306':r'./malware/RANSOM_termite.yar',
	'namespace307':r'./malware/RANSOM_TeslaCrypt.yar',
	'namespace308':r'./malware/RANSOM_Tox.yar',
	'namespace309':r'./malware/RAT_Adwind.yar',
	'namespace310':r'./malware/RAT_Adzok.yar',
	'namespace311':r'./malware/RAT_Asyncrat.yar',
	'namespace312':r'./malware/RAT_BlackShades.yar',
	'namespace313':r'./malware/RAT_Bolonyokte.yar',
	'namespace314':r'./malware/RAT_Bozok.yar',
	'namespace315':r'./malware/RAT_Cerberus.yar',
	'namespace316':r'./malware/RAT_Crimson.yar',
	'namespace318':r'./malware/RAT_CyberGate.yar',
	'namespace319':r'./malware/RAT_DarkComet.yar',
	'namespace320':r'./malware/RAT_FlyingKitten.yar',
	'namespace321':r'./malware/RAT_Gh0st.yar',
	'namespace322':r'./malware/RAT_Gholee.yar',
	'namespace323':r'./malware/RAT_Glass.yar',
	'namespace324':r'./malware/RAT_Havex.yar',
	'namespace325':r'./malware/RAT_Hizor.yar',
	'namespace326':r'./malware/RAT_Indetectables.yar',
	'namespace327':r'./malware/RAT_Inocnation.yar',
	'namespace328':r'./malware/RAT_jRAT.yar',
	'namespace329':r'./malware/RAT_Meterpreter_Reverse_Tcp.yar',
	'namespace330':r'./malware/RAT_Nanocore.yar',
	'namespace331':r'./malware/RAT_NetwiredRC.yar',
	'namespace332':r'./malware/RAT_Njrat.yar',
	'namespace333':r'./malware/RAT_Orcus.yar',
	'namespace334':r'./malware/RAT_PlugX.yar',
	'namespace335':r'./malware/RAT_PoetRATDoc.yar',
	'namespace336':r'./malware/RAT_PoetRATPython.yar',
	'namespace337':r'./malware/RAT_PoisonIvy.yar',
	'namespace338':r'./malware/RAT_Ratdecoders.yar',
	'namespace339':r'./malware/RAT_Sakula.yar',
	'namespace340':r'./malware/RAT_ShadowTech.yar',
	'namespace341':r'./malware/RAT_Shim.yar',
	'namespace342':r'./malware/RAT_Terminator.yar',
	'namespace343':r'./malware/RAT_xRAT.yar',
	'namespace344':r'./malware/RAT_xRAT20.yar',
	'namespace345':r'./malware/RAT_Xtreme.yar',
	'namespace346':r'./malware/RAT_ZoxPNG.yar',
	'namespace347':r'./malware/TOOLKIT_Chinese_Hacktools.yar',
	'namespace348':r'./malware/TOOLKIT_Dubrute.yar',
	'namespace349':r'./malware/TOOLKIT_exe2hex_payload.yar',
	'namespace350':r'./malware/TOOLKIT_FinFisher_.yar',
	'namespace351':r'./malware/TOOLKIT_Gen_powerkatz.yar',
	'namespace353':r'./malware/TOOLKIT_PassTheHash.yar',
	'namespace354':r'./malware/TOOLKIT_Powerstager.yar',
	'namespace355':r'./malware/TOOLKIT_Pwdump.yar',
	'namespace356':r'./malware/TOOLKIT_THOR_HackTools.yar',
	'namespace357':r'./malware/TOOLKIT_Wineggdrop.yar',

})


# for loop iterate through os obtained files

path = input("input: ")
dirs = os.listdir(path)

for root, dirs, files in os.walk(path):
    for f in files:
        try:
            pathsingle = os.path.join(root,f)
            matches = rules.match("'" + pathsingle + "'")
        except:
            continue
        if matches == True:
            print(matches)
            print("Malware was detected. Would you like to remove it?")
            answer = input("Please type Y/N")
            if answer == "Y":
                os.remove(f)
        