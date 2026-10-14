"""Optional browser smoke test. Requires Playwright and a local Chromium executable."""
from pathlib import Path
import json
import os
import shutil
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
    executable=os.environ.get('CHROMIUM_EXECUTABLE') or shutil.which('chromium') or shutil.which('chromium-browser')
    browser=p.chromium.launch(headless=True,executable_path=executable,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1440,'height':1300},device_scale_factor=1)
    errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    page.set_content((ROOT/'reviews/generated/federal-election-timeline.html').read_text(encoding='utf-8'))
    page.wait_for_selector('.eventrow')
    assert page.locator('.eventrow').count()==285
    assert page.locator('#detail h2').inner_text()=='2025 federal election'
    page.screenshot(path=str(ROOT/'review-desktop.png'),full_page=True)
    page.select_option('#kind','elections');assert page.locator('.eventrow').count()==54
    page.select_option('#kind','transfers');assert page.locator('.eventrow').count()==40
    page.fill('#search','Wentworth');assert page.locator('.eventrow').count()==1
    page.locator('.eventrow').first.click();assert 'LIB -1' in page.locator('#detail').inner_text()
    page.screenshot(path=str(ROOT/'review-by-election.png'),full_page=True)
    page.click('#reset');page.select_option('#kind','pm');assert page.locator('.eventrow').count()==38
    page.click('#reset');page.fill('#from','2010');page.locator('#from').dispatch_event('change')
    assert page.locator('.eventrow').count()>0
    assert page.locator('.eventrow').count()<285
    page.click('#reset');page.fill('#search','zzzz-no-event');assert page.locator('.eventrow').count()==0
    page.click('#reset');page.select_option('#kind','elections');page.fill('#search','2013');page.locator('.eventrow[data-id="general-2013"]').click()
    assert 'WA result later annulled' in page.locator('#detail').inner_text()
    page.click('#latest');assert page.locator('#detail h2').inner_text()=='2025 federal election'
    with page.expect_download() as download:
        page.click('#json')
    assert download.value.suggested_filename=='federal-election-timeline.json'
    page.click('#reset');page.set_viewport_size({'width':390,'height':844})
    page.screenshot(path=str(ROOT/'review-mobile.png'),full_page=True)
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
    assert not errors,errors
    report={'passed':True,'checks':15,'browser':'Chromium via Playwright','desktop':[1440,1300],'mobile':[390,844],'console_errors':errors,'tested':'initial render; category and year filters; transfer search; event selection; PM count; empty results; WA annulment; latest reset; JSON export; mobile overflow'}
    (ROOT/'reviews/generated/ui-test-report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    browser.close()
