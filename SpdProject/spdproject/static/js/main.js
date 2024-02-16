document.querySelector('#check').addEventListener('click', check)

function check() {
  const month = document.getElementById('month').value
  const day = document.getElementById('day').value


  if (month == "Jan" && day < 20) {
    document.getElementById("capricorn").style.display = 'block';
  } else if (month == "Jan" && day >= 20) {
    document.getElementById("aquarius").style.display = 'block';
  } else if (month == "Feb" && day < 19) {
    document.getElementById("aquarius").style.display = 'block';
  } else if (month == "Feb" && day >= 19) {
    document.getElementById("pisces").style.display = 'block';
  } else if (month == "Mar" && day < 21) {
    document.getElementById("pisces").style.display = 'block';
  } else if (month == "Mar" && day >= 21) {
    document.getElementById("aries").style.display = 'block';
  } else if (month == "Apr" && day < 20) {
    document.getElementById("aries").style.display = 'block';
  } else if (month == "Apr" && day >= 20) {
    document.getElementById("taurus").style.display = 'block';
  } else if (month == "May" && day < 21) {
    document.getElementById("taurus").style.display = 'block';
  } else if (month == "May" && day >= 21) {
    document.getElementById("gemini").style.display = 'block';
  } else if (month == "Jun" && day < 22) {
    document.getElementById("gemini").style.display = 'block';
  } else if (month == "Jun" && day >= 22) {
    document.getElementById("cancer").style.display = 'block';
  } else if (month == "Jul" && day < 23) {
    document.getElementById("cancer").style.display = 'block';
  } else if (month == "Jul" && day >= 23) {
    document.getElementById("leo").style.display = 'block';
  } else if (month == "Aug" && day < 23) {
    document.getElementById("leo").style.display = 'block';
  } else if (month == "Aug" && day >= 23) {
    document.getElementById("virgo").style.display = 'block';
  } else if (month == "Sep" && day < 23) {
    document.getElementById("virgo").style.display = 'block';
  } else if (month == "Sep" && day >= 23) {
    document.getElementById("libra").style.display = 'block';
  } else if (month == "Oct" && day < 23) {
    document.getElementById("libra").style.display = 'block';
  } else if (month == "Oct" && day >= 23) {
    document.getElementById("scorpio").style.display = 'block';
  } else if (month == "Nov" && day < 22) {
    document.getElementById("scorpio").style.display = 'block';
  } else if (month == "Nov" && day >= 22) {
    document.getElementById("sagittarius").style.display = 'block';
  } else if (month == "Dec" && day < 22) {
    document.getElementById("sagittarius").style.display = 'block';
  } else if (month == "Dec" && day >= 22) {
    document.getElementById("capricorn").style.display = 'block';
  }
}
