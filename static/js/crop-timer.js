$(document).ready(function () {

    let dbHarvestDate = $('#harvest-time').text().split(' ');

    const month = dbHarvestDate[0].slice(0, -1);
    const day = dbHarvestDate[1].slice(0, -1);
    const year = dbHarvestDate[2].slice(0, -1);
    hoursMins = dbHarvestDate[3].split(':');
    const hour = hoursMins[0];
    const minute = hoursMins[1];

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

    const date = new Date(year, months[month] -1, day, hour, minute);


      


});