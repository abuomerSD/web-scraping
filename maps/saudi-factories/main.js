const {Builder, Browser} = require('selenium-webdriver');
let url = "https://www.google.com/maps/search/%D9%85%D8%B5%D8%A7%D9%86%D8%B9+%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9%E2%80%AD%E2%80%AD/@23.4513623,38.078165,1394172m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI0MTIxMC4wIKXMDSoASAFQAw%3D%3D";
(async function helloSelenium() {
  let driver = await new Builder().forBrowser(Browser.CHROME).build();

  console.log('Opening Browser ...');
  
  console.log('Opening Browser ...');
//   process.stdout.write('test');
  
  await driver.get(url);

  await driver.quit();
})();

