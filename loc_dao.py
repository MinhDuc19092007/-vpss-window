import os
import threading
import time
import random
import sys
from datetime import datetime
import requests
from colorama import Fore, Style

#Màu
red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
dark_green = Fore.GREEN + Style.BRIGHT
pink = Fore.MAGENTA
green = Fore.GREEN
reset = Style.RESET_ALL
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'

output_lock = threading.Lock()
#banner
def banner():
    ban = """[38;2;252;8;8m█[38;2;252;12;12m█[38;2;252;16;16m█[38;2;252;20;20m█[38;2;252;24;24m█[38;2;252;28;28m█[38;2;252;32;32m█[38;2;252;36;36m█[38;2;252;40;40m╗[38;2;252;44;44m█[38;2;252;48;48m█[38;2;252;52;52m╗[38;2;252;56;56m [38;2;252;60;60m [38;2;252;64;64m [38;2;252;68;68m█[38;2;252;72;72m█[38;2;252;76;76m╗[38;2;252;80;80m [38;2;252;84;84m [38;2;252;88;88m [38;2;252;92;92m█[38;2;252;96;96m█[38;2;252;100;100m█[38;2;252;104;104m█[38;2;252;108;108m█[38;2;252;112;112m█[38;2;252;116;116m█[38;2;252;120;120m█[38;2;252;124;124m╗[38;2;252;128;128m [38;2;252;132;132m█[38;2;252;136;136m█[38;2;252;140;140m█[38;2;252;144;144m█[38;2;252;148;148m█[38;2;252;152;152m█[38;2;252;156;156m╗[38;2;252;160;160m [38;2;252;164;164m [38;2;252;168;168m█[38;2;252;172;172m█[38;2;252;176;176m█[38;2;252;180;180m█[38;2;252;184;184m█[38;2;252;188;188m█[38;2;252;192;192m╗[38;2;252;196;196m [38;2;252;200;200m█[38;2;252;204;204m█[38;2;252;208;208m╗[38;2;252;212;212m [38;2;252;216;216m [38;2;252;220;220m [38;2;252;224;224m [38;2;252;228;228m 
[38;2;252;8;8m╚[38;2;252;12;12m═[38;2;252;16;16m═[38;2;252;20;20m█[38;2;252;24;24m█[38;2;252;28;28m╔[38;2;252;32;32m═[38;2;252;36;36m═[38;2;252;40;40m╝[38;2;252;44;44m█[38;2;252;48;48m█[38;2;252;52;52m║[38;2;252;56;56m [38;2;252;60;60m [38;2;252;64;64m [38;2;252;68;68m█[38;2;252;72;72m█[38;2;252;76;76m║[38;2;252;80;80m [38;2;252;84;84m [38;2;252;88;88m [38;2;252;92;92m╚[38;2;252;96;96m═[38;2;252;100;100m═[38;2;252;104;104m█[38;2;252;108;108m█[38;2;252;112;112m╔[38;2;252;116;116m═[38;2;252;120;120m═[38;2;252;124;124m╝[38;2;252;128;128m█[38;2;252;132;132m█[38;2;252;136;136m╔[38;2;252;140;140m═[38;2;252;144;144m═[38;2;252;148;148m═[38;2;252;152;152m█[38;2;252;156;156m█[38;2;252;160;160m╗[38;2;252;164;164m█[38;2;252;168;168m█[38;2;252;172;172m╔[38;2;252;176;176m═[38;2;252;180;180m═[38;2;252;184;184m═[38;2;252;188;188m█[38;2;252;192;192m█[38;2;252;196;196m╗[38;2;252;200;200m█[38;2;252;204;204m█[38;2;252;208;208m║[38;2;252;212;212m [38;2;252;216;216m [38;2;252;220;220m [38;2;252;224;224m [38;2;252;228;228m 
[38;2;252;8;8m [38;2;252;12;12m [38;2;252;16;16m [38;2;252;20;20m█[38;2;252;24;24m█[38;2;252;28;28m║[38;2;252;32;32m [38;2;252;36;36m [38;2;252;40;40m [38;2;252;44;44m█[38;2;252;48;48m█[38;2;252;52;52m║[38;2;252;56;56m [38;2;252;60;60m [38;2;252;64;64m [38;2;252;68;68m█[38;2;252;72;72m█[38;2;252;76;76m║[38;2;252;80;80m█[38;2;252;84;84m█[38;2;252;88;88m█[38;2;252;92;92m█[38;2;252;96;96m█[38;2;252;100;100m╗[38;2;252;104;104m█[38;2;252;108;108m█[38;2;252;112;112m║[38;2;252;116;116m [38;2;252;120;120m [38;2;252;124;124m [38;2;252;128;128m█[38;2;252;132;132m█[38;2;252;136;136m║[38;2;252;140;140m [38;2;252;144;144m [38;2;252;148;148m [38;2;252;152;152m█[38;2;252;156;156m█[38;2;252;160;160m║[38;2;252;164;164m█[38;2;252;168;168m█[38;2;252;172;172m║[38;2;252;176;176m [38;2;252;180;180m [38;2;252;184;184m [38;2;252;188;188m█[38;2;252;192;192m█[38;2;252;196;196m║[38;2;252;200;200m█[38;2;252;204;204m█[38;2;252;208;208m║[38;2;252;212;212m [38;2;252;216;216m [38;2;252;220;220m [38;2;252;224;224m [38;2;252;228;228m 
[38;2;252;8;8m [38;2;252;12;12m [38;2;252;16;16m [38;2;252;20;20m█[38;2;252;24;24m█[38;2;252;28;28m║[38;2;252;32;32m [38;2;252;36;36m [38;2;252;40;40m [38;2;252;44;44m█[38;2;252;48;48m█[38;2;252;52;52m║[38;2;252;56;56m [38;2;252;60;60m [38;2;252;64;64m [38;2;252;68;68m█[38;2;252;72;72m█[38;2;252;76;76m║[38;2;252;80;80m╚[38;2;252;84;84m═[38;2;252;88;88m═[38;2;252;92;92m═[38;2;252;96;96m═[38;2;252;100;100m╝[38;2;252;104;104m█[38;2;252;108;108m█[38;2;252;112;112m║[38;2;252;116;116m [38;2;252;120;120m [38;2;252;124;124m [38;2;252;128;128m█[38;2;252;132;132m█[38;2;252;136;136m║[38;2;252;140;140m [38;2;252;144;144m [38;2;252;148;148m [38;2;252;152;152m█[38;2;252;156;156m█[38;2;252;160;160m║[38;2;252;164;164m█[38;2;252;168;168m█[38;2;252;172;172m║[38;2;252;176;176m [38;2;252;180;180m [38;2;252;184;184m [38;2;252;188;188m█[38;2;252;192;192m█[38;2;252;196;196m║[38;2;252;200;200m█[38;2;252;204;204m█[38;2;252;208;208m║[38;2;252;212;212m [38;2;252;216;216m [38;2;252;220;220m [38;2;252;224;224m [38;2;252;228;228m 
[38;2;252;8;8m [38;2;252;12;12m [38;2;252;16;16m [38;2;252;20;20m█[38;2;252;24;24m█[38;2;252;28;28m║[38;2;252;32;32m [38;2;252;36;36m [38;2;252;40;40m [38;2;252;44;44m╚[38;2;252;48;48m█[38;2;252;52;52m█[38;2;252;56;56m█[38;2;252;60;60m█[38;2;252;64;64m█[38;2;252;68;68m█[38;2;252;72;72m╔[38;2;252;76;76m╝[38;2;252;80;80m [38;2;252;84;84m [38;2;252;88;88m [38;2;252;92;92m [38;2;252;96;96m [38;2;252;100;100m [38;2;252;104;104m█[38;2;252;108;108m█[38;2;252;112;112m║[38;2;252;116;116m [38;2;252;120;120m [38;2;252;124;124m [38;2;252;128;128m╚[38;2;252;132;132m█[38;2;252;136;136m█[38;2;252;140;140m█[38;2;252;144;144m█[38;2;252;148;148m█[38;2;252;152;152m█[38;2;252;156;156m╔[38;2;252;160;160m╝[38;2;252;164;164m╚[38;2;252;168;168m█[38;2;252;172;172m█[38;2;252;176;176m█[38;2;252;180;180m█[38;2;252;184;184m█[38;2;252;188;188m█[38;2;252;192;192m╔[38;2;252;196;196m╝[38;2;252;200;200m█[38;2;252;204;204m█[38;2;252;208;208m█[38;2;252;212;212m█[38;2;252;216;216m█[38;2;252;220;220m█[38;2;252;224;224m█[38;2;252;228;228m╗
[38;2;252;8;8m [38;2;252;12;12m [38;2;252;16;16m [38;2;252;20;20m╚[38;2;252;24;24m═[38;2;252;28;28m╝[38;2;252;32;32m [38;2;252;36;36m [38;2;252;40;40m [38;2;252;44;44m [38;2;252;48;48m╚[38;2;252;52;52m═[38;2;252;56;56m═[38;2;252;60;60m═[38;2;252;64;64m═[38;2;252;68;68m═[38;2;252;72;72m╝[38;2;252;76;76m [38;2;252;80;80m [38;2;252;84;84m [38;2;252;88;88m [38;2;252;92;92m [38;2;252;96;96m [38;2;252;100;100m [38;2;252;104;104m╚[38;2;252;108;108m═[38;2;252;112;112m╝[38;2;252;116;116m [38;2;252;120;120m [38;2;252;124;124m [38;2;252;128;128m [38;2;252;132;132m╚[38;2;252;136;136m═[38;2;252;140;140m═[38;2;252;144;144m═[38;2;252;148;148m═[38;2;252;152;152m═[38;2;252;156;156m╝[38;2;252;160;160m [38;2;252;164;164m [38;2;252;168;168m╚[38;2;252;172;172m═[38;2;252;176;176m═[38;2;252;180;180m═[38;2;252;184;184m═[38;2;252;188;188m═[38;2;252;192;192m╝[38;2;252;196;196m [38;2;252;200;200m╚[38;2;252;204;204m═[38;2;252;208;208m═[38;2;252;212;212m═[38;2;252;216;216m═[38;2;252;220;220m═[38;2;252;224;224m═[38;2;252;228;228m╝
[38;2;252;8;8m=[38;2;252;13;13m=[38;2;252;18;18m=[38;2;252;23;23m=[38;2;252;28;28m=[38;2;252;33;33m=[38;2;252;38;38m=[38;2;252;43;43m=[38;2;252;48;48m=[38;2;252;53;53m=[38;2;252;58;58m=[38;2;252;63;63m=[38;2;252;68;68m=[38;2;252;73;73m=[38;2;252;78;78m=[38;2;252;83;83m=[38;2;252;88;88m=[38;2;252;93;93m=[38;2;252;98;98m=[38;2;252;103;103m=[38;2;252;108;108m=[38;2;252;113;113m=[38;2;252;118;118m=[38;2;252;123;123m=[38;2;252;128;128m=[38;2;252;133;133m=[38;2;252;138;138m=[38;2;252;143;143m=[38;2;252;148;148m=[38;2;252;153;153m=[38;2;252;158;158m=[38;2;252;163;163m=[38;2;252;168;168m=[38;2;252;173;173m=[38;2;252;178;178m=[38;2;252;183;183m=[38;2;252;188;188m=[38;2;252;193;193m=[38;2;252;198;198m=[38;2;252;203;203m=[38;2;252;208;208m=[38;2;252;213;213m=[38;2;252;218;218m=[38;2;252;223;223m=
[38;2;252;8;8m_[38;2;252;12;12m_[38;2;252;16;16m_[38;2;252;20;20m_[38;2;252;24;24m_[38;2;252;28;28m_[38;2;252;32;32m_[38;2;252;36;36m_[38;2;252;40;40m_[38;2;252;44;44m_[38;2;252;48;48m_[38;2;252;52;52m_[38;2;252;56;56m_[38;2;252;60;60m_[38;2;252;64;64m_[38;2;252;68;68mT[38;2;252;72;72mo[38;2;252;76;76mo[38;2;252;80;80ml[38;2;252;84;84m [38;2;252;88;88mB[38;2;252;92;92my[38;2;252;96;96m [38;2;252;100;100mA[38;2;252;104;104mn[38;2;252;108;108mo[38;2;252;112;112mn[38;2;252;116;116m [38;2;252;120;120mx[38;2;252;124;124mS[38;2;252;128;128me[38;2;252;132;132mv[38;2;252;136;136me[38;2;252;140;140mn[38;2;252;144;144m_[38;2;252;148;148m_[38;2;252;152;152m_[38;2;252;156;156m_[38;2;252;160;160m_[38;2;252;164;164m_[38;2;252;168;168m_[38;2;252;172;172m_[38;2;252;176;176m_[38;2;252;180;180m_[38;2;252;184;184m_[38;2;252;188;188m_[38;2;252;192;192m_[38;2;252;196;196m_[38;2;252;200;200m_
[38;2;252;8;8mC[38;2;252;16;16mr[38;2;252;24;24me[38;2;252;32;32m [38;2;252;40;40m:[38;2;252;48;48m [38;2;252;56;56mN[38;2;252;64;64mg[38;2;252;72;72mu[38;2;252;80;80my[38;2;252;88;88mễ[38;2;252;96;96mn[38;2;252;104;104m [38;2;252;112;112mT[38;2;252;120;120mư[38;2;252;128;128m [38;2;252;136;136m([38;2;252;144;144ma[38;2;252;152;152mn[38;2;252;160;160mo[38;2;252;168;168mn[38;2;252;176;176m [38;2;252;184;184mx[38;2;252;192;192mS[38;2;252;200;200me[38;2;252;208;208mv[38;2;252;216;216me[38;2;252;224;224mn[38;2;252;232;232m)
[38;2;252;8;8mZ[38;2;252;21;21ma[38;2;252;34;34ml[38;2;252;47;47mo[38;2;252;60;60m [38;2;252;73;73m:[38;2;252;86;86m [38;2;252;99;99m0[38;2;252;112;112m3[38;2;252;125;125m7[38;2;252;138;138m9[38;2;252;151;151m0[38;2;252;164;164m8[38;2;252;177;177m8[38;2;252;190;190m1[38;2;252;203;203m4[38;2;252;216;216m9
[38;2;252;8;8mF[38;2;252;12;12ma[38;2;252;16;16mc[38;2;252;20;20me[38;2;252;24;24mb[38;2;252;28;28mo[38;2;252;32;32mo[38;2;252;36;36mk[38;2;252;40;40m [38;2;252;44;44m:[38;2;252;48;48m [38;2;252;52;52mh[38;2;252;56;56mt[38;2;252;60;60mt[38;2;252;64;64mp[38;2;252;68;68ms[38;2;252;72;72m:[38;2;252;76;76m/[38;2;252;80;80m/[38;2;252;84;84mw[38;2;252;88;88mw[38;2;252;92;92mw[38;2;252;96;96m.[38;2;252;100;100mf[38;2;252;104;104ma[38;2;252;108;108mc[38;2;252;112;112me[38;2;252;116;116mb[38;2;252;120;120mo[38;2;252;124;124mo[38;2;252;128;128mk[38;2;252;132;132m.[38;2;252;136;136mc[38;2;252;140;140mo[38;2;252;144;144mm[38;2;252;148;148m/[38;2;252;152;152mb[38;2;252;156;156me[38;2;252;160;160mt[38;2;252;164;164mu[38;2;252;168;168md[38;2;252;172;172mz[38;2;252;176;176m2[38;2;252;180;180m0[38;2;252;184;184m1[38;2;252;188;188m0[38;2;252;192;192m.[38;2;252;196;196ms[38;2;252;200;200me[38;2;252;204;204mv[38;2;252;208;208me[38;2;252;212;212mn
[38;2;252;8;8mY[38;2;252;11;11mo[38;2;252;14;14mu[38;2;252;17;17mT[38;2;252;20;20mu[38;2;252;23;23mb[38;2;252;26;26me[38;2;252;29;29m [38;2;252;32;32m:[38;2;252;35;35m [38;2;252;38;38mh[38;2;252;41;41mt[38;2;252;44;44mt[38;2;252;47;47mp[38;2;252;50;50ms[38;2;252;53;53m:[38;2;252;56;56m/[38;2;252;59;59m/[38;2;252;62;62my[38;2;252;65;65mo[38;2;252;68;68mu[38;2;252;71;71mt[38;2;252;74;74mu[38;2;252;77;77mb[38;2;252;80;80me[38;2;252;83;83m.[38;2;252;86;86mc[38;2;252;89;89mo[38;2;252;92;92mm[38;2;252;95;95m/[38;2;252;98;98m@[38;2;252;101;101mB[38;2;252;104;104me[38;2;252;107;107mT[38;2;252;110;110mu[38;2;252;113;113md[38;2;252;116;116mz[38;2;252;119;119m_[38;2;252;122;122m2[38;2;252;125;125m0[38;2;252;128;128m1[38;2;252;131;131m0[38;2;252;134;134m_[38;2;252;137;137m?[38;2;252;140;140ms[38;2;252;143;143mi[38;2;252;146;146m=[38;2;252;149;149mu[38;2;252;152;152mP[38;2;252;155;155mb[38;2;252;158;158mz[38;2;252;161;161mX[38;2;252;164;164mG[38;2;252;167;167mS[38;2;252;170;170mi[38;2;252;173;173mW[38;2;252;176;176mk[38;2;252;179;179mQ[38;2;252;182;182mK[38;2;252;185;185mF[38;2;252;188;188mf[38;2;252;191;191mA[38;2;252;194;194m2
[38;2;252;8;8m=[38;2;252;13;13m=[38;2;252;18;18m=[38;2;252;23;23m=[38;2;252;28;28m=[38;2;252;33;33m=[38;2;252;38;38m=[38;2;252;43;43m=[38;2;252;48;48m=[38;2;252;53;53m=[38;2;252;58;58m=[38;2;252;63;63m=[38;2;252;68;68m=[38;2;252;73;73m=[38;2;252;78;78m=[38;2;252;83;83m=[38;2;252;88;88m=[38;2;252;93;93m=[38;2;252;98;98m=[38;2;252;103;103m=[38;2;252;108;108m=[38;2;252;113;113m=[38;2;252;118;118m=[38;2;252;123;123m=[38;2;252;128;128m=[38;2;252;133;133m=[38;2;252;138;138m=[38;2;252;143;143m=[38;2;252;148;148m=[38;2;252;153;153m=[38;2;252;158;158m=[38;2;252;163;163m=[38;2;252;168;168m=[38;2;252;173;173m=[38;2;252;178;178m=[38;2;252;183;183m=[38;2;252;188;188m=[38;2;252;193;193m=[38;2;252;198;198m=[38;2;252;203;203m=[38;2;252;208;208m=[38;2;252;213;213m=[38;2;252;218;218m=[38;2;252;223;223m=
[38;2;252;8;8mN[38;2;252;17;17mh[38;2;252;26;26mậ[38;2;252;35;35mp[38;2;252;44;44m [38;2;252;53;53ms[38;2;252;62;62mố[38;2;252;71;71m [38;2;252;80;80m[[38;2;252;89;89m1[38;2;252;98;98m][38;2;252;107;107m [38;2;252;116;116mđ[38;2;252;125;125mể[38;2;252;134;134m [38;2;252;143;143ml[38;2;252;152;152mọ[38;2;252;161;161mc[38;2;252;170;170m [38;2;252;179;179mp[38;2;252;188;188mr[38;2;252;197;197mo[38;2;252;206;206mx[38;2;252;215;215my
[38;2;252;8;8mN[38;2;252;17;17mh[38;2;252;26;26mậ[38;2;252;35;35mp[38;2;252;44;44m [38;2;252;53;53ms[38;2;252;62;62mố[38;2;252;71;71m [38;2;252;80;80m[[38;2;252;89;89m2[38;2;252;98;98m][38;2;252;107;107m [38;2;252;116;116mđ[38;2;252;125;125mể[38;2;252;134;134m [38;2;252;143;143mđ[38;2;252;152;152mà[38;2;252;161;161mo[38;2;252;170;170m [38;2;252;179;179mp[38;2;252;188;188mr[38;2;252;197;197mo[38;2;252;206;206mx[38;2;252;215;215my[38;2;252;224;224m 
[38;2;252;8;8m=[38;2;252;13;13m=[38;2;252;18;18m=[38;2;252;23;23m=[38;2;252;28;28m=[38;2;252;33;33m=[38;2;252;38;38m=[38;2;252;43;43m=[38;2;252;48;48m=[38;2;252;53;53m=[38;2;252;58;58m=[38;2;252;63;63m=[38;2;252;68;68m=[38;2;252;73;73m=[38;2;252;78;78m=[38;2;252;83;83m=[38;2;252;88;88m=[38;2;252;93;93m=[38;2;252;98;98m=[38;2;252;103;103m=[38;2;252;108;108m=[38;2;252;113;113m=[38;2;252;118;118m=[38;2;252;123;123m=[38;2;252;128;128m=[38;2;252;133;133m=[38;2;252;138;138m=[38;2;252;143;143m=[38;2;252;148;148m=[38;2;252;153;153m=[38;2;252;158;158m=[38;2;252;163;163m=[38;2;252;168;168m=[38;2;252;173;173m=[38;2;252;178;178m=[38;2;252;183;183m=[38;2;252;188;188m=[38;2;252;193;193m=[38;2;252;198;198m=[38;2;252;203;203m=[38;2;252;208;208m=[38;2;252;213;213m=[38;2;252;218;218m=[38;2;252;223;223m=
[38;2;252;8;8m [38;2;252;12;12m [38;2;252;16;16m [38;2;252;20;20m [38;2;252;24;24m [38;2;252;28;28m [38;2;252;32;32m [38;2;252;36;36m [38;2;252;40;40m [38;2;252;44;44m [38;2;252;48;48m [38;2;252;52;52m [38;2;252;56;56m [38;2;252;60;60m [38;2;252;64;64m [38;2;252;68;68m [38;2;252;72;72m [38;2;252;76;76m [38;2;252;80;80m [38;2;252;84;84m [38;2;252;88;88m [38;2;252;92;92m [38;2;252;96;96m [38;2;252;100;100m [38;2;252;104;104m [38;2;252;108;108m [38;2;252;112;112m [38;2;252;116;116m [38;2;252;120;120m [38;2;252;124;124m [38;2;252;128;128m [38;2;252;132;132m [38;2;252;136;136m [38;2;252;140;140m [38;2;252;144;144m [38;2;252;148;148m [38;2;252;152;152m [38;2;252;156;156m [38;2;252;160;160m [38;2;252;164;164m [38;2;252;168;168m [38;2;252;172;172m [38;2;252;176;176m [38;2;252;180;180m [38;2;252;184;184m [38;2;252;188;188m [38;2;252;192;192m [38;2;252;196;196m [38;2;252;200;200m [38;2;252;204;204m [38;2;252;208;208m [38;2;252;212;212m [38;2;252;216;216m [38;2;252;220;220m [38;2;252;224;224m [38;2;252;228;228m 
[0;00m"""
    for X in ban:
        sys.stdout.write(X)
        sys.stdout.flush()
        time.sleep(0.00)
    

#________
def get_time_rn():
    date = datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

def clear():
    os.system("cls" if os.name == "nt" else "clear")

class ProxyInfo:
    def __init__(self, proxy):
        self.proxy = proxy
        self.location = None
        self.type = None
        self.response_time = None

    def determine_location(self):
        try:
            response = requests.get('https://ipinfo.io/json', proxies={"http": self.proxy, "https": self.proxy}, timeout=5)
            self.location = response.json().get("country", "NO")
            return True
        except:
            self.location = "NO"
            return False

    def determine_type(self):
        types = ["http", "https"]
        for t in types:
            try:
                response = requests.get("http://judge1.api.proxyscrape.com/", proxies={t: self.proxy}, timeout=5)
                if response.status_code == 200:
                    self.type = t.upper()
                    return
            except:
                pass
        self.type = "NO"

    def measure_response_time(self):
        try:
            response = requests.get("http://judge1.api.proxyscrape.com/", proxies={"http": self.proxy, "https": self.proxy}, timeout=5)
            self.response_time = response.elapsed.total_seconds()
        except:
            self.response_time = float('inf')

    def get_info(self):
        is_live = self.determine_location()
        if is_live:
            self.determine_type()
            self.measure_response_time()
        return is_live

def check_live_proxies(filename, num_threads):
    live_proxies = {"HTTP": [], "HTTPS": [], "NO": []}
    printed_count = 0

    def check_proxy_thread(proxy):
        nonlocal printed_count
        proxy_info = ProxyInfo(proxy)
        if proxy_info.get_info(): 
            live_proxies[proxy_info.type].append(proxy_info.proxy)
            printed_count += 1
            total = printed_count
            time_rn = get_time_rn()
            print(f"\x1b[38;5;255m[ \x1b[38;5;160mCountry : \x1b[38;5;255m{proxy_info.location}{reset} \x1b[38;5;255m] \x1b[38;5;160m| \x1b[38;5;255m(\x1b[38;5;160mTotal : \x1b[38;5;255m{total}{reset}) \x1b[38;5;255m{pretty}\x1b[38;5;160mProxy --> \x1b[38;5;255m{proxy}{Fore.RESET}")
    
    with open(filename, "r") as file:
        proxies = file.readlines()

    threads = []
    for proxy in proxies:
        proxy = proxy.strip()
        thread = threading.Thread(target=check_proxy_thread, args=(proxy,))
        thread.start()
        threads.append(thread)
        if len(threads) >= num_threads:
            for thread in threads:
                thread.join()
    
    return live_proxies

if __name__ == "__main__":
    try:
        time.sleep(1.5)
        clear()
        banner() 
        choice = input("\x1b[38;5;160mChọn chế độ của bạn \x1b[38;5;255m(1/2): \033[1;33m")
        #lọc proxy 
        if choice == "1":
            print("\x1b[38;5;255mANON XSEVEN \x1b[38;5;160m| \x1b[38;5;255mNhập tên file chứa proxy !!! \x1b[38;5;160m| \x1b[38;5;255mVí dụ : proxies.txt")
            filename = input("\x1b[38;5;160m>>> \x1b[38;5;255m")
            print("\x1b[38;5;255mNhập số luồng !!! \x1b[38;5;160m| \x1b[38;5;255mVí dụ : 22222")
            num_threads = int(input("\x1b[38;5;160m>>> \x1b[38;5;255m"))
            check_proxy = check_live_proxies(filename, num_threads)            
            with open("check_live_proxies.txt", "w") as file:
                for proxy_type, proxies in check_proxy.items():
                    for proxy in proxies:
                        file.write(f"{proxy_type}: {proxy}\n")
            print("\033[1;31mCác proxy đã được lọc và lưu vào tệp \033[1;37mcheck_live_proxies.txt.")
            exit()
        #Đào proxy   
        elif choice == "2":
            raw_proxy_sites = ["https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
                   "https://api.openproxylist.xyz/http.txt",
                   "http://alexa.lr2b.com/proxylist.txt",
                   "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                   "http://worm.rip/http.txt",
                   "https://proxy-spider.com/api/proxies.example.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://proxyspace.pro/http.txt",
                   "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
                   "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
                   "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
                   "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
                   "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
                   "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
                   "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
                   "https://openproxylist.xyz/http.txt",
                   "https://dodanhtai.site/proxy/http.txt",
                   "http://worm.rip/http.txt",
                   "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
                   "http://rootjazz.com/proxies/proxies.txt",
                   "https://api.proxyscrape.com/?request=displayproxies&proxytype=https",
                   "https://www.proxy-list.download/api/v1/get?type=http",
                   "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
                   "https://api.openproxylist.xyz/http.tx",
                   "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
                   "http://alexa.lr2b.com/proxylist.txt",
                   "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
                   "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
                   "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
                   "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
                   "https://proxy-spider.com/api/proxies.example.txt",
                   "https://multiproxy.org/txt_all/proxy.txt",
                   "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
                   "https://proxyspace.pro/http.txt",
                   "https://proxyspace.pro/https.txt",
                   "https://proxyspace.pro/https.txt",
                   "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
                   "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
                   "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
                   "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
                   "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
                   "https://rootjazz.com/proxies/proxies.txt",
                   "https://www.proxy-list.download/api/v1/get?type=https",
                   "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
                   "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt",
                   "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
                   "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
                   "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
                   "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",
                   "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
                   "https://sunny9577.github.io/proxy-scraper/proxies.txt",
                   "https://api.getproxylist.com/proxy?protocol[]=http&anonymity[]=high&allowsHttps=true&allowsPost=true&maxConnectTime=1&maxSecondsToFirstByte=1",]
            proxies = set()
            for site in raw_proxy_sites:
                try:
                    response = requests.get(site)
                    response.raise_for_status()  
                    for line in response.text.split("\n"):
                        if ":" in line:
                            proxies.add(line.strip())
                except Exception as e:
                    print(f"\x1b[38;5;160mĐã xảy ra lỗi khi lấy proxy từ \x1b[38;5;255m{site}: \033[0;31m{e}")
            with open("proxies.txt", "w") as file:
                for proxy in proxies:
                    file.write(proxy + "\n")
            print("\x1b[38;5;160mCác proxy đã được đào và lưu vào tệp \033[1;37mproxies.txt.")
        else:
            print("\x1b[38;5;160mLựa chọn không hợp lệ. Vui lòng chọn \033[1;33m1 \x1b[38;5;160mhoặc \033[1;33m2.")           
    except KeyboardInterrupt:
        time.sleep(1)
        exit()