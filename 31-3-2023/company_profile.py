from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'tester'

mysql = MySQL(app)

company_profiles = {
    # 1-20
    '2S.BK': {
        'name': '2S Metal Public Company Limited',
        'address': 'No. 8/5 Moo 14, Tha-chang Bang Klam 90110 Thailand',
        'phone': '66 7 480 0111',
        'website': 'https://www.ss.co.th',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': '2S Metal Public Company Limited, together with its subsidiaries, engages in the production and distribution of steel products in Thailand. It operates through two segments, Production and Trading. The company offers galvanized steel pipes, equal angles, H-beams, I-beams, channel steel, gutters, bars, checkered plates, hot rolled coils, deformed bars, cold round bars, C- and U-channels, light lip channels, cut and bend rebars, galvanized steel battens, annealing wires, and chain link and crimped wire meshes, as well as flat bars, metal framework products, and C-line products. It also trades in steel products; and provides transportation services. The company was formerly known as Southern Steel Public Company Limited and changed its name to 2S Metal Public Company Limited in April 2010. 2S Metal Public Company Limited was founded in 1992 and is headquartered in Bang Klam, Thailand.'
    },
    '3K-BAT.BK': {
        'name': 'Thai Energy Storage Technology Public Company Limited',
        'address': '387, Moo 4, Sukhumvit Road Phraek Sa Sub-district Mueang Samut Prakan 10280 Thailand',
        'phone': '66 2 709 3535',
        'website': 'https://www.3kbattery.com',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'Thai Energy Storage Technology Public Company Limited manufactures and distributes batteries in Thailand and internationally. It provides automotive, motorcycle, traction, EB, forklift, lighting, and golf cart batteries. The company was founded in 1986 and is based in Mueang Samut Prakan, Thailand. Thai Energy Storage Technology Public Company Limited is a subsidiary of Sustainable Battery Solutions, Inc.'
    },
    '7UP.BK': {
        'name': 'Seven Utilities and Power Public Company Limited',
        'address': '73 Mahachol Building Soi Sukhumvit 62 Sukhumvit Road Prakhanong Tai, Prakhanong Bangkok 10260 Thailand',
        'phone': '66 2 741 5700',
        'website': 'https://www.sevenup.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Specialty Retail',
        'description': 'Seven Utilities and Power Public Company Limited, together with its subsidiaries, operates as a renewable energy and public utility company in Thailand. It operates LPG stations and water treatment solutions; transports LPG; manages NGV gas stations; and produces and distributes biogas electricity. The company is also involved in the design, construction, installation, operation, and management of water resources and environmental engineering business; and provision of hazardous and non- hazardous industrial waste treatment services. The company was formerly known as Ferrum Public Company Limited and changed its name to Seven Utilities and Power Public Company Limited in April 2018. Seven Utilities and Power Public Company Limited was incorporated in 1995 and is headquartered in Bangkok, Thailand.'
    },
    'A.BK': {
        'name': 'Areeya Property Public Company Limited',
        'address': '999 Praditmanutham Road Saphansong Wangthonglang Bangkok 10310 Thailand',
        'phone': '66 2 798 9999',
        'website': 'https://www.areeya.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Areeya Property Public Company Limited, together with its subsidiaries, develops real estate projects in Thailand. It primarily develops single detached houses, twinhome, village towns, townhomes, home offices, and condominiums; and community malls. The company is also involved in the provision of after sales services for property; construction services; and property management services, as well as in the restaurant and hotels business. Areeya Property Public Company Limited was founded in 2000 and is headquartered in Bangkok, Thailand.'
    },
    'AAI.BK': {
        'name': 'Asian Alliance International Public Company Limited',
        'address': '55/2 Moo 2, Rama 2 Road Bang Krachao Subdistrict Mueang District Mueang Samut Sakhon 74000Thailand',
        'phone': '66 3 484 5575-87',
        'website': 'https://www.asianalliance.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Asian Alliance International Public Company Limited manufactures and sells pet food and ready-to-eat human food products in Thailand. It offers wet pet food products, such as soups, salads, fish and meat dishes, mousse, and pate, as well as dry pet food products for dogs and cats under the monchou, monchou balanced, Hajiko, and PRO brand names ; and ready-to-eat human food products made of tuna, salmon, tilapia, sea bass, mackerel, and shrimp in sealed containers. The company was founded in 2005 and is based in Mueang Samut Sakhon, Thailand.'
    },
    'AAV.BK': {
        'name': 'Asia Aviation Public Company Limited',
        'address': 'Central Office Building Room No. 3200, 3rd Floor No.222, Don Mueang International Airport Vibhavadee Rangsit Road, Don Mueang Bangkok 10210 Thailand',
        'phone': '66 2 562 5700',
        'website': 'https://www.aavplc.com',
        'sector': 'Industrials',
        'industry': 'Airlines',
        'description': 'Asia Aviation Public Company Limited provides airline services in Thailand. The company operates through Scheduled Flight Operations and Charter Flight Operations segments. The Scheduled Flight Operations segment offers passenger air transportation services to routine destinations for scheduled flights. This segment sells tickets through its distribution channels, including website, sale counters, travel agents, etc. The Chartered Flight Operations segment provides passenger air transportation services to non-routine destinations that serves tourist agency companies. It also operates an academy institution of learning and competency development for aviation tourism and hospitality industries. Asia Aviation Public Company Limited was founded in 2004 and is headquartered in Bangkok, Thailand.'
    },
    'ACC.BK': {
        'name': 'Advanced Connection Corporation Public Company Limited',
        'address': '944 Mitrtown Office Tower 16th Floor Rama 4 Road, Wangmai Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 219 1642',
        'website': 'https://acc-plc.com',
        'sector': 'Industrials',
        'industry': 'Conglomerates',
        'description': 'Advanced Connection Corporation Public Company Limited, together with its subsidiaries, operates in the infrastructure, financial, and cannabis businesses primarily in Thailand. It operates solar rooftop and farm projects. The company also operates in the banquet and restaurant, and property development businesses; and property rental. In addition, it provides consignment and non-performing loan services; financing and factoring; and construction contracting services. Further, the company is involved in the trading business; research, development, production, cultivation, processing, import, distribution, and export of cannabis; and development of an e-commerce system for online marketing. Additionally, it is engaged in manufacturing and distribution of ceiling fan; and production and distribution of electricity from solar power. The company was formerly known as Compass East Industry (Thailand) Public Company Limited and changed its name to Advanced Connection Corporation Public Company Limited in November 2015. Advanced Connection Corporation Public Company Limited was incorporated in 1987 and is headquartered in Bangkok, Thailand.'
    },
    'ACE.BK': {
        'name': 'Absolute Clean Energy Public Company Limited',
        'address': '140/6 ITF Tower 7th Floor Silom Road Suriyawong, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 233 2559',
        'website': 'https://www.ace-energy.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Absolute Clean Energy Public Company Limited, together with its subsidiaries, operates biomass, municipal solid waste, natural gas, and solar energy power plants in Thailand. The company operates through four segments: Biomass Power Plants, Solid Waste Power Plant, Natural Gas Power Plant, and Solar Energy Power Plant. As of December 31, 2021, it has 23 power plants with an installed capacity of 257.57 megawatts. Absolute Clean Energy Public Company Limited was incorporated in 2015 and is headquartered in Bangkok, Thailand.'
    },
    'ACG.BK': {
        'name': 'Autocorp Holding Public Company Limited',
        'address': '1111, Moo 1, Maliwan Road Ban Thum Mueang Khon Kaen Khon Kaen 40000 Thailand',
        'phone': '66 4 330 6333',
        'website': 'https://www.ach.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Auto & Truck Dealerships',
        'description': 'Autocorp Holding Public Company Limited, a investment holding company, operates in distribution of cars and spare parts, and services center dealership in Thailand. It operates through Cars and accessories dealership, and Repair and maintenance service and spare parts dealership segments. The company also engages in manufacturing and distribution of Honda cars including selecting a dealer, setting price policies, and organize promotional programs, as well as supply orders from dealers. In addition, it offers oil changes, tires, maintenance of brake systems, batteries, shock absorbers, suspensions, and air conditioning systems, as well as suggestion for car insurance services. The company was founded in 2015 and is headquartered in Khon Kaen, Thailand.'
    },
    'ADVANC.BK': {
        'name': 'Advanced Info Service Public Company Limited',
        'address': '414 AIS Tower 1 Phaholyothin Road Samsen Nai Phayathai Bangkok 10400 Thailand',
        'phone': '66 2 029 5000',
        'website': 'https://www.ais.th',
        'sector': 'Communication Services',
        'industry': 'Telecom Services',
        'description': 'Advanced Info Service Public Company Limited, together its subsidiaries, provides mobile network, fixed broadband, and digital services primarily in Thailand. The company operates through three segments: Mobile Phone Services, Mobile Phone and Equipment Sales, and Datanet and Broadband Services. It is involved in the operation of cellular telephone networks. The company also distributes handsets, as well as cash cards; and electronic money and electronic payment services. In addition, it provides international telephone service, broadcasting network, and television broadcasting services for various channels, as well as insurance brokerage services. Further, the company offers IT system, content aggregator, and billing and collection outsourcing services; call center services; and land and building rental services, as well as related facilities. Additionally, it provides internet data center, and internet and satellite uplink-downlink services for communications; distributes internet equipment; publishes telephone directories and advertising; offers mobile contents; and provides training and online advertising services. The company was founded in 1986 and is headquartered in Bangkok, Thailand.'
    },
    'AEONTS.BK': {
        'name': 'AEON Thana Sinsap (Thailand) Public Company Limited',
        'address': '388, Exchange Tower 27th Floor Sukhumvit Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 665 0123',
        'website': 'https://www.aeon.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'AEON Thana Sinsap (Thailand) Public Company Limited provides various retail finance services in Thailand. The company operates through Retail Finance Services and Other Business segments. It offers credit card, hire purchase, personal loans, and other services. The company also provides debt collection and insurance brokerage services. As of February 28, 2022, it had 101 branches. The company was incorporated in 1992 and is headquartered in Bangkok, Thailand. AEON Thana Sinsap (Thailand) Public Company Limited is a subsidiary of AEON Bank, Ltd.'
    },
    'AFC.BK': {
        'name': 'Asia Fiber Public Company Limited',
        'address': 'Wall Street Tower 27th Floor 33/133-136 Surawongse Road Suriyawongse, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 632 7071-79',
        'website': 'https://www.asiafiber.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Textile Manufacturing',
        'description': 'Asia Fiber Public Company Limited manufactures and sells nylon products in Thailand. The company offers nylon chips, filament, textured, and recycled textured yarns, as well as nylon taffeta fabrics. It also provides daily use products, which include threads, fishing nets, ropes, ribbons, carpets, elastic tapes, gauzes, gloves, socks, laces, and swim wears, as well as brassier tapes, flags, garments and jackets, pants and tracksuits, bags, luggages, and umbrellas. The company was incorporated in 1970 and is headquartered in Bangkok, Thailand.'
    },
    'AGE.BK': {
        'name': 'Asia Green Energy Public Company Limited',
        'address': '273/1 Rama 2 Road Samaedam Bangkhunthian Bangkok 10150 Thailand',
        'phone': '66 2 894 0088',
        'website': 'https://www.age.co.th/',
        'sector': 'Energy',
        'industry': 'Thermal Coal',
        'description': 'Asia Green Energy Public Company Limited engages in the distribution of coal business in Thailand. It offers coal transportation and jetty services. The company provides boiler and chartering services, as well as involved in sourcing of steam coal activities. It also engages in export business. Asia Green Energy Public Company Limited was founded in 2004 and is based in Bangkok, Thailand.'
    },
    'AH.BK': {
        'name': 'AAPICO Hitech Public Company Limited',
        'address': '99 Moo 1 Hitech Industrial Estate Tambol Ban Lane Ampur Bang Pa-in Phra Nakhon Si Ayutthaya 13160 Thailand',
        'phone': '66 3 535 0880',
        'website': 'https://www.aapico.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Auto Parts',
        'description': 'AAPICO Hitech Public Company Limited engages in the manufacture and distribution of automobile parts, dies, and jigs in Thailand, China, Malaysia, and Portugal. It operates in three segments: Manufacture of Auto Parts; Sales of Automobiles and Provision of Automobiles Repair Service; and Others. The company offers stamped and pressed parts, including floor parts, cross members, side sills, brackets, clips, and sub-assembly parts; chassis frame components; housing axles parts; forged and machined parts, such as transmission, power train, steering and suspension systems, engine, shafts, wheel hubs, and other parts, as well as camber link for chassis systems, braking pawn for braking systems, copper forged parts; and plastic parts and plastic fuel tanks. It also provides casting parts; assembly jigs; and stamping dies. In addition, the company is involved in the sale of automobiles; provision of automobile repair, training, technical support, and information technology consulting and advisory services; venture capital business; investment in other companies; and import and export of vehicles and parts. Further, it manufactures car navigation systems and digital map solutions, as well as Oracle ERP systems; car accessories; and operates car dealership service centers. The company was founded in 1996 and is headquartered in Phra Nakhon Si Ayutthaya, Thailand.'
    },
    'AHC.BK': {
        'name': 'Aikchol Hospital Public Company Limited',
        'address': '68/3 Moo 2 Phrayasatja Road Amphoe Muang Chonburi 20000 Thailand',
        'phone': '66 38 939 999',
        'website': 'https://www.aikchol.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Aikchol Hospital Public Company Limited provides medical and nursing care services under the Aikchol Hospital trademark in Thailand. The company offers various hospital services comprising disease protection, medical treatment, health strengthening, and health rehabilitation services with 310 beds in service. It serves primarily individuals, group of policyholders of the insurance company, group of contract parties companies, and group of insured on social security. Aikchol Hospital Public Company Limited was founded in 1978 and is headquartered in Chonburi, Thailand.'
    }
    ,
    'AI.BK': {
        'name': 'Asian Insulators Public Company Limited',
        'address': '254 Seri Thai Road Kannayaow Bangkok 10230 Thailand',
        'phone': '66 2 517 1451',
        'website': 'https://www.asianinsulators.com',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'Asian Insulators Public Company Limited, together with its subsidiaries, manufactures and distributes porcelain insulators products for electricity distribution and transmission in Thailand. It offers spool, strain, line post type, pin post type, suspension, station post type, cleat, porcelain, and horizontal mounting solid core line post insulators; and underground cable support products, as well as ceramic glazed porcelain cable spacers. The company also provides services for design, supply, and installation of high voltage substation, distribution, and transmission line systems; and project management, industrial maintenance, construction, and engineering services to the water, power, and communications industries. It is also involved in producing and distributing biodiesel, vegetable oil, and animal oil fats; and exporting vegetable oil under the Pamola brand. In addition, it trades in electrical equipment, as well as provides port services. Asian Insulators Public Company Limited was founded in 1981 and is headquartered in Bangkok, Thailand.'
    },
    'AIE.BK': {
        'name': 'AI Energy Public Company Limited',
        'address': '55/2 Moo 8 Sethakit 1 Road Tambol Klongmadua Amphur Krathum Baen Samut Sakhon 74110 Thailand',
        'phone': '66 3 487 7485-8',
        'website': 'https://www.aienergy.co.th',
        'sector': 'Energy',
        'industry': 'Oil & Gas Refining & Marketing',
        'description': 'AI Energy Public Company Limited produces and distributes bio diesel and vegetable oil in Thailand. It also offers refined glycerin; and palm fatty acid distillate and glycerin pitch. The company was incorporated in 2006 and is headquartered in Samut Sakhon, Thailand. AI Energy Public Company Limited is a subsidiary of Asian Insulators Public Company Limited.'
    },
    'AIMCG.BK': {
        'name': 'AIM Commercial Growth Freehold And Leasehold Real Estate Investment Trust',
        'address': 'Unit 803, 8th Floor Tower B, GPF Witthayu Building, No. 93/1 Witthayu Road, Lumpini Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2254 0441-2',
        'website': 'https://www.aimcgreit.com/en',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'Investing in the leasehold and sublease rights of land and buildings consisting of 3 projects namely UD Town Project, 72 Courtyard Project and Porto Chino Project, and the ownership right in condominium for commercial use in Noble Solo Project.'
    #description from SET, sector & industry same with AIMIRT.BK
    },
    'AIMIRT.BK': {
        'name': 'AIM Industrial Growth Freehold and Leasehold Real Estate Investment Trust',
        'address': 'Unit 803, 8th floor,Tower B, GPF Witthayu Building, No. 93/1, Witthayu Road, Lumpini, Pathumwan Bangkok 10330',
        'phone': '66 2 254 0441-2',
        'website': 'https://www.aimirt.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'AIM Industrial Growth Freehold and Leasehold Real Estate Investment Trust focuses on investing in freehold right of land, cold storage buildings, and immovable assets related to cold storage and warehouses in Thailand. These are located in Samut Sakhon and Chachoengsao areas with total leasable area of 36,908.00 sq.m. It also intends to invest in freehold right of land and warehouses, including 5 units of warehouses with total leasable area of 21,651 sq.m. in Bang Phi, Samut Prakan. The company is based in Bangkok, Thailand.'
    },
    'AIT.BK': {
        'name': 'Advanced Information Technology Public Company Limited',
        'address': '37/2 Suthisarnvinijchai Road Samseannok HuayKwang Bangkok 10320 Thailand',
        'phone': '66 2 275 9400',
        'website': 'https://www.ait.co.th',
        'sector': 'Technology',
        'industry': 'Information Technology Services',
        'description': 'Advanced Information Technology Public Company Limited, together with its subsidiaries, designs, sells, installs, services, repairs, maintains, and trains information and communication technology network systems in Thailand. The company operates through two segments, Sales and Service, and Rental of Equipment. It provides IT solutions, including carrier grade router/switch, Web/video caching, DDOS protection, software-defined networking or the network controlled by the program to work as defined, network function virtualization, and other. The company also offers data center and cloud solutions, such as consolidation and virtualization, unified data center, converged and hyper converged infrastructure, private and public cloud infrastructure, software-defined networking or the network controlled by the program, and other. In addition, it provides collaboration solutions comprising communication through IP/VoIP system or unified communication, video and Web conferencing, contact center, and others; IoT solutions; and various enterprise network solutions consisting of router, switch, wireless LAN, WAN optimization, security, application delivery control, DNS server, identity system, network management, and other. Further, the company offers the services in the development of information technology systems to various projects with the combination of concepts in applying technology with the framework in developing the system accordingly. Additionally, it provides managed services managing complicated IT system; and maintenance service on checking the operational condition of the system, as well as spare parts for saving the time in solving the problem and mitigating the risks from the damage of equipment. The company was founded in 1992 and is headquartered in Bangkok, Thailand.'
    }
    ,

    # 21-40
    'AJ.BK': {
        'name': 'A.J. Plast Public Company Limited',
        'address': 'No. 95, Thakarm Road Kwaeng Samaedam Khet Bangkhuntien Bangkok 10150 Thailand',
        'phone': '66 2 415 0035',
        'website': 'https://www.ajplast.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Packaging & Containers',
        'description': 'A.J. Plast Public Company Limited manufactures, sells, and exports plastic films and scrap products in Thailand and internationally. It offers biaxially oriented polypropylene (BOPP), biaxially oriented polyester (BOPET), biaxially oriented polyamide (BOPA), biaxially oriented poly lactic acid (BOPLA), and cast polypropylene (CPP) films, as well as metallized BOPP, BOPET, BOPA, BOPLA, and CPP films; and Krystalox and Krystalent films. The companys products are primarily used in packaging, adhesive tapes, cassette tapes, frozen food industry etc. A.J. Plast Public Company Limited was founded in 1987 and is headquartered in Bangkok, Thailand.'
    },
    'AJA.BK': {
        'name': 'AJ Advance Technology Public Company Limited',
        'address': 'No. 427/2 Rama 2 Road Kwaeng Samaedum Khet Bangkuntien Bangkok 10150 Thailand',
        'phone': '66 2 451 6888',
        'website': 'https://www.ajthai.com',
        'sector': 'Technology',
        'industry': 'Electronics & Computer Distribution',
        'description': 'AJ Advance Technology Public Company Limited, together with its subsidiaries, engages in the wholesale and retail of electric appliances under the AJ brand in Thailand. It retails and wholesales audio and visual products, such as home theatre sets, micro-components, speakers, portable radios, audio amplifiers, Bluetooth speakers, music boxes, karaoke audio sets and players, and other audio and visual products; home appliances, including air conditioners, refrigerators, washing machines, air purifiers, thermal bottles, blenders, induction cookers, electric pots, oil-free fryers, irons, steam iron blenders, water purifies, fans, gas stoves, and solar LEDs; and electric motorcycle bikes. The company also provides top-up services for prepaid phone and service prepaid kiosks. In addition, it is also involved in the distribution of sport shoes; retail of top-up machines; logistic and export business, including TV drama programs and other entertainment media businesses; provision of e-money services and accept payment through electronic methods; investment in digital assets; and mining and trading of digital assets, including investment or providing other services about cryptocurrency and digital token transactions. The company was formerly known as Crown Tech Advance Public Company Limited and changed its sport shoes name to AJ Advance Technology Public Company Limited in June 2017. AJ Advance Technology Public Company Limited was founded in 2001 and is headquartered in Bangkok, Thailand.'
    },
    'AKR.BK': {
        'name': 'Ekarat Engineering Public Company Limited',
        'address': '9/291 U.M. Tower Building 28th Floor Ramkhamhaeng Road Suanluang Sub-Dist., Suanluang Dist. Bangkok 10250 Thailand',
        'phone': '66 2 719 8777',
        'website': 'https://www.ekarat.co.th',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'Ekarat Engineering Public Company Limited manufactures and distributes transformers and solar farms in Thailand. The company is involved in the manufacture and sale of solar cells and solar panels, including the design, construction, installation, maintenance of electricity systems from solar cells and other renewable energy; and electrical maintenance and repair, and substation construction activities. It also engages in bidding and tendering activities, as well as provision of investment advisory, engineering, and energy management services. In addition, the company distributes solar modules; and produces and sells electricity from solar cells, as well as provides consulting services on energy conservation. Ekarat Engineering Public Company Limited was incorporated in 1981 and is headquartered in Bangkok, Thailand.'
    },
    'ALLA.BK': {
        'name': 'Alla Public Company Limited',
        'address': '933, 935,937,939 Soi Onnut46 Onnut Road Onnut Suanluang Bangkok 10250 Thailand',
        'phone': '66 2 322 0777',
        'website': 'https://alla.co.th',
        'sector': 'Industrials',
        'industry': 'Industrial Distribution',
        'description': 'Alla Public Company Limited imports, manufactures, and distributes cranes and electric hoists, industrial doors, loading docks, electronic lifts, racking and automated storage and retrieval system, and related parts and other equipment in Thailand. It provides crane and hoist, includes overhead, gantry and semi gantry crane, jib, wall traveling, monorail, suspension, and explosion proof cranes; and electric chain and wire, manual chain, and explosion proof hoists. The company also offers loading dock and equipment comprises electric hydraulic, mechanical dock, airbag, dock seal, inflatable dock, and retractable dock shelter; overhead sectional, high speed, traffic, and cold storage doors; and PVC strip and air curtains. In addition, it provides warehouse systems, include warehouse management systems and accessories, automated sorting and retrieving systems, warehouse control systems, transportation management systems, conveyors, picking and sorting systems, racking systems, high volume low speed fans, and warehouse LED systems; and distributes and install solar cell panels. Further, it provides installation and after-sales services. Alla Public Company Limited was founded in 1990 and is headquartered in Bangkok, Thailand.'
    },
    'ALLY.BK': {
        'name': 'Ally Leasehold Real Estate Investment Trust',
        'address': '888 Crystal Design Center, E Building, Praditmanutham Road, Klongjan, Bangkok, Thailand 10240',
        'phone': '66 2 101 5888',
        'website': 'http://www.allyreit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Retail',
        'description': 'Investing in leasehold rights/sub-leasehold rights of 13 projects as follows 1. The Crystal Design Center 2. The Crystal Ekamai-Ramindra 3. The Crystal SB Ratchapruek 4. Amorini 5. Im Park 6. Plearnary Mall 7. Sammakorn Place Ramkhamhaen 8. Sammakorn Place Rangsit 9. Sammakorn Place Ratchapruek 10. The Scene 11. Kad Farang Village 12. The Crystal Chaiyapruek 13. The Prime Hua Lamphong'
    
    },
    'ALT.BK': {
        'name': 'ALT Telecom Public Company Limited',
        'address': '52/1 Moo 5, Bang Kruay-Sai Noi Road Bang Si Thong Sub-district Bang Kruai 11130 Thailand',
        'phone': '66 2 863 8999',
        'website': 'https://www.alt.co.th',
        'sector': 'Technology',
        'industry': 'Communication Equipment',
        'description': 'ALT Telecom Public Company Limited engages in the manufacture, installation, maintenance, rental, and sale of telecommunication network equipment in Thailand and internationally. The company operates through three segments: Network Equipment and Electricity Meter Distribution, Network Equipment Installation Business, and Network Equipment Rental Business. It also manufactures, assembles, installs, and distributes electricity meters; and offers telecommunication products comprising fiber optic cables, telecom shelters, cell-on-wheel vehicles, antennas, tappers, splitters, repeaters, wireless range extenders, optical cables, and outdoor enclosures, as well as rapid deployment products. In addition, it is involved in the construction of base stations; installation and repairing of telecommunication, digital, and renewable energy equipment; sale, installation, and maintenance of electrical equipment and systems; leasing and management of telecommunication basic structures. The company was incorporated in 2001 and is headquartered in Bang Kruai, Thailand.'
    },
    'ALUCON.BK': {
        'name': 'Alucon Public Company Limited',
        'address': '500 Moo 1, Soi Sirikam Sukhumvit Road Samrong Nua Sub-district Mueang Samut Prakan 10270 Thailand',
        'phone': '66 2 398 0147',
        'website': 'https://www.alucon.th.com',
        'sector': 'Basic Materials',
        'industry': 'Aluminum',
        'description': 'Alucon Public Company Limited produces and distributes aluminum containers primarily in Thailand. It operates in two segments, Can and Tube, and Slug. The company offers aluminum collapsible tubes, monobloc aerosol cans, bottles, and rigid wall containers, as well as marker pen bodies. It also provides technical impact extrusions, aluminium slugs, aluminium coils, aluminium pellets, strips, plates, etc. The company exports its products to approximately 40 countries, including Japan, Australia, the United States, Indonesia, and South Africa. Alucon Public Company Limited was founded in 1961 and is headquartered in Mueang Samut Prakan, Thailand.'
    },
    'AMANAH.BK': {
        'name': 'Amanah Leasing Public Company Limited',
        'address': '16-16/1 Soi Kasemsan 1 Phayathai Road Wangmai Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 091 6456',
        'website': 'https://www.amanah.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Amanah Leasing Public Company Limited provides hire purchase, financial and operating lease, and inventory finance services to consumers and corporates in Thailand. It operates in two segments, Hire Purchase and Others. The company also offers quick loans for used cars, and car leasing business, as well as auto to money services. It operates 46 branches in the central region, northeastern region, northern region, and southern region across the country. The company was formerly known as Nava Leasing Public Company Limited and changed its name to Amanah Leasing Public Company Limited in October 2010. Amanah Leasing Public Company Limited was founded in 1992 and is headquartered in Bangkok, Thailand.'
    },
    'AMARIN.BK': {
        'name': 'Amarin Printing and Publishing Public Company Limited',
        'address': '378 Chaiyaphruk Road Taling Chan Bangkok 10170 Thailand',
        'phone': '66 2 422 9999',
        'website': 'https://www.amarin.co.th',
        'sector': 'Communication Services',
        'industry': 'Publishing',
        'description': 'Amarin Printing and Publishing Public Company Limited, together with its subsidiaries, engages in the publishing, advertising, and publications distribution businesses in Thailand. It offers a range of printing services, such as artwork creative design, photography, and image retouching, as well as digital and packaging printing service. The company also conceptualizes, compiles, designs, publishes, and delivers offline content, including books, magazines/newsletters, cards/leaflets/brochures/posters, annual reports, anniversary books, pocket books, and gifts; online content, including e-books, video clips, websites, and applications, as well as augmented reality and social network content; and visual content comprising infographics, illustrations, picture, and photography content. In addition, it engages in the organization of events, fairs, and seminars, as well as offsite training programs for private companies and SMEs; purchase, procurement, lease, and leasehold of various assets; and production, distribution, retail, and wholesale of various publication formats that include Thai and translated foreign language books, Praew and Sudsapda magazines for women, electronic creative media comprising video and multimedia teaching materials, and other printed materials. The company was formerly known as Amarin Printing Group Company Limited and changed its name to Amarin Printing and Publishing Public Company Limited in 1993. Amarin Printing and Publishing Public Company Limited was founded in 1976 and is headquartered in Bangkok, Thailand.'
    },
    'AMATA.BK': {
        'name': 'Amata Corporation Public Company Limited',
        'address': '2126 Kromadit Building New Petchburi Road Bangkapi Huaykwang Bangkok 10310 Thailand',
        'phone': '66 2 792 0000',
        'website': 'https://www.amata.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Amata Corporation Public Company Limited, together with its subsidiaries, engages in the planning, developing, managing, and marketing of industrial estates in Thailand and internationally. The company also produces, distributes, and treats water for industrial use; provides management services in common area; operates a school; and constructs factory for rent. In addition, it operates as a REIT manager. The company was founded in 1989 and is headquartered in Bangkok, Thailand.'
    },
    'AMATAR.BK': {
        'name': 'Amata Summit Growth Freehold and Leasehold Real Estate Investment Trust',
        'address': '2126 Kromadit Building New Petchburi Road Bangkapi Huay Kwang Bangkok 10310 Thailand',
        'phone': '66 2 792 0089',
        'website': 'https://www.amatareit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'Amata Summit Growth Freehold and Leasehold Real Estate Investment Trust is a real estate investment trust externally managed by Amata Summit REIT Management Co., Ltd. It invests in the real estate markets. Amata Summit Growth Freehold and Leasehold Real Estate Investment Trust is based in Bangkok, Thailand.'
    },
    'AMATAV.BK': {
        'name': 'Amata VN Public Company Limited',
        'address': '2126, Kromadit Building New Petchburi Road Bangkapi Huay Kwang Bangkok 10310 Thailand',
        'phone': '66 2 792 0000',
        'website': 'https://www.amatavn.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate Services',
        'description': 'Amata VN Public Company Limited, through its subsidiaries, engages in the development of industrial estate and related business in Vietnam. It is also involved in the leasing of industrial land, ready built factories, and commercial and residential land, as well as office rental activities. In addition, the company provides utility services. The company was incorporated in 2012 and is headquartered in Bangkok, Thailand.'
    },
    'AMC.BK': {
        'name': 'Asia Metal Public Company Limited',
        'address': '55, 55/1 Moo 2 Soi Watnamdaeng Srinakarin Road T.Bangkeaw Bang Phli 10540 Thailand',
        'phone': '66 2 338 7222',
        'website': 'https://www.asiametal.co.th',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'Asia Metal Public Company Limited produces and sells processed steel products in Thailand. It offers hot-rolled, pickled and oiled, and cold-rolled products to steel wholesalers and end user factories; and round, square, and rectangular steel pipes, as well as light lips channels and C-shaped furring. The company also trades in round-bars and deformed-bars, as well as square and round steel tubes. In addition, it provides steel cutting and modifying services. The company was founded in 1993 and is headquartered in Bang Phli, Thailand.'
    },
    'AMR.BK': {
        'name': 'AMR Asia Public Company Limited',
        'address': '469 Soi Prawit Lae Phuaen Prachachuen Road Las Yao Chatuchak 10900 Thailand',
        'phone': '66 2 589 9955',
        'website': 'https://www.amrasia.com',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'AMR Asia Public Company Limited provides construction services for telecommunication, and electronic and computer systems in Thailand. It also offers equipment installation and related services. The company was incorporated in 1999 and is headquartered in Chatuchak, Thailand.'
    },
    'ANAN.BK': {
        'name': 'Ananda Development Public Company Limited',
        'address': 'No. 99/1 Moo 14 Soi Windmill Housing Estate Bangna-Trad Road (K.M.10.5) Bangpleeyai Sub-district, Bangplee Dist.  Bang Phli 10540 Thailand',
        'phone': '66 2 317 1155',
        'website': 'https://www.ananda.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Ananda Development Public Company Limited, together with subsidiaries, engages in the development and sale of various real estate projects in Thailand. It operates through Real Estate Development, Management of Real Estate Development Project, and Other segments. The company provides management services for real estate projects; house construction services; and real estate brokerage services, as well as acts as a property agent. It is also involved in the juristic person management; media production; and property rental, as well as provision of academic seminar services. The company develops condominium projects under the Ashton, Ideo Q, Venio, Ideo Mobi, Ideo, Elio, and Unio brands; and housing projects and townhouses under the Artale, Airi, Atoll, Arden, Urbanio, and Unio Town brands. Ananda Development Public Company Limited was founded in 1999 and is headquartered in Bang Phli, Thailand.'
    },
    'AOT.BK': {
        'name': 'Airports of Thailand Public Company Limited',
        'address': 'No. 333, Cherdwutagard Road Srikan Don Mueang Bangkok 10210 Thailand',
        'phone': '66 2 535 1192',
        'website': 'https://www.airportthai.co.th',
        'sector': 'Industrials',
        'industry': 'Airports & Air Services',
        'description': 'Airports of Thailand Public Company Limited, together with its subsidiaries, engages in the airport business in Thailand. The company operates through Airport Management Business, Hotel Business, Ground Aviation Services, Security Business, and Project on Perishable Goods Business segments. It operates 6 international airports, including Suvarnabhumi Airport, Don Mueang International Airport, Chiang Mai International Airport, Hat Yai International Airport, Phuket International Airport and Mae Fah Luang - Chiang Rai International Airport. The company is also involved in the hotel and restaurant business; and operation and management of the project on perishable goods at Suvarnabhumi Airport. In addition, it apron services, ground equipment, ground passenger services, security services at airports, and other airport related services; aircraft maintenance, repair, and overhaul services; catering services for airlines; hydrant dispenser and aircraft refueling services; aviation depot; electronics information exchange services; and cargo depot services. Airports of Thailand Public Company Limited was incorporated in 2002 and is headquartered in Bangkok, Thailand.'
    },
    'AP.BK': {
        'name': 'AP (Thailand) Public Company Limited',
        'address': 'Ocean Tower I Building 18th Floor 170/57 New Ratchadapisek Road Klongtoey District Bangkok 10110 Thailand',
        'phone': '66 2 261 2518',
        'website': 'https://www.apthai.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'AP (Thailand) Public Company Limited, together with its subsidiaries, engages in the real estate development in Thailand. It operates through LowRise, HighRise, and Other segments. The Low-rise segment develops single detached houses and townhouses. The High-rise segment develops condominiums. The Other segment provides after-sales, property brokerage, and construction services. This segment also offers education and training services. The company was formerly known as Asian Property Development Public Company Limited and changed its name to AP (Thailand) Public Company Limited in May 2013. AP (Thailand) Public Company Limited was founded in 1991 and is headquartered in Bangkok, Thailand.'
    },
    'APCO.BK': {
        'name': 'Asian Phytoceuticals Public Company Limited',
        'address': '84/3 Moo 4 Northern Region Ind. Est (W. Super Highway No.11 Road Banklang Subdistrict Muang Lamphun District Lamphun 51000 Thailand',
        'phone': '66 5 358 1374',
        'website': 'https://www.apco.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Household & Personal Products',
        'description': 'Asian Phytoceuticals Public Company Limited engages in the research and development, manufacture, and distribution of healthcare and natural extracts-based beauty products in Thailand and internationally. Its products include dietary supplements, cosmetics, and personal care products that are developed from natural plant and botanical extracts. The company also provides slimming, anti-wrinkle, and skin care products, as well as products for balancing immunity. It distributes its products through call centers, direct service method, large drug stores, distributors, and digital and multi-level-marketing channels. The company was formerly known as Natural Cosmetics Research Co., Ltd. and changed its name to Asian Phytoceuticals Public Company Limited in July 2005. Asian Phytoceuticals Public Company Limited was founded in 1988 and is headquartered in Lamphun, Thailand.'
    },
    'APCS.BK': {
        'name': 'Asia Precision Public Company Limited',
        'address': 'Amata Nakorn Industrial Estate 700/331 Moo 6 Donhualor Muang Chonburi Chonburi 20000 Thailand',
        'phone': '66 3 846 8300',
        'website': 'https://www.apcs.co.th',
        'sector': 'Industrials',
        'industry': 'Metal Fabrication',
        'description': 'Asia Precision Public Company Limited, together with its subsidiaries, manufactures and sells precision metal parts and components in Thailand and internationally. The company is also involved in the design, engineering, consultation, construction, maintenance, system testing, and sale of construction related equipment for various power plant projects, such as renewable power plants, power sub-stations, and raw water distributing facilities; production and distribution of raw water; distribution of materials, tools, equipment, and spare parts for the construction of power plants; and other energy businesses. It serves automotive, air conditioning and refrigeration compressor, digital camera, and medical sectors. The company was founded in 1994 and is headquartered in Chonburi, Thailand.'
    },
    'APEX.BK': {
        'name': 'Apex Development Public Company Limited',
        'address': 'Zone A, 900 Tonson Tower 18th Floor Ploenchit Road Lumpini, Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 636 2465',
        'website': 'https://www.apexpcl.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Apex Development Public Company Limited develops and sells real estate properties. The company develops residential condominiums, villas, and hotels, as well as resorts and land. It also provides services for customers to operate apartments and villas for rent. In addition, the company engages in the operation of rental management. The company was formerly known as Sun Tech Group Public Company Limited and changed its name to Apex Development Public Company Limited in August 2007. Apex Development Public Company Limited was founded in 1988 and is headquartered in Bangkok, Thailand.'
    }
    ,

    # 41-60
    'APURE.BK': {
        'name': 'Agripure Holdings Public Company Limited',
        'address': 'The Ruamjaipattana Foundation Building No. 70, Moo 6 Klong 1 District Klong Luang Pathum Thani 12120 Thailand',
        'phone': '66 2 516 0941',
        'website': 'https://www.apureholdings.com',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Agripure Holdings Public Company Limited, through its subsidiaries, manufactures and distributes agro products in Thailand. The company offers canned and pouched sweet corn products; fresh vegetable and fruit products; and commercial seeds, as well as breeds and distributes corn seeds. It also exports its products to approximately 50 countries. The company was founded in 1986 and is based in Pathum Thani, Thailand.'
    },
    'AQ.BK': {
        'name': 'AQ Estate Public Company Limited',
        'address': 'AQ Square Building 102 Rimklongbangkapi Road Bang Kapi Sub-District Huai Khwang District Bangkok 10310 Thailand',
        'phone': '66 2 033 5555',
        'website': 'https://www.aqestate.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'AQ Estate Public Company Limited develops and sells properties in Thailand. It operates in four segments: Property Development Low Rise, Property Development High Rise, Services, and Property Rental and Service. The company primarily develops single house, condominium, town home, and hospitality projects. It also provides recreational and sale management services; operates hotels and resorts; manages commercial space; and offers real estate trading and rental services. The company was formerly known as Krisdamahanakorn Public Company Limited and changed its name to AQ Estate Public Company Limited in April 2014. AQ Estate Public Company Limited was founded in 1982 and is headquartered in Bangkok, Thailand.'
    },
    'AQUA.BK': {
        'name': 'Aqua Corporation Public Company Limited',
        'address': 'R.S. Tower 21st Floor 121/68-69, Ratchadapisek Road Dindaeng Bangkok 10400 Thailand',
        'phone': '66 2 694 8888',
        'website': 'https://www.aquacorp.co.thSector',
        'sector': 'Communication Services',
        'industry': 'Advertising Agencies',
        'description': 'Aqua Corporation Public Company Limited provides out of home media services in Bangkok. The company operates through Out of Home Media; and Property for Rent and Service segments. It provides real estate rental services and warehouse rental services. The company was formerly known as P Plus P Public Company Limited and changed its name to Aqua Corporation Public Company Limited in April 2012. Aqua Corporation Public Company Limited was founded in 1994 and is based in Bangkok, Thailand.'
    },
    'AS.BK': {
        'name': 'Asiasoft Corporation Public Company Limited',
        'address': 'No.51, Major Tower Rama 9 - Ramkumhang 18th Floor, Room No.3-8 Rama 9 Road, Hua Mak Sub-District Bangkapi District Bangkok 10240 Thailand',
        'phone': '66 2 769 8888',
        'website': 'https://www.asiasoft.co.th',
        'sector': 'Communication Services',
        'industry': 'Electronic Gaming & Multimedia',
        'description': 'Asiasoft Corporation Public Company Limited, together with its subsidiaries, engages in the provision of established community platform and expansive distribution network for game developers in Thailand, Vietnam, Indonesia, Singapore, Malaysia, the Philippines, and internationally. The company operates through two segments, Online Game and Distribution. The Online Game segment offers online games, including massive multiplayer online role-playing, casual, first person shooting, and mobile games. The Distribution segment provides payment channel services. The company publishes the games under the PlayPark brand. It also offers @Cafe programme, which brings online games to Internet cafe gamers, as well as promotional media and various marketing services for its member shops; and @Cash that is an in-game credits top-up system. The company was formerly known as B.M. Media (Thailand) Company Limited. Asiasoft Corporation Public Company Limited was incorporated in 2001 and is headquartered in Bangkok, Thailand.'
    },
    'ASAP.BK': {
        'name': 'Synergetic Auto Performance Public Company Limited',
        'address': '149 Moo 3 Theparak Road Theparak, A Mueang Samut Prakan 10270 Thailand',
        'phone': '66 2 091 8181',
        'website': 'https://www.asapcarrent.com',
        'sector': 'Industrials',
        'industry': 'Rental & Leasing Services',
        'description': 'Synergetic Auto Performance Public Company Limited provides car rental services in Thailand. The company offers operating leasing services for corporate customers; short-term car rental services for ordinary customers; limousine rental services for corporate customers; and car rental services through an asap application. It also operates Lifestyle Mall, a car rental center and complete used cars, which include food and beverage outlets; and asap select franchises that are service centers for short-term car rentals and second-hand car sales. In addition, the company provides car maintenance services. It offers services under asap brand name. Synergetic Auto Performance Public Company Limited is headquartered in Mueang Samut Prakan, Thailand.'
    },
    'ASEFA.BK': {
        'name': 'Asefa Public Company Limited',
        'address': '5 Moo 1, Rama II Road Khok-Krabue Muang Samutsakhon Samut Sakhon 74000 Thailand',
        'phone': '66 2 686 7777',
        'website': 'https://www.asefa.co.th',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'Asefa Public Company Limited manufactures and provides electrical power distribution, switchboard, trunking, lighting, automation, and energy management solutions in Thailand. The company manufactures and sells modular switchboards, such as electric control panels, automation devices, motor panels, substation units, and other panels related to electrical distribution system; licensed type tested switchboards; metal trunking products comprising wire ways, cable trays, cable ladders, flush floor, underfloor ducts, and perforated trunking products; and fluorescent-lamp luminaires for recessed and pendant installation applications under the ASEFA brand. It also distributes and supplies electrical and control, electrical power distribution, lighting and equipment, and mineral insulated metal sheated cables. In addition, the company offers design, consulting, planning and equipment selection, installation and modification, test and commissioning, and ETAP electrical engineering software solutions; integrated solutions comprising electrical power distribution solutions, data center and redundancy electrical power system, energy management and monitoring systems, automation and communication system, power quality solutions, and lighting solutions; and after sales services. It serves infrastructure, industry, commercial building, residential, healthcare, data center and telecommunication, and power generation sectors. Asefa Public Company Limited was incorporated in 1997 and is based in Samut Sakhon, Thailand.'
    },
    'ASIA.BK': {
        'name': 'Asia Hotel Public Company Limited',
        'address': 'No. 296 Phayathai Road ThanonPetchari Rajathevi Bangkok 10400 Thailand',
        'phone': '66 2 217 0808',
        'website': 'https://www.asiahotel.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'Asia Hotel Public Company Limited, together with its subsidiaries, engages in the hotel and restaurant business in Thailand and internationally. The company is involved in the rental of a shopping center and hotel; and provision of utility, security, and cleaning services. Asia Hotel Public Company Limited was incorporated in 1964 and is based in Bangkok, Thailand.'
    },
    'ASIAN.BK': {
        'name': 'Asian Sea Corporation Public Company Limited',
        'address': '55/2 Moo 2 Rama 2 Road Bangkrajao Muang Samut Sakhon 74000 Thailand',
        'phone': '66 3 482 2700',
        'website': 'https://www.asiansea.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Asian Sea Corporation Public Company Limited, together with its subsidiaries, engages in the production and distribution of processed frozen seafood and provision of cold storage services in Thailand and internationally. The company operates through three segments: Frozen and Packaged Food Products, Feedstuff, and Other Business. Its frozen food includes shrimp, squid, Sillago fish, octopus, and cuttle fish. The company is also involved in the production of frozen ready-to-eat foods, packaged seafoods, fishmeal, and feedstuff; production and distribution of animal feeds; and provision of marketing and management services. In addition, it offers wet pet food products, such as soups, salads, fish and meat dishes, mousse, and pate; aquaculture feed pellets; canned and pouch tuna products; and dry feed products for pets, including cats and dogs. The company offers its products under the Monchou, Monchou Balanced, and Hajiko brand names. Asian Sea Corporation Public Company Limited was founded in 1964 and is headquartered in Mueang Samut Sakhon, Thailand.'
    },
    'ASIMAR.BK': {
        'name': 'Asian Marine Services Public Company Limited',
        'address': '128 Moo 3 Suksawad Road Laemfapa Prasamutjedee Samut Prakan 10290 Thailand',
        'phone': '66 2 815 2060',
        'website': 'https://www.asimar.com',
        'sector': 'Industrials',
        'industry': 'Aerospace & Defense',
        'description': 'Asian Marine Services Public Company Limited, together with its subsidiaries, engages in the ship building and ship repairing businesses in Thailand. The company constructs various types of ships; undertakes ship conversion projects; and offers a range of offshore support services, as well as engineering services. It also operates as an agent of machinery and equipment for marine service; and subcontractor of ship repair, as well as provides pollution control and environmental management services. The company was founded in 1981 and is headquartered in Samut Prakan, Thailand.'
    },
    'ASK.BK': {
        'name': 'Asia Sermkij Leasing Public Company Limited',
        'address': 'Sathorn City Tower 24th Floor 175, South Sathorn Road Tungmahamek, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 679 6226',
        'website': 'https://www.ask.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Asia Sermkij Leasing Public Company Limited provides auto hire purchase services primarily in Thailand. It operates through five segments: Hire Purchase, Leasing, Loan, Factoring, and Insurance Broker. The company provides automobile hire purchase services for new and used automobiles, including passenger and commercial cars, such as pickup, van, truck, taxi, etc.; auto and machine leasing services for commercial customers; personal loans, sale and hire purchase back, and floor plan financing to hire purchase customers, entrepreneurs, and automotive dealers; and factoring services to commercial customers in various industries. It also offers insurance brokerage services to hire purchase and finance lease customers; and auto registration and tax renewal services. The company was founded in 1984 and is headquartered in Bangkok, Thailand. Asia Sermkij Leasing Public Company Limited is a subsidiary of Chailease Holding Company Limited.'
    },
    'ASP.BK': {
        'name': 'Asia Plus Group Holdings Public Company Limited',
        'address': 'Sathorn City Tower Floors 3,9 and 11 No. 175, South Sathorn Road Thungmahamek, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 680 1111',
        'website': 'https://www.asiaplusgroup.co.th',
        'sector': 'Financial Services',
        'industry': 'Capital Markets',
        'description': 'Asia Plus Group Holdings Public Company Limited, together with its subsidiaries, engages in the securities business in Thailand. It operates through four segments: Securities and Derivatives Brokerage, Investment Banking, Fund Management, and Investment Trading. The company provides securities and derivatives brokering services for local and foreign investors; investment advisory; security underwriting; securities borrowing and lending; venture capital management; financial advisory; and private, derivatives, and mutual fund management services. It also invests in unit trusts; and buys, sells, and exchanges securities. The company was formerly known as Asia Plus Group Holdings Securities Public Company Limited and changed its name to Asia Plus Group Holdings Public Company Limited in July 2015. Asia Plus Group Holdings Public Company Limited was incorporated in 1974 and is based in Bangkok, Thailand.'
    },
    'ASW.BK': {
        'name': 'Assetwise Public Company Limited',
        'address': '9 Soi Ramintra 5 Junction 23 Anusawari Bang Khen Bangkok 10220 Thailand',
        'phone': '66 2 521 9533',
        'website': 'https://assetwise.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Asset Wise Public Company Limited develops and sells residential real estate properties in Thailand. It develops condominiums and low-rise real estate projects consisting of housing estates, townhomes, and home offices. The company also rents real estate properties; and offers management and real estate brokerage services. Asset Wise Public Company Limited was incorporated in 2005 and is headquartered in Bangkok, Thailand.'
    },
    'AURA.BK': {
        'name': 'Aurora Design Public Company Limited',
        'address': '444 Soi Udomsuk 26 Bang Na Nuea Subdistrict Bang Na District Bangkok 10260 Thailand',
        'phone': '66 2 749 5044',
        'website': 'http://www.auroradesign.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Luxury Goods',
        'description': 'Retail business of gold jewelries, diamond and gemstone jewelries and other relating businesses providing one-stop service'
    },
    'AWC.BK': {
        'name': 'Asset World Corp Public Company Limited',
        'address': 'Empire Tower 54th Floor 1 South Sathorn Road Yannawa, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 180 9999',
        'website': 'https://www.assetworldcorp-th.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate Services',
        'description': 'Asset World Corp Public Company Limited invests in, develops, and manages real estate properties in Thailand. The company operates in two segments: Hotel and Related Services, and Rental and Rendering of Commercial Building Services. Its business portfolio consists of hotels; lifestyle destinations, community shopping malls, and community markets; and mixed-use properties. The company also operates digital platforms; and engages in property leasing activities. Asset World Corp Public Company Limited was incorporated in 2018 and is headquartered in Bangkok, Thailand.'
    },
    'AYUD.BK': {
        'name': 'Allianz Ayudhya Capital Public Company Limited',
        'address': '898 Ploenchit Tower 7th Floor Ploenchit Road, Lumpini Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 305 7374',
        'website': 'https://www.ayud.co.th',
        'sector': 'Financial Services',
        'industry': 'Insurance—Property & Casualty',
        'description': 'Allianz Ayudhya Capital Public Company Limited, an investment holding company, provides non-life insurance products in Thailand. It operates in three segments: Non-Life Insurance Business, Investment Business, and Service Business. The company offers fire, marine, motor, and miscellaneous insurance products. It also provides health services. The company was formerly known as Sri Ayudhya Capital Public Company Limited and changed its name to Allianz Ayudhya Capital Public Company Limited in April 2019. Allianz Ayudhya Capital Public Company Limited was incorporated in 1950 and is headquartered in Bangkok, Thailand.'
    },
    'B.BK': {
        'name': 'Begistics Public Company Limited',
        'address': '52 Thaniya Plaza Building 28th Floor Silom Road Suriyawongse, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 096 4999',
        'website': 'https://www.begistics.co.th',
        'sector': 'Industrials',
        'industry': 'Marine Shipping',
        'description': 'Begistics Public Company Limited, together with its subsidiaries, engages in the operation of a port in Bangpakong, Thailand. The company offers container depot, warehousing, wharf, and other related services. It also provides logistics services, which consist of domestic transportation services with trucks, trailers, containers, bulk cargoes, large cargoes, and cranes; crane rental services, international freight management services; logistics and project management services; and truck sales and maintenance services. In addition, the company engages in buying, selling, renting, exchanging condominiums, apartments, and other real estate, as well as provides loan and factoring services. Further, it distributes raw water, tap water, PVC pipes, and plastic pipes; and offers repairs, maintains, installs, and assembles sewer and wastewater pipes, as well as car rental services; and trade consultant services. The company was formerly known as Bangpakong Terminal Public Company Limited and changed its name to Begistics Public Company Limited in March 2018. Begistics Public Company Limited was incorporated in 1995 and is headquartered in Bangkok, Thailand.'
    },
    'B52.BK': {
        'name': 'B-52 Capital Public Company Limited',
        'address': '973 President Tower 7th Floor, Unit 7B, 7C, 7D and 7I Ploenchit Road, Lumpini Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 656 0189',
        'website': 'https://b52.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate Services',
        'description': 'B-52 Capital Public Company Limited, together with its subsidiary, provides wholesale distribution, retail sales, and advertising media solutions in Thailand. It offers logistical planning, product distribution, and warehousing solutions to retailers; operates e-commerce marketing solutions under the TANJAI-D name; media and marketing solutions; and network marketing solutions. The company also provides commercial and small business loans, as well as insurance policies. The company was formerly known as Digital Tech Planet Public Company Limited and changed its name to B-52 Capital Public Company Limited in May 2019. B-52 Capital Public Company Limited was founded in 1964 and is based in Bangkok, Thailand.'
    },
    'BA.BK': {
        'name': 'Bangkok Airways Public Company Limited',
        'address': 'Vibhavadirangsit Road 99 Mu 14 Chom Phon Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 265 5678',
        'website': 'https://www.bangkokair.com',
        'sector': 'Industrials',
        'industry': 'Airlines',
        'description': 'Bangkok Airways Public Company Limited, together with its subsidiaries, provides air transportation and airport services. The company operates through three segments: Airline, Airport, and Supporting Airline Business. The Airline segment engages in the sale of tickets, as well as the provision of services for passengers. The Airport segment offers location services for passengers and airlines. The Supporting Airline Business segment provides ground handling, cargo, and catering services for airlines and customers. The company also offers aviation training, and REIT and other management services; development and management services for public airports; operates restaurants; distributes souvenirs; and produces and processes food for distribution. Bangkok Airways Public Company Limited was founded in 1968 and is headquartered in Bangkok, Thailand.'
    },
    'BAFS.BK': {
        'name': 'Bangkok Aviation Fuel Services Public Company Limited',
        'address': '171/2 Kamphaeng Phet 6 Road Don Mueang Khet Don Mueang Bangkok 10210 Thailand',
        'phone': '66 2 834 8900',
        'website': 'https://www.bafsthai.com',
        'sector': 'Industrials',
        'industry': 'Airports & Air Services',
        'description': 'Bangkok Aviation Fuel Services Public Company Limited provides aviation fuel storage and aircraft refueling services at Bangkok International Airport in Thailand. The company offers into-plane, hydrant network, and fuel pipeline transportation services, as well as assembles and maintains hydrant dispensers. It also manufactures and distributes electricity from solar power; invests in solar power business; and provides property rental services. The company was incorporated in 1983 and is headquartered in Bangkok, Thailand.'
    },
    'BAM.BK': {
        'name': 'Bangkok Commercial Asset Management Public Company Limited',
        'address': '99, Surasak Road Silom Sub-district Bangrak District Bangkok 10500 Thailand',
        'phone': '66 2 267 1900',
        'website': 'https://www.bam.co.th',
        'sector': 'Financial Services',
        'industry': 'Asset Management',
        'description': 'Bangkok Commercial Asset Management Public Company Limited operates as an asset management company. It purchases non-performing loans (NPLs) from financial institutions in Thailand, including banks and other financial institutions; and manages NPLs through debt restructuring negotiations with debtors. The company also acquires non-performing assets (NPAs) through various means, such as negotiating with debtors for the transfer of the guarantee or repayment property, foreclosing the debt settlement, and purchasing NPAs directly from other financial institutions. Its NPLs are primarily guaranteed by real estate properties, secured by the first mortgage registration; and NPAs are primarily real estate assets, such as empty lands, hotels, commercial buildings, movable assets, and other securities, as well as residential properties, including detached houses, townhouses, and condominiums. The company was founded in 1998 and is headquartered in Bangkok, Thailand.'
    },

    # 61-80
    'BANPU.BK': {
        'name': 'Banpu Public Company Limited',
        'address': 'Thanapoom Tower 27th Floor 1550 New Petchburi Road Makkasan, Ratchathewi Bangkok 10400 Thailand',
        'phone': '66 2 694 6600',
        'website': 'https://www.banpu.com',
        'sector': 'Energy',
        'industry': 'Thermal Coal',
        'description': 'Banpu Public Company Limited engages in the coal mining and power businesses. The company operates various coal project in Mongolia; thermal power plants in Thailand, Lao PDR, and China; wind farm in Vietnam; and solar farms in Japan. It provides solar rooftop solutions and installation for industries and large businesses; energy storage solutions; electric vehicle and fleet management services; consultation services on customized energy management system; and renewable energy ecosystem for clean energy. The company also involved in the power and steam production, purchase, and trading business; provident fund management; solar power generation; logistics; sales and marketing activities; natural gas business; investment in power and renewable energy; and research and development business. In addition, it provides coal mining and trading; and business consultancy services, as well as fuel trading services. The company was formerly known as Ban Pu Coal Company Limited and changed its name to Banpu Public Company Limited in July 1993. Banpu Public Company Limited was founded in 1983 and is headquartered in Bangkok, Thailand.'
    },
    'BAREIT.BK': {
        'name': 'BA Airport Leasehold Real Estate Investment Trust',
        'address': '99 Moo 14 Vibhavadi Rangsit Road, Chom Phon, Chatuchak, Bangkok 10900 Thailand',
        'phone': '66 2 265 5709',
        'website': 'http://www.bareit.co.th',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'nvestment in the leasehold rights over the land, structures, and components of certain parts of the assets used in the operation of the airport in the Samui Airport'
    },
    'BAY.BK': {
        'name': 'Bank of Ayudhya Public Company Limited',
        'address': '1222 Rama III Road Bang Phongphang Subdistrict Yannawa District Bangkok 10120 Thailand',
        'phone': '66 2 296 2000',
        'website': 'https://www.krungsri.com',
        'sector': 'Financial Services',
        'industry': ' Banks—Regional',
        'description': 'Bank of Ayudhya Public Company Limited, together with its subsidiaries, provides commercial banking products and services to individuals, corporates, small and medium-sized businesses, and financial institutions. Its Retail segment offers a range of banking and related financial services, including current and savings accounts, fixed deposits, bills of exchange, housing loans, credit cards, personal loans and sale finance loans, hire-purchase and leasing, wealth management, and bancassurance products. The companys Commercial segment provides financial services and products comprising the range of credit facilities, which comprise short-term working capital, cash management, trade finance, transactional banking, advisory services, and treasury and money markets products. It also offers refinancing and venture capital services; car rental, collection, and personnel services; mutual funds and private fund management services; factoring and information technology services; and microfinance, real estate lease, and securities services, as well as operates as a life, non-life, and general insurance broker. In addition, the company develops, manages, and sells non-performing assets and other assets transferred from financial institutions. Bank of Ayudhya Public Company Limited was founded in 1945 and is headquartered in Bangkok, Thailand. Bank of Ayudhya Public Company Limited is a subsidiary of MUFG Bank, Ltd.'
    },
    'BBGI.BK': {
        'name': 'BBGI Public Company Limited',
        'address': '2098 M Tower Building 5th Floor Sukhumvit Road, Phra Khanong Tai Phra Khanong Bangkok 10260 Thailand',
        'phone': '66 2 335 8899',
        'website': 'https://www.bbgigroup.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'BBGI Public Company Limited manufactures and distributes biofuel and related products in Thailand. It operates through three segments: Biodiesel, Ethanol, and Others. The company offers biodiesel products, including crude glycerine and methyl ester products; and bioethanol products. It also provides bio-based products, such as ASTA  IMMU, a supplement for aesthetic and antiviral benefits; ASTA  ViS for vision and healthy eyes; and Calcium LT for bone and joint care. The company is headquartered in Bangkok, Thailand. BBGI Public Company Limited is a subsidiary of Bangchak Corporation Public Company Limited.'
    },
    'BBL.BK': {
        'name': 'Bangkok Bank Public Company Limited',
        'address': '333 Silom Road Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 645 5555',
        'website': 'https://www.bangkokbank.com',
        'sector': 'Financial Services',
        'industry': 'Banks—Regional',
        'description': 'Bangkok Bank Public Company Limited provides various commercial banking products and services in Thailand and internationally. The company operates through Domestic Banking, International Banking, Investment Banking, and Others segments. It offers various personal banking products and services, including savings, current, fixed deposit, foreign currency, and other accounts; home and personal loans, as well as loans for pensioners; mutual funds; investments products and services, such as bonds and debentures, as well as agency services; life and non-life bancassurance products; payment, funds transfer, currency exchange and foreign instrument, and SMS services; debit, credit, and prepaid cards; and phone and Internet banking, mobile banking, ATMs, and other services. The company also provides business banking products and services comprising operating accounts; loans for SMEs, international trade, investment banking, and e-guarantee services; securities services, such as custodian, mutual fund supervisor, provident fund registrar, securities registrar, and debenture holders representative services; personal loans for small businesses; payment, collection, and merchant services; digital banking services; and commercial cards. In addition, it offers trade finance, remittances, export and import, project, corporate finance, electronic services, and financial advisory services, as well as liquidity, fund, and asset management services. The company was founded in 1944 and is headquartered in Bangkok, Thailand.'
    },
    'BCH.BK': {
        'name': 'Bangkok Chain Hospital Public Company Limited',
        'address': '44 Moo 4, Chaengwattana Road Pakkred Nonthaburi 11120 Thailand',
        'phone': '66 2 836 9907',
        'website': 'https://www.bangkokchainhospital.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Bangkok Chain Hospital Public Company Limited, together with its subsidiaries, operates private hospitals in Thailand. It offers diagnosis, treatment, prevention, rehabilitation services for heart disease; open heart surgery to provide heart care and clinical treatment by cardiologists; and medical supports. The company also operates diagnostic imaging center; eye center that provide a full range of eye examination, treatment, and surgery services; and cancer center that offers services ranging from screening, diagnosis, and chemotherapy. In, addition it operates fertility center for infertility treatment, as well as diabetic wound treatment center. The company was founded in 1984 and is based in Nonthaburi, Thailand.'
    },
    'BCP.BK': {
        'name': 'Bangchak Corporation Public Company Limited',
        'address': '2098 M Tower Building 8th Floor Sukhumvit Road Phra Kanong Tai, Phra Kanong Bangkok 10260 Thailand',
        'phone': '66 2 335 8888',
        'website': 'https://www.bangchak.co.th',
        'sector': 'Energy',
        'industry': 'Oil & Gas Refining & Marketing',
        'description': 'Bangchak Corporation Public Company Limited, an energy company, engages in the refining and marketing of petroleum products in Thailand, Singapore, Norway, Korea, and internationally. It operates through six segments: Refinery and Oil Trading, Marketing, Electricity, Bio-Based Product, Natural Resource, and Others. The company explores and produces petroleum products; produces biodiesel, ethanol, and biogas; produces and distributes electricity from solar cells; invests in alternative energy business; manufactures and distributes biofuel products; operates service stations; and mines lithium. It serves consumers in various sectors comprising transportation, aviation, shipping, construction, industrial, and agriculture. The company was formerly known as The Bangchak Petroleum Public Company Limited and changed its name to Bangchak Corporation Public Company Limited in April 2017. Bangchak Corporation Public Company Limited was founded in 1984 and is headquartered in Bangkok, Thailand.'
    },
    'BCPG.BK': {
        'name': 'BCPG Public Company Limited',
        'address': '2098 M Tower Building 12th Floor Sukhumvit Road Phra Khanong Tai, Phra Khanong Bangkok 10260 Thailand',
        'phone': '66 2 335 8999',
        'website': 'https://www.bcpggroup.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'CPG Public Company Limited, together with its subsidiaries, engages in the production and distribution of electric power from renewable resources in Thailand, Japan, Taiwan, Laos, Vietnam, Indonesia, and the Philippines. It generates electricity from solar, wind, and hydro power. The company was founded in 2015 and is headquartered in Bangkok, Thailand. BCPG Public Company Limited operates as a subsidiary of Bangchak Corporation Public Company Limited.'
    },
    'BCT.BK': {
        'name': 'Birla Carbon (Thailand) Public Company Limited',
        'address': '888/122, 188/128, Mahatun Plaza Bldg. 12th Floor Ploenchit Road Lumpini, Pratumwan Bangkok 10330 Thailand',
        'phone': '66 2 253 6745',
        'website': 'https://www.birlacarbon.com/investor-relations/',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'Birla Carbon (Thailand) Public Company Limited is involved in the manufacture and sale of carbon black for rubber and specialty applications. The company sells its products under the Birla Carbon brand name. It has operations in Thailand, Japan, Indonesia, Vietnam, Malaysia, and internationally. The company was formerly known as Thai Carbon Black Public Company Limited and changed its name to Birla Carbon (Thailand) Public Company Limited in July 2018. Birla Carbon (Thailand) Public Company Limited was incorporated in 1978 and is headquartered in Bangkok, Thailand.'
    },
    'BDMS.BK': {
        'name': 'Bangkok Dusit Medical Services Public Company Limited',
        'address': '2, Soi Soonvijai 7 New Petchburi Road Bang Kapi Huaykwang Bangkok 10310 Thailand',
        'phone': '66 2 310 3000',
        'website': 'https://www.bdms.co.th',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Bangkok Dusit Medical Services Public Company Limited, together with its subsidiaries, operates hospitals in Thailand and internationally. The company owns and manages 6 hospital groups, including Bangkok Hospital Group, Samitivej Hospital Group, BNH Hospital, Phyathai Hospital Group, Paolo Hospital Group, and Royal Hospital Group. It operates holistic clinical wellness. In addition, the company operates hotels and restaurant; sells health and cosmetic products; provides accounting, health insurance, laboratory services, investment, information technology, training, skin and aesthetics telemedicine, genome sequencing, insurance brokerage, air transportation, facility management, and property management services, as well as asset management services; and manufactures and distributes medicine and pharmaceutical products and medical equipment. Further, it is involved in the e-commerce and real estate business. Bangkok Dusit Medical Services Public Company Limited was incorporated in 1969 and is based in Bangkok, Thailand.'
    },
    'BEAUTY.BK': {
        'name': 'Beauty Community Public Company Limited',
        'address': '50/1-3 Soi Nuanchan 34 nuanchan Road, Nuanchan Subdistrict, Buengkum District Bangkok 10230',
        'phone': '66 2 946 0700',
        'website': 'https://www.beautycommunity.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Household & Personal Products',
        'description': 'Beauty Community Public Company Limited engages in the retail sale and distribution of cosmetic and skincare products under the Beauty Buffet, Beauty Cottage, Beauty Market, Beauty Plaza, and Made In Nature names in Thailand and internationally. It provides make up, facial care, body care, hair care, and beauty drink and food supplement products, as well as beauty accessories. The company sells its products through retail and non-retail channels, as well as franchises; and e-commerce channel. It operates through 21 branches in Indonesia, 2 branches in Vietnam, 3 branches in the Philippines, 29 branches in India, 14 branches in Myanmar, 4 branches in Malaysia, 5 branches in Laos, 1 branch in Brunei, and 1 branch in Japan, as well as 34,000 points of sale in the Peoples Republic of China. The company was formerly known as Monopolitan Co., Ltd. and changed its name to Beauty Community Public Company Limited in July 2012. Beauty Community Public Company Limited was founded in 1998 and is headquartered in Bangkok, Thailand.'
    },
    'BEC.BK': {
        'name': 'BEC World Public Company Limited',
        'address': '3199 Maleenont Tower Floor 2, 3, 4, 9, 10, 30-34 Rama 4 Road Klongton, Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 262 3333',
        'website': 'https://www.becworld.com',
        'sector': 'Communication Services',
        'industry': 'Broadcasting',
        'description': 'BEC World Public Company Limited, together with its subsidiaries, engages in the entertainment and recreation business in Thailand and internationally. The company provides content on various platforms, such as television and digital platform, global content licensing, and supporting business; provides and produces TV and news programs; and sells airtime for advertising. It also provides information technology and maintenance services; retails computer accessories; and invests in digital platform businesses. In addition, the company operates digital TV business. BEC World Public Company Limited was founded in 1967 and is headquartered in Bangkok, Thailand.'
    },
    'BEM.BK': {
        'name': 'Bangkok Expressway and Metro Public Company Limited',
        'address': '587 Sutthisarn Road Ratchadaphisek Subdistrict Dindaeng District Bangkok 10400 Thailand',
        'phone': '66 2 641 4611',
        'website': 'https://www.bemplc.co.th',
        'sector': 'Industrials',
        'industry': 'Railroads',
        'description': 'Bangkok Expressway and Metro Public Company Limited, together with its subsidiaries, engages in the construction and management of expressways and rail mass rapid transit system projects in Thailand. The company operates through four segments: Expressway Business, Rail Business, Commercial Development Business, and Others. It undertakes commercial developments relating to the expressway and operates metro services. The company also operates and manages the Si Rat Expressway, the Si Rat - Outer Ring Road Expressway, and the Udon Ratthaya Expressway, as well as the MRT Blue Line and MRT Chalong Ratchadham Line projects. In addition, it engages in the rental of retail space, and provision of advertising services, as well as offers telecommunication services for underground train stations and on expressways. Bangkok Expressway and Metro Public Company Limited was founded in 1998 and is headquartered in Bangkok, Thailand.'
    },
    'BEYOND.BK': {
        'name': 'Bound and Beyond Public Company Limited',
        'address': 'No. 130–132 Sindhorn Tower 2 15th Floor Wireless Road Lumpini Sub-District, Pathum Wan Distric Bangkok 10330 Thailand',
        'phone': '66 2 028 2626',
        'website': 'https://www.boundandbeyond.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'Bound and Beyond Public Company Limited, together with its subsidiaries, owns and operates hotels in Thailand. It owns and manages the Four Seasons Hotel Bangkok and Capella Bangkok. The company was formerly known as Padaeng Industry Public Company Limited and changed its name to Bound and Beyond Public Company Limited in October 2021. Bound and Beyond Public Company Limited was founded in 1981 and is headquartered in Bangkok, Thailand.'
    },
    'BGC.BK': {
        'name': 'BG Container Glass Public Company Limited',
        'address': '47/1 Moo 2, Rangsit-Nakornnayok Road Km.7 Buengyeetho Pathumthani Thanyaburi 12130 Thailand',
        'phone': '66 2 834 7000',
        'website': 'https://www.bgc.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Packaging & Containers',
        'description': 'BG Container Glass Public Company Limited, together with its subsidiaries, manufactures and distributes glass bottles and other packaging in Thailand and internationally. It offers containers, plastic bottles and caps, plastic crates, wrap and shrink films, corrugated boxes and sheets, product trays, and corrugated box separator. The company also generates and distributes electricity from solar power. It serves customers in various industries, such as beverage bottles, alcoholic beverage, food, insecticide and drugs, and others. The company was founded in 1974 and is headquartered in Thanyaburi, Thailand. BG Container Glass Public Company Limited is a subsidiary of Bangkok Glass Public Company Limited.'
    },
    'BGRIM.BK': {
        'name': 'B.Grimm Power Public Company Limited',
        'address': 'Dr. Gerhard Link Building Krungthepkreetha Road Huamark Bangkapi Bangkok 10240 Thailand',
        'phone': '66 2 710 3400',
        'website': 'https://www.bgrimmpower.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Independent Power Producers',
        'description': 'B.Grimm Power Public Company Limited, an energy company, engages in the development, financing, construction, and operation of green-field power plants in Thailand, Laos PDR, Cambodia, the Philippines, The Republic of Korea, and Malaysia. It operates in two segments, Electricity Generating and Other Businesses. The Electricity Generation segment generates and distributes electricity for the government sectors and industrial users. The Other Businesses segment provides maintenance and operating services for power plants. The company generates electricity through co-generation, solar, hydro, wind, hybrid, and waste to energy sources. The company was founded in 1878 and is headquartered in Bangkok, Thailand.'
    },
    'BH.BK': {
        'name': 'Bumrungrad Hospital Public Company Limited',
        'address': '33 Sukhumvit Soi 3 (Nana Nua) Sukhumvit Road Klongtoey Nua Sub District Wattana Distric Bangkok 10110 Thailand',
        'phone': '66 2 066 8888',
        'website': 'https://www.bumrungrad.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Bumrungrad Hospital Public Company Limited owns and operates healthcare-related entities in Thailand and internationally. It operates allergy centers, arrhythmia centers, behavioral health centers, breast centers, breastfeeding clinics, home service centers, clinics yangon, COVID-19 recovery clinics, heart valve centers, robotic surgery centers, spine institute, rehabilitation centers, childrens (pediatrics) centers, colorectal surgery centers, complex coronary artery intervention centers, comprehensive sleep clinics, cornea transplant centers, dental centers, diagnostic centers, diagnostic radiology and nuclear medicine, dialysis centers, digestive disease centers, ear, nose and throat centers, emergency centers, endocrinology, diabetes and clinical nutrition centers, esperance, expatriate liaison centers, eye centers, fertility centers and IVF clinics, gastrointestinal motility centers, health screening centers, hearing and balance clinics, heart institute, holistic wound care centers, horizon regional cancer centers, hyperbaric oxygen therapy centers, intensive care unit, and medical clinics. The company also operates memory clinics, nephrology centers, neurocritical care, neuroscience centers, new life healthy aging clinics, nutrition services, orthopedic centers, parkinsons disease and movement disorders clinics, perinatal centers, pharmacy services, plastic (cosmetic) surgery centers, preventive genomics and integrative medicine, pride clinics, pulmonary (lung) centers, refractive surgery centers, robotic scoliosis centers, skin (dermatology) centers, sports medicine & joint centers, surgery clinics and surgery centers, travel medicine centers, urology centers, vaccine clinics, scientific wellness centers, vitallife skin and aesthetic centers, and womens centers. The company was founded in 1980 and is headquartered in Bangkok, Thailand.'
    },
    'BIG.BK': {
        'name': 'Big Camera Corporation Public Company Limited',
        'address': '115, 115/1 Sawatdikarn 1 Road Nongkheam Subdistrict Nongkheam District Bangkok 10160 Thailand',
        'phone': '66 2 809 9956',
        'website': 'https://www.bigcamera.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Specialty Retail',
        'description': 'Big Camera Corporation Public Company Limited, together with its subsidiaries, distributes cameras and photography-related products in Thailand. The company offers digital cameras, lens, action cameras/360 cameras, VDOs, drones, instant cameras/instant films, camera bags, straps, flashes, gimbal stabilizers, broadcast accessories, tripods, memory cards, filters, printers, binoculars, batteries, and others. It also provides mobile phones, and photography and mobile phone related products; and related services, including photographic processing and photographic equipment repair services, etc. In addition, the company is involved in the printing business. It operates approximately 200 branches. The company was founded in 1997 and is based in Bangkok, Thailand.'
    },
    'BIOTEC.BK': {
        'name': 'Bio Green Energy Tech Public Company Limited',
        'address': '153 Mano Tower Soi Sukumvit 39 Sukumvit Road Klongtonnua, Wattana Bangkok 10110 Thailand',
        'phone': '66 2 260 0050',
        'website': 'https://www.jutha.co.th',
        'sector': 'Industrials',
        'industry': 'Marine Shipping',
        'description': 'Bio Green Energy Tech Public Company Limited, together with its subsidiaries, provides marine transportation services in Thailand and internationally. It offers time charter; ship management services, including vessel operation and manning; and semi-liner services. The company also provides marine-related services, such as cargo booking brokerage, sale and purchase of ship brokerage, and ship charter brokerage services. In addition, it is involved in the manufacture and distribution of biodiesel and glycerin products. The company was formerly known as Jutha Maritime Public Company Limited and changed its name to Bio Green Energy Tech Public Company Limited in May 2022. Bio Green Energy Tech Public Company Limited was founded in 1976 and is headquartered in Bangkok, Thailand.'
    },
    'BIZ.BK': {
        'name': 'Business Alignment Public Company Limited',
        'address': '92/45 Sathorn Thani Building 2 16th Floor North Sathorn Road Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 636 6828',
        'website': 'https://www.bizalignment.com',
        'sector': 'Healthcare',
        'industry': 'Medical Devices',
        'description': 'Business Alignment Public Company Limited engages in the distribution and installation of medical equipment and software system for cancer treatment through radiotherapy in Thailand. It is also involved in the construction of building for locating medical equipment; and providing repair and maintenance services for medical equipment. In addition, the company operates cancer specialized hospital. Business Alignment Public Company Limited was incorporated in 2000 and is headquartered in Bangkok, Thailand.'
    },

    # 81-100
    'BJC.BK': {
        'name': 'Berli Jucker Public Company Limited',
        'address': 'Berli Jucker House, 99 Soi Rubia, Sukhumvit 42 Road Phrakanong Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2146 5999',
        'website': 'https://www.bjc.co.th',
        'sector': 'Industrials',
        'industry': 'Conglomerates',
        'description': 'Berli Jucker Public Company Limited manufactures, distributes, and services in the areas of packaging, consumer, healthcare and technical, modern retail supply chain, and other group businesses in Thailand. It designs, manufactures, markets, and distributes glass and plastic packaging products, and aluminum cans. The company is involved in the distribution of personal care products, including Cellox facial tissues and toilet papers, Zilk toilet papers, Maxmo multi-purpose papers, Tasto potato chips, Dozo rice crackers, Party and Campus extruded snacks, Parrot soaps, and Dermapon baby soaps, as well as provides logistics management services, such as warehouse, transportation, customs brokerage, and freight forwarding representative services. In addition, it offers food products comprises snacks, beverages, packaged fruits, and dairy and yogurt products; and non-food products, which includes personal care, household products, stationery and office equipment, and others. Further, the company imports and distributes medicines, medical supplies, cosmeceuticals, pharmaceuticals, food supplements, and health products; medicines for treatment of various diseases such as kidney, hematology, cardiovascular, endocrine system, genitourinary system, skeleton, infection, oncology and tumors, pediatric medicines, and beauty products. It also offers medical devices, such as computed radiography systems, ultrasound systems, digital mammography systems, X-ray systems, 3D medical image processing systems, and laboratory information systems. Additionally, the company engages in bakery, food and nutraceutical, and cosmetic ingredients; industrial chemicals and refrigerants; e-commerce business; consultancy, design, installation, and the after-sales services for cranes and solar rooftop system; and weighing control system. The company was founded in 1882 and is headquartered in Bangkok, Thailand. Berli Jucker Public Company Limited is a subsidiary of TCC Corporation Company Limited.'
    },
    'BJCHI.BK': {
        'name': 'BJC Heavy Industries Public Company Limited',
        'address': 'No. 594 Moo 4 Makhamkoo Sub-district Nikompattana District Rayong 21180 Thailand',
        'phone': '66 3 301 7345',
        'website': 'https://www.bjc1994.com',
        'sector': 'Industrials',
        'industry': 'Metal Fabrication',
        'description': 'BJC Heavy Industries Public Company Limited manufactures and sells fabricated steel and equipment, and provides modularization services in Thailand and internationally. It fabricates steel into various steel structures by cutting, bending, welding, and assembling structural steel, pipes, and components based on client design and specifications; executes large-scale modularization projects; builds steel structures for mines, power plants, and industrial plants; and manufactures a range of precast concrete products, including breakwater and port construction materials, railway sleepers, pre-stressed concrete panels, and large files for use in the construction of harbors, bridges, and railways. The company also provides built-up beams, as well as grating, galvanizing, and post-weld heat treatment services. It serves oil and gas, petrochemical, refining, mining, renewable energy, power, and other industries. BJC Heavy Industries Public Company Limited was incorporated in 1994 and is headquartered in Rayong, Thailand.'
    },
    'BKD.BK': {
        'name': 'Bangkok Dec-Con Public Company Limited',
        'address': '52/3 Moo 8 Bangbuathong-Suphanburi Road, Lahan, Bangbuathong Nonthaburi 11110',
        'phone': '66 2 925 5777',
        'website': 'http://www.bangkokdeccon.com',
        'sector': 'Industrials',
        'industry': 'Specialty Business Services',
        'description': 'The Bangkok Wooden was established in 1985. In 1992, rebranded to Bangkok Dec-Con with a registered capital of 437 million Baht by running the business as the interior design and renovation contractor and furniture manufacturers such as condominiums, hotels, office buildings, department stores, universities, hospitals, and government buildings. The company has a long experience, expertise, and availability of services. Responsible for all aspects of interior design and renovation with the expertise teams to achieve the requirements of our valuable customers. By attention to the detail and process that consideration of the customer satisfaction according to operation policies which are focused on honesty, accuracy and verifiable and safety in the workplace and necessary to be completed as the period with the quality as specified standards and on customer budget requirements. The company has two main target customers, which are state enterprises and private enterprises. We are the first interior construction company to be listed in both MAI, and later on, SET Market of Thailand.'
    },
    'BKI.BK': {
        'name': 'Bangkok Insurance Public Company Limited',
        'address': 'Bangkok Insurance Building No. 25 South Sathon Road Thung Maha Mek Sathon Bangkok 10120 Thailand',
        'phone': '66 2 285 8888',
        'website': 'https://www.bangkokinsurance.com',
        'sector': 'Financial Services',
        'industry': 'Insurance—Property & Casualty',
        'description': 'angkok Insurance Public Company Limited is involved in the non-life insurance business in Thailand. It offers fire, marine and transportation, cargo, motor, travel accident, personal accident, residential and commercial property, health, property, third party liability, business all risks, engineering, and miscellaneous insurance products. The company was incorporated in 1947 and is headquartered in Bangkok, Thailand.'
    },
    'BKKCP.BK': {
        'name': 'Bangkok Commercial Property Fund',
        'address': 'Siam Tower 24th Floor 989 Rama 1 Road Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 659 8888',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Office',
        'description': 'Bangkok Commercial Property Fund specializes in real estate investments. The Fund has invested in freehold right on 1) office and commercial strata title units in Charn Issara Tower and 2) office and commercial strata title units in Charn Issara Tower 2.'
    },
    'BLA.BK': {
        'name': 'Bangkok Life Assurance Public Company Limited',
        'address': '415 Krungthep - Nonthaburi Road Wongsawang Bangsue Bangkok 10800 Thailand',
        'phone': '66 2 777 8888',
        'website': 'https://www.bangkoklife.com',
        'sector': 'Financial Services',
        'industry': 'Insurance—Life',
        'description': 'Bangkok Life Assurance Public Company Limited, together with its subsidiaries, provides life insurance services to individuals and corporates in Thailand. Its life insurance products include protection, savings, education, pension, accident plans, total permanent disability, and health and critical illness products. The company also provides general insurance products comprise personal insurance and business all risks insurance products, including fire, motor, burglary, personal accident, accident and personal health, travel accident, cancer, golfers indemnity, home multicover, medical malpractice liability, business interruption, marine, hull, workmens compensation, money, contractors plant and equipment, contractors all risks, erection all risks, boiler and pressure vessel, electronic equipment, industrial all risks, public liability, neon-sign, plate glass, fidelity guarantee, group accident and health, and shop multicover insurance products. In addition, it offers bancassurance products; and equity, long term equity, mixed, foreign investment, fixed income, money market, fixed income, and retirement mutual funds. Bangkok Life Assurance Public Company Limited was founded in 1951 and is headquartered in Bangkok, Thailand.'
    },
    'BLAND.BK': {
        'name': 'Bangkok Land Public Company Limited',
        'address': 'New Geneva Building 47/569-576 Moo 3, 10th Floor Popular 3 Road, Tambol Bannmai Amphur Pakkred Nonthaburi 11120 Thailand',
        'phone': '66 2 504 4949',
        'website': 'https://www.bangkokland.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Diversified',
        'description': 'Bangkok Land Public Company Limited, together with its subsidiaries, engages in the real estate development, exhibition and convention, food and beverage, and hotel investment businesses in Thailand. The company develops, rents, and sells residential housings and commercial properties, including single houses, townhouses, condominiums, shophouses, high rise office buildings, shopping complex, community, and retail malls; operates hotel and various restaurants, as well as catering facilities; and operates retail shops, food courts, fresh food market, and car parks. It also provides financing services; project and infrastructure management services; building management and maintenance services; landscaping and waste treatment services; and real estate investment trust management services, as well as issues foreign currency bonds. Bangkok Land Public Company Limited was founded in 1973 and is based in Nonthaburi, Thailand.'
    },
    'BLISS.BK': {
        'name': 'Bliss Intelligence Public Company Limited (Listed company which has possibility to be delisted)',
        'address': 'office No. 96 Chaloem Phrakiat RatchakanThi 9 Road, Pravet, Nongbon Bangkok 10250',
        'phone': 'N/A',
        'website': 'http://www.blisstel.co.th',
        'sector': 'Technology',
        'industry': 'Information Technology Services',
        'description': 'Operating business in information technology, telecommunications and infrastructure. Which provides both software and hardware services'
    },
    'BOFFICE.BK': {
        'name': 'Bhiraj Office Leasehold Real Estate Investment Trust',
        'address': '591 United Business Center II Building 7th floor Sukhumvit Road Khlong Nuea Vadhana 10110 Thailand',
        'phone': '66 2 261 0170',
        'website': 'https://www.bofficereit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'To invest in long-term leasehold right over Bhiraj Tower at EmQuartier office building and ownership of movable properties related with office operation. Leasehold period is approximately 26 years and 9 months counted from register date. To invest in long-term leasehold right over Bhiraj Tower at BITEC office building and ownership of movable properties related with office operation. Leasehold period is 30 years counted from register date .'
    },
    'BPP.BK': {
        'name': 'Banpu Power Public Company Limited',
        'address': '1550 Thanapoom Tower 26th Floor New Petchburi Road Makkasan, Ratchathewi Bangkok 10400 Thailand',
        'phone': '66 2 007 6000',
        'website': 'https://www.banpupower.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Independent Power Producers',
        'description': 'Banpu Power Public Company Limited engages in thermal and renewable power business in Thailand and internationally. It produces and sells power using solar, wind, coal, and natural gas. The company is also involved in the production and sale of steam; and provision of solar rooftops, electric vehicles, energy storage, and energy management systems. It owns and operates 42 power plants and projects. The company was founded in 1996 and is headquartered in Bangkok, Thailand. Banpu Power Public Company Limited is a subsidiary of Banpu Public Company Limited.'
    },
    'BR.BK': {
        'name': 'Bangkok Ranch Public Company Limited',
        'address': '18/1 Moo 12 Langwatbangpleeyainai Rd Bangphliyai Bang Phli 10540 Thailand',
        'phone': '66 2 337 3280',
        'website': 'https://investor.bangkokranch.com',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Bangkok Ranch Public Company Limited produces and supplies duck meat products in Thailand and internationally. The company also offers processed foods and by-products. In addition, it provides animal feed; and operates duck farms, hatcheries, feed mills, and distribution centers. Further, the company engages in the duck slaughtering and duck meat trading businesses. Bangkok Ranch Public Company Limited was founded in 1984 and is headquartered in Bang Phli, Thailand.'
    },
    'BRI.BK': {
        'name': 'Britania Public Company Limite',
        'address': '4345 Bhiraj Tower, 21st Floor, BITEC Bangna, Sukhumvit Road, Bangna, Bangna Bangkok 10260',
        'phone': '66 2 161 3000',
        'website': 'https://www.britania.co.th/',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Britania Public Company Limited engages in residential property development business in Thailand. It develops detached and semidetached houses, townhomes, townhouses, and other properties under four brand names, including Belgravia, Grand Britania, Britania, and Brighton. The company was formerly known as Origin House Company Limited. The company was incorporated in 2016 and is based in Samut Prakan, Thailand. Britania Public Company Limited is a subsidiary of Origin Property Public Company Limited.'
    },
    'BROCK.BK': {
        'name': 'Baan Rock Garden Public Company Limited',
        'address': '601 Soi Ramkhamhaeng 39, Pracha-Uthit Road Wang Thonglang Bangkok 10310 Thailand',
        'phone': '66 2 934 7000',
        'website': 'https://www.rockgarden.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Baan Rock Garden Public Company Limited engages in the real estate development business in Thailand. It develops and sells townhouses, single detached houses, and commercial buildings under the Baan Rock Garden brand. The company was formerly known as Chucheep South Group, Co., Ltd. Baan Rock Garden Public Company Limited was founded in 1990 and is headquartered in Bangkok, Thailand.'
    },
    'BRR.BK': {
        'name': 'Buriram Sugar Public Company Limited',
        'address': 'No. 237 Moo 2 Baan Sao-Ae Tambol Hin Lek Fai Amphur Kumueug Buriram 31190 Thailand',
        'phone': '66 4 466 6592',
        'website': 'https://www.buriramsugar.com',
        'sector': 'Consumer Defensive',
        'industry': 'Confectioners',
        'description': 'Buriram Sugar Public Company Limited, together with its subsidiaries, manufactures and distributes sugar and molasses in Thailand and internationally. It operates through Sugar and Molasses Business, Trading Agriculture Products, Electricity and Steam Generation and Distribution, and Others segments. The company offers refined, brown, white, cane, and raw sugar; bagasse; and filter cakes. It is also involved in trading of agricultural products; generation and distribution of electricity using biomass; and production and distribution of organic and organic chemical fertilizers using filter cakes, as well as provision of research and development services to improve the efficiency of sugarcane farming and nourishment. In addition, the company provides logistics services, which consists of land and water product transportation services, both domestic and international. Further, it is involved in the manufacture and distribution of packaging products, which are made from bagasse; and steam generation and distribution activities, as well as invests wood pellet business. The company was incorporated in 1963 and is headquartered in Buriram, Thailand. Buriram Sugar Public Company Limited operates as a subsidiary of Buriram Capital Co., Ltd.'
    },
    'BRRGIF.BK': {
        'name': 'Buriram Sugar Group Power Plant Infrastructure Fund',
        'address': '175 Sathorn City Tower, 7th , 21st and 26th Floor, South Sathorn Road, Thung Mahamek Sub-district, Sathorn District Bangkok 10120',
        'phone': '66 2 674 6488',
        'website': 'https://brrgif.com/home.html',
        'sector': 'Utilities',
        'industry': 'Utilities—Independent Power Producers',
        'description': 'BRRGIF is to invest in the right to the Net Revenue by entering into the Net Revenue Purchase and Transfer Agreement of Buriram Energy Co.,Ltd. and Buriram Power Co.,Ltd. , a subsidiary of Buriram Sugar Public Company Limited (BRR), for the period of approximately 18 years until the Expiry Date, which is April 6, 2035 .'
    },
    'BSBM.BK': {
        'name': 'Bangsaphan Barmill Public Company Limited',
        'address': '28/1 Prapawit Building 8th Floor Surasak Road Kwang Silom, Khet Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 630 0590',
        'website': 'https://www.bsbm.co.th',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'Bangsaphan Barmill Public Company Limited manufactures and distributes deformed and round steel bars for concrete building structures in Thailand. The company was incorporated in 1994 and is based in Bangkok, Thailand.'
    },
    'BTG.BK': {
        'name': 'Betagro Public Company Limited',
        'address': '323 Betagro Tower(North Park) Moo 6, Vibhavadi Rangsit Road Kwaeng Thungsonghong Ket Laksi Bangkok 10210 Thailand',
        'phone': '66 2833 8000',
        'website': 'https://www.betagro.com',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Betagro Public Company Limited manufactures and distributes animal feed and health, and livestock products in Thailand, the Southeast Asia, other Asian countries, and internationally. It operates through nine segments: Agro Business, Export Business, Consumer Food Business, Non-Package Meat Business, Co & By-Products and Other Food Business, Livestock Business, International Business, Pet Business, and Others. The company produces and distributes livestock and aquaculture feed under the Betagro, Balance, and MASTER brands; animal pharmaceutical, supplements, and hygienic products under the Better Pharma and Nexgen brand names; packaged fresh and frozen chicken meat, pork meat, eggs, and processed food and meat under the BETAGRO, S-Pure, and ITOHAM brands; poultry meat, pork meat, egg, processed food, processed meat, and other food products; fresh pork and poultry products; and pet food products, including snacks for dogs and cats, as well as pet care products, such as medicine, supplementary food, and shampoo. It also engages in the sale and provision of farm equipment installation service comprising ventilation system, feeding system, water system, layer cage system, cooling pads, heating system, composter system, and silometric sensor; provision of laboratory testing services; sale of leftover animal parts from the slaughterhouse processes; rearing and sale of live chickens, pigs and fish to farms and industrial processors; swine and egg production; and operation of feed mill, grandparent and parent pig farms, fattening farms, layer farm, fattening pig contract farms, broiler contract farms with local farmers, poultry farms, Betagro shops, and slaughterhouse; and swine breeder trading. The company was founded in 1967 and is based in Bangkok, Thailand.'
    },
    'BTNC.BK': {
        'name': 'Boutique Newcity Public Company Limited',
        'address': '1112/53-75 Soi Sukhumvit 48 (Piyavat) Sukhumvit Road Phra Khanong Khlong Toei Bangkok 10110 Thailand',
        'phone': '66 2 391 3320',
        'website': 'https://www.btnc.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Apparel Retail',
        'description': 'Boutique Newcity Public Company Limited, manufactures and distributes womens fashion products in Thailand. It operates through four segments: Domestic Retail, Online, Foreign Retail, and Uniform. The company offers its products under the Uniform Specializer, GSP, C&D, Jousse, LOF-FI-CIEL, FLIP, and Guy Laroche brands. The company also operates AMAZE, a multi-brand store. The company was founded in 1974 and is headquartered in Bangkok, Thailand.'
    },
    'BTS.BK': {
        'name': 'BTS Group Holdings Public Company Limited',
        'address': 'TST Tower 21 Soi Choei Phuang 15th Floor Viphavadi-Rangsit Road Chomphon, Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 273 8611',
        'website': 'https://www.btsgroup.co.th',
        'sector': 'Industrials',
        'industry': 'Railroads',
        'description': 'BTS Group Holdings Public Company Limited, together with its subsidiaries, engages in mass transit, property, media, and service businesses in Thailand. The company operates in three segments: Move, Mix, and Match. It operates and maintains BTS Sky Train system; constructs, operates, installs, and maintains electric rails; and train procurement services and other related services, as well as provides bus rapid transit services. The company also offers marketing solutions through offline and online media; advertising, digital, and sales services; system installation and integration services; and insurance brokerage services for offline and online distribution channels, as well as services related to rabbit card. In addition, the company offers investment in various businesses, such as restaurant operations, construction services, golf course services, and other services businesses. Further, it invests in the securities of other companies; provides architecture and engineering work consultancy services; and manages food and beverage businesses; provides electronic payment, electronic money, and bill payment services; develops software and provides technology and system integration services; and offers CRM loyalty program and coupon kiosks. The company was formerly known as Tanayong Public Company Limited and changed its name to BTS Group Holdings Public Company Limited in May 2010. BTS Group Holdings Public Company Limited was founded in 1968 and is based in Bangkok, Thailand.'
    },
    'BTSGIF.BK': {
        'name': 'BTS Rail Mass Transit Growth Infrastructure Fund',
        'address': '175 Sathorn City Tower 7th, 21st, and 26th Floor South Sathorn Road Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 674 6488',
        'website': 'http://www.btsgif.com',
        'sector': 'Industrials',
        'industry': 'Railroads',
        'description': 'The Fund has invested in the Sale Revenue to be generated from the operation of the Core BTS SkyTrain System (being the original lines of the BTS SkyTrain System covering 23.5 kilometres, consisting of the 17 kilometre Sukhumvit line from Mo-Chit to On-Nut, and the 6.5 kilometre Silom line from National Stadium to Taksin Bridge) pursuant to the Concession Agreement, from the Closing Date until the Concession Expiry Date, which is December 4 2029,the term of the Concession Agreement of which is 30 years.'
    },

    # 101-120
    'BUI.BK': {
        'name': 'Bangkok Union Insurance Public Company Limited',
        'address': '175–177 Bangkok Union Insurance Bldg Surawong Road Suriyawong Sub-District Bangrak District Bangkok 10500 Thailand',
        'phone': '66 2 233 6920',
        'website': 'https://www.bui.co.th',
        'sector': 'Financial Services',
        'industry': 'Insurance—Property & Casualty',
        'description': 'Bangkok Union Insurance Public Company Limited provides non-life insurance products for retail and corporate customers in Thailand. The company underwrites fire, marine and transportation, and motor insurance, as well as reinsurance products. It also underwrites miscellaneous insurance comprising property all risks, health, personal accident, public liability, plat glass, golfers indemnity, burglary, money, and fidelity guarantee insurance products; and engineer liability policies, including contract work, machinery, boiler, contractors equipment, and electronic equipment insurance products. In addition, it is also involved in the rental of office space. The company was incorporated in 1929 and is headquartered in Bangkok, Thailand.'
    },
    'BWG.BK': {
        'name': 'Better World Green Public Company Limited',
        'address': '488 Soi Ladprao 130 (Mahatthai 2) Ladprao Road Klongchan Sub-District Bangkapi District Bangkok 10240 Thailand',
        'phone': '66 2 012 7888',
        'website': 'https://www.bwg.co.th',
        'sector': 'Industrials',
        'industry': 'Waste Management',
        'description': 'Better World Green Public Company Limited, together with its subsidiaries, engages in integrated waste treatment and disposal of the industrial waste in Thailand. The company offers landfill disposal systems; chemical and biological wastewater treatment services for industrial factories; and solid waste-to-renewable energy systems. It also provides burning systems; analysis systems for laboratory operations; and waste management consulting services in the areas of waste management and disposal methods, transportation and collection system, wastewater treatment, waste manifest system, and social activities. In addition, the company offers construction, transportation and agency, and incinerating services; and acts as a broker or agent for the treatment of industrial waste, and hazardous or non-hazardous waste. Further, it engages in the generation and distribution of electricity; property development activities; and purchase and sale of real estate properties for industrial plants or commercial business. The company was founded in 1997 and is headquartered in Bangkok, Thailand.'
    },
    'B-WORK.BK': {
        'name': 'Bualuang Office Leasehold Real Estate Investment Trust',
        'address': '175 Sathorn City Tower, 7th, 21st and 26th Floor, South Sathorn Road, Sathorn Bangkok 10120',
        'phone': '66 2 674 6488',
        'website': 'http://www.bworkreit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'To invest in 30 years leasehold right of True Tower 1 and True Tower 2 office buildings'
    },
    'BYD.BK': {
        'name': 'Beyond Securities Public Company Limited',
        'address': '46/7 Rungrojthanakul 11th,12th Floor Ratchadaphisek Road Huai Khwang Bangkok 10310 Thailand',
        'phone': '66 2 820 0100',
        'website': 'https://www.beyondsecurities.co.th',
        'sector': 'Financial Services',
        'industry': 'Capital Markets',
        'description': 'Beyond Securities Public Company Limited provides securities brokerage services to individual and institutional investors in Thailand. The company offers securities brokerage services through securities trading accounts comprising cash, cash balance, and credit balance accounts; derivatives brokerage; internet trading; investment banking, including financial advisory, mergers and acquisitions, initial public offerings, debt financing and restructuring, real estate investment trust/infrastructure fund, corporate structuring, and capital restructuring; mutual funds; securities borrowing and lending; private funds; and fixed income products. The company was formerly known as AEC Securities Public Company Limited and changed its name to Beyond Securities Public Company Limited in August 2021. Beyond Securities Public Company Limited was incorporated in 1971 and is based in Bangkok, Thailand.'
    },
    'CBG.BK': {
        'name': 'Carabao Group Public Company Limited',
        'address': '393 Silom Building 7th - 10th floor 393, Silom Road Silom, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 636 6111',
        'website': 'https://www.carabaogroup.com',
        'sector': 'Consumer Defensive',
        'industry': 'Beverages—Non-Alcoholic',
        'description': 'Carabao Group Public Company Limited, through its subsidiaries, manufactures, markets, distributes, and sells beverages in Thailand and internationally. Its products primarily include carbonated and non-carbonated energy drinks, drinking water, ready-to-drink coffee, instant powder 3-in-1 coffee, vitamin C drinks, and sport drinks under the Carabao, Carabao Sport, and Woody C+ Lock brands. The company also manufactures and distributes bottles and glass products and aluminum cans; and packaging products for energy drinks and other beverages. In addition, it is involved in the investment, data management, and trading activities. Carabao Group Public Company Limited was founded in 2001 and is headquartered in Bangkok, Thailand.'
    },
    'CCET.BK': {
        'name': 'Cal-Comp Electronics (Thailand) Public Company Limited',
        'address': 'CTI Tower 191/54, 191/57, 18th Floor Rachadapisek Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 261 5033',
        'website': 'https://www.calcomp.co.th',
        'sector': 'Technology',
        'industry': 'Computer Hardware',
        'description': 'Cal-Comp Electronics (Thailand) Public Company Limited, together with its subsidiaries, manufactures electronic products worldwide. The company offers computers and computer peripherals, such as mainboards, external hard disk drives, NAS and PCBA for hard disk drives, USB pen drives, storage server PCBA, and assembly products, as well as ink-jet printers, laser printers, multi-function printers, dot-matrix printers, and large format printers; telecommunication products, including set-top boxes and their component parts, and Bluetooth headsets; and smart appliances that comprise smart TV, mirrors, and POS machines, as well as digital camera PCBA and media players. It also provides consumer electronics, which include facial cleaning brushes, iron brushes, cordless airbrush makeup kits, displays, electronic keyboards, hubs, rovers, and calculators; intelligent warehouse, machinery, and robotics, as well as smart factory products; smart beauty products comprising facial moisturizing sprays, facial cleaning brushes, facial massagers, mirror, smart body scale, and electric toothbrushes; and healthcare and wearable devices. In addition, the company offers semiconductor design and packaging services; and robotic applications for edutainment and smart service products. Cal-Comp Electronics (Thailand) Public Company Limited was founded in 1989 and is headquartered in Bangkok, Thailand.'
    },
    'CCP.BK': {
        'name': 'Chonburi Concrete Product Public Company Limited',
        'address': '39/1 Moo 1 Sukhumvit Road Tambol Huaykapi Amphur Muang Chonburi 2000 Thailand',
        'phone': '66 61 409 8877',
        'website': 'https://www.ccp.co.th',
        'sector': 'Basic Materials',
        'industry': 'Building Materials',
        'description': 'Chonburi Concrete Product Public Company Limited manufactures and distributes concrete products in Thailand. The company offers ready-mixed concrete and precast concrete for work system structure decoration. It also distributes construction materials and home decoration equipment; and manufactures and distributes autoclaved aerated concrete blocks and concrete blocks, as well as provides real estate leasing services. Chonburi Concrete Product Public Company Limited was founded in 1983 and is based in Chonburi, Thailand.'
    },
    'CEN.BK': {
        'name': 'Capital Engineering Network Public Company Limited',
        'address': '1011, Supalai Grand Tower 17th Floor Rama 3 Road Chongnonsi, Yannawa Bangkok 10120 Thailand',
        'phone': '66 2 049 1041',
        'website': 'https://www.cenplc.com',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'Capital Engineering Network Public Company Limited, through its subsidiaries, manufactures and distributes prestressed concrete wires and strand wires, and welding wires in Thailand. It also manufactures and distributes industrial equipment, transmission line towers, and telecommunication towers, as well as electricity and heat energy; and distributes substation steel structures. In addition, the company engages in the construction and tunnel excavation, trading and investing, and fabrication construction and design activities; distributes fuel for power plants; and operates biogas power plants. Further, it manufactures and sells woodchips; manages human resource functions; and leases a telecommunication tower. The company was formerly known as Eastern Wire Public Company Limited and changed its name to Capital Engineering Network Public Company Limited in May 2009. Capital Engineering Network Public Company Limited was founded in 1988 and is based in Bangkok, Thailand.'
    },
    'CENTEL.BK': {
        'name': 'Central Plaza Hotel Public Company Limited',
        'address': '1695 Phaholyothin Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 541 1234',
        'website': 'https://www.centarahotelsresorts.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Resorts & Casinos',
        'description': 'Central Plaza Hotel Public Company Limited, together with its subsidiaries, engages in the hotel business in Thailand and internationally. It operates in two segments, Hotel and Related Services Operation; and Food and Ice-Cream. It is also involved in the food and beverage, hotel management, and import and export businesses, as well as operates a spa and learning centre. The company was founded in 1980 and is based in Bangkok, Thailand.'
    },
    'CFRESH.BK': {
        'name': 'Seafresh Industry Public Company Limited',
        'address': '402 Moo 8 Chumphon-Paknam Road Paknam Mueang Chumphon 86000 Thailand',
        'phone': '66 2 637 8888',
        'website': 'https://www.seafresh.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Seafresh Industry Public Company Limited, together with its subsidiaries, engages in the manufacture and distribution of frozen raw shrimp, processed shrimp, vegetable and fruit, and others seafood products in Thailand and internationally. It provides raw, cooked, sushi, and value added shrimp products, as well as shrimp powder and peeled head shrimp products. The company offers its products under the Seafresh, Sea Angel, GO-GO, Thai Chia, Phoenix, C Angel, and Ultra brands. In addition, the company provides managerial, technical, supporting, and financial management services; sale of chilled seafood products; and develops, produce, and supply aqua feed solutions for aquaculture industry. Further, it offers project management and support services; integrated shrimp production facilities; retail and food services of seafood; produce and sell animal feed and nutrition; and operates seafood business, primarily offers warm water prawns. The company was founded in 1982 and is headquartered in Mueang Chumphon, Thailand.'
    },
    'CGD.BK': {
        'name': 'Country Group Development Public Company Limited',
        'address': 'No. 898 Ploenchit Tower 20th floor Ploenchit Road Lumpini, Pathum Wan Bangkok 10330 Thailand',
        'phone': '66 2 658 7888',
        'website': 'https://www.cgd.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Country Group Development Public Company Limited, together with its subsidiaries, engages in the real estate development business in Thailand and internationally. The company trades, rents, and operates real estate properties; wholesales equipment and furniture used in construction; and manages real estate properties. It also engages in the construction business. The company was formerly known as Dragon One Public Company Limited and changed its name to Country Group Development Public Company Limited in May 2010. Country Group Development Public Company Limited was incorporated in 1995 and is headquartered in Bangkok, Thailand.'
    },
    'CGH.BK': {
        'name': 'Country Group Holdings Public Company Limited',
        'address': '132, Sindhorn Tower 3 20th Floor Wireless Road Lumpini, Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 256 7999',
        'website': 'https://www.cgholdings.co.th',
        'sector': 'Financial Services',
        'industry': 'Capital Markets',
        'description': 'Country Group Holdings Public Company Limited, through its subsidiaries, primarily engages in the securities business in Thailand. It operates through three segments: Securities and Derivatives Brokerage, Investment Banking, and Securities Trading. The company offers securities brokerage, securities trading, securities underwriting, investment advisory, mutual fund management, private fund management, stock borrowing and lending, and venture capital management services. It is also involved in the derivatives brokerage, dealer, and advisor activities; and investment manager of derivative product. The company was incorporated in 2014 and is based in Bangkok, Thailand.'
    },
    'CH.BK': {
        'name': 'Chin Huay Public Company Limited',
        'address': 'No. 181 Thakham Road Samae-Dam Subdistrict Bangkhuntien District Bangkok 10150 Thailand',
        'phone': '66 2 416 0708',
        'website': 'https://chinhuay.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Chin Huay Public Company Limited manufactures and distributes canned food, dried fruits, and fried vegetables and fruits. It operates in Thailand, the United States of America, Japan, Canada, Italy, Mauritius, China, Myanmar, India, the Netherlands, and internationally. The company was founded in 1925 and is headquartered in Bangkok, Thailand.'
    },
    'CHARAN.BK': {
        'name': 'Charan Insurance Public Company Limited',
        'address': '408/1 Ratchadapisak Road Samsennok Huaykwang Bangkok 10310 Thailand',
        'phone': '66 2 276 1024',
        'website': 'https://charaninsurance.co.th',
        'sector': 'Financial Services',
        'industry': 'Insurance—Property & Casualty',
        'description': 'Charan Insurance Public Company Limited provides non-life insurance products in Thailand. The company offers fire, marine and transport, motor, personal accident, and miscellaneous insurance products. It also provides motor, compulsory, marine cargo, SME risks, property, engineering, and other insurance products. The company was founded in 1949 and is headquartered in Bangkok, Thailand.'
    },
    'CHASE.BK': {
        'name': 'Chase Asia Public Company Limited',
        'address': '8/9-10 Soi Vibhavadi Rangsit 44 Ladyao Subdistrict Chatuchak District Bangkok 10900 Thailand',
        'phone': '66 2 558 9009',
        'website': 'https://www.chase.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Chase Asia Public Company Limited provides debt collection and financial advisory services in Thailand. The company offers advice on debt resolution planning; debt negotiation, tracking, and debt collection services for financial institutions and companies, including telecommunication; and credit card, home, land, and auto loan provider companies, as well as insurance, hotel, and other microfinance companies. It also provides litigation, letter, and training services. The company was founded in 1998 and is based in Bangkok, Thailand.'
    },
    'CHAYO.BK': {
        'name': 'Chayo Group Public Company Limited',
        'address': '44/499-504 Phahonyothin Road Anusawari Subdistrict Bang Khen District Bangkok 10220 Thailand',
        'phone': '66 2 004 5555',
        'website': 'https://chayo555.com',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Chayo Group Public Company Limited, together with its subsidiaries, invests in and manages non-performing loans. It also provides debt tracking and collection, personal loan, and call center services, as well as product distribution through call center, TV Shopping, and online channels. The company was formerly known as Khien and Clay Company Limited and changed its name to Chayo Group Public Company Limited in December 2015. The company was founded in 1997 and is headquartered in Bangkok, Thailand.'
    },
    'CHG.BK': {
        'name': 'Chularat Hospital Public Company Limited',
        'address': '88/8-9, Teparak Km. 15 Road Tambol Bangpla Amphur Bangplee Samut Prakan 10540 Thailand',
        'phone': '66 2 033 2900',
        'website': 'https://www.chularat.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Chularat Hospital Public Company Limited operates clinics and hospitals in Thailand. It operates through two segments, Hospital Operations and Other Businesses. The company also distributes medical instruments and dietary supplement products. It operates branches of clinics and hospitals. The company was founded in 1986 is headquartered in Samut Prakan, Thailand.'
    },
    'CHOTI.BK': {
        'name': 'Kiang Huat Sea Gull Trading Frozen Food Public Company Limited',
        'address': '4/2 Moo 3, Asia 43 Road Tambol Namom Amphur Namom Songkhla 90310 Thailand',
        'phone': '66 7 422 2333',
        'website': 'https://www.kst-hatyai.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Kiang Huat Sea Gull Trading Frozen Food Public Company Limited, through its subsidiary, Teppitak Seafood Company Limited, manufactures and sells frozen seafood in Thailand, rest of Asia, Europe, and the United States. The company offers various block, semi-IQF, IQF, and vacuum packed items comprising raw and cooked head-on, headless, and peeled shrimps; extended shrimps; cooked tail-on butterfly, breaded, and easy peeled shrimps; and slipper lobster tail and meat. It sells its products under the Sea King, Sea Champion, Eagle, Sea Queen, Sea Flower, and Blue Gulf brands. The company was founded in 1978 and is headquartered in Songkhla, Thailand.'
    },
    'CI.BK': {
        'name': 'Charn Issara Development Public Company Limited',
        'address': '2922/200, Charn Issara Tower 2 10th Floor New Petchburi Road, Bangkapi Sub-Dist. Huaykwang District Bangkok 10310 Thailand',
        'phone': '66 2 308 2020',
        'website': 'https://www.charnissara.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Charn Issara Development Public Company Limited, together with its subsidiaries, primarily engages in real estate development activities in Thailand. The company operates through four segments: Real Estate Development, Lease of Office Condominium Units, Hotel Operations, and Sales of Goods. It develops and sells residential properties, such as single-detached houses, townhomes, condominiums, and luxury villas; operates spas and hotels; sells or leases office condominiums; and provides REIT management services. The company also engages in the dining and entertainment activities. Charn Issara Development Public Company Limited was founded in 1989 and is based in Bangkok, Thailand.'
    },
    'CIMBT.BK': {
        'name': 'CIMB Thai Bank Public Company Limited',
        'address': 'Langsuan Building 44 Langsuan Road Lumpini Patumwan Bangkok 10330 Thailand',
        'phone': '66 2 638 8000',
        'website': 'https://www.cimbthai.com',
        'sector': 'Financial Services',
        'industry': 'Banks—Regional',
        'description': 'CIMB Thai Bank Public Company Limited, together with its subsidiaries, provides various banking and financial products and services to individuals and commercial customers in Thailand. It operates through Consumer Banking and Wholesale Banking segments. The Consumer Banking segment offers consumer sales and distribution, retail financial, and commercial banking and personal financing services. The Wholesale Banking segment provides investment banking services, such as financial advisory, trade securities transactions, and asset management businesses; and corporate lending and deposit taking, transaction banking, and treasury and market services. The company also offers savings, foreign currency, and current accounts, as well as fixed deposits; personal and home loans, and multi-purpose loans; cards; and life and non-life insurance. The company was formerly known as Bank Thai Public Company Limited and changed its name to CIMB Thai Bank Public Company Limited in May 2009. CIMB Thai Bank Public Company Limited was founded in 1949 and is headquartered in Bangkok, Thailand. CIMB Thai Bank Public Company Limited is a subsidiary of CIMB Bank Berhad.'
    },

    # 121-140
    'CITY.BK': {
        'name': 'City Steel Public Company Limited',
        'address': '88/3 Moo 4, Bypass Road Tumbol Nongmaidaeng Amphur Muang Chonburi 20000 Thailand',
        'phone': '66 8 1359 6942',
        'website': 'http://www.citysteelpcl.com',
        'sector': 'Industrials',
        'industry': 'Metal Fabrication',
        'description': 'City Steel Public Company Limited, together with its subsidiaries, primarily engages in the manufacture and sale of metal structures, storage systems and material handling equipment, and fabricated metal parts in Thailand. It also provides steel service center and processing services. The companys storage systems and material handling equipment consist of racking, modular, special, mobile shelving system, pipe rack, shelving, and conveyor systems, as well as mezzanine platform, cabinets and lockers, carts and dollies, pallets, and dock and handling equipment. Further, it sells metal products, industrial materials, and equipment. The company was founded in 1995 and is headquartered in Chonburi, Thailand. City Steel Public Company Limited is a subsidiary of WKP Asset Plus Company Limited.'
    },
    'CIVIL.BK': {
        'name': 'Civil Engineering Public Company Limited',
        'address': '68/12 CEC Building 7th Floor Kampaengpet 6 Road Ladyao, Jatujak Bangkok 10900 Thailand',
        'phone': '66 2 589 8888',
        'website': 'https://www.civilengineering.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'Civil Engineering Public Company Limited provides construction services in Thailand. It constructs highways and roads, high speed and double track rail systems, airports and ports, and water infrastructure and industrial projects, as well as other projects, such as waste ponds and wastewater treatment systems. The company also manufactures and sells reinforced concrete pipes for drainage works; prefabricated hollow concrete bridge sections, reinforced concrete parts, and prefabricated products; concrete products; and asphaltic products, as well as corrugated steel railing products that are used for highway works. In addition, it trades in construction materials; and engages in the investment and real estate development business that covers rental of office buildings. The company was founded in 1966 and is headquartered in Bangkok, Thailand. Civil Engineering Public Company Limited is a subsidiary of Atsavasirisuk Holding Company Limited.'
    },
    'CK.BK': {
        'name': 'CH. Karnchang Public Company Limited',
        'address': '587 Viriyathavorn Building Sutthisarnvinitchai Road Ratchadaphisek Subdistrict Dindaeng District Bangkok 10400 Thailand',
        'phone': '66 2 277 0460',
        'website': 'https://www.ch-karnchang.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'CH. Karnchang Public Company Limited, together with its subsidiaries, provides construction services in Thailand and the Lao Peoples Democratic Republic. It operates through Construction and Related Service; and Investment in Infrastructure Business segments. The companys construction business engages in construction by accepting engagements from government agencies, state enterprises, and private entities in the form of main contractor and sub-contractor. In addition, it invests in infrastructure project development business, which includes transportation, mass rapid transit, water infrastructure, and electric power systems through operate-transfer, build-transfer-operate, build-own-operate, build-own-operate-transfer, etc.; and engages in the sale of construction materials and rents construction. The company was founded in 1972 and is headquartered in Bangkok, Thailand.'
    },
    'CKP.BK': {
        'name': 'CK Power Public Company Limited',
        'address': 'No. 587 Viriyathavorn Buildin 19th Floor Sutthisan Winitchai Road Ratchadaphisek Subdistrict, Dindaeng Sub Bangkok 10400 Thailand',
        'phone': '66 2 691 9720',
        'website': 'https://www.ckpower.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'CK Power Public Company Limited, through its subsidiaries, generates and sells electricity and steam in Thailand. The company operates through three segments: Generation of Electricity from Hydroelectric Power, Generation of Electricity from Solar Power, and Generation of Electricity from Thermal Power. It also operates 2 hydro power plants with a capacity of 1,900 MW; 9 solar power plant with a capacity of 29 MW; and 2 cogeneration power plants with installed capacity of 238 MW. In addition, the company provides consulting and other services related to electricity generating projects. CK Power Public Company Limited was incorporated in 2011 and is based in Bangkok, Thailand.'
    },
    'CM.BK': {
        'name': 'Chiangmai Frozen Foods Public Company Limited',
        'address': '149/34 Soi Anglo Plaza 3rd-4th Floor Surawongse Road Surawongse, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 238 4091',
        'website': 'https://www.cmfrozen.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Chiangmai Frozen Foods Public Company Limited manufactures and exports frozen vegetables in Thailand and internationally. It offers soybeans, green beans, sweet corn, baby corn, carrots, and mixed vegetables. The company offers its products under the Eda, BENAS, and Cornista brands. In addition, it manufactures and distributes fresh fruits, frozen fruits, and freeze-dried fruits and foods. Chiangmai Frozen Foods Public Company Limited was founded in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'CMAN.BK': {
        'name': 'Chememan Public Company Limited',
        'address': '195/11-12 Lake Rajada Office Complex 2 10th-11th Floor Rajadapisek Road Klongtoey District Bangkok 10110 Thailand',
        'phone': '66 2 661 9734',
        'website': 'https://www.chememan.com',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'Chememan Public Company Limited manufactures and distributes mineral lime and chemical products in Thailand. The companys products include quicklime, hydrated lime, and limestone and grinded limestone. Its lime products are used in industrial, agricultural, environmental, and household applications. The company also provides dump and tank trucks transportation services, as well as technical support services. It also exports its products. The company was incorporated in 2003 and is headquartered in Bangkok, Thailand.'
    },
    'CMC.BK': {
        'name': 'Chaoprayamahanakorn Public Company Limited',
        'address': '909/1, CMC Tower 6th Floor, Unit 601-602 Somdejprachaotaksin Road, Dao Khanong Khet Thonburi District Bangkok 10600 Thailand',
        'phone': '66 2 468 9000',
        'website': 'https://www.cmc.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Diversified',
        'description': 'Chaoprayamahanakorn Public Company Limited engages in the residential real estate development activities in Thailand. It is also involved in the real estate rental, construction, hospitality, and mecial equipment and herbal medical supply businesses. The company was founded in 1994 and is based in Bangkok, Thailand.'
    },
    'CMR.BK': {
        'name': 'Chiang Mai Ram Medical Business Public Company Limited',
        'address': '1, Sukkasem Road Nakhon Ping Subdistrict Patan Subdistrict Mueang District Chiang Mai 50300 Thailand',
        'phone': '66 5 213 4777',
        'website': 'https://www.lanna-hospital.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Chiang Mai Ram Medical Business Public Company Limited, together with its subsidiaries, operates a medical care center in Thailand. It offers medical services in the areas of internal medicine, cardiology, general practice, pediatric, orthopedic and general surgery, pediatric surgery, obstetrics-gynecology, radiology, dentistry, anesthetic, ENT, and eye; and operates sub-specialty clinics for urology, neurology, endocrinology, oncology, hematology, plastic surgery, GI tract, and dermatology, as well as infertile and gynecologic oncology clinics. The company also provides dental, X-ray, CT colonoscopy, cardiac catheterization, gynecologic cancer, back pain, physical therapy, operating theatre, laboratory examination, real-time PCR, ambulance, and CRD and health check-up services; and insurance products. It operates a medical care center under the Lanna Hospital name. The company was founded in 1974 and is headquartered in Chiang Mai, Thailand. Chiang Mai Ram Medical Business Public Company Limited is a subsidiary of Vibhavadi Medical Center Public Company Limited.'
    },
    'CNT.BK': {
        'name': 'Christiani & Nielsen (Thai) Public Company Limited',
        'address': '727 La Salle Road Bangna-Tai Subdistrict Bangna Bangkok 10260 Thailand',
        'phone': '66 2 338 8000',
        'website': 'https://www.cn-thai.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'Christiani & Nielsen (Thai) Public Company Limited, together with its subsidiaries, provides construction services for government and private sectors in Thailand, Myanmar, and Cambodia. The company operates in two segments, Construction Services and Sales and Service. It engages in the design and construction of building and civil engineering projects; and design, fabrication, and erection of steel structures, and mechanical and electrical installations. The company also provides services for energy solutions in solar, wind, and other renewable energy sectors; develops renewable energy based power producing facilities; and develops office buildings, residential buildings, and commercial and industry buildings. The company was formerly known as Christiani & Nielsen (Siam) Ltd. and changed its name to Christiani & Nielsen (Thai) Public Company Limited in November 1992. The company was founded in 1904 and is headquartered in Bangkok, Thailand. Christiani & Nielsen (Thai) Public Company Limited is a subsidiary of Globex Corporation Limited.'
    },
    'COM7.BK': {
        'name': 'Com7 Public Company Limited',
        'address': '549/1 Sanphawut Road Bangna Tai Bangkok 10260 Thailand',
        'phone': '66 2 017 7777',
        'website': 'https://www.comseven.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Specialty Retail',
        'description': 'Com7 Public Company Limited, together with its subsidiaries, engages in the retail business of information technology products in Thailand. The companys products include laptop computers, desktop computers, mobiles, phones, tablets, and IT products and accessories. The company also develops computer software; provides repair and other services, as well as training services. In addition, it engages in distribution activities. The company offers products through its retail outlets and bnn.in.th website, as well as apple product repair centers. Com7 Public Company Limited was founded in 2004 and is headquartered in Bangkok, Thailand.'
    },
    'COTTO.BK': {
        'name': 'SCG Ceramics Public Company Limited',
        'address': '1 Siam Cement Road Bangsue Bangkok 10800 Thailand',
        'phone': '66 2 586 3333',
        'website': 'https://www.scgceramics.com',
        'sector': 'Industrials',
        'industry': 'Building Products & Equipment',
        'description': 'SCG Ceramics Public Company Limited manufactures, distributes, sells, and installs ceramic tiles in Thailand and internationally. Its products include ceramic floor and wall tiles. The company offers its ceramic tiles under the COTTO, SOSUCO, and CAMPANA brands. It is also involved in the development of industrial estate; and installation of solar equipment, as well as real estate business. The company was incorporated in 2018 and is headquartered in Bangkok, Thailand. SCG Ceramics Public Company Limited is a subsidiary of SCG Building Materials Co., Ltd.'
    },
    'CPALL.BK': {
        'name': 'CP ALL Public Company Limited',
        'address': '313 C.P. Tower 24th Floor, Silom Road Bangrak District Bangkok 10500 Thailand',
        'phone': '66 2 071 9000',
        'website': 'https://www.cpall.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Grocery Stores',
        'description': 'CP ALL Public Company Limited, together with its subsidiaries, operates and franchises convenience stores under the 7-Eleven name to other retailers primarily in Thailand. It operates through three segments: Wholesale Business, Retail Business, and Management of Rental Spaces in Shopping Centers. The Wholesale Business segment engages in import, export, and distribution of frozen and chilled food with delivery services and focuses on selling consumer products, including fresh food, dry food, and consumer products under Makro brand. Its Retail Business segment is involved in domestic supply chain, distribution system, logistics network, and brand equity businesses. This segment also sells its products under various domestic, international, and small and medium enterprises brands. The companys Management of Rental Spaces in Shopping Centers segment manages buildings and retail spaces in shopping malls. In addition, the company is involved in sale and maintenance of retail equipment; cash and carry, catalog, and e-commerce businesses; marketing and advertising activities; provision of information technology and research and development services, as well as engaged in bill payment collection, life insurance, and non-life insurance broker business. Further, the company offers educational institution, training, business seminar services, as well as healthcare and medical specialists consultation services. The company was formerly known as C.P. Seven Eleven Public Company Limited. CP ALL Public Company Limited was founded in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'CPF.BK': {
        'name': 'Charoen Pokphand Foods Public Company Limited',
        'address': '313 C.P. Tower Silom Road Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 766 8000',
        'website': 'https://www.cpfworldwide.com',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Charoen Pokphand Foods Public Company Limited, together with its subsidiaries, operates in the agro-industrial and integrated food businesses in Thailand and internationally. It operates in two segments, Livestock Business and Aquaculture Business. The company produces and sells swine, chicken, duck, pigs, shrimp, and fish feed; and breeds and farms swine, broiler, layer, duck, and shrimp. It is also involved in the animal feed raw materials distribution, investment and international trading, food products wholesale and retail, property investment, property lease-out, shrimp hatchery, and animal feedmill businesses. In addition, the company produces and distributes elite seeds, pet food, chlortetracycline, aquatic feed, and sea food products; and imports and distributes eggs, processed meat, milk products, and ready meals. Further, it offers economic and trade consulting, management and advisory, financial guarantee, biological waste management, information technology, food research and development, logistics, and financial services. Additionally, the company engages in the operation of food processing plants, hotels and restaurants, slaughterhouses, and training centers; broiler chicken integration business; provision and development of Asian food products; and swine farm construction activities. It provides its products primarily under the CP brand. The company also exports its products. Charoen Pokphand Foods Public Company Limited was incorporated in 1978 and is headquartered in Bangkok, Thailand.'
    },
    'CPH.BK': {
        'name': 'Castle Peak Holdings Public Company Limited',
        'address': 'CPH Tower 9-14th Floor 899 Petchkasem Road Khet Bangkae, Bangkae District Bangkok 10160 Thailand',
        'phone': '66 2 455 0300',
        'website': 'https://www.castlepeak.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Apparel Manufacturing',
        'description': 'Castle Peak Holdings Public Company Limited, together with its subsidiaries, manufactures and exports garments in Thailand. It operates in two segments, Garment Manufacturing, and Development of Real Estate for Sale. The company primarily offers jackets, fashion coats, shorts, pants, skirts, skorts, dressed, pets wear, and outerwear. It exports its garments to the United States, Europe and other countries. The company was founded in 1976 and is headquartered in Bangkok, Thailand.'
    },
    'CPI.BK': {
        'name': 'Chumporn Palm Oil Industry Public Company Limited',
        'address': '296, Moo 2, Phet Kasem Road Tambon Salui Salui Sub District Thasae District Tha Sae 86140 Thailand',
        'phone': '66 7 761 1000',
        'website': 'https://www.cpi-th.com',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Chumporn Palm Oil Industry Public Company Limited, together with its subsidiaries, manufactures and distributes palm oil products in Thailand. It also provides palm seeds and sprouts, palm seedling products, and crude palm oil and crude palm kernel oil; refined bleached deodorized (RBD) palm oil, palm kernel oil, palm olein, and palm stearin; and palm fatty acid distillate, palm kernel fatty acid distillate, and kernel meal for the use in soap, food, and margarine and shortening industries, as well as used as a raw material for animal feed. The company offers oils in PET bottles, tins, and pouches under the LEELA brand, as well as acts as an original equipment manufacturer. In addition, it produces and distributes biodiesel, and electricity from biogas. The company also exports its products. Chumporn Palm Oil Industry Public Company Limited was incorporated in 1979 and is headquartered in Tha Sae, Thailand.'
    },
    'CPL.BK': {
        'name': 'CPL Group Public Company Limited',
        'address': '700 Moo 6 Sukhumvit Road Bang Poo Mai Muang Samutprakran Samut Prakan 10280 Thailand',
        'phone': '66 2 709 5633',
        'website': 'https://www.cpl.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Footwear & Accessories',
        'description': 'CPL Group Public Company Limited manufactures and distributes leather products in Thailand. It offers leather products, which include full grain and suede split leather products comprising nubuck, oil and wax, pigment, sued, and waterproof leather for shoe factories; and aniline and cow splits leather. The company also provides tanning services; and manufactures and distributes personal protective equipment. The company also exports its products to China, Vietnam, Indonesia, India, etc. CPL Group Public Company Limited was founded in 1989 and is headquartered in Samutprakarn, Thailand.'
    },
    'CPN.BK': {
        'name': 'Central Pattana Public Company Limited',
        'address': 'the Offices at CentralWorld 31st Floor 999/9 Rama I Road Patumwan District Bangkok 10330 Thailand',
        'phone': '66 2 667 5555',
        'website': 'https://www.centralpattana.co.th/en',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Diversified',
        'description': 'Central Pattana Public Company Limited invests in, develops, and manages real estate properties in Thailand. It develops and rents shopping centers, office buildings, condominiums, and residential buildings; offers property management consulting and corporate services; and sells land, houses, and condominium units. The company also offers utility services for shopping centers; and sells food and beverages. In addition, the company operates play land, water theme parks, and hotels; manages real estate investment trust, condominium juristic person, and housing estate juristic person; and provides training and personnel development services. Central Pattana Public Company Limited was founded in 1980 and is headquartered in Bangkok, Thailand.'
    },
    'CPNCG.BK': {
        'name': 'CPN Commercial Growth Leasehold Property Fund',
        'address': 'SCB Park Plaza 1 7-8th Floor 18 Ratchadapisek Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 949 1500',
        'website': 'https://www.cpncg.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Diversified',
        'description': 'CPN Commercial Growth Leasehold Property Fund invests in real estate. The fund focuses on prime office buildings in Bangkoks Central Business District.'
    },
    'CPNREIT.BK': {
        'name': 'CPN Retail Growth Leasehold REIT',
        'address': 'No. 999/9 Rama I Road Pathumwan Sub-district Pathumwan District Bangkok 10900 Thailand',
        'phone': '66 2 667 5555',
        'website': 'https://www.cpnreit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Diversified',
        'description': 'CPN Retail Growth Leasehold REIT (CPNREIT) is Thailands largest retail-focused real estate investment trust listed on the Stock Exchange of Thailand (SET). CPNREIT was established from the conversion of CPN Retail Growth Leasehold Property Fund (CPNRF) which was set up and publicly traded on the SET since 2005. Upon conversion on 1 December 2017, CPNREIT acquired all CPNRFs quality portfolio, and invested in a new mix-used project consisting of CentralFestival Pattaya Beach shopping center and Hilton Pattaya. At present, CPNREIT invested in a well-diversified portfolio of 5 shopping centers and 1 hotel across Thailands prime destinations.'
    },
    'CPT.BK': {
        'name': 'CPT Drives and Power Public Company Limited',
        'address': 'No.230/7, Thetsabarnrungruknuer Road Ladyao Jattujak Bangkok 10900 Thailand',
        'phone': '66 2 954 2590',
        'website': 'https://www.cptthailand.com',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'CPT Drives and Power Public Company Limited, together with its subsidiaries, provides electrical power and control systems in Thailand. The company offers drives and automation products, such as DC drives, LV and MV inverters, and starters; PLC, SCADA, and HMI products; speed feedback devices; and motion-controllers. It also provides electrical power components, including MCCB and ELCB, contactors and relays, air circuit and vacuum circuit breakers, vacuum contactors, power fuses, ring main units, motor protection relays, MV switchgears, transformers, and bus ducts; liquid and oil-cooled starters/NGR products; and power capacitors. In addition, the company offers electric motor products, such as AC and DC motors. CPT Drives and Power Public Company Limited was founded in 1995 and is headquartered in Bangkok, Thailand.'
    },

    # 141-160
    'CPTGF.BK': {
        'name': 'C.P. Tower Growth Leasehold Property Fund',
        'address': 'Empire Tower 32nd Floor 195 South Sathon Road Yannawa, Sathon Bangkok 10120 Thailand',
        'phone': '66 2 686 6100',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'The Fund has invested in the leasehold rights to land, buildings, components of land and buildings, and systems which are necessary for utilizing the buildings, and ownership of equipment and other assets which are and necessary for the utilizing of the office buildings. There are 30-year leasehold rights to 3 (three) buildings which the Fund has invested in, as follows 1) C.P. Tower 1 (Silom) Building 2) C.P. Tower 2 (Fortune Town) Building and 3) C.P. Tower 3 (Phayathai) Building.'
    },
    'CPW.BK': {
        'name': 'Copperwired Public Company Limited',
        'address': '159/6 Serm-Mit Tower Unit 201-202, 2nd Floor Sukhumvit 21 (Asoke) road North Klongtoey, Wattana Bangkok 10110 Thailand',
        'phone': '66 2 665 2950',
        'website': 'https://www.copperwired.co.th',
        'sector': 'Technology',
        'industry': 'Electronics & Computer Distribution',
        'description': 'Copperwired Public Company Limited distributes and repairs computers, mobile phones, and related accessories in Thailand. It also engages in the import, purchase, sale, and retail of computer and electronic accessories. The company was incorporated in 2019 and is based in Bangkok, Thailand. Copperwired Public Company Limited operates as a subsidiary of Vnet Capital Co., Ltd.'
    },
    'CRANE.BK': {
        'name': 'Chukai Public Company Limited',
        'address': '44/88 Moo 1 , Sisa Chorakhe Ya Bangsaothong Samut Prakan 10570 Thailand',
        'phone': '66 2 715 0000',
        'website': 'https://www.chukai.co.th',
        'sector': 'Industrials',
        'industry': 'Rental & Leasing Services',
        'description': 'Chukai Public Company Limited, together with its subsidiaries, engages in the heavy duty machinery business. It sells truck cranes, all terrain cranes, rough terrain cranes, crawler cranes, drilling rigs, wall grabs, and excavators. The company is also involved in the rental of heavy duty machinery, such as forklifts, container handlers, trucks, trailers, and tail trailers; and foundation construction business, including bored piles, barrette piles, diaphragm walls, high-pressure cement injection, and general construction work. In addition, it provides repair services for heavy duty machinery. The company was incorporated in 1997 and is headquartered in Samut Prakan, Thailand.'
    },
    'CRC.BK': {
        'name': 'Central Retail Corporation Public Company Limited',
        'address': '22 Soi Somkid Ploenchit Road Lumpini Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 650 3600',
        'website': 'https://www.centralretail.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Department Stores',
        'description': 'Central Retail Corporation Public Company Limited operates as a multi-format and multi-category retailing platform in Southeast Asia and Italy. It operates through Fashion, Hardline, Food and Property segments. The company focuses on apparel, accessories, electronics, and home improvement products, as well as groceries. It also provides vitamins, dietary supplements, and medical supplies by doctors, as well as leases retail property to third parties. Central Retail Corporation Public Company Limited was founded in 1947 and is headquartered in Bangkok, Thailand.'
    },
    'CSC.BK': {
        'name': 'Crown Seal Public Company Limited',
        'address': '5 Soi Rangsit-Nakornnayok 46 Prachatipat Thanyaburi 12130 Thailand',
        'phone': '66 2 533 0450',
        'website': 'https://www.crownseal.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Packaging & Containers',
        'description': 'Crown Seal Public Company Limited manufactures and distributes caps for bottles in Thailand and internationally. It operates through Manufacture and Sale of Caps; and Hire of Printing Sheets for Can segments. The companys products include crown, pilfer-proof, maxi crown, ring pull, maxi, maxi-PG, plastic, and composite caps, which are used as container seals for various drinks, such as soft drink, tea, soy milk and juice, health beverage, energy and sport drink, alcohol, drug, green tea drink, drinking water, beer, liquor, soda, chicken essences, birds nests, concentrated juice, and medical supplies, etc. It also provides hand-crowner; maxi crimping; and pilfer-proof cap crimping machines, as well as coating and printing services on steel and aluminum sheets. In addition, the company offers pre-sales and after-sales services; supplies spare parts; and equipment sale and services. Crown Seal Public Company Limited was incorporated in 1968 and is headquartered in Thanyaburi, Thailand.'
    },
    'CSP.BK': {
        'name': 'CSP Steel Center Public Company Limited',
        'address': 'No. 475 Rama 3 Road Bangklo Bangkolaem Bangkok 10120 Thailand',
        'phone': '66 2 291 6314',
        'website': 'https://www.cspsteel.com',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'CSP Steel Center Public Company Limited manufactures and distributes steel products in Thailand. It offers steel sheets, such as master coil, cutting sheet, slitting coil, and tolling for processing steel. The company also provides hot-rolled and cold-rolled steel sheets and pipes; and specializes in customizing steel sheets to other shapes. It serves clients in the automobiles, home and electric appliances, steel furniture, general usage, and structure and construction industries. The company was formerly known as CSP Trading Company Limited and changed its name to CSP Steel Center Public Company Limited in July 2005. CSP Steel Center Public Company Limited was founded in 1992 and is headquartered in Bangkok, Thailand.'
    },
    'CSR.BK': {
        'name': 'City Sports and Recreation Public Company Limited',
        'address': '22 Navatanee Road Ramindra Kannayao Bangkok 10230 Thailand',
        'phone': '66 2 376 1818',
        'website': 'http://www.navatanee.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Leisure',
        'description': 'City Sports and Recreation Public Company Limited operates golf courses, restaurants, and sport clubs in Thailand. The company was founded in 1970 and is headquartered in Bangkok, Thailand.'
    },
    'CSS.BK': {
        'name': 'Communication & System Solution Public Company Limited',
        'address': '329 Moo 3 Banmai Sub-district Pakkred District Nonthaburi 11120 Thailand',
        'phone': '66 2 018 1111',
        'website': 'https://www.cssthai.com',
        'sector': 'Technology',
        'industry': 'Electronics & Computer Distribution',
        'description': 'Communication & System Solution Public Company Limited, together with its subsidiaries, distributes and installs production equipment for electricity, water, air conditioning, and telecommunication systems in Thailand. The company operates through two segments: Distribution Electrical Equipment and Installation Service segment. The Distribution Electrical Equipment segment supplies electronic cables and other electrical systems equipment, and fire protection equipment. The Installation Service segment designs and installs telecommunication and fire protection systems. The company also distributes and installs tubes. Communication & System Solution Public Company Limited was founded in 1994 and is headquartered in Nonthaburi, Thailand.'
    },
    'CTARAF.BK': {
        'name': 'Centara Hotels and Resorts Leasehold Property Fund',
        'address': '400/22 KASIKORNBANK Building 6th and 12th floor Phahon Yothin Road Samsen Nai Sub-District, Phaya Thai District Bangkok Thailand',
        'phone': '66 2 673 3999',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'Centara Hotels and Resorts Leasehold Property Fund is a fund of Kasikorn Asset Management Co.,Ltd. The Fund has invested in propertys leasehold right named Centara Grand Beach Resort Samui.'
    },
    'CTW.BK': {
        'name': 'Charoong Thai Wire and Cable Public Company Limited',
        'address': '589/71, Central City Tower 12A Floor Debaratana Road North Bangna Sub-District, Bangna Dist. Bangkok 10260 Thailand',
        'phone': '66 2 745 6118',
        'website': 'https://www.ctw.co.th',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'Charoong Thai Wire and Cable Public Company Limited, together with its subsidiaries, manufactures and distributes electric wires and cables, and telephone cables under the CTW brand in Thailand, India, China, and internationally. It operates in four segments: Power Cable, Communication Cable, Fiber Optic Cable, and Enameled and Non-Enameled Wire. The company offers aluminum electrical wires and cables, copper electrical wires, high-voltage and low voltage power cables, telecommunication cables, fire resistance and flame-retardant cables, and control and instrument cables, as well as aluminum/copper conductor cables. Further, it manufactures and distributes fiber optic cables; and enameled and non-enameled wires, including enameled copper and aluminum wires, and non-enameled copper wires. In addition, the company engages in the fabrication of copper rods; and designing and manufacturing of custom OEM products. It serves government and private sector clients. Charoong Thai Wire and Cable Public Company Limited was founded in 1967 and is headquartered in Bangkok, Thailand.'
    },
    'CV.BK': {
        'name': 'Clover Power Public Company Limited',
        'address': 'No. 159 Soi Rama IX 57/1 (Wiset Suk 2) Phatthanakan Suanluang Bangkok 10250 Thailand',
        'phone': '66 2 731 7999',
        'website': 'https://www.cloverpower.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Clover Power Public Company Limited engages in generation and sale of electricity. It operates power plant and waste power plants. The company is involved in the design, construction, maintenance, and management of power plants; supplying and trading of machinery and equipment; operation of waste recycling and waste power plant to produce and distribute waste fuel; and supplying and distributing biomass fuel. It operates in Thailand and Australia. Clover Power Public Company Limited was incorporated in 2013 and is headquartered in Bangkok, Thailand.'
    },
    'CWT.BK': {
        'name': 'Chai Watana Tannery Group Public Company Limited',
        'address': 'No. 176/1,1480 Moo 1 Tannery Industrial District (K.M. 30) Sukhumwit Road Thambon Thaiban Mueang Samut Prakan 10280 Thailand',
        'phone': '66 2 703 7880',
        'website': 'http://www.cwt.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Auto Parts',
        'description': 'Chai Watana Tannery Group Public Company Limited, together with its subsidiaries, manufactures and exports leather-based products. It operates through six segments: Tannery Hide, Automotive Leather Cutting, Dog Chewable Toys, Furniture, Energy Business, and Design and Distribution of Aluminum Boat and Mini Bus. The company offers trim seat covers, steering wheels and gear knobs, and dog chews, as well as quilting, cutting, spray, and beam house and tanning services. In addition, it is involved in the design and distribution of boats and minibuses made from aluminum; property rental business; provision of consulting services for renewable energy projects; wholesale of wood chips; and generation and sale of electricity using waste. Further, the company provides services on waste disposal plants. Chai Watana Tannery Group Public Company Limited was founded in 1972 and is headquartered in Mueang Samut Prakan, Thailand.'
    },
    'DCC.BK': {
        'name': 'Dynasty Ceramic Public Company Limited',
        'address': '37/7 DCC Building Suthisarn-Vinijchai Road Samsen-Nok Sub-district HuayKwang District Bangkok 10310 Thailand',
        'phone': '66 2 276 9275',
        'website': 'https://www.dynastyceramic.com',
        'sector': 'Industrials',
        'industry': 'Building Products & Equipment',
        'description': 'Dynasty Ceramic Public Company Limited engages in the manufacture and sale of ceramic wall and floor tiles in Thailand and internationally. It offers its products under the Dynasty, Tile Top, Jaguar, Value, Mustang, Chicken, Birdie, Ducky, Swan, M, Cosmo, Rover, and Monte brand names. The company was formerly known as Royal Floor Tile Co. Ltd. and changed its name to Dynasty Ceramic Public Company Limited. Dynasty Ceramic Public Company Limited was founded in 1989 and is headquartered in Bangkok, Thailand.'
    },
    'DCON.BK': {
        'name': 'Dcon Products Public Company Limited',
        'address': '3300/57 Chang Tower B Building 8th Floor Phaholyothin Road Chomphon Subdistrict, Chatuchak District Bangkok 10900 Thailand',
        'phone': '66 2 937 3312',
        'website': 'https://www.dconproduct.com',
        'sector': 'Basic Materials',
        'industry': 'Building Materials',
        'description': 'Dcon Products Public Company Limited, together with its subsidiaries, manufactures and sells construction supplies in Thailand. It operates through Sales of Construction Supplies; Sales of Real Estate; and Real Estate for Lease segments. The company provides pre-stressed planks and piles, corrugated planks, cowboy and concrete fences, blocks, hallow core, hexagon piles, and footing products under the DCON name; and precast walls and floors, concrete posts, and other products. It is also involved in the sale and lease of real estate properties. The company was incorporated in 1996 and is headquartered in Bangkok, Thailand.'
    },
    'DDD.BK': {
        'name': 'Do Day Dream Public Company Limited',
        'address': 'No. 32, Keharomklao Road Ratpattana Saphansung Bangkok 10240 Thailand',
        'phone': '66 2 917 3055',
        'website': 'https://www.dodaydream.com',
        'sector': 'Consumer Defensive',
        'industry': 'Household & Personal Products',
        'description': 'Do Day Dream Public Company Limited, together with its subsidiaries, manufactures and distributes skin care products and supplements in Thailand. The company operates through Skincare business and Beauty Products business segments. It offers acne-prone and sensitive skin products under OXECURE; skin care and deep-nourishing products under SOS; hair styling appliance under LESASHA; oral care products, including toothpastes and toothbrushes under SPARKLE; and fitness equipment under JASON brands. In addition, the company provides home electrical appliance under AT HOME; hair removal devices under EMJOI; intense pulse light hair removal devices under SMOOTH SKIN; beauty innovation products under Kuron; and electrical appliance for cooking under BEAR brands. Do Day Dream Public Company Limited was incorporated in 2010 and is headquartered in Bangkok, Thailand.'
    },
    'DELTA.BK': {
        'name': 'Delta Electronics (Thailand) Public Company Limited',
        'address': '909 Soi 9, Moo 4, E.P.Z. Bangpoo Industrial Estate Tambon Prakasa Amphur Muangsamutprakarn Samut Prakan 10280 Thailand',
        'phone': '66 2 709 2800',
        'website': 'https://www.deltathailand.com',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'Delta Electronics (Thailand) Public Company Limited, together with its subsidiaries, researches and develops, manufactures, and distributes electronic products. It operates through Power Electronics, Infrastructure, and Automation segments. It offers inductors, RF inductors, transformers, networking products, EMI filters, solenoids, current sensing resistors, and power modules; switching power supplies, standard power modules, and lighting ballasts and LED drivers; DC brushless fans and blowers, motors, thermal management products, cabinet thermal solutions, and indoor air quality and automotive fans; EV/HEV powertrain solutions and power electronics components comprise of on-board chargers and DC/DC converters; and display and visualization, mobile power, industrial power, and medical power products, as well as healthcare devices. The company also provides industrial automation products and solutions, including drives and power quality products, motion control solutions, control systems, robots, software systems, and manufacturing equipment, as well as field devices that include temperature controllers, machine vision systems, power meters, and smart and vision sensors. In addition, it offers building automation products comprising building management and control system, LED lighting, intelligent surveillance, and building energy management system products; telecom power systems, networking systems, and UPS and datacenter infrastructure solutions; and EV charging and energy storage systems, renewable energy, industrial battery charging, healthcare devices, industrial equipment, energy IoT, and display and visualization products. Further, the company rents properties. It operates in the United States, China, Germany, India, Ireland, Mexico, Singapore, Norway, Taiwan, the Netherlands, and internationally. Delta Electronics (Thailand) Public Company Limited was incorporated in 1988 and is based in Samut Prakan, Thailand.'
    },
    'DEMCO.BK': {
        'name': 'Demco Public Company Limited',
        'address': '59 Moo 1, Tambol Suanphrikthai Amphur Muangpathumthani Pathum Thani 12000 Thailand',
        'phone': '66 2 959 5811',
        'website': 'https://www.demco.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'Demco Public Company Limited, together with its subsidiaries, engages in the provision of electric system construction and service works in the fields of electric engineering and telecommunication in Thailand. The company operates through six segments: Sales, Electricity from Solar Power, Electrical Work Services, Electrical and Mechanical Work Services, Engagement Work Services, and Other Services. The Sales segment produces and sells steel structure fabrications for electrical and telecommunication works, as well as supplies water. The Electricity from Solar Power segment generates and sells electricity from solar power. The Electrical Work Services segment designs, constructs, and manages electrical work. The Electrical and Mechanical Work Services segment designs, constructs, and manages mechanical and electric systems and facilities, such as electrical, water management, air-conditioning and ventilation, and steam and hot water systems. The Engagement Work Services segment produces and installs fabricated steel structures and high pressure vessels. The Other Services segment provides civil work, communication, and other services. It also manufactures and trades in steel structures and steel towers; and trades in assembled telecommunication equipment, communication equipment, and electrical equipment, as well as sells construction materials. The company was incorporated in 1992 and is headquartered in Pathum Thani, Thailand.'
    },
    'DIF.BK': {
        'name': 'Digital Telecommunications Infrastructure Fund',
        'address': '7-8th Floor. SCB Park Plaza 1 18 Ratchadapisek Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 949 1500',
        'website': 'N/A',
        'sector': 'Technology',
        'industry': 'Information Technology Services',
        'description': 'Digital Telecommunications Infrastructure Fund specializes in infrastructure investments in the digital telecommunications sector. We own or are entitled to the net revenues generated from a portfolio of 16,059 telecommunications towers comprising 9,727 towers owned by the Fund (comprising True Tower Assets and TUC Towers for Additional Investment No. 2, No.3 and No. 4) and 6,332 towers from which the Fund is entitled to the net revenue (comprising the BFKT Towers, AWC Towers, AWC Towers for Additional Investment No. 1 and No. 2), including the ownership in the certain BFKT Telecom Assets after the expiry of the HSPA Agreements and certain AWC Towers after the expiry of the AWC Leasing Agreement, Additional AWC Leasing Agreement No. 1 and Additional AWC Leasing Agreement No. 2. and FOC and Upcountry Broadband System'
    },
    'DMT.BK': {
        'name': 'Don Muang Tollway Public Company Limited',
        'address': '40/40, Viphavadi-Rangsit Road Sanambin Don Muang Bangkok 10210 Thailand',
        'phone': '66 2 792 6500',
        'website': 'https://www.tollway.co.th',
        'sector': 'Industrials',
        'industry': 'Infrastructure Operations',
        'description': 'Don Muang Tollway Public Company Limited provides elevated toll road service in Thailand. The company operates a toll road from Din Daeng to National Memorial Monument with total length of 21.9 kilometers. It offers a range of services to the tollway users comprising toll collection, traffic management, rescue, and maintenance services. Don Muang Tollway Public Company Limited was incorporated in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'DOHOME.BK': {
        'name': 'Dohome Public Company Limited',
        'address': '60 Soi Ruam Mit, Din Daeng Road, Sam Sen Nai Sub-district, Phaya Thai District Bangkok 10400',
        'phone': '66 2 027 8787',
        'website': 'https://www.dohome.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Home Improvement Retail',
        'description': 'Dohome Public Company Limited, together with its subsidiaries, engages in the retailing and wholesaling of construction materials, office equipment, and household products in Thailand. The company offers construction materials products, such as steel sections, skirting boards, cement and other infrastructure products, etc.; repair materials products, including tools agriculture, gardening and plumbing equipment, electric equipment, sanitary equipment, etc.; and decoration materials products comprising electrical appliances, home furniture appliances, home decorations, bedding, gift shops, etc. It is also involved in the production and distribution of electricity; and property investment activities. The company was founded in 1983 and is based in Ubon Ratchathani, Thailand.'
    },

    # 161-180
    'DREIT.BK': {
        'name': 'Dusit Thani Freehold and Leasehold Real Estate Investment Trust',
        'address': 'No. 319 Chamchuri Square Building 29th Floor Phayathai Road Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 200 9999',
        'website': 'https://www.dtcreit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Hotel & Motel',
        'description': 'Dusit Thani Freehold and Leasehold Real Estate Investment Trust is a real estate investment trust. The firm focuses on investing in high potential freehold or leasehold properties especially in hotel properties, as well as investing in other assets that favor hotel-related business, such as meeting and convention room, restaurants, fitness center, spa, swimming pool, tennis court etc. The firm is based in Bangkok, Thailand.'
    },
    'DRT.BK': {
        'name': 'Diamond Building Products Public Company Limited',
        'address': '69-70 Moo 1 Mitraphab Km. 115 Thambon Talingchan Tambon Talingchan Amphur Muang Sara Buri 18000 Thailand',
        'phone': '66 3 622 4171',
        'website': 'https://www.dbp.co.th',
        'sector': 'Industrials',
        'industry': 'Building Products & Equipment',
        'description': 'Diamond Building Products Public Company Limited, together with its subsidiaries, manufactures and distributes roof tiles, artificial woods, and autoclaved aerated concrete products in Thailand and internationally. The company offers roofing products, wall sidings and ceilings, and artificial boards, as well as equipment for installation of roofs and house structural members. It also provides other roof accessories and non-roof products; and services for design and installation of roofs under the Diamond Roof, Adamas, and Jearanai names. The company was formerly known as Diamond Roofing Tiles Public Company Limited and changed its name to Diamond Building Products Public Company Limited in January 2011. The company was founded in 1985 and is headquartered in Saraburi, Thailand. Diamond Building Products Public Company Limited is a subsidiary of Myriad Materials Co., Ltd'
    },
    'DTCENT.BK': {
        'name': 'D.T.C. Enterprise Public Company Limited',
        'address': '63 Soi Sukhumvit 68 Sukhumvit Road Bangna Nuea Subdistrict Bangna District Bangkok 10260 Thailand',
        'phone': '1176',
        'website': 'https://www.dtc.co.th',
        'sector': 'Technology',
        'industry': 'Scientific & Technical Instruments',
        'description': 'D.T.C. Enterprise Public Company Limited produces and deals in satellite land vehicle tracking devices and black box sets, and IoT solutions in Thailand and internationally. The company provides real-time GPS tracking, blue box real time GPS tracking, container tracking, motorcycle tracking, and device options for GPS tracking systems; mobile DVR smart eye model, driving, mobile CCTV online model MDVR, and in vehicle monitoring systems; and software solutions, including transport management, business activity management, online map system, DTC fleet maintenance, and smart farm solutions. It also offers excise departments gauge systems, information technology systems for internal office system development, information and DVR camera systems for fire engines and rescue departments, administrative agency resources management systems, smart vending machine IoT solutions, and fire detection systems; and monitoring, controlling, and tracking systems for oil handling along border zone, as well as to draw up database of liquor sale located close by or around schools. In addition, the company exports its products to China, Philippines, Indonesia, India, Laos, Bangladesh, Vietnam, Kenya, Malaysia, Hong Kong, Myanmar, Cambodia, and other countries. The company was founded in 1996 and is based in Bangkok, Thailand.'
    },
    'DTCI.BK': {
        'name': 'D.T.C. Industries Public Company Limite',
        'address': '176, D.T.C. Building Sukhumvit 64 Sukhumvit Road Bangchak, Prakhanong Bangkok Thailand',
        'phone': '66 2 311 1371',
        'website': 'N/A',
        'sector': 'Industrials',
        'industry': 'Business Equipment & Supplies',
        'description': 'D.T.C. Industries Public Company Limited produces and distributes pens and related products in Thailand and internationally. It also provides space rental. The company was incorporated in 1971 and is headquartered in Bangkok, Thailand.'
    },
    'DUSIT.BK': {
        'name': 'Dusit Thani Public Company Limited',
        'address': '319 Chamchuri Square Building 29th Floor Phyathai Road Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 200 9999',
        'website': 'https://dusit-international.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'Dusit Thani Public Company Limited, together with its subsidiaries, owns and operates hotels and resorts in Thailand and internationally. The company operates through five segments: Hotel and Hotel Management, Education, Foods, Property development, and Others. It operates hotels under the Dusit Thani, Dusit Devarana, dusitD2, Dusit Princess, ASAI Hotels, and Elite Havens brands; spas under the Devarana Spa and Namm Spa brands; and healthy food restaurants. The company also provides hotel management and consultancy services; and engages in the food and beverage catering, and distribution business. In addition, it operates Dusit Thani College; Dusit Thani Excellence Centre; Le Cordon Bleu Dusit Culinary School; and The Food School. Further, the company operates as a REIT manager for real estate investment trust; and distributor of bakery and franchise business. Additionally, it is involved in the property leasing and sub-leasing; and property development businesses, as well as operates culinary schools and hospitality colleges in Thailand. Dusit Thani Public Company Limited was founded in 1948 and is headquartered in Bangkok, Thailand.'
    },
    'EA.BK': {
        'name': 'Energy Absolute Public Company Limited',
        'address': 'AIA Capital Center Building 16th Floor No. 89, Ratchadaphisek Road Dindaeng Bangkok 10400 Thailand',
        'phone': '66 2 248 2488',
        'website': 'https://www.energyabsolute.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Energy Absolute Public Company Limited, together with its subsidiaries, engages in the manufacturing and distribution of crude palm oil, biodiesel products, and glycerol in Thailand. The company provides phase change materials, as well as electric buses, car, ferry, and boats; and development, manufacture, and distribution of lithium-ion polymer batteries. It also generates electricity through solar, wind, and biogas power plants; provides construction projects consulting, hire purchase of electric vehicles, shore tank rental, and crude palm oil pipeline transport services; and operates charging stations. The company was formerly known as Suntech Palm Oil Ltd. and changed its name to Energy Absolute Public Company Limited in 2008. Energy Absolute Public Company Limited was incorporated in 2006 and is headquartered in Bangkok, Thailand.'
    },
    'EASON.BK': {
        'name': 'Eason & Co Public Company Limited',
        'address': '7/1-2 Moo 1 Tombol Panthong Amphur Panthong Phan Thong 20160 Thailand',
        'phone': '66 3 845 1833',
        'website': 'http://www.easonplc.com',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'Eason & Co Public Company Limited manufactures and sells industrial and automotive paints primarily in Thailand. It offers packaging coatings for interior and exterior application to crown caps, ROPP, screw caps, lug caps, and other closures. The company also provides offset inks comprising metal decorating inks for 2-piece cans; and conventional and UV metal decorating inks for 3-piece cans. In addition, it offers motorcycle coatings, including poly urethane, acrylic, and air dry paints, as well as trades in industrial paints. The company was formerly known as Eason Paint Public Company Limited and changed its name to Eason & Co Public Company Limited in May 2020. Eason & Co Public Company Limited was incorporated in 1965 and is headquartered in Phan Thong, Thailand.'
    },
    'EASTW.BK': {
        'name': 'Eastern Water Resources Development and Management Public Company Limited',
        'address': 'East Water Building 23rd-26th Floors 1 Vipavadeerangsit 5 Vipavadeerangsit Rd,Jomphol, Jatujak Bangkok 10900 Thailand',
        'phone': '66 2 272 1600',
        'website': 'https://www.eastwater.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Regulated Water',
        'description': 'Eastern Water Resources Development and Management Public Company Limited, together with its subsidiaries, engages in the development and management of water distribution pipeline systems in the eastern seaboard area of Thailand. It produces and supplies tap water; provides waste treatment, waterworks management, engineering services, operation and maintenance management, and renewable energy management services; recycles water; and supplies raw water. The company was founded in 1992 and is headquartered in Bangkok, Thailand.'
    },
    'ECL.BK': {
        'name': 'Eastern Commercial Leasing Public Company Limited',
        'address': '976/1 Soi Rama IX Hospital Rim Klong Samsen Road Bangkapi Sub-District Huay Kwang District Bangkok 10310 Thailand',
        'phone': '66 2 641 5252',
        'website': 'https://www.ecl.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Eastern Commercial Leasing Public Company Limited engages in the provision of credit services to personal and juristic person in the form of hire purchase, loans, and sale with right of redemption agreement in Thailand. It also provides vehicle registration, vehicle insurance, vehicle third party liability insurance, and life insurance renewal services. The company was founded in 1982 and is headquartered in Bangkok, Thailand.'
    },
    'EE.BK': {
        'name': 'Eternal Energy Public Company Limited',
        'address': '888 I Tower Building 8th Floor Vibhavadi Rangsit Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 554 8000',
        'website': 'http://www.eternalenergy.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Eternal Energy Public Company Limited, together with its subsidiaries, engages in the cassava plantation activities in Thailand. The company is involved in the plantation of tapioca and other energy crops. It also rents real estate properties. The company was formerly known as Sea Horse Public Company Limited and changed its name to Eternal Energy Public Company Limited in October 2009. Eternal Energy Public Company Limited was incorporated in 1987 is headquartered in Bangkok, Thailand.'
    },
    'EGATIF.BK': {
        'name': 'Electricity Generating Authority Of Thailand- North Bangkok Power Plant Block 1 Infrastructure Fund',
        'address': 'No. 1, Empire Tower, 32nd Floor, South Sathorn Road, Yannawa Subdistrict, Sathorn District Bangkok 10120',
        'phone': '66 2 686 6100',
        'website': 'N/A',
        'sector': 'Utilities',
        'industry': 'Utilities—Independent Power Producers',
        'description': 'EGATIF invest in the future Availability Revenue obtainable from North Bangkok Power Plant Block 1, a Contracted Capacity of 670 MW , for the period of 20 years'
    },
    'EGCO.BK': {
        'name': 'Electricity Generating Public Company Limited',
        'address': 'EGCO Tower 14th and 15th floor 222, Vibhavadi Rangsit Road Tungsonghong, Laksi Bangkok 10210 Thailand',
        'phone': '66 2 998 5000',
        'website': 'https://www.egco.com/th/',
        'sector': 'Utilities',
        'industry': 'Utilities—Independent Power Producers',
        'description': 'Electricity Generating Public Company Limited, together with its subsidiaries, generates and sells electricity to government sector and industrial users primarily in Thailand, the Philippines, Australia, South Korea, Taiwan, the United States, Laos, and Indonesia. The company operates in two segments, Electricity Generation and Other Businesses. It generates electricity from various resources, such as natural gas, liquefied natural gas, coal, biomass, hydro, solar, wind, geothermal, and fuel cell. As of December 31, 2022, the company operated 31 domestic and overseas power plants with total capacity of 6,202 MW equity; operating power plants with a total capacity of 5,972 MW equity and projects under construction with total equity contracted capacity of 230 MW. It also provides operation, maintenance, engineering, and construction services to power plants, petrochemical plants, oil refineries, and other industries. The company was incorporated in 1992 and is headquartered in Bangkok, Thailand.'
    },
    'EKH.BK': {
        'name': 'Ekachai Medical Care Public Company Limited',
        'address': '99/9 Moo 4, Ekachai Road Tambol Khokkham Amphur Muang 74000 Thailand',
        'phone': '66 3 441 7999',
        'website': 'https://www.ekachaihospital.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Ekachai Medical Care Public Company Limited, together with its subsidiaries, operates Ekachai hospital in Thailand. It offers plastic surgery, fertility and genetic, pediatric, obstetrics and gynecology, general medicine clinic, general surgery, orthopedics, ophthalmology, emergency, health promotion, hemodialysis, dental, physical, mobile checkup, pre-employment checkup, aesthetic and dermatology center, and child and teen development center services, as well as mobile checkup and physical therapy services. Ekachai Medical Care Public Company Limited was incorporated in 2003 and is headquartered in Muang, Thailand.'
    },
    'EMC.B': {
        'name': 'EMC Public Company Limited',
        'address': '140/66-67, ITF Tower 28th-30th Floor Silom Road Suriyawong, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 615 6100',
        'website': 'http://www.emc.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'EMC Public Company Limited, together with its subsidiaries, engages in the construction contracting and real estate development businesses in Hong Kong. It offers construction for skyscrapers and industrial construction; and barrage construction, waterway construction, soil destruction prevention, roadway construction, etc. The company also provides electrical and mechanical engineering services, such as installation of electrical systems, plumbing systems, and ventilation systems for hotels, hospitals, condominiums, offices, shopping malls, and industrial factories. In addition, it develops various projects, including house, twin house, town house, commercial buildings, condominium, etc. The company was formerly known as EMC Engineering Limited Partnership. EMC Public Company Limited was incorporated in 1979 and is headquartered in Bangkok, Thailand.'
    },
    'EP.BK': {
        'name': 'Eastern Power Group Public Company Limited',
        'address': '51/29, 51/61Soi. Soi Viphavadee Rangsit 66 (Siamsamakee) Vibhavadi Rangsit Road Talad Bang Khen Subdistrict, Lak Si Dist Bangkok 10210 Thailand',
        'phone': '66 2 551 0541',
        'website': 'https://epgroup.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Eastern Power Group Public Company Limited engages in the solar power generation business. It also involved in the maintenance and installation service contract in solar power project. The company was formerly known as Eastern Printing Public Company Limited and changed its name to Eastern Power Group Public Company Limited in April 2020. Eastern Power Group Public Company Limited was incorporated in 1993 and is headquartered in Bangkok, Thailand.'
    },
    'EPG.BK': {
        'name': 'Eastern Polymer Group Public Company Limited',
        'address': '770 Moo 6, Theparak Road Theparak Muang Samutprakarn Mueang Samut Prakan 10270 Thailand',
        'phone': '66 2 383 6599',
        'website': 'https://www.epg.co.th',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'Eastern Polymer Group Public Company Limited, through its subsidiaries, engages in the manufacture and distribution of rubber insulation, automotive, plastic packing, and research and development business in Thailand and internationally. It also manufactures bed liners and covers of pickup trucks, as well as automotive accessories products. In addition, the company is involved in the import and export of machinery and chemicals; manufacture of rubber for cars, machinery, buildings, and other products; assembly and distribution of molded plastic parts; and injection and molding of plastic parts. Further, it designs, manufactures, and trades in accessories for 2, 4WD, light commercial, and heavy transportation vehicles, as well as provides calibration services. The company was formerly known as Eastern Polymer Industry Company Limited. The company was incorporated in 1978 and is headquartered in Mueang Samut Prakan, Thailand. Eastern Polymer Group Public Company Limited is a subsidiary of Vitoorapakorn Holding Co., Ltd.'
    },
    'ERW.BK': {
        'name': 'The Erawan Group Public Company Limited',
        'address': 'Ploenchit Center 6th Floor 2 Sukhumvit Road Kwang Klongtoey, Khet Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 257 4588',
        'website': 'https://www.theerawan.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'The Erawan Group Public Company Limited, through its subsidiaries, engages in hotel, and building rental and management businesses in Thailand. The company operates hotels and resorts under the Grand Hyatt Erawan Bangkok, JW Marriott Bangkok, The Naka Island, Renaissance Koh Samui Resort and Spa, Courtyard by Marriott Bangkok, Holiday Inn Pattaya, Mercure Bangkok Siam, ibis Hotel, Novotel Bangkok Sukhumvit 4, Mercure Bangkok Sukhumvit 24, ibis Styles Bangkok Sukhumvit 4, ibis Bangkok Siam, ibis Styles Krabi Ao Nang, ibis Pattaya, ibis Phuket Patong, ibis Phuket Kata, ibis Samui Bophut, ibis Hua Hin, and HOP INN names. It also owns and operates retail property under the name Erawan Bangkok, and manages Ploenchit Center a luxury retail property adjacent to Grand Hyatt Erawan Hotel, and manages Ploenchit Center. The company is also involved in the development of properties; retail space rental; and provision of office buildings management services. The Erawan Group Public Company Limited was incorporated in 1982 and is headquartered in Bangkok, Thailand.'
    },
    'ERWPF.BK': {
        'name': 'Erawan Hotel Growth Property Fund',
        'address': 'The 9th Towers Grand Rama 9 Floor 18 33/4 Rama 9 Road Huaykwang Bangkok 10310 Thailand',
        'phone': '66 2 949 1500',
        'website': 'https://www.scbam.com/en/fund/property-fund/fund-information/erwpf',
        'sector': 'Real Estate',
        'industry': 'REIT—Hotel & Motel',
        'description': 'The Fund has invested in Freehold right of the ibis Patong Hotel and the ibis Pattaya Hotel. The properties consist of land with construction, buildings, public utility system in relation to the hotel business and furniture, fixtures and fittings and equipment.'
    },
    'ESSO.BK': {
        'name': 'Esso (Thailand) Public Company Limited',
        'address': '3195/17-29 Rama IV Road Klong Ton Klong Toey District Bangkok 10110 Thailand',
        'phone': '66 2 407 4000',
        'website': 'https://www.esso.co.th',
        'sector': 'Energy',
        'industry': 'Oil & Gas Refining & Marketing',
        'description': 'Esso (Thailand) Public Company Limited refines and markets petroleum products in Thailand and internationally. It operates through two segments, Downstream and Petrochemicals. The company provides liquefied petroleum gas, gasoline, naphtha, jet fuel/kerosene, diesel, fuel oil, and asphalt; and other petroleum products comprising mineral and synthetic lubricants under the Mobil brand. It sells refined petroleum products through retail service stations under the Esso brand; and commercial channels that consist of sales to industrial end users, wholesalers, and customers in the aviation and marine industries. The company also offers hydrocarbon solvents, such as hexane used in edible oil seed extractions and as a carrier in petrochemical production; rubber solvents that are used as adhesives and rubber cement for manufacturing of tires; white spirits for coating and paint industries; and Exxsol D80 for household, industrial, and metal working applications. In addition, it imports and markets aromatic solvents that are used in the automotive paint coating industry; sells plasticizers; and leases real estate properties. The company was formerly known as Esso Standard Thailand Co., Ltd. and changed its name to Esso (Thailand) Public Company Limited in 1996. The company was founded in 1894 and is based in Bangkok, Thailand. Esso (Thailand) Public Company Limited is a subsidiary of ExxonMobil Asia Holding Private Limited.'
    },
    'ESTAR.BK': {
        'name': 'Eastern Star Real Estate Public Company Limited',
        'address': '898 Ploenchit Tower 5th Floor Ploenchit Road Lumpini Sub-dist, Pathumwan Bangkok 10330 Thailand',
        'phone': '66 91 949 0000',
        'website': 'https://www.estarpcl.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Eastern Star Real Estate Public Company Limited, together with its subsidiaries, engages in the property development business in Thailand. The company operates in three segments: Real Estate Business, Golf Course Business, and Rental Business. It develops and sells land, houses, and residential condominium units; and rents properties. The company also operates golf courses, as well as offers sport memberships. Eastern Star Real Estate Public Company Limited was founded in 1989 and is headquartered in Bangkok, Thailand.'
    },

    # 181-200
    'ETC.BK': {
        'name': 'Earth Tech Environment Public Company Limited',
        'address': 'No. 88,88/1 Moo 1 Ban That Subdistrict Kaeng Khoi District Kaeng Khoi 18110 Thailand',
        'phone': '66 3 620 9294',
        'website': 'https://www.etcenvi.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Earth Tech Environment Public Company Limited generates and distributes electricity using processed municipal and industrial waste in Thailand. The company operates power plants with an installed capacity of 9.4 MW located in Kaeng Khoi industrial estate, Kaeng Khoi district; 7.0 MW installed capacity in NakornLuang industrial estate, Nakhon Luang district; and 5.5 MW located in Phra Nakhon Si Ayutthaya. It is also involved in the procurement of machinery and equipment, and integrated plant construction, operation, and maintenance, as well as provision of engineering design services. The company was incorporated in 2004 and is headquartered in Kaeng Khoi, Thailand.'
    },
    'EVER.BK': {
        'name': 'Everland Public Company Limited',
        'address': '223/96 Country Complex Tower Building A 21st Floor Sanphawut Road Kwang Bangna, Khet Bangna Bangkok 10260 Thailand',
        'phone': '66 2 361 6156',
        'website': 'https://www.everland.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Everland Public Company Limited, together with its subsidiaries, engages in the property development business in Thailand. It operates in two segments, Property Development, and Hospital and Dental Clinic. The company develops various projects, such as townhomes, single houses, and condominiums, as well as commercial buildings. It is also involved in the operation of private hospitals and dental clinics; and provision of land and hospital buildings for rent. The company was founded in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'F&D.BK': {
        'name': 'Food and Drinks Public Company Limited',
        'address': '15th Floor, Regent House Bldg., 183 Rajdamri Rd., Lumpini, Patumwan Bangkok 10330',
        'phone': '66 2 253 5232',
        'website': 'http://www.foodanddrinks.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Food and Drinks Public Company Limited manufactures and sells foods products, beverages, and frozen foods in Thailand. It offers curry paste, curry sauce, spices, and cooking sauces; aloe vera, bamboo shoot, mango, and mixed fruits, and vegetables, as well as spices, such as lemon grass, chilli, and coriander; and brine, vinegar, syrup, or water for fruits and vegetables. The company also provides fruit and vegetable juices, and ready-to-drink tea; and ready to eat products comprising rice with chicken basil stir fried, minced chicken hot yellow curry paste, steamed glutinous rice in banana leaf, and papaya salad. It also exports its products. Food and Drinks Public Company Limited was founded in 1985 and is headquartered in Chonburi, Thailand.'
    },
    'FANCY.BK': {
        'name': 'Fancy Wood Industries Public Company Limited',
        'address': '357 Moo 12, Soi Suksawat 84 (Kusang) Suksawad Road Naikhlongbangplakot Sub-district Prasamutjaedee District Samut Prakan 10290 Thailand',
        'phone': '66 2 578 2823',
        'website': 'http://www.fancywood.th.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Furnishings, Fixtures & Appliances',
        'description': 'Fancy Wood Industries Public Company Limited, together with its subsidiaries, manufactures and sells rubber wood products in Thailand and internationally. The company offers particle board, modified rubber wood, and services related to rubber wood. It is also involved in the real estate development activities, as well as rental of property. The company was founded in 1970 and is headquartered in Samut Prakan, Thailand.'
    },
    'FE.BK': {
        'name': 'Far East Fame Line DDB Public Company Limited',
        'address': '465/1-467 Si Ayutthaya Rd Thungphayathai Ratchathewi District Bangkok 10400 Thailand',
        'phone': '66 2 354 3333',
        'website': 'https://www.fareastfamelineddb.com',
        'sector': 'Communication Services',
        'industry': 'Advertising Agencies',
        'description': 'Far East Fame Line DDB Public Company Limited, together with its subsidiaries, engages in the advertising agency business in Thailand. The company offers digital marketing, creative communication, campaign management, graphic design, production, media and performance, branding, data analysis and transformation, CX solutions, and social media management services. The company was formerly known as Far East DDB Public Company Limited and changed its name to Far East Fame Line DDB Public Company Limited in January 2018. Far East Fame Line DDB Public Company Limited was incorporated in 1964 and is headquartered in Bangkok, Thailand.'
    },
    'FMT.BK': {
        'name': 'Fine Metal Technologies Public Company Limited',
        'address': '183 Regent House Building 14th Floor Rajdamri Road Lumpini, Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 256 0641',
        'website': 'https://www.fmt.co.th',
        'sector': 'Industrials',
        'industry': 'Metal Fabrication',
        'description': 'Fine Metal Technologies Public Company Limited engages in the manufacturing and distributing of seamless copper tubes in Thailand, Malaysia, Singapore, Japan, and internationally. The company offers smooth tubes for heat exchanger and piping; multi-grooved tubes to produce the air conditioners; accumulator tubes for use as the pressure reservoir tank or refrigerant; and capillary tubes. The company was formerly known as Furukawa Metal (Thailand) Public Company Limited and changed its name to Fine Metal Technologies Public Company Limited in November 2020. The company was incorporated in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'FN.BK': {
        'name': 'FN Factory Outlet Public Company Limited',
        'address': '991 FN Building Rama 9 Road Suan Luang Sub-District Suan Luang District Bangkok 10250 Thailand',
        'phone': '66 2 300 4951',
        'website': 'https://www.fnoutlet.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Apparel Retail',
        'description': 'FN Factory Outlet Public Company Limited merchandises clothing and consumer products in Thailand. The company retails apparel and non-apparel goods through factory outlets. Its stores also offer clothes, beddings, leather, furniture, cosmetics, and household products; and accessories, such as shoes, bags, belt, and jewelries, as well as snacks. The company offers its products under the Inco Men, Monsieur Inco, Inco Women, Madame Inco, Cheval, Cheval Black Collection, Lady De Cheval, Cheval Kid, Sleepmate, Rollica, Prim, Cushy, and Cherish brands. FN Factory Outlet Public Company Limited was founded in 2000 and is headquartered in Bangkok, Thailand.'
    },
    'FNS.BK': {
        'name': 'FNS Holdings Public Company Limited',
        'address': '345 Surawong Building 6th Floor 345 Surawong Road Suriyawong, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 697 3700',
        'website': 'https://www.fnsplc.com',
        'sector': 'Financial Services',
        'industry': 'Asset Management',
        'description': 'FNS Holdings Public Company Limited, together with its subsidiaries, provides various financial services in Thailand. It operates through three segments: Investment, Advisory and Management Business; Securities Business; and Warehouse and Factory Leasing Business. The company invests in and provides finance and management advisory services; and offers warehouse and factory leasing services. It also provides investment banking; underwriting; mutual fund selling agency; bond trading; and investment advisory services, as well as private equity investment services. The company was formerly known as Finansa Public Company Limited. FNS Holdings Public Company Limited was incorporated in 1989 and is based in Bangkok, Thailand.'
    },
    'FORTH.BK': {
        'name': 'Forth Corporation Public Company Limited',
        'address': '1053/1, Phaholyothin Road Phayathai Bangkok 10400 Thailand',
        'phone': '66 2 265 6700',
        'website': 'https://www.forth.co.th',
        'sector': 'Technology',
        'industry': 'Electronic Components',
        'description': 'Forth Corporation Public Company Limited, together with its subsidiaries, manufactures and distributes electronic equipment in Thailand. It operates through three segments: Electronics Manufacturing Service Business; Enterprise Solutions Business; and Smart Service Business. It offers Forth Taglock EM, a tracking device made for prisoners; nurse call systems; GPS devices and GPS tracking systems; lighting system solutions; smart traffic light systems; smart grids; multi-service access network telephone exchange equipment; EV charging stations; smart meter systems, including digital meters that show energy/water consumptions digitally, as well as smart software, which pulls data from meters automatically; and small gas station and oil vending machines. The company also provides top-up and payment kiosks; Boonterm Counter Service that has a touch screen with a data acquisition system that helps monitor usage and print receipts backwards; Boonterm water dispensers; automated cup beverage vending machines; smart vending machines; and KODIAK, a high performance aircraft, as well as operates commercial aircraft maintenance center. In addition, it engages in the trading of electronic parts; sale and installation of light boards and traffic systems; provision of consulting service for information management and computer software management, as well as engineering services; sale of aircraft, aircraft hangar and maintenance business, and flight training; electronic commerce business; and turnkey on installation of CCTV. Additionally, the company offers nano finance and personal loan services; and distributes goods. Forth Corporation Public Company Limited was founded in 1989 and is headquartered in Bangkok, Thailand.'
    },
    'FPT.BK': {
        'name': 'Frasers Property (Thailand) Public Company Limited',
        'address': 'No. 944 Mitrtown Office Tower 20th Floor Rama 4 Road, Wangmai Subdistrict Pathumwan District Bangkok 10330 Thailand',
        'phone': '66 2 483 0000',
        'website': 'https://www.frasersproperty.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Frasers Property (Thailand) Public Company Limited, together with its subsidiaries, primarily develops industrial real estate properties in Thailand. The company develops and sells range of residential properties, which include single-detached and semi-detached houses, and townhomes. It also provides development of industrial properties including factory and warehouses, such as ready-build factory and warehouse, built-to-suit factory and warehouse, investment and property management, trust management, and other services comprising modification of factory/warehouse building, procurement of utilities and authority permits and other related services. In addition, the company engages commercial property business, which include serviced apartments, hotels, and office buildings. The company was formerly known as TICON Industrial Connection Public Company Limited and changed its name to Frasers Property (Thailand) Public Company Limited in January 2019. Frasers Property (Thailand) Public Company Limited was founded in 1990 and is based in Bangkok, Thailand.'
    },
    'FSS.BK': {
        'name': 'Finansia Syrus Securities Public Company Limited',
        'address': 'No. 999/9, The Offices at Centralworld 18th and 25th Floors Rama I Road Pathumwan Sub-district, Pathumwan Dist. Bangkok 10330 Thailand',
        'phone': '66 2 658 9000',
        'website': 'https://www.fnsyrus.com',
        'sector': 'Financial Services',
        'industry': 'Capital Markets',
        'description': 'Finansia Syrus Securities Public Company Limited, together with its subsidiaries, engages in the securities and derivatives brokerage business in Thailand. The company operates in three segments: Securities and Derivatives Brokerage, Investment Banking, and Proprietary Trading. It offers securities brokerage and trading, investment and financial advisory, securities underwriting, derivative brokerage, securities borrowing and lending, and mutual fund and private fund management services. As of December 31, 2021, the company had 24 branches. The company was formerly known as Syrus Securities Public Company Limited and changed its name to Finansia Syrus Securities Public Company Limited in June 2009. Finansia Syrus Securities Public Company Limited was founded in 2002 and is headquartered in Bangkok, Thailand.'
    },
    'FTE.BK': {
        'name': 'Firetrade Engineering Public Company Limited',
        'address': 'No. 1198/5 Rama 9 Road Phatthanakan Sub-district Suan Luang District Bangkok 10250 Thailand',
        'phone': '66 2 026 0470',
        'website': 'https://firetrade.co.th',
        'sector': 'Industrials',
        'industry': 'Security & Protection Services',
        'description': 'Firetrade Engineering Public Company Limited designs, sells, installs, repairs, and maintains fire protection equipment and systems in Thailand. The company operates in two segments, Sales of Fire Protection Equipment and Systems, and Project Works and Services. Its products include fire protection valves, grooved couplings and fittings, fire hose cabinets and internal accessories, portable fire extinguishers, switches, fire pumps, and pressure gauges; fire suppression systems; fire extinguishing systems; clean agent extinguishing systems; gaseous systems; fire smoke detection equipment; heat detectors; fire alarm equipment; fire alarm control panels; uninterruptible power supplies; and equipment for data center. Firetrade Engineering Public Company Limited was founded in 1999 and is headquartered in Bangkok, Thailand.'
    },
    'FTI.BK': {
        'name': 'Function International Public Company Limited',
        'address': '313 Charoen Phatthana Rd Bang Chan Khlong Sam Wa 10510 Thailand',
        'phone': '66 2 540 6263',
        'website': 'https://www.functioninter.co.th',
        'sector': 'Industrials',
        'industry': 'Pollution & Treatment Controls',
        'description': 'Function International Public Company Limited engages in manufacturing, importing, and wholesaling water purifiers and water systems in Thailand and internationally. It offers household water purifiers, water purifier RO systems, and water filters; commercial water purifiers, water dispensers, water vending machines, and water makers; industrial RO systems and tanks; and pumps and valves. The company sells its products under the Aquatek, Star Pure, Hydro Max, Treatton, Unipure, Fast Pure, BIO MAX, Dosag Pump, Ultratek, CNP, HP Watermaker, PENTAIR, RUN-XIN, SUEZ, and VONTRON brands. Function International Public Company Limited was founded in 1997 and is based in Khlong Sam Wa, Thailand.'
    },
    'FTREIT.BK': {
        'name': 'Frasers Property Thailand Industrial Freehold & Leasehold REIT',
        'address': 'No.944 Mitrtown Office Tower, 22nd - 23rd Floor, Rama 4 Road, Wang Mai Sub-district, Pathum Wan District Bangkok 10330',
        'phone': '66 2 483 0000',
        'website': 'http://www.ftreit.co.th',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'Investing in the freehold and leasehold right of warehouses and factories.'
    },
    'FUTUREPF.BK': {
        'name': 'Future Park Leasehold Property Fund',
        'address': '175 Sathorn City Tower 21st South Sathorn Road Thung Maha Mek, Sathorn Bangkok 10120 Thailand',
        'phone': '662 674 6488',
        'website': 'https://investor.futurepark.co.th/en',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'The Fund has invested in the leasehold right for some portions of the Future Park Rangsit complex. It encompasses all the commercial space and the open area within the shopping complex as well as the wall surfaces outside the building.'
    },
    'GAHREIT.BK': {
        'name': 'Grande Hospitality Real Estate Investment Trust',
        'address': 'Siam Piwat Tower Building 9th and 24th Floors 989 Rama 1 Road Patumwan Bangkok Thailand',
        'phone': '66 2 659 8888',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'GAHREIT invests in the freehold right of land, building and construction as well as system, fixtures and facilities and movable properties of Sheraton Huahin Resort & Spa Project.'
    },
    'GBX.BK': {
        'name': 'Globlex Holding Management Public Company Limited',
        'address': '87/2 CRC All Seasons Place 12th Floor Wireless Road, Lumpini Patumwan Bangkok 10330 Thailand',
        'phone': '66 2 672 5995',
        'website': 'https://www.globlexholding.co.th',
        'sector': 'Financial Services',
        'industry': 'Capital Markets',
        'description': 'Globlex Holding Management Public Company Limited, an investment holding company, engages in securities, investment, and financial advisory businesses in Thailand. The company operates through three segments: Holding Business, Securities Business, and Other Business. The company was incorporated in 2003 and is headquartered in Bangkok, Thailand.'
    },
    'GC.BK': {
        'name': 'Global Connections Public Company Limited',
        'address': '13/1 Moo 2 King-Kaew Road Rachateva Bang Phli 10540 Thailand',
        'phone': '66 2 763 7999',
        'website': 'https://www.gc.co.th',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'Global Connections Public Company Limited operates as distributing agent of plastic and plastic-related products in Thailand. It offers commodity polymers and special additive products; engineering plastic, synthetic rubber, special chemicals, biosurfactant chemicals, and petrochemicals and additives, which are used in petrochemical and plastic transformation process. The company also produces and distributes solar power installed on roof. Global Connections Public Company Limited was founded in 1994 and is headquartered in Bang Phli, Thailand.'
    },
    'GEL.BK': {
        'name': 'General Engineering Public Company Limited',
        'address': '44/2, Moo 2, Tivanon Road Bangkadi Muang Pathumthani Pathum Thani 12000 Thailand',
        'phone': '66 2 501 2020',
        'website': 'https://www.gel.co.th',
        'sector': 'Basic Materials',
        'industry': 'Building Materials',
        'description': 'General Engineering Public Company Limited manufactures and distributes construction materials in Thailand and internationally. The Company operates through three segments: Manufacturing and Distribution of Concrete Products; Construction Services; and Manufacturing and Distribution of PC Wire and PC Strand. It offers prestressed concrete pile products, such as square, I shape, and square hollow core piles; bored piles; soil cement columns; spun concrete piles; precast concrete; segments and girders; post-tensioned slabs; biaxial slabs; and glassfiber reinforced concrete for roofing, cladding, interior decoration, landscape, and other projects. The company also provides construction chemical products for grouting, concrete repair and protection, tiling work, waterproofing, rebar embedding, joint sealant, concrete surface strengthening work, and concrete admixture; and PC wires and strands. In addition, it offers construction and installation, as well as engineering services, including waterproofing system, crack repair, structural reinforcement work, reinforcement steel embedding work, and specialized repair work. General Engineering Public Company Limited was incorporated in 1962 and is headquartered in Pathum Thani, Thailand.'
    },
    'GENCO.BK': {
        'name': 'General Environmental Conservation Public Company Limited',
        'address': '447 Bondstreet Road Bangpood Parkkred Nonthaburi 11120 Thailand',
        'phone': '66 2 502 0900',
        'website': 'http://www.genco.co.th',
        'sector': 'Industrials',
        'industry': 'Waste Management',
        'description': 'General Environmental Conservation Public Company Limited, together with its subsidiaries, engages in the treatment of industrial waste and unavoidable by-products of manufacturing processes in Thailand. The company operates through Treatment of Industrial Waste Business; Property Development Business; and Other Business segments. It collects, stores, and transports hazardous and non-hazardous industrial waste. The company also develops and sells various real estate properties, including residential townhouses, commercial buildings, and condominiums primarily in the greater Bangkok Metropolitan area, as well as buys and sells land. In addition, it develops and operates solar energy power plants, as well as distributes medical equipment. The company was founded in 1994 and is headquartered in Nonthaburi, Thailand.'
    },

    # 201-220
    'GFPT.BK': {
        'name': 'GFPT Public Company Limited',
        'address': '312 Rama 2 Road Bangmod Jomthong Bangkok 10150 Thailand',
        'phone': '66 2 473 8000',
        'website': 'http://www.gfpt.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'GFPT Public Company Limited, together with its subsidiaries, produces and distributes frozen and cooked chicken products in Thailand and internationally. The company is involved in the chicken evisceration activities; producing and distributing processed chicken food and by-products; and operating a feed mill, grandparent chicken farm, parent chicken farm, broiler farm, and hatchery farm. GFPT Public Company Limited was incorporated in 1981 and is headquartered in Bangkok, Thailand.'
    },
    'GGC.BK': {
        'name': 'Global Green Chemicals Public Company Limited',
        'address': '555/1, Energy Complex Building A, 4th Floor Vibhavadi-Rangsit Road Chatuchak Sub-Dist, Chatuchak Dist Bangkok 10900 Thailand',
        'phone': '66 2 558 7300',
        'website': 'http://www.ggcplc.com',
        'sector': 'Basic Materials',
        'industry': 'Chemicals',
        'description': 'Global Green Chemicals Public Company Limited produces, distributes, and transports oleochemical products in Thailand, the Peoples Republic of China, India, Korea, and internationally. The company operates in two segments, Methyl Ester and Fatty Alcohols. It provides methyl ester, which is used as an ingredient in biodiesel as alternative chemicals; ethanol that is used as he renewable energy; and fatty alcohols that are used in various goods, including plasticizers, solvents, flavorings, fragrances, detergents, foam stabilizers, lubricants, cosmetics, plastic intermediates, shampoos, paints and coatings, textile and leather auxiliaries, and printing inks. The company also offers refined glycerine, which is used for pharmaceutical and medical products, creams and lotions, oral care, resins, plastics, and tobacco; and used as a means of emollient to provide lubrication and moisture for personal care products, as well as an emulsifier for other industrial applications. In addition, it provides fatty acid; fatty amine; other alcohols ester; other by-products; and sells raw materials. The company was formerly known as Thai Oleochemicals Company Limited. The company was incorporated in 2005 and is headquartered in Bangkok, Thailand. Global Green Chemicals Public Company Limited is a subsidiary of PTT Global Chemical Public Company Limited.'
    },
    'GIFT.BK': {
        'name': 'Gratitude Infinite Public Company Limited',
        'address': '9/8 Moo 5, Baromratchonnani Road Salathammasop Taweewattana district Bangkok 10170 Thailand',
        'phone': '66 2 888 6800',
        'website': 'http://www.gratitudeinfinite.co.th',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'Gratitude Infinite Public Company Limited, together with its subsidiaries, supplies and distributes chemical products in Thailand. It also produces and distributes supplementary health food; and sells pharmaceutical and medical products, fragrances and skincare-cosmetic products, and health supplements. The company was formerly known as Union Intraco Public Company Limited. The company was founded in 1999 and is headquartered in Bangkok, Thailand. Gratitude Infinite Public Company Limited is a subsidiary of Union Petrochemical Public Company Limited.'
    },
    'GJS.BK': {
        'name': 'G J Steel Public Company Limited',
        'address': '88 PASO Tower 24th Floor Silom Road Suriyawong, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 267 8222',
        'website': 'https://www.gjsteel.co.th',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'G J Steel Public Company Limited manufactures and sells flat-rolled steel products in Thailand. It offers commercial/drawing, structural, pipe, automotive, atmospheric corrosion resistance, and gas cylinder and pressure vessel steel products. The company was formerly known as Nakornthai Strip Mill Public Company Limited and changed its name to G J Steel Public Company Limited in June 2008. G J Steel Public Company Limited was founded in 1994 and is headquartered in Bangkok, Thailand.'
    },
    'GL.BK': {
        'name': 'Group Lease Public Company Limited (Listed company which has possibility to be delisted)',
        'address': '63 Soi 1, Thetsabannimittai Road Ladyao Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 580 7555',
        'website': 'https://grouplease.international',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Group Lease Public Company Limited, together with its subsidiaries, provides hire purchase services and asset-backed loans to consumers in Thailand, Cambodia, Singapore, Laos, Indonesia, and Myanmar. The company offers hire purchase services and asset-backed loans for motorcycles, cars, agricultural machinery and tools, and Trucks. It also provides auction services; microfinance; and business management and consulting services comprising financing to corporates and other investment holding companies, as well as smart dealer business engine, a software that facilitates dealers to record all the information related to sales of motorcycles and create an organized database and other key information of their customers. The company was founded in 1986 and is headquartered in Bangkok, Thailand.'
    },
    'GLAND.BK': {
        'name': 'Grand Canal Land Public Company Limited',
        'address': '161 Rama 9 Road Huay Kwang Sub District Huay Kwang District Bangkok 10310 Thailand',
        'phone': '66 2 246 2323',
        'website': 'http://www.grandcanalland.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate Services',
        'description': 'Grand Canal Land Public Company Limited develops real estate properties in Thailand. It operates through two segments, Real Estate for Sale Business, and Real Estate for Rental and Service Business. The Real Estate for Sale Business segment develops land and house, and residential condominium projects. The Real Estate for Rental and Service Business segment rents office buildings. Grand Canal Land Public Company Limited also operates hotels; and acts as an investment manager. The company was formerly known as Media of Medias Public Company Limited and changed its name to Grand Canal Land Public Company Limited in May 2010. The company was incorporated in 1985 and is headquartered in Bangkok, Thailand. Grand Canal Land Public Company Limited is a subsidiary of CPN Pattaya Company Limited.'
    },
    'GLOBAL.BK': {
        'name': 'Siam Global House Public Company Limited',
        'address': '232 Moo 19 Tambol Robmuang Amphur Mueang Roi Et 45000 Thailand',
        'phone': '66 4 351 9777',
        'website': 'http://www.globalhouse.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Home Improvement Retail',
        'description': 'Siam Global House Public Company Limited engages in the merchandising of construction and decoration materials and equipment in Thailand, Kingdom of Cambodia, and Republic of the Union of Myanmar. It offers mortar; steel; electric appliances; doors and windows; water tanks and plumbing equipment; home improvement and repair equipment; tools and hardware products; TV and stereo; bathroom products; floor and wall products; furniture; electrical equipment; kitchen appliances; agricultural and gardening equipment; lamp and lighting products; painting and chemical products; home decoration products; storage and cleaning equipment; bedroom products; sports and recreation goods; toys and fashion products; consumer goods; and related installation services. The company was founded in 1995 and is headquartered in Mueang Roi Et, Thailand.'
    },
    'GLOCON.BK': {
        'name': 'Global Consumer Public Company Limited',
        'address': 'Soi Praditmanutham 19 2nd Floor 60, Praditmanutham Road Lat Phrao Bangkok 10230 Thailand',
        'phone': '66 2 712 5487',
        'website': 'http://www.glocon.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Global Consumer Public Company Limited, a food conglomerate, provides frozen processed ready-to-eat foods in Thailand. It offers various food products, including frozen and chilled, plant based, hemp, sauce, dried fruit, and processed foods products under the Kitchen plus, Viiva, and LookChin Thip brand names. The company also engages in the manufacture and distribution of packaged food and beverages, such as flexible packaging, polyethylene terephthalate bottle, and vacuum thermoforming. In addition, it is involved in the restaurant; manufacture and sale of seafood; network marketing; trading; manufacture and sale of processed meat; and provision of advertising rental service in gas station. The company was formerly known as NPPG (Thailand) Public Company Limited and changed its name to Global Consumer Public Company Limited in October 2019. Global Consumer Public Company Limited was founded in 1987 and is headquartered in Bangkok, Thailand.'
    },
    'GPI.BK': {
        'name': 'Grand Prix International Public Company Limited',
        'address': 'No. 4/299, Moo 5, Soi Ladplaklao 66 Ladplakhao Road Kwang Anusaovaree Khet Bangkhen Bangkok 10220 Thailand',
        'phone': '66 2 522 1731',
        'website': 'http://www.grandprix.co.th',
        'sector': 'Communication Services',
        'industry': 'Advertising Agencies',
        'description': 'Grand Prix International Public Company Limited operates automotive-related exhibitions in Thailand and internationally. The company organizes events, such as motor sport, quarter mile, off road car, and motorcycle racing activities; and automotive testing, Caravan rally, and safe driving exercise services. It also publishes and distributes auto-related print media, such as Grand Prix, off road, Motorcycle, and XO Autosport magazines, as well as YuadYan newspaper, life style magazine, and Garage Life; and offers broader and digital media services. In addition, the company provides printing services to enterprise customers in various industries, such as fashion, textile, food, real estate, tourism, automobile industries, government, direct sale, etc. Further, it provides advertising media services in printing, television, and website. Additionally, the company produces and distributes books; and invests in power plant business. Grand Prix International Public Company Limited was founded in 1970 and is headquartered in Bangkok, Thailand.'
    },
    'GPSC.BK': {
        'name': 'Global Power Synergy Public Company Limited',
        'address': 'No.555/2 Energy Complex Building B 5th Floor Vibhavadi-Rangsit Road Chatuchak Sub-District, Chatuchak Dist. Bangkok 10900 Thailand',
        'phone': '66 2 140 4600',
        'website': 'http://www.gpscgroup.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Regulated Electric',
        'description': 'Global Power Synergy Public Company Limited, together with its subsidiaries, engages in the production and distribution of electricity, steam, and water for industrial, government and industrial customers in Thailand. The company operates through three segments: Independent Power Producer, Small Power Producer, and Others. It generates electricity through solar, wind, hydropower, and thermal power plants. It owns and operates 4,501 megawatts (MW) of power generation; 3,064 tons of steam; 7,026 cubic meters of industrial water; and 15,400 refrigerated tons of chilled water. Global Power Synergy Public Company Limited was founded in 2013 and is headquartered in Bangkok, Thailand.'
    },
    'GRAMMY.BK': {
        'name': 'GMM Grammy Public Company Limited',
        'address': '50 GMM Grammy PLACE Sukhumvit 21 Road (Asoke) Klongtoey Nua Wattana Bangkok 10110 Thailand',
        'phone': '66 2 669 9000',
        'website': 'http://www.gmmgrammy.com',
        'sector': 'Communication Services',
        'industry': 'Entertainment',
        'description': 'GMM Grammy Public Company Limited, together with its subsidiaries, engages in the music, satellite television, digital television, movies, and home shopping businesses in Thailand. The company operates through three segments, Music, Media, and Others. It is involved in the production, marketing, and distribution of music products, as well as content management; music distribution through physical and digital channels; show business; artist management business; organization of various concerts and music festivals; and copyright and artist management activities. The company also operates digital television channels and radio stations; produces television programs, such as dramas and various other programs; rents studios; and engages in wholesale and retail activities. In addition, it produces and distributes satellite television and digital TV receivers; operates satellite television platforms; and produces movies. Further, the company engages in trading of satellite television set-top-boxes, terrestrial digital TV set-top boxes, and internet TV set-top boxes; music publishing business; digital TV broadcasting activities; and marketing of set-top-boxes and TV sticks. It also operates GR Vocal Studio, an academy for teaching singing, music, acting, and dance school; manages artists, performers, and artists; and offers digital music content through online music streaming platforms. The company was formerly known as Grammy Entertainment Public Company Limited and changed its name to GMM Grammy Public Company Limited in 2001. GMM Grammy Public Company Limited was founded in 1983 and is based in Bangkok, Thailand.'
    },
    'GRAND.BK': {
        'name': 'Grande Asset Hotels and Property Public Company Limited',
        'address': 'Exchange Tower Building 32th Floor Room No. 3203-4 388 Sukhumvit Road, Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 204 9900',
        'website': 'http://www.grandeasset.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'Grande Asset Hotels and Property Public Company Limited, together with its subsidiaries, engages in the hotel, property development, and rental businesses in Thailand. It also manufactures and distributes rubber gloves. The company was formerly known as Grande Asset Development Public Company Limited and changed its name to Grande Asset Hotels and Property Public Company Limited in February 2008. The company was incorporated in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'GREEN.BK': {
        'name': 'Green Resources Public Company Limited',
        'address': '405 Soi 13 Bond Street Road Bang Pood Subdistrict Pak Kret District Nonthaburi 11120 Thailand',
        'phone': '66 2 504 5237',
        'website': 'http://www.greenresources.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Green Resources Public Company Limited, together with its subsidiaries, engages in real estate development business in Thailand. The company focuses on the development and sales of various properties, such as condominiums. It also generates and distributes electricity from solar projects; and sells products with installation of solar-cell systems. The company was formerly known as Asia Corporate Development Public Company Limited and changed its name to Green Resources Public Company Limited in February 2016. Green Resources Public Company Limited was founded in 1992 and is headquartered in Nonthaburi, Thailand.'
    },
    'GROREIT.BK': {
        'name': 'Grande Royal Orchid Hospitality Real Estate Investment Trust with Buy-Back Condition',
        'address': '9th and 24th Floor, Siam Piwat Tower Building, 989 Rama 1 Road, Pathumwan Bangkok 10330',
        'phone': '66 2 659 8888',
        'website': 'http://www.one-asset.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Hotel & Motel',
        'description': 'The trust invests in the freehold right of the Royal Orchid Sheraton Hotel and Tower. Royal Orchid Hotel (Thailand) Public Company Limited (ROH) as former owner shall be lessee and buyer for asset buy-back. The period of leasing is for 3 years and shall be renew the term of 2 times, for 1 year each. The trust has condition of selling asset to ROH at the end of year 3-5.'
    },
    'GSTEEL.BK': {
        'name': 'G Steel Public Company Limited (Listed company which has possibility to be delisted)',
        'address': '88 PASO Tower, 18th Floor, Silom Road, Suriyawong, Bangrak Bangkok 10500',
        'phone': '66 2 634 2222',
        'website': 'http://www.gsteel.com',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'The Company is the producer and distributor of hot rolled coil and slab. Its products serve as raw materials for such downstream industries as cold rolled coils, galvanized steel, steel pipe, structural steel products for construction, LPG container, automobile, electrical appliance as well as steel furniture industries.'
    },
    'GULF.BK': {
        'name': 'Gulf Energy Development Public Company Limited',
        'address': 'M.Thai Tower 11th Floor All Seasons Place 87 Wireless Road, Lumpini, Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 080 4499',
        'website': 'http://www.gulf.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Gulf Energy Development Public Company Limited generates and sells electricity and steam to public and private clients in Thailand and internationally. It operates through four segments: Power Business, Consulting Business, Infrastructure Business, and Satellite Business. The company generates electricity through gas-fired, solar, biomass, and wind power projects under the independent power producers and small power producers. It also undertakes infrastructure projects; distributes, supplies, and sells natural gas; and operates a digital infrastructure. In addition, the company is involved in the management, technical support, technology, investment, and trading services; storing and converting natural gas; satellite and related services; sale of direct television and satellite equipment; transponder services; engineering and development services; broadband network and content services; and broadcasting, television, and telecommunication services. Further, it provides system integration consultancy services for broadband network. Gulf Energy Development Public Company Limited was founded in 2007 and is headquartered in Bangkok, Thailand.'
    },
    'GUNKUL.BK': {
        'name': 'Gunkul Engineering Public Company Limited',
        'address': '1177, Pearl Bangkok Building 8th Floor Phahonyothin Road Phayathai Bangkok 10400 Thailand',
        'phone': '66 2 242 5800',
        'website': 'http://www.gunkul.com',
        'sector': 'Industrials',
        'industry': 'Conglomerates',
        'description': 'Gunkul Engineering Public Company Limited engages in manufacturing and distribution of equipment for electrical systems in Thailand, Japan, Vietnam, and internationally. It operates through four segments: Manufacturing and Selling of Equipments for Electrical Systems; Generating and Selling Electricity; Construction Service; and Maintenance Service, Rental Service, and Others. The company is involved in the construction and investing in the generating and selling electricity business; producing and distributing power from renewable energy sources, such as solar farm, solar PV rooftop, wind farm, biomass, and floating solar; engineering, procurement, and construction for solar and wind power plant, submarine cable, microgrid, and bypass cable; operation and maintenance of solar roofs; as well as solar installation business on the roof of factory, commercial buildings, residential group, organizations and government agencies. It also offers cables and accessories, fuses and switches, hardware and connectors, insulators, lightning protection products, service and maintenance equipment, tools and instruments, live part covers and animal protection systems, grounding systems, lightening and control products, and hardware products for transmission lines, substations, distribution lines, and low voltage lines. Gunkul Engineering Public Company Limited was founded in 1982 and is headquartered in Bangkok, Thailand.'
    },
    'GVREIT.BK': {
        'name': 'Golden Ventures Leasehold Real Estate Investment Trust',
        'address': '22nd Floor, Mitrtown Office Tower 944 Rama Rama 4 Road, Wangmai , Pathumwa Bangkok 10330 Thailand',
        'phone': '66 2 483 0000',
        'website': 'http://www.gvreit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Office',
        'description': 'Golden Ventures Leasehold Real Estate Investment Trust, a real estate investment trust, engages in the rental of properties in Thailand. It holds leasehold rights of Park Ventures Ecoplex building, as well as land and building sub-lease rights of Sathorn Square located at the Central Business District of Thailand. The company has elected to be taxed as a real estate investment trust. As a result, it would not be subject to corporate income tax on that portion of its net income that is distributed to shareholders. The company was founded in 2016 and is based in Bangkok, Thailand.'
    },
    'GYT.BK': {
        'name': 'Goodyear (Thailand) Public Company Limited',
        'address': '50/9 Moo 3, Phaholyothin Road, K.M. 36 Klongnueng Klongluang Pathum Thani 12120 Thailand',
        'phone': '66 2 909 8080',
        'website': 'http://www.goodyear.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Auto Parts',
        'description': 'Goodyear (Thailand) Public Company Limited manufactures, distributes, and sells motor vehicle and aero tires in Thailand. It provides private automobile tires, and small and large truck tires for commercial use; and aviation tires and tire retreads. The company also exports its products. The company was incorporated in 1968 and is based in Pathum Thani, Thailand. Goodyear (Thailand) Public Company Limited operates as a subsidiary of The Goodyear Tire & Rubber Company.'
    },
    'HANA.BK': {
        'name': 'Hana Microelectronics Public Company Limited',
        'address': '65/98, Soi Vibhavadi-Rangsit 64 Junction 2 Kwang Talad Bangkhen Khet Laksi Bangkok 10210 Thailand',
        'phone': '66 2 551 1297',
        'website': 'https://www.hanagroup.com',
        'sector': 'Technology',
        'industry': 'Electronic Components',
        'description': 'Hana Microelectronics Public Company Limited, together with its subsidiaries, provides electronic manufacturing services. The company manufactures chip-on-board and printed circuit board assemblies, integrated circuit assemblies and tests, and liquid crystal on silicon devices. It also manufactures radio frequency identification devices (RFID), MEMS, and high-temperature polysilicon products. In addition, the company offers agent and customer services; and trades in electronic components. It has operations in Singapore, the United States, China, Malaysia, Switzerland, and internationally. Hana Microelectronics Public Company Limited was founded in 1978 and is headquartered in Bangkok, Thailand.'
    },

    # 221-240
    'HENG.BK': {
        'name': 'Heng Leasing and Capital Public Company Limited',
        'address': '69 Moo 7 Tambon Sansai Noi Amphur Sansai San Sai 50210 Thailand',
        'phone': '66 2 153 9587',
        'website': 'https://www.hengleasing.com/',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Heng Leasing and Capital Public Company Limited provides financial services in Thailand. The company offers hire purchase, loans secured against vehicle registrations, land and building loans, personal loans, and nano finance without collateral, as well as non-life and life insurance brokerage services. It operates through 617 branches. The company was founded in 2015 and is headquartered in San Sai, Thailand.'
    },
    'HFT.BK': {
        'name': 'Hwa Fong Rubber (Thailand) Public Company Limited',
        'address': '317 Moo 4, Soi 6C Bangpoo Industrial Estate Praksa Subdistrict Muang Samut Prakan District Samut Prakan 10280 Thailand',
        'phone': '66 2 709 6580',
        'website': 'http://www.duro.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Auto Parts',
        'description': 'Hwa Fong Rubber (Thailand) Public Company Limited, together with its subsidiaries, manufactures and distributes tires and tubes in Thailand, rest of Asia, Europe, the United States, and internationally. The company operates in two segments, Sale of Goods and Services, and Investment. It offers tires and tubes for bicycles, motorcycles, and small logistics vehicles. The company markets its products under the DUNLOP, DURO, Q-UICK, and PREMIUM HFT trademarks. It is also involved in investing in bonds and securities; and the wholesale and retail trade of tires and tubes, and equipment. The company was founded in 1987 and is headquartered in Samutprakarn, Thailand. Hwa Fong Rubber (Thailand) Public Company Limited is a subsidiary of Hwa Fong Rubber Industries Company Limited.'
    },
    'HMPRO.BK': {
        'name': 'Home Product Center Public Company Limited',
        'address': '31 Prachachuen-Nonthaburi Road Bangkhen Amphoe Muang Nonthaburi Thailand',
        'phone': '66 2 832 1000',
        'website': 'http://www.homepro.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Home Improvement Retail',
        'description': 'Home Product Center Public Company Limited operates as a home improvement retailer in Thailand, Malaysia, and Vietnam. The company trades in goods and materials for construction, extension, refurbishment, renovation, and improvement of buildings, houses, and residences; and range of related services. It also offers 3D, installation, maintenance, home makeover, cleaning, warehousing, and distribution services. In addition, the company leases space. The company was founded in 1995 and is headquartered in Nonthaburi, Thailand.'
    },
    'HPF.BK': {
        'name': 'Hemaraj Industrial Property and Leasehold Fund',
        'address': '199 Column Tower Ground Floor & 21st-23rd Floor Ratchadapisek Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 649 2000',
        'website': 'http://www.mfcfund.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'The Fund has invested in freehold right of land and factory of 47 units, which have area of 95,941 square meters, (64 percentage of factory area) and Leasehold right of land and factory of 57 units, which have area of 54,176 square meters (36 percentage of factory area).'
    },
    'HTC.BK': {
        'name': 'Haad Thip Public Company Limited',
        'address': '87/1, Kanchanavanich Road Thambol Banphru Amphur Hadyai Songkhla 90250 Thailand',
        'phone': '66 7 421 0008',
        'website': 'https://www.haadthip.com',
        'sector': 'Consumer Defensive',
        'industry': 'Beverages—Non-Alcoholic',
        'description': 'Haad Thip Public Company Limited manufactures and distributes soft drinks in Thailand and internationally. The company offers sparkling beverages under the Coca-Cola, Fanta, Sprite, Schweppes, and A&W trademarks; and non-carbonated/still beverages under the Minute Maid, Namthip, fuzetea, and Bon Aqua trademarks. It also manufactures and distributes plastic bottles and semi-finished plastic bottles, as well as provides plastic bottles blowing services; manufactures and distributes food products and consumer goods; and engages in the restaurant and real estate development businesses. The company was incorporated in 1994 and is headquartered in Songkhla, Thailand.'
    },
    'HTECH.BK': {
        'name': 'Halcyon Technology Public Company Limited',
        'address': '41 Moo14 Bangchan Industrial Estate Soi 6, Serithai Road Minburi Bangkok 10510 Thailand',
        'phone': '66 2 906 3242',
        'website': 'https://www.halcyon.co.th',
        'sector': 'Industrials',
        'industry': 'Tools & Accessories',
        'description': 'Halcyon Technology Public Company Limited, together with its subsidiaries, manufactures, distributes, imports, and sells cutting tools, jig and fixtures, and custom metallic devices in Thailand and internationally. The company offers polycrystalline diamond (PCD) drills, reamers, endmills, face mills, hollow tools, brazed tools, inserts, boring bars, wear parts, wear parts, and other special tools; wheel dressers; polycrystalline carbon boron nitride (PCBN) inserts and boring tools; monocrystalline cutting tools; and special carbide cutting tools, such as carbide drills, reamers, endmills, inserts, boring tools, and other tools. It also provides customized metal fabricated products, such as tool holders, jigs and fixtures, and other high-precision parts. It serves hard disk drive parts, automotive, aerospace, lens, and watch and jewelry industries. The company was founded in 2002 and is based in Bangkok, Thailand.'
    },
    'HUMAN.BK': {
        'name': 'Humanica Public Company Limited',
        'address': '2 Soi Rongmuang 5 Rongmuang Road Rongmuang Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 636 6999',
        'website': 'http://www.humanica.com',
        'sector': 'Technology',
        'industry': 'Software—Application',
        'description': 'Humanica Public Company Limited provides human resource services and solutions in Thailand, Singapore, Japan, Malaysia, Indonesia, Myanmar, Vietnam, Philippines, and internationally. It operates through five segments: Human Resource Management System Services; Enterprise Resource Planning Services; Accounting and Financing; Sales of Advance Access Control Devices; and Life and Non-Life Insurance Broker. The company offers various solutions, such as Workplaze, an employee-centric HR solution; Workplaze Payroll; Workplaze Time; Workplaze Benefit; Workplaze Training; Workplaze Talent Management; Workplaze Recruitment; Workplaze Analytics and Reporting; Workplaze Attendance Recording; and Workplaze Mobile, as well as Enterprise Resource Planning (ERP) system implementation solutions. It also provides accounting and financial services; visa and work permit service, and company registration services; software-as-a-service (SaaS); consulting; and project implementation services. In addition, the company offers payroll outsourcing services; implementation services for human resource systems and computer software for enterprise resource planning; life and non-life insurance brokerage services. Further, it sells advance access control devices. The company was founded in 2003 and is headquartered in Bangkok, Thailand.'
    },
    'HYDROGEN.BK': {
        'name': 'HYDROGEN Freehold And Leasehold Real Estate Investment Trust',
        'address': '944 Mitrtown Office Tower, 29 Floor, Room No. 2907-2910, Rama 4 Road, Wang Mai, Pathumwan Bangkok',
        'phone': '66 2 219 1675',
        'website': 'http://www.hydrogenreit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'Investment in leasehold rights in some land and factory buildings in Saha Group Industrial Park - Si Racha project, Kabinburi project, Mae Sot project and ownership of some land and warehouses in Tiger Suvarnabhumi DC project.'
    },
    'ICC.BK': {
        'name': 'I.C.C. International Public Company Limited',
        'address': '530 Soi Sathupradit 58 Road Bang Phong Phang subdistrict Yannawa district Bangkok 10210 Thailand',
        'phone': '66 2 293 9000',
        'website': 'http://www.icc.co.th',
        'sector': 'Consumer Cyclica',
        'industry': 'Apparel Retai',
        'description': 'I.C.C. International Public Company Limited, together with its subsidiaries, engages in the distribution of fashion consumer products in Thailand and internationally. The company operates through four segments: Cosmetics Toiletries & Perfumeries; Womens Apparel; Mens Apparel; and Household Products. It offers tops, pants, blazers, dresses, skirts, sportswear, lingerie and night wear, maternity wear, bags, shoes, accessories, cosmetics, and other products for women; and shirts and T-shirts, trousers, jackets, sportswear, underwear, blazers and suits, bags, shoes, accessories, and other products for men. The company also provides tops, pants, skirts, underwear, bags, shoes, accessories, beds, and other products for kids and babies, as well as products for newborn. It sells its products through department stores and various stores. The company was formerly known as International Cosmetics Public company Limited and changed its name to I.C.C. International Public Company Limited in 1996. I.C.C. International Public Company Limited was founded in 1964 and is headquartered in Bangkok, Thailand.'
    },
    'ICHI.BK': {
        'name': 'Ichitan Group Public Company Limited',
        'address': 'No. 8 T-One Building 42nd – 44th Floor Sukhumvit 40 Alley Kwang Phra Khanong, Khet Khlong Toei Bangkok 10110 Thailand',
        'phone': '66 2 023 1111',
        'website': 'Consumer Defensive',
        'sector': 'Consumer Defensive',
        'industry': 'Beverages—Non-Alcoholic',
        'description': 'Ichitan Group Public Company Limited engages in manufacture and sale of beverages in Thailand and internationally. The company offers ready to drink green tea under the Ichitan Green Tea; herbal drink under the Yen Yen by Ichitan brand; green tea with chewy cube of coconut under the Ichitan Chew Chew brand; and fruit juices and jellies under the Bireleys brand. It also provides ready to drink black tea. The company was formerly known as Mai Tan Company Limited. Ichitan Group Public Company Limited was incorporated in 2010 and is headquartered in Bangkok, Thailand.'
    },
    'IFEC.BK': {
        'name': 'Inter Far East Energy Corporation Public Company Limited (Listed company which has possibility to be delisted)',
        'address': 'No. 33/4, The Nine Tower, 29 th Floor, Rama IX Road., Huai Khwang Sub-district, Huai Khwang District Bangkok 10310',
        'phone': '66 2 168 1378',
        'website': 'http://www.ifec.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Investing in subsidiaries to produce and distribute electricity from renewable energy, waste management and hotel business'
    },
    'IFS.BK': {
        'name': 'IFS Capital (Thailand) Public Company Limited',
        'address': 'Lumpini Tower 20th Floor 1168/55 Rama IV Road Tungmahamek, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 285 6326',
        'website': 'http://www.ifscapthai.com',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'IFS Capital (Thailand) Public Company Limited provides factoring, leasing, hire purchase, and other financial services in Thailand, Singapore, Malaysia, and Indonesia. The company offers factoring services for traders; manufacturers including electronics, packaging, automobile parts, plastic products, etc.; and service companies, such as advertising agency, security guard, manpower supply, etc. It also provides leasing and hire purchase for industrial machinery, various vehicles including truck, trailer, van, forklift, executive car, etc., and used equipment; supply chain finance; other services, which include confirming LC/TR, inventory financing, floor plan, contract financing, block discounting, and group digital marketing services; and e-factoring services. In addition, the company serves small and medium-sized enterprises in various industries, such as service comprising recruitment/human resource, food and beverages, medicine, motor vehicles and auto parts, paper and packaging, electric appliances, construction and building materials, plastic, and electronic parts. IFS Capital (Thailand) Public Company Limited was incorporated in 1991 and is based in Bangkok, Thailand.'
    },
    'IHL.BK': {
        'name': 'Interhides Public Company Limited',
        'address': '678 Soi T.J.C. Sukhumvit Road Bangpoomai Mueang Samut Prakan 10280 Thailand',
        'phone': '66 2 2897 2837',
        'website': 'http://www.interhides.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Auto Parts',
        'description': 'Interhides Public Company Limited manufactures and distributes leather coverings for car seats and other related products in Thailand, China, Japan, Vietnam, Indonesia, Malaysia, India, England, and internationally. It offers finished leather products, cut parts, and trim covers for use in car seats, steering wheels, gear knobs, and safety shoes. The company also provides spray and tanning services; and bleaching, dyeing finishing, and other services. In addition, it manufactures and distributes hydrolyzed protein from leather scrap; and dog chew products. The company also exports its products. It primarily serves the automotive industry, as well as furniture makers, dog chew makers, etc. The company was founded in 1945 and is headquartered in Mueang Samut Prakan, Thailand.'
    },
    'III.BK': {
        'name': 'Triple i Logistics Public Company Limited',
        'address': '628 Triple i Building 3rd Floor Soi KlabChom, Nonsee Road Chongnonsee, Yannawa Bangkok 10120 Thailand',
        'phone': '66 2 681 8700',
        'website': 'http://www.iii-logistics.com',
        'sector': 'Industrials',
        'industry': 'Integrated Freight & Logistics',
        'description': 'Triple i Logistics Public Company Limited, together with its subsidiaries, provides domestic and international freight forwarding and integrated logistics services. It operates through Air Freight; Sea and In-Land Freight Logistics Management; Chemical and Hazardous Goods Logistics; and Other Management Services segments. The company offers air freight services, such as wholesale air freight, forwarding, general sales agency for airlines, and airport cargo terminal services; sea freight and inland transportation services, including shipping line agency, less than container load, and inland container transport services; logistics management, and warehouse and distribution services; and chemical and specialty logistics services, such as hazardous and dangerous goods logistics integrating, and dangerous goods packaging solutions. It also provides packaging services. In addition, the company offers office rental and other management services. Triple i Logistics Public Company Limited was incorporated in 2017 and is headquartered in Bangkok, Thailand.'
    },
    'ILINK.BK': {
        'name': 'Interlink Communication Public Company Limited',
        'address': '48 Interlink Building Soi Rung Reung Ratchadapisek Road, Samsennok Huay Khwang Bangkok 10310 Thailand',
        'phone': '66 2 666 1111',
        'website': 'http://www.interlink.co.th',
        'sector': 'Technology',
        'industry': 'Communication Equipment',
        'description': 'Interlink Communication Public Company Limited imports and distributes IT network cabling system products in Thailand. The company operates through three segments: Distribution Business, Telecommunication Business, and Engineering Business. It also outsources the design and installation service of network and cabling systems for computers and telecommunications. In addition, the company operates as a telecommunication service provider, which invests in the construction of a fiber-optic cable network to provide high-speed leased line service; and a contractor in submarine cable and transmission lines, including fiber optic and high voltage. Further, it provides data center services, such as co-location, cloud computing, and disaster recovery services. Interlink Communication Public Company Limited was founded in 1995 and is headquartered in Bangkok, Thailand.'
    },
    'ILM.BK': {
        'name': 'Index Living Mall Public Company Limited',
        'address': 'No. 147, Soi Rama 2 Soi 50, Rama 2 Road Samae Dam Subdistrict Bang Khun Thian District Bangkok 10150 Thailand',
        'phone': '66 2 898 6420',
        'website': 'http://www.indexlivingmall.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Furnishings, Fixtures & Appliances',
        'description': 'Index Living Mall Public Company Limited engages in the retail and wholesale of furniture, electronic, and home decorative products in Thailand. It operates through four segments: Retail of Furniture, Manufacturing of Furniture, Rental Area and Service, and Others. The company is also involved in the manufacture, import, export, and distribution of furniture and home appliances; and warehouse rental activities, as well as in the franchise business. The company was founded in 1973 and is headquartered in Bangkok, Thailand.'
    },
    'IMPACT.BK': {
        'name': 'Impact Growth Real Estate Investment Trust',
        'address': '47/569-576 Moo 3, New Geneva Building 10th Floor Popular Road 3 Banmai, Pakkred Nonthaburi 11120 Thailand',
        'phone': '66 2 833 5589',
        'website': 'http://www.impactgrowthreit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Specialty',
        'description': 'IMPACT Growth Real Estate Investment Trust is a real estate investment trust externally managed by RMI Company Limited. It invests in real estate markets of Thailand. The firm invests in freehold right of Building Exhibition and Conference of IMPACT Muang Thong Thani. IMPACT Growth Real Estate Investment Trust is domiciled in Thailand.'
    },
    'INET.BK': {
        'name': 'Internet Thailand Public Company Limited',
        'address': 'No. 1768, Thai Summit Tower 10th-12th Floors, and IT Floor New Petchburi Road Bangkapi Sub-district, Huay Khwang District Bangkok 10310 Thailand',
        'phone': '66 2 257 7000',
        'website': 'http://www.inet.co.th',
        'sector': 'Technology',
        'industry': 'Information Technology Services',
        'description': 'Internet Thailand Public Company Limited, together with its subsidiaries, provides Internet access, and information and communication technology services for businesses and individuals in Thailand. It operates through two segments, Access Business and Business Solutions. The company offers INET data center solutions, including co-location and business continuity planning center; cloud solutions, such as virtual machine as a service, backup as a service, disaster recovery as a service, database as a service, hybrid cloud, SAP HANA as a services, container as a service, and web hosting services; and smart office solutions comprising file sharing as a services, desktop as a service, and document management system. It also provides security as a service, including INET VFW, a computer network security system; INET iLog, a traffic data storage on computer; and INET Hybrid WAN, a network connection from different locations to the center infrastructure. In addition, the company offers NET Cloud Connect, which links the networks from different locations to the central infrastructure; INET NODE, a leased line; INET Load Balance, a system management to minimize the unnecessary expenses; and INET WebEx, an eMeeting for the efficient online meeting. Further, it provides smart solution, such as artificial intelligence, chatbot as a service, analytics as a service, and big data as a service. The company was founded in 1995 and is based in Bangkok, Thailand.'
    },
    'INETREIT.BK': {
        'name': 'Inet Leasehold Real Estate Investment Trust',
        'address': '1768 Thai Summit Tower, 24th Floor, New Petchaburi Road, Bang Kapi Sub-district, Huay Khwang District Bangkok 10310',
        'phone': '66 2 257 7000',
        'website': 'http://www.inetreit.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Diversified',
        'description': 'Investment in ownership of buildings and equipment related to the operation of Data Center INET-IDC3 Phase 1 project and the leasehold right of the land which the substation building is located.'
    },
    'INGRS.BK': {
        'name': 'Ingress Industrial (Thailand) Public Company Limited',
        'address': 'No. 9/141 UM Tower 14th Floor, Unit A 1 Ramkhamhaeng Road Suanluang Bangkok 10250 Thailand',
        'phone': '66 2 719 9644',
        'website': 'http://www.ingress.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Auto Parts',
        'description': 'Ingress Industrial (Thailand) Public Company Limited, an investment holding company, engages in the manufacture and distribution of automotive components in Thailand, Malaysia, Indonesia, and India. The company offers roll forming products, which include door module comprising door, lower, and inner sash, and glass guide; sealing system products, such as windshield, beltline, and roof drip; and exhaust system products consisting of EGR and collapsible pipes and bellow. It also provides stamping products including module assembly products, such as apron front fender sub module assembly, front end module, panel assembly rare wheel housing outer, body lower back, and module assembly; heat management products comprising heat manifold and protectors; under body products including cross beam and side sill outer; side structure comprising pillar body and pillar inner, and side structure; and other products, such as brake plates, door hinge, trapezoidal and stamped impact beam products. In addition, the company offers die making products, which include cam camber, sear recliner, upper, and lower die; and automation solutions, such as automated guided vehicle, production monitoring system, autonomous robotic, cobot, manufacturing execution system, smart factory, specialized machinerie, testing equipment, jigs and fixtures, and engineering services. The company was founded in 2014 and is headquartered in Bangkok, Thailand.'
    },

    # 241-260
    'INOX.BK': {
        'name': 'POSCO-Thainox Public Company Limited',
        'address': '622 Emporium Tower Floor 15/6-8 Sukhumvit Road Klongton, Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 494 3130',
        'website': 'http://www.poscothainox.com',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'POSCO-Thainox Public Company Limited produces, sells, and exports cold-rolled stainless steel products in Thailand and internationally. It offers austenitic and ferritic stainless steel products used as raw material in the production of automotive and transportation parts; electrical home appliances; household appliances; food processing and medical equipment; heavy industry, energy, and environmental equipment; and architecture, decoration, and construction equipment. The company was formerly known as Thainox Stainless Public Company Limited and changed its name to POSCO-Thainox Public Company Limited in 2011. The company was founded in 1990 and is headquartered in Bangkok, Thailand. POSCO-Thainox Public Company Limited is a subsidiary of POSCO Co., Ltd.'
    },
    'INSET.BK': {
        'name': 'Infraset Public Company Limited',
        'address': 'No. 165/37-39 Ramintra Road Anusawari Bang Khen Bangkok 10220 Thailand',
        'phone': '66 2 092 7444',
        'website': 'http://www.infraset.co.th',
        'sector': 'Technology',
        'industry': 'Information Technology Services',
        'description': 'Infraset Public Company Limited constructs data centers, information technology and infrastructure, and telecommunication networks in Thailand. It offers design, engineering, and construction services for data center information technology; consulting, survey, design, installation, and system management services, as well as maintenance and supervision services for installation of telecommunications infrastructure and network equipment; and maintenance and services for structural engineering systems, as well as transportation infrastructure services. The company was incorporated in 2006 and is headquartered in Bangkok, Thailand.'
    },
    'INSURE.BK': {
        'name': 'Indara Insurance Public Company Limited',
        'address': 'No. 364/29, Sri Ayuthaya Road Thanon Phaya Thai Subdistrict Ratchathewi District Bangkok 10400 Thailand',
        'phone': '66 2 247 9261',
        'website': 'http://www.indara.co.th',
        'sector': 'Financial Services',
        'industry': 'Insurance—Property & Casualty',
        'description': 'Indara Insurance Public Company Limited provides non-life insurance services in Thailand. It offers fire, marine and transportation, motor, personal accident, health, and other insurance products. The company was formerly known as Inter life Insurance Company Limited. Indara Insurance Public Company Limited was founded in 1949 and is headquartered in Bangkok, Thailand. Indara Insurance Public Company Limited is a subsidiary of Rod Dee Det Auto Company Limited.'
    },
    'INTUCH.BK': {
        'name': 'Intouch Holdings Public Company Limited',
        'address': '87 M.Thai Tower 27th Floor Unit 2 All Seasons Place, Wireless Road Lumpini Sub-district, Pathumwan District Bangkok 10330 Thailand',
        'phone': '66 2 118 6900',
        'website': 'http://www.intouchcompany.com',
        'sector': 'Communication Services',
        'industry': 'Telecom Services',
        'description': 'Intouch Holdings Public Company Limited, through its subsidiaries, engages in the satellite, Internet, telecommunications, and media and advertising businesses. It operates through Local Wireless Telecommunications, Satellite and International Businesses, and Other Businesses segments. The company offers broadband content services; satellite uplink-downlink, broadcasting television and telecommunication services; online data communications through telephone landline and optical fiber, and telecom and network operator; broadcasting network services; Internet data center; advertising, insurance broker, and other related services; and telephone network and engineering development services on communication technology and electronics. It also operates transponder services for domestic and international communications; sells user terminals of IPSTAR and direct television equipment; and distributes internet equipment. In addition, the company offers local mobile telecommunication services; and trades in and rents telecommunications equipment and accessories. It has operations in Thailand, Australia, India, Japan, Myanmar, Malaysia, and internationally. The company was formerly known as Shin Corporation Public Company Limited and changed its name to Intouch Holdings Public Company Limited in March 2014. The company was founded in 1983 and is headquartered in Bangkok, Thailand.'
    },
    'IRC.BK': {
        'name': 'Inoue Rubber (Thailand) Public Company Limited',
        'address': 'No. 258, Soi Rangsit-Nakornnayok 49 Prachathipat sub-district Thunyaburi Pathum Thani 12130 Thailand',
        'phone': '66 2 996 0890',
        'website': 'http://www.ircthailand.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Auto Parts',
        'description': 'Inoue Rubber (Thailand) Public Company Limited engages in the research, development, manufacture, and distribution of motorcycle tires and tubes in Thailand and internationally. The company also provides industrial elastomer rubber parts, including rubber bushing, railway rubber, housing gasket, rubber chip, grommet, rubber level crossing, hole protection, covers, cushion rubber, rubber protector, trim bonnet rear, and rubber isolator for sport track, agriculture and fishery, infrastructure project, construction, and other industries. It also offers automotive elastomer products, such as hose air intake, socket covers, lamp and lens gasket, door and front grommets, column hole/cover assy-hole, weather strip inner and hood, shield fuel tank, gauge oil level, door stoppers, trunk lids, weather strip front window, rubber strap and mirror, and plug for automotive industry; and cover rubbers, socket body products, rubber seats, grommets, guide chains, chain guards, vale comp inlets, rollers, sprockets, O-ring, float, pealing fuel, and rubber bushes for motorcycle industry. In addition, the company provides cooling machine rubber cushions for electrical appliances, construction material, container seals, and other products. Further, it manufactures, repairs, and modifies metal molds and equipment for the production of motorcycle tires, tubes, and automotive rubber parts. The company also exports its products. The company was founded in 1969 and is headquartered in Pathum Thani, Thailand.'
    },
    'IRPC.BK': {
        'name': 'IRPC Public Company Limited',
        'address': '555/2 Energy Complex Building B, 6th Floor Vibhavadi Rangsit Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 765 7000',
        'website': 'https://www.irpc.co.th',
        'sector': 'Energy',
        'industry': 'Oil & Gas Refining & Marketing',
        'description': 'IRPC Public Company Limited, together with its subsidiaries, provides petroleum and petrochemical products in Thailand, Singapore, and internationally. The company operates through Petroleum Products, Petrochemical Products, and Other Business segments. It offers petroleum products, including liquefied petroleum gas, gasohol, gasoline base, diesel, diesel base, gasoline, fuel oil, lube base oil, slack wax, aromatic extract, treated distillate aromatic extract and residue aromatic extract, asphalt, straight-run fuel oil, white spirit, C9 aromatic/aromatic, toluene, xylene, mixed xylenes; and polyethylene, polypropylene, acrylonitrile-butadiene-styrene, acrylonitrile styrene, polystyrene, expandable polystyrene, and additives. It also generates and distributes electricity, power, steam, industrial water, and air systems; and wastewater treatment services for industrial customers. In addition, the company offers port and tank services, such as tugboats, piloting services, lighters, fresh water and fuel, weigh scales, container yards, warehouses, and machines and equipment for the transshipment of goods. Further, it is involved in the provision of asset management and oil vessel renting services; manufacture and distribution of plastic resins; operation of vocational schools; distribution of non-woven fabric products and medical consumables; and distribution of petrochemical products, as well as power plant, jetty, and other utilities operations. The company was formerly known as Thai Petrochemical Industry Public Company Limited and changed its name to IRPC Public Company Limited in October 2006. IRPC Public Company Limited was incorporated in 1978 and is headquartered in Rayong, Thailand.'
    },
    'IT.BK': {
        'name': 'IT City Public Company Limited',
        'address': 'The Palladium World Shopping Mall 555 B1, B2, 5th Floor Ratchaprarop Road Makkasan, Ratchathew Bangkok 10400 Thailand',
        'phone': '66 2 656 5030',
        'website': 'http://www.itcity.co.th',
        'sector': 'Technology',
        'industry': 'Electronics & Computer Distribution',
        'description': 'IT City Public Company Limited engages in the retail of computers, tablets, peripherals, smartphones, and other related IT products under the IT CITY name. The company also offers Internet of Thing and gaming devices; IP, car, and action cameras; robots; 3G/4G air cards; mouse, keyboards, and computer software; ink and toner cartridges, printing paper, UPS, power banks, and power extension outlets; loudspeakers, headphones, optical drives, CD/DVD, hard disks, computer components, network equipment, and cables; carry bags and smart phone accessories; digital LED TVs and home audio video devices; office equipment, photo copiers, sticker cutting machines, label printers, barcode scanners, projectors, etc.; small home appliances, such as air purifiers, small kitchen utensils, etc.; desktops, notebooks, and LCD and LED monitors; wearable devices; and printers, including ink jet, dot matrix, laser, and multi-function printers. In addition, it operates repair and maintenance service centers; supplies genuine parts; and provides technicians. IT City Public Company Limited was incorporated in 2002 and is headquartered in Bangkok, Thailand.'
    },
    'ITC.BK': {
        'name': 'i-Tail Corporation Public Company Limited',
        'address': '979/92-94, S.M.Tower 29th Floor Phaholyothin Rd, Phayathai Sub-Dist. Phayathai District Bangkok 10400 Thailand',
        'phone': '66 2 298 0029',
        'website': 'http://www.i-tail.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'i-Tail Corporation Public Company Limited, together with its subsidiaries, manufactures, distributes, and exports canned seafood and animal feeds. The company operates through three segments: Pet Food; Ambient Seafood and Value-Added; and Other Products. It manufactures and distributes tuna and canned seafood; and imports and distributes pet food and pet related products. The company also provides wet and dry food products and treats for dog and cat; and wet cat food products made from fresh meat and seafood, such as tuna, shrimp, or salmon. It offers its products under the Bellotta, Marvo, ChangeTer, Calico Bay, and Paramount brands in Thailand, the United States, Australia, the Middle East, European countries, and internationally. The company was formerly known as Songkla Canning Public Company Limited and changed its name to i-Tail Corporation Public Company Limited in September 2021. The company was founded in 1981 and is headquartered in Bangkok, Thailand. i-Tail Corporation Public Company Limited is a subsidiary of Thai Union Group Public Company Limited.'
    },
    'ITD.BK': {
        'name': 'Italian-Thai Development Public Company Limited',
        'address': '2034/132-161 Italthai Tower  New Petchburi Road Bangkapi Huaykwang Bangkok 10310 Thailand',
        'phone': '66 2 716 1600',
        'website': 'http://www.itd.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'Italian-Thai Development Public Company Limited, together with its subsidiaries, engages in the construction business in Thailand, India, Bangladesh, and internationally. It provides soil and coal extraction, and removal services; construction support services; and foundation and piling work services. The company also manufactures, distributes, and sells concrete products and cement; manufactures and distributes steel pipes; produces and sells vessels and equipment; manufactures, distributes, and installs concrete sheets; and holds concession for constructing ports and railways. In addition, it engages in real estate development; investments in other projects; production and distribution of electricity; leasing and sale of sheet piles and beams for foundation construction work; and rock quarrying, processing, and distribution, as well as operates as a coal mining contractor. The company was incorporated in 1958 and is headquartered in Bangkok, Thailand.'
    },
    'ITEL.BK': {
        'name': 'Interlink Telecom Public Company Limited',
        'address': '48/66 Soi Rung-reung Ratchadaphisek Road Samsennok,Huay Khwang Bangkok 10310 Thailand',
        'phone': '66 2 666 2222',
        'website': 'http://www.interlinktelecom.co.th',
        'sector': 'Communication Services',
        'industry': 'Telecom Services',
        'description': 'Interlink Telecom Public Company Limited provides telecommunication services through fiber optic network in Thailand. The company offers various services, such as interlink dark fiber, interlink wavelength, interlink international private leased circuits, and interlink multi-protocol label switching technology, as well as telecommunication network installation services. It also provides data center space services, including co-location, virtual server rentals and disaster recovery services. The company was founded in 2007 and is headquartered in Bangkok, Thailand.'
    },
    'IVL.BK': {
        'name': 'Indorama Ventures Public Company Limited',
        'address': '75/102, Ocean Tower 2 37th Floor Sukhumvit Soi 19 Bangkok 10110 Thailand',
        'phone': '66 2 661 6661',
        'website': 'http://www.indoramaventures.com',
        'sector': 'Basic Materials',
        'industry': 'Chemicals',
        'description': 'Indorama Ventures Public Company Limited, together with its subsidiaries, engages in the production and distribution of petrochemical products in Thailand and internationally. The company operates through three segments: Combined PET, Integrated Oxides & Derivatives, and Fibers. The Combined PET segment manufactures and distributes PET value chain comprising PX, PTA, PET, and recycled PET flakes; PET preforms and packaging products; and specialty PET-related chemicals, such as PIA and NDC, as well as PET resins. The Integrated Oxides & Derivatives segment offers monoethylene glycol, diethylene glycol, triethylene glycol, purified ethylene oxide, propylene oxide derivatives, polypropylene glycol, propylene glycol ethers, propylene carbonate, tertiary butyl alcohol, methyl tertiary-butyl ether, surfactants, LAB, and ethanolamines. The segment also provides oleochemical derivatives, including lauryl alcohol, caprylic / capric acid, cetostearyl alcohol, and glycerin, as well as solvents. The Fibers segment offers polyester, polyolefin, and bicomponent fibers; and worsted wool and nylon 6.6 tire cord yarn products. The company was formerly known as Beacon Global Limited and changed its name to Indorama Ventures Public Company Limited in March 2009. The company was founded in 2003 and is headquartered in Bangkok, Thailand. Indorama Ventures Public Company Limited operates as a subsidiary of Indorama Resources Limited.'
    },
    'J.BK': {
        'name': 'JAS Asset Public Company Limited',
        'address': '87, The Jas Ramintra Building 3rd Floor, Room A315 Lad pla khao Road Anusawari Sub-district,Bang Khen Distric Bangkok 10220 Thailand',
        'phone': '66 2 012 1277',
        'website': 'http://www.jasasset.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate Services',
        'description': 'JAS Asset Public Company Limited provides rental and related services in Thailand. It operates in four segments: Rental and Related Services Business, Food and Beverage Business, Real Estate Business, and Others. The company also manages rented space for mobile phones and IT products in shopping centers for retail sellers under the IT Junction name; food courts under the Urban Food Ville brand; and indoor amusement park under the Totem Kingdom brand name. In addition, it develops and manages community markets and malls under the J Market, The Jas, and The Jas Urban names; and develops condominium projects under the Newera brand name. The company was founded in 2012 and is headquartered in Bangkok, Thailand. JAS Asset Public Company Limited is a subsidiary of Jay Mart Public Company Limited.'
    },
    'JAS.BK': {
        'name': 'Jasmine International Public Company Limited',
        'address': '200, Chaengwattana Road 29th-30th Floor, Moo 4 Pakkred Sub-district Pakkred District Nonthaburi 11120 Thailand',
        'phone': '66 2 100 3000',
        'website': 'http://www.jasmine.com',
        'sector': 'Communication Services',
        'industry': 'Telecom Services',
        'description': 'Jasmine International Public Company Limited engages in the telecommunications business in Thailand. The company provides content for internet protocol television services; satellite telecommunications services; internet and international calling card services; online movie and internet protocol television services; computer system integration, software development, and cloud computing services; and high-speed data communication services. It also offers circuit leasing, local and international data communication, and Bitcoin mining services; fixed-line services and data communication network services; and cloud AI, internet of things, and fintech and engineer design and consultancy services in energy management and clean energy systems. In addition, it engages in the rental of office building; distribution of computer products; design, installation, and testing of telecommunications systems; survey, design, and construction for civil work of telecommunications projects; and development, distribution, and provision of various types of software. The company was founded in 1982 and is based in Nonthaburi, Thailand.'
    },
    'NAJASIF.BKME': {
        'name': 'Jasmine Broadband Internet Infrastructure Fund',
        'address': '175 Sathorn City Tower, 7,21,26 Floor, South Sathorn Road, Tungmahamek, Sathorn Bangkok 10120',
        'phone': '66 2 674 6488',
        'website': 'http://www.jas-if.com',
        'sector': 'Communication Services',
        'industry': 'Telecom Services',
        'description': 'JASIF has ownership of the Optical Fiber Cables of 1,680,500 core kilometers which the Fund purchased from TTTBB. The Fund entered into the Amended and Restated Main Lease Agreement and the Amended and Restated Rental Assurance Agreement with TTTBB for a lease of total assets. And the Fund entered into the Amended and Restated OFCs Maintenance Agreement with TTTBB by appointing TTTBB to carry out the services of repairing, replacing, maintaining and managing total OFCs on behalf of the Fund. In addition, TTTBB and the Fund entered into the Amended and Restated Marketing Services Agreement pursuant to which the Fund will appoint TTTBB to perform marketing services and to arrange for lease, either in whole or in part, of 20% of total OFCs received by the Fund pursuant to the Initial Asset Sale and Transfer Agreement and the Additional Asset Sale and Transfer Agreement by any lessee procured by TTTBB or the Fund.'
    },
    'JCK.BK': {
        'name': 'JCK International Public Company Limited',
        'address': 'TFD Building 18 Soi Sathorn 11 Yaek 9 Yannawa Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 676 4031',
        'website': 'http://www.jck.international',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'JCK International Public Company Limited, together with its subsidiaries, primarily engages in the property development classification activities in Thailand and the United Kingdom. It operates through five segments: Land and Factory Building for Sale; Land and Warehouse Building for Rent; Office Building for Rent; Residential Condominium Units for Sale; and REIT Manager. The company develops land for industrial estates; rents office and factory spaces; develops and sells residential condominium units; and provides construction and property management services. It also invests, leases, and sells land and warehouses; and manages a real estate investment trust. The company was formerly known as Thai Factory Development Public Company Limited and changed its name to JCK International Public Company Limited in April 2018. JCK International Public Company Limited was founded in 1977 and is headquartered in Bangkok, Thailand.'
    },
    'JCT.BK': {
        'name': 'Jack Chia Industries (Thailand) Public Company Limited',
        'address': '144/1-2 Sri Bamphen Road Chong Nonsi Subdistrict Yannawa District Bangkok Thailand',
        'phone': '66 2 012 0012',
        'website': 'http://www.Jackchia.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Household & Personal Products',
        'description': 'Jack Chia Industries (Thailand) Public Company Limited, together with its subsidiary, manufactures and distributes pharmaceuticals and cosmetics in Thailand. It also offers medical equipment and other consumer products. The company sells its products under the Tigerplast, Tensoplast, Kangaroo, Tabu, Thermaplast, Jason, Ronson, and Golden lion brands. It also exports its products. The company was founded in 1966 and is based in Bangkok, Thailand.'
    },
    'JDF.BK': {
        'name': 'JD Food Public Company Limited',
        'address': 'Office 116, 116/1, 116/2, Moo 3 Bang Torad Subdistrict Mueang Samut Sakhon District Samut Sakhon 74000 Thailand',
        'phone': '66 3 444 0681',
        'website': 'http://www.jdfthailand.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'JD Food Public Company Limited manufactures and distributes seasonings and dehydrated foods in Thailand, the United Kingdom, Canada, the United States, and internationally. The company offers seasonings for savory and sweet food products, instant soup powders, Thai style, western style, Asian style, and other products; sauces and fillings; and coconut chips, air dried meat products, and air-dried vegetables. It offers Thai food under the Kin dee brand; coconut chips, bites, and clusters under the Crispconu brand; and seasonings and fillings under the OK brand. The company serves entrepreneurs, SMEs, and large food industries. The company also exports its products. JD Food Public Company Limited was incorporated in 1999 and is headquartered in Samut Sakhon, Thailand.'
    },
    'JKN.BK': {
        'name': 'JKN Global Group Public Company Limited',
        'address': 'No. 818 JKN Empire Building Moo 2, Samrong Nuea Subdistrict Samut Prakan District Mueang Samut Prakan 10270 Thailand',
        'phone': '66 2 021 7777',
        'website': 'http://www.jknglobalgroup.com',
        'sector': 'Communication Services',
        'industry': 'Broadcasting',
        'description': 'JKN Global Group Public Company Limited, together with its subsidiaries, engages in content distribution business in Thailand. It operates through five segments: Sales of Program Rights, Advertising Services, Sale of Products, Miss Universe License Management Business, and Other Business. The company is involved in the distribution of contents of the movies, series, and documentaries; and production and distribution of non-alcoholic beverages. It also provides advertising services; offers television stations; engages in the manufacture and distribution of health, beauty, and consumer products; and produces and distributes television programs that granting the copyright to the Miss Universe pageant and relating to the Miss Universe pageants activities. In addition, the company offers studio leasing, costume rental, and artist management services, as well as organizes events; and retail sale through mail order, television, radio, and telephone. It also exports its products. The company was formerly known as JKN Global Media Public Company Limited and changed its name to JKN Global Group Public Company Limited in May 2022. JKN Global Group Public Company Limited was founded in 2013 and is headquartered in Mueang Samut Prakan, Thailand.'
    },
    'JMART.BK': {
        'name': 'Jay Mart Public Company Limited',
        'address': '187, 189 Jaymart Building Ramkhamhaeng Road Rat Phatthana Sub - District Saphan Sung District Bangkok 10240 Thailand',
        'phone': '66 2 483 7979',
        'website': 'http://www.jaymart.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Specialty Retail',
        'description': 'Jay Mart Public Company Limited, through its subsidiaries, engages in the wholesale and retail of mobile phones and related accessories in Thailand and Cambodia. It is also involved in the development, sale, and rental of properties; and operation of specialty coffee shop under the Casa Lapin and Rabb Coffee brand names. The company also engages in the debt collection and debt management; non-life insurance business; application development activities; and product distribution activities under the SINGER brand, as well as provision of hire-purchase services and car title loan services. In addition, it offers consulting services in E-commerce and information technology sectors; consumer loan services, such as revolving loan, term loan, mobile loan, and car for cash and other types of loans under the Kashjoy brand. The company was founded in 1988 and is based in Bangkok, Thailand.'
    },
    'JMT.BK': {
        'name': 'JMT Network Services Public Company Limited',
        'address': '187, Jaymart Building 4th - 6th Floor Ramkhamhaeng Road Rat Phatthana Sub-Dist.,Saphan Sung Dist Bangkok 10240 Thailand',
        'phone': '66 2 481 9889',
        'website': 'http://www.jmtnetwork.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'JMT Network Services Public Company Limited, together with its subsidiaries, provides debt tracking and collection services in Thailand. The company also engages in the purchase of non-performing accounts receivable for debts management and collection. In addition, it offers asset management, non-life insurance, and appraisal services, as well as operates as an insurance broker. The company was incorporated in 1994 and is based in Bangkok, Thailand. JMT Network Services Public Company Limited is a subsidiary of Jay Mart Public Company Limited.'
    },

    # 261-280
    'JR.BK': {
        'name': 'J.R.W. Utility Public Company Limited',
        'address': '32 / 288-290 Moo 8 Soi Ramindra 65 Ramindra Road Tharang Bangkok 10230Thailand',
        'phone': '66 2 509 7000',
        'website': 'http://www.jrw.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'J.R.W. Utility Public Company Limited engages in the design, procurement, construction, and installation of electrical power and telecommunication, and information technology systems. It is involved in high voltage transmission line system construction; high voltage substation construction and equipment installation; construction for changing the electrical cable to the underground systems; and infrastructure system planning, core network system, software and application system construction, and system implementation of other equipment activities. The company also maintains, repairs, and sells electrical system equipment, and telecommunication and information technology systems. The company was incorporated in 1993 and is headquartered in Bangkok, Thailand.'
    },
    'JTS.BK': {
        'name': 'Jasmine Technology Solution Public Company Limited',
        'address': '200, Moo 4, Jasmine International Tower 9th Floor Chaengwattana Road Tambon Pakkret, Amphoe Pakkret Nonthaburi 11120 Thailand',
        'phone': '66 2 100 8300',
        'website': 'http://www.jts.co.th',
        'sector': 'Communication Services',
        'industry': 'Telecom Services',
        'description': 'Jasmine Technology Solution Public Company Limited engages in the design and installation of telecommunication systems, and telecom service and other businesses in Thailand. The company also provides computer systems integration and cloud computing services; smart closed-circuit camera and hyper-converged infrastructure systems; and maintenance services for computer hardware and other peripheral equipment, as well as develops and distributes software. In addition, it offers server and client computer, firewall and data security, smart building management, cloud infrastructure-as-a-service, and cloud software-as-a-service systems; backup solutions for preventing ransomware; and data, fiber optic, and LAN networks. The company serves government agencies, state enterprises, private companies converted from state enterprises, private small and medium enterprises, and large private companies. The company was formerly known as Jasmine Telecom Systems Public Company Limited and changed its name to Jasmine Technology Solution Public Company Limited in October 2021. Jasmine Technology Solution Public Company Limited was founded in 1995 and is headquartered in Nonthaburi, Thailand.'
    },
    'KAMART.BK': {
        'name': 'Karmarts Public Company Limited',
        'address': '81-81/1, Soi Phetchakasem 54 Yak 3 Phetchakasem Road Bangduan Phasicharoen Bangkok 10160 Thailand',
        'phone': '66 2 805 2756',
        'website': 'http://www.karmarts.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Household & Personal Products',
        'description': 'Karmarts Public Company Limited, together with its subsidiary, engages in the manufacturing, packaging, import, and distribution of cosmetics and consumer products in Thailand. The company operates in three segments, Manufacture and Distribution of Consumer Products; Warehouse for Rental; and Investment properties and distribution of by-products and agriculture segment. It offers facial care and cleanser, body care and cleanser, makeup, eye and brow makeup, beauty accessories, body fragrance, hair care, dietary supplement, scented, acne and sensitive skin care, oral care, hand sanitizer, face mask, and dishwashing products under the Cathy Doll, Baby Bright, Boya, Jejuvita, Reunrom, SKYNLAB, 7 Clean, Browit, and Tha brands. It distributes products through convenience stores; supermarkets/hypermarkets, and discount stores; and specialty stores, as well as through catalogs and online. The company operates 19 shops under the KARMART brand. It also exports its products to Vietnam, Japan, Myanmar, China, Laos, the Philippines, the United Arab Emirates, Malaysia, Taiwan, Iraq, the United States, Hong Kong, Russia, and Kuwait. The company was formerly known as Distar Electric Corporation Public Company Limited and changed its name to Karmarts Public Company Limited in April 2011. Karmarts Public Company Limited was incorporated in 1982 and is headquartered in Bangkok, Thailand.'
    },
    'KBANK.BK': {
        'name': 'Kasikornbank Public Company Limited',
        'address': '400/22 Phahon Yothin Road Sam Sen Nai Sub-District Phaya Thai District Bangkok 10400 Thailand',
        'phone': '66 2 222 0000',
        'website': 'http://www.kasikornbank.com',
        'sector': 'Financial Services',
        'industry': 'Banks—Regional',
        'description': 'Kasikornbank Public Company Limited, together with its subsidiaries, provides commercial banking products and services in Thailand and internationally. The companys personal banking products and services include savings, current, fixed deposit, and foreign currency accounts; personal, home, and auto loans; debit and credit cards; life and non-life insurance products; investment products, such as mutual funds, stocks, and derivatives/futures exchange; money transfer and bill payment, cheque and draft, and foreign exchange services; and digital banking services. It also offers various products and services for small and medium enterprises, including savings, current, and fixed deposits; working capital, commercial, and special loans, as well as letters of guarantee; collection and payment services; life, non-life, and group insurance products; and import, export, and money transfer services. In addition, the company provides various products and services for corporate customers, such as cash management solutions comprising current, savings, special savings deposit, and fixed deposit accounts, as well as collection, payment, liquidity management, and electronic service solutions; international trade solutions comprising import and export, global money transfer, guarantee, and trade finance solutions; working capital loans, term loans, special loans, and letters of guarantee; supply chain financing; life, non-life, and group insurance products; and foreign exchange and derivatives, corporate finance, securities, investment, and business card services. Further, it offers auto and equipment leasing, and venture capital management services. Kasikornbank Public Company Limited was founded in 1945 and is headquartered in Bangkok, Thailand.'
    },
    'KBS.BK': {
        'name': 'Khonburi Sugar Public Company Limited',
        'address': '5 Soi Sukhumvit 57 Khlongton-Nue Wattana Bangkok 10110 Thailand',
        'phone': '66 2 725 4888',
        'website': 'http://www.kbs.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Confectioners',
        'description': 'Khonburi Sugar Public Company Limited engages in the manufacture and distribution of sugar in Thailand, Asia, Europe, and internationally. It operates through three segments: Sugar Cane, Sugar and Molasses Trading, and Utilities. The Sugar Cane segment produces and distributes sugar cane, as well as provides agricultural machines and vehicles to planters. The Sugar and Molasses Trading segment purchases and sells sugar, molasses, and by products. The Utilities segment is involved in the generation of electricity and steam using bagasse as fuel. Its products include refined, white, brown, and raw sugar. The company also manufactures and distributes ethanol; and provides knowledge seminars to planters. Khonburi Sugar Public Company Limited was founded in 1965 and is headquartered in Bangkok, Thailand.'
    },
    'KBSPIF.BK': {
        'name': 'Khonburi Sugar Power Plant Infrastructure Fund',
        'address': 'No. 1 Empire Tower, 32nd Floor, South Sathorn Road, Yannawa, Sathorn Bangkok 10120',
        'phone': '66 2 686 6100',
        'website': 'http://www.kbspif.com',
        'sector': 'Utilities',
        'industry': 'Utilities-Diversified',
        'description': 'To invest 62 percent of the right to Revenue from the Electricity Business Operations under the power purchase agreements from small power plant (SPP) in the cogeneration system using bagasse as primary of Khonburi Power Plant Co., Ltd (KPP), (subsidiary of Khonburi Sugar Public Company Limited (KBS)) by expiry date of the right in the Revenue is on December 31 ,2039'
    },
    'KC.BK': {
        'name': 'K.C. Property Public Company Limited',
        'address': 'Le Concorde Building 19th Floor, Room 1903 No. 202, Ratchadapisek Road Huaykwang Subdistrict, Huai Khwang Dist. Bangkok 10310 Thailand',
        'phone': '66 2 276 5924',
        'website': 'http://www.kcproperty.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'K.C. Property Public Company Limited engages in the development and sale of properties in Thailand. It develops detached houses, townhomes, condominiums, and commercial buildings, as well as vacant lands. The company was incorporated in 1993 and is based in Bangkok, Thailand.'
    },
    'KCAR.BK': {
        'name': 'Krungthai Car Rent and Lease Public Company Limited',
        'address': 'No. 455/1, Rama 3 Road Kwang Bangklo Khet Bangkorlaem Bangkok 10120 Thailand',
        'phone': '66 2 291 8888',
        'website': 'http://www.krungthai.co.th',
        'sector': 'Industrials',
        'industry': 'Rental & Leasing Services',
        'description': 'Krungthai Car Rent and Lease Public Company Limited, operates as a car leasing and rental company in Thailand. It is also involved in the buying, selling, and exchanging of used and unused cars and spare parts. In addition, the company offers car maintenance services, such as fitting and repairing services; and car insurance and replacement services, as well as third-party insurance. It serves individuals; and medium and large, multinational corporation, government, and state enterprises. The company was incorporated in 1992 and is headquartered in Bangkok, Thailand.'
    },
    'KCE.BK': {
        'name': 'KCE Electronics Public Company Limited',
        'address': '72-72/1-3 Lat Krabang Industrial Estate Soi Chalongkrung 31 Kwang Lumplatew Khet Lat Krabang Bangkok 10520 Thailand',
        'phone': '66 2 326 0196',
        'website': 'http://www.kcethai.in.th',
        'sector': 'Technology',
        'industry': 'Electronic Components',
        'description': 'KCE Electronics Public Company Limited, together with its subsidiaries, manufactures and distributes electric printed circuit boards (PCBs) under the KCE trademark worldwide. The company operates through three segments: Manufacturing and Distributing of Prepreg and Laminate, Manufacturing and Distributing of Printed Circuit Board, and Manufacturing and Distributing of Chemical. The companys PCBs are manufactured from copper clad laminate that are used in various applications, including automotive, industrial, computer, and telecom systems. It also manufactures and distributes chemicals products, and prepreg and laminate products, as well as engages in the rental of buildings. The company was formerly known as Kuang Charoen Electronics Company Limited. KCE Electronics Public Company Limited was founded in 1982 and is based in Bangkok, Thailand.'
    },
    'KDH.BK': {
        'name': 'Thonburi Medical Centre Public Company Limited',
        'address': '337, Somdet Prachao Taksin Road Samrae Thonburi Bangkok 10600 Thailand',
        'phone': '66 2 438 0040',
        'website': 'http://www.samitivejthonburi.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Thonburi Medical Centre Public Company Limited engages in operation of hospital business in Thailand. It offers services comprising hair treatment, weight control, facial treatment, non-surgical facelift, anti-aging, sexual health, cosmetic surgery, and laser hair removal. The company was formerly known as Krungdhon Hospital Public Company Limited and changed its name to Thonburi Medical Centre Public Company Limited in April 2013. Thonburi Medical Centre Public Company Limited was founded in 1977 and is based in Bangkok, Thailand.'
    },
    'KEX.BK': {
        'name': 'Kerry Express (Thailand) Public Company Limited',
        'address': 'No. 89, Chao Phaya Tower 9th Floor, Room 906 Soi Wat Suan Phlu, Charoen Krung Road Bang Rak Sub-District, Bang Rak District Bangkok 10500 Thailand',
        'phone': '66 2 238 5558',
        'website': 'https://th.kerryexpress.com/th/home',
        'sector': 'Industrials',
        'industry': 'Integrated Freight & Logistics',
        'description': 'Kerry Express (Thailand) Public Company Limited provides parcel delivery services in Thailand. The company was founded in 2006 and is headquartered in Bangkok, Thailand. Kerry Express (Thailand) Public Company Limited is a subsidiary of KLN Logistics (Thailand) Limited.'
    },
    'KGI.BK': {
        'name': 'KGI Securities (Thailand) Public Company Limited',
        'address': 'No. 173 Asia Centre Building 8th-11th Floor South Sathorn Road Thungmahamek Sub-Dist., Sathorn Dist. Bangkok 10120 Thailand',
        'phone': '66 2 658 8888',
        'website': 'http://www.kgieworld.co.th',
        'sector': 'Financial Services',
        'industry': 'Capital Markets',
        'description': 'KGI Securities (Thailand) Public Company Limited, together with its subsidiaries, engages in the securities and derivatives business in Thailand. The company provides securities brokerage, securities dealing, investment advisory, securities borrowing and lending, securities registrar, derivatives brokerage, financial instruments, and financial advisory services, as well as over-the-counter derivatives and sells mutual fund units. It also offers securities trading, derivative warrants, futures, fixed income, private repo, and securities underwriting services. In addition, the company provides OTC equity derivatives, structured products, and exchange-traded funds; and investment banking services, including fund raising, IPOs, secondary market placements, mergers and acquisitions, firm valuations, loan arrangements, debt restructuring, and other advisory services, as well as proprietary trading and wealth management services. As of December 31, 2021, it operated 14 branches in Bangkok and other provinces. The company was formerly known as KGI Securities One Public Company Limited and changed its name to KGI Securities (Thailand) Public Company Limited in May 2001.KGI Securities (Thailand) Public Company Limited was founded in 1975 and is headquartered in Bangkok, Thailand.'
    },
    'KIAT.BK': {
        'name': 'Kiattana Transport Public Company Limited',
        'address': '100 Moo 3 Bangtanai Sub-district Pakkret District Nonthaburi 11120 Thailand',
        'phone': '66 2 501 73308',
        'website': 'http://www.kiattana.co.th',
        'sector': 'Industrials',
        'industry': 'Trucking',
        'description': 'Kiattana Transport Public Company Limited provides transportation services in Thailand and internationally. The company offers integrated logistics services to the energy, chemical, and related industries through a fleet of approximately 700 trucks. It also provides warehousing, product sourcing, customs clearance and documentation, transportation management, and goods custodial services, as well as trades in chemicals used in industry. In addition, the company distributes and rents hardware and software accessories relating to IT systems and various types of global positioning systems; and offers rail freight services. Further, it also provides rental of cars and tanks, and accessories installation services. Kiattana Transport Public Company Limited was incorporated in 1994 and is headquartered in Nonthaburi, Thailand.'
    },
    'KISS.BK': {
        'name': 'Rojukiss International Public Company Limited',
        'address': 'Vongvanich Complex B Building 100/8,100/51-54, 12th & 19th Floor Rama 9 Road Huai Khwang 10310 Thailand',
        'phone': '66 2 645 1313',
        'website': 'http://www.rojukissinternational.com',
        'sector': 'Consumer Defensive',
        'industry': 'Household & Personal Products',
        'description': 'Rojukiss International Public Company Limited engages in the distribution of skincare products, cosmetics, and food supplements in Thailand, Hong Kong, Indonesia, Cambodia, Laos, and internationally. The company also engages in the wholesale of pharmaceutical and medical products. It markets products under the Rojukiss, PHDerma, Best Korea, Wonder Herb, and Sis2Sis brands. The company was formerly known as Agenz Company Limited. Rojukiss International Public Company Limited was incorporated in 2007 and is headquartered in Huai Khwang, Thailand.'
    },
    'KKC.BK': {
        'name': 'Kulthorn Kirby Public Company Limited',
        'address': '126 Soi Chalong Krung 31 Chalong Krung Road Khwaeng Lam Pla Thio Khet Lat Krabang Bangkok 10520 Thailand',
        'phone': '66 2 326 0831',
        'website': 'http://www.kulthorn.com',
        'sector': 'Industrials',
        'industry': 'Specialty Industrial Machinery',
        'description': 'Kulthorn Kirby Public Company Limited, together with its subsidiary, manufactures and distributes hermetic compressors for refrigerators, freezers, water coolers, commercial refrigerators, and air conditioners. The company operates through four segments: Compressors and Parts, Enameled Wire, Steel Sheet, and Steel Coil Center. It also produces iron castings for compressor parts and automotive parts; enameled copper wires and thermostats for use in air conditioners and refrigerators; forging, machining, and heat treatment metal parts; and steel coil center for the manufacturer of motor compressors, electrical motors, and other parts. In addition, the company is involved in the slitting of electrical steel for compressors; and the provision of services related to technology research and development for products and manufacturing. Further, it offers condensing units for refrigeration products, electrical motor parts, and other motor compressor parts. The company serves in Thailand, Hong Kong, China, Indonesia, Australia, Saudi Arabia, and internationally. Kulthorn Kirby Public Company Limited was founded in 1980 and is headquartered in Bangkok, Thailand.'
    },
    'KKP.BK': {
        'name': 'Kiatnakin Phatra Bank Public Company Limited',
        'address': '209 KKP Tower Sukhumvit 21 (Asoke) Road Khlong Toey Nua Wattana Bangkok 10110 Thailand',
        'phone': '66 2 165 5555',
        'website': 'https://bank.kkpfg.com/',
        'sector': 'Financial Services',
        'industry': 'Banks—Regional',
        'description': 'Kiatnakin Phatra Bank Public Company Limited, together with its subsidiaries, provides various banking products and services in Thailand. The company operates through Commercial Banking Business, Capital Market Business, and Debt Restructuring segments. Its deposit products include current, savings, and fixed deposit accounts, as well as certificates of deposit. The company also provides auto, home, and personal loans; and business loans, including construction machinery and materials, real estate, apartment and hotel, specialized industrial, and logistics loans. In addition, it is involved in the car auction, securities, financial service and digital asset, real estate, investments, and fund management businesses. Further, the company offers debit cards, digital and e-banking services, bancassurance, and SME banking products, as well as foreign exchange, letter of guarantee, and other services. The company was formerly known as Kiatnakin Bank Public Company Limited and changed its name to Kiatnakin Phatra Bank Public Company Limited in August 2020. Kiatnakin Phatra Bank Public Company Limited was founded in 1971 and is headquartered in Bangkok, Thailand.'
    },
    'KPNPF.BK': {
        'name': 'KPN Property Fund',
        'address': '400/22, KASIKORNBANK Building 6th and 12th Floor, Phahon Yothin Road Samsen Nai Sub-District Phaya Thai District Bangkok Thailand',
        'phone': '66 2 673 3999',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Office',
        'description': 'KPN Property Fund is a real estate investment fund launched and managed by Kasikorn Asset Management Co.,Ltd. The fund invests in real estate markets of Thailand. It invest in the freehold right of land and the building of KPN Tower located on the prime location of Rama IX Road. KPN Property Fund is domiciled in Thailand.'
    },
    'KSL.BK': {
        'name': 'Khon Kaen Sugar Industry Public Company Limited',
        'address': '503 KSL Tower 9th Floor, Sriayudhya Road Thanon Phaya Thai Sub-District Rajathevi District Bangkok 10400 Thailand',
        'phone': '66 2 642 6191',
        'website': 'http://www.kslgroup.com',
        'sector': 'Consumer Defensive',
        'industry': 'Confectioners',
        'description': 'Khon Kaen Sugar Industry Public Company Limited, together with its subsidiaries, engages in the production and sale of sugar and related products in Thailand. It offers raw, very high polarization, white, liquid, and refined sugar, as well as molasses, bagasse, and filter cakes. The company also manufactures bio-fertilizers; produces and distributes electricity and ethanol; and provides terminal and warehousing facilities. In addition, it engages in the agricultural business; and provision of transport, trading, and consulting services, as well as exports sugar. The company was founded in 1945 and is headquartered in Bangkok, Thailand.'
    },
    'KTB.BK': {
        'name': 'Krung Thai Bank Public Company Limited',
        'address': 'Building 1 35 Sukhumvit Road Klong Toey Nua Subdistrict Wattana District Bangkok 10110 Thailand',
        'phone': '66 2 111 1111',
        'website': 'https://krungthai.com',
        'sector': 'Financial Services',
        'industry': 'Banks—Regional',
        'description': 'Krung Thai Bank Public Company Limited provides various commercial banking products and services. The company operates through three segments: Retail Banking, Corporate Banking, and Treasury and Investment. It offers various personal banking products and services, including current, savings, and fixed deposit accounts; time and foreign currency deposits; personal and housing loans; debit, travel, cash and top up, and credit cards; investment services; life, health, motor, accident, and non-life insurance products; money transfer, payment and top up, foreign exchange, and overseas education services; and e-banking services. The company also provides SME loans for small and medium businesses; and international business loans. In addition, it offers corporate banking products and services comprising cash management services, such as collection, liquidity management, and transfer and payment services; fixed deposit and current accounts; foreign currency and term deposits; cards; Fx, interest rate, commodity, equity, and credit derivatives; financial advisory, underwriting, and selling agent services for products offered through the equity capital markets; financial advisory services related to merger and acquisition transactions; project finance advisory and feasibility study services, as well as e-banking services; and investment solutions, such as government and corporate bonds, structured notes, and investment units. The company provides its products and services through a network of branches in Thailand and various centers internationally. Krung Thai Bank Public Company Limited was founded in 1966 and is headquartered in Bangkok, Thailand.'
    },
    'KTBSTMR.BK': {
        'name': 'KTBST Mixed Freehold and Leasehold Real Estate Investment Trust',
        'address': '87/2 CRC Tower 18th Floor All Seasons Place, Wireless Road Lumpini, Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 351 1800',
        'website': 'http://www.daol.co.th',
        'sector': 'Real Estate',
        'industry': 'REIT—Diversified',
        'description': 'KTBST Mixed Freehold and Leasehold Real Estate Investment Trust, a real estate investment trust, invests in various property development projects in Thailand. It has rights to lease and sub-lease land, warehouse and factory buildings, office buildings, and community malls. The company was founded in 2021 and is based in Bangkok, Thailand.'
    }
    ,

    # 281-300
    'KTC.BK': {
        'name': 'Krungthai Card Public Company Limited',
        'address': 'UBC II Building 14th Floor 591 Sukhumvit Road Klongton Nua, Wattana Bangkok 10110 Thailand',
        'phone': '66 2 123 5000',
        'website': 'http://www.ktc.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Krungthai Card Public Company Limited engages in the credit card, personal loan, and other related businesses in Thailand. It also engages in the merchant acquiring, payment services, retail lending business, occupational retail lending business, e-money business, and hire purchase and leasing business. Krungthai Card Public Company Limited was incorporated in 1996 and is based in Bangkok, Thailand.'
    },
    'KTIS.BK': {
        'name': 'Kaset Thai International Sugar Corporation Public Company Limited',
        'address': '1/1 Moo 14 Tambon Nongpo Amphur Taklee Nakhon Sawan 60140 Thailand',
        'phone': '66 6 2310 0311',
        'website': 'https://www.ktisgroup.com',
        'sector': 'Consumer Defensive',
        'industry': 'Confectioners',
        'description': 'Kaset Thai International Sugar Corporation Public Company Limited produces and distributes sugar in Thailand and internationally. It offers raw, white, and refined sugar; molasses products or sugar residues that are used as raw material in various products, such as food and ethanol; dry and wet pulp; bio-fertilizers; and ethanol products, including industrial and fuel alcohol. The company is also involved in the generation and sale of electricity through a biomass power plant; trade and rental of properties; and rental of agricultural machinery for farmers. In addition, it engages in the manufacture and distribution of containers and organic fertilizers; and provision of research and development, and asset management services. The company was formerly known as Kaset Thai Industry Sugar Company Limited. The company was founded in 1957 and is headquartered in Nakhon Sawan, Thailand.'
    },
    'KWC.BK': {
        'name': 'Krungdhep Sophon Public Company Limited',
        'address': '185 Ratburana Road Kwaeng Bangpakok Khet Rajburana Bangkok 10140 Thailand',
        'phone': '66 2 427 3374',
        'website': 'https://www.kwc.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate Services',
        'description': 'Krungdhep Sophon Public Company Limited engages in the development and leasing of real estate properties in Thailand. The company also operates warehouse, wharf, and stevedoring business that offers space renting and port of loading/unloading goods to retail customers. In addition, it provides storage and management services for document and computer backup media. The company was formerly known as Krungdhep Warehouse Company Limited and changed its name to Krungdhep Sophon Public Company Limited in December 1995. Krungdhep Sophon Public Company Limited was founded in 1961 and is headquartered in Bangkok, Thailand.'
    },
    'KWI.BK': {
        'name': 'KWI Public Company Limited',
        'address': '43 Thai CC Tower, 26th Floor, South Sathorn Road, Yannawa, Sathorn, Bangkok 10120',
        'phone': '66 2 129 5999',
        'website': 'https://www.kwiasia.com',
        'sector': 'Financial Services',
        'industry': 'Insurance—Diversified',
        'description': 'KWI Public Company Limited operates in the life and non-life insurance, and real estate development businesses in Thailand. It engages in the development of residential housing and condominium projects. The company also provides rental and other services for office spaces. In addition, it offers general insurance products comprising commercial motor, business secure, commercial property, construction and engineering, general liability, group personal accident, marine, miscellaneous, and professional liability insurance products. Further, the company provides health, life and critical illness, and endowment insurance products, as well as investment-linked plans. Additionally, it offers mutual fund management, private and provident fund management, and investment advisory services. The company was formerly known as King Wai Group (Thailand) Public Company Limited and changed its name to KWI Public Company Limited in December 2021. The company was founded in 1983 and is headquartered in Bangkok, Thailand. KWI Public Company Limited is a subsidiary of Tommo (Thailand) Company Limited.'
    },
    'KYE.BK': {
        'name': 'Kang Yong Electric Public Company Limited',
        'address': '67 Moo 11, Debaratna Road Km. 20, Bangchalong Bang Phli 10540 Thailand',
        'phone': '66 2 337 2900',
        'website': 'http://www.mitsubishi-kye.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Furnishings, Fixtures & Appliances',
        'description': 'Kang Yong Electric Public Company Limited manufactures and distributes household electrical appliances in Thailand, Japan, and internationally. The company provides home electrical appliances, such as refrigerators, electric fans, ventilating fans, water pumps, and jet towels under the Mitsubishi Electric trade name. It also exports its products to approximately 20 countries. The company was formerly known as Kang Yong Electric Manufacturing Co., Ltd. Kang Yong Electric Public Company Limited was founded in 1964 and is based in Bang Phli, Thailand.'
    },
    'L&E.BK': {
        'name': 'Lighting and Equipment Public Company Limited',
        'address': 'Gypsum Metropolitan Tower 16-17 Floor 539/2 Sri-Ayudhya Road Rajthevee Bangkok 10400 Thailand',
        'phone': '66 2 248 8133',
        'website': 'http://www.lighting.co.th',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'Lighting and Equipment Public Company Limited designs, manufactures, and trades in electric and lighting systems in Thailand and internationally. Its indoor lighting products include linear fixtures, recessed and surface fluorescent, suspension, recessed and surface downlight, ceiling-mounted, spotlight and track light, and low bay and high bay lighting products; and outdoor lighting products comprise linear fixture, inground, flood light, area light, streetlight, canopy, wall mount, border and bollard, ground spike, underwater, and post-top lighting products. The company also provides decorative lighting products, including chandeliers and pendants, table and floor lamps, wall lamps, and ceiling-mounted lamps. In addition, it offers special and stage light products, including stage and event, clean room and weatherproof, explosion proof, exit sign and emergency, and obstruction light and airfield lightings; switch/receptacle/signage; LED, retrofit, and smart lamps; LED modules; poles; components and control equipment; UVC disinfection; and horticulture and biological lighting products. Further, the company provides IOT products, such as Wi-Fi smart home ecosystem, Bluetooth smart bulb/tunable white lighting products and controls, zigbee and NB-IOT smart lighting, lighting management system, and smart lighting with smart city solutions. Lighting and Equipment Public Company Limited was founded in 1993 and is headquartered in Bangkok, Thailand.'
    },
    'LALIN.BK': {
        'name': 'Lalin Property Public Company Limited',
        'address': 'Lalin Building 222/2 Srinakharin Road Huamark Subdistrict Bangkapi District Bangkok 10240 Thailand',
        'phone': '66 2 732 1041',
        'website': 'https://www.lalinproperty.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Lalin Property Public Company Limited, through its subsidiaries, engages in the property development activities in Thailand. The company was incorporated in 1988 and is based in Bangkok, Thailand.'
    },
    'LANNA.BK': {
        'name': 'Lanna Resources Public Company Limited',
        'address': '888/99, Mahathun Plaza Building 9th Floor, Ploenchit Road Lumpini, Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 253 8080',
        'website': 'https://www.lannar.com',
        'sector': 'Energy',
        'industry': 'Thermal Coal',
        'description': 'Lanna Resources Public Company Limited, together with its subsidiaries, manufactures and distributes lignite in Thailand and internationally. It operates through five segments: Domestic Coal, Overseas Coal, Ethanol, Wood Pellet, and Soil Conditioner. The company also purchases and sells coal; produces and sells coal, ethanol, and wood pellets; and generates and distributes power. In addition, it is involved in renewable energy, coal trading, and ocean freight shipping businesses. The company was founded in 1985 and is headquartered in Bangkok, Thailand.'
    },
    'LEE.BK': {
        'name': 'Lee Feed Mill Public Company Limited',
        'address': 'Wall Street Tower 28th Floor 33/137 Surawong Road Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 632 7300',
        'website': 'http://www.leepattana.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Lee Feed Mill Public Company Limited, together with its subsidiaries, manufactures and distributes animal feed primarily in Thailand. The company provides pet food, livestock feed, and aquatic feed products. It offers products in concentrated pellet and powder forms to livestock and aquaculture industries, as well as concentrated feed for swine, chickens, ducks, cattle, fish, frogs, and shrimps under the Lee, Win, Max, and Pro-grade brand names. The company is also involved in breeding broiler chicks; crop drying, silo grain storage, experimental farming, and crop farming, as well as rental farming businesses; and the distribution of raw materials for the animal feed manufacturers. It also sells its products in the Lao Peoples Democratic Republic, Thailand, and internationally. Lee Feed Mill Public Company Limited was founded in 1983 and is headquartered in Bangkok, Thailand.'
    },
    'LH.BK': {
        'name': 'Land and Houses Public Company Limited',
        'address': 'Q House Lumpini Building 36-38th Floors No. 1, South Satorn Road Kwaeng Tungmahamek, Khet Satorn Bangkok 10120 Thailand',
        'phone': '66 2 343 8900',
        'website': 'http://www.lh.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Land and Houses Public Company Limited engages in the property development activities in Thailand and the United States. It operates in two segments, Real Estate Business, and Rental and Service Business. The companys Real Estate Business segment develops and sells single detached houses, townhouses, and residence condominium projects. Its Rental and Service Business segment is involved in the rental of shopping malls, hotels, and apartments. The company also offers project administration and management, and investment advisory services. Land and Houses Public Company Limited was founded in 1973 and is headquartered in Bangkok, Thailand.'
    },
    'LHFG.BK': {
        'name': 'LH Financial Group Public Company Limited',
        'address': 'No. 1, Q-House Lumpini Building 5th Floor South Sathorn Road Thungmahamek Sub-Dist., Sathorn Dist. Bangkok 10120 Thailand',
        'phone': '66 2 359 0000',
        'website': 'https://www.lhfg.co.th',
        'sector': 'Financial Services',
        'industry': 'Banks—Regional',
        'description': 'LH Financial Group Public Company Limited, an investment holding company, engages in banking business in Thailand. It operates in four segments: Investment Holding Business, Banking Business, Fund Management Business, and Securities Businesses. The company accepts deposit products, such as demand deposits, savings deposits, time deposits, and fixed deposit receipts; and offers loans, including housing, retail, and commercial loans. It also provides securities brokerage, trading, and underwriting services; and investment advisory services. The company was founded in 2009 and is based in Bangkok, Thailand.'
    },
    'LHHOTEL.BK': {
        'name': 'LH Hotel Leasehold Real Estate Investment Trust',
        'address': '11 Q.House Sathorn Building 14th Floor South Sathorn Road Tungmahamek, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 286 3484',
        'website': 'http://www.lhfund.co.th',
        'sector': 'Real Estate',
        'industry': 'REIT—Hotel & Motel',
        'description': 'LH Hotel Leasehold Real Estate Investment Trust operates as a real estate investment trust in Thailand. It is involved in the rental of immovable properties. The company was founded in 2015 and is based in Bangkok, Thailand.'
    },
    'LHK.BK': {
        'name': 'Lohakit Metal Public Company Limited',
        'address': '66/1 Moo 6, Soi Suksawad 76 Suksawad Road Bangjak Phra Pradaeng 10130 Thailand',
        'phone': '66 2 463 0158',
        'website': 'http://www.lohakit.co.th',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'Lohakit Metal Public Company Limited, together with its subsidiaries, engages in processing, distribution, and shearing of stainless steel, steel, and metal products in Thailand. The company offers cold and hot rolled, austenitic, ferritic, and special stainless steel products; and ornamental tube, square and rectangular tube, automotive pipe, electro-galvanized steel, and galvanized steel products. It also distributes metal and non-ferrous metal products, as well as aluminum coil and sheet, copper coil, sheet, angle bar, rod bar, pipe, and zinc products; and provides cutting, drilling, and polishing services. It serves construction, automotive, food, petrochemical, electrical and electronic, and household appliances industries. The company also exports its products. The company was formerly known as Lohakit Metal Service Center Company Limited and changed its name to Lohakit Metal Public Company Limited on January 2, 2003. Lohakit Metal Public Company Limited was founded in 1989 and is headquartered in Phra Pradaeng, Thailand.'
    },
    'LHPF.BK': {
        'name': 'Land and Houses Freehold and Leasehold Property Fund',
        'address': '11 Q.House Sathon Building 14th floor South Sathon Road Tungmahamek Sathon Bangkok 10120 Thailand',
        'phone': '66 2 286 3484',
        'website': 'https://www.lhpf-pf.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Residential',
        'description': 'Land and Houses Freehold and Leasehold Property Fund is a real estate investment trust launched and managed by Land and Houses Fund Management Co., Ltd. The fund invests on real estate markets of Thailand. Land and Houses Freehold and Leasehold Property Fund was formed on March 22, 2012 and is domiciled in Thailand.'
    },
    'LHSC.BK': {
        'name': 'LH Shopping Centers Leasehold Real Estate Investment Trust',
        'address': '11 Q. House Sathon Building 14th Floor South Sathorn Road Tungmahamek, Sathon Bangkok 10120 Thailand',
        'phone': '66 2 286 3484',
        'website': 'http://www.lhfund.co.th',
        'sector': 'Real Estate',
        'industry': 'REIT—Diversified',
        'description': 'LH Shopping Centers Leasehold Real Estate Investment Trust is a real estate investment trust externally managed by Land and Houses Fund Management Company Limited. The firm invest in the leasehold right in the immovable properties and the ownership in the movable properties in Terminal 21 Shopping Center from L&H Property Company Limited in an approximate total area of 97,905 square meters, for an approximate term of 26 years ending on 31 August 2040. LH Shopping Centers Leasehold Real Estate Investment Trust is based in Bangkok, Thailand.'
    },
    'LOXLEY.BK': {
        'name': 'Loxley Public Company Limited',
        'address': '102 Na Ranong Road Khwang Khlong Toei Khet Khlong Toei Bangkok 10110 Thailand',
        'phone': '66 2 348 8000',
        'website': 'http://www.loxley.co.th',
        'sector': 'Industrials',
        'industry': 'Conglomerates',
        'description': 'Loxley Public Company Limited engages in the trading and turnkey contract sale of telecommunication equipment, rail transport engineering and other systems in Thailand. It operates through six segments: Information Technology Business Group, Services Business Group, Energy Business Group, Network Solutions Business Group, Trading Business Group, and Special and Other Businesses. The company offers designing, procurement, installation, and management of information systems; financial transaction application platform; and blockchain technology and cybersecurity to manage data. It is also involved in the trading of computers, computer spare parts, and equipment; telecommunication equipment; supply, maintenance, and set up of work systems; installation of computers; management of computerized center; installation and repair of IT equipment; sale of computers and peripherals; import, export, and distribution of virtual learning services; systems development activities; and import, wholesale, and distribution of food ingredients and food products. In addition, the company provides recruitment, personnel development, training, and other related services; telecommunication, information technology systems, and submarine cable network services; and distributes food ingredients and products; manufactures, assembles, and distributes steam generators; and airport security and project management services. Further, it engages in Installing and testing the power system; and design and install solar power plant, as well as manufactures and distributes water and wastewater management system and equipment. The company was formerly known as Loxley (Bangkok) Company Limited and changed its name to Loxley Public Company Limited in April 1993. Loxley Public Company Limited was incorporated in 1939 and is headquartered in Bangkok, Thailand.'
    },
    'LPF.BK': {
        'name': 'Lotus Retail Growth Freehold and Leasehold Property Fund',
        'address': '1 Empire Tower 32nd Floor South Sathorn Road Yannawa, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 686 6100',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Retail',
        'description': 'Tesco Lotus Retail Growth Freehold and Leasehold Property Fund specializes in investments in freehold and leasehold of 17 shopping malls anchored by a Tesco Lotus hypermarket.'
    },
    'LPH.BK': {
        'name': 'Ladprao General Hospital Public Company Limited',
        'address': '2699 Ladprao Road Khlong Chaokhun Sing Wangthonglang Bangkok 10310 Thailand',
        'phone': '66 2 530 2556',
        'website': 'http://www.ladpraohospital.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Ladprao General Hospital Public Company Limited, together with its subsidiaries, engages in the hospital business in Thailand. The company operates Ladprao General Hospital, a private hospital. It provides services in the field of neurology, cardiology, hypertension, dental, hemodialysis, pediatric, refractive surgery, womens health, aesthetics, laser, and dermatology, as well as eye, ear, nose, and throat; and operates health screening, gastrointestinal, liver, bones and joints, physical therapy, and rehabilitation centers. It also offers scientific analytical and diagnostic services for food and agricultural, pharmaceutical, environmental, calibration of instruments, and inspections, as well as certifications in accordance with quality systems and international standards; and hospital management and consulting, health mobile checkups, and nurse services in factories and agencies. In addition, the company researches, develops, cultivates, and distributes herbal products for medical benefits. Ladprao General Hospital Public Company Limited was founded in 1990 and is based in Bangkok, Thailand.'
    },
    'LPN.BK': {
        'name': 'L.P.N. Development Public Company Limited',
        'address': '1168/109, Lumpini Tower 36th Floor, Rama IV Road Tungmahamek subdistrict Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 285 5011',
        'website': 'http://www.lpn.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'L.P.N. Development Public Company Limited, together with its subsidiaries, develops real estate properties in Thailand. The company develops residential condominiums, houses, and townhomes. It also provides community management services; residential, office, and commercial building management services; services for tenants and buyers; and engineering services for condominiums. In addition, the company offers project management services; construction management services; cleaning and receptionist, and community services; and consulting and research services. Further, it leases office buildings; and provides security services, as well as advisory and management services for project development. L.P.N. Development Public Company Limited was founded in 1989 and is based in Bangkok, Thailand.'
    },
    'LRH.BK': {
        'name': 'Laguna Resorts & Hotels Public Company Limited',
        'address': '21/17B, 21/17C, 21/65, Thai Wah Tower I 7th, 22nd and 24th floor South Sathorn Road Tungmahamek, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 677 4455',
        'website': 'http://www.lagunaresorts.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'Laguna Resorts & Hotels Public Company Limited, together with its subsidiaries, engages in the hotel and property development businesses. The company operates through Hotel Business, Property Development, and Office Rental segments. It operates five hotels in Laguna Phuket, including Angsana Laguna Phuket, Banyan Tree Phuket, Angsana Villas Resort Phuket, Cassia Phuket, and Laguna Holiday Club Phuket Resort located in Phuket; the Banyan Tree Bangkok hotel located in Bangkok; and golf clubs comprising Laguna Golf Phuket and Laguna Golf Bintan, as well as sells merchandise. The company also develops and sells properties; sells holiday club memberships; and leases spa, land, building, offices, and shops. In addition, it is involved in travel operations and Farming and restaurant business. The company was founded in 1983 and is headquartered in Bangkok, Thailand. Laguna Resorts & Hotels Public Company Limited operates as a subsidiary of Banyan Tree Assets (Thailand) Company Limited.'
    }
    ,

    # 301-320
    'LST.BK': {
        'name': 'Lam Soon (Thailand) Public Company Limited',
        'address': '64 Soi Bangna-Trad 25 North Bangna Subdistrict Bangna District Bangkok 10260 Thailand',
        'phone': '66 2 361 8959',
        'website': 'http://www.lamsoon.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Lam Soon (Thailand) Public Company Limited manufactures and distributes palm oil in Thailand. The company offers cooking oil, margarine, shortening, and special vegetable fat; pastry and flour; seasoning and sauces; organic rice, wheat, spaghetti, macaroni, fusilli, and penne; salted and unsalted butter; and coconut, soybean, sunflower seed, corn, olive, blended canola, sunflower, and rice bran oil. It also engages in the manufacture and distribution of processed fruits and vegetables, canned juice, and drinks; processing of crude and kernel palm oil; manufacture of frozen fruits and vegetables; oil palm plantation activities; holding of concessions to use forest reserve land; and generation of electricity using biogases. The company was incorporated in 1974 and is headquartered in Bangkok, Thailand.'
    },
    'LUXF.BK': {
        'name': 'Luxury Real Estate Investment Fund',
        'address': 'Abdulrahim Place Building 32nd Floor 990 Rama 4 Road Silom, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 636 1800',
        'website': 'https://www.eastspring.co.th/',
        'sector': 'Real Estate',
        'industry': 'REIT—Diversified',
        'description': 'The Fund has invested in freehold right on land, property and other assets. The Land is located on Six Senses Yao Noi Project, Koh Yao District, Phang Nga Province.'
    },
    'M.BK': {
        'name': 'MK Restaurant Group Public Company Limited',
        'address': '1200 Debaratna Road Bangnatai Bangna Bangkok 10260 Thailand',
        'phone': '66 2 836 1000',
        'website': 'http://www.mkrestaurant.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Restaurants',
        'description': 'MK Restaurant Group Public Company Limited, together with its subsidiaries, sells food and beverages through restaurants under the MK Restaurants name in Thailand. The company operates through two segments, Restaurant Business and Other Businesses. It also provides training services; manufactures and distributes food products; and researches and develops food and beverage products. The company was formerly known as MK Restaurant Company Limited and changed its name to MK Restaurant Group Public Company Limited in August 2012. MK Restaurant Group Public Company Limited was founded in 1962 and is based in Bangkok, Thailand.'
    },
    'MACO.BK': {
        'name': 'Master Ad Public Company Limited',
        'address': 'No.21, TST TOWER 21-22nd Floors Viphavadi-Rangsit Road Chom Phon, Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 938 3388',
        'website': 'http://www.masterad.com',
        'sector': 'Communication Services',
        'industry': 'Advertising Agencies',
        'description': 'Master Ad Public Company Limited, together with its subsidiaries, provides advertising services in Thailand, Hong Kong, and Vietnam. The company operates in two segments, Advertising and System Installation Service segments. The company provides street furniture comprising LED digital screens; out of home media services for highway, city center, business area, airports, and other spots; and system integration services for advertising and public transportation. It also provides media rental services; invests in advertising media; and distributes software and computer related products including system development, installation, and maintenance. Master Ad Public Company Limited was founded in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'MAJOR.BK': {
        'name': 'Major Cineplex Group Public Company Limited',
        'address': '1839, 1839/1-6 Phaholyothin road Ladyao Jatujak Bangkok 10900 Thailand',
        'phone': '66 2 515 5555',
        'website': 'http://www.majorcineplex.com',
        'sector': 'Communication Services',
        'industry': 'Entertainment',
        'description': 'Major Cineplex Group Public Company Limited, together with its subsidiaries, operates as a lifestyle entertainment company primarily in Thailand. It operates through five segments: Cinema Business, Advertising Business, Bowling and Karaoke Business, Rental and Services Business, and Movie Content Business. The Cinema Business segment offers theater, foods and drinks, and relevant services. This segment operates cineplexes under the Major Cineplex, EGV Cinema, Paragon Cineplex, Esplanade Cineplex, Paradise Cineplex, Mega Cineplex, Hatyai Cineplex, Quartier CineArt, Westgate Cineplex, Cineplex, Icon Cineconic, and Major Cinema brands. The Advertising Business segment provides various advertising services, including screen advertising, VDO walls, tri-vision, plasma screens, menu board, outdoor media, and 4D ads. The Bowling and Karaoke Business segment provides bowling services under the Major Bowl Hit and Blu-O Rhythm & Bowl brands; karaoke rooms; and Sub-Zero, an ice skate rinks. The Rental and Services Business segment offers retail spaces for rent in the cineplexes. The Movie Content Business segment produces and distributes films; distributes VCD/DVD, Blu-ray, and film rights; and engages in advertising, satellite broadcasting, and television programing activities. The company was founded in 1995 and is based in Bangkok, Thailand.'
    },
    'MAKRO.BK': {
        'name': 'Siam Makro Public Company Limited',
        'address': '1468 Phatthanakan Road Khwaeng Phatthanakan Khet Suan Luang Bangkok 10250 Thailand',
        'phone': '66 2 067 8999',
        'website': 'http://www.siammakro.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Food Distribution',
        'description': 'Siam Makro Public Company Limited operates cash and carry trade centers under the Makro name. It operates through Cash and Carry, Retail, Mall Rental, and Food Services segments. The companys trade centers sell food and non-food products to registered members, including small and medium-sized businesses, retailers, caterers, professional sectors, and institutions. It offers freight, delivery rental, and storage services; marketing and consulting services; and imports, exports, trades in, and distributes food products. The company is also involved in the provision of technical and support services; trading of non-food products; investing and operation of retail business and mall rental activities; importing and trading of frozen and chilled foods; telecommunication business; and operation of restaurant and minimart. As of December 31, 2021, it operated 135 Makro stores and 7 frozen shops. The company was incorporated in 1988 and is headquartered in Bangkok, Thailand. Siam Makro Public Company Limited is a subsidiary of CP ALL Public Company Limited.'
    },
    'MALEE.BK': {
        'name': 'Malee Group Public Company Limited',
        'address': 'No. 401/1 Moo 8, Phaholyothin Road Lam Luk Ka 12130 Thailand',
        'phone': '66 2 080 7899',
        'website': 'http://www.maleegroup.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Malee Group Public Company Limited, together with its subsidiaries, manufactures and distributes canned food and juice, and non-alcohol beverages products in Thailand and internationally. It manufactures and distributes canned fruits, and UHT and pasteurized fruit juices under Malee brand; UHT and pasteurized milk under Farm Chokchai brand; and other beverage products under Malee Brand. In addition, it offers research and development of scientifically transformation agriculture; provides office buildings for rent; operates agriculture and dairy farm. The company was formerly known as Malee Sampran Public Company Limited and changed its name to Malee Group Public Company Limited in April 2016. Malee Group Public Company Limited was founded in 1978 and is based in Lam Luk Ka, Thailand.'
    },
    'MANRIN.BK': {
        'name': 'Mandarin Hotel Public Company Limited',
        'address': '662 Rama 4 Road Mahaprutharam Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 238 0230',
        'website': 'http://www.mandarin-bkk.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'Mandarin Hotel Public Company Limited engages in hotel and resort business in Thailand. The company was founded in 1965 and is headquartered in Bangkok, Thailand.'
    },
    'MATCH.BK': {
        'name': 'Matching Maximize Solution Public Company Limited',
        'address': 'No. 305/12, Soi Sukhothai 6 Sukhothai Road Dusit Bangkok 10300 Thailand',
        'phone': '66 2 669 4200',
        'website': 'http://www.matchinggroup.com',
        'sector': 'Communication Services',
        'industry': 'Entertainment',
        'description': 'Matching Maximize Solution Public Company Limited, together with its subsidiaries, engages in television (TV) content production and other related businesses. It produces television programs; provides post production and edits visuals and audio effects of films; commercial production, including broadcasting of advertisement or program; offers film production equipment for rent and related services; selling of goods; provides services and rents studio; offers production service; and is involved in co-operation of movie films. The company was formerly known as Matching Studio Public Company Limited and changed its name to Matching Maximize Solution Public Company Limited in May 2010. The company was founded in 1992 and is based in Bangkok, Thailand. Matching Maximize Solution Public Company Limited operates as a subsidiary of The BBTV Productions Co., Ltd.'
    },
    'MATI.BK': {
        'name': 'Matichon Public Company Limited',
        'address': '12 Tethsaban-Narueman Road Prachanivate 1 Ladyao Chatuchuk Bangkok 10900 Thailand',
        'phone': '66 2 589 0020',
        'website': 'http://www.matichon.co.th',
        'sector': 'Communication Services',
        'industry': 'Publishing',
        'description': 'Matichon Public Company Limited, together with its subsidiaries, publishes newspapers, pocketbooks, and journals in Thailand. The company also provides advertisement services; preparation of various advertising media including engagement of advertising materials; and organizes exhibitions and various activities; training services, and seminars. Matichon Public Company Limited was founded in 1978 and is based in Bangkok, Thailand.'
    },
    'MAX.BK': {
        'name': 'Max Metal Corporation Public Company Limited (Listed company which has possibility to be delisted)',
        'address': '90 CW Tower Unit B2202, 22nd Floor Ratchadaphisek Road Huay Kwang Sub-District, Huay Kwang District Bangkok 10310 Thailand',
        'phone': '66 2 168 3018',
        'website': 'http://www.maxmetalcorp.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'The Company has invested in1. Producing and distributing palm oil, crude palm seed oil, crude palm oil, plam seed meal (as livestock food), organic fertilizers.2. Golf Club and Resort.3. Producing and distributing the alternative energy.'
    },
    'MBK.BK': {
        'name': 'MBK Public Company Limited',
        'address': 'MBK Center Building 8th Floor 444 Phayathai Road Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 853 9000',
        'website': 'http://www.mbkgroup.co.th',
        'sector': 'Industrials',
        'industry': 'Conglomerates',
        'description': 'MBK Public Company Limited, together with its subsidiaries, engages in shopping center and real estate business in Thailand, the United States, Canada, Europe, and the Asia Pacific. It also engages in hotel and tourism, golf, food solution, financial, auction, corporate supporting center, and other business. The company offers property management and security services, personal management services, processing and packaging of rice, motor cycle hire purchase, car park rental, trading, and IT services; and food, shopping, and fitness centres. In addition, it provides leasing and hire purchase, hotel management and travel, golf course and real estate, investment, call center services, online selling, CRM services, loyalty program, and vehicle brokering services, as well as survey and appraisal services, ware house, land rental and transportation, and inventory trading and insurance broker services. The company was incorporated in 1974 and is based in Bangkok, Thailand.'
    },
    'MC.BK': {
        'name': 'MC Group Public Company Limited',
        'address': 'No. 448, 450 On Nut Road Prawet Sub-District Prawet District Bangkok 10250 Thailand',
        'phone': '66 2 329 1050',
        'website': 'http://www.mcgroupnet.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Apparel Manufacturing',
        'description': 'MC Group Public Company Limited, together with its subsidiaries, manufactures, distributes, and retails apparel, accessories, and lifestyle products in Thailand. It offers ready-to-wear clothing and apparels, as well as bags, belts, and activewears. The company markets its products under the Mc, Mc Lady, Mc Mini, The Blue Brothers, McT, U-P, and M&C brands. It also offers skincare and aromatic products; and inventory management services for online and other businesses. In addition, the company manages PCs and warehouse employees; and distributes products and services through online/internet channel, as well as manages trade and products. As of June 30, 2022, it operated a network of 638 points of sales in Thailand, as well as 9 points of sales internationally. The company also offers its products online through mcshop.com. MC Group Public Company Limited was founded in 1975 and is headquartered in Bangkok, Thailand.'
    },
    'M-CHAI.BK': {
        'name': 'Mahachai Hospital Public Company Limited',
        'address': '927/43 K., Settakij 1 Road Mahachai Amphur Muang Samut Sakhon 74000 Thailand',
        'phone': '66 3 442 4990',
        'website': 'http://www.mahachaihospital.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Mahachai Hospital Public Company Limited operates private hospitals under the Mahachai Hospital name in Thailand. It is also involved in the trading of medical and other supplies. The company was incorporated in 1987 and is headquartered in Samut Sakhon, Thailand.'
    },
    'MCOT.BK': {
        'name': 'MCOT Public Company Limited',
        'address': '63/1 Rama IX Road Hauy Kwang Bangkok 10310 Thailand',
        'phone': '66 2 201 6000',
        'website': 'http://www.mcot.net',
        'sector': 'Communication Services',
        'industry': 'Broadcasting',
        'description': 'MCOT Public Company Limited, together with its subsidiaries, engages in the mass media business in Thailand. It operates through Television business, Radio broadcasting business, Digital terrestrial television broadcasting business, and Digital and new businesses segments. The company provides digital terrestrial television (TV) broadcasting network services, including a high definition variety and standard definition family channels with programs comprising news and situation report, entertainment, edutainment, general knowledge, and sports; and engages in the production, marketing, and management of broadcasting various informative and entertaining radio programs through a network of 62 central and regional radio stations broadcasting in FM and AM frequencies in the areas of politics, economy, society, foreign affairs, technology, life balance, music, sports, tourism, health and recreation activities, and news reports, as well as public and local interest programs. It is also involved in the production, gathering, storage, and dissemination of news and information through various media platforms, including Modernine Television Station, 9 MCOT HD Channel 30, and radio station network, as well as electronic media comprising website, social media, cooperation, and news exchange with foreign news agencies and other media channels. In addition, the company offers satellite TV rental services; television network services; digital media services through the internet and other platforms; and operates academic and training institute that provides a range of mass media training courses. MCOT Public Company Limited was founded in 1977 and is headquartered in Bangkok, Thailand.'
    },
    'MCS.BK': {
        'name': 'M.C.S. Steel Public Company Limited',
        'address': '70 Moo 2 Changyai Bangsai Phra Nakhon Si Ayutthaya 13290 Thailand',
        'phone': '66 3 537 2961',
        'website': 'http://www.mcssteel.com',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'M.C.S. Steel Public Company Limited produces and distributes structural steel products for building construction in Thailand and internationally. The company engages in the fabrication of steel structure buildings, power plants, bridges, and general steel works. It is also involved in welder training and real estate activities; and the provision of engineering and design services, as well as parts. The company was formerly known as M.C.S. HOKOKU CO., LTD. and changed its name to M.C.S. Steel Public Company Limited in 2001. M.C.S. Steel Public Company Limited was incorporated in 1992 and is headquartered in Ayutthaya, Thailand.'
    },
    'MDX.BK': {
        'name': 'MDX Public Company Limited',
        'address': 'Column Tower Floor 12A No. 199 Ratchadaphisek Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 302 2300',
        'website': 'http://www.mdx.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'MDX Public Company Limited, together with its subsidiaries, invests in and develops real estate and infrastructure projects. It operates through three segments: Real Estate, Electricity Generation and Distribution, and Others Business. The company also generates and distributes electricity from renewable energy; invests in various electrical power production and distribution projects; and provides investment and financial consulting services. In addition, it offers land management and rental services. The company was incorporated in 1988 and is based in Bangkok, Thailand.'
    },
    'MEGA.BK': {
        'name': 'Mega Lifesciences Public Company Limited',
        'address': '909, Ample Tower 9th floor Debaratna Road Bangna Nuea, Bangna Bangkok 10260 Thailand',
        'phone': '66 2 769 4222',
        'website': 'http://www.megawecare.com',
        'sector': 'Healthcare',
        'industry': 'Drug Manufacturers—Specialty & Generic',
        'description': 'Mega Lifesciences Public Company Limited, together with its subsidiaries, manufactures and sells health food supplements, prescription pharmaceutical products, over-the-counter (OTC) products, herbal products, vitamins, and fast moving consumer goods. The company operates through three segments: Brands, Distribution, and Original Equipment Manufacture. It provides various medicines for allergy, blood circulation and memory, bone and joint, kids, liver and digestive, eye, heart, pain, skin, sleeping, well-being, herbal, and cough and cold care, as well as vitamins, probiotics, medical and sports nutrition, and mens and womens care products; and prescription medicines in the areas of anti-allergic, anti-infective, central nervous system, cardio vascular system, dermatology, diabetes, gastroenterology, gynaecology, nephrology, oncology, ophthalmology, orthopaedic, pain, respiratory, rheumatology, and urology. The company also offers logistical and marketing services for the sale of goods manufactured by third parties, as well as involved in the software design, development, and other services business. It operates in the Asia Pacific, the Middle East, Africa, and the Commonwealth of Independent States. The company was incorporated in 1982 and is headquartered in Bangkok, Thailand. Mega Lifesciences Public Company Limited is a subsidiary of Unistretch Limited.'
    },
    'MENA.BK': {
        'name': 'Mena Transport Public Company Limited',
        'address': '280/8, Moo 9 Tub Kwang Kaeng Khoi 18260 Thailand',
        'phone': '66 3 620 0321',
        'website': 'http://www.menatransport.co.th',
        'sector': 'Industrials',
        'industry': 'Trucking',
        'description': 'Mena Transport Public Company Limited provides concrete transportation concrete transportation services in Thailand. It operates through Transportation Services, Concrete Transportation Services and Sale of Materials, and Equipment and Tools for Construction segments. Mena Transport Public Company Limited was incorporated in 1993 and is headquartered in Kaeng Khoi, Thailand.'
    },
    'METCO.BK': {
        'name': 'Muramoto Electron (Thailand) Public Company Limited',
        'address': 'No. 886 Ramindhra Road Khwaeng Kannayao Khet Kannayao Bangkok 10230 Thailand',
        'phone': '66 2 518 1280',
        'website': 'http://www.metco.co.th',
        'sector': 'Technology',
        'industry': 'Electronic Components',
        'description': 'Muramoto Electron (Thailand) Public Company Limited manufactures and sells metal and plastic parts for audio/visual equipment; and electronic equipment for automobiles and office automation appliances in Thailand, Japan, the United States, and internationally. It operates through three segments: Electric Parts for Automotive Business, Electronic Parts for Office Automation Business, and Other Business. The company offers car related products, such as display audio units, audio panels, CD and DVD changers, gear units, air bag parts, keyless entry transmitters and receivers, corner sensors, press and window regulator parts, mounting boards for keyless entry receivers, print circuit board assemblies for CD changers, and mounting boards for cameras. It also manufactures video cameras and single-lens reflex camera products for consumers, including video camera LCD units, back cover and lens units for single lens reflex cameras, and top cover units for mirrorless cameras; and printer finished products and electronic parts, such as printer finished products, thermal fuses, hermetic terminals, and magnetron filter box parts for use in industrial applications. The company was founded in 1987 and is headquartered in Bangkok, Thailand. Muramoto Electron (Thailand) Public Company Limited is a subsidiary of Muramoto Industry Co., Ltd.'
    }
    ,

    # 321-340
    'MFC.BK': {
        'name': 'MFC Asset Management Public Company Limited',
        'address': '199 Column Tower Ground Floor & 21st-23rd Floor Ratchadapisek Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 649 2000',
        'website': 'http://www.mfcfund.com',
        'sector': 'Financial Services',
        'industry': 'Asset Management',
        'description': 'MFC Asset Management Public Company Limited is a publicly owned investment manager. The firm manages mutual funds for its clients. It also manages provident funds for its clients. The firm invests in public equity and fixed income markets of the world. It also invests in industrial property. The firm deals in acquiring and leasing the property. It includes freehold and leasehold, ownership and freehold rights of land and factories. The firm conducts in-house research to make its investments. MFC Asset Management Public Company Limited was previously known as The Mutual Fund Public Company Limited. MFC Asset Management Public Company Limited was founded on 14 March 1975, and is based in Bangkok, Thailand.'
    },
    'MFEC.BK': {
        'name': 'MFEC Public Company Limited',
        'address': '349 SJ Infinite One Business Complex Vibhavadi-Rangsit Road Chompol Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 821 7999',
        'website': 'http://www.mfec.co.th',
        'sector': 'Technology',
        'industry': 'Information Technology Services',
        'description': 'MFEC Public Company Limited, together with its subsidiaries, provides system implementation and maintenance, and program development and related services in Thailand. The company operates through Systems Integration, Maintenance Service, IT Professional Service, and Cloud Computing Service segments. It offers database and big data solutions, application infrastructure, and analytic and business intelligent services; lending solutions, and data and endpoint security; technical operation and professional, various service packages, and cloud platform services; digital process automation, customer service and financial solutions, and enterprise content management; and system infrastructure, modernize datacenter, intelligent data protection, and digital workplace services. In addition, the company offers outsourcing and managed, installation and maintenance, Microsoft, and other product support services; and RPA support services, as well as sells computers and computer systems. Further, it is involved in the development and sale of computer software, which includes entertainment media; provision of electronic payment gateway services; sale and development of computer programs; acts as a consultant for designing the network systems and developing computer programs; consulting, monitoring, and development of blockchain platform and off-chain applications; provision of consulting and personnel recruitment services; designs working systems; and IT system maintenance services. MFEC Public Company Limited was founded in 1997 and is headquartered in Bangkok, Thailand.'
    },
    'MICRO.BK': {
        'name': 'Micro Leasing Public Company Limited',
        'address': '863/3 Petchkasem Road Sanamchan Sub-district Mueang District Nakhon Pathom 73000 Thailand',
        'phone': '66 3 410 9200',
        'website': 'http://www.microleasingplc.com',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Micro Leasing Public Company Limited provides hire-purchase finance for six-wheel and ten-wheel trucks, and motorcycles in Thailand. It also offers life and non-life insurance brokerage, and finance services. The company was founded in 1994 and is headquartered in Nakhon Pathom, Thailand.'
    },
    'MIDA.BK': {
        'name': 'Mida Assets Public Company Limited',
        'address': '267 Charansanitwong Road Bang-Or Bangplad Bangkok 10700 Thailand',
        'phone': '66 2 434 2390-7',
        'website': 'http://www.midaassets.com',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Mida Assets Public Company Limited engages in the sale and hire-purchase of electronic home appliances and motorcycles in Thailand. It offers products on hire purchase, such as televisions, DVD players, air conditioners, home theatre sets, refrigerators, washing machines, electric fans, etc. The company also develops real estate properties; operates hotels; rents golf courses; and provides real estate agency services. In addition, it offers advertising services; public relation and events organizing services; financial services for used cars; and security guard services. Further, the company offers asset management services. The company was formerly known as Nakornpathom Mida 1991 and changed its name to Mida Assets Public Company Limited in 1997. Mida Assets Public Company Limited was founded in 1991 and is based in Bangkok, Thailand.'
    },
    'M-II.BK': {
        'name': 'MFC Industrial Investment Property and Leasehold Fund',
        'address': '199 Column Tower Ground Floor & 21st-23rd Floor Ratchadapisek Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 649 2000',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'The Fund has invested in freehold right of land and building in two locations consist of 16 buildings in TFD industrial estate with land 34 Rai 1 Ngarn 31.6 Square Wah and 1 building in Nava Nakorn Industrial Promotional Zone with land 2 Rai 2 Ngarn 2.40 Square Wah and leasehold right of novation of lease and sublease of land 29 Rai 1 Ngarn 46.09 Square Wah with right of 18 buildings in Laem Chabang Industrial Estate and leasehold right of land 25 Rai 1 Ngarn 96 Square Wah with right of 17 buildings on King Kaew road.'
    },
    'MILL.BK': {
        'name': 'Millcon Steel Public Company Limited',
        'address': '9, 11, 13, Soi Banggradee 32 Banggradee Road Samaedum Bangkhuntien Bangkok 10150 Thailand',
        'phone': '66 2 896 4444',
        'website': 'http://www.millconsteel.com',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'Millcon Steel PLC Group or MILLCON is a manufacturer and a distributor of a complete range of steel products, of which both domestic and international institutions certify. MILLCON strives for excellent operation capability to create value for all stakeholders with 3 strategic investments: (1) Vertical Integration by investing in construction material distribution companies, (2) Customer-centric Differentiation by investing the manufacture of specialized steel products for automobile manufacturing industry, and (3) Demand-oriented Supply Chain by investing in auxiliary companies. The strategy revolves around the concept ?Think Beyond Steel? where the core business operation is supported and strengthen to create value for customers in every business aspect.'
    },
    'MINT.BK': {
        'name': 'Minor International Public Company Limited',
        'address': '88 The Parq Building 12th Floor Ratchadaphisek Road Klongtoey Subdistrict, Klongtoey Dist Bangkok 10110 Thailand',
        'phone': '66 2 365 7500',
        'website': 'http://www.minor.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'Minor International Public Company Limited, together with its subsidiaries, operates as a hospitality, restaurant, and lifestyle company in Thailand, China, Australia, and internationally. It operates in four segments: Hotel, Mixed use, Restaurant, and Retail. The company operates The Pizza Company, The Coffee Club, Riverside, Benihana, Thai Express, Bonchon, Swensens, Sizzler, Dairy Queen, and Burger King brands. It also invested in, owned, and operated a portfolio of hotels and serviced suites under the Anantara, Avani, Oaks, Tivoli, NH Collection, NH Hotels, nhow, Elewana Collection, Four Seasons, St. Regis, JW Marriott, Radisson Blu, and Minor International brands in countries across the Asia Pacific, the Middle East, Africa, the Indian Ocean, Europe, and the Americas. In addition, the company distributes fashion and lifestyle products under the Anello, Bodum, Bossini, Charles & Keith, Esprit, Joseph Joseph, OVS, Radley, Zwilling J.A. Henckels, and Minor Smart Kids brands through retail points of sale; and provides online shopping and contract manufacturing services. Further, it is involved in the shopping mall, food and beverage sale, spa, supply chain management, distribution, management, vacation club point sale, entertainment, franchise, marketing, consulting, tour operation, asset management, airport lounge, and healthcare businesses; property investment, development, and sales activities; operation of business school; and manufacture and sale of cheese and ice-cream. The company was formerly known as Royal Garden Resorts Plc. and changed its name to Minor International Public Company Limited in 2005. Minor International Public Company Limited was founded in 1978 and is headquartered in Bangkok, Thailand.'
    },
    'MIPF.BK': {
        'name': 'Millionaire Property Fund',
        'address': '9th, 24th Floor Siam Piwat Tower Building 989 Rama 1 Road Patumwan Bangkok 10330 Thailand',
        'phone': '66 2 659 8888',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Office',
        'description': 'Millionaire Property Fund is a closed-ended real estate investment trust launched and managed by One Asset Management Limited. It invests in the real estate markets of Thailand. The fund seeks to invest in a diversified portfolio of real estate related assets. Millionaire Property Fund was formed on January 25, 2005 and is domiciled in Thailand.'
    },
    'MIT.BK': {
        'name': 'MFC Industrial Real Estate Investment Trust',
        'address': '199 Column Tower Ground and 21st-23rd Floors Ratchadapisek Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 649 2182',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'MFC Industrial Real Estate Investment Trust, through its subsidiary, APUK Ltd, invests in and owns land and data center building located in London, the United Kingdom. The company qualifies as a real estate investment trust for federal income tax purposes. It generally would not be subject to federal corporate income taxes if it distributes at least 90percent of its taxable income to its stockholders. MFC Industrial Real Estate Investment Trust is based in Bangkok, Thailand.'
    },
    'MJD.BK': {
        'name': 'Major Development Public Company Limited',
        'address': '141 Major Tower 16th Floor Soi Thonglor 10, Sukhumvit 55 Klongton Nua, Wattana Bangkok 10110 Thailand',
        'phone': '66 2 030 1111',
        'website': 'http://www.mjd.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Major Development Public Company Limited, together with its subsidiaries, engages in the development and sale of properties in Thailand. The company operates through three segments: Property Development, Hotel Business, and Rental and Service Business. It is also involved in hotel; office building space rental and service; real estate agency, representative, and advisory; condominium juristic person management; and high-end condominium development businesses. Major Development Public Company Limited Major Development Public Company Limited was founded in 1999 and is headquartered in Bangkok, Thailand.'
    },
    'MJLF.BK': {
        'name': 'Major Cineplex Lifestyle Leasehold Property Fund.',
        'address': '400/22 KASIKORNBANK Building 6th and 12th Floor Phahon Yothin Road Samsen Nai Sub-District, Phaya Thai District Bangkok Thailand',
        'phone': '66 2 673 3999',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Retail',
        'description': 'The Fund has invested in the leasehold rights of two large lifestyle entertainment complexes i.e., Major Cineplex Ratchyothin and Major Cineplex Rangsit Projects. Additionally, it has invested on the leasehold rights of Suzuki Avenue, the community mall project, at Ratchayothin.'
    },
    'MK.BK': {
        'name': 'M.K. Real Estate Development Public Company Limited',
        'address': 'No.345 Surawong Building 6th- 8th Floor Surawong Road Suriyawong, Bang Rak District Bangkok 10500 Thailand',
        'phone': '66 2 234 8888',
        'website': 'http://www.mk.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'M.K. Real Estate Development Public Company Limited engages in the property development business in Thailand. The company operates through five segments: Real Estate; Rental Warehouse, Factory and Others; Golf Services; Property Management; and Health and Wellness Center. It develops and sells land, houses, and condominiums; and provides property management services. The company is also involved in building and parking rental activities; and golf course business. In addition, it operates health and wellness centers. The company was founded in 1956 and is headquartered in Bangkok, Thailand.'
    },
    'ML.BK': {
        'name': 'Mida Leasing Public Company Limited',
        'address': '48/1-5 Soi Chaengwattana 14 Chaengwattana Road Thung Song Hong Lak Si Bangkok 10210 Thailand',
        'phone': '62 2 574 6901',
        'website': 'http://www.mida-leasing.com',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Mida Leasing Public Company Limited provides financial services for used cars hire-purchasing and management of non-performing assets in Thailand. The company also engages in the asset management from transferred non-performing asset of financial institutions. It also provides other financial services. The company was founded in 2000 and is headquartered in Bangkok, Thailand.'
    },
    'MNIT.BK': {
        'name': 'MFC-Nichada Thani Property Fund',
        'address': '199 Column Tower Ground Floor & 21st-23rd Floor Ratchadapisek Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 649 2000',
        'website': 'http://www.mfcfund.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Residential',
        'description': 'The Fund has invested (freehold) in 1) Lakeshore-North Apartment Building - an apartment for rent, 2) Lakeshore-West Apartment Building - an apartment for rent, 3) Land with units of 2-storeyed private houses of Raintree Residence Project and 4) Land with units of 2-storeyed private homes of Sunshine Place Project. All assets are located in the Nichada Thani Project.'
    },
    'MNIT2.BK': {
        'name': 'MFC-Nichada Thani Property Fund 2',
        'address': '199 Column Tower Ground Floor & 21st-23rd Floor Ratchadapisek Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 649 2000',
        'website': 'http://www.mfcfund.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Residential',
        'description': 'The Fund has invested (freehold) in 1) land with units of 2-storeyed private houses located in the Regent Project 1 and 2) land with units of 2-storeyed private houses located in the Regent Project 2. These 2 projects are located in Amphur Pakkred, Nonthaburi.'
    },
    'MNRF.BK': {
        'name': 'MFC Multi-National Residence Fund',
        'address': '199 Column Tower Ground Floor and 21st-23rd Floor Ratchadapisek Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 649 2000',
        'website': 'http://www.mfcfund.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Residential',
        'description': 'The Fund has invested (freehold) in 1. Palm Tree Place, Changwattana Rd, Nonthaburi, 2. Nichada At Eastern Seaboard, Sriracha, Chonburi, and 3. Danicha Garden Condominium, Changwattana Rd, Nonthaburi.'
    },
    'MODERN.BK': {
        'name': 'Modernform Group Public Company Limited',
        'address': 'Modernform Tower, Floors 1-4 699 Srinakarin Road Phatthanakan Subdistrict Suan Luang District Bangkok 10250 Thailand',
        'phone': '66 2 094 9999',
        'website': 'http://www.modernform.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Furnishings, Fixtures & Appliances',
        'description': 'Modernform Group Public Company Limited manufactures and distributes residential and office furniture in Thailand and internationally. It operates through four segments: Furniture Business, Furniture Fitting and Other Materials Business, Rental and Service Business, and Architectural Design and Construction Business. The company offers office, home, and kitchen furniture. It also provides steel case, walk-in closet and storage, and hardware and fitting furniture. In addition, the company offers architectural design and construction services. It also sells its products through online. The company was founded in 1980 and is headquartered in Bangkok, Thailand.'
    },
    'MONO.BK': {
        'name': 'Mono Next Public Company Limited',
        'address': '29/9 Moo 4, Chaiyaphruek Road Bang Phlap Pak Kret 11120 Thailand',
        'phone': '66 2 100 8100',
        'website': 'http://www.mono.co.th',
        'sector': 'Communication Services',
        'industry': 'Entertainment',
        'description': 'Mono Next Public Company Limited, together with its subsidiaries, engages in the media and content business primarily in Thailand. The company produces and distributes entertainment content, magazines and general books, and motion pictures, as well as provides design and implementation services for online business. It also offers online and home shopping agency and location services; actor and artist services; radio station and broadcasting services; and produces TV and other programming. In addition, it provides enterprise software and digital content, and broadcasting and television services. Mono Next Public Company Limited was founded in 2002 and is headquartered in Pak Kret, Thailand.'
    },
    'MOSHI.BK': {
        'name': 'Moshi Moshi Retail Corporation Public Company Limited',
        'address': '26/18 Moo 10 Bang Khun Thian Subdistrict Chom Thong District Bangkok 10150 Thailand',
        'phone': '66 2 891 3088',
        'website': 'http://www.moshimoshi.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Department Stores',
        'description': 'Moshi Moshi Retail Corporation Public Company Limited engages in the retail and wholesale of lifestyle products in Thailand. It sells home furnishings, bags, pens, pencils, notebooks, stickers, rulers, folders, plush toys, fashion items, t-shirts, long sleeves, shorts, pajamas, beauty accessories, hats, scarves, sunglasses, shoes, perfumes, hand creams, and body lotions. The company also offers IT equipment, bluetooth speakers, headphones, mobile phone chargers, toys, food and drink products, cloth masks, keychains, eyebrow pencils, lipsticks, candies, COVID-19 testing kits, rugs, picture frames, and artificial plants. In addition, the company sells its products online. The company was founded in 2000 and is based in Bangkok, Thailand.'
    },
    'M-PAT.BK': {
        'name': 'MFC Patong Heritage Property Fund',
        'address': '199 Column Tower Ground floor & 21st - 23rd floor, Ratchadapisek road, Klongtoey Bangkok 10110',
        'phone': '66 2 649 2000',
        'website': 'http://www.mfcfund.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Hotel & Motel',
        'description': 'M-PAT is a freehold property fund which initially invest in land and building 183 units of "Patong Night Plaza" condominium, currently running a hotel business under the title "Patong Heritage Hotel" as mid-scale 164-key hotel, including other properties deemed as a component part of land as well as tools and equipments, and other assets related to the operation the hotel located nearby the hotel. M-PAT has policy in procuring benefits from the asset by leasing out the asset to hotel operator Patong Heritage Co., Ltd.for operating as a hotel for 2 years.'
    }
    ,

    # 341-360
    'MPIC.BK': {
        'name': 'M Pictures Entertainment Public Company Limited',
        'address': '234, 234/1-3, Ratchayothin Avenue Bldg 3rd Floor, Room No. B301-B306 Ratchadapisek Road Ladyao, Jatuchak Bangkok 10900 Thailand',
        'phone': '66 2 512 0300',
        'website': 'http://www.mpictures.co.th',
        'sector': 'Communication Services',
        'industry': 'Entertainment',
        'description': 'M Pictures Entertainment Public Company Limited provides media and marketing services in Thailand. The company is also involved in the distribution of film rights; film and series production; and acquisition of Thai and international film copyrights for cinema. In addition, it offers rights to free TV, cable TV, pay TV, video on demand, and other digital media services. The company was formerly known as Traffic Corner Holdings Public Company Limited and changed its name to M Pictures Entertainment Public Company Limited in May 2008. The company was incorporated in 2001 and is headquartered in Bangkok, Thailand. M Pictures Entertainment Public Company Limited is a subsidiary of Major Cineplex Group Public Company Limited.'
    },
    'MSC.BK': {
        'name': 'Metro Systems Corporation Public Company Limited',
        'address': '400 Chalermprakiat Rama IX Road Nong Bon Prawet Bangkok 10250 Thailand',
        'phone': '66 2 089 4000',
        'website': 'http://www.metrosystems.co.th',
        'sector': 'Technology',
        'industry': 'Electronics & Computer Distribution',
        'description': 'Metro Systems Corporation Public Company Limited, together with its subsidiaries, engages in trading computers and equipment, software, supplies, and office equipment, as well as the provision of related services in Thailand. It operates through four segments: Sales Computer and Equipment, Sales and Installation Software, Sales Supplies and Office Equipment, and Rental and Other Services. The company provides server, storage, and network solutions for IT infrastructure; backup, modernized application, and IBM i solutions for infrastructure; hardware, contractual, supplies, and outsourcing printing and services solutions for digital printing; and compute, network, storage, HCI, private, hybrid, public cloud, middleware and other, database, API, and backup and DR solutions, as well as operating systems for digital infrastructure. It also offers digital businesses transformation, architecture design, application development, and application and infrastructure managed services for digital transformation; workforce and unified collaboration, mobility workforce, business process automation, and IT process management solutions for digital collaboration; and SOLIDWORKS 3D CAD, simulation, electrical design, SOLIDWORKS product data management, and technical communication solutions for designed and engineering. In addition, the company provides big data integration tools and platform, BI and data visualization, advance analytics and AI/ML, and data scientist platform solutions for data and analysis. Further, it offers end point, network, server and data, cloud, and mobility security solutions for cyber security; and training and services. Additionally, the company engages in the sale, and maintenance and services of computer and computer software. Metro Systems Corporation Public Company Limited was founded in 1986 and is headquartered in Bangkok, Thailand.'
    },
    'MST.BK': {
        'name': 'Maybank Securities (Thailand) Public Company Limited',
        'address': 'No. 999/9, The Offices at Central World 20th - 21st Floors Rama 1 Road Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 658 5050',
        'website': 'http://www.maybank-ke.co.th',
        'sector': 'Financial Services',
        'industry': 'Capital Markets',
        'description': 'Maybank Securities (Thailand) Public Company Limited provides investment and securities services to corporate and individual customers in Thailand. It operates through two segments, Securities Business and Investment Banking. The company provides online trading, retail broking, derivatives trading and warrants, investment management, offshore trading, mutual funds, block trade, and institutional sale services, as well as broker agent. It also offers investment banking and advisory services, such as securities offering, mergers and acquisitions, independent financial advisory, debt and corporate restructurings, and other financial advisory; securities underwriting services; and securities trading, borrowing, and lending services. The company was formerly known as Maybank Kim Eng Securities (Thailand) Public Company Limited and changed its name to Maybank Securities (Thailand) Public Company Limited in November 2021. The company was incorporated in 1996 and is based in Bangkok, Thailand. Maybank Securities (Thailand) Public Company Limited is a subsidiary of Maybank IBG Holdings Limited.'
    },
    'M-STOR.BK': {
        'name': 'MFC-Strategic Storage Fund',
        'address': '199 Column Tower Ground Floor & 21st-23rd Floor Ratchadapisek Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 649 2000',
        'website': 'http://www.mfcfund.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Diversified',
        'description': 'The Fund has invested in freehold right of real estate which comprised of land and building and equipment of P.P. Food Supply Co. Limited, North Agricultural Co. Ltd, Agri World Co. Ltd and Siam Nippon Engineering Part Co. Ltd. which are cold storage and warehouse operators.'
    },
    'MTC.BK': {
        'name': 'Muangthai Capital Public Company Limited',
        'address': 'No.332/1 Jaransanitwong Road Bangplad Sub-district Bangplad District Bangkok 10700 Thailand',
        'phone': '66 2 483 8888',
        'website': 'http://www.muangthaicap.com',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Muangthai Capital Public Company Limited engages in the lending business in Thailand. It offers loans that are secured against vehicle registrations, land title deeds loans, and Nano finance, as well as personal loans without collateral. The company also provides car, pickup trucks, motorcycles, and agricultural vehicle loans. In addition, it provides installment loans; and hire purchase and insurance brokerage services. The company was formerly known as Muangthai Leasing Public Company Limited and changed its name to Muangthai Capital Public Company Limited in April 2018. Muangthai Capital Public Company Limited was founded in 1992 and is headquartered in Bangkok, Thailand.'
    },
    'MTI.BK': {
        'name': 'Muang Thai Insurance Public Company Limited',
        'address': '252 Rajadapisek Road Huaykwang Sub-district Bangkok 10310 Thailand',
        'phone': '66 2 665 4000',
        'website': 'http://www.muangthaiinsurance.com',
        'sector': 'Financial Services',
        'industry': 'Insurance—Property & Casualty',
        'description': 'Muang Thai Insurance Public Company Limited provides non-life insurance products and services in Thailand. The company offers motor insurance; and non-motor products that include property, marine and transportation, engineering, personal accident and health, special, liability, and miscellaneous insurance products, as well as travel and commercial insurance products. It also provides financial and investment management services for various securities, as well as engages in the reinsurance business. Muang Thai Insurance Public Company Limited was founded in 1932 and is based in Bangkok, Thailand.'
    },
    'NATION.BK': {
        'name': 'Nation Group (Thailand) Public Company Limited',
        'address': '1854 Debaratna Road 9th, 10th, 11th Floors Bangna-Tai Bangna District Bangkok 10260 Thailand',
        'phone': '66 2 338 3333',
        'website': 'http://www.nationgroup.com',
        'sector': 'Communication Services',
        'industry': 'Publishing',
        'description': 'Nation Group (Thailand) Public Company Limited, together with its subsidiaries, engages in publishes and distributes newspapers, and provides advertising and news services in Thailand. It operates through Publishing and Advertising and Related New Media and Event; and Broadcasting and New Media and Related operation segments. The company also produces television (TV) programs, as well as advertisements through TV and new media forms; and offers digital publishing services. In addition, it invests in application in areas of financial and investment. The company was formerly known as Nation Multimedia Group Public Company Limited. Nation Group (Thailand) Public Company Limited was founded in 1971 and is headquartered in Bangkok, Thailand.'
    },
    'NC.BK': {
        'name': 'Newcity (Bangkok) Public Company Limited',
        'address': '666 Rama 3 Road Bangpongphang Yannawa Bangkok 10120 Thailand',
        'phone': '66 2 294 6999',
        'website': 'http://www.newcity.co.th',
        'sector': ' Consumer Cyclical',
        'industry': 'Apparel Manufacturing',
        'description': 'Newcity (Bangkok) Public Company Limited engages in the distribution of pantyhose products, cosmetics, innerwear, and exercise outfits in Thailand. It also exports its products. The company was founded in 1964 and is based in Bangkok, Thailand.'
    },
    'NCAP.BK': {
        'name': 'Next Capital Public Company Limited',
        'address': '163 Thai Samut Building 15th Floor, Surawong Road Suriyawong Bang Rak Bangkok 10500 Thailand',
        'phone': '66 2 342 9699',
        'website': 'http://www.nextcapital.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Next Capital Public Company Limited provides motorcycle hire-purchase loans in Thailand. It also offers second-hand motorcycle hire purchase services, as well as motorcycle registration and motorcycle insurance services. The company serves individual customers and motorcycle dealers. It operates through branches. The company was formerly known as Buff (Thailand) Company Limited. Next Capital Public Company Limited was founded in 2004 and is headquartered in Bangkok, Thailand.'
    },
    'NCH.BK': {
        'name': 'N.C. Housing Public Company Limited',
        'address': '1/765 Moo 17, Soi Amporn Phaholyothin Rd. K.M. 26 Tambol Kookhot Lumlookka District Pathum Thani 12130 Thailand',
        'phone': '66 2 993 5080',
        'website': 'http://www.ncgroup.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Diversified',
        'description': 'N.C. Housing Public Company Limited operates as a real estate development company in Thailand. It develops and sells housing estates and land, detached houses, twin houses, townhouses, and condominiums; provides contractor, construction, and project and property management services; and rents space in club houses, health rehabilitation and senior care centers, etc. The company was founded in 1963 and is headquartered in Pathum Thani, Thailand. N.C. Housing Public Company Limited is a subsidiary of NCH 2555 Holding Company Limited.'
    },
    'NEP.BK': {
        'name': 'NEP Realty and Industry Public Company Limited',
        'address': '41 Soi Phaholyothin 5, Phaholyothin Road Phayathai Subdistrict Phayathai District Bangkok 10400 Thailand',
        'phone': '66 2 271 4213',
        'website': 'http://www.nep.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Packaging & Containers',
        'description': 'NEP Realty and Industry Public Company Limited engages in the production and distribution of plastic packaging products in Thailand. It is also involved in the investment business. The company was founded in 1953 and is headquartered in Bangkok, Thailand.'
    },
    'NER.BK': {
        'name': 'North East Rubber Public Company Limited',
        'address': '398 Moo 4 Khok Ma Kok Ma Sub-distric Prakhon Chai 31140 Thailand',
        'phone': '66 4 466 6928',
        'website': 'http://www.nerubber.com',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'North East Rubber Public Company Limited engages in the manufacture and sale of rubber products in Thailand. It provides rubber smoked sheets, skim block rubbers, mixtures rubber, livestock rubber mat, and standard Thai rubbers primarily for the automotive industry. The company also exports its products to China, Singapore, Bangladesh, Switzerland, and India. North East Rubber Public Company Limited was incorporated in 2006 and is headquartered in Prakhon Chai, Thailand.'
    },
    'NEW.BK': {
        'name': 'Wattana Karnpaet Public Company Limited',
        'address': '70/7-8 Suphakitjanya Road Mhakkang Sub-district Muang Udonthanee District Udon Thani 41000 Thailand',
        'phone': '66 4 221 9888',
        'website': 'http://www.wattanahospital.net',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Wattana Karnpaet Public Company Limited engages in hospital and medical trading businesses in Thailand. It operates 100 beds private hospital under the North Eastern Wattana Hospital name. The company was incorporated in 1985 and is based in Udon Thani, Thailand.'
    },
    'NEX.BK': {
        'name': 'Nex Point Public Company Limited',
        'address': '999/999 Moo 4. Bangchalongn Bang Phli Samut Prakan 10540 Thailand',
        'phone': '66 2 026 3599',
        'website': 'http://www.nexpoint.co.th',
        'sector': 'Technology',
        'industry': 'Electronic Components',
        'description': 'Nex Point Public Company Limited provides installation and consulting services for computer systems in Thailand. It also offers software, and application and platform for large logistics management system; financial technology services; sells hardware and software products; rents and sells buses; sells engines and vehicle spare parts; maintenance and repair services for engine -auto spare parts and air-conditioned buses; and distributes commercial electricity vehicles. In addition, the company is involved in the transportation and logistics, supply assets, and property rental businesses. Further, it creates, develops, and customizes computer software for IT services. The company was formerly known as Single Point Parts (Thailand) Public Company Limited and changed its name to Nex Point Public Company Limited in May 2019. Nex Point Public Company Limited was founded in 1997 and is based in Samut Prakan, Thailand.'
    },
    'NFC.BK': {
        'name': 'NFC Public Company Limited',
        'address': '88 SC Group Building 3rd Floor The Park Land Road Bangna Nuea, Bangna Bangkok 10260 Thailand',
        'phone': '66 2 348 0580',
        'website': 'http://www.nfc.co.th',
        'sector': 'Basic Materials',
        'industry': 'Agricultural Inputs',
        'description': 'NFC Public Company Limited, together with its subsidiaries, engages in the sale of chemical products and other chemical related services in Thailand. The company produces and sells ammonia, ammonium hydroxide, and sulfuric acid. It also provides wharf frontage, warehousing, logistics and liquid storage, yard, and port services. The company was formerly known as NFC Fertilizer Public Company Limited and changed its name to NFC Public Company Limited in June 2017. NFC Public Company Limited was incorporated in 1982 and is headquartered in Bangkok, Thailand.'
    },
    'NKI.BK': {
        'name': 'The Navakij Insurance Public Company Limited',
        'address': 'Sathon Thani Complex 26th and 27th Floors 100/47-55, and 90/3-6, North Sathorn Rd Silom, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 664 7777',
        'website': 'http://www.navakij.co.th',
        'sector': 'Financial Services',
        'industry': 'Insurance—Property & Casualty',
        'description': 'The Navakij Insurance Public Company Limited provides non-life insurance products in Thailand. The company offers fire, marine and transportation, motor, property, and miscellaneous insurance products. It offers its products through 24 branches. The company was formerly known as Luang Lee Insurance Company Limited and changed its name to The Navakij Insurance Public Company Limited in 1985. The Navakij Insurance Public Company Limited was founded in 1933 and is headquartered in Bangkok, Thailand.'
    },
    'NNCL.BK': {
        'name': 'Nava Nakorn Public Company Limited',
        'address': '999 Moo 13, Phaholyothin Road Tambol Klong Nueng Amphur Klong Luang Khlong Luang 12120 Thailand',
        'phone': '66 2 529 0031',
        'website': 'http://www.navanakorn.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate Service',
        'description': 'Nava Nakorn Public Company Limited operates as a real estate development company in Thailand. It operates in two segments, Real Estate Business and Utilities Services Business. The company engages in property development and industrial promotion zone projects for trading and leasing. It also provides utilities and other facilities services in the industrial promotion zone. In addition, the company operates real estate, hotels, resort hotels, and condominium, as well as other accommodation. Nava Nakorn Public Company Limited was founded in 1971 and is headquartered in Khlong Luang, Thailand.'
    },
    'NOBLE.BK': {
        'name': 'Noble Development Public Company Limited',
        'address': 'Noble Building 1035 Ploenchit Road Lumpini Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 251 9955',
        'website': 'http://www.noblehome.com',
        'sector': 'Real Estate',
        'industry': ' Real Estate—Development',
        'description': 'Noble Development Public Company Limited, together with its subsidiaries, develops and sells real estate properties in Thailand. It offers construction, rental and service, and construction consulting services. The company was founded in 1991 and is headquartered in Bangkok, Thailand.'
    },
    'NOK.BK': {
        'name': 'Nok Airlines Public Company Limited',
        'address': '222 Central Building Room No. 4235 4th Floor, Don Mueang Intl. Airport Vibhavadi Rangsit, Sanambin Sub-district Bangkok 10120 Thailand',
        'phone': '66 2 627 2000',
        'website': 'http://www.nokair.com',
        'sector': 'Industrials',
        'industry': 'Airlines',
        'description': 'Nok Airlines Public Company Limited, together with its subsidiaries, offers air transport services for passengers, and parcels and parcel posts in Thailand. The company operates in two segments, Domestic Air services and International Air services. It also provides tourism and other related services. The company was formerly known as Nok Airlines Co., Ltd. and changed its name to Nok Airlines Public Company Limited in January 2013. Nok Airlines Public Company Limited was incorporated in 2004 and is headquartered in Bangkok, Thailand.'
    },
    'NOVA.BK': {
        'name': 'Nova Empire Public Company Limited',
        'address': 'No. 88 Soi Bangna-Trad 30 Debaratana Road Bangna Tai Bangna Bangkok 10260 Thailand',
        'phone': '66 2 399 2210',
        'website': 'Technology',
        'sector': 'Solar',
        'industry': 'http://www.tiw.co.th',
        'description': 'Nova Empire Public Company Limited, together with its subsidiaries, engages in the manufacture and distribution of electricity in Thailand. The company operates in two segments, Solar Power and Wind Power. It is also involved in the investment business. The company was formerly known as Thailand Iron Works Public Company Limited and changed its name to Nova Empire Public Company Limited in January 2021. Nova Empire Public Company Limited was founded in 1958 and is based in Bangkok, Thailand.'
    }
    ,

    # 361-380
    'NRF.BK': {
        'name': 'NR Instant Produce Public Company Limited',
        'address': 'No. 99/1, Moo 4 Khae Rai Subdistrict Krathum Baen District Samut Sakhon 74110 Thailand',
        'phone': '66 3 484 9576',
        'website': 'https://www.nrinstant.com/',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'NR Instant Produce Public Company Limited, through its subsidiaries, engages in manufacture and distribution of food products in Thailand, the United States, Europe, Asia, and internationally. The company manufactures and distributes ethnic/specialty food products comprising food seasonings, recipe mix, ready-to-cook, and beverages under the THAI TASTE, Santa Maria, LEE KUM KEE, DRAGONFLY, Woolworths, and THAI CHOICE brands; plant-based food products, including jackfruit, konjac, soymilk, plantbased tuna, and eel under the BRECKS, OCEAN HUGGER FOODS, MORACLE NOODLE, good dot, UPTON, SHIP PO, THE MEATLESS FARM CO, and the Phuture brands; and distribution of alcohol gel products with other food and non-food products in V-shapes packaging under the NRF brand. It also offers sauces, condiments, and curries under the Por Kwan brand; sauce under the Sabzu brand; soups, pastes, sauces, and condiments under the Lee brand; ready-to-eat meals under the Thai Delight brand; and instant tea under the De De brand. The company offers its products through ecommerce stores. NR Instant Produce Public Company Limited was incorporated in 1991 and is headquartered in Samut Sakhon, Thailand.'
    },
    'NSI.BK': {
        'name': 'Nam Seng Insurance Public Company Limited',
        'address': 'No. 767 Krungthep-Nonthaburi Road Bangsue Sub-district Bang Sue District Bangkok 10800 Thailand',
        'phone': '66 2 017 3333',
        'website': 'http://www.namsengins.co.th',
        'sector': 'Financial Services',
        'industry': 'Insurance—Property & Casualty',
        'description': 'Nam Seng Insurance Public Company Limited provides non-life insurance in Thailand. It operates in two segments, Motor Insurance and Others Insurance. The company offers fire, marine and transportation, motor, and personal accident, as well as miscellaneous insurance products and services. It also engages in the reinsurance business. The company was founded in 1948 and is headquartered in Bangkok, Thailand.'
    },
    'NSL.BK': {
        'name': 'NSL Foods Public Company Limited',
        'address': '55/22 Moo 3 Bangbuathong-Nonthaburi bridge (345) Roa Tambol Lam Pho Ampher Bang Bua Thong Nonthaburi 11110 Thailand',
        'phone': '66 2 525 8520',
        'website': 'https://nslfoods.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'NSL Foods Public Company Limited manufactures and distributes bakery products in Thailand. The company offers snacks, sandwiches, and seafood products. It also engages in the wholesale of frozen and processed fish, aquatic products, meat, seaweeds, and vegetables. The company offers its products under the Natural BITES, BUTTERFIN, and PANGTAI brands. It also exports its products, as well as sells its products online. The company was formerly known as NSL Foods Company Limited. The company was founded in 2003 and is headquartered in Nonthaburi, Thailand.'
    },
    'NTV.BK': {
        'name': 'Nonthavej Hospital Public Company Limited',
        'address': 'No. 30/8 Ngamwongwan Road Bang Khen Sub-district Muang District Nonthaburi 11000 Thailand',
        'phone': '66 2 596 788',
        'website': 'http://www.nonthavej.co.th',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Nonthavej Hospital Public Company Limited operates as a hospital in Thailand. The company provides medical services for inpatients and outpatients, as well as emergency cases with 24-hour ambulance service. It operates specialized medical centers and clinics that offer services in the areas of laparoscope surgery, breast cancer, children and teens, neurology, dental, diabetes, diagnostic digital imaging, emergency, gastrointestinal system and liver, general medicine, gynecologic cancer treatment, gynecologic laparoscopic surgery and gynecologic cancer, gynecological, hemodialysis, ICU and CCU, minimally invasive surgery, nephrology, operations, orthopedics, physical medicine and rehabilitation, pregnancy, respiration, skin and cosmetic surgery, sleep lab, vascular, and wellness, as well as eye, ear, nose, and throat. The company also provides health checkup, ambulatory, and ward facility services. Nonthavej Hospital Public Company Limited was founded in 1981 and is headquartered in Nonthaburi, Thailand.'
    },
    'NUSA.BK': {
        'name': 'Nusasiri Public Company Limited',
        'address': 'No. 2922/209 Charn Issara Tower 2 13th floor (12 A) New Petchburi Road Bangkapi, Huay Kwang Bangkok 10310Thailand',
        'phone': '66 2 030 1399',
        'website': 'http://www.nusasiri.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Nusasiri Public Company Limited engages in the property development business in Thailand. It operates through four segments: Property Development, Rental and Service, Cultural Theme-Park, and Medical and Health. The company develops and sells land, houses, and residential condominiums. It is also involved in cultural theme park, art cultural center, golf course, IT, and hotel operations. In addition, the company invests in hospital business; leases spaces; rents vehicles; operates travel agency; and provides financial services. Further, it is involved in the medical and technological business; distributes medical and healthcare products; and develops tourism platform. The company was formerly known as Angpao Assets Public Company Limited and changed its name to Nusasiri Public Company Limited in May 2012. Nusasiri Public Company Limited was founded in 1960 and is headquartered in Bangkok, Thailand.'
    },
    'NV.BK': {
        'name': 'Nova Organic Public Company Limited',
        'address': '190/4 Moo 8 Nai Khlong Bang Pla Kot Sub-district Phra Samut Chedi 10290 Thailand',
        'phone': '66 2 417 1130',
        'website': 'https://www.nova-organic.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Nova Organic Public Company Limited produces and distributes dietary supplements and health beverages in Thailand, southeast Asia, Europe, and Hong Kong. It offers nutritional supplement products for beauty under the Donutt collagen and Donutt Total fiberly brands; nutritional supplement products for holistic health care under the LIVNEST brand; and other products, such as Lingzhi Plus Shitake, Matsutake, Chompoo24, and Q-Tin for hair and scalp. The company was founded in 2013 and is based in Phra Samut Chedi, Thailand.'
    },
    'NVD.BK': {
        'name': 'Nirvana Daii Public Company Limited',
        'address': 'No. 343/351 Prasert - Manukitch Road Nuanchan Buengkum Chomphon, Chatuchak Bangkok 10230 Thailand',
        'phone': '66 2 105 6789',
        'website': 'http://www.nirvanadaii.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate Service',
        'description': 'Nirvana Daii Public Company Limited, together with its subsidiaries, develops and sells real estate properties. It also provides construction services; and distributes precast concrete products. The company was formerly known as Daii Group Public Company Limited and changed its name to Nirvana Daii Public Company Limited in May 2017. The company is headquartered in Bangkok, Thailand.'
    },
    'NWR.BK': {
        'name': 'Nawarat Patanakarn Public Company Limited',
        'address': 'Bangna Towers A 18th - 19th Floor No. 2/3 Moo 14 Bangna-Trad Road Km. 6.5,Bangkaew Samut Prakan 10540 Thailand',
        'phone': '66 2 730 2100',
        'website': 'http://www.nawarat.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'Nawarat Patanakarn Public Company Limited provides construction contracting services to the government agencies, state enterprises, and private sectors in Thailand. The company operates through three segments: Construction Contracting Business; Real Estate Development Business; and Manufacture of Concrete Product Business. It undertakes various construction contracting works, including buildings, warehouses, and industrial plants; utilities and civil works; ports, berths, and jetties, power plants, electricity generating reservoirs; wastewater treatment systems and plants; tunneling and pipe jacking works; and construction of electrical railway transportation systems. The company also supplies pre-stressed concrete piles, pre-stressed concrete girders, and precast concrete pipes for the construction of wastewater treatment projects; parapets; and concrete pre-cast slabs and sheet piles to protect from land subsidence, as well as manufactures and sells fabricated steel products, and operates petrol station under Shell name. In addition, it is involved in the water and wastewater utility management, construction consulting, property development, and restaurant and processed food businesses. Nawarat Patanakarn Public Company Limited was incorporated in 1976 and is headquartered in Samut Prakan, Thailand.'
    },
    'NYT.BK': {
        'name': 'Namyong Terminal Public Company Limited',
        'address': '1168/52 Lumpini Tower 19th Floor Rama IV Road Thungmahamek, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 679 7357',
        'website': 'http://www.namyongterminal.com',
        'sector': 'Industrials',
        'industry': 'Marine Shipping',
        'description': 'Namyong Terminal Public Company Limited provides port, carriage, and handling of goods and warehouse services in Thailand. The company offers roll-on/roll-off terminal services for liners and automobile manufacturers to transport vehicles and general cargo at the A5 Terminal in Laem Chabang Port located in the Chonburi. It also provides parking space for preparing vehicles prior to export or after import; and office and equipment rental services, as well as vehicle cleaning services. The company was incorporated in 2012 and is headquartered in Bangkok, Thailand.'
    },
    'OCC.BK': {
        'name': 'O.C.C. Public Company Limited',
        'address': 'No. 729/4-7 Radchadaphisek Road Bangpongpang Yannawa Bangkok 10120 Thailand',
        'phone': '66 2 295 4545',
        'website': 'http://www.occ.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Household & Personal Products',
        'description': 'O.C.C. Public Company Limited distributes cosmetics, clothes, and beauty accessories primarily in Thailand. It operates through three segments: Cosmetics Distributing and Beauty Services, Clothes, and Others. The company also provides beauty services, as well as manufactures/distributes bakery and beverages. In addition, it distributes cosmetics for face and body; hair care products; and womens wear products, such as lingerie, night wears, sport wear, swim wear, and casual wear under the Covermark, Paul & Joe, KMA, GUNZE, Ritmuller, Sungrace, Shiseido Professional, BSC Hair Care, Guy Laroche, MAKEUP STUDIO, Limex, and G&G brands. Further, the company engages in the haircut service business under the Easy Cut brand. Additionally, it offers hair styling and treatment products, and musical instruments. The company distributes its products through department stores, beauty centers, beauty salons, and modern trades. The company was incorporated in 1973 and is headquartered in Bangkok, Thailand.'
    },
    'OGC.BK': {
        'name': 'Ocean Glass Public Company Limited',
        'address': '75/88-91 Ocean Tower 2 34th Floor Sukhumvit 19 (Soi Wattana) North-Klongtoey, Wattana Bangkok 10110 Thailand',
        'phone': '66 2 661 6556',
        'website': 'http://www.oceanglass.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Furnishings, Fixtures & Appliances',
        'description': 'Ocean Glass Public Company Limited, together with its subsidiaries, manufactures and sells table glassware in Thailand. It manufactures glassware for retail stores, companies, shops, governmental agencies, hotels, restaurant, etc. The company offers its products under the Ocean, POSH, and Lucaris brands. It exports its products to approximately 90 countries worldwide. Ocean Glass Public Company Limited was founded in 1979 and is headquartered in Bangkok, Thailand.'
    },
    'OHTL.BK': {
        'name': 'OHTL Public Company Limited',
        'address': '48 Oriental Avenue Soi Burapa Charoenkrung Road Khwaeng Bangrak, Khet Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 659 9000',
        'website': 'https://www.mandarinoriental.com/en/bangkok',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'OHTL Public Company Limited, together with its subsidiaries, operates hotels and restaurants in Thailand. The company operates through Hotel Operation, Food and Beverage, and Outside Shops segments. It provides spa services; operates cooking schools; and leases land and buildings. OHTL Public Company Limited was founded in 1876 is headquartered in Bangkok, Thailand.'
    },
    'OISHI.BK': {
        'name': 'Oishi Group Public Company Limited',
        'address': 'No. 90 CW Tower 36th Floor Ratchadapisek Road Huai Khwang Bangkok 10310 Thailand',
        'phone': '66 2 768 8888',
        'website': 'http://www.oishigroup.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Restaurants',
        'description': 'Oishi Group Public Company Limited, together with its subsidiaries, operates Japanese restaurant in Thailand and internationally. It operates in two segments, Food and Beverage. The company also offers ramen, and snack and frozen foods; ready-to-cook and ready-to-eat products; produces and distributes green tea, fruit juice flavored drinks, herbal drinks, and drinking water; and distributes food and beverage products under the OISHI brand. In addition, it provides brand and marketing management; consulting; and food delivery services, as well as sells food online in Thailand. The company was founded in 1999 and is based in Bangkok, Thailand. Oishi Group Public Company Limited is a subsidiary of Thai Beverage Public Company Limited.'
    },
    'ONEE.BK': {
        'name': 'The ONE Enterprise Public Company Limited',
        'address': '50 GMM Grammy Place Sukhumvit 21 Road, (Asoke) Khlongtoeinuea Vadhana Bangkok 10110 Thailand',
        'phone': '66 2 669 9697',
        'website': 'http://www.theoneenterprise.com',
        'sector': 'Communication Services',
        'industry': 'Entertainment',
        'description': 'The One Enterprise Public Company Limited engages in media and entertainment businesses in Thailand. The company produces various types of programs, such as dramas, sitcoms, variety programs, and news; manages licensed content by distributing programs through television stations, online channels, and international platforms; and owns copyrights for producing programs in television station and online channels. It also acts as a direct marketer for digital television channel; and organizes events and provides public relations materials related to the event. In addition, it engages in producing radio programs for broadcasting through radio and online channels, including websites and applications; artist management business; the sale of merchandising products related to programs or artists; and provision of rental service for filming, working, and hosting events, such as commercial shoots, TV shows, feature films, and weddings. The company is based in Bangkok, Thailand.'
    },
    'OR.BK': {
        'name': 'PTT Oil and Retail Business Public Company Limited',
        'address': 'Building B 12th Floor 555/2 Energy Complex Vibhavadi-Rangsit Road Chatuchak 10900 Thailand',
        'phone': '66 2 196 5959',
        'website': 'http://www.pttor.com',
        'sector': 'Energy',
        'industry': 'Oil & Gas Refining & Marketing',
        'description': 'PTT Oil and Retail Business Public Company Limited, together with its subsidiaries, engages in the commercial and retail marketing of petroleum products and other services in Thailand and internationally. The company operates through Mobility Business, Lifestyle Business, and Global Business segments. It offers lube oil blending, bottling, marketing, and retail services, as well as other fuel-related services; aircraft refueling services; oil and retail business management services; human resources management services; personnel services; business services; and online automotive services. The company also invests in companies, which engages in the management of fuel stations, convenience stores, and space management in fuel stations. In addition, it operates Cafe Amazon stores, convenience stores, and food and beverage retail stores; and engages in the area management, coffee, and beverage businesses. The company was incorporated in 2007 and is headquartered in Chatuchak, Thailand. PTT Oil and Retail Business Public Company Limited is a subsidiary of PTT Public Company Limited.'
    },
    'ORI.BK': {
        'name': 'Origin Property Public Company Limited',
        'address': '496 Moo 9 Tambon Samrong Nuea Mueang Samut Prakan 10270 Thailand',
        'phone': '66 2 030 0000',
        'website': 'http://www.origin.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Origin Property Public Company Limited, together with its subsidiaries, engages in development of properties in Thailand. It sells residential condominium units, land, and house. The company also provides interior decoration, property management, asset management, health, energy, and real estate agency and related services; and invests in other companies. In addition, it engages in the food and beverage; life and non-life insurance brokerage; development of artists; and sourcing, import, and distribution of liquefied natural gas businesses. The company was founded in 2009 and is based in Mueang Samut Prakan, Thailand.'
    },
    'OSP.BK': {
        'name': 'Osotspa Public Company Limited',
        'address': '348 Ramkhamhaeng Road Huamark Bangkapi Bangkok 10240 Thailand',
        'phone': '66 2 351 1000',
        'website': 'http://www.osotspa.com',
        'sector': 'Consumer Defensive',
        'industry': 'Beverages—Non-Alcoholic',
        'description': 'Osotspa Public Company Limited, together with its subsidiaries manufactures and distributes energy drinks and personal care products worldwide. The company operates in three segments: Beverage, Personal Care, and Others. It offers energy drinks under the M-150, Lipovitan-D, Chalarm, Som in-Sum, White Shark, Still Shark, Clickz Energy Drink, Shark Energy Drink, and M-Storm brand names; ready-to drink coffee under the M-Presso name; sport drinks under the M-Electrolyte brand; and functional drinks under the Peptein, C-Vitt, Calpis Lacto, and Slimma brands. The company also provides baby care products under the Babi Mild brand name; male grooming products under the Exit brand; women beauty care products under the Twelve Plus, PROhada, and OTG brands; healthcare products under the KRISNAKLAN, Utaitip, Tamjai, YATHAD 4, and BANNER brands; and confectionery products under the Botan and Ole brand names. In addition, it provides marketing and property rental services; manufactures and distributes glass, and beverage concentrates and premixes; and distributes food, beverages, and cullet products. Further, the company engages in the import, retail, and wholesale of beverages; investing in other companies; provision of research and development services; electronic commerce business; and education and sale of herbal products. Additionally, it offers manufacturing and distribution services. The company was founded in 1891 and is based in Bangkok, Thailand.'
    },
    'PACE.BK': {
        'name': 'Pace Development Corporation Public Company Limited (Listed company which has possibility to be delisted)',
        'address': 'No. 53 Sivatel Tower, 16th Floor Room 1606 WirelessRoad, Lumpini Subdistrict Pathumwan District Bangkok 10330 Thailand',
        'phone': '66 2 118 9599',
        'website': 'http://www.pacedev.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Pace Development Corporation Public Company Limited engages in the property development and management businesses in Thailand and the United States. The company was formerly known as Cinkara Company Limited and changed its name to Pace Development Corporation Public Company Limited in September 2011. Pace Development Corporation Public Company Limited was incorporated in 2003 and is headquartered in Bangkok, Thailand.'
    },
    'PAF.BK': {
        'name': 'Pan Asia Footwear Public Company Limited',
        'address': 'No. 620/5 Moo 11 Nong Kham Subdistrict Si Racha 20230 Thailand',
        'phone': '66 3 848 0020',
        'website': 'http://www.panasiafootwear.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Footwear & Accessories',
        'description': 'Pan Asia Footwear Public Company Limited engages in the manufacture and distribution of footwear and bags in Thailand. It is also involved in the manufacture of soles and parts for footwear; manufacture and distribution of plastic parts and injection; manufacture, repair, and maintenance of molds; manufacture and dyeing of fabrics; and manufacture of polypropylene cutting board and eyelets, as well as organic farming business activities. The company was incorporated in 1979 and is headquartered in Si Racha, Thailand.'
    },
    'PAP.BK': {
        'name': 'Pacific Pipe Public Company Limited',
        'address': '298, 298/2, Soi Klabcharoen Suksawat Road Tambon Pakklongbangplakod Samutprakarn Phra Samut Chedi 10290 Thailand',
        'phone': '66 2 679 9000',
        'website': 'http://www.pacificpipe.co.th',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'Pacific Pipe Public Company Limited, together with its subsidiaries, manufactures and distributes steel pipes for construction works in Thailand. It also provides steel fabrication services, such as cutting, drilling, and bending services. Pacific Pipe Public Company Limited was founded in 1972 and is headquartered in Phra Samut Chedi, Thailand.'
    }
    ,

    # 381-400
    'PATO.BK': {
        'name': 'Pato Chemical Industry Public Company Limited',
        'address': 'Pato Building 3388 New Petchburi Road Bangkapi Huaykwang Bangkok 10310 Thailand',
        'phone': '66 2 318 5612',
        'website': 'http://www.patochemical.com',
        'sector': 'Basic Materials',
        'industry': 'Agricultural Inputs',
        'description': 'Pato Chemical Industry Public Company Limited manufactures, imports, formulates, and distributes pesticides in Thailand. It offers herbicides, insecticides, acaricides, and fungicides, as well as rodenticide, mollusicide, and plant hormones. The company was founded in 1972 and is headquartered in Bangkok, Thailand.'
    },
    'PB.BK': {
        'name': 'President Bakery Public Company Limited',
        'address': '121/84-85, RS Tower Building 29th Floor Ratchadapisek Road Dindaeng Bangkok 10400 Thailand',
        'phone': '66 2 209 3000',
        'website': 'http://www.farmhouse.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'President Bakery Public Company Limited manufactures and sells bakery products in Thailand. Its bakery products include sliced and snack bread, burger and hot dog buns, snack buns, pastries, burger buns, and confectioneries; sandwich and snack cakes; fried products; and fast food and catering products, as well as hot dog and hamburger buns. In addition, it retails its products under the Deliya by Farmhouse, Madame Marco cake, Good Morning Farmhouse, Farmhouse Moon Cake, and Farmhouse brand names; and restaurants under the Shinjuku Tonkatsu Saboten name. The company also exports bakery products. President Bakery Public Company Limited was incorporated in 1980 and is headquartered in Bangkok, Thailand. President Bakery Public Company Limited is a subsidiary of Thai President Foods Public Company Limited.'
    },
    'PCC.BK': {
        'name': 'Precise Corporation Public Company Limited',
        'address': 'No.1842, Krung Thep-Nonthaburi Road Wong Sawang Bangsue 10800 Thailand',
        'phone': '66 2 910 9700',
        'website': 'http://www.precise.co.th',
        'sector': 'Industrials',
        'industry': 'Conglomerates',
        'description': 'Precise Corporation Public Company Limited engages in the production and distribution of electricity from renewable energy in Thailand and internationally. The company is also involved in the production and distribution of electricity transmission equipment; project management; electrical system maintenance and electrical equipment repair works; maintenance in low and high voltage of power industries; and power utility management activities. It also engages in the construction of power stations, transmission lines, and high voltage substations. Further, the company designs software management system, and platform and information system for enterprises; and imports and exports electrical and mechanical equipment. In addition, it engages in the production and distribution of switchgears, switchboards, load switches, control boards, and metal products. Precise Corporation Public Company Limited was formerly known as Precise Corporation Co., Ltd. and changed its name to Precise Corporation Public Company Limited in January 2018. Precise Corporation Public Company Limited was founded in 1983 and is headquartered in Bang Sue, Thailand'
    },
    'PCSGH.BK': {
        'name': 'P.C.S. Machine Group Holding Public Company Limited',
        'address': '2/1-9 Moo 3 Mittraparp Road Kokkruad Muang Nakhon Ratchasima District Nakhon Ratchasima 30280 Thailand',
        'phone': '66 4 470 1300',
        'website': 'http://www.pcsgh.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Auto Parts',
        'description': 'P.C.S. Machine Group Holding Public Company Limited manufactures and distributes automotive parts in Asia, Europe, and internationally. It provides engine parts; transmission parts; final drives; and other parts comprising steering knuckle and engine mounting bracket. The company was incorporated in 2013 and is headquartered in Nakhon Ratchasima, Thailand.'
    },
    'PDJ.BK': {
        'name': 'Pranda Jewelry Public Company Limited',
        'address': '28 Soi Bangna-Trad 28 Bangna Tai Subdistrict Bangna District Bangkok 10260 Thailand',
        'phone': '66 2 769 9999',
        'website': 'http://www.pranda.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Luxury Goods',
        'description': 'Pranda Jewelry Public Company Limited engages in the production, distribution, and retail of fine jewelry in Thailand, the United States of America, Germany, and internationally. The company offers gold and silver jewelry, and brass and fashion costume jewelry products under the PRIMA, Prima Gold, Prima Art, Merii, and Gemondo brands. It is also involved in dormitory rental activities.The company distributes its products through department stores, chain stores, websites, TV, and catalogs. Pranda Jewelry Public Company Limited was formerly known as Pranda Design Co., Ltd. The company was founded in 1973 and is headquartered in Bangkok, Thailand.'
    },
    'PEACE.BK': {
        'name': 'Peace & Living Public Company Limited',
        'address': '231/14 Soi Ekamai 7 Sukhumvit Road, 63 Khlong Tan Nuea Subdistrict Watthana District Bangkok 10110 Thailand',
        'phone': '66 2 392 1066',
        'website': 'http://www.peaceandliving.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Peace & Living Public Company Limited operates as a residential real estate development company in Thailand. It also provides after sale service for properties. The company was incorporated in 1989 and is based in Bangkok, Thailand.'
    },
    'PERM.BK': {
        'name': 'Permsin Steel Works Public Company Limited',
        'address': '4, 95-96 Moo 6 Rama 2 Road Koak-Kam Sub-district Mueang Samut Sakhon 74000 Thailand',
        'phone': '66 3 482 5090',
        'website': 'http://www.permsin.com',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'Permsin Steel Works Public Company Limited, together with its subsidiaries, manufactures and distributes steel products in Thailand. The company operates through three segments: Distribution of Rolled Steel, Manufacturing and Distribution of Metal Sheet, and Manufacturing and Distribution of Steel Pipes. It also offers hot and cold rolled steel, electro-galvanized steel, c-line, c-u, t-bar, roll forming metal sheet, and c-channel galvanized high tensile strength products, as well as steel purlins, galvanized iron, and steel coating products. In addition, the company provides steel cutting, steel slit work, packaging, and delivery services. Permsin Steel Works Public Company Limited was founded in 1989 and is headquartered in Mueang Samut Sakhon, Thailand.'
    },
    'PF.BK': {
        'name': 'Property Perfect Public Company Limited',
        'address': '100/1 Vorasombat Building 17th Floor Rama IX Road Huaykwang Bangkok 10310 Thailand',
        'phone': '66 2 245 6640',
        'website': 'http://www.pf.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Property Perfect Public Company Limited, together with its subsidiaries, engages in the real estate development business in Thailand. It develops single detached houses, duplex houses, townhouses, condominiums, shopping malls, office buildings, commercial areas, investment-purpose retail business, hotels, and overseas properties; rents residential properties; manages resorts, spas, and hotels; and provides rental property administration and contractor management services. The company also offers construction services; invests in other companies and projects; and manufactures and installs prefab structures and materials, which are parts of single houses, townhouses, and project fences, as well as condominiums. In addition, it is involved in the manufacturer and distribution of medical rubber gloves; operation of fitness clubs and sport clubs; and cultivation and sale of agricultural products. The company was founded in 1985 and is headquartered in Bangkok, Thailand.'
    },
    'PG.BK': {
        'name': 'People Garment Public Company Limited',
        'address': 'No.666, Rama3 Road Bangpongpang Yannawa Bangkok 10120 Thailand',
        'phone': '66 2 685 6500',
        'website': 'http://www.pg.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Apparel Manufacturing',
        'description': 'People Garment Public Company Limited manufactures and sells ready-to-wear garments in Thailand. The company offers mens and womens wear, swimwear, sportswear, menS underwear, and uniforms under the ARROW, LACOSTE, ELLE, and BSC brands; knitted fabrics and functional textiles; and medical textile products, such as fabric masks and personal protective equipment. The company also exports its products to Asia, the United States, and the European Union. People Garment Public Company Limited was founded in 1980 and is headquartered in Bangkok, Thailand.'
    },
    'PIN.BK': {
        'name': 'Pinthong Industrial Park Public Company Limited',
        'address': '789 Moo 1, Sai Nong Kho-Laem Chabang Road Nong Kham Subdistrict Si Racha District Chonburi 20230 Thailand',
        'phone': '66 3 8296 335',
        'website': 'https://www.pinthongindustrial.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Pinthong Industrial Park Public Company Limited develops and manages industrial estates and logistics parks. The company manages and develops real estate properties and factory buildings, as well as provides warehouses for rent. It serves in Japan, Thailand, China, and Taiwan. Pinthong Industrial Park Public Company Limited was founded in 1995 and is based in Chonburi, Thailand.'
    },
    'PJW.BK': {
        'name': 'Panjawattana Plastic Public Company Limited',
        'address': 'No. 19, 21, Soi Ekkachai 63 Ekkachai Road Klong Bang Bon Sub-district Bang Bon District Bangkok 10150 Thailand',
        'phone': '66 2 898 0018',
        'website': 'http://www.pjw.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Packaging & Containers',
        'description': 'Panjawattana Plastic Public Company Limited, together with its subsidiaries, manufactures and distributes plastic packaging and industrial plastic parts. It operates through Plant - Samuthsakhon, Plant - Chonburi, Plant - Bangkok, Plant - Tianjin (China), Plant - Jiangsu (China), Service, and Business Trading segments. The company plastic packaging products are used for containing lubricants, fresh milk and yoghurt milk, consumer products, and agro chemicals. It also trades in lid and plastic resins; commercial laundary service; and provides service to check the amount/standards of various goods and inspect measurement tools. The company was incorporated in 1987 and is headquartered in Bangkok, Thailand. '
    },
    'PK.BK': {
        'name': 'Patkol Public Company Limited',
        'address': '348 Chaloem Phrakiat Rama 9 Road Nong Bon Subdistrict Prawet District Bangkok 10250 Thailand',
        'phone': '66 2 328 1035',
        'website': 'http://www.patkol.com',
        'sector': 'Industrials',
        'industry': 'Specialty Industrial Machinery',
        'description': 'Patkol Public Company Limited, together with its subsidiaries, trades in and services various engineering products in Thailand and internationally. It offers turnkey sales services in the design, manufacturing, and installation of various industrial refrigeration machinery for ice making, supermarket, dairy and ice-cream processing, and food related processing plants and supplies industries. The company provides ice making machines, ice storage equipment, and ice handling machines; and cold room products, chillers, refrigeration equipment, supermarket showcases, and freezers. It also offers food and dairy machinery, including thermization and pasteurization machinery, UHT units, pouch filers, tubular heat exchangers, clean in place machinery; mixing and blending systems, extraction systems, fermenter systems, dissolving systems, filling systems, heating and cooling systems, and utilities systems, as well as control and automation systems, milk collection centers, and hot water units. In addition, the company provides receiving, storage, milk transport, aseptic storage, mixing, jacket, fermenter, pharmaceutical grade, and cooling tanks, as well as ultra mixers and fiter vessels. Further, it sells evaporative condensers, spare parts, and equipment for evaporative condensers; and designs, manufactures, installs, and maintains pressure and no pressure tanks. The company serves meat processing, frozen food, non-alcoholic, sauce and seasonings, pharmaceutical, chemical, cosmetics, alcoholic drink, and cold storage and distributor industries. The company was formerly known as Patanakolkarn Co., Ltd and changed its name to Patkol Public Company Limited in 1993. Patkol Public Company Limited was incorporated in 1965 and is headquartered in Bangkok, Thailand.'
    },
    'PL.BK': {
        'name': 'Phatra Leasing Public Company Limited',
        'address': '252/6, Muang Thai Phatra Complex 1 29th Floor Rachadaphisek Road Huaykwang Bangkok 10320 Thailand',
        'phone': '66 2 290 7575',
        'website': 'https://www.pl.co.th',
        'sector': 'Industrials',
        'industry': 'Rental & Leasing Services',
        'description': 'Phatra Leasing Public Company Limited provides leasing services primarily to corporate enterprises in Thailand. The company operates in two segments, Land Vehicles and Other segments. It offers operating and finance leases for executive cars, business cars, and service cars or trucks, as well as business jets, and yacht and speed boats. The company also rents cars; and machinery, equipment, office equipment, and computers, as well as provides financial services. The company was incorporated in 1987 and is based in Bangkok, Thailand.'
    },
    'PLANB.BK': {
        'name': 'Plan B Media Public Company Limited',
        'address': '1213/420 Soi Ladprao 94 Plubpla Wang Thonglang Bangkok Thailand',
        'phone': '66 2 530 8053',
        'website': 'https://www.planbmedia.co.th',
        'sector': 'Communication Services',
        'industry': 'Advertising Agencies',
        'description': 'Plan B Media Public Company Limited provides advertising media production services in Thailand. The company operates in two segments, Advertising Media and Engagement Marketing segment. It offers out of home advertising media services. In addition, the company provides digital advertising agency, advertising space rental, and airtime rental services; and mobile software applications services. Further, it manages and develops artists; operates as an advertising media design and production, and advertising agency; and offers billboard rental services. Additionally, the company organizes an esports tournament under the Thai E-League Pro name; and provides sports marketing services. Furthermore, it engages in trading of books and other printed form materials. The company was incorporated in 2005 and is based in Bangkok, Thailand.'
    },
    'PLAT.BK': {
        'name': 'The Platinum Group Public Company Limited',
        'address': 'The Platinum Fashion Mall Building 11th Floor, 222/1398, Phetchaburi Road Petchaburi Road Sub-district Ratchathewi District Bangkok 10400 Thailand',
        'phone': '66 2 121 9999',
        'website': 'https://www.theplatinumgroup.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate Services',
        'description': 'The Platinum Group Public Company Limited, together with its subsidiaries, operates in the real estate development and investment business in Thailand. It develops and rents retail space in shopping centers; and operates a hotels and food centers. The company was incorporated in 2013 and is headquartered in Bangkok, Thailand.'
    },
    'PLE.BK': {
        'name': 'Power Line Engineering Public Company Limited',
        'address': '2, Soi Sukhumvit 81 (Siripot) Sukhumvit Road Bangjak Phrakhanong Bangkok 10260 Thailand',
        'phone': '66 2 332 0345',
        'website': 'https://www.ple.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'Power Line Engineering Public Company Limited, together with its subsidiaries, engages in the design, engineering, and installation of mechanical and electrical systems for private and government sectors in Thailand and internationally. It operates through System Installation and Construction, and Real Estate Development segments. The company is also involved in the installation of telecommunication, air conditioning, sanitary and plumbing, and fire protection systems; and civil construction operations in the areas of super structures, reinforced concrete roads, diaphragm and curtain walls, and tunneling and site drainage facilities. Power Line Engineering Public Company Limited was founded in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'PLUS.BK': {
        'name': 'Royal Plus Public Company Limited',
        'address': 'No. 84/3-7 Rama II Soi 69 Samae Dam Sub-district Bang Khun Thian District Bangkok 10150 Thailand',
        'phone': '66 2 416 9209',
        'website': 'https://www.royalplus.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Beverages—Non-Alcoholic',
        'description': 'Royal Plus Public Company Limited engages in the manufacture and distribution of beverages, fruit juices, fruit juices with basil seeds, fruit juices with chia seeds, coconut milk, and soy milk. It operates in Thailand, the United States, China, and internationally. The company was incorporated in 1998 and is headquartered in Bangkok, Thailand.'
    },
    'PM.BK': {
        'name': 'Premier Marketing Public Company Limited',
        'address': '1 Premier Corporate Park Soi Premier 2 Srinakarin Road, Kwaeng Nongbon Khet Prawet Bangkok Thailand',
        'phone': '66 2 301 1000',
        'website': 'https://www.premier-marketing.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Food Distribution',
        'description': 'Premier Marketing Public Company Limited distributes consumer products in Thailand, Japan, and internationally. The company operates through Distribution of Consumer Products, Manufacture of Food, and Cold Storage Warehouse and Services segments. It distributes snack foods, confectionery, food and beverages, nutrition food and medicine, and personal care and household products. The company also manufactures and sells fish strip, sheets, coated, and crispy products under the Taro brand name; fried seaweed products under the Taro Biggu brand; and tuna related products, such as pouched and canned ready-to-eat tuna, and tuna pet food under the customer brand. In addition, it manufactures ketchup and chilli sauce under the King Kitchen brand. Further, the company provides frozen processed food, as well as space and cold storage rental services. It distributes its products through wholesalers, general retailers, sales staff; and trade stores. It also exports its tuna products to Asia, Europe, and the Middle East. The company was incorporated in 1977 and is based in Bangkok, Thailand.'
    },
    'PMTA.BK': {
        'name': 'PM Thoresen Asia Holdings Public Company Limited',
        'address': '26/26-27 Orakarn Building 8th Floor Soi Chidlom, Ploenchit Road Kwaeng Lumpinee, Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 250 0569',
        'website': 'http://www.pmthoresenasia.com',
        'sector': 'Basic Materials',
        'industry': 'Agricultural Inputs',
        'description': 'PM Thoresen Asia Holdings Public Company Limited, an investment holding company, manufactures and sells fertilizer and agrochemical products primarily in Vietnam. The company operates through two segments, Manufacture of Fertiliser and Crop Care Products; and Factory Area Management Services. Its products include NPK (nitrogen, phosphorus, and potassium) compounds, NPK synthesized chemical and microelement fertilizers, mixed fertilizers, compound and single fertilizers, and foliar, as well as pesticides. The company sells its fertilizers under the STORK trademark in Vietnam. It also exports fertilizer products to approximately 30 countries worldwide. In addition, the company supplies seeds and agriculture materials; and operates storage and warehousing facilities. Further, it manufactures, imports, and exports plant protection chemicals, as well as provides factory area management services. The company sells its products through a network of wholesalers, dealers, and suppliers. The company was founded in 1995 and is based in Bangkok, Thailand. PM Thoresen Asia Holdings Public Company Limited is a subsidiary of Thoresen Thai Agencies Public Company Limited.'
    },
    'POLAR.BK': {
        'name': 'Polaris Capital Public Company Limited (Listed company which has possibility to be delisted)',
        'address': '503/34, K.S.L. Tower Building, 18th Floor, Sri-Ayutthaya Road, Thanon Phayathai, Ratchathewi Bangkok 10400',
        'phone': 'N/A',
        'website': 'http://www.polariscap.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'The Company and subsidiaries engaged in business of property development for sales both horizontal and vertical projects.'
    },
    'POLY.BK': {
        'name': 'Polynet Public Company Limited',
        'address': '888 Moo. 11 Bangsaotong District Bang Sao Thong 10570 Thailand',
        'phone': '66 2 397 9094',
        'website': 'https://www.polynet.co.th',
        'sector': 'Industrials',
        'industry': 'Metal Fabrication',
        'description': 'Polynet Public Company Limited produces and sells rubber, plastic, and silicone related products in Thailand, Japan, and European countries. The company offers rubber and plastic products for the automotive, medical, food and beverages, electrical appliances, lighting, pet products, and sports equipment industries. It also research, develops, mold, design, mold, as well as manufactures plastic molding solutions. Polynet Public Company Limited was founded in 1999 and is headquartered in Bang Sao Thong, Thailand.'
    }
    ,

    # 401-420
    'POPF.BK': {
        'name': 'Prime Office Leasehold Property Fund',
        'address': 'Building 1, Siam Commercial Park Plaza Floor 7-8 18 Ratchadaphisek Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 949 1500',
        'website': 'https://www.popf-fund.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Diversified',
        'description': 'The Fund has invested in leasehold right on land, building and other construction, including with purchasing equipments and systems relevant to UBC 2 building. The Fund has also invested in the ownership of building and other construction, including related system and transferring the leasehold rights on land which Pleonchit Center building is located. Moreover, the fund has invested in leasehold right on land, 4 office buildings and other construction related to Bangna Tower.'
    },
    'PORT.BK': {
        'name': 'Sahathai Terminal Public Company Limited',
        'address': '51/1 Moo 3 Poo Chao Samingprai Road Tumbon Bangyaprak Prapradang Samut Prakan 10130 Thailand',
        'phone': '66 2 386 8000',
        'website': 'http://sahathaiterminal.com/',
        'sector': 'Industrials',
        'industry': 'Marine Shipping',
        'description': 'Sahathai Terminal Public Company Limited provides commercial port and logistics services in Thailand. The company is involved in the coastal port, coastal port management consultancy, tugboat, inland transport, and related merchant marine businesses. It also offers on-site container inspection, cleaning, maintenance, repair, and upgradation services; multipurpose terminal services, such as bulk and project cargo, and coastal shipping; warehousing services; and value added logistics services inside the port. The company was founded in 2007 and is based in Samut Prakan, Thailand.'
    },
    'POST.BK': {
        'name': 'Bangkok Post Public Company Limited (Listed company which has possibility to be delisted)',
        'address': 'Bangkok Post Building 136 Sunthorn Kosa Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 616 4000',
        'website': 'https://www.bangkokpost.co.th/',
        'sector': 'Communication Services',
        'industry': 'Publishing',
        'description': 'Bangkok Post Public Company Limited, together with its subsidiaries, publishes and distributes newspapers, magazines, and books in Thailand. It operates through three segments: Publishing and Advertising, Production of Television Programs, and Other. The company publishes, distributes, and advertises newspapers, including the Bangkok Post, an English-language daily newspaper; and Post Today, a Thai-language online news site, as well as Thai-language magazines under the Elle Thailand and Forbes Thailand names. It also publishes books under the Post Books name; produces multimedia and video content for television and digital media; and rents studio. In addition, the company provides digital media platforms and applications in English and Thai languages; information services through various social media platforms; and general printing services to various government and business organizations. Further, it publishes and distributes English-language lifestyle magazines, such as Guru and B Magazine, as well as offers content creation, event management, and digital marketing solutions for public agencies and private organizations. The company was formerly known as The Post Publishing Public Company Limited and changed its name to Bangkok Post Public Company Limited in May 2017. Bangkok Post Public Company Limited was founded in 1946 and is headquartered in Bangkok, Thailand.'
    },
    'PPF.BK': {
        'name': 'Pinthong Industrial Park Property Fund',
        'address': 'SCB Park Plaza 1 7-8th Floor 18 Ratchadapisek Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 949 1500',
        'website': 'https://www.scbam.com/en/fund/property-fund/fund-information/ppf',
        'sector': 'Real Estate',
        'industry': 'REIT—Residential',
        'description': 'The Fund has invested in freehold right of land, factory and warehouse buildings located in Pinthong Industrial Park Project located in Pinthong Industrial Park Project, which comprise of Pinthong Industrial Park (Pinthong 1), Pinthong Industrial Park (Laem Chabang) (Pinthong 2) and Pinthong Industrial Park (Project 3) (Pinthong 3) in the total of 90 units, consist of land with 151 rai, 1 ngarn, 87.1 square wah, and the total leasable area is 134,338.4 square meters.'
    },
    'PPP.BK': {
        'name': 'Premier Products Public Company Limited',
        'address': 'No. 2 Premier Place Soi Premier 2 Srinakarin Road Nong Bon, Prawet Bangkok 10250 Thailand',
        'phone': '66 2 301 2100',
        'website': 'http://www.premier-products.co.th',
        'sector': 'Industrials',
        'industry': 'Pollution & Treatment Controls',
        'description': 'Premier Products Public Company Limited manufactures and distributes environmental products, construction materials, and industrial products in Thailand. It operates through three segments: Water Treatment Solution, Environmental Preservation Products, and Clean Energy Business. The company offers water storage systems, wastewater management systems, grease trap systems, membrane water filter systems water treatment systems, and wastewater parts; and environmental preservation products, such as chemical resist tanks, glass fiber reinforced concrete products, noise barriers, fiberglass pipes and fittings, fiberglass coating products, and air treatment systems. It also provides solar roofs, solar inverters, and solar mounting structures, as well as produces electricity from solar power. Premier Products Public Company Limited also exports its products. The company was incorporated in 1975 and is headquartered in Bangkok, Thailand.'
    },
    'PPPM.BK': {
        'name': 'PP PRIME Public Company Limited',
        'address': '62-62/1 Moo 2 Utapao Road Nongchumpol Khao Yoi 76140 Thailand',
        'phone': '66 3 289 9881',
        'website': 'https://www.ppprime.co.th/',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'PP PRIME Public Company Limited manufactures and distributes feeds for aquatic animals and pets feed in Thailand and Japan. It operates through Aquatic Animal Feed, Pet Food, and Electricity Generation and Distribution segments. The company offers black tiger and other shrimp feed products; fish feed products; and dog, cat, and other pet food products. It also engages in the geothermal and wing power generation business; and consulting and management business. The company was formerly known as Thai Luxe Enterprises Public Company Limited and changed its name to PP PRIME Public Company Limited in September 2018. PP PRIME Public Company Limited was founded in 1987 and is headquartered in Khao Yoi, Thailand.'
    },
    'PQS.BK': {
        'name': 'Premier Quality Starch Public Company Limited',
        'address': '185 Moo 14 Kham Pa Lai Mueang Mukdahan Mukdahan 49000 Thailand',
        'phone': '66 4 264 3818',
        'website': 'https://www.pqstarch.com',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Premier Quality Starch Public Company Limited produces and sells starch from fresh roots for the food ingredients and non-food market worldwide. It offers tapioca starch; and generates electricity powered by biogas derived from an organic matter in wastewater and cassava pulp. The company was founded in 2005 and is based in Mukdahan, Thailand.'
    },
    'PR9.BK': {
        'name': 'Praram 9 Hospital Public Company Limited',
        'address': '99, Rama IX Road Bangkapi Subdistrict Huai Khwang District Bangkok 10310 Thailand',
        'phone': '66 2 202 9999',
        'website': 'http://www.praram9.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Praram 9 Hospital Public Company Limited operates a hospital under the Praram 9 Hospital name in Thailand. The company operates medicine, surgery, diabetes and metabolic, spine, neurology, thyroid and thyroid surgery, obstetrics gynecology, IVF, oncocare, emergency, imaging, LASIK, skin and cosmetic laser surgery, mind, gastroenterology and hepatobiliary, dental, check-up, eye, pediatric, sleep, ear, nose, and throat centers, as well as breast, and vaccination and travel medicine clinics. It is also involved in the operation of kidney disease and transplantation, cardiovascular, and pain management and wellness institutes. Praram 9 Hospital Public Company Limited was founded in 1992 and is based in Bangkok, Thailand.'
    },
    'PRAKIT.BK': {
        'name': 'Prakit Holdings Public Company Limited',
        'address': '88 Soi Sukhumvit 62 3rd intersection Sukhumvit Road, Phra Khanong Tai Phra Khanong Bangkok 10260 Thailand',
        'phone': '66 2 715 3000',
        'website': 'http://www.prakit.com',
        'sector': 'Communication Services',
        'industry': 'Advertising Agencies',
        'description': 'Prakit Holdings Public Company Limited, together with its subsidiaries, engages in media and advertisement, media agency, and securities investment businesses in Thailand and internationally. It is involved in media planning and buying; managing and brokering various advertising media; and producing advertising materials, such as printed materials, TV commercials, radio spots, online films, launch and sales events, and others for mainstream and online media. The company was formerly known as Prakit & FCB Public Company Limited and changed its name to Prakit Holdings Public Company Limited in December 1999. Prakit Holdings Public Company Limited was founded in 1978 and is based in Bangkok, Thailand.'
    },
    'PREB.BK': {
        'name': 'Pre-Built Public Company Limited',
        'address': '503, Bondstreet Road 1st Floor Bangpood Pakkred Nonthaburi 11120 Thailand',
        'phone': '66 2 960 1380',
        'website': 'https://www.prebuilt.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'Pre-Built Public Company Limited, together with its subsidiaries, engages in the hire construction works in Thailand. The company also manufactures and sells precast floor products; and develops and sells real estate properties. In addition, it engages in the investment activities. The company serves government organization, state enterprises, and private companies. Pre-Built Public Company Limited was founded in 1995 and is headquartered in Nonthaburi, Thailand.'
    },
    'PRECHA.BK': {
        'name': 'Preecha Group Public Company Limited',
        'address': '1919 Preecha Group Building Pattanakarn Road Suan Luang Sub district Suan Luang District Bangkok 10250 Thailand',
        'phone': '66 2 722 8855',
        'website': 'https://www.preecha.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Preecha Group Public Company Limited engages in the real estate business in Thailand. It develops and rents properties; and provides related services. The company was founded in 1989 and is headquartered in Bangkok, Thailand.'
    },
    'PRG.BK': {
        'name': 'PRG Corporation Public Company Limited',
        'address': '88, Moo 2, Tiwanont Road Bangkadee Sub-District Muang District Pathum Thani 12000 Thailand',
        'phone': '66 2 501 2175',
        'website': 'https://www.patumrice.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'PRG Corporation Public Company Limited, together with its subsidiaries, engages in the processing and packaging of rice and related business in Thailand, the United States, Canada, Europe, the Asia Pacific, and internationally. It operates through two segments, Improving the Quality and Packaging of Milled Rice, and Food Center Business. The company offers hom mali, Japanese, white, jasmine, organic, riceberry, four hearty, and RD43 rice, as well as mixed rice with multigrain or dry vegetables, drinking water, and organic rice brain oil. It is also involved in the rental of warehouse and factory building; operation of a food center; distribution of rice; and provision of transportation service. The company formerly known as Patum Rice Mill and Granary Public Company Limited and changed its name to PRG Corporation Public Company Limited in May 2021. PRG Corporation Public Company Limited was founded in 1979 and is headquartered in Pathum Thani, Thailand. PRG Corporation Public Company Limited is a subsidiary of MBK Public Company Limited.'
    },
    'PRIME.BK': {
        'name': 'Prime Road Power Public Company Limited',
        'address': 'TP&T Tower Building 22nd Floor, 1 Soi Vibhavadi Rangsit 19 Chatuchak Subdistrict Bangkok 10900 Thailand',
        'phone': '66 2 105 8686',
        'website': 'https://www.primeroadpower.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Prime Road Power Public Company Limited, together with its subsidiaries, engages in the generation and distribution of electricity from solar energy in Thailand and internationally. The company has a total installed capacity of 294.7 megawatts in Thailand, Japan, Taiwan, and Cambodia. It serves industrial and business sectors, household businesses, government agencies, exports, and others. Prime Road Power Public Company Limited was incorporated in 2003 and is based in Bangkok, Thailand.'
    },
    'PRIN.BK': {
        'name': 'Prinsiri Public Company Limited',
        'address': '246, Watcharaphon Road Tha Raeng Bang Khen Bangkok 10230 Thailand',
        'phone': '66 2 022 8988',
        'website': 'http://www.prinsiri.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Prinsiri Public Company Limited, together with its subsidiaries, engages in the development, lease, and sale of real estate properties. The companys properties include townhomes, single houses, and condominiums. It also provides construction distributor and contractor services, as well as food service in restaurants and food shops. In addition, the company engages in the generation and distribution of electricity from solar cells and alternative energy. Prinsiri Public Company Limited was incorporated in 2004 and is headquartered in Bangkok, Thailand.'
    },
    'PRINC.BK': {
        'name': 'Principal Capital Public Company Limited',
        'address': 'Bangkok Business Center Building 23rd Floor No.29, Sukhumvit 63 road Klongton Nua, Wattana Bangkok 10110 Thailand',
        'phone': '66 2 714 2171',
        'website': 'http://www.principalcapital.co.th',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Principal Capital Public Company Limited operates and manages private hospitals in Thailand. The company also engages in operating hotels and serviced apartments; office building rental; and property development and rental activities. In addition, it is involved in the provision of office building management services. The company was formerly known as Metro Star Property Public Company Limited and changed its name to Principal Capital Public Company Limited in August 2013. Principal Capital Public Company Limited was incorporated in 2000 and is based in Bangkok, Thailand.'
    },
    'PRM.BK': {
        'name': 'Prima Marine Public Company Limited',
        'address': '80 Soi Bangna-Trad 30 Debaratna Road Bangna Tai Sub-District Bangna District Bangkok 10260 Thailand',
        'phone': '66 2 016 0190',
        'website': 'http://www.primamarine.co.th',
        'sector': 'Energy',
        'industry': 'Oil & Gas Midstream',
        'description': 'Prima Marine Public Company Limited operates marine transport business in Thailand and Singapore. The company offers transportation and storage of crude oil, petroleum products, semi-petroleum products, and liquefied petroleum gas. It also engages in business of service provision for supporting exploration and production of offshore petroleum products by sending staff and exploration equipment from a place to another place, and accommodation work barges. In addition, the company provides ship management, ship agent, recruitment, and transportation services for crews. Prima Marine Public Company Limited was founded in 1987 and is headquartered in Bangkok, Thailand. Prima Marine Public Company Limited is a subsidiary of Nathalin Co., Ltd.'
    },
    'PRO.BK': {
        'name': 'Professional Waste Technology (1999) Public Company Limited (Listed company which has possibility to be delisted)',
        'address': '1184/38-39 Soi Phahonyothin 32, Phahonyothin Rd., Chadrakasem Subdistrict, Chatuchak District Bangkok 10900',
        'phone': '66 2 924 9480',
        'website': 'http://www.prowaste.co.th',
        'sector': 'Industrials',
        'industry': 'Waste Management',
        'description': 'The company provides full service in elimination industrial waste both hazardous waste and non-hazardous waste. The company has its industrial waste treatment center in Sa Kaew Province where the waste has been directly transported from its client factory for professional treatment with concept of safety and correctness and concerning the environmental protection of the nation.'
    },
    'PROSPECT.BK': {
        'name': 'Prospect Logistics and Industrial Freehold and Leasehold Real Estate Investment Trust',
        'address': 'No. 345, 345 Surawong Building 7th Floor Surawong Road Suriyawong, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 235 4559',
        'website': 'http://www.prospectreit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Diversified',
        'description': 'The trust invests in the sub-leasehold rights of parts of land with warehouses and factories in the Bangkok Free Trade Zone.'
    },
    'PRTR.BK': {
        'name': 'Prtr Group Public Company Limited',
        'address': '2034/82 Ital – Thai Tower 18th Floor New Petchburi Road Bangkapi, Huaykwang Bangkok 10310 Thailand',
        'phone': '66 2 716 0000',
        'website': 'https://www.prtr.com/',
        'sector': 'Industrials',
        'industry': 'Staffing & Employment Services',
        'description': 'PRTR Group Public Company Limited provides human resource services in Thailand and internationally. The company offers recruitment services, such as eastern seaboard recruitment, executive recruitment, mass recruitment, database recruitment, campus recruitment, and Japanese recruitment; recruitment services in the areas of banking and financial recruitment, IT recruitment, and manufacturing recruitment; and HR services, including outsourcing, payroll, employee background check, and training and development services. It also operates an online job search platform; and seminar services. The company was incorporated in 1993 and is based in Bangkok, Thailand.'
    }
    ,

    # 421-440
    'PSH.BK': {
        'name': 'Pruksa Holding Public Company Limited',
        'address': '1177, Pearl Bangkok Building 24th Floor, Phaholyothin Road Phayathai District Bangkok 10400 Thailand',
        'phone': '66 2 080 1739',
        'website': 'http://www.psh.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Pruksa Holding Public Company Limited, through its subsidiaries, develops and sells residential real estate properties in Thailand. The company develops townhouses, single-detached houses, and condominiums. It also provides management, home decoration, and construction services; and operates hospitals and clinics. Pruksa Holding Public Company Limited was founded in 1993 and is headquartered in Bangkok, Thailand.'
    },
    'PSL.BK': {
        'name': 'Precious Shipping Public Company Limited',
        'address': 'No. 8 North Sathorn Road G, 7th, 8th, and 9th Floors Silom Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 696 8800',
        'website': 'http://www.preciousshipping.com',
        'sector': 'Industrials',
        'industry': 'Marine Shipping',
        'description': 'Precious Shipping Public Company Limited owns and operates dry bulk ships on a tramp-shipping basis worldwide. It is involved in the chartering and owning of ships, as well as in marine transportation. The companys cargoes primarily handle cement, agricultural products, steel, fertilizers, ores and concentrates, coal, logs, and other items. As of December 31, 2022, it owned and operated 38 dry bulk ships, including 9 Supramax, 8 Ultramax, and 21 Handysize, including 4 cement carriers with a total capacity of 1,657,579 deadweight tons. Precious Shipping Public Company Limited was founded in 1989 and is headquartered in Bangkok, Thailand.'
    },
    'PT.BK': {
        'name': 'Premier Technology Public Company Limited',
        'address': 'ONE Premier Corporate Park Soi Premier 2 Srinakarin Road Kwang Nongbon, Khet Prawet Bangkok 10250 Thailand',
        'phone': '66 2 301 1550',
        'website': 'http://www.premier-technology.co.th',
        'sector': 'Technology',
        'industry': 'Information Technology Services',
        'description': 'Premier Technology Public Company Limited, an investment holding company, provides services related to information technology systems in Thailand. The company offers hardware and software products, which include enterprise IT infrastructure and professional multimedia products, system and data management systems, and application software. In addition, it provides a range of services, including data centers and office continuity, maintenance, implementation, training and consulting, IT managed, Software as a Service, and other professional services; and space rental services. The company was formerly known as Premier Engineering and Technology Public Company Limited and changed its name to Premier Technology Public Company Limited in October 2006. Premier Technology Public Company Limited was founded in 1973 and is headquartered in Bangkok, Thailand.'
    },
    'PTECH.BK': {
        'name': 'Plus Tech Innovation Public Company Limited',
        'address': '41/1 Moo.10, Soi Wat Suan Som Poochao-Saming Prai Road Samrongtai Phrapradaeng Samut Prakan 10130 Thailand',
        'phone': '66 2 754 2650',
        'website': 'http://www.plustech.co.th',
        'sector': 'Industrials',
        'industry': 'Specialty Business Services',
        'description': 'Plus Tech Innovation Public Company Limited, together with its subsidiaries, engages in the manufacture and sale of plastic cards and vending machines in Thailand, rest of Asia, and internationally. The company offers plastic cards, including EMV, smart, near field communication business, top up, member, and specialty cards; and fingerprint card and dynamic card verification value, as well as packing and delivery, and inventory management services. It also provides card personalization services; and operates other security documents. The company was formerly known as TBSP Public Company Limited and changed its name to Plus Tech Innovation Public Company Limited. The company was incorporated in 1978 and is based in Samut Prakan, Thailand. Plus Tech Innovation Public Company Limited is a subsidiary of Sabuy Technology Public Company Limited.'
    },
    'PTG.BK': {
        'name': 'PTG Energy Public Company Limited',
        'address': '90, CW Tower A Building 33rd Floor Ratchadaphisek Road Huay Kwang Bangkok 10310 Thailand',
        'phone': '66 2 168 3377',
        'website': 'http://www.ptgenergy.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Specialty Retail',
        'description': 'PTG Energy Public Company Limited trades in petroleum products, gas products, and supplies and equipment for oil service stations, consumable products, and transportation in Thailand. It also engages in food and beverages business; operates convenience stores under the PT Mart and Max Mart name; coffee shops under the Punthai Coffee and Coffee World name; ice-cream shops under the Cream & Fudge name; restaurants under the Thai Chef express; and sandwich shop under the New York 5th Av. Deli name. In addition, it is involved in trading of petroleum, LPG, cosmetics, beauty products, and cooking gas; and production and trading of renewable energy. Further, the company provides service stations, car service center, membership management services, construction services, and electronic money and electronic card services. The company was formerly known as Paktai Chueplerng Company Limited. PTG Energy Public Company Limited was founded in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'PTL.BK': {
        'name': 'Polyplex (Thailand) Public Company Limited',
        'address': '75/26, Ocean Tower II 18th Floor Soi Sukhumvit 19, Sukhumvit Road Kwaeng North Klongtoey, Khet Wattana Bangkok 10110 Thailand',
        'phone': '66 2 665 2706',
        'website': 'http://www.polyplexthailand.com',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'Polyplex (Thailand) Public Company Limited, together with its subsidiaries, manufactures and distributes polyester films and chips, metalized films, extrusion coated films, cast polypropylene films, silicone coated films, and PET resins in Thailand and internationally. The company offers Sarafil range of plastic films, such as BOPET, bi-oriented polypropylene, cast polypropylene, blown polypropylene, and sustainable films for use in packaging, electrical, industrial, pressure sensitive, and other applications. It also provides Saracote range of silicone coated films for use in labels, tapes, roofing shingles, and peel and stick underlayments. In addition, the company offers Saralam range of extrusion coated film products comprising reflective insulation films; decorative lamination films; thin and thick gauge polyester thermal lamination films; and polypropylene, polyester, nylon, and UV polyester thermal lamination films for use in book covers, identity cards, carton lamination, wide format commercial films, etc. Further, it manufactures and distributes recycled plastic products. The company was incorporated in 2002 and is headquartered in Bangkok, Thailand.'
    },
    'PTT.BK': {
        'name': 'PTT Public Company Limited',
        'address': '555 Vibhavadi-Rangsit Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 537 2000',
        'website': 'http://www.pttplc.com',
        'sector': 'Energy',
        'industry': 'Oil & Gas Integrated',
        'description': 'PTT Public Company Limited, together with its subsidiaries, operates as a petroleum and petrochemical company in Thailand, other Asian countries, Europe, the United States, and internationally. It operates through Upstream Petroleum and Natural Gas Business Group, Downstream Petroleum Business Group, and New Business and Infrastructure Group. The company is involved in the exploration and production of petroleum; and natural gas procurement, pipeline transmission, distribution, and separation activities. In addition, it engages in the exploration, production, and distribution of coal; and marketing of petroleum products and lube oil through an operating system of procurement, storage, and distribution of products, as well as the retail business at service stations. Further, the company imports and exports petroleum and petrochemical products, as well as other related products; produces and distributes electricity, steam, and water for industrial purpose; and offers project management, human resource support, petroleum related technology, consultant management, technical consultant for electricity businesses, petrol station and convenience store management, factory maintenance and engineering, oil and gas, safety and environmental, and business services, as well as services for the storage and handling of liquid chemicals. Additionally, it invests in liquefied natural gas business; produces and distributes chilled water/constructs and installs electricity generating systems; develops electricity power production projects; develops, markets, and distributes polymers products, by products, and other polymers-related products; develops real estate properties; operates vocational schools; and manufactures and distributes biochemical products, paraxylene, and industrial coatings and additives, as well as engages in the transportation, warehouse, and bagging packing management of polyethylene. The company was founded in 1978 and is headquartered in Bangkok, Thailand.'
    },
    'PTTEP.BK': {
        'name': 'PTT Exploration and Production Public Company Limited',
        'address': '555/1 Energy Complex Building A 6th and 19th–36th Floors Vibhavadi-Rangsit Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 537 4000',
        'website': 'http://www.pttep.com',
        'sector': 'Energy',
        'industry': 'Oil & Gas E&P',
        'description': 'PTT Exploration and Production Public Company Limited, together with its subsidiaries, engages in the exploration and production of petroleum in Thailand and internationally. It is also involved in the gas pipeline transportation business; investment funding; and the provision of petroleum-related technology, human resource support, treasury center, technology, and solar power businesses, as well as renewable energy and related activities. The company was founded in 1985 and is headquartered in Bangkok, Thailand. PTT Exploration and Production Public Company Limited is a subsidiary of PTT Public Company Limited.'
    },
    'PTTGC.BK': {
        'name': 'PTT Global Chemical Public Company Limited',
        'address': '555/1 Energy Complex, Building A 14th-18th Floor Vibhavadi-Rangsit Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 265 8400',
        'website': 'http://www.pttgcgroup.com',
        'sector': 'Basic Materials',
        'industry': 'Chemicals',
        'description': 'PTT Global Chemical Public Company Limited produces and distributes ethylene, propylene, polyethylene plastic pellets, and biochemical products in Thailand, the Peoples Republic of China, Vietnam, Singapore, India, Malaysia, Indonesia, Japan, the United States, and internationally. It operates through seven segments: Refinery, Aromatics, Olefins and Derivatives, Green Chemicals, Performance Materials and Chemicals, Service and Others, and Investments in Other Joint Ventures and Associates. The company offers refined products, including liquefied petroleum gas (LPG), light naphtha, reformate, jet fuel, diesel, and fuel oil. It also provides aromatics products, such as benzene, toluene, paraxylene, cyclohexane, and orthoxylene; olefins comprising ethylene and propylene, mixed c4, tail gas, cracker bottom, hydrogen, and pyrolysis gasoline; and polymers consisting of HDPE, LDPE, LLDPE, PP, PTA, PET, PS, and rotomolding compounds. In addition, the company offers EO-based performance products, including ethylene glycol and ethanolamine; green chemicals, such as methyl ester, glycerin, fatty acid and alcohol, ethoxylate, oleochemicals, and bioplastic; and phenol, bisphenol A, and acetone. Further, it provides hexamethylene diisocyanate and derivatives, as well as acrylonitrile and methyl methacrylate. Additionally, the company operates production support facilities, such as jetty and buffer tank farm services for liquid chemical, and oil and gas; manufactures and distributes industrial coating resins, additives, petrochemical, health, nutrition, and recycled plastic products. It also offers factory maintenance and engineering services; real estate development services; safety and environmental services; service for the storage and handling of liquid chemicals, oil, and gas; and research and development of bio-based chemicals. In addition, the company produces and distributes electricity, water, steam, and other utilities. The company is headquartered in Bangkok, Thailand.'
    },
    'PYLON.BK': {
        'name': 'Pylon Public Company Limited',
        'address': '252 SPE Tower Building 14th floor Phahonyothin Road Samsen Nai Subdistrict,Phayathai Distric Bangkok 10400 Thailand',
        'phone': '66 2 615 1259',
        'website': 'http://www.pylon.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'Pylon Public Company Limited, together with its subsidiaries, provides construction services in Thailand. It offers foundation services, including bored piles, ground improvement, diaphragm walls/ barrette pile, and other construction services. The company was incorporated in 2002 and is headquartered in Bangkok, Thailand.'
    },
    'Q-CON.BK': {
        'name': 'Quality Construction Products Public Company Limited',
        'address': 'Bang Pa-In Industrial Estate 144 Moo 16, Udomsorayuth Road Tambol Bangkrasan Amphur Bang pa-in Phra Nakhon Si Ayutthaya 13160 Thailand',
        'phone': '66 35 259 131',
        'website': 'https://www.qcon.co.th',
        'sector': 'Industrials',
        'industry': 'Building Products & Equipment',
        'description': 'Quality Construction Products Public Company Limited, together with its subsidiary, produces and distributes autoclaved aerated concrete blocks, reinforced wall panels, floor panels, and lintels for construction uses in Thailand and internationally. It also offers readymade counters, plastering mortar, bed adhesive mortar, aerated stair system, and tools and accessories. The company was founded in 1994 and is based in Phra Nakhon Si Ayutthaya, Thailand. Quality Construction Products Public Company Limited is a subsidiary of SCG Building Materials Company Limited.'
    },
    'QH.BK': {
        'name': 'Quality Houses Public Company Limited',
        'address': 'Q. House Lumpini Building 6th and 7th Floor No. 1 South Sathorn Road Thungmahamek, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 677 7000',
        'website': 'http://www.qh.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Diversified',
        'description': 'Quality Houses Public Company Limited, together with its subsidiaries, engages in the property development business in Thailand. It operates in four segments: Real Estate Business, Hotel Business, Rental Business, and Others. The company develops and sells land and houses, and condominium units; rents residential, hotels, and office buildings; and services residential buildings, as well as manages public utilities and real estate business of landowners. It also engages in hotel operations; lease of land; management of buildings; and manufacture and distribution of precast concrete. The company was incorporated in 1983 and is headquartered in Bangkok, Thailand.'
    },
    'QHHR.BK': {
        'name': 'Quality Houses Hotel and Residence Freehold and Leasehold Property Fund',
        'address': '11 Q. House Sathorn Building 14th Floor South Sathorn Road Thungmahamek, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 286 3484',
        'website': 'https://www.qhhr-pf.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Hotel & Motel',
        'description': 'Quality Houses Hotel and Residence Freehold and Leasehold Property Fund specializes in real estate investments. The fund seeks to make house, hotel, and residence property investments.'
    },
    'QHOP.BK': {
        'name': 'Quality Hospitality Leasehold Property Fund',
        'address': '23A, 25th floor - Asia Center Building 173/27-30, 32-33 South Sathon Roa Thungmahamek, Sathon Bangkok 10120 Thailand',
        'phone': '66 2 786 2000',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Specialty',
        'description': 'The Fund has invested in leasehold right of land and building in Boulevard Hotel ฺBangkok Project and purchasing furniture and fixtures necessary for the hotel project.'
    },
    'QHPF.BK': {
        'name': 'Quality Houses Leasehold Property Fund',
        'address': 'Q. House Sathon Building 14th Floor 11 South Sathon Road Tungmahamek, Sathon Bangkok 10120 Thailand',
        'phone': '66 2 286 3484',
        'website': 'https://www.qhpf.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Office',
        'description': 'The Fund has invested in leasehold rights on Q. House Lumpini, Wave Place and Q. House Ploenchit.'
    },
    'QTC.BK': {
        'name': 'QTC Energy Public Company Limited',
        'address': '2/2 soi Krungthep Kritha 8(5) krungthep Kritha Road Huamark Bangkapi Bangkok 10240 Thailand',
        'phone': '66 2 379 3089',
        'website': 'http://www.qtc-energy.com',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'QTC Energy Public Company Limited manufactures and sells electric transformers in Thailand and internationally. It also provides various services, such as scheduled checks and maintenance, transformer repairs and maintenance, transformer oil fill, transformer rental services, etc. In addition, the company invests in the renewable energy business; and produces and distributes electricity from solar energy. It offers its products under the QTC name, as well as under customer specific brands. The company was formerly known as QTC Transformers Co., Ltd. and changed its name to QTC Energy Public Company Limited in August 2010. QTC Energy Public Company Limited was founded in 1996 and is based in Bangkok, Thailand.'
    },
    'RABBIT.BK': {
        'name': 'Rabbit Holdings Public Company Limited',
        'address': 'No. 21, TST Tower 20th Floor Soi Choei Phuang Vibhavadi-Rangsit Road,Chomphon, Chatuch Bangkok 10900 Thailand',
        'phone': '66 2 273 8838',
        'website': 'http://www.rabbitholdings.co.th',
        'sector': 'Technology',
        'industry': 'Software—Infrastructure',
        'description': 'Rabbit Holdings Public Company Limited engages in the financial services business. The company was formerly known as U City Public Company Limited and changed its name to Rabbit Holdings Public Company Limited in December 2022. Rabbit Holdings Public Company Limited was incorporated in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'RAM.BK': {
        'name': 'Ramkhamhaeng Hospital Public Company Limited',
        'address': '436 Ramkhamhaeng Road Kwaeng Huamark Khet Bangkapi Bangkok 10240 Thailand',
        'phone': '66 2 743 9999',
        'website': 'https://www.ram-hosp.co.th',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Ramkhamhaeng Hospital Public Company Limited, together with its subsidiaries, operates a private hospital that provides medical services in Thailand. It operates in two segments, Hospital and Others. The company also sells medical equipment and instruments. In addition, it is involved in the property development; training; and software businesses. The company was founded in 1976 and is based in Bangkok, Thailand.'
    },
    'RATCH.BK': {
        'name': 'Ratch Group Public Company Limited',
        'address': '72 Ngam Wong Wan Rd. Bang Khen Muang Nonthaburi 11000 Thailand',
        'phone': '66 2 794 9999',
        'website': 'http://www.ratch.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Regulated Electric',
        'description': 'Ratch Group Public Company Limited, through its subsidiaries, engages in generation and sale of electricity in Thailand, Australia, and internationally. The company operates through four segments: Domestic Electricity Generating, Renewable Energy, International Power Projects, and Related Business and Infrastructure segments. It also generates electricity through natural gas, coal, and fuel oil, as well as solar power, wind power, and biomass renewable projects. In addition, the company offers power plant operation services, as well as invests in the power energy business. Ratch Group Public Company Limited was incorporated in 2000 and is based in Nonthaburi, Thailand.'
    },
    'RBF.BK': {
        'name': 'R&B Food Supply Public Company Limited',
        'address': '77 Soi Pho kaeo 3 Klongchan Bangkapi Bangkok 10240 Thailand',
        'phone': '66 2 946 6812',
        'website': 'https://www.rbfoodsupply.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'R&B Food Supply Public Company Limited, together with its subsidiaries, manufactures and trades bread products, colors, fragrances, and chemicals that are used in food, beverage, and consumer product industries in Thailand. The company was founded in 1989 and is headquartered in Bangkok, Thailand.'
    }
    ,

    # 441-460
    'RCL.BK': {
        'name': 'Regional Container Lines Public Company Limited',
        'address': 'Panjanthani Tower Building 30th Floor 127/35 Ratchadapisek Road Chongnonsi, Yannawa Bangkok 10120 Thailand',
        'phone': '66 2 296 1096',
        'website': 'http://www.rclgroup.com',
        'sector': 'Industrials',
        'industry': 'Marine Shipping',
        'description': 'Regional Container Lines Public Company Limited, together with its subsidiaries, owns, operates, and manages ships in North East Asia, South East Asia, Indian Sub-Continent, and the Middle East. The company owns and operates 49 container vessels. It also provides logistics, cargo consolidation and operation, shipping agency, and transportation and cargo handling services. In addition, the company operates terminals; and rents warehouse facilities. Regional Container Lines Public Company Limited was founded in 1979 and is headquartered in Bangkok, Thailand.'
    },
    'RICHY.BK': {
        'name': 'Richy Place 2002 Public Company Limited',
        'address': '667/15 Attapawan Building 7th Floor Charansanitwong Road, Arun Amarin Bangkok Noi Bangkok 10700 Thailand',
        'phone': '66 2 886 1816',
        'website': 'http://www.richy.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Richy Place 2002 Public Company Limited engages in the real estate development business in Thailand. It develops and sells single-family houses, townhouses, townhomes, condominiums, and other properties. The company was incorporated in 2002 and is based in Bangkok, Thailand.'
    },
    'RJH.BK': {
        'name': 'Rajthanee Hospital Public Company Limited',
        'address': 'No. 111 Moo 3 Rojana Road Khlong Suan Phlu Sub-district Phra Nakhon Si Ayutthaya District Phra Nakhon Si Ayutthaya 13000 Thailand',
        'phone': '66 3 533 5555-71',
        'website': 'http://www.rajthanee.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Rajthanee Hospital Public Company Limited, together with its subsidiaries, offers healthcare services in Thailand. The company operates medical centers, including trauma emergency and neurosurgery, non-trauma emergency, cardiology, minimally invasive surgery, surgery, orthopedic, wellness and occupational health, radiology, MRI, ophthalmology, hemodialysis, sleep lab, dental, physical therapy, and laboratory centers; and medical clinics, such as hematology, nephrology, arthritis and rheumatic, dermatology, allergy and immunology, oncology and chemotherapy, stroke, endocrinology, pulmonary, gastrointestinal and liver diseases, pediatrics, maternal and fetal medicine, obstetrics and gynecology, otolaryngology, psychiatric, and screening clinic for respiratory diseases. Rajthanee Hospital Public Company Limited was incorporated in 1990 and is headquartered in Phra Nakhon Si Ayutthaya, Thailand.'
    },
    'RML.BK': {
        'name': 'Raimon Land Public Company Limited',
        'address': '3 Rajanakarn Building 19th Floor South Sathorn Road Yannawa, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 029 1889',
        'website': 'http://www.raimonland.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Raimon Land Public Company Limited, together with its subsidiaries, engages in the property development activities in Thailand. It develops and sells land, houses, and residential condominiums. The company is also involved in the rental of office buildings, residential condominiums, and community malls; and hospitality, and food and beverage businesses. In addition, it offers property rental, lease, and resale agency services. Raimon Land Public Company Limited was founded in 1987 and is headquartered in Bangkok, Thailand.'
    },
    'ROCK.BK': {
        'name': 'Rockworth Public Company Limited',
        'address': '294-300 Asoke-Dindaeng Road Huaykwang Bangkok 10320 Thailand',
        'phone': '66 2 246 8888',
        'website': 'http://www.rockworth.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Furnishings, Fixtures & Appliances',
        'description': 'Rockworth Public Company Limited manufactures and distributes office furniture in Thailand, rest of Asia, and internationally. It offers smart office solutions, such as workspace booking and analytics, smart locker, and visitor management systems; architectural and acoustic solutions, including wall systems, modular carpets, and acoustic panels; and office seating products comprising chairs, modular seating lounges, benches and ottomans, stools, sofas, and beam seating products. The company provides desk systems and tables; room elements and space division products that include pods, screen and space dividers, and panel and reception systems; pedestals and personal storage systems, shelves and cabinets, and lockers; and collaborative tools, desk accessories and décor products, as well as technology support, power access, and lighting solutions. Rockworth Public Company Limited was founded in 1972 and is headquartered in Bangkok, Thailand.'
    },
    'ROH.BK': {
        'name': 'Royal Orchid Hotel (Thailand) Public Company Limited',
        'address': '2 Captain Bush Lane Charoen Krung Road Kwaeng Bangrak Khet Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 266 0123',
        'website': 'http://www.royalorchidsheraton.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'Royal Orchid Hotel (Thailand) Public Company Limited operates a hotel in Thailand. It offers various types of rooms, food and beverages, and other ancillary services. The company was founded in 1978 and is headquartered in Bangkok, Thailand. Royal Orchid Hotel (Thailand) Public Company Limited is a subsidiary of Grande Asset Hotels and Property Public Company Limited.'
    },
    'ROJNA.BK': {
        'name': 'Rojana Industrial Park Public Company Limited',
        'address': '2034/115, Ital Thai Tower 26th Floor New Petchaburi Road Bang Kapi, Huai Khwang Bangkok 10310 Thailand',
        'phone': '66 2 716 1750',
        'website': 'http://www.rojana.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Independent Power Producers',
        'description': 'Rojana Industrial Park Public Company Limited, together with its subsidiaries, engages in the manufacture and sale of electricity from solar cell system in Thailand. The company operates through Real Estate Development and Related Service, Electricity Generating, Production and Distribution Industrial Water, Rental Services, and Medical Services segments. It also develops industrial estates in Ayutthaya, Rayong, and Chonburi Provinces; and provides water and wastewater treatment services. In addition, the company provides medical services; spices, aromatic, and drugs and pharmaceutical crops; consulting and advising services; and produces products from plants and animals for diseases treatment. The company was founded in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'RPC.BK': {
        'name': 'RPCG Public Company Limited',
        'address': '86/2 Sammakorn Place Ramkhamhaeng Road Saphan Sung Bangkok 10240 Thailand',
        'phone': '66 2 372 3600',
        'website': 'http://www.rpcthai.com',
        'sector': 'Energy',
        'industry': 'Oil & Gas Refining & Marketing',
        'description': 'RPCG Public Company Limited, through its subsidiaries, engages in the energy and real estate businesses in Thailand. The company engages in wholesale and retailing of diesel oil, fuel oil, and petrochemical products through a network of gas stations; distribution and maintenance of gas station equipment; rental of oil depot; and port business. It also develops, sells, and rents real estate properties; and provides construction services. The company was formerly known as Rayong Purifier Public Company Limited and changed its name to RPCG Public Company Limited in January 2014. RPCG Public Company Limited was founded in 1995 and is headquartered in Bangkok, Thailand.'
    },
    'RPH.BK': {
        'name': 'Ratchaphruek Hospital Public Company Limited',
        'address': '456, Moo 14, Mittraphap Road Amphur Mueng Khon Kaen 40000 Thailand',
        'phone': '66 4 333 3555',
        'website': 'http://www.rph.co.th',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Ratchaphruek Hospital Public Company Limited engages in the hospital business under the Ratchaphruek Hospital name in Thailand. The company provides medical services in the field of internal medicine, such as dermatology, neurology, hematology, rheumatology, gastroenterology, nephrology, and diabetes and endocrine; general, urological, and colorectal surgeries; and pediatrics, orthopedics, otorhinolaryngology, ophthalmology, obstetrics and gynecology, check-up, dentistry, anesthesiology, emergency medical, stroke, breast, hearing and balance, rehabilitation, and diagnostic radiology. It also sells medicines and medical supplies. The company was formerly known as Sithan Karnpat Company Limited and changed its name to Ratchaphruek Hospital Public Company Limited in September 2016. Ratchaphruek Hospital Public Company Limited was incorporated in 1993 and is based in Khon Kaen, Thailand.'
    },
    'RS.BK': {
        'name': 'RS Public Company Limited',
        'address': '27 RS Group Building Tower A Prasert-Manukitch Road Sena Nikhom, Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 037 8888',
        'website': 'http://www.rs.co.th',
        'sector': 'Communication Services',
        'industry': 'Entertainment',
        'description': 'RS Public Company Limited, together with its subsidiaries, engages in the commerce, media, and music and other businesses in Thailand. It operates Channel 8, a digital television; RS Mall Channel, an shopping channel; radio frequency system of F.M. 93.0 MHz under the COOLfahrenheit brand, through online channel at www.COOLISM.net and COOLISM application on smartphones; COOLive, which organizes events and concerts; and COOLanything, a commerce business platform. Its music business engages in the content creation, marketing, artist management, and song content management through online media, such as streaming and social media, as well as offline media comprising television, events, and showbiz; and creates music under the RoseSound, Kamikaze, and RSiam labels. In addition, the company offers health, beauty and fashion, home, and pet products, as well as electrical and home appliances. Further, it provides dietary supplements under the Vitanature+ brand and food supplements under the S.O.M. brand. The company was formerly known as RS Promotion Public Co. Ltd. and changed its name to RS Public Company Limited in December 2005. RS Public Company Limited was founded in 1976 and is headquartered in Bangkok, Thailand.'
    },
    'RSP.BK': {
        'name': 'Rich Sport Public Company Limited',
        'address': '116/20 Na Ranong Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 249 8709',
        'website': 'http://www.richsport.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Footwear & Accessories',
        'description': 'Rich Sport Public Company Limited, together with its subsidiaries, engages in the distribution of fashion and lifestyle products in Thailand and internationally. Its products include footwear, apparels, and accessories such as bags, caps, and socks. The company offers its products primarily under the Converse, havaianas, Cole Haan, Barrel, ECCO, and GEOX brands. Rich Sport Public Company Limited was founded in 2003 and is based in Bangkok, Thailand.'
    },
    'RT.BK': {
        'name': 'Right Tunnelling Public Company Limited',
        'address': '292 Moo 4 Bangna - Trad Rd. (km 26) Bangbor Bang Bo District Samut Prakan 10560 Thailand',
        'phone': '66 2 313 4848',
        'website': 'https://www.rtco.co.th/',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'Right Tunnelling Public Company Limited engages in the provision of construction services, open and underground rock excavation, dam excavation, and other construction works in Thailand, Myanmar, the Lao Peoples Democratic Republic, and Cambodia. It is also involved in mineral exploration activities. The company was founded in 2000 and is based in Samut Prakan, Thailand.'
    },
    'S.BK': {
        'name': 'Singha Estate Public Company Limited',
        'address': '123 Suntowers Building B 22nd Floor Vibhavadi-Rangsit Road Chom Phon, Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 050 5555',
        'website': 'http://www.singhaestate.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Singha Estate Public Company Limited, together with its subsidiaries, develops and invests in real estate properties for rental and sale in Thailand and internationally. The company develops single detached houses, townhomes, home offices, and condominium; and owns commercial buildings, hospitality, and infrastructure. It also engages in the provision of hotel, hotel management, and hospitality services; and construction and project management services, as well as property development and real estate. The company was formerly known as Rasa Property Development Public Company Limited and changed its name to Singha Estate Public Company Limited in September 2014. Singha Estate Public Company Limited was founded in 1995 and is headquartered in Bangkok, Thailand.'
    },
    'S&J.BK': {
        'name': 'S & J International Enterprises Public Company Limited',
        'address': '2 Naradhiwas Rajanagarindra Road Tungwatdon Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 676 2727',
        'website': 'http://www.snjinter.com',
        'sector': 'Consumer Defensive',
        'industry': 'Household & Personal Products',
        'description': 'S & J International Enterprises Public Company Limited, together with its subsidiaries, manufactures and distributes cosmetic products in Thailand and internationally. The company operates through three segments: Cosmetics, Packaging, and Others. It offers color cosmetic products; skin, body, and hair care products; and fragrances and toiletries. In addition, it is involved in the research and development of cosmetic formulations. S & J International Enterprises Public Company Limited was founded in 1980 and is headquartered in Bangkok, Thailand.'
    },
    'S11.BK': {
        'name': 'S 11 Group Public Company Limited',
        'address': '888, Soi. Chatuchot 10 Chatuchot Road Ao-Ngoen Sub-District Saimai District Bangkok 10220 Thailand',
        'phone': '66 2 022 8888',
        'website': 'http://www.sgroup.co.th',
        'sector': 'Industrials',
        'industry': 'Rental & Leasing Services',
        'description': 'S 11 Group Public Company Limited, through its subsidiary, MOD S Company Limited, engages in conducting loan services for hire purchase of motorcycles to individuals in Thailand. The company provides after-sales services, including renewal tax registration, insurance, and sign act services to customers. S 11 Group Public Company Limited was incorporated in 2011 and is headquartered in Bangkok, Thailand.'
    },
    'SA.BK': {
        'name': 'Siamese Asset Public Company Limited',
        'address': '1077/48 Phahon Yothin Road Phaya Thai Subdistrict Phaya Thai District Bangkok 10400 Thailand',
        'phone': '66 2 617 1555',
        'website': 'http://www.siameseasset.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Siamese Asset Public Company Limited operates real estate development business in Thailand. The company develops residential real estate for sale, which include condominiums, houses, townhomes and home offices, and offer juristic person management service. It also engages in hotel business and commercial space for rent, food and beverages business, spa and wellness business, technology business, and finance and investment. The company was founded in 2010 and is headquartered in Bangkok, Thailand.'
    },
    'SABINA.BK': {
        'name': 'Sabina Public Company Limited',
        'address': '177, Moo 8 Wang Kai Tuen Sub-District Hankha 17130 Thailand',
        'phone': '66 2 422 9400',
        'website': 'http://www.sabina.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Apparel Manufacturing',
        'description': 'Sabina Public Company Limited, together with its subsidiaries, manufactures and sells ladies lingerie in Thailand and internationally. It offers bras, panties, shapewear, sports and swimwear, and special bras and other products for children, teenagers, and adults under the BigC, Tesco Lotus, Doomm Series, Wireless bras, Modern V, Madmoiselle, Maggiemae, and Cris Collection brand names. The company was formerly known as J&D Apparel Public Company Limited and changed its name to Sabina Public Company Limited in May 2007. Sabina Public Company Limited was incorporated in 1995 and is headquartered in Hankha, Thailand.'
    },
    'SABUY.BK': {
        'name': 'Sabuy Technology Public Company Limited',
        'address': '230 Bang Khun Thian-Chai Thale Road Samae Dam Bang Khun Thian Bangkok 10150 Thailand',
        'phone': '66 2 451 5335',
        'website': 'http://www.sabuytechnology.com',
        'sector': 'Industrials',
        'industry': 'Business Equipment & Supplies',
        'description': 'Sabuy Technology Public Company Limited engages in the rendering of top-up service for prepaid phone and electronical receipt through top-up machines in Thailand. The company offers electronic payment services; food court management services; financial and loan brokerage services; transport and postal services; and trades food and beverages through vending machines, as well as manufactures plastic cards. Sabuy Technology Public Company Limited was founded in 2016 and is based in Bangkok, Thailand.'
    },
    'SAK.BK': {
        'name': 'Saksiam Leasing Public Company Limited',
        'address': '49/47 Jetsada Badin Road Tha It Sub-district Mueang Uttaradit District Uttaradit 53000 Thailand',
        'phone': '66 5 544 4495',
        'website': 'http://www.saksiam.com',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Saksiam Leasing Public Company Limited provides financial services in Thailand. It offers personal, nano finance, hire purchase, and non-life insurance loans, as well as other credit services. The company also sells drone equipment and agricultural drone. Saksiam Leasing Public Company Limited is incorporated in 1995 and is headquartered in Uttaradit, Thailand.'
    },
    'SAM.BK': {
        'name': 'Samchai Steel Industries Public Company Limited',
        'address': '75/14, 75/17, 85 Moo 5 Soi Wat Sopanaram Ekkachai Road, Tumbol Kokkham Amphur Muang Samut Sakhon 74000 Thailand',
        'phone': '66 3 483 3891',
        'website': 'http://www.samchaisteel.com',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'Samchai Steel Industries Public Company Limited manufactures and distributes steel pipes and tubes for the construction and furniture industries in Thailand and internationally. It provides structural steel pipes; galvanized steel pipes; round and deformed bars, wide flange, h-beam, I-beam, channels, angles, plates, checkered plates, and fittings. The company was formerly known as Samchai Holding Public Company and changed its name to Samchai Steel Industries Public Company Limited in December 2002. Samchai Steel Industries Public Company Limited was founded in 1997 and is headquartered in Samutsakorn, Thailand.'
    }
    ,

    # 461-480
    'SAMART.BK': {
        'name': 'Samart Corporation Public Company Limited',
        'address': '99/1 Moo 4, Software Park Building 35th Floor Chaengwattana Road Klong Gluar, Pak-Kred Nonthaburi 11120 Thailand',
        'phone': '66 2 502 6000',
        'website': 'http://www.samartcorp.com',
        'sector': 'Technology',
        'industry': 'Information Technology Services',
        'description': 'Samart Corporation Public Company Limited designs and installs telecommunications systems, and sells telecommunications equipment in Thailand, Cambodia, and internationally. It operates in four segments: ICT Solution and Service; Digital; Utilities and Transportations; and Technology Related Services. The ICT Solution and Service segment offers solutions and services in information and communication technology and digital solutions, including network solutions, enhanced technology in ICT, and business application ranging from consulting, system design, installation and implementation, operation, and maintenance as total solutions and services for clients in government and private sectors. The Digital segment provides integrated services in digital network, solution, and content. The Utilities and Transportations segment provides air traffic control services; supplies electricity in Cambodia; and offers design and installation services of electrical power transmission systems. The Technology Related Services segment manufactures and distributes television, and radio antennas and satellite dishes; and distributes, installs, and maintains communication and security systems. The company also provides broadcast network and system integrator services; produce metal work, metal sheet products, and related products; Internet Services; leases freehold land; and invests in public utilities in the Indochina region. In addition, it provides audio and video conference, wire and wireless communication system; and trading of radiation measurement equipment, radiation measurement service, and radiation project management services. The company was founded in 1955 and is headquartered in Nonthaburi, Thailand.'
    },
    'SAMCO.BK': {
        'name': 'Sammakorn Public Company Limited',
        'address': '188, Spring Tower Building 21st Floor Thung Phaya Thai Phaya Thai, Ratchathewi Bangkok 10400 Thailand',
        'phone': '66 2 106 8300',
        'website': 'http://www.sammakorn.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate Services',
        'description': 'Sammakorn Public Company Limited, together with its subsidiaries, engages in the real estate development business in Thailand. The company operates through Real Estate Development, Rental, Restaurant and Bakery, and Service segments. It also develops land into community malls; and offers real estate management and other related services. In addition, the company engages in the food and beverage restaurant business. The company was founded in 1970 and is headquartered in Bangkok, Thailand.'
    },
    'SAMTEL.BK': {
        'name': 'Samart Telcoms Public Company Limited',
        'address': 'SOFTWARE PARK BUILDING FLOOR 29, 99/7 MOO 4, PAK KRET Nonthaburi 11120',
        'phone': '66 2 502 6000',
        'website': 'http://www.samtel.com',
        'sector': 'Communication Services',
        'industry': 'Telecom Services',
        'description': 'Samart Telcoms Public Company Limited engages in the integrated telecommunications, communication network, and information technology businesses in Thailand. It operates through three segments: Network Infrastructure Solutions, Enhanced Technology Solutions, and Business Application. The Network Infrastructure Solutions segment provides advanced solutions for telecommunications and data communication networks comprising consultation, survey, design, installation and implementation, and system management services, as well as professional maintenance services for wired and wireless networks, including core networks, access networks, and network equipment and end devices; and various communications services through high-speed networks and satellite communications. The Enhanced Technology Solutions segment offers solutions, such as consultation, engineering design and software development, installation, project management, management, and maintenance services for information technology systems consists of advanced systems customization. The Business Application segment provides advanced software application services for the corporate and public sector client operations. It is also involved in the design and installation of communication and network public rural telephone projects, telecommunications network, and enterprise resource planning (ERP) system and integrated ERP solution for government and public sectors; electronic payment systems; electronic data interchange; production of software packages; provision of software development and internet services; e-learning software development consultation; cyber security; communication equipment and computer distribution activities; and repair and maintenance of systems. The company was founded in 1986 and is based in Pathum Thani, Thailand. Samart Telcoms Public Company Limited is a subsidiary of Samart Corporation Public Company Limited.'
    },
    'SAPPE.BK': {
        'name': 'Sappe Public Company Limited',
        'address': '9/3 Serithai Road Kannayao Kannayao District Bangkok 10230 Thailand',
        'phone': '66 2 319 4949',
        'website': 'http://www.sappe.com',
        'sector': 'Consumer Defensive',
        'industry': 'Beverages—Non-Alcoholic',
        'description': 'Sappe Public Company Limited, together with its subsidiaries, manufactures and distributes healthy food and beverage products in Thailand, Indonesia, the Philippines, Korea, and internationally. The company operates in two segments, Health Drinking Products and Coconut Products. It offers fruit and non-fruit flavored juices under the Mogu Mogu brand name; candies under the KRUPENSRI brand name; jellies under the Gumi Gumi brand name; sparkling kombucha under the KEAF brand name; dietary supplement drink shots under the SAPPE x TAKABB brand name; tonic herbal drink under the Ruby Lady brand name; sugar free coffee under the MAXTIVE Coffee and Preaw Coffee brand name; fruit flavored vitamin water under the Blue brand; and beauty powder, jelly, drink under the Sappe brand name. The company also provides grilled fish snacks under the ZeaMax brand; fruit jelly snack mixed with carageenan and konjac under the Gumi Gumi Jelly brand; and fruit juice mixed with aloe vera in various flavors under the Sappe Aloe Vera brand. The company was formerly known as Sapanan General Food Company Limited and changed its name to Sappe Public Company Limited in September 2013. Sappe Public Company Limited was founded in 1973 and is headquartered in Bangkok, Thailand.'
    },
    'SAT.BK': {
        'name': 'Somboon Advance Technology Public Company Limited',
        'address': 'No. 129 Moo 2 KM. 15th Bangna-Trad Road Tambon Bangchalong Bang Phli 10540 Thailand',
        'phone': '66 2 080 8123',
        'website': 'http://www.satpcl.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Auto Parts',
        'description': 'Somboon Advance Technology Public Company Limited, together with its subsidiaries, engages in the manufacturing and distribution of motor vehicle parts for passenger cars, pickup trucks, trucks, and agricultural machinery in Thailand. It offers axle shafts, disc and drum brakes, leaf and coil springs, stabilizer bars, exhaust manifolds, inner shafts, flywheel, and camshafts. The company also provides case bevel and case front gears, holder front and rear products, cover and case front axle, manifold exhaust, case rear and brake products, and case hydraulic cylinders; and case unloader, roller 275, frame tension, gear case, guide crawler, roller guide, as y blade, knift guard, and v-pulley products. In addition, it rents and invests in real estate. The company serves original equipment manufacturers and replacement equipment manufacturers. Somboon Advance Technology Public Company Limited was founded in 1995 and is headquartered in Bang Phli, Thailand.'
    },
    'SAUCE.BK': {
        'name': 'Thaitheparos Public Company Limited',
        'address': '208 Moo 6 Taiban Road Taiban Sub-District Samut Prakan 10280 Thailand',
        'phone': '66 2 703 4444',
        'website': 'http://www.gmsauce.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Thaitheparos Public Company Limited manufactures and distributes sauces and condiments in Thailand and internationally. It offers seasoning food products under the Golden Mountain brand, including seasoning sauces, chilli sauces, distilled vinegar products, chilli and tomato sauces, ketchups, chicken, and oyster sauces, as well as soy sauces; chilli and oyster sauces under the E Zee brand; and Japanese soy sauce under the Kinzan Shoyu brand. The company was formerly known as Thai Theparos Food Products Public Company Limited and changed its name to Thaitheparos Public Company Limited in April 2011. Thaitheparos Public Company Limited was founded in 1954 and is headquartered in Samut Prakan Thailand.'
    },
    'SAWAD.BK': {
        'name': 'Srisawad Corporation Public Company Limited',
        'address': '99/392 Srisawad Building 4,6 Floor, Chaeng Watthana 10 Alley 3 Sub Alley, Chaeng Watthana Road Thungsonghong, Laksi Bangkok 10210 Thailand',
        'phone': '66 2 693 5555',
        'website': 'http://www.meebaanmeerod.com',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Srisawad Corporation Public Company Limited, together with its subsidiaries, provides finance services in Thailand. It offers hire-purchase and loan, and non-performing assets management services. The company also invests in other companies; and provides management and consulting services for retail credit systems in local and foreign countries, as well as credit sale in foreign countries. In addition, it provides digital personal loan services. The company was formerly known as Srisawad Power 1979 Public Company Limited and changed its name to Srisawad Corporation Public Company Limited in July 2017. Srisawad Corporation Public Company Limited was founded in 2008 and is based in Bangkok, Thailand.'
    },
    'SAWANG.BK': {
        'name': 'Sawang Export Public Company Limited',
        'address': '307-307/1-4, 56, 305 Surawongse Road Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 266 4422',
        'website': 'N/A',
        'sector': 'Consumer Cyclical',
        'industry': 'Luxury Goods',
        'description': 'Sawang Export Public Company Limited engages in the manufacture and distribution of jewelry products and precious stones in Thailand, German, Australia, the United States, and internationally. The company provides diamond, precious, semi-precious, CZ, and created stones; color stones, such as rubies, and natural blue and yellow sapphires, as well as synthetic stones; and gold and silver jewelry sets. It also exports its products. Sawang Export Public Company Limited was incorporated in 1993 and is based in Bangkok, Thailand.'
    },
    'SC.BK': {
        'name': 'SC Asset Corporation Public Company Limited',
        'address': '1010 Vibhavadi Rangsit Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 949 2000',
        'website': 'http://www.scasset.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'SC Asset Corporation Public Company Limited, together with its subsidiaries, operates as a real estate development company in Thailand. It operates through Real Estates sales; Rental and Rendering of Services; and Consulting and Management Service segments. The company develops and sells single detached houses, townhomes, and condominiums, as well as home offices; and rents office and technical buildings. It also provides consulting and management services. The company was incorporated in 1989 and is headquartered in Bangkok, Thailand.'
    },
    'SCAP.BK': {
        'name': 'Srisawad Capital 1969 Public Company Limited',
        'address': '99/392 Srisawad Building 1,3,5,6 Floor Soi Chaeng Wattana 10 Yak 3 (Benjamitre) Changwattana Road, Tungsonghong, Laksi Bangkok 10210 Thailand',
        'phone': '66 2 073 0677',
        'website': 'http://www.bfit.co.th',
        'sector': 'Financial Services',
        'industry': 'Capital Markets',
        'description': 'Srisawad Capital 1969 Public Company Limited provides financial services in Thailand. It offers commercial lending services, such as loans for working capital with various short-term maturities; medium- and long-term loan facilities to finance expansion and capital expenditures; and aval and guarantee facilities. The company was formerly known as Srisawad Finance Public Company Limited and changed its name to Srisawad Capital 1969 Public Company Limited in September 2022. Srisawad Capital 1969 Public Company Limited was incorporated in 1969 and is based in Bangkok, Thailand.'
    },
    'SCB.BK': {
        'name': 'SCB X Public Company Limited',
        'address': '9 Ratchadapisek Road Jatujak Bangkok 10900 Thailand',
        'phone': '66 2 544 1000',
        'website': 'https://www.scb.co.th',
        'sector': 'Financial Services',
        'industry': 'Banks—Regional',
        'description': 'SCB X Public Company Limited operates as a holding company for The Siam Commercial Bank Public Company Limited that provides various financial products and services. The company offers various personal banking products and services, including savings, current, fixed deposit, and long term deposit accounts; payroll solutions; home, car, and personal loans; accident, savings, health, and other insurance services; debit, credit, prepaid, and gift cards; mutual funds, bonds, debentures, and other investment products; and payment, digital banking, and other services. It also provides corporate banking products and services comprising credit facilities; financial advisory and merger acquisition services; fixed income instrument and underwriting, structured finance, and project finance services; foreign exchange rate risk management, interest rate risk management, and investment solutions; cash management services; custodian, mutual fund supervisory, registrar, escrow and security agency, debentures holder representative, and custodian net services; and trade finance and remittance, and digital banking services. In addition, the company engages in the blockchain system. The company provides its products and services through its head office and branch network in Thailand; and through its branches in Singapore, Hong Kong, Laos, Vietnam, China, and the Cayman Islands. The company was formerly known as SCB Holdings Public Company Limited. SCB X Public Company Limited was founded in 1906 and is headquartered in Bangkok, Thailand.'
    },
    'SCC.BK': {
        'name': 'The Siam Cement Public Company Limited',
        'address': '1 Siam Cement Road Bangsue Bangkok 10800 Thailand',
        'phone': '66 2 586 3333',
        'website': 'https://www.scg.com',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'The Siam Cement Public Company Limited, together with its subsidiaries, operates in the cement and building materials, chemicals, and packaging businesses in Thailand and internationally. The company operates through Cement-Building Materials Business, Chemicals Business, Packaging Business, and Others segments. The Cement-Building Materials Business segment manufactures and distributes grey cement, ready-mixed concrete, white cement, dry mortar, refractory products, lightweight concrete, roof tiles, ceiling and wall boards, wood substitutes, concrete paving blocks, ceramic tiles, and sanitary wares and fittings. This segment also distributes cement, and building and decorative products for home and residence through omni channel; and offers logistics, delivery, and import and export services. The Chemicals Business segment manufactures and sells olefins, polyolefins, and vinyl and other chemical products. The Packaging Business segment provides fiber-based, paper and performance, and polymer packaging products; foodservice products; and pulp and paper products comprising primarily printing and writing paper and pulp; and recovered paper and plastic. The Others segment invests primarily in agricultural machines, automotive parts and components, steel, clean energy business, and pertinent technologies, as well as automation system integration business and other services. The Siam Cement Public Company Limited was founded in 1913 and is headquartered in Bangkok, Thailand.'
    },
    'SCCC.BK': {
        'name': 'Siam City Cement Public Company Limited',
        'address': 'Column Tower 3rd, 10th - 12th Floors 199 Ratchadapisek Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 797 7000',
        'website': 'http://www.siamcitycement.com',
        'sector': 'Basic Materials',
        'industry': 'Building Materials',
        'description': 'Siam City Cement Public Company Limited, together with its subsidiaries, manufactures, imports, exports, and sells cement and cement related products in Thailand, Vietnam, Sri Lanka, Australia, Cambodia, Bangladesh, China, and internationally. It operates through Cement, Concrete and Aggregate, Trading, and Light Building Material segments. The company offers mixed, hydraulic, and masonry cement under the INSEE Cement brand name; conventional and pumping, waterproofing, small and big bored pile, topping, mortar, sulfate resistant, and non-shrink concrete under the INSEE Concrete brand name; plastering, brick laying, floor leveling, tile adhesive, dry concrete, cementitious grout, and other products under the INSEE Mortar brand name; and blocks, lintels, and panels under the INSEE SUPERBLOCK brand name. In addition, it provides ready-mixed concrete and aggregates; construction materials and light-weight concrete products; industrial waste disposal, alternative fuel, raw material trading, and industrial cleaning services; waste disposal and management; and generates electricity from waste heat, and provides technical services, information technology management, and development services. The company was founded in 1969 and is headquartered in Bangkok, Thailand.'
    },
    'SCG.BK': {
        'name': 'Sahacogen (Chonburi) Public Company Limited',
        'address': '636 Moo 11 Sukaphiban 8 Road Nongkarm Sriracha Chonburi 20230 Thailand',
        'phone': '66 3 848 1555',
        'website': 'http://www.sahacogen.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Regulated Electric',
        'description': 'The Company operates the business of generating electricity and steam at Saha Group Industrial Park, Sriracha using a co-generating heat power production technology (Cogeneration Combined Cycle). Current capacity is at 214 megawatts of electricity and 96 tons of steam per hour. In addition, there are two renewable energy businesses through operation of biomass at Saha Industrial Park, Lamphun with capacity of 9.6 megawatts and steam 25 tons of steam per hour and at Phran Kratai District, Kamphaeng Phet Province with capacity of 7.5 megawatts.'
    },
    'SCGP.BK': {
        'name': 'SCG Packaging Public Company Limited',
        'address': '1 Siam Cement Road Bangsue Bangkok 10800 Thailand',
        'phone': '66 2 586 3333',
        'website': 'http://www.scgpackaging.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Packaging & Containers',
        'description': 'SCG Packaging Public Company Limited, through its subsidiaries, engages in the packaging business in Thailand, Indonesia, Vietnam, China, the Philippines, the United Kingdom, Spain, and Internationally. It operates through Integrated Packaging and Fibrous Business segments. The company produces and sells corrugated containers, retail display packaging, and flexible and rigid packaging, and medical supplies and labware, as well as packaging paper, grocery bags, and industrial bags. It offers flexible and rigid primary packaging; secondary packaging, such as folding carton; and tertiary packaging, including corrugated containers, parcel box, and paper tray and pallet. The company also offers foodservice products, such as food safety and eco-friendly packaging; printing and writing paper; and pulp products. In addition, it offers services in the areas of designing, including graphic and packaging design; integration of services for marketing events; E-Commerce services; and sustainable waste management services. The company was founded in 1975 and is headquartered in Bangkok, Thailand. SCG Packaging Public Company Limited is a subsidiary of The Siam Cement Public Company Limited.'
    },
    'SCI.BK': {
        'name': 'SCI Electric Public Company Limited',
        'address': 'No. 107/1 Moo 1 Bangna-Trad Km. 27 Road Bang Phriang Subdistrict Bang Bo 10560 Thailand',
        'phone': '66 2 338 1414',
        'website': 'http://www.sci-mfgr.com',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'SCI Electric Public Company Limited engages in the manufacture and sale of electrical switch boards and galvanized steel structures to various public and private sector projects in Thailand and internationally. It operates through three segments: Manufacture of Switch Board, Manufacture and Galvanized Service, and Services and Others. The Manufacturer of Switch Board segment manufactures and sells low and medium voltage electrical switch boards, cable trays, support systems, and related equipment. The Manufacture and Galvanized Service segment manufactures high voltage line tower and telecommunication towers, as well as galvanizing steel structures; sells wiring equipment; and offers hot dip galvanized services. The Services and Others segment offers project management services under the engineering, procurement, and construction contract; and sells electricity produced from the hydroelectric power plant. SCI Electric Public Company Limited was founded in 1966 and is headquartered in Bang Bo, Thailand.'
    },
    'SCM.BK': {
        'name': 'Successmore Being Public Company Limited',
        'address': '10/1-2 Ratchadapisek Road Chatuchak sub-district Chatuchak district Bangkok 10900 Thailand',
        'phone': '66 2 511 5955',
        'website': 'http://www.successmore.com',
        'sector': 'Consumer Defensive',
        'industry': 'Household & Personal Products',
        'description': 'Successmore Being Public Company Limited operates as a network marketing company in Thailand and internationally. It operates through Multi-Level Marketing, Distributor Sales, and Rendering Services segments. The company is involved in the research, development, manufacture, and distribution of dietary supplement, cosmetic, personal care, household, agricultural, and technology related products. It also arranges seminars; and provides render personnel services. The company sells its products under the Nutrinal, S Mone, Body Cheer, Neatly Home, Growing More, Smart Creation, and Multi Potential brands. Successmore Being Public Company Limited was incorporated in 2012 and is headquartered in Bangkok, Thailand.'
    },
    'SCN.BK': {
        'name': 'Scan Inter Public Company Limited',
        'address': '355, Bondstreet Road Bangpood Pakkret Nonthaburi 11120 Thailand',
        'phone': '66 2 503 4116',
        'website': 'http://www.scan-inter.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Regulated Gas',
        'description': 'Scan Inter Public Company Limited, together with its subsidiaries, primarily engages in trading natural gas through vehicle service stations in Thailand. The company operates through four segments: Gas and Oil Related Business; Natural Gas Vehicles Related Business; Renewable Energy; and Transportation Business. It engages in trading of gas through natural gas for vehicle (NGV) service stations; filling gas of industrial compressed natural gas for industrial applications; providing service for quality improvement of natural gas, and repair and maintenance services for NGV service stations; and trading of related parts and equipment. It is also involved in the design and installation of gas system in vehicles, as well as the testing of vehicle cylinders; and trading of related spare parts and equipments and repair and maintenance of vehicles and natural gas buses. In addition, the company operates a solar power plant; exports battery and glass; trades in solar cells, liquid carbon dioxide, engine oil, and lubricants; offers transportation, warehousing, and distribution services; manufactures and leases minibuses; cultivates and distributes cannabis and hemp; and engages in information technology business. Scan Inter Public Company Limited is headquartered in Nonthaburi, Thailand.'
    },
    'SCP.BK': {
        'name': 'Southern Concrete Pile Public Company Limited',
        'address': '555, SSP Tower Building 17th Floor Sukhumvit 63 (Ekamai) North Klongton, Wattana Bangkok 10110 Thailand',
        'phone': '66 2 711 5134',
        'website': 'http://www.scp.co.th',
        'sector': 'Basic Materials',
        'industry': 'Building Materials',
        'description': 'Southern Concrete Pile Public Company Limited manufactures, sells, installs, and services prestressed concrete products primarily in Thailand. Its prestressed concrete products include prestressed concrete piles, prestressed concrete spun piles, prestressed concrete slabs, prestressed plank girders, and retaining prestressed concrete piles. The company also offers electricity concrete products comprising prestressed concrete poles, concrete cross-arms, and concrete stabs, as well as prestressed anchors and pole foundations; and precasted concrete product, such as concrete flooring tiles, concrete mortar flooring tiles, concrete paving blocks, round big curbs, precast reinforced concrete, and main-holds. Southern Concrete Pile Public Company Limited was incorporated in 1979 and is headquartered in Bangkok, Thailand.'
    },
    'SDC.BK': {
        'name': 'Samart Digital Public Company Limited',
        'address': 'Software Park Building 34th Floor 99/3 Moo 4, Chaengwattana Road Klong Gluar, Pak-kred Nonthaburi Thailand',
        'phone': '66 2 502 6000',
        'website': 'http://www.samartdigital.com',
        'sector': 'Communication Services',
        'industry': 'Telecom Services',
        'description': 'Samart Digital Public Company Limited, together with its subsidiaries, distributes communications and electronics equipment in Thailand and internationally. The company operates through two segments, Digital Network and Digital Content. The Digital Network segment provides digital trunked radio systems and distribution equipment, audio-visual equipment network and software systems, and mobile antenna services. The Digital Content segment offers voice, audiovisual or multimedia, and infotainment services through mobile phones; content services through multimedia channels; multimedia and interactive media services; website services; and entertainment services, as well as produces television and radio programs, printed media, and billboards. It also engages in the production of outsource, live broadcast, and taped sporting events. The company was formerly known as Samart I-Mobile Public Company Limited and changed its name to Samart Digital Public Company Limited in October 2017. The company was founded in 1995 and is based in Nonthaburi, Thailand. Samart Digital Public Company Limited is a subsidiary of Samart Corporation Public Company Limited.'
    }
    ,

    # 481-500
    'SEAFCO.BK': {
        'name': 'Seafco Public Company Limited',
        'address': '144 Prayasuren Road Bangchan Khlong Sam Wah Bangkok 10510 Thailand',
        'phone': '66 2 919 0090',
        'website': 'http://seafco.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'Seafco Public Company Limited, together with its subsidiaries, engages in the construction of foundation and general public works in Thailand and internationally. It offers bored piling services, such as small and large diameter bored piling; rectangular, L shape, and T shape barrette piling services; and diaphragm walling services for deep basements, underpass tunnels, deep shafts, MRTA subway stations, and cut and cover tunnels. The company also undertakes ground improvement works, including soil improvement, deep mixing, and jet grouting for embankment foundations of highways, canals, riverbanks, tunnel openings, etc., as well as provision of vertical drain installation services. In addition, it is involved in the diaphragm wall, foundation, and building construction activities; and provision of various testing services comprising integrity test, drilling monitoring, pile load test, and geotechnical instrumentation. Seafco Public Company Limited was incorporated in 1974 and is headquartered in Bangkok, Thailand.'
    },
    'SE-ED.BK': {
        'name': 'SE-Education Public Company Limited',
        'address': '1858/87-90, Interlink Tower 19th Floor Debaratna Road Bangna Tai, Bangna Bangkok 10260 Thailand',
        'phone': '66 2 826 8000',
        'website': 'http://www.se-ed.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Specialty Retail',
        'description': 'SE-Education Public Company Limited, together with its subsidiaries, operates bookstores in Thailand. The company operates through Retail Business, Other Distribution Channels, and School Business segments. It operates SE-ED book centers, network stores, and various university bookstores in Bangkok and other provinces. The company also publishes books, and academic and educational books, as well as monthly magazines. In addition, it operates Plearnpattana School, which provides courses for students from pre-kindergarten to Matayom 6; offers consulting services; designs, develops, and distributes software and hardware products; and distributes books to bookstores. The company was founded in 1974 and is headquartered in Bangkok, Thailand.'
    },
    'SENA.BK': {
        'name': 'Sena Development Public Company Limited',
        'address': '448 Thanyalakpark Building Ratchadapisek 26 Khwaeng Samsen Nok Khet Huai Khwang Bangkok 10310 Thailand',
        'phone': '66 2 541 4642',
        'website': 'http://www.sena.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Sena Development Public Company Limited, together with its subsidiaries, engages in the development and sale of properties in Thailand. It primarily develops single houses, townhouses, shophouses, and condominiums; and rents apartments; and constructs residential real estate properties. The company is also involved in the golf course, juristic person management, and project management businesses. In addition, it manufactures and distributes electricity from solar energy; acts as a real estate agent and a broker; and provides information technology system, advertising management, asset management, and advisory services. The company was formerly known as Krungthep Keha Group Co., Ltd. Sena Development Public Company Limited was founded in 1977 and is headquartered in Bangkok, Thailand.'
    },
    'SFLEX.BK': {
        'name': 'Starflex Public Company Limited',
        'address': '189/48-49 Moo.3 Theparak Road T. Bangpreang Bang Bo 10560 Thailand',
        'phone': '66 2 708 2555',
        'website': 'http://www.starflex.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Packaging & Containers',
        'description': 'Manufacturing and distribution of flexible packaging for both food and non-food products in the form of made to order. The products can be divided into two forms which are roll form and pre form pouch.'
    },
    'SFP.BK': {
        'name': 'Siam Food Products Public Company Limited',
        'address': '1 Empire Tower 43rd Floor South Sathorn Road, Yannawa Sathorn Bangkok Thailand',
        'phone': '66 2 287 7000',
        'website': 'http://www.siamfood.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Siam Food Products Public Company Limited, together with its subsidiaries, grows, manufactures, and distributes processed food from agricultural products. Its products include pineapples in cans; aseptic and plastic bags; pineapple juice concentrates; other fruits in can and plastic cups; and canned pineapple juices, as well as animal feeds. The company is also involved in the commercial and investment activities. It also exports its products. The company was founded in 1970 and is based in Bangkok, Thailand. Siam Food Products Public Company Limited is a subsidiary of Plantheon Company Limited.'
    },
    'SGC.BK': {
        'name': 'SG Capital Public Company Limited',
        'address': '72 NT Bangrak Tower 20th Floor Charoenkrung Road Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 028 2828',
        'website': 'http://www.sgcapital.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Provide (1) hire-purchase financing for home appliances, commercial appliances and machine (2) hire-purchase financing and vehicle title loans (3) debt consolidation credit services and (4) Click2Gold credit services under "SG Capital" trademark.'
    },
    'SGP.BK': {
        'name': 'Siamgas and Petrochemicals Public Company Limited',
        'address': '553 The Palladium Building 30th Floor Ratchaprarop Road Makkasan, Ratchathewi Bangkok 10400 Thailand',
        'phone': '66 2 120 9999',
        'website': 'http://www.siamgas.com',
        'sector': 'Energy',
        'industry': 'Oil & Gas Refining & Marketing',
        'description': 'Siamgas and Petrochemicals Public Company Limited, together with its subsidiaries, trades in petroleum and petrochemical products in Thailand and internationally. It operates through Petroleum and Petrochemical Products, Transportation Services, and Other segments. The company involved in trading of petroleum for household cooking, industry, and transportation sectors. In addition, it provides transportation services by land and ship; manufactures and distributes LPG cylinders; and oil depots and port services, as well as warehousing and storage services. The company was formerly known as VSPP Development Company Limited and changed its name to Siamgas and Petrochemicals Public Company Limited. Siamgas and Petrochemicals Public Company Limited was founded in 2001 and is headquartered in Bangkok, Thailand.'
    },
    'SHANG.BK': {
        'name': 'Shangri-La Hotel Public Company Limited',
        'address': 'No. 89 Soi Wat Suan Plu Charoenkrung Road Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 236 7777',
        'website': 'http://www.shangri-la.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'Shangri-La Hotel Public Company Limited operates hotels in Bangkok and Chiang Mai provinces. Its hotel facilities include rooms and suites, restaurants, bars and lounges, and various other services. The company was founded in 1981 and is based in Bangkok, Thailand. Shangri-La Hotel Public Company Limited is a subsidiary of Shangri-La Asia Limited.'
    },
    'SHR.BK': {
        'name': 'S Hotels and Resorts Public Company Limited',
        'address': '123 Suntowers Building B 10th Floor Vibhavadi-Rangsit Road Chom Phon, Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 058 9888',
        'website': 'http://www.shotelsresorts.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Resorts & Casinos',
        'description': 'S Hotels and Resorts Public Company Limited, together with its subsidiaries, engages in the investment, hospitality, and related businesses in Thailand. It offers a portfolio of properties to guests in the Republic of Maldives, the Republic of Fiji, the Republic of Mauritius, the United Kingdom, and Thailand. The company was incorporated in 2019 and is based in Bangkok, Thailand. S Hotels and Resorts Public Company Limited is a subsidiary of Singha Estate Public Company Limited.'
    },
    'SHREIT.BK': {
        'name': 'Strategic Hospitality Extendable Freehold and Leasehold Real Estate Investment Trust',
        'address': 'Unit 2401, Empire Tower 24th Floor South Sathorn Road Yannawa Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 286 2461',
        'website': 'https://www.sh-reit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Hotel & Motel',
        'description': 'Strategic Hospitality Extendable Freehold and Leasehold Real Estate Investment Trust ("SHREIT") is a pioneering international REIT managed by Strategic Property Investors Company Limited. We provide investors with well-diversified portfolio of hospitality assets, access to younger and faster growing Mekong region countries through a regulated vehicle. SHREITs initial portfolio is spread across key cities in Mekong region  Ho Chi Minh City and Jakarta. Each of the asset in the initial portfolio is strategically located, urban focused, and fully differentiates itself from it competitors. The REITs hotels are catered for different customer segments, ranging from economy to luxury, with a total of 632 rooms under management. The hotels are operated by top international hotel operators such as Accor and Frasers.'
    },
    'SIAM.BK': {
        'name': 'Siam Steel International Public Company Limited',
        'address': '51 Moo 2, Poochao Road Bangyaprak Phra Pradaeng 10130 Thailand',
        'phone': '66 2 384 2876',
        'website': 'http://www.siamsteel.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Furnishings, Fixtures & Appliances',
        'description': 'Siam Steel International Public Company Limited, together with its subsidiaries, manufactures and sells steel office equipment and furniture, and furniture parts in Thailand. The company is also involved in construction business. Its steel and wooden furniture products include cabinets, lockers, and combine furniture systems; desks and tables; chairs; partitions; safes; shelving systems; and furniture for stadiums comprising bleachers and folding stages. In addition, the company provides prefabricated building systems that consist of permanent buildings, which includes business hotels, convenience stores, showrooms, etc.; temporary buildings, such as mobile offices, mobile clinics, kiosks, mobile toilets, etc.; and storage buildings, which consists of telecom shelters, warehouse units, soundproof rooms, etc. Further, it offers special products, such as flood protection panel and related products, bathroom pods, smart wall systems, earthquake and seismic retrofits, bulletproof security products, and steel structure solutions, as well as building materials, including doors, staircases, etc. It also invests in solar energy plants and alternative energy; and manufactures and distributes solar equipment and fuel stick. The company offers its products under the Lucky, Kingdom, Siamsteel, Okamura, Chitose, ITO, and Pilot brand names. Siam Steel International Public Company Limited was founded in 1953 and is headquartered in Phra Pradaeng, Thailand.'
    },
    'SINGER.BK': {
        'name': 'Singer Thailand Public Company Limited',
        'address': '72, NT Bangrak Building 17th Floor Charoen Krung Road Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 352 4777',
        'website': 'http://www.singerthai.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Specialty Retail',
        'description': 'Singer Thailand Public Company Limited distributes household electrical and commercial appliances in Thailand. The company operates through three segments: Trade sales, Hire purchase and loans, and Service and Others. It offers household electrical appliances, such as sewing machines, sewing needles, general lubricating oils in drip bottles, and scissors; refrigerators, washing machines, gas stoves, and air conditioners; and audio and video products, including flat screen LED TVs, digital set-top boxes, and home theatre systems. The company also provides commercial appliances comprising freezers, beverage coolers, wine coolers cabinets, ice cream and bakery freezers, and slush ice machines; airtime, petrol, and drinking water vending machines; and agricultural equipment, such as water pumps, portable fertilizer spraying machines, and rice milling machines. In addition, the company engages in the life and non-life insurance brokerage business; hire purchase of home appliances, sewing machines, commercial products, mobile phones, and vehicles, as well as loan receivables with vehicle collateral and others; and repair and maintenance service of electrical appliances. Further, it provides debt collection services to a related company; and personal loans. The company sells its products under the Singer brand name through a network of branch outlets and sales representatives, as well as through debt collectors in Thailand. The company was founded in 1889 and is headquartered in Bangkok, Thailand.'
    },
    'SIRI.BK': {
        'name': 'Sansiri Public Company Limited',
        'address': 'Siri Campus Building 59 Soi Rim Khlong Phra Khanong Phra Khanong Nuea Sub-district Vadhana District Bangkok 10110 Thailand',
        'phone': '66 2 027 7888',
        'website': 'http://www.sansiri.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Sansiri Public Company Limited, together with its subsidiaries, engages in the property development business in Thailand. It operates through Property Development; Building Management, Project Management and Real Estate Brokerage; Hotel Management; and Other Business segments. The company develops single-detached and semi-detached houses, townhouses, home offices, and condominium projects; and invests in leasehold commercial building under the Habito Mall retail name, which includes various retails shops and restaurants. In addition, the company offers property and asset management services, including property brokerage services, property sales management, property development consultancy, and property management; building inspection services; lifestyle concierge service for individuals and corporates; and event management and wedding planning services, as well as operates hospitality business and educational business under the Satit Pattana School brand. It also engages in investment business, which invests in future, such as way of life, work, recreation, and learning through new technologies and media. The company was founded in 1984 and is headquartered in Bangkok, Thailand.'
    },
    'SIRIP.BK': {
        'name': 'Siri Prime Office Property Fund',
        'address': '7-8th Floor, SCB Park Plaza 1, 18 Ratchadapisek Rd., Chatuchak Bangkok 10900',
        'phone': '66 2 949 1500',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Office',
        'description': 'The Fund has invested in freehold right of Siripinyo Building Project ,the office building for rent, consist of land with 2 rai, 3 ngarn, 13.4 square wah and 1 office building with utilities systems and other movable properties in connection with the operation of building. The total usable area is 41,758 square meters, and the total leased area is 18,364 square meters.'
    },
    'SIS.BK': {
        'name': 'SiS Distribution (Thailand) Public Company Limited',
        'address': 'No. 9, Pakin Building Room No.901, 9th Floor Ratchadaphisek Road Din Daeng Sub-Dist., Din Daeng District Bangkok 10400 Thailand',
        'phone': '66 2 020 3000',
        'website': 'http://www.sisthai.com',
        'sector': 'Technology',
        'industry': 'Electronics & Computer Distribution',
        'description': 'SiS Distribution (Thailand) Public Company Limited, together with its subsidiaries, distributes computer components, smartphones, and office automation equipment in Thailand. The company operates through four segments: Commercial Products, Consumer Products, Value Added Products, and Phones. It is also involved in the servicing and rental of computers and accessories. The company was founded in 1998 and is headquartered in Bangkok, Thailand.'
    },
    'SISB.BK': {
        'name': 'SISB Public Company Limited',
        'address': '498/12, Soi Ramkhamhaeng 39 (Tepleela 1) Pracha Uthit Road Wangthonglang Bangkok 10310 Thailand',
        'phone': '66 2 158 9090',
        'website': 'http://www.sisb.ac.th',
        'sector': 'Consumer Defensive',
        'industry': 'Education & Training Services',
        'description': 'SISB Public Company Limited provides educational services. The company owns and manages Singapore international schools in Thailand, including four campuses that adopt Singapore and the United Kingdom curricula as the foundation for teaching and learning. It also owns and manages three schools in Bangkok. The company was incorporated in 2001 and is headquartered in Bangkok, Thailand.'
    },
    'SITHAI.BK': {
        'name': 'Srithai Superware Public Company Limited',
        'address': '15 Suksawat Road Soi 36, Bangpakok Rasburana Bangkok 10140 Thailand',
        'phone': '66 2 427 0088',
        'website': 'http://www.srithaisuperware.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Packaging & Containers',
        'description': 'Srithai Superware Public Company Limited, together with its subsidiaries, manufactures and distributes household plasticware and industrial products in Vietnam and internationally. It provides various food packaging products; beverage packaging products comprising PET bottle crate, drink lids, and preforms; rigid packaging products; automotive and motorcycle battery cases; material handling products, such as pallets and crates, garbage bins; plastic furniture products comprise tables and chairs. The company also manufactures and distributes melamine products; and mold for plastic injection. Srithai Superware Public Company Limited was founded in 1963 and is headquartered in Bangkok, Thailand.'
    },
    'SJWD.BK': {
        'name': 'SCGJWD Logistics Public Company Limited',
        'address': '36 Krungthep Kreetha Road Huamark Bangkapi Bangkok 10240 Thailand',
        'phone': '66 2 710 4000',
        'website': 'http://www.jwd-group.com',
        'sector': 'Industrials',
        'industry': 'Integrated Freight & Logistics',
        'description': 'SCGJWD Logistics Public Company Limited, together with its subsidiaries, engages in the integrated in-land and oversea logistics business in Thailand, Taiwan, Singapore, the United States, and internationally. The company operates through six segments: Integrated Logistics, Supply Chain and Warehouse Management; Transportation Services; Domestic and International Removal; Record and Information Storage; Foods; and Others. It offers general, and chemical and dangerous goods warehousing, automotive logistics and yard management, cold chain management, freight forwarding and supply chain management, transportation and distribution, document storage and information management, and project cargo logistics services; and moving and relocation, self-storage, fine art logistics, and e-commerce logistics and fulfillment services, as well as logistics software development services. The company also provides information technology (IT) logistics solutions; port, art gallery, coastal freight forwarding, logistics and medical transportation management, and laboratory testing services; leases land and buildings; packing, domestic and overseas moving services; and sells and installs electronics devices, software applications, and network services. The company was formerly known as JWD InfoLogistics Public Company Limited and changed its name to SCGJWD Logistics Public Company Limited in February 2023. SCGJWD Logistics Public Company Limited was founded in 1979 and is based in Bangkok, Thailand.'
    },
    'SKE.BK': {
        'name': 'Sakol Energy Public Company Limited',
        'address': '15 Moo 1 Chiang Rak Noi Sam Khok Pathum Thani 12160 Thailand',
        'phone': '66 2 026 3451',
        'website': 'http://www.sakolenergy.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Diversified',
        'description': 'Sakol Energy Public Company Limited operates in the energy industry in Thailand. The company provides natural gas compression services to the natural gas transportation vehicles of PTT Public Company Limited. It also produces and distributes compressed bio-methane gas; generates and supplies electricity from biomass with the installed capacity of 9.90 megawatts; waste and non-hazardous materials management services; and rents real estate property. The company was founded in 2009 and is headquartered in Pathum Thani, Thailand.'
    },
    'SKN.BK': {
        'name': 'S.Kijchai Enterprise Public Company Limited',
        'address': '99/9 Moo 7, Huay-yang Klang District Rayong 21110 Thailand',
        'phone': '66 3 892 8188',
        'website': 'http://www.skn.co.th',
        'sector': 'Basic Materials',
        'industry': 'Lumber & Wood Production',
        'description': 'S.Kijchai Enterprise Public Company Limited manufactures and distributes wood substitute products with medium density fiber boards in Thailand. The companys products include furniture, flooring, and interior products, as well as doors. It also offers glue and chemical products, as well as involved in the manufacturing of paper and paper pulp through of recycling wastepaper. The company was founded in 2010 and is based in Rayong, Thailand.'
    }
    # ,

    # 501-520
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },

    # 521-540
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
}


@app.route('/')
def insert_profiles():
    try:
        cur = mysql.connection.cursor()

        for ticker, profile in company_profiles.items():
            name = profile['name']
            address = profile.get('address', None)
            phone = profile.get('phone', None)
            website = profile.get('website', None)
            sector = profile.get('sector', None)
            industry = profile.get('industry', None)
            description = profile['description']

            # check if the record already exists
            cur.execute("SELECT * FROM company_profiles WHERE ticker=%s", (ticker,))
            record = cur.fetchone()
            if record:
                # update the existing record
                cur.execute("UPDATE company_profiles SET name=%s, address=%s, phone=%s, website=%s, sector=%s, industry=%s, description=%s WHERE ticker=%s", (name, address, phone, website, sector, industry, description, ticker))
            else:
                # insert a new record
                cur.execute("INSERT INTO company_profiles (ticker, name, address, phone, website, sector, industry, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ticker, name, address, phone, website, sector, industry, description))

            mysql.connection.commit()

        cur.close()
        return 'Company profiles inserted successfully!'

    except Exception as e:
        return str(e)



if __name__ == '__main__':
    app.run(debug=True)