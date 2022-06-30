$(document).ready(function () {

  $(".plant").each(function () {

    const months = {
      Jan: '01',
      Feb: '02',
      Mar: '03',
      Apr: '04',
      May: '05',
      Jun: '06',
      Jul: '07',
      Aug: '08',
      Sep: '09',
      Oct: '10',
      Nov: '11',
      Dec: '12',
    }

    let dbHarvestDate = $(this).find('.harvest-time').text().split(' ');
    let hMonth = dbHarvestDate[0].slice(0, -1);
    let hDay = dbHarvestDate[1].slice(0, -1);
    let hYear = dbHarvestDate[2].slice(0, -1);
    hHoursMins = dbHarvestDate[3].split(':');
    let hHour = hHoursMins[0];
    let hMinute = hHoursMins[1];
    let hSec = hHoursMins[2];
    let hDate = new Date(hYear, months[hMonth] - 1, hDay, hHour, hMinute, hSec);

    let dbPlantDate = $(this).find('.plant-time').text().split(' ');
    let pMonth = dbPlantDate[0].slice(0, -1);
    let pDay = dbPlantDate[1].slice(0, -1);
    let pYear = dbPlantDate[2].slice(0, -1);
    pHoursMins = dbPlantDate[3].split(':');
    let pHour = pHoursMins[0];
    let pMinute = pHoursMins[1];
    let pSec = pHoursMins[2];
    let pDate = new Date(pYear, months[pMonth] - 1, pDay, pHour, pMinute, pSec);

    let bar = $(this).find('.progressContainer');
    let harv = $(this).find('.progressHarvestContainer');

    var start = pDate;
    var end = hDate;

    updateTimer();

    function updateTimer() {
      setInterval(addFrame, 1000);
    }

    function addFrame() {

      var today = new Date();

      var timeBetweenStartAndEnd = (end - start);
      var timeBetweenStartAndToday = (today - start);

      var p = Math.round(timeBetweenStartAndToday / timeBetweenStartAndEnd * 100);

      if (p < 100) {
        harv.hide();
        bar.html(p + '%');
      } else {
        bar.hide();
        harv.show();
      }

    }

  });

});