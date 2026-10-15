# Appointment date reconciliation

This review applies date-only amendments to existing appointment IDs. The 174 attributable personal profiles cover 2,349 existing occupational, governance and elected records. Employer-specific searches (1,438, plus supplementary role searches) yielded 139 matched date pairs for 74 members. Search indexes expose only fragments; missing dates remain unknown. No claim of complete profile histories is made.

The overlay changes 74 boundaries across 43 appointments; 16 conflicting appointment pairs retain their original dates. Another 23 ranges remain unassigned because they do not isolate a discrete appointment.

## Application and review rules

The owning research branches still contain the member records. This register joins those records in `build_careers.py` when they are integrated; it does not copy unrelated member data into this branch. Absent members are skipped. Existing employer, role, dates and precision must match the recorded baseline or the build fails for review. The baseline commit is recorded per match.

Only start/end dates are newly retained. Month/year precision is preserved; exact existing days are retained when compatible. A conflicting boundary holds the entire pair. An indexed “Present” label supplies no end date and never clears an existing closed end. Employer-wide periods and promotion-spanning intervals are withheld. Titles, employers, sector classifications, FTE, counting notes and headline totals are unchanged. Headline totals are not recalculated from these dates.

Evidence came from public search-index excerpts, checked 2026-10-15. Direct profile retrieval was unavailable. Excerpts may be stale, and have not been independently verified against live profiles. Source-identifying URLs and raw excerpts are not included in this review. The dates are proposed evidence, not authoritative corrections.

## Matched appointment review

Appointment labels below reproduce the existing career data. “Held” preserves both original boundaries; “reconciled” accepts compatible refinements/additions. A closed-end warning preserves the existing end despite an indexed ongoing label.

| Member / appointment | Existing dates | Indexed dates | Result | Decision |
|---|---|---|---|---|
| ALDRED, Mary / 11788-18 / Lifeline Gippsland / Board member | 2010 → 2013 | 2010 → 2013 | 2010 → 2013 | reconciled |
| ANANDA-RAJAH, Dr Michelle / 290544-04 / JAMA Network Open / Statistical and methods reviewer | 2019-07 → 2022-08 | 2019-07 → 2022-08 | 2019-07 → 2022-08 | reconciled |
| BELL, Angie Marion / 282981-09 / Paint Place Group of Stores / Paint Place Group Limited — contracting entity to confirm / National business development manager | 2015-01 → 2018-10 | 2015-01 → 2018-10 | 2015-01 → 2018-10 | reconciled |
| BELYEA, Jodie Anne / 309484-01 / Connectus / Premier's Drug Prevention Council project (legal employer unresolved) / Executive manager | 2005 → 2007 | 2005-02 → 2007-07 | 2005-02 → 2007-07 | reconciled |
| BELYEA, Jodie Anne / 309484-02 / Jobs Australia Foundation / Executive manager | 2010 → 2015 | 2010-01 → 2015-03 | 2010-01 → 2015-03 | reconciled |
| BELYEA, Jodie Anne / 309484-03 / Anglicare Victoria / Partnerships coordinator | 2015 → 2017 | 2015-09 → 2017-07 | 2015-09 → 2017-07 | reconciled |
| BERRY, Carol / 23497-ombudsman / NSW Ombudsman / Principal Project Officer, Practice Reform, Disability Reportable Incidents Division; disability-sector oversight | 2013-12 → 2018-03 | 2013-12 → 2018-03 | 2013-12 → 2018-03 | reconciled |
| BIRRELL, Samuel (Sam) James / 288713-01 / Wayne Skinner Rural Supplies Pty Ltd / Croptec / Agronomist | 2002-02 → 2008-09 | 2002-01 → 2008-08 | 2002-02 → 2008-09 | held_conflict |
| BIRRELL, Samuel (Sam) James / 288713-04 / Committee for Greater Shepparton / Chief executive officer | 2016-03-01 → 2021-12-24 | 2016-03 → 2022-01 | 2016-03-01 → 2021-12-24 | held_conflict |
| BLEYER, Vanessa / 25813-03 / Wilmoth Field Warne Lawyers / Commercial lawyer | 2003 → 2005 | 2003 → 2005 | 2003 → 2005 | reconciled |
| BLEYER, Vanessa / 25813-09 / Architects Registration Board of Victoria / Board member, Consumer Affairs nominee | 2006-09 → 2012-06-30 | 2006 → 2012 | 2006-09 → 2012-06-30 | reconciled |
| BLEYER, Vanessa / 25813-13 / Community Care Tasmania / Board member | 2017-09 → ? | 2017 → Present | 2017-09 → ? | reconciled |
| BRAGG, Andrew James / 256063-candidate / Liberal Party of Australia / Senate campaign (payroll entity unresolved) / Endorsed Liberal candidate for the Senate | 2018-12 → 2019-07 | 2018-12 → 2019-07 | 2018-12 → 2019-07 | reconciled |
| BRAGG, Andrew James / 256063-woolworths / Woolworths Limited / Management traineeship | 2002-02 → 2003-02 | 2002-02 → 2003-02 | 2002-02 → 2003-02 | reconciled |
| BROCKMAN, William (Slade) Edward Slade / 30484-08 / Ideas Department / Operations and general manager | 1996 → 1998 | 1996 → 1998 | 1996 → 1998 | reconciled |
| CANAVAN, the Hon. Matthew (Matt) James / 245212-04 / Office of Senator Barnaby Joyce / Chief of staff | 2010 → 2013 | 2010-03 → 2013-07 | 2010-03 → 2013-07 | reconciled |
| CHANEY, Kate / 300006-08 / Anglicare WA / Director, Innovation and Strategy | 2017 → 2022 | 2017-10 → 2022-01 | 2017-10 → 2022-01 | reconciled |
| CHANEY, Kate / 300006-13 / Next25 / Board member | 2013-03 → 2022-01-22 | 2013-03 → 2022-01 | 2013-03 → 2022-01-22 | reconciled |
| CHANEY, Kate / 300006-14 / Awesome Arts / Board member | 2014-05 → 2016-07 | 2014-05 → 2016-07 | 2014-05 → 2016-07 | reconciled |
| CLARE, the Hon. Jason Dean / HWL-transurban / Transurban / Manager of Corporate Relations | 2003 → 2007 | 2003 → 2007 | 2003 → 2007 | reconciled |
| CLUTTERHAM, Claire Louise / 316101-03 / Al Tamimi & Company / Arbitration lawyer, Dubai | ? → ? | 2008 → 2013 | 2008 → 2013 | reconciled |
| CLUTTERHAM, Claire Louise / 316101-04 / Clifford Chance / Lawyer / senior associate, Dubai | ? → ? | 2013 → 2016 | 2013 → 2016 | reconciled |
| CLUTTERHAM, Claire Louise / 316101-05 / ASC Pty Ltd / Deputy general counsel | 2017 → 2021 | 2017 → 2021 | 2017 → 2021 | reconciled |
| COLBECK, the Hon. Richard Mansell / 00AOL-12 / Australian Senate / Senator for Tasmania, first service period | 2002-02-04 → 2016-07-02 | 2002 → 2016-07 | 2002-02-04 → 2016-07-02 | reconciled |
| COLLINS, Dr Jessica / 297964-macquarie-support / Macquarie University / Support Academic | 2014-03 → 2014-06 | 2014-03 → 2014-06 | 2014-03 → 2014-06 | reconciled |
| COLLINS, the Hon. Julie Maree / HWM-13 / Australian Labor Party (Tasmania) / State secretary | 2006 → 2007 | 2006-02 → 2007-11 | 2006-02 → 2007-11 | reconciled |
| CONAGHAN, Patrick (Pat) John / 279991-lawyers-subspell / Conaghan Lawyers (legal payroll link to Conaghan Lawyers Pty Ltd not separately established) / Senior Solicitor; criminal-defence solicitor advocate | 2010-12 → 2019-05 | 2010-12 → 2019-05 | 2010-12 → 2019-05 | reconciled |
| DARMANIN, Lisa / 301128-04 / HESTA / Board member | 2013 → 2017 | 2013 → 2017-12 | 2013 → 2017-12 | reconciled |
| DARMANIN, Lisa / 301128-07 / Australian Services Union, Victorian and Tasmanian Branch / Branch secretary | 2018-06-26 → 2024-06-02 | 2018-05 → 2024-06 | 2018-06-26 → 2024-06-02 | held_conflict |
| DARMANIN, Lisa / 301128-09 / Vision Super / Chair | 2021-07-01 → 2024-05-10 | 2021-07 → 2024-06 | 2021-07-01 → 2024-05-10 | held_conflict |
| DARMANIN, Lisa / 301128-11 / Portable Long Service Leave Authority / Board member | 2022-09-01 → 2024-02-27 | 2022-09 → 2024-04 | 2022-09-01 → 2024-02-27 | held_conflict |
| DARMANIN, Lisa / 301128-12 / Super Members Council of Australia / Board member | 2023-11 → 2024-05 | 2023-11 → 2024-05 | 2023-11 → 2024-05 | reconciled |
| DARMANIN, Lisa / 301128-tfnboard / Trust for Nature (Victoria) / Trustee | 2022-05-03 → 2024-04-19 | 2022-05 → 2024-06 | 2022-05-03 → 2024-04-19 | held_conflict |
| DOLEGA, Josh / 316935-04 / Australian Taxation Office / Tax officer | 2005 → 2018 | 2017-05 → 2019-05 | 2005 → 2018 | held_conflict |
| DOLEGA, Josh / 316935-06 / Community and Public Sector Union, PSU Group / Work health and safety lead organiser | 2023 → 2025 | 2023-09 → 2025-05 | 2023-09 → 2025-05 | reconciled |
| FARUQI, Dr Mehreen Saeed / 250362-port-council / Port Macquarie-Hastings Council / Manager, Natural Resources and Environmental Engineer | 2001-08 → 2004-08 | 2001-07 → 2004-08 | 2001-08 → 2004-08 | held_conflict |
| FRENCH, Tom / 316550-05 / Electrical Trades Union, WA Branch / Industrial officer | 2024-07 → 2025-05 | 2024-07 → 2025-05 | 2024-07 → 2025-05 | reconciled |
| FRENCH, Tom / 316550-06 / United Professional Firefighters Union / Industrial officer / lawyer; title transitions unconfirmed | ? → ? | 2022-06 → 2024-06 | 2022-06 → 2024-06 | reconciled |
| GORMAN, the Hon. Patrick / 74519-04 / United Voice, national office, Sydney / Director of Public Affairs | 2014 → 2015 | 2014 → 2015 | 2014 → 2015 | reconciled |
| GOSLING, Luke John Anthony, OAM / 245392-03 / Australian Army, Timor-Leste / Military officer | 2005 → 2008 | 2005 → 2008 | 2005 → 2008 | reconciled |
| GROGAN, Karen Ann / 296331-08 / University of South Australia / Director, Centre for Participation and Community Engagement; interim Head, UniSA College | 2009-10 → 2010-10 | 2009-10 → 2010-10 | 2009-10 → 2010-10 | reconciled |
| GROGAN, Karen Ann / 296331-09 / Office of the Hon. Mark Butler MP / Chief of staff | 2010-09 → 2016-10 | 2010-09 → 2016-10 | 2010-09 → 2016-10 | reconciled |
| GROGAN, Karen Ann / 296331-12 / Wentworth Group of Concerned Scientists / Executive director | 2018-11 → 2019-08 | 2018-12 → 2019-08 | 2018-11 → 2019-08 | held_conflict |
| HAINES, Dr Helen Mary / 282335-07 / Hume Medicare Local / Company director | 2012 → 2015 | 2012-07 → 2015-07 | 2012-07 → 2015-07 | reconciled |
| HAINES, Dr Helen Mary / 282335-08 / Karolinska Institutet, Sweden / Postdoctoral fellow | 2014-04 → 2014-11 | 2014-01 → 2014-12 | 2014-04 → 2014-11 | held_conflict |
| HAINES, Dr Helen Mary / 282335-10 / St Catherine's, Wangaratta / Board member | 2016 → 2019 | 2016-12 → Present | 2016-12 → 2019 | reconciled; closed end retained |
| HUME, the Hon. Edwina Jane (Jane) / 266499-03 / National Australia Bank / Private banker | 1998-08 → 1999-06 | 1998-08 → 1999-06 | 1998-08 → 1999-06 | reconciled |
| HUME, the Hon. Edwina Jane (Jane) / 266499-07 / Royal Children's Hospital, Melbourne / Non-executive director; Community Advisory Committee chair; Finance Committee member | 2011 → 2016-05-09 | 2011-07 → 2016-05 | 2011-07 → 2016-05-09 | reconciled |
| HUME, the Hon. Edwina Jane (Jane) / 266499-09 / AustralianSuper (trustee AustralianSuper Pty Ltd) / Senior strategic policy adviser | 2015 → 2016 | 2015-06 → 2016-06 | 2015-06 → 2016-06 | reconciled |
| HUSIC, the Hon. Edham (Ed) Nurredin / 91219-integral / Integral Energy / Corporate Affairs Manager | 1999 → 2004 | 1999 → 2004 | 1999 → 2004 | reconciled |
| KEARNEY, the Hon. Gerardine (Ged) Mary / LTU-08 / Australian Council of Trade Unions / President | 2010-07-01 → 2018 | 2010-07 → 2018-03 | 2010-07-01 → 2018-03 | reconciled |
| KENNEDY, Simon Peter / 267506-clayton-utz / Clayton Utz / Paralegal / graduate lawyer specialising in mergers and acquisitions | 2005-12 → 2007-05 | 2005-12 → 2007-05 | 2005-12 → 2007-05 | reconciled |
| KEOGH, the Hon. Matthew (Matt) James / 249147-01 / iiNet / Senior customer service officer | 2000 → 2002 | 2000 → 2002 | 2000 → 2002 | reconciled |
| KEOGH, the Hon. Matthew (Matt) James / 249147-06 / Commonwealth Director of Public Prosecutions / Prosecutor; later Principal Federal Prosecutor | 2006 → 2011 | 2006-10 → 2011-03 | 2006-10 → 2011-03 | reconciled |
| KEOGH, the Hon. Matthew (Matt) James / 249147-10 / Law Access Limited / Inaugural chairperson; director | ? → 2017-12 | 2014-12 → 2017-12 | 2014-12 → 2017-12 | reconciled |
| KHALIL, the Hon. Peter / 101351-14 / Special Broadcasting Service / Director, strategy and communications; later corporate affairs | 2012-05-21 → 2015-07 | 2012 → 2015 | 2012-05-21 → 2015-07 | reconciled |
| KHALIL, the Hon. Peter / 101351-16 / Victorian Multicultural Commission / Commissioner and regional advisory council chair | 2015 → 2016-02-07 | 2015 → 2016 | 2015 → 2016-02-07 | reconciled |
| KING, the Hon. Madeleine Mary Harvie / 102376-08 / Sexual and Reproductive Health Western Australia / Volunteer board member | 2008-03 → 2014-04 | 2008-03 → 2014-04 | 2008-03 → 2014-04 | reconciled |
| LANDRY, the Hon. Michelle Leanne / 249764-02 / National Australia Bank / Supervisor | 1985 → 2007 | 1985-02 → 2007-03 | 1985-02 → 2007-03 | reconciled |
| LAWRENCE, Tania / 299150-05 / Beelu Forest Distilling Company Pty Ltd / Managing director / founder | 2021-04 → ? | 2021-04 → Present | 2021-04 → ? | reconciled |
| LAXALE, Jerome / 299174-family-business / Laxale's Hair & Beauty Supplies Pty Ltd / General Manager and Director | 2004-11 → 2017-11 | 2004-11 → 2017-11 | 2004-11 → 2017-11 | reconciled |
| LAXALE, Jerome / 299174-parramatta-river / Parramatta River Catchment Group / Chair | 2015-09 → 2017-10 | 2015-09 → 2017-10 | 2015-09 → 2017-10 | reconciled |
| LAXALE, Jerome / 299174-statecover / StateCover Mutual Limited / Non-Executive Director and Risk Committee Chair | 2018-09-10 → 2022-06 | 2018-09 → 2022-06 | 2018-09-10 → 2022-06 | reconciled |
| LAXALE, Jerome / 299174-venture-cafe / Venture Café Sydney / Advisory Board member | 2018-07 → 2021-09 | 2018-07 → 2021-09 | 2018-07 → 2021-09 | reconciled |
| LEESER, Julian Martin / 109556-acu / Australian Catholic University / Director, Government Policy and Strategy; senior executive | 2012-07 → 2016 | 2012 → 2016 | 2012-07 → 2016 | reconciled |
| LEESER, Julian Martin / 109556-mallesons / Mallesons Stephen Jaques (now King & Wood Mallesons) / Solicitor; Executive Adviser | 2002 → 2004 | 2002 → 2004 | 2002 → 2004 | reconciled |
| LIM, Sam / 300130-01 / Royal Malaysia Police / Police constable | 1980 → 1981 | 1980-06 → 1981-12 | 1980-06 → 1981-12 | reconciled |
| MASCARENHAS, Zaneta Felice Antoinetta / 298800-14 / The Climate Reality Project / Presenter | 2009 → 2022 | 2018 → 2020 | 2009 → 2022 | held_conflict |
| MILLER-FROST, Louise Jane / 296272-04 / City of Port Adelaide Enfield / Director, Community Development | 2010-01 → 2012-02 | 2010-01 → 2012-02 | 2010-01 → 2012-02 | reconciled |
| MILLER-FROST, Louise Jane / 296272-05 / City of Burnside / General manager, Community and Development; Corporate Services | 2012-02 → 2017-03 | 2012-02 → 2017-04 | 2012-02 → 2017-03 | held_conflict |
| MILLER-FROST, Louise Jane / 296272-07 / St Vincent de Paul Society (SA) Inc. / Chief executive officer | 2020-03-10 → 2021-09 | 2020-03 → 2021-09 | 2020-03-10 → 2021-09 | reconciled |
| MILLER-FROST, Louise Jane / 296272-10 / Therapeutic Goods Administration, Advisory Committee on Vaccines / Committee member | 2017 → 2018 | 2017-01 → 2018-12 | 2017-01 → 2018-12 | reconciled |
| MILLER-FROST, Louise Jane / 296272-25 / Belair Primary School / Governing Council member | ? → ? | 2023-09 → Present | 2023-09 → ? | reconciled |
| MULINO, the Hon. Dr Daniel / 132880-08 / Nous Group / Senior consultant | 2008-06 → 2010-11 | 2008-06 → 2010-11 | 2008-06 → 2010-11 | reconciled |
| MULINO, the Hon. Dr Daniel / 132880-09 / Pottinger / Director, Policy | 2012-09 → 2014-04 | 2012-09 → 2014-04 | 2012-09 → 2014-04 | reconciled |
| McBAIN, the Hon. Kristy Louise / 281988-clark-rideaux / Clark Rideaux Lawyers / Senior Associate | 2009-07 → 2013-02 | 2009-07 → 2013-02 | 2009-07 → 2013-02 | reconciled |
| McBAIN, the Hon. Kristy Louise / 281988-symons-phillips / Symons Phillips Lawyers / Associate | 2009-01 → 2009-07 | 2009-01 → 2009-07 | 2009-01 → 2009-07 | reconciled |
| McCARTHY, the Hon. Malarndirri Barbara Anne / 122087-07 / Malarndirri Media / Freelance journalist | 2016-04 → 2016 | 2016-04 → 2016-06 | 2016-04 → 2016-06 | reconciled |
| McCORMACK, the Hon. Michael Francis / 219646-daily-editor / The Daily Advertiser / Riverina Media Group / Editor | 1992-03-01 → 2002-02 | 1992 → 2002 | 1992-03-01 → 2002-02 | reconciled |
| McCORMACK, the Hon. Michael Francis / 219646-riverina-group-editor / Riverina Media Group / Group Editor | 1996 → 2002-02 | 1996 → 2002 | 1996 → 2002-02 | reconciled |
| McKENZIE, the Hon. Bridget / 207825-04 / Monash University, Faculty of Education, Gippsland campus / Lecturer; professional-experience unit coordinator | 2009 → 2010 | 2008 → 2010 | 2009 → 2010 | held_conflict |
| NAMPIJINPA PRICE, Jacinta / 263528-03 / Yangapi Productions Pty Ltd / Co-founder and executive director | 2014-08 → 2019-06 | 2014-08 → 2019-06 | 2014-08 → 2019-06 | reconciled |
| O'BRIEN, Edward (Ted) Lynam / 138932-06 / Barton Deakin (Queensland) / Managing Director | 2011-11 → 2012-11 | 2011-11 → 2012-11 | 2011-11 → 2012-11 | reconciled |
| O'BRIEN, Edward (Ted) Lynam / 138932-07 / Ted O'Brien & Associates / Visible Hand Consulting (Edward Lynam O'Brien, sole trader) / Managing Director / consultant | 2014-02 → ? | 2014-02 → Present | 2014-02 → ? | reconciled |
| O'NEIL, the Hon. Clare Ellen / 140590-11 / Springvale Community Aid and Advice Bureau Incorporated / Board member | 2002 → 2006 | 2002 → 2006 | 2002 → 2006 | reconciled |
| O'SULLIVAN, Matt / 283585-02 / Terravision Pty Ltd / Electronic technician | 1996-01 → 1999-12 | 1996-01 → 1999-12 | 1996-01 → 1999-12 | reconciled |
| O'SULLIVAN, Matt / 283585-05 / Garden City Christian Church / Youth leader | 2003 → 2007 | 2003-01 → 2008-07 | 2003 → 2007 | held_conflict |
| PENFOLD, Alison Louise / 248895-littleproud-office / Office of the Hon. David Littleproud MP / Chief of Staff | ? → ? | 2018-05 → 2019-06 | 2018-05 → 2019-06 | reconciled |
| PENFOLD, Alison Louise / 248895-truss-office / Office of the Hon. Warren Truss MP / Political staff member (exact progression unresolved) | ? → ? | 1999 → 2004 | 1999 → 2004 | reconciled |
| PENFOLD, Alison Louise / 248895-vaile-staff / Office of the Hon. Mark Vaile MP / Political staff member (exact progression unresolved) | 2004 → 2006 | 2004 → 2006 | 2004 → 2006 | reconciled |
| PENFOLD, Alison Louise / 248895-woolworths / Woolworths Group / Government Relations Manager; observed acting Head of Government Relations | 2016-12 → 2018-03 | 2016-12 → 2018-03 | 2016-12 → 2018-03 | reconciled |
| PHILLIPS, Fiona Evon / 147140-shoalhaven-council / Shoalhaven City Council / Human Resources Officer | 1996 → 1997 | 1996 → 1997 | 1996 → 1997 | reconciled |
| PHILLIPS, Fiona Evon / 147140-uow / University of Wollongong, Shoalhaven Campus / Commerce Tutor teaching management, finance and leadership | 2002 → 2015 | 2002 → 2015-10 | 2002 → 2015-10 | reconciled |
| REBELLO, Leon / 316547-08 / King & Wood Mallesons / Summer clerk | 2016-11 → 2017-02 | 2016-11 → 2017-02 | 2016-11 → 2017-02 | reconciled |
| ROWLAND, the Hon. Michelle Anne / 159771-parklands-trust / Western Sydney Parklands Trust / Non-executive director | 2007 → 2010-07-07 | 2007 → 2010 | 2007 → 2010-07-07 | reconciled |
| RUSTON, the Hon. Anne Sowerby / 243273-01 / Office of Peter Arnold MP, South Australian Parliament / Electorate officer | 1987 → 1993 | 2022-06 → Present | 1987 → 1993 | held_conflict; closed end retained |
| RYAN, Monique Marie / 297660-17 / University of Melbourne / Honorary clinical professor | ? → ? | 2016-04 → 2021-12 | 2016-04 → 2021-12 | reconciled |
| RYAN, Monique Marie / 297660-18 / Monash University / Adjunct clinical professor | ? → ? | 2016-01 → 2021-12 | 2016-01 → 2021-12 | reconciled |
| RYAN, Monique Marie / 297660-19 / Murdoch Children’s Research Institute / Honorary fellow manager | ? → 2021 | 2006-06 → 2021-12 | 2006-06 → 2021-12 | reconciled |
| SCARR, Paul Martin / 282997-06 / Mallesons Stephen Jaques, now King & Wood Mallesons, Brisbane / Senior associate | 2005 → 2007 | 2005 → 2007 | 2005 → 2007 | reconciled |
| SHARMA, Devanand (Dave) Noel / 274506-pmc / Department of the Prime Minister and Cabinet / Assistant Secretary and acting First Assistant Secretary, International Division | 2010-01 → 2012 | 2010-01 → 2012-01 | 2010-01 → 2012-01 | reconciled |
| SMITH, David Philip Benedict / 276714-03 / Slough Borough Council, United Kingdom / Council employee — public-service improvement targets | 2001 → 2002 | 2001 → 2002 | 2001 → 2002 | reconciled |
| SMITH, Dean Anthony / 241710-05 / Office of Minister for Justice and Customs / Special adviser | 2002 → 2002 | 2002 → 2002-10 | 2002 → 2002-10 | reconciled |
| STEGGALL, Zali, OAM / 175696-05 / Olympic Winter Institute of Australia / Independent non-executive director, later term | 2013-11-22 → 2019-05-27 | 2014 → 2019-05 | 2013-11-22 → 2019-05-27 | held_conflict |
| STEGGALL, Zali, OAM / 175696-06 / Sport Australia Hall of Fame / Independent non-executive director | 2015 → ? | 2015-03 → 2019-05 | 2015-03 → 2019-05 | reconciled |
| STEGGALL, Zali, OAM / 175696-11 / NSW Bar Association / Councillor; health, sport and recreation committee chair | 2010 → 2013 | 2010 → 2013 | 2010 → 2013 | reconciled |
| STEGGALL, Zali, OAM / 175696-kemp-strang / Kemp Strang / Legal-practice role (title unresolved in accessible excerpt) | 2007-10 → 2008-04 | 2007-10 → 2008-04 | 2007-10 → 2008-04 | reconciled |
| STEGGALL, Zali, OAM / 175696-ski-snowboard-director / Ski and Snowboard Association of Australia / Director | 2002 → 2006 | 2002 → 2006 | 2002 → 2006 | reconciled |
| TAYLOR, the Hon. Angus James / 231027-01 / McKinsey & Company / Management consultant, later partner | 1994-03 → 2001-01 | 1994-03 → 2001-01 | 1994-03 → 2001-01 | reconciled |
| TAYLOR, the Hon. Angus James / 231027-03 / Port Jackson Partners / Director and strategy/business consultant | 2002-11 → 2013-07 | 2002-11 → 2013-07 | 2002-11 → 2013-07 | reconciled |
| TEESDALE, Jess / 314526-06 / Indie Education / Indie School Launceston, contract entity to verify / Teacher | ? → 2025 | 2024-02 → Present | 2024-02 → 2025 | reconciled; closed end retained |
| THISTLETHWAITE, the Hon. Matthew (Matt) James / 182468-03 / Australian Labor Party, NSW / General secretary | 2008-10 → 2010 | 2008-10 → 2010-08 | 2008-10 → 2010-08 | reconciled |
| THISTLETHWAITE, the Hon. Matthew (Matt) James / 182468-04 / Mallesons Stephen Jaques / Solicitor / senior consultant | 2010-09 → 2011-07 | 2010-09 → 2011-07 | 2010-09 → 2011-07 | reconciled |
| THWAITES, the Hon. Kate Lynne / 282212-01 / Australian Broadcasting Corporation / Television and radio news journalist | 2002 → 2008 | 2002-06 → 2008-09 | 2002-06 → 2008-09 | reconciled |
| THWAITES, the Hon. Kate Lynne / 282212-02 / Oxfam Australia / Media adviser / media coordinator | 2008 → 2010 | 2008-10 → 2010-10 | 2008-10 → 2010-10 | reconciled |
| THWAITES, the Hon. Kate Lynne / 282212-08 / National Disability Insurance Agency / Director, media and communications | 2015-07 → 2015-11 | 2015-07 → 2015-11 | 2015-07 → 2015-11 | reconciled |
| VIOLI, Aaron / 300147-06 / Office of Senator James Paterson / Electorate officer / adviser | 2016-03 → 2016-09 | 2016-03 → 2016-09 | 2016-03 → 2016-09 | reconciled |
| WALKER, Charlotte Grace / 316818-01 / Drakes Supermarkets (profile label; earlier local operator to verify) / Casual retail assistant | 2018-10 → 2022-10 | 2018-10 → 2022-10 | 2018-10 → 2022-10 | reconciled |
| WALKER, Charlotte Grace / 316818-04 / Health Partners, South Australian mutual insurer (Health Partners Limited; individual contract not seen) / Customer Experience Support | 2023-12 → 2024-06 | 2023-12 → 2024-06 | 2023-12 → 2024-06 | reconciled |
| WALLACE, Andrew Bruce / 265967-08 / Sunshine Coast Children's Therapy Centre / President | ? → ? | 2009-01 → 2011-09 | 2009-01 → 2011-09 | reconciled |
| WATT, the Hon. Murray Patrick / 245759-03 / Federal Court of Australia / Associate to the Hon. Peter Gray | 1999 → 2000 | 1999-06 → 2000-06 | 1999-06 → 2000-06 | reconciled |
| WATT, the Hon. Murray Patrick / 245759-09 / Maurice Blackburn Lawyers / Senior associate | 2012 → 2016 | 2012-10 → 2016-06 | 2012-10 → 2016-06 | reconciled |
| WATTS, the Hon. Timothy (Tim) Graham / 193430-01 / Mallesons Stephen Jaques / Solicitor | 2003-02 → 2005-02 | 2003-02 → 2005-02 | 2003-02 → 2005-02 | reconciled |
| WATTS, the Hon. Timothy (Tim) Graham / 193430-02 / Office of Senator Stephen Conroy / Deputy chief of staff | 2005-02 → 2007-07 | 2005-02 → 2007-07 | 2005-02 → 2007-07 | reconciled |
| WELLS, the Hon. Anika Shay / 264121-04 / Maurice Blackburn Lawyers / Lawyer specialising in workers' compensation and road-injury matters | 2014-08 → 2019-05 | 2014-08 → 2019-05 | 2014-08 → 2019-05 | reconciled |
| WHITEAKER, Ellie / 316555-05 / Australian Manufacturing Workers Union / Organiser | 2013-03 → 2016-07 | 2013-03 → 2016-07 | 2013-03 → 2016-07 | reconciled |
| WHITEAKER, Ellie / 316555-06 / Office of Senator Louise Pratt / Electorate officer | 2016-07 → 2018-05 | 2016-07 → 2018-05 | 2016-07 → 2018-05 | reconciled |
| WILLCOX, Andrew / 286535-10 / Koorelah Farms; employing/trustee legal entity to confirm / Managing director | 1996 → 2010 | 1996 → 2010 | 1996 → 2010 | reconciled |
| WILSON, the Hon. Timothy (Tim) Robert / IMW-04 / Australian APEC Study Centre, then associated with Monash University / Development project manager | 2004 → 2006-04 | 2004 → 2006 | 2004 → 2006-04 | reconciled |
| WILSON, the Hon. Timothy (Tim) Robert / IMW-11 / Australian Human Rights Commission / Human Rights Commissioner | 2014-02-17 → 2016-02-19 | 2014 → 2016 | 2014-02-17 → 2016-02-19 | reconciled |
| WILSON, the Hon. Timothy (Tim) Robert / IMW-14 / Dynamic Sunrise Consulting / Principal consultant between parliamentary terms | 2022 → 2025 | 2022-05 → 2025-05 | 2022-05 → 2025-05 | reconciled |
| WILSON, the Hon. Timothy (Tim) Robert / IMW-16 / Alfred Health / Board director | 2011 → 2014-06-30 | 2011 → 2014 | 2011 → 2014-06-30 | reconciled |
| WITTY, Sarah / 316660-13 / UDIA Victoria / Awards for Excellence submissions committee | 2019-04 → 2019-12 | 2019-04 → 2019-12 | 2019-04 → 2019-12 | reconciled |
| WITTY, Sarah / 316660-15 / Permanent Care and Adoptive Families / Non-executive director | 2019-10 → ? | 2019-10 → Present | 2019-10 → ? | reconciled |
| WITTY, Sarah / 316660-16 / Yarra City Council / Business Advisory Group member | 2019-10 → ? | 2019-10 → Present | 2019-10 → ? | reconciled |
| YOUNG, Terry James / 201906-02 / James Saddlery, Brendale / Factory hand | 1984 → 1984 | 1984-03 → 1984-06 | 1984-03 → 1984-06 | reconciled |
| YOUNG, Terry James / 201906-03 / Glenfords Power Tools / Storeperson and sales assistant | 1984 → 1986 | 1984-07 → 1986-01 | 1984-07 → 1986-01 | reconciled |
| YOUNG, Terry James / 201906-04 / Errol Stewarts, Strathpine / Sales assistant | 1986 → 1988 | 1986-01 → 1988-12 | 1986-01 → 1988-12 | reconciled |
| YOUNG, Terry James / 201906-11 / The Good Guys, Morayfield / Joint-venture partner and managing director | 2001-08 → 2007-01 | 2001-08 → 2007-01 | 2001-08 → 2007-01 | reconciled |

## Unassigned ranges

| Member ID / candidate appointment | Indexed dates | Reason |
|---|---|---|
| 26417 / 26417-acf | 2006 → 2009 | Different or unidentified appointment at the same organisation. |
| 282997 / 282997-02 | 1992 → 2005 | Employer-wide range spans several existing Allens appointments. |
| 274506 / 274506-dfat-graduate | 1999-02 → 2017-12 | Employer-wide range spans several diplomatic postings. |
| 281688 / 281688-06 | 2011 → 2025-08 | Range spans executive and later patron roles. |
| 300006 / 300006-02 | 2016-07 → 2016-12 | Indexed interval does not establish the same existing appointment. |
| 62329 / 62329-colly-farm | 1983-01 → 2000-01 | Employer-wide range spans operational and chief-executive roles. |
| 260805 / 260805-02 | 2003-01 → 2005-12 | ADFA subperiod cannot replace combined ADFA and Duntroon chronology. |
| HWA / HWA-07 | 2001 → 2007 | Organisation range does not isolate representative and training appointments. |
| 266499 / 266499-04 | 2002-10 → 2002-12 | Range may describe a subrole within combined manager/key-account record. |
| 282335 / 282335-04 | 2015-03 → 2019-03 | Several university appointments; range lacks a discrete role locator. |
| 91219 / 91219-cepu-leadership | 2006 → 2010 | Several union offices; range lacks a discrete role locator. |
| 138932 / 138932-05 | 2001-01 → 2011-11 | Employer-wide range does not isolate component appointments. |
| 248895 / 248895-mills-senior-policy-adviser | 2009-03 → 2011-09 | Combined staff range crosses a documented promotion. |
| 243273 / 243273-05 | 1996 → 2002 | Wine-centre range does not isolate planning work from CEO appointment. |
| 282997 / 282997-07 | 2007-02 → 2019-02 | PanAust range spans separately coded ownership/control spells. |
| 243273 / 243273-06 | 2003 → 2015 | Business range spans active operator and later continuing ownership. |
| 276714 / 276714-05 | 2004 → 2007 | Employer date range and existing role boundary require scope review. |
| 175696 / 175696-10 | 2010 → 2019-05 | Organisation range does not identify the existing tribunal appointment. |
| 201906 / 201906-09 | 1997-01 → 2001-01 | Philips range does not isolate subsidiary/role appointments. |
| 274506 / 274506-swg | 2023-02 → 2023-12 | Director/partner boundaries require scope review. |
| 241710 / 241710-09 | 2009 → 2010 | Employer range and existing role boundary require scope review. |
| 241710 / 241710-10 | 2010 → 2012-04 | Company range and ownership/consulting boundary require scope review. |
| 316101 / 316101-08 | 2022-11 → 2025-05 | Combined principal/special-counsel range does not identify promotion boundaries. |
