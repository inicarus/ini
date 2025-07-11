# -*- coding: utf-8 -*-

# بخش اضافه شده: کتابخانه‌های مورد نیاز
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
import jdatetime

# ===================================================================
# بخش اضافه شده: تابع ارسال پیام به تلگرام
# این تابع کاملاً مستقل است و در بالای کد قرار گرفته است
# ===================================================================
def send_telegram_message(bot_token, channel_id, message):
    """
    یک پیام متنی به کانال تلگرام مشخص شده ارسال می‌کند.
    """
    if not bot_token or not channel_id:
        print("توکن ربات یا شناسه کانال برای ارسال پیام تنظیم نشده است. از ارسال پیام صرف‌نظر می‌شود.")
        return
        
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': channel_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        response = requests.post(url, data=payload, timeout=15)
        response.raise_for_status()
        print("پیام تلگرام با موفقیت ارسال شد.")
    except requests.exceptions.RequestException as e:
        print(f"خطا در ارسال پیام تلگرام: {e}")

# ===================================================================
# کد اصلی شما - این بخش دست‌نخورده باقی مانده است
# ===================================================================
old_webpage_addresses = [
    "https://t.me/s/v2ray_configs_pool", "https://t.me/s/XpnTeam", "https://t.me/s/v2rayNGcloud",
    "https://t.me/s/ZibaNabz", "https://t.me/s/FreakConfig", "https://t.me/s/V_2rey",
    "https://t.me/s/V2ray_Alpha", "https://t.me/s/PROXY_MTM", "https://t.me/s/SiNABiGO",
    "https://t.me/s/v2rayng12023", "https://t.me/s/vlessconfig", "https://t.me/s/piazshekan",
    "https://t.me/s/Free_Internet_Iran", "https://t.me/s/ARv2ray", "https://t.me/s/VPNCUSTOMIZE",
    "https://t.me/s/UnlimitedDev", "https://t.me/s/MARAMBASHI", "https://t.me/s/PrivateVPNs",
    "https://t.me/s/client_proo", "https://t.me/s/nufilter", "https://t.me/s/icv2ray",
    "https://t.me/s/Vpn_Mikey", "https://t.me/s/v2rayngvpn", "https://t.me/s/kingspeedchanel",
    "https://t.me/s/VPN_Xpace", "https://t.me/s/SVNTEAM", "https://t.me/s/WPSNET",
    "https://t.me/s/v2rayng_fa2",
]

webpage_addresses = [
    "https://t.me/s/Hope_Net", "https://t.me/s/ServerNett", "https://t.me/s/alfred_config",
    "https://t.me/s/allv2ray", "https://t.me/s/alo_v2rayng", "https://t.me/s/angus_vpn",
    "https://t.me/s/antifilterservice", "https://t.me/s/arv2ray", "https://t.me/s/asak_vpn",
    "https://t.me/s/asintech", "https://t.me/s/astrovpn_official", "https://t.me/s/awlix_ir",
    "https://t.me/s/azarbayjab1", "https://t.me/s/bermudavpn24", "https://t.me/s/bigsmoke_config",
    "https://t.me/s/blueberrynetwork", "https://t.me/s/bored_vpn", "https://t.me/s/catvpns",
    "https://t.me/s/cconfig_v2ray", "https://t.me/s/city_v2rayng", "https://t.me/s/configforvpn",
    "https://t.me/s/configpositive", "https://t.me/s/configt", "https://t.me/s/configv2rayforfree",
    "https://t.me/s/custom_config", "https://t.me/s/customizev2ray", "https://t.me/s/cvrnet",
    "https://t.me/s/dailyv2ry", "https://t.me/s/daredevill_404", "https://t.me/s/deragv2ray",
    "https://t.me/s/digiv2ray", "https://t.me/s/directvpn", "https://t.me/s/donald_vpn",
    "https://t.me/s/drvpn_net", "https://t.me/s/easy_free_vpn", "https://t.me/s/entrynet",
    "https://t.me/s/ev2rayy", "https://t.me/s/expressvpn_420", "https://t.me/s/external_net",
    "https://t.me/s/farahvpn", "https://t.me/s/fasst_vpn", "https://t.me/s/fast_2ray",
    "https://t.me/s/fastkanfig", "https://t.me/s/fastshadow_vpn", "https://t.me/s/filterk0sh",
    "https://t.me/s/flyv2ray", "https://t.me/s/freakconfig", "https://t.me/s/freakconfig1",
    "https://t.me/s/freakconfig2", "https://t.me/s/free1_vpn", "https://t.me/s/free_vpn02",
    "https://t.me/s/freeconfig01", "https://t.me/s/freeconfigvpns", "https://t.me/s/freeiranweb",
    "https://t.me/s/freenapsternetv", "https://t.me/s/freev2raym", "https://t.me/s/freevirgoolnet",
    "https://t.me/s/fsv2ray", "https://t.me/s/ghalagyann", "https://t.me/s/godv2ray_ng",
    "https://t.me/s/golestan_vpn", "https://t.me/s/grizzlyvpn", "https://t.me/s/hajimamadvpn",
    "https://t.me/s/hamster_vpnn", "https://t.me/s/hatunnel_vpn", "https://t.me/s/hope_net",
    "https://t.me/s/hopev2ray", "https://t.me/s/hormozvpn", "https://t.me/s/hose_io",
    "https://t.me/s/icv2ray", "https://t.me/s/imrv2ray", "https://t.me/s/ios_v2",
    "https://t.me/s/ipcloudflaretamiz", "https://t.me/s/ipv2ray", "https://t.me/s/iranbaxvpn",
    "https://t.me/s/iraniv2ray_config", "https://t.me/s/irv2rey", "https://t.me/s/isvvpn",
    "https://t.me/s/kafing_2", "https://t.me/s/kingofilter", "https://t.me/s/lightning6",
    "https://t.me/s/ln2ray", "https://t.me/s/lombo_channel", "https://t.me/s/mahdiserver",
    "https://t.me/s/manzariyeh_rasht", "https://t.me/s/maznet", "https://t.me/s/meli_proxyy",
    "https://t.me/s/mester_v2ray", "https://t.me/s/mgvpnsale", "https://t.me/s/mikasavpn",
    "https://t.me/s/miov2ray", "https://t.me/s/moftinet", "https://t.me/s/msv2ray",
    "https://t.me/s/msv2raynp", "https://t.me/s/n2vpn", "https://t.me/s/netmellianti",
    "https://t.me/s/new_proxy_channel", "https://t.me/s/noforcedheaven", "https://t.me/s/npvv2rayfilter",
    "https://t.me/s/nufilter", "https://t.me/s/ohvpn", "https://t.me/s/orange_vpns",
    "https://t.me/s/outline_ir", "https://t.me/s/outline_vpn", "https://t.me/s/pars_vpn3",
    "https://t.me/s/parsashonam", "https://t.me/s/pashmam_vpn", "https://t.me/s/pishiserver",
    "https://t.me/s/pqv2ray", "https://t.me/s/privatevpns", "https://t.me/s/proprojec",
    "https://t.me/s/proxiiraniii", "https://t.me/s/proxy_n1", "https://t.me/s/proxyfull",
    "https://t.me/s/proxystore11", "https://t.me/s/prroxyng", "https://t.me/s/puni_shop_v2rayng",
    "https://t.me/s/qeshmserver", "https://t.me/s/realvpnmaster", "https://t.me/s/rnrifci",
    "https://t.me/s/satoshivpn", "https://t.me/s/savagev2ray", "https://t.me/s/selinc",
    "https://t.me/s/servernett", "https://t.me/s/shadowproxy66", "https://t.me/s/shokhmiplus",
    "https://t.me/s/sinavm", "https://t.me/s/sobi_vpn", "https://t.me/s/special_net8",
    "https://t.me/s/spikevpn", "https://t.me/s/srcvpn", "https://t.me/s/summertimeus",
    "https://t.me/s/superv2rang", "https://t.me/s/svnteam", "https://t.me/s/tehranargo",
    "https://t.me/s/tehranargo1", "https://t.me/s/thexconfig", "https://t.me/s/thunderv2ray",
    "https://t.me/s/tv_v2ray", "https://t.me/s/ultrasurf_12", "https://t.me/s/v2_city",
    "https://t.me/s/v2aryng_vpn", "https://t.me/s/v2boxvpnn", "https://t.me/s/v2graphy",
    "https://t.me/s/v2net_iran", "https://t.me/s/v2ngfast", "https://t.me/s/v2pedia",
    "https://t.me/s/v2ra2", "https://t.me/s/v2raand", "https://t.me/s/v2rang00",
    "https://t.me/s/v2range", "https://t.me/s/v2raxx", "https://t.me/s/v2ray1_ng",
    "https://t.me/s/v2ray6388", "https://t.me/s/v2ray_alpha07", "https://t.me/s/v2ray_configs_pool",
    "https://t.me/s/v2ray_fark", "https://t.me/s/v2ray_ng", "https://t.me/s/v2ray_one1",
    "https://t.me/s/v2ray_raha", "https://t.me/s/v2ray_rolly", "https://t.me/s/v2rayargon",
    "https://t.me/s/v2raych", "https://t.me/s/v2rayfast", "https://t.me/s/v2rayfast_7",
    "https://t.me/s/v2rayfree_irr", "https://t.me/s/v2rayiman", "https://t.me/s/v2raylandd",
    "https://t.me/s/v2rayn2g", "https://t.me/s/v2rayng3", "https://t.me/s/v2rayng_city",
    "https://t.me/s/v2rayng_madam", "https://t.me/s/v2rayng_prime", "https://t.me/s/v2rayngv",
    "https://t.me/s/v2rayngvpnn", "https://t.me/s/v2rayngzendegimamad", "https://t.me/s/v2rayprotocol",
    "https://t.me/s/v2rayyngvpn", "https://t.me/s/v2rez", "https://t.me/s/v2rray_ng",
    "https://t.me/s/v2ry_proxy", "https://t.me/s/v2ryng01", "https://t.me/s/v2ryng_vpn",
    "https://t.me/s/v2ryngfree", "https://t.me/s/v2safe", "https://t.me/s/v2safee",
    "https://t.me/s/v_2rayngvpn", "https://t.me/s/vip_vpn_2022", "https://t.me/s/vipv2rayngnp",
    "https://t.me/s/vipv2rey", "https://t.me/s/vipvpn_v2ray", "https://t.me/s/vistav2ray",
    "https://t.me/s/vlessconfig", "https://t.me/s/vmesc", "https://t.me/s/vmess_ir",
    "https://t.me/s/vmess_iran", "https://t.me/s/vmesskhodam", "https://t.me/s/vmesskhodam_vip",
    "https://t.me/s/vmessprotocol", "https://t.me/s/vp22ray", "https://t.me/s/vpfreen",
    "https://t.me/s/vpn_accounti", "https://t.me/s/vpn_free_v2ray5", "https://t.me/s/vpn_ioss",
    "https://t.me/s/vpn_kanfik", "https://t.me/s/vpn_mikey", "https://t.me/s/vpn_proxy_custom",
    "https://t.me/s/vpn_tehran", "https://t.me/s/vpn_vip_nor", "https://t.me/s/vpnazadland",
    "https://t.me/s/vpnconfignet", "https://t.me/s/vpnfail_v2ray", "https://t.me/s/vpnhubmarket",
    "https://t.me/s/vpnkanfik", "https://t.me/s/vpnmasi", "https://t.me/s/vpnowl",
    "https://t.me/s/vpnstorefast", "https://t.me/s/vpnv2rayngv", "https://t.me/s/vpnxyam_ir",
    "https://t.me/s/wedbaztel", "https://t.me/s/wsbvpn", "https://t.me/s/xpnteam",
    "https://t.me/s/xvproxy", "https://t.me/s/zede_filteri", "https://t.me/s/zibanabz",
    "https://t.me/s/zohalserver"
]

new_webaddresses = [
    "https://t.me/s/vpnaloo", "https://t.me/s/godot404", "https://t.me/s/dailyv2ry",
    "https://t.me/s/prrofile_purple", "https://t.me/s/vpnsaint", "https://t.me/s/azadnet",
    "https://t.me/s/sinavm", "https://t.me/s/appsooner", "https://t.me/s/V2SayFreeArchive",
    "https://t.me/s/shadoowvpnn", "https://t.me/s/v2fre"
]

newaddresses = [
    "https://t.me/s/ConfigsHubPlus", "https://t.me/s/imtproxy_ir", "https://t.me/s/PASARGAD_V2rayNG",
    "https://t.me/s/SRCVPN", "https://t.me/s/Outline_ir", "https://t.me/s/SvnTeam",
    "https://t.me/s/club_profsor", "https://t.me/s/Speeds_vpn1", "https://t.me/s/Airdorap_Free",
    "https://t.me/s/VPN_SOLVE", "https://t.me/s/bglvps", "https://t.me/s/YamYamProxy",
    "https://t.me/s/ProtoLandCo", "https://t.me/s/ArV2ray", "https://t.me/s/ConfigX2ray"
]

def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))

# ===================================================================
# بخش اصلی برنامه
# ===================================================================
if __name__ == "__main__":
    # خواندن توکن و شناسه کانال از متغیرهای محیطی
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')

    try:
        # منطق اصلی کد شما در اینجا اجرا می‌شود
        print("شروع فرآیند استخراج کانفیگ‌ها...")
        
        html_pages = []
        for url in newaddresses:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                html_pages.append(response.text)
                print(f"موفقیت در دریافت اطلاعات از: {url}")
            except requests.RequestException as e:
                print(f"خطا در دریافت اطلاعات از {url}: {e}")
                continue # اگر یک لینک خراب بود، به سراغ لینک بعدی برو

        codes = []
        for page in html_pages:
            soup = BeautifulSoup(page, 'html.parser')
            code_tags = soup.find_all('code')
            for code_tag in code_tags:
                code_content = code_tag.text.strip()
                if any(proto in code_content for proto in ["vless://", "ss://", "vmess://", "trojan://"]):
                    codes.append(code_content)

        codes = remove_duplicates(codes)
        print(f"تعداد {len(codes)} کانفیگ خام پیدا شد.")

        processed_codes = []
        for code in codes:
            # این بخش از کد شما کمی پیچیده بود و ساده‌سازی شد
            # هدف اصلی حذف # بعد از کانفیگ است
            processed_part = code.split("#")[0]
            processed_codes.append(processed_part)

        processed_codes = remove_duplicates(processed_codes)
        print(f"تعداد {len(processed_codes)} کانفیگ پس از پردازش اولیه باقی ماند.")

        # نوشتن کانفیگ‌ها در فایل
        current_date_time = jdatetime.datetime.now(pytz.timezone('Asia/Tehran'))
        final_string = current_date_time.strftime("%b-%d | %H:%M")
        final_others_string = current_date_time.strftime("%b-%d")

        with open("config.txt", "w", encoding="utf-8") as file:
            for i, code in enumerate(processed_codes):
                if i == 0:
                    config_name = f"#🌐 به روزرسانی شده در {final_string} | هر 15 دقیقه کانفیگ جدید داریم"
                else:
                    config_name = f"#🌐سرور {i} | {final_others_string} | MTSRVRS"
                
                config_final = code + config_name
                file.write(config_final + "\n")
        
        print(f"فایل config.txt با موفقیت با {len(processed_codes)} کانفیگ ساخته شد.")

        # ارسال پیام موفقیت به تلگرام
        success_message = (
            f"✅ **عملیات با موفقیت انجام شد**\n\n"
            f"تعداد `{len(processed_codes)}` کانفیگ جدید استخراج و در فایل `config.txt` ذخیره شد.\n"
            f"آخرین به‌روزرسانی: `{current_date_time.strftime('%Y-%m-%d %H:%M:%S')}`"
        )
        send_telegram_message(BOT_TOKEN, CHANNEL_ID, success_message)

    except Exception as e:
        print(f"یک خطای پیش‌بینی نشده در اجرای اسکریپت رخ داد: {e}")
        # در صورت بروز خطا، ارسال پیام خطا به تلگرام
        error_message = f"❌ **خطا در اجرای اسکریپت**\n\nیک مشکل در فایل `config.py` رخ داد:\n`{e}`"
        send_telegram_message(BOT_TOKEN, CHANNEL_ID, error_message)
