$(document).ready(function () {

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

  let dbHarvestDate = $('#harvest-time').text().split(' ');
  const hMonth = dbHarvestDate[0].slice(0, -1);
  const hDay = dbHarvestDate[1].slice(0, -1);
  const hYear = dbHarvestDate[2].slice(0, -1);
  hHoursMins = dbHarvestDate[3].split(':');
  const hHour = hHoursMins[0];
  const hMinute = hHoursMins[1];
  const hDate = new Date(hYear, months[hMonth] - 1, hDay, hHour, hMinute).getTime();

  let dbPlantDate = $('#plant-time').text().split(' ');
  const pMonth = dbPlantDate[0].slice(0, -1);
  const pDay = dbPlantDate[1].slice(0, -1);
  const pYear = dbPlantDate[2].slice(0, -1);
  pHoursMins = dbPlantDate[3].split(':');
  const pHour = pHoursMins[0];
  const pMinute = pHoursMins[1];
  const pDate = new Date(pYear, months[pMonth] - 1, pDay, pHour, pMinute).getTime();

  // var Time = hDate.getTime() - pDate.getTime();
  // console.log(Time)
  //var Days = Time / (1000 * 3600 * 24); //Diference in Days
  //console.log(Days)


  var slider = document.getElementById("progressBar");
  var progressBar = document.getElementById("progress");


  // Get todays date and time
  // var now = new Date().getTime();

  // Find the distance between now and the count down date
  // var distanceWhole = hDate - pDate;
  // var distanceLeft = hDate - now;

  var start = dbPlantDate
  var end = dbHarvestDate
  var today = new Date().getTime; // April 23, 2015
  p = Math.round(((today - start) / (end - start)) * 100);
  // Update the progress bar
  //$('.bar').css("width", p).after().append(p);

  // Time calculations for minutes and percentage progressed
  // var minutesLeft = Math.floor(distanceLeft / (1000 * 60));
  // var minutesTotal = Math.floor(distanceWhole / (1000 * 60));
  // var progress = Math.floor(((minutesTotal - minutesLeft) / minutesTotal) * 100);


  window.onload = function () {
    setInterval(addFrame, 100);
  }

  function addFrame() {
    progressBar.style.width = p + "%";
    progressBar.innerHTML = p + "%";
  }

});