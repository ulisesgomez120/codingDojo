
$('#add').click(function() {
    $(this).addClass('white-text');
});
$('#hide').click(function(){
    $(this).siblings('h3').hide();
});
$('#hide-show').click(function(){
    $(this).siblings('h3').toggle();
});
$('#show').click(function(){
    $(this).siblings('h3').show();
});
$('#slide-up').click(function(){
    $(this).siblings('h3').slideUp();
});
$('#up-down').click(function(){
    $(this).siblings('h3').slideToggle();
});
$('#slide-down').click(function(){
    $(this).siblings('h3').slideDown();
});
$('#fade-out').click(function(){
    $(this).siblings('h3').fadeOut();
});
$('#fade-in').click(function(){
    $(this).siblings('h3').fadeIn();
});

$('#before').click(function(){
    $(this).before("<p>I come before</p>")
});
$('#after').click(function(){
    $(this).after("<p>I come after</p>")
});
$('#append').click(function(){
    $(this).append("<p>I've been added!</p>")
});
$('#html').click(function(){
    $(this).html("<h2>I'm an h2 now</h2>")
});
$('#link').click(function(){
    $('a').attr("href", "https://www.codingdojo.com/");
});

function displayVals () {
    var select = $('select').val();

    $('#display-val').text(select);
}
$("select").change(displayVals);
displayVals();
