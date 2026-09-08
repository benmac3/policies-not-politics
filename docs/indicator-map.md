# Transcript-to-data map

All targets below are source families or collection names; only the explicitly loaded observations in `data/observations.json` have been ingested. Detailed series identifiers must be fixed before adding any new table. OECD is an intergovernmental harmonisation layer, not a national statistical office. The 38-country directory identifies national entry points; it is not a completed country-by-indicator data-availability audit.

| Indicator family | Transcript claim IDs | Australian government source | Comparable international source | Definition / caution |
|---|---|---|---|---|
| Output per hour and multifactor productivity | C18, C19, C24 | ABS national accounts; Productivity Commission | OECD Productivity Database DSD_PDB@DF_PDB | Hours, sector and PPP vintage must match |
| Real GDP per capita | C14, C18 | ABS National Income, Expenditure and Product | OECD Annual National Accounts | Separate population from productivity; China non-member |
| Real household disposable income | C02, C24 | ABS household sector accounts; household surveys | OECD Household Dashboard / Income Distribution Database | Mean vs median; household size adjustment |
| Wages and cost of living | C02, C03 | ABS WPI, CPI, Selected Living Cost Indexes | OECD earnings and consumer prices; national statistical offices | Use matched periods and indexes; mortgage interest differs between measures |
| Housing affordability | C12 | ABS housing and income collections; RBA housing tables | OECD analytical house-price indicators | Price-to-income index not an absolute affordability multiple |
| Household liquid buffers and financial stress | C01, C05 | ABS Household Expenditure Survey and income/wealth surveys | OECD Wealth Distribution Database; Federal Reserve SHED for US | Emergency size, means of payment and survey denominator differ |
| Wealth shares, inequality and poverty | C15, C21 | ABS Household Income and Wealth | OECD IDD / WDD; US Fed Distributional Financial Accounts | Household vs individual; wealth stock vs income flow; include debts |
| Capital ownership and financial independence | C05, C22 | ABS wealth; APRA superannuation; ATO statistics | OECD pension/wealth statistics | No harmonised annual labour-to-capital transition measure identified |
| Government expenditure / GDP | C03, C08, C18 | ABS Government Finance Statistics; Treasury Budget | OECD general-government accounts and COFOG | All levels vs central government; transfers not direct production |
| Gross / net debt and interest | C07, C21 | Treasury Budget; PBO; AOFM; ABS GFS | OECD general-government financial accounts | Publicly held and gross concepts differ; match fiscal scope |
| Money and central-bank bond holdings | C07 | RBA statistical tables | National central banks | Debt issuance is not automatically monetary financing |
| Tax mix and effective burdens | C09, C10, C11 | ATO Taxation Statistics; Treasury tax expenditure reporting | OECD Revenue Statistics / Taxing Wages; national tax authorities | Effective vs statutory; income vs wealth; lifecycle and company tax |
| Public and publicly funded employment | C08, C20 | ABS public-sector employment, Labour Account, Census; NDIA workforce evidence | OECD Government at a Glance / national labour statistics | Employer control and funding share are separate axes |
| Business formation and innovation | C15, C17 | ABS business entries/exits, innovation and R&D surveys | OECD business demography / MSTI; Statistics Denmark | Rates per active firms/person; survival and high-growth definitions |
| University staff mix and graduate outcomes | C04, C13 | Department of Education higher-education staff/student collections; ATO HELP data | US NCES/IPEDS; OECD Education at a Glance | Qualifications not unique graduates; administrative roles change |
| AI adoption and age-specific employment | C19, C24 | ABS business technology and labour-force collections; Jobs and Skills Australia | OECD ICT business use and labour data; US BLS/Census | Occupation exposure is not actual adoption; cohort effects |
| Energy costs and security | C23 | DCCEEW fuel statistics; AEMO demand and generation; ABS energy CPI | IEA and national energy administrations | Stocks, consumption, import cover and capacity not interchangeable |
| NDIS spending / outcomes / integrity | Extension of C03, C08, C20 | NDIA annual/quarterly reports and AFSR; ANAO; Senate estimates; NDIA/AFP outcomes | No directly comparable scheme across OECD identified | Compare disability-support systems by function, not programme name |
| Parliamentary career history | C16 | Parliamentary Handbook and official member/senator biographies | Not part of this OECD panel | Full census, mixed careers, date intervals and missingness |

Source links are in `data/sources.json` and `data/countries.json`. Further official entry points to verify and freeze at ingestion: https://www.ato.gov.au/ ; https://www.apra.gov.au/ ; https://www.education.gov.au/ ; https://www.aofm.gov.au/ ; https://www.anao.gov.au/ ; https://www.jobsandskills.gov.au/ ; https://www.aemo.com.au/ ; https://nces.ed.gov/ipeds/ ; https://www.bls.gov/ ; https://www.federalreserve.gov/releases/z1/dataviz/dfa/ . AEMO is the market operator rather than a government statistical agency; label that provenance separately.
