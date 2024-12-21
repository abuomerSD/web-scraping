const {Builder, Browser, By} = require('selenium-webdriver');

(async function helloSelenium() {
  let driver = await new Builder().forBrowser(Browser.CHROME).build();
  let url = 'https://www.google.com/maps/search/%D9%85%D8%B5%D8%A7%D9%86%D8%B9+%D8%A7%D9%84%D9%83%D9%88%D9%8A%D8%AA%E2%80%AD/@28.8753334,47.2053136,187148m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI0MTIwOS4wIKXMDSoASAFQAw%3D%3D';
  let saudiUrl = 'https://www.google.com/maps/search/%D9%85%D8%B5%D8%A7%D9%86%D8%B9+%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9%E2%80%AD%E2%80%AD/@23.4513623,38.078165,1394172m/data=!3m2!1e3!4b1?entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D';

  console.log('Openning the browser...');
  
  await driver.get(saudiUrl);
  
  let flag =1;
  // scrolling the page
  console.log('scrolling the page');
  console.log('='.repeat(50));
  await driver.executeScript(pageScroll)

  let data = []
  // get all results data 
  let results = await driver.findElements(By.css('.lI9IFe'));
  // console.log(results);
  
  // console.log(results);

  for(let result of results) {
    let title = await result.findElement(By.css('.qBF1Pd.fontHeadlineSmall ')).getText();
    let phone;
    let website ;
    try {
      phone = await result.findElement(By.css('.UsdlK')).getText();
      website = await result.findElement(By.css(".lcr4fd.S9kvJb")).getText();
    } catch (error) {
      console.log("can't find some data for this place");
      website = 'لا يوجد';
      phone = 'لا يوجد';
    }
    console.log(await title);
    console.log(await phone);
    console.log(await website);
    console.log('='.repeat(50));
    
  }

  // closing the browser
  await driver.quit();
})();


// to scroll the results to get more items
function pageScroll() {
  let scrollableDiv = document.querySelector('div[role="feed"]');
          function scrollWithinElement(scrollableDiv) {
              return new Promise((resolve, reject) => {
                  var totalHeight = 0;
                  var distance = 1000;
                  var scrollDelay = 10000;
                  
                  var timer = setInterval(() => {
                      var scrollHeightBefore = scrollableDiv.scrollHeight;
                      scrollableDiv.scrollBy(0, distance);
                      totalHeight += distance;

                      if (totalHeight >= scrollHeightBefore) {
                          totalHeight = 0;
                          setTimeout(() => {
                              var scrollHeightAfter = scrollableDiv.scrollHeight;
                              if (scrollHeightAfter > scrollHeightBefore) {
                                  return;
                              } else {
                                  clearInterval(timer);
                                  resolve();
                              }
                          }, scrollDelay);
                      }
                  }, 200);
              });
          }

          return scrollWithinElement(scrollableDiv);
}

// function to delay the time
const delay = ms => new Promise(resolve => setTimeout(resolve, ms))