const {Builder,By, Browser} = require('selenium-webdriver');
const ExcelJs = require('exceljs');

let oldFile = './old-file.xlsx';

(async function helloSelenium() {
  let driver = await new Builder().forBrowser(Browser.CHROME).build();

  let data = []
    const workbook = new ExcelJs.Workbook();
    await workbook.xlsx.readFile(oldFile);
    const sheet = workbook.getWorksheet(1);
    
    let flag = 1;
    for(let i=2 ; i<= sheet.rowCount; i++) {
        const row = sheet.getRow(i);
        let url = row.getCell(1).value.text;
        let name = row.getCell(2).value;
        let price = row.getCell(3).value;
        let desc = row.getCell(4).value;
        let imagesUrls = row.getCell(5).value;

        // opening the urls
        console.log(">".repeat(50));
        console.log(`Opening url number: ${flag} ...`);
        console.log(`url: ${url}`);
        console.log(`name: ${name}`);
        await driver.get(url);

        // const title = await driver.findElement(By.css('section h1')).getText();
        
        let saledTimes;
        try {
            let s = await driver.findElement(By.className('lang')).getText();
            saledTimes = s.replace(/[^0-9]/g, '');
        } catch (error) {
            saledTimes = 'لا يوجد تفاصيل';
            console.log("can't find saled times for this item");
        }
        
        console.log(`saledTimes: ${saledTimes}`);
        // sleep(1000);
        let progress= (flag / sheet.rowCount) * 100
        console.log(`[progress][${'>'.repeat(Math.round(progress/2))}][${Math.ceil(progress)}%]`);
        flag++;

        // let saledTimes = row.getCell(6).value = "اختبار";
        let obj = [url, name, price, desc, imagesUrls, saledTimes];
        data.push(obj);
    }

    
    await writeDataToFile(data);
      
  console.log('='.repeat(50));
  console.log('exiting the broswer ...');
  
  await driver.quit();
})();

async function writeDataToFile(data) {
    // writing the data to new file
    const newWorkBook = new ExcelJs.Workbook();
    const newSheet = newWorkBook.addWorksheet('Scraped Data');
    newSheet.columns = [
        {header: 'رابط المنتج', key: 'الرابط', width: 20},
        {header: 'اسم المنتج', key: 'اسم المنتج', width: 20},
        {header: 'السعر', key: 'السعر', width: 20},
        {header: 'الوصف', key: 'الوصف', width: 20},
        {header: 'روابط الصور', key: 'روابط الصور', width: 20},
        {header: 'عدد مرات الشراء', key: 'عدد مرات الشراء', width: 20},
    ]

    data.forEach(item => {
        newSheet.addRow(item);
    });

    // newSheet.addRows(JSON.parse(data));
    console.log('writing data to new File');
    
    await newWorkBook.xlsx.writeFile(`data-${Date.now()}.xlsx`); 
}
const sleep = ms => new Promise( resolve => setTimeout(resolve, ms));
