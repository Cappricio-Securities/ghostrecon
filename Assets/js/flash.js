$( document ).ready(function() {
  $(".flash").addClass("animate--drop-in-fade-out");
  setTimeout(function () {
    $(".flash").removeClass("animate--drop-in-fade-out");
  }, 3500);
});


/*
$(".button").click(function () {
  $(".flash").addClass("animate--drop-in-fade-out");
  setTimeout(function () {
    $(".flash").removeClass("animate--drop-in-fade-out");
  }, 3500);
});
*/