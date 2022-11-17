
extern crate reqwest;
extern crate scraper;
use std::{error::Error, fs::OpenOptions};
use csv::Writer;
use scraper::{Html, Selector};

fn main(){
    println!("Welcome! The data we are going to get is: ");
    scrape_team_data("https://crypto.com/price");
}

fn scrape_team_data(url:&str){

    let mut req = reqwest::get(url).unwrap();
    assert!(req.status().is_success());
    let doc_body = Html::parse_document(&req.text().unwrap());

    // let team = Selector::parse(".chakra-text.css-rkws3").unwrap();
    let cryptoname = Selector::parse(".chakra-text.css-rkws3").unwrap();
    let cryptoprice = Selector::parse(".css-16q9pr7").unwrap();
    let change24h = Selector::parse(".css-1b7j986").unwrap();
    let volumeandmarktcap= Selector::parse(".css-1nh9lk8").unwrap();
    let mut column1: Vec<&str> = Vec::new();
    let mut column2: Vec<&str> = Vec::new();
    let mut column3: Vec<&str> = Vec::new();
    let mut temp_: Vec<&str> = Vec::new();
    let mut column4: Vec<&str> = Vec::new();
    let mut column5: Vec<&str> = Vec::new();

    let mut final_: Vec<&str> = Vec::new();
    for cryptoname in doc_body.select(&cryptoname){
        let cryptonames = cryptoname.text().collect::<Vec<_>>();
        column1.push(cryptonames[0])
 
    };
    for cryptoprice in doc_body.select(&cryptoprice){
        let cryptoprices = cryptoprice.text().collect::<Vec<_>>();
        column2.push(cryptoprices[0])
 
    };
    for change24h in doc_body.select(&change24h){
        let change24hs = change24h.text().collect::<Vec<_>>();
        if change24hs.len() == 2{
            column3.push(change24hs[1])
        }

        if change24hs.len() == 1{
            let ch = change24hs[0].chars().nth(0).unwrap();
            if ch == '.' {
                print!("")
            }
            else  if change24hs.len() == 1{
                column3.push(change24hs[0])
            }
        }
    }
    for volumeandmarktcap in doc_body.select(&volumeandmarktcap){
        let volumeandmarktcaps = volumeandmarktcap.text().collect::<Vec<_>>();
        temp_.push(volumeandmarktcaps[0])
     
        };
    for item in temp_.iter().step_by(2) {
        column4.push(item)
        
        }
    for item in temp_.iter().skip(1).step_by(2) {
        column5.push(item)
        };  
        let mut n = 0;
        let mut count = 0;

     
        for i in &column1 {
            if count == 0{
                writeheader();
                count = count + 1
            }
            else{
            writerow(column1[n],column2[n],column3[n],column4[n],column5[n]);
            n = n + 1;
        }
        }
   
}

fn writeheader() -> Result<(), Box<dyn Error>>{
    let mut file = OpenOptions::new()
    .write(true)
    .append(true)
    .open("foo.csv")
    .unwrap();
    let mut wtr = Writer::from_writer(file);
    wtr.write_record(&["Name","Price","24h Change","24h volume","Market Cap"])?;
    wtr.flush()?;
    Ok(())
}
fn writerow(col1:&str,col2:&str,col3:&str,col4:&str,col5:&str) -> Result<(), Box<dyn Error>> {
    let mut file = OpenOptions::new()
    .write(true)
    .append(true)
    .open("foo.csv")
    .unwrap();
    let mut wtr = Writer::from_writer(file);
    wtr.write_record(&[&col1,&col2,&col3,&col4,&col5])?;
    wtr.flush()?;
    Ok(())
}