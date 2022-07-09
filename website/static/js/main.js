const select1 = document.getElementById('vote1');
const select2 = document.getElementById('vote2');


select1.addEventListener('click', () => {
  document.getElementById('vote1').classList.toggle('active');
  if (document.getElementById('vote2').classList.contains('active')){
    document.getElementById('vote2').classList.remove('active')
  }
});

select2.addEventListener('click', () => {
  document.getElementById('vote2').classList.toggle('active');
  if (document.getElementById('vote1').classList.contains('active')){
    document.getElementById('vote1').classList.remove('active')
  }
});

