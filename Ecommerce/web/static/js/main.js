


//========================================
//          HEADER SCROLL FIXED
//========================================
$(window).on("scroll", function(){
    var scrolling = $(this).scrollTop();
    // console.log(scrolling)
    if (scrolling > 130){
        $(".header-part").addClass("active");
    }else{
        $(".header-part").removeClass("active");
    }
});


//========================================
//          BACK TO TOP BUTTON
//========================================
$(window).on("scroll", function(){
    var scroll = $(this).scrollTop();
    if(scroll > 700){
        $(".backtop").show();
    }else{
        $(".backtop").hide();
    }
});


//========================================
//        DROPDOWN MENU FUNCTION
//========================================
$(function () {
    $(".dropdown-link").click(function() {
        $(this).next().toggle();
        $(this).toggleClass('active');
        if($('.dropdown-list:visible').length > 1) {
            $('.dropdown-list:visible').hide();
            $(this).next().show();
            $('.dropdown-link').removeClass('active');
            $(this).addClass('active');
        }
    }); 
});


//========================================
//       NAV SIDEBAR MENU ACTIVE
//========================================
$('.nav-link').on('click', function(){
    $('.nav-list li a').removeClass('active');
    $(this).addClass('active');
});


//========================================
//        CATEGORY SIDEBAR FUNCTION
//========================================
$('.header-cate, .cate-btn').on('click', function(){
    $('body').css('overflow', 'hidden');
    $('.category-sidebar').addClass('active');
    $('.category-close').on('click', function(){
        $('body').css('overflow', 'inherit');
        $('.category-sidebar').removeClass('active');
        $('.backdrop').fadeOut();
    });
});


//========================================
//         NAV SIDEBAR FUNCTION
//========================================
$('.header-user').on('click', function(){
    $('body').css('overflow', 'hidden');
    $('.nav-sidebar').addClass('active');
    $('.nav-close').on('click', function(){
        $('body').css('overflow', 'inherit');
        $('.nav-sidebar').removeClass('active');
        $('.backdrop').fadeOut();
    });
});


//========================================
//         CART SIDEBAR FUNCTION
//========================================
$('.header-cart, .cart-btn').on('click', function(){
    $('body').css('overflow', 'hidden');
    $('.cart-sidebar').addClass('active');
    $('.cart-close').on('click', function(){
        $('body').css('overflow', 'inherit');
        $('.cart-sidebar').removeClass('active');
        $('.backdrop').fadeOut();
    });
});


//========================================
//       BACKDROP SIDEBAR FUNCTION
//========================================
$('.header-user, .header-cart, .header-cate, .cart-btn, .cate-btn').on('click', function(){
    $('.backdrop').fadeIn();

    $('.backdrop').on('click', function(){
        $(this).fadeOut();
        $('body').css('overflow', 'inherit');
        $('.nav-sidebar').removeClass('active');
        $('.cart-sidebar').removeClass('active');
        $('.category-sidebar').removeClass('active');
    });
});


//========================================
//       COUPON FORM FUNCTION
//========================================
$('.coupon-btn').on('click', function(){
    $(this).hide();
    $('.coupon-form').css('display', 'flex');
});


//========================================
//       RESPONSIVE SEARCH BAR
//========================================
$('.header-src').on('click', function(){
    $('.header-form').toggleClass('active');
    $(this).children('.fa-search').toggleClass('fa-times');
});


//========================================
//       WISH ICON ACTIVE FUNCTION
//========================================
$('.wish').on('click', function(){
    $(this).toggleClass('active');
}); 


//========================================
//      ADD TO CART BUTTON FUNCTION
//========================================
$('.product-add').on('click', function(){
    var productAdd = $(this).next('.product-action');

    $(this).hide();
    productAdd.css('display', 'flex');
});


//========================================
//      INCREMENT PRODUCT QUANTITY
//========================================
$('.action-plus').on('click', function(){
    var increamentValue = $(this).closest('.product-action').children('.action-input').get(0).value++
    var actionMinus = $(this).closest('.product-action').children('.action-minus');

    if(increamentValue > 0) {
        actionMinus.removeAttr('disabled');
    }
});


//========================================
//      DECREMENT PRODUCT QUANTITY
//========================================
$('.action-minus').on('click', function(){
    var decrementValue = $(this).closest('.product-action').children('.action-input').get(0).value--

    if(decrementValue == 2) {
        $(this).attr('disabled', 'disabled');
    }
});


//========================================
//         REVIEW WIDGET BUTTON
//========================================
$('.review-widget-btn').on('click', function(){
    $(this).next('.review-widget-list').toggle();
});


//========================================
//          COUPON SELECT TEXT
//========================================
$('.offer-select').on('click', function(){
    $(this).text('Copied!');
});


//========================================
//        PRODUCT VIEW IMAGE SHOW
//========================================
$('.modal').on('shown.bs.modal', function (e) {
    $('.preview-slider, .thumb-slider').slick('setPosition', 0);
});


//========================================
//         PROFILE SCHEDULE ACTIVE
//========================================
$('.profile-card.schedule').on('click', function(){
    $('.profile-card.schedule').removeClass('active');
    $(this).addClass('active');
});


//========================================
//         PROFILE CONTACT ACTIVE
//========================================
$('.profile-card.contact').on('click', function(){
    $('.profile-card.contact').removeClass('active');
    $(this).addClass('active');
});


//========================================
//          PROFILE ADDESS ACTIVE
//========================================
$('.profile-card.address').on('click', function(){
    $('.profile-card.address').removeClass('active');
    $(this).addClass('active');
});


//========================================
//         PROFILE PAYMENT ACTIVE
//========================================
$('.payment-card.payment').on('click', function(){
    $('.payment-card.payment').removeClass('active');
    $(this).addClass('active');
});

// yadiel

// card numbers
var cardNumberElements = document.getElementsByClassName("card-number");
for (var i = 0; i < cardNumberElements.length; i++) {
    var cardNumberElement = cardNumberElements[i];
    var cardNumber = cardNumberElement.innerHTML;
    var lastFourDigits = cardNumber.substring(cardNumber.length - 4);
    cardNumberElement.innerHTML = "XXXX XXXX XXXX " + lastFourDigits;
}

//separete number in cellphone 
var phoneNumberElement = document.getElementById("phone");
if (phoneNumberElement) {
  var phoneNumber = phoneNumberElement.textContent;
  var formattedPhoneNumber = phoneNumber.replace(/(\d{3})(\d{3})(\d{4})/, "$1-$2-$3");
  phoneNumberElement.textContent = formattedPhoneNumber;
}


// show the card info in the edit pay ment
document.addEventListener('DOMContentLoaded', function() {
    var selectedCard = document.getElementById('selectedCard');
    var cardNameInput = document.getElementById('cardName');
    var cardTypeInput = document.getElementById('cardType');
    var expirationDateInput = document.getElementById('expirationDate');
    var card_id = document.getElementById('card_id');
  
    if (selectedCard && cardNameInput && cardTypeInput && expirationDateInput) {
      selectedCard.addEventListener('change', function() {
        var selectedCardValue = selectedCard.value.trim();
        var index = cardData.findIndex(function(card) {
          return card[3] == selectedCardValue;
        });
  
        if (index >= 0) {
          cardNameInput.value = cardData[index][1];
          cardTypeInput.value = cardData[index][2];
          expirationDateInput.value = cardData[index][5] + '-' + cardData[index][4];
          card_id.value = cardData[index][0];
        } else {
          cardNameInput.value = '';
          cardTypeInput.value = '';
          expirationDateInput.value = '';
          card_id.value = '';
        }
      });
    }
  });
  
// display account info in backend 
function populateFormFields(id) {
    // Find the data from the list based on the ID
    var foundUser = null;
    for (var i = 0; i < users.length; i++) {
        if (users[i].id === id) {
            foundUser = users[i];
            break;
        }
    }
    // Populate the form fields with the retrieved data
    if (foundUser) {
        document.getElementById('A_Name').value = foundUser.name;
        document.getElementById('A_LName').value = foundUser.Lname;
        document.getElementById('A_password').value = foundUser.pass;
        document.getElementById('A_Email').value = foundUser.Email;
        document.getElementById('A_phone').value = foundUser.phone;
        document.getElementById('A_status').value = foundUser.status; 
        document.getElementById('A_id').value = foundUser.id;
    } else {
        // Handle case when user is not found
        console.log("User not found.");
    }
}
