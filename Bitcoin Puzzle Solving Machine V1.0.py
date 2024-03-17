"""
Bitcoin Puzzle Solving Machine V1.0

Developed by Mustafa AKBAL 
                                             ██████╗██╗  ██╗ █████╗ ██╗    ██╗██████╗ ███████╗███████╗██╗  ██╗
                                            ██╔════╝██║  ██║██╔══██╗██║    ██║██╔══██╗██╔════╝██╔════╝██║  ██║
                                            ██║     ███████║███████║██║ █╗ ██║██████╔╝█████╗  ███████╗███████║
                                            ██║     ██╔══██║██╔══██║██║███╗██║██╔══██╗██╔══╝  ╚════██║██╔══██║
                                            ╚██████╗██║  ██║██║  ██║╚███╔███╔╝██║  ██║███████╗███████║██║  ██║
                                             ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
                                            AUTHOR : Mustafa AKBAL e-mail: mstf.akbal@gmail.com 
                                            Telegram: @chawresho   Instagram: mstf.akbal
                                             ================= DONATE ADDRESSES ========================
                                            BTC p2pkh                : 191QB72rS77vP8NC1EC11wWqKtkfbm5SM8
                                            BTC p2wpkh               : bc1q2l29nc6puvuk0rn449wf6l8rm62wuxst7uvjeu
                                            BTC p2wpkh_in_p2sh       : 3AkjfoQn494K5FBdqMrnQRr4UsWji7Az62
                                            BTC p2wsh_in_p2sh        : 3Cf3J2jw4xx8DVuwHDiQuVrsRoroUgzd7M
                                            BTC p2sh                 : 3LPo8JHFdXZxvyZDQiWxiWCvPYU4oUhyHz
                                            BTC p2wsh                : bc1q47rduwq76v4fteqvxm8p9axq39nq25kurgwlyaefmyqz3nhyc8rscuhwwq
                                            ETH/BSC/AVAX/POLYGON     : 0x279f020A74BfE5Ba6a539B0f523D491A4122d18D
                                            TRX                      : TDahqcDTkM2qnfoCPfed1YhcB5Eocc2Cwe
                                            DOGE                     : DD9ViMyVjX2Cv8YnjpBZZhgSD2Uy1NQVbk
                                            DASH dash_p2pkh          : XihF1MgkPpLWY4xms7WDsUCdAELMiBXCFZ
                                            ZEC zec_p2pkh            : t1Rt1BSSzQRuWymR5wf189kckaYwkSSQAb1
                                            LTC ltc_p2pkh            : LTEMSKLgWmMydw4MBNBJHxabY77wp1zyZ6
                                            LTC ltc_p2sh             : MSbwSBhDaeRPjUq7WbWJY9TKiF4WpZbBd8
                                            LTC ltc_p2wsh            : ltc1q47rduwq76v4fteqvxm8p9axq39nq25kurgwlyaefmyqz3nhyc8rsmce759
                                            LTC ltc_p2wpkh           : ltc1q2l29nc6puvuk0rn449wf6l8rm62wuxst6qkkpv


License: MIT License  
Note: This application is the result of hard work and dedication. Please do not distribute it without permission and respect the effort put into its development.

Legal Disclaimer and Warning for Unlawful Use

THE USE OF THIS SOFTWARE FOR ANY ILLEGAL ACTIVITY IS STRICTLY PROHIBITED. THE AUTHORS AND COPYRIGHT HOLDERS OF THIS SOFTWARE DISCLAIM ANY LEGAL RESPONSIBILITY FOR UNLAWFUL USE OR ENGAGEMENT IN ILLEGAL ACTIVITIES USING THIS SOFTWARE.

USERS ARE SOLELY RESPONSIBLE FOR ENSURING THAT THEIR USE OF THIS SOFTWARE COMPLIES WITH APPLICABLE LAWS AND REGULATIONS. ANY UNLAWFUL ACTIVITIES UNDERTAKEN USING THIS SOFTWARE ARE AT THE USER'S OWN RISK.

THIS SOFTWARE IS INTENDED FOR LEGAL AND ETHICAL USE ONLY. ANY USE CONTRARY TO LOCAL, NATIONAL, OR INTERNATIONAL LAWS IS EXPRESSLY PROHIBITED. THE AUTHORS AND COPYRIGHT HOLDERS DO NOT SUPPORT OR CONDONE ILLEGAL ACTIVITIES.

BY USING THIS SOFTWARE, YOU ACKNOWLEDGE AND AGREE THAT UNLAWFUL USE MAY RESULT IN LEGAL CONSEQUENCES, INCLUDING BUT NOT LIMITED TO CRIMINAL PROSECUTION AND CIVIL LIABILITY.

IF YOU ENGAGE IN ILLEGAL ACTIVITIES, YOU DO SO AT YOUR OWN PERIL, AND THE AUTHORS AND COPYRIGHT HOLDERS SHALL NOT BE HELD LIABLE FOR ANY SUCH ACTIONS.

IT IS STRONGLY ADVISED TO USE THIS SOFTWARE RESPONSIBLY AND LEGALLY. IF YOU CANNOT COMPLY WITH THESE TERMS, YOU SHOULD IMMEDIATELY CEASE THE USE OF THIS SOFTWARE.


Disclaimer of Liability

THE USE OF THIS SOFTWARE AND ANY ACTIONS RESULTING FROM IT ARE THE SOLE RESPONSIBILITY OF THE USER. THE AUTHORS AND COPYRIGHT HOLDERS OF THIS SOFTWARE ARE NOT LIABLE FOR ANY DAMAGES, LOSSES, OR RESPONSIBILITIES ARISING OUT OF THE USE OF THIS SOFTWARE.

THIS SOFTWARE IS PROVIDED "AS IS," WITHOUT ANY WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. NO WARRANTIES ARE PROVIDED FOR THE USE OF THIS SOFTWARE.

THE USE OF THIS SOFTWARE MAY INVOLVE RISKS OF DAMAGE TO COMPUTER SYSTEMS OR DATA. USERS SHOULD TAKE NECESSARY SECURITY PRECAUTIONS BEFORE USING THE SOFTWARE AND SHOULD BE SURE TO BACK UP THEIR DATA BEFORE CONTINUING TO USE THE SOFTWARE.

THE USE OF THE SOFTWARE IMPLIES THAT YOU UNDERSTAND AND ACCEPT THIS DISCLAIMER OF LIABILITY IN ITS ENTIRETY. IF YOU DO NOT AGREE TO THESE TERMS, YOU SHOULD NOT USE THE SOFTWARE.


"""

from bit import *
from bit.format import bytes_to_wif
import random, codecs, sys, atexit, time, requests, os
from rich.console import Console
import os
from rich.panel import Panel
from rich.traceback import install
from rich import print

install()
console = Console()
appPath = os.path.dirname(os.path.abspath(__file__))
found_addresses_filename = os.path.join(appPath, 'found.txt')



author = ("""[gold1 on grey15]\
                                             ██████╗██╗  ██╗ █████╗ ██╗    ██╗██████╗ ███████╗███████╗██╗  ██╗
                                            ██╔════╝██║  ██║██╔══██╗██║    ██║██╔══██╗██╔════╝██╔════╝██║  ██║
                                            ██║     ███████║███████║██║ █╗ ██║██████╔╝█████╗  ███████╗███████║
                                            ██║     ██╔══██║██╔══██║██║███╗██║██╔══██╗██╔══╝  ╚════██║██╔══██║
                                            ╚██████╗██║  ██║██║  ██║╚███╔███╔╝██║  ██║███████╗███████║██║  ██║
                                             ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
                                            AUTHOR : Mustafa AKBAL e-mail: mstf.akbal@gmail.com 
                                            Telegram: @chawresho   Instagram: mstf.akbal
                                             ================= DONATE ADDRESSES ========================
                                            Compressed Address: 191QB72rS77vP8NC1EC11wWqKtkfbm5SM8
                                            UnCompressed Address: 1HTZrCDM9Qsp7aztvbeSo5cP7u9dbwn6Qr
                                            BTC p2pkh                : 191QB72rS77vP8NC1EC11wWqKtkfbm5SM8
                                            BTC p2wpkh               : bc1q2l29nc6puvuk0rn449wf6l8rm62wuxst7uvjeu
                                            BTC p2wpkh_in_p2sh       : 3AkjfoQn494K5FBdqMrnQRr4UsWji7Az62
                                            BTC p2wsh_in_p2sh        : 3Cf3J2jw4xx8DVuwHDiQuVrsRoroUgzd7M
                                            BTC p2sh                 : 3LPo8JHFdXZxvyZDQiWxiWCvPYU4oUhyHz
                                            BTC p2wsh                : bc1q47rduwq76v4fteqvxm8p9axq39nq25kurgwlyaefmyqz3nhyc8rscuhwwq
                                            ETH/BSC/AVAX/POLYGON     : 0x279f020A74BfE5Ba6a539B0f523D491A4122d18D
                                            TRX                      : TDahqcDTkM2qnfoCPfed1YhcB5Eocc2Cwe
                                            DOGE                     : DD9ViMyVjX2Cv8YnjpBZZhgSD2Uy1NQVbk
                                            DASH dash_p2pkh          : XihF1MgkPpLWY4xms7WDsUCdAELMiBXCFZ
                                            ZEC zec_p2pkh            : t1Rt1BSSzQRuWymR5wf189kckaYwkSSQAb1
                                            LTC ltc_p2pkh            : LTEMSKLgWmMydw4MBNBJHxabY77wp1zyZ6
                                            LTC ltc_p2sh             : MSbwSBhDaeRPjUq7WbWJY9TKiF4WpZbBd8
                                            LTC ltc_p2wsh            : ltc1q47rduwq76v4fteqvxm8p9axq39nq25kurgwlyaefmyqz3nhyc8rsmce759
                                            LTC ltc_p2wpkh           : ltc1q2l29nc6puvuk0rn449wf6l8rm62wuxst6qkkpv[/]""")


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

animation = ["□□□□□□□□□□□□□□□□□□□□  0%", "■□□□□□□□□□□□□□□□□□□□  5%", "■■□□□□□□□□□□□□□□□□□□ 10%",
             "■■■□□□□□□□□□□□□□□□□□ 15%", "■■■■□□□□□□□□□□□□□□□□ 20%", "■■■■■□□□□□□□□□□□□□□□ 25%",
             "■■■■■■□□□□□□□□□□□□□□ 30%", "■■■■■■■□□□□□□□□□□□□□ 35%", "■■■■■■■■□□□□□□□□□□□□ 40%",
             "■■■■■■■■■□□□□□□□□□□□ 45%", "■■■■■■■■■■□□□□□□□□□□ 50%", "■■■■■■■■■■■□□□□□□□□□ 55%",
             "■■■■■■■■■■■■□□□□□□□□ 60%", "■■■■■■■■■■■■■□□□□□□□ 65%", "■■■■■■■■■■■■■■□□□□□□ 70%",
             "■■■■■■■■■■■■■■■□□□□□ 75%", "■■■■■■■■■■■■■■■■□□□□ 80%", "■■■■■■■■■■■■■■■■■□□□ 85%",
             "■■■■■■■■■■■■■■■■■■□□ 90%", "■■■■■■■■■■■■■■■■■■■□ 95%", "■■■■■■■■■■■■■■■■■■■■100%"]

def get_all_key(data):
    key = Key.from_int(data[-1])
    wifu = bytes_to_wif(key.to_bytes(), compressed=False)
    wifc = bytes_to_wif(key.to_bytes(), compressed=True)
    keyu = Key(wifu)
    caddr = key.address
    uaddr = keyu.address
    result = {
        'key': key,
        'wifu': wifu,
        'wifc': wifc,
        'keyu': keyu,
        'caddr': caddr,
        'uaddr': uaddr
    }
    return result


def main():
    counter = 0
    found = 0
    total = 0
    pagenumber = 0  # Initialize pagenumber here
    while True:
        ran = random.randrange(a, b)
        seed = str(ran)
        data_wallet = map(get_all_key, [(i, ran + i) for i in range(128)])
        wallets = [wallet_ for wallet_ in data_wallet]
        query = [i['caddr'] for i in wallets]
        query1 = [i['uaddr'] for i in wallets]
        counter += 1
        total += 256

        pagenumber = (int(seed) // 128) + 1
        if len(query) == 128 or len(query1) == 128:

            try:
                request = requests.get(
                    "https://blockchain.info/multiaddr?active=%s" % ','.join(query) + '&base=BCH&cors=true', timeout=10)
                request = request.json()

                def find_wallet():
                    with open(found_addresses_filename, "a") as f:
                        print("start write")
                        text = f"""\nBitcoin Address with Balance Found
                                \nPage Number: {str(pagenumber)}
                                \nPrivateKey (hex): {wallets[0]['key'].to_hex()}
                                \nBitcoin Address Compressed : {wallets[0]['caddr']}
                                \nBitcoin Address UnCompressed : {wallets[0]['uaddr']}
                                \nPrivateKey (wif) Compressed :  {wallets[0]['wifc']}
                                \nPrivateKey (wif) UnCompressed : {wallets[0]['wifu']}\n"""
                        f.write(text)
                        found += 1

                for row in request["addresses"]:
                    #print(row)
                    if row["final_balance"] or row["total_received"] > 0:
                        find_wallet()
                        break
                request1 = requests.get("https://blockchain.info/multiaddr?active=%s" % ','.join(query1), timeout=10)
                request1 = request1.json()

                for row in request1["addresses"]:
                    #print(row)
                    if row["final_balance"] or row["total_received"] > 0:
                        find_wallet()
                        break
            except:
                time.sleep(5)
                try:
                    request = requests.get(
                        "https://blockchain.info/multiaddr?active=%s" % ','.join(query) + '&base=BCH&cors=true', timeout=10)
                    request = request.json()

                    def find_wallet():
                        with open(found_addresses_filename, "a") as f:
                            print("start write")
                            text = f"""\nBitcoin Address with Balance Found
                                    \nPage Number: {str(pagenumber)}
                                    \nPrivateKey (hex): {wallets[0]['key'].to_hex()}
                                    \nBitcoin Address Compressed : {wallets[0]['caddr']}
                                    \nBitcoin Address UnCompressed : {wallets[0]['uaddr']}
                                    \nPrivateKey (wif) Compressed :  {wallets[0]['wifc']}
                                    \nPrivateKey (wif) UnCompressed : {wallets[0]['wifu']}n"""
                            f.write(text)
                            found += 1

                    for row in request["addresses"]:
                        #print(row)
                        if row["final_balance"] or row["total_received"] > 0:
                            find_wallet()
                            break
                    request1 = requests.get("https://blockchain.info/multiaddr?active=%s" % ','.join(query1), timeout=10)
                    request1 = request1.json()

                    for row in request1["addresses"]:
                        #print(row)
                        if row["final_balance"] or row["total_received"] > 0:
                            find_wallet()
                            break
                except:
                    pass

            query = []

            clear_terminal()
            print(author)
            infoPanel = (
                f"[gold1 on grey15]PAGE NUMBER : [green_yellow][bold]{str(pagenumber)}[/][gold1 on grey15] "
                f"[gold1 on grey15]TOTAL CHECKED : [orange_red1]{str(total)} [/]"
                f"[gold1 on grey15]FOUND: [white]{str(found)}[/]\n"
                f"[gold1 on grey15]PRIVATE KEY (HEX):       : [grey54]{wallets[0]['key'].to_hex()}[/]\n"
                 f"[gold1 on grey15]PRIVATE KEY (DEC):       : [grey54]{seed}[/]\n"
                f"[gold1 on grey15]Bitcoin Address  Compressed : [white]{wallets[0]['caddr']}[/]\n"
                f"[gold1 on grey15]Bitcoin Address UnCompressed : [white]{wallets[0]['uaddr']}[/]\n"
                f"[gold1 on grey15]PrivateKey (wif) Compressed :  [white]{wallets[0]['wifc']}[/]\n"
                f"[gold1 on grey15]PrivateKey (wif) UnCompressed : [white]{wallets[0]['wifu']}[/]\n"
            )
            style = "bold on grey11"

            console.print(
                Panel(str(infoPanel), title="[white]BITCOIN PUZZLE SOLVING MACHINE[/]",
                      subtitle="[green_yellow] Developed By Mustafa AKBAL contact: mstf.akbal@gmail.com [/]", style="gold1"), style=style, justify="full"
            )
            for i in range(len(animation)):
                time.sleep(0.1)
                console.print(" [gold1 on grey15]Loading Next Lucky Page:[/]" + animation[i % len(animation)], end="\r")

if __name__ == '__main__':
    console.print("[gold1 on grey15]               PROGRAM IS STARTING[/]")
    console.print("[gold1 on grey15] Input Range to start [orange_red1](Min=0 Max=256) [gold1 on grey15] EXAMPLE [green_yellow] For Puzzle66 (Min=66 Max=67) [/]")
    x = int(input(" Input Puzzle Start Number (Min = 0)   : "))
    a = 2 ** x
    y = int(input(" Input Puzzle Stop Number  (Max = 256) : "))
    b = 2 ** y
    

    while True:
        main()