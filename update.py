import mysql.connector
import yfinance as yf
#update from list
li = [ 
#   '2S', '3K-BAT', '7UP', 'A', 'AAI', 'AAV', 'ACC', 'ACE', 'ACG', 'ADVANC', 
# 'AEONTS', 'AFC', 'AGE', 'AH', 'AHC', 'AI', 'AIE', 'AIMCG', 'AIMIRT', 'AIT',
# 'AJ', 'AJA', 'AKR', 'ALLA', 'ALLY', 'ALT', 'ALUCON', 'AMANAH', 'AMARIN', 'AMATA', 
# 'AMATAR', 'AMATAV', 'AMC', 'AMR', 'ANAN', 'AOT', 'AP', 'APCO', 'APCS', 'APEX', 
# 'APURE', 'AQ', 'AQUA', 'AS', 'ASAP', 'ASEFA', 'ASIA', 'ASIAN', 'ASIMAR', 'ASK',
# 'ASP', 'ASW', 'AURA', 'AWC', 'AYUD', 'B','b', 'B52', 'BA','BAFS',
# 'BAM', 'BANPU', 'BAREIT', 'BAY', 'BBGI', 'BBL', 'BCH', 'BCP', 'BCPG', 'BCT',
# 'BDMS', 'BEAUTY', 'BEC', 'BEM', 'BEYOND', 'BGC', 'BGRIM', 'BH', 'BIG', 'BIOTEC',
# 'BIZ','BJC', 'BJCHI', 'BKD', 'BKI', 'BKKCP', 'BLA', 'BLAND', 'bland', 'BOFFICE', 
# 'BPP', 'BR', 'BRI', 'BROCK', 'BRR', 'BRRGIF', 'BSBM', 'BTG', 'BTNC', 'BTS',
# 'BTSGIF', 'BUI', 'BWG', 'BYD', 'CBG', 'CCET', 'CCP', 'CEN', 'CENTEL', 'CFRESH',
# 'CGD', 'CGH', 'CH', 'CHARAN', 'CHAYO', 'CHG', 'CHOTI', 'CI', 'CIMBT', 'CITY',
# 'CIVIL', 'CK', 'CKP', 'CM', 'CMAN', 'CMC', 'CMR', 'CNT', 'COM7', 'COTTO',
# 'CPALL', 'CPF', 'CPH', 'CPI', 'CPL', 'CPN', 'CPNCG', 'CPNREIT', 'CPT', 'CPTGF',
# 'CPW', 'CRANE', 'CRC', 'CSC', 'CSP', 'CSR', 'CSS', 'CTARAF', 'CTW', 'CV',
# 'CWT', 'DCC', 'DCON', 'DDD', 'DELTA', 'DEMCO', 'DIF', 'DMT', 'DOHOME', 'DREIT',
# 'DRT', 'DTAC', 'DTCENT', 'DTCI', 'DUSIT', 'EA', 'EASON', 'EASTW', 'ECL', 'EE',
# 'EGATIF', 'EGCO', 'EKH', 'EMC', 'EP', 'EPG', 'ERW', 'ERWPF', 'ESSO', 'ESTAR',
# 'ETC', 'EVER', 'F&D', 'FANCY', 'FE', 'FMT', 'FN', 'FNS', 'FORTH', 'FPT',
# 'FSS', 'FTE', 'FTI', 'FTREIT', 'FUTUREPF', 'GAHREIT', 'GBX', 'GC', 'GEL', 'GENCO',
# 'GFPT', 'GGC', 'GIFT', 'GJS', 'GL', 'GLAND', 'GLOBAL', 'GLOCON', 'GPI', 'GPSC',
# 'GRAMMY', 'GRAND', 'GREEN', 'GROREIT', 'GSTEEL', 'GULF', 'GUNKUL', 'GVREIT', 'GYT', 'HANA',
# 'HENG', 'HFT', 'HMPRO', 'HPF', 'HTC', 'HTECH', 'HUMAN', 'HYDROGEN', 'ICC', 'ICHI',
# 'ichi', 'IFS', 'IHL', 'III', 'ILINK', 'ILM', 'IMPACT', 'INET', 'INETREIT', 'INGRS',
# 'INOX','INSET', 'INSURE', 'INTUCH', 'IRC', 'IRPC', 'IT', 'ITC', 'ITD', 'ITEL',
# 'IVL', 'J', 'JAS', 'JASIF', 'JCK', 'JCT', 'JDF', 'JKN', 'JMART', 'JMT',
# 'JR', 'JTS', 'JWD', 'KAMART', 'KBANK', 'KBS', 'KBSPIF', 'KC', 'KCAR', 'KCE',
# 'KDH', 'KEX', 'KGI', 'KIAT', 'KISS', 'KKC', 'KKP', 'KPNPF', 'KSL', 'KTB',
# 'KTBSTMR', 'KTC', 'KTIS', 'KWC', 'KWI', 'KYE', 'L&E', 'LALIN', 'LANNA', 'LEE',
# 'LH', 'LHFG', 'LHHOTEL', 'LHK', 'LHPF', 'LHSC', 'LOXLEY', 'LPF', 'LPH', 'LPN',
# 'LRH', 'LST', 'LUXF', 'M', 'M-CHAI', 'M-II', 'm-ii', 'M-STOR', 'MACO', 'MAJOR',
# 'MAKRO', 'MALEE', 'MANRIN', 'MATCH', 'MATI', 'MAX', 'MBK', 'MC', 'MCOT', 'MCS',
# 'MDX', 'MEGA', 'MENA', 'METCO', 'MFC', 'MFEC', 'MICRO', 'MIDA', 'MILL', 'MINT',
# 'MIPF', 'MIT', 'MJD', 'MJLF', 'MK', 'ML', 'MNIT', 'MNIT2', 'MNRF', 'MODERN',
# 'MONO', 'MOSHI', 'MPIC', 'MSC', 'MST', 'MTC', 'MTI', 'NATION', 'NC', 'NCAP',
# 'NCH', 'NEP', 'NER', 'NEW', 'NEX', 'NFC', 'NKI', 'NNCL', 'NOBLE', 'NOK',
# 'NOVA', 'NRF', 'NSI', 'NSL', 'NTV', 'NUSA', 'NV', 'NVD', 'NWR', 'NYT',
# 'OCC', 'OGC', 'OHTL', 'OISHI', 'ONEE', 'OR', 'ORI', 'OSP', 'PACE', 'PAF',
# 'PAP', 'PATO', 'PB', 'PCC', 'PCSGH', 'PDJ', 'PEACE', 'PERM', 'PF', 'PG',
# 'PIN', 'PK', 'PL', 'PLANB', 'PLAT', 'PLE', 'PLUS', 'PM', 'PMTA', 'POLAR',
# 'POLY', 'POPF', 'PORT', 'POST', 'PPF', 'PPP', 'PPPM', 'PR9', 'PRAKIT', 'PREB',
# 'PRECHA', 'PRG', 'PRIME', 'PRIN', 'PRINC', 'PRM', 'prm', 'PROSPECT', 'PSH', 'PSL',
# 'PT', 'PTECH', 'PTG', 'PTL', 'PTT', 'PTTEP', 'PTTGC', 'PYLON', 'Q-CON', 'QH',
# 'QHHR', 'QHOP', 'QHPF', 'QTC', 'RABBIT', 'RAM', 'RATCH', 'RBF', 'RCL', 'RICHY',
# 'RJH', 'RML', 'ROCK', 'ROH', 'ROJNA', 'RPC', 'RPH', 'RS', 'RSP', 'RT', 
# 'S', 'S&J', 'S11', 'SA', 'SABINA', 'SABUY', 'SAK', 'SAM', 'SAMART', 'SAMCO',
# 'SAMTEL', 'SAPPE', 'SAT', 'SAUCE', 'SAWAD', 'SAWANG', 'SC', 'SCAP', 'SCB', 'SCC',
# 'SCCC', 'SCG', 'SCGP', 'SCI', 'SCM', 'SCN', 'SCP', 'SDC', 'SE-ED', 'SEAFCO',
# 'SENA', 'SFLEX', 'SFP', 'SGC', 'SGP', 'SHANG', 'SHR', 'SHREIT', 'SIAM', 'SINGER',
# 'SIRI', 'SIRIP', 'SIS', 'SISB', 'SITHAI', 'SKE', 'SKN', 'SKR', 'SKY', 'SLP',
# 'SM', 'SMIT', 'SMK', 'SMPC', 'SMT', 'SNC', 'SNNP', 'SNP', 'SO', 'SOLAR',
# 'SORKON', 'SPACK', 'SPALI', 'SPC', 'SPCG', 'SPG', 'SPI', 'SPRC', 'SPRIME', 'SQ',
# 'SRICHA', 'SRIPANWA', 'SSC', 'SSF', 'SSP', 'SSPF', 'SSSC', 'SST', 'SSTRT', 'STA',
# 'STANLY', 'STARK', 'STEC', 'STECH', 'STGT', 'STHAI', 'STI', 'STPI', 'SUC', 'SUN',
# 'SUPER', 'SUPEREIF', 'SUSCO', 'SUTHA', 'SVI', 'SVOA', 'SVT', 'SYMC', 'SYNEX', 'SYNTEC',
'TAE', 'TASCO', 'TC', 'TCAP', 'TCC', 'TCCC', 'TCJ', 'TCMC', 'TCOAT', 'TEAM',
'TEAMG', 'TEGH', 'TEKA', 'TFFIF', 'TFG', 'TFI', 'TFM', 'TFMAMA', 'TGE', 'TGH',
'TGPRO', 'TH', 'th', 'THANI', 'THCOM', 'THE', 'THG', 'THIP', 'thip', 'THRE',
'THREL', 'TIDLOR', 'TIF1', 'TIPCO', 'TIPH', 'TISCO', 'TK', 'TKC', 'TKN', 'TKS',
'TKT', 'TLHPF', 'TLI', 'TMD', 'TMT', 'TNITY', 'TNL', 'TNPC', 'TNPF', 'TNR',
'TOA', 'TOG', 'TOP', 'TOPP', 'TPA', 'TPAC', 'TPBI', 'TPAC', 'TPIPL', 'TPIPP', 
'TPOLY', 'TPP', 'TPRIME', 'TQM', 'TR', 'TRC', 'TRITN', 'TRU', 'TRUBB', 'TRUE',
'TSC', 'TSE', 'TSI', 'TSR', 'TSTE', 'TSTH', 'TTA', 'TTB', 'TTCL', 'TTI',
'TTLPF', 'TTT', 'TTW', 'TU', 'tu', 'TVI', 'TVO', 'TWP', 'TWPC', 'TWZ',
'TYCN', 'UAC', 'UBE', 'UMI', 'UNIQ', 'UOBKH', 'UP', 'UPF', 'UPOIC', 'URBNPF',
'UTP', 'UV', 'UVAN', 'VARO', 'VGI', 'VIBHA', 'VIH', 'VNG', 'VPO', 'VRANDA',
'W', 'WACOAL', 'WAVE', 'WFX', 'WGE', 'WHA', 'WHABT', 'WHAIR', 'WHART', 'WHAUP',
'WICE', 'WIIK', 'WIN', 'WORK', 'WP', 'WPH', 'XPG', 'ZEN' ]

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
)
def newList(li):
  return [i+'.BK' for i in li]
data_li = newList(li)

mycursor = mydb.cursor()

for i in data_li:
    dhr = yf.Ticker(i)
    info = dhr.info
    index = data_li.index(i)
    print(i)
    sql = "UPDATE sp01.stock SET sector= %s, industry= %s, symbol= %s WHERE stock_id = %s"
    val = [(info.get('sector'), info.get('industry'), i, index+551
    #index+1
    )]

    mycursor.executemany(sql, val)
    mydb.commit()

print(mycursor.rowcount, "was inserted.")


#in li second index 57 'B' = B-WORK, 56 = B (b) 
#B-work, bkd, bliss, brrgif
#index 89 bliss.bk = bland
#index 231 ichi = IFEC 
#index 307 M-PAT  => m-ii
#417 pro -> prm
#579 THL -> thip
#573 THAI -> th
#635 TU-PF ->tu