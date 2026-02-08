import os

# Folder to scan
ROOT_FOLDER = r"Siteconfigs/"

# Filenames to look for
TARGET_FILES = {
    "[ENC]unifi.com.my_0.siteconfig.php",
    "[ENC]transvision.co.id_0.siteconfig.php",
    "[ENC]pluto.tv_0.siteconfig.php",
    "[ENC]playtv.unifi.com.my_0.siteconfig.php",
    "[ENC]player.bt.com_0.siteconfig.php",
    "[ENC]mtel.ba_0.siteconfig.php",
    "[ENC]mncvision.id_0.siteconfig.php",
    "[ENC]mewatch.sg_0.siteconfig.php",
    "[ENC]firstmediax.id_0.siteconfig.php",
    "[ENC]firstmedia.com_0.siteconfig.php",
    "[ENC]dens.tv_0.siteconfig.php",
    "[ENC]cignalplay.com_0.siteconfig.php",
    "[ENC]beinsports.com[ID]_0.siteconfig.php",
    "[ENC]astro.com.my_0.siteconfig.php",
    "[ENC]alkassdigital.net_0.siteconfig.php",
    "[ENC]alkass.net_0.siteconfig.php",
    "[ENC]aisplay.ais.co.th_0.siteconfig.php",
    "[ENC][EX]visionplus.id_0.siteconfig.php",
    "[ENC][EX]tv.trueid.net[en]_1.siteconfig.php",
    "[ENC][EX]singtel.com_0.siteconfig.php",
    "[ENC][EX]radiotimes.com_0.siteconfig.php",
    "[ENC][EX]mtel.ba[msat]_0.siteconfig.php",
    "[ENC][EX]mtel.ba[iptv]_0.siteconfig.php",
    "[ENC][EX]cubmu.com_0.siteconfig.php",
    "vidio.com_0.siteconfig.php",
    "tvhebdo.com_0.siteconfig.php",
    "tvarenasport.com_ba_0.siteconfig.php",
    "sriwijayatv.tv_0.siteconfig.php",
    "spotvasia.com[ID]_0.siteconfig.php",
    "jadwaltv.net_0.siteconfig.php",
    "indosiar.com_0.siteconfig.php",
    "indihometv.com_0.siteconfig.php",
    "guidatv.sky.it_0.siteconfig.php",
    "garuda.tv_0.siteconfig.php",
    "beinsports.com[ID]_0.siteconfig.php",
}

for root, _, files in os.walk(ROOT_FOLDER):
    for filename in files:
        if filename in TARGET_FILES:
            full_path = os.path.join(root, filename)
            print(full_path)
