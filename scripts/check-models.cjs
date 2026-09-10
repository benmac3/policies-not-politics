// Exercise actual calculator functions without a browser or external dependencies.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const path=require('path'),root=path.join(__dirname,'..');
const data={};for(const name of ['observations','sources','countries','claims','panel','metrics','budget','extensions','parliament'])data[name]=JSON.parse(fs.readFileSync(path.join(root,'data',name+'.json')));
const elements={};const el=id=>elements[id]??={value:'',innerHTML:'',dataset:{},addEventListener(){},classList:{toggle(){}}};
const ctx={DATA:data,document:{querySelector:el,querySelectorAll:()=>[]},window:{addEventListener(){},scrollTo(){}},location:{hash:'#dashboard'},console};
vm.createContext(ctx);
// Reserve the browser's unforgeable Window names. Node VM does not enforce
// browser global-property restrictions, so use lexical reservations here.
vm.runInContext('const top = null, window = globalThis.window, location = globalThis.location, document = globalThis.document;',ctx);
vm.runInContext(fs.readFileSync(path.join(root,'dist/app.js'),'utf8'),ctx);
for(const route of ['dashboard','learn','countries','ndis','scenarios','representatives','evidence']){
  const html=vm.runInContext(route+'()',ctx);assert(html.includes('<h1>'));assert(!html.includes('undefined'));
}
for(const [id,value]of Object.entries({'saving':'1','interest':'0','debt-years':'10','debt-share':'100'}))el('#'+id).value=value;
vm.runInContext('debt()',ctx);assert(el('#debt-result').innerHTML.includes('$10.00bn less debt'));
el('#interest').value='4';vm.runInContext('debt()',ctx);assert(el('#debt-result').innerHTML.includes('$12.01bn less debt'));
el('#debt-share').value='0';vm.runInContext('debt()',ctx);assert(el('#debt-result').innerHTML.includes('$0.00bn less debt'));
el('#saving').value='-1';vm.runInContext('debt()',ctx);assert(el('#debt-result').innerHTML.includes('Enter valid'));
for(const[id,value]of Object.entries({'growth-a':'0','growth-b':'0','years':'20'}))el('#'+id).value=value;
vm.runInContext('growth()',ctx);assert(el('#growth-output').innerHTML.includes('<strong>100.0</strong>'));
el('#growth-a').value='0.5';el('#growth-b').value='1.5';vm.runInContext('growth()',ctx);assert(el('#growth-output').innerHTML.includes('21.9% higher'));
el('#years').value='1.2';vm.runInContext('growth()',ctx);assert(el('#growth-output').innerHTML.includes('whole number'));
el('#country-search').value='Australia';el('#country-scope').value='all';vm.runInContext('countryTable()',ctx);assert(el('#country-table').innerHTML.includes('Australia'));assert(el('#country-history').innerHTML.includes('2000'));
el('#panel-metric').value='GC.DOD.TOTL.GD.ZS';el('#panel-year').value='2025';vm.runInContext('countryTable()',ctx);assert(el('#country-table').innerHTML.includes('Not available'));
el('#rep-search').value='ALBANESE';el('#rep-chamber').value='all';vm.runInContext('repList()',ctx);assert(el('#rep-list').innerHTML.includes('Bank officer'));
const broken=vm.runInContext("lineChart([{name:'gap',values:[1,null,3]}],['2000','2001','2002'])",ctx);assert(!broken.includes('NaN'));assert((broken.match(/<polyline/g)||[]).length===2);
el('#claim-search').value='unlikely-nonexistent-key';vm.runInContext('claimList()',ctx);assert(el('#claims-list').innerHTML.includes('No claims match'));
console.log('PASS: seven view templates, finance and productivity edge cases, missing data and search');
