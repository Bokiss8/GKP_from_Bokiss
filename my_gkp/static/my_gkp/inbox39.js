


//const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views

//=======================================mousedown===============================================
//----------------------------------------------------------------------------
    document.querySelector('#indicator_gas').addEventListener('mousedown', () => {
      console.log(`work indicator gas post start`);
      location = 'indicator_gas';
      let servis = 'gas';
     // load_gkp(servis);

    });
//----------------------------------------------------------------------------
document.querySelector('#list_gas').addEventListener('mousedown', () => {
  console.log(`work list gas post start`);
  location = 'list_gas';
  let servis = 'gas';
 // load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#import_gas').addEventListener('mousedown', () => {
  console.log(`work import gas post start`);
  location = 'import_gas';
  let servis = 'gas';
 // load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#indicator_res_1').addEventListener('mousedown', () => {
  console.log(`work indicator res 1 start`);
  location = 'indicator_res_1';
  let servis = 'res';
  //load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#list_res_1').addEventListener('mousedown', () => {
  console.log(`work list res 1 start`);
  location = 'list_res_1';
  let servis = 'gas';
 // load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#indicator_res_2').addEventListener('mousedown', () => {
  console.log(`work indicator res 2 start`);
  location = 'indicator_res_2';
  let servis = 'res';
  //load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#list_res_2').addEventListener('mousedown', () => {
  console.log(`work list res 2 start`);
  location = 'list_res_2';
  let servis = 'gas';
 // load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#indicator_res_3').addEventListener('mousedown', () => {
  console.log(`work indicator res 3 start`);
  location = 'indicator_res_3';
  let servis = 'res';
  //load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#list_res_3').addEventListener('mousedown', () => {
  console.log(`work list res 3 start`);
  location = 'list_res_3';
  let servis = 'gas';
 // load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#indicator_water').addEventListener('mousedown', () => {
  console.log(`work indicator water post start`);
  location = 'indicator_water';
  let servis = 'water';
  //load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#list_water').addEventListener('mousedown', () => {
  console.log(`work list water start`);
  location = 'list_water';
  let servis = 'water';
 // load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#indicator_rent').addEventListener('mousedown', () => {
  console.log(`work rent post start`);
  location = 'rent';
  let servis = 'gas';
 // load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#trash').addEventListener('mousedown', () => {
  console.log(`work trash post start`);
  location = 'trash';
  let servis = 'gas';
 // load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#internet').addEventListener('mousedown', () => {
  console.log(`work internet post start`);
  location = 'internet';
  let servis = 'gas';
 // load_gkp(servis);

});
//=======================================touchstart===============================================
//----------------------------------------------------------------------------
document.querySelector('#indicator_gas').addEventListener('touchstart', () => {
  console.log(`work indicator gas post start`);
  location = 'indicator_gas';
  let servis = 'gas';
 // load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#list_gas').addEventListener('touchstart', () => {
console.log(`work list gas post start`);
location = 'list_gas';
let servis = 'gas';
// load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#import_gas').addEventListener('touchstart', () => {
console.log(`work import gas post start`);
location = 'import_gas';
let servis = 'gas';
// load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#indicator_res_1').addEventListener('touchstart', () => {
console.log(`work indicator res 1 start`);
location = 'indicator_res_1';
let servis = 'res';
//load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#list_res_1').addEventListener('touchstart', () => {
console.log(`work list res 1 start`);
location = 'list_res_1';
let servis = 'gas';
// load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#indicator_res_2').addEventListener('touchstart', () => {
console.log(`work indicator res 2 start`);
location = 'indicator_res_2';
let servis = 'res';
//load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#list_res_2').addEventListener('touchstart', () => {
console.log(`work list res 2 start`);
location = 'list_res_2';
let servis = 'gas';
// load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#indicator_res_3').addEventListener('touchstart', () => {
console.log(`work indicator res 3 start`);
location = 'indicator_res_3';
let servis = 'res';
//load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#list_res_3').addEventListener('touchstart', () => {
console.log(`work list res 3 start`);
location = 'list_res_3';
let servis = 'gas';
// load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#indicator_water').addEventListener('touchstart', () => {
console.log(`work indicator water post start`);
location = 'indicator_water';
let servis = 'water';
//load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#list_water').addEventListener('touchstart', () => {
console.log(`work list water start`);
location = 'list_water';
let servis = 'water';
// load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#indicator_rent').addEventListener('touchstart', () => {
console.log(`work rent post start`);
location = 'rent';
let servis = 'gas';
// load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#trash').addEventListener('touchstart', () => {
console.log(`work trash post start`);
location = 'trash';
let servis = 'gas';
// load_gkp(servis);

});
//----------------------------------------------------------------------------
document.querySelector('#internet').addEventListener('touchstart', () => {
console.log(`work internet post start`);
location = 'internet';
let servis = 'gas';
// load_gkp(servis);

});
//=======================================other===============================================
//----------------------------------------------------------------------------
document.querySelector('#gas').addEventListener('touchstart', () => {
console.log(`work gas click start`);
document.querySelector('.menu_li > .menu_ul').style.display = 'block';
  //alert ("Hello World!");
    
});
//----------------------------------------------------------------------------
document.querySelector('#res').addEventListener('touchstart', () => {
console.log(`work res click start`);
document.querySelector('.menu_li > .menu_ul').style.display = 'block';
    //alert ("Hello World!");
      
});
//----------------------------------------------------------------------------
document.querySelector('#water').addEventListener('touchstart', () => {
console.log(`work water click start`);
document.querySelector('.menu_li > .menu_ul').style.display = 'block';
//alert ("Hello World!");
  
});
//----------------------------------------------------------------------------
document.querySelector('#home').addEventListener('mousedown', () => {
      //console.log(`work following post start`);
     
     // load_posts(global_posts);

});
//----------------------------------------------------------------------------
//document.querySelector('.submit').addEventListener('mousedown', () => {
  //console.log(`work following post start`);
 // document.querySelector('h2').innerHTML = `Внесення показників лічильника по газу`;
 // load_posts(global_posts);

//});
    

  });
  //----------------------------------------------------------------------------
  //function load_gkp(servis) {

   
    // console.log(`work ${posts} start`);
     // Show the category posts and hide other views
    // if (servis == 'gas'){
  
    //   document.querySelector('h2').innerHTML = `Внесення показників лічильника по газу`;
    // } else if (servis == 'res'){
      
    //   document.querySelector('h2').innerHTML = `Внесення показників лічильника по електроенергії`;
    // } else if (posts == 'following'){
       
    //   document.querySelector('h2').innerHTML = `<h3>Following</h3> <hr>`;
   //  } else {
    //   
   //    document.querySelector('h2').innerHTML = `такої послуги не існує!`;
   //  } 

   // }
 